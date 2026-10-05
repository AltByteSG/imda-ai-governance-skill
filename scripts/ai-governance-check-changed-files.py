#!/usr/bin/env python3
"""Flag changed files that probably need an agentic-AI governance review.

This is a deterministic tripwire, not a compliance decision engine and not
regulatory advice. It detects likely agentic-AI touchpoints (agent code, tool
and MCP definitions, prompts, approval and guardrail logic, evals) and points
the developer back to the imda-ai-governance skill.

Requires Python 3.9+ (PEP 585 builtin generics in annotations).
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from pathlib import Path

DEFAULT_CONFIG = ".ai-governance.json"
VALID_POLICIES = {"warn", "block-on-sensitive-change"}
VALID_FRAMEWORKS = {"sg-mgf-agentic"}
VALID_TIERS = {"unassessed", "low", "medium", "high"}
GIT_TIMEOUT_SECONDS = 30

# Path rules name folders that are agent-specific on their own. Generic names
# (tools/, actions/, plugins/, policies/, benchmarks/) are deliberately absent:
# they match build tooling, CI actions, Redux, IAM and docs far more often than
# agents. Agent code in such folders is still caught by the content scan.
PATH_RULES = [
    (
        re.compile(r"(^|/)(\.mcp\.json|mcp\.json|mcp[_-]?servers?|mcp)(/|\.|$)", re.I),
        "05-technical-controls",
        "MCP server configuration or integration",
    ),
    (
        re.compile(r"(^|/)(agents?|sub[_-]?agents?|agent[_-]?tools|orchestrat\w*|crews?|swarms?)"
                   r"(/|\.|$)", re.I),
        "03-architecture-and-bounding",
        "agent or orchestration code",
    ),
    (
        re.compile(r"(^|/)(prompts?|system[_-]?prompts?)(/|\.|$)", re.I),
        "08-monitoring-and-operations",
        "agent instructions (a change-review trigger)",
    ),
    (
        re.compile(r"(^|/)(guardrails?|approvals?|hitl)(/|\.|$)", re.I),
        "06-human-oversight",
        "guardrail or approval logic",
    ),
    (
        re.compile(r"(^|/)(evals?|red[_-]?team\w*)(/|\.|$)", re.I),
        "07-testing-and-evaluation",
        "agent evaluation or red-team suite",
    ),
]

CONTENT_RULES = [
    (
        re.compile(
            r"\b("
            # Agent frameworks and SDKs. Matched as words after identifier
            # splitting, so `from langgraph.graph import` and `LangGraph` both hit.
            r"langgraph|langchain|crewai|autogen|semantic kernel|llama ?index|"
            r"pydantic ai|google adk|smolagents|from agents import|"
            r"agents sdk|agent sdk|claude agent sdk|openai agents|strands agents|"
            r"bedrock agent\w*|vertex ai agent\w*|agentcore|"
            # Protocols. The camelCase split turns `Agent2Agent` into
            # `Agent2 Agent`, hence the optional space.
            r"mcp server|model context protocol|mcp client|agent2 ?agent|"
            r"agentic commerce|"
            # Tool-use surface.
            r"tool use|tool calls?|tool choice|bind tools|computer use|browser use|"
            # Autonomy and loop control.
            r"max iterations|max steps|max turns|recursion limit|system prompt|"
            # Oversight and guardrails.
            r"human in the loop|hitl|requires approval|approval required|"
            r"interrupt before|interrupt after|guardrails?|kill switch|"
            # Identity.
            r"agent id|agent identity"
            r")\b",
            re.I,
        ),
        "agentic-AI keyword",
    ),
    (
        # Model identifiers. A one-line model swap is a material change under
        # MGF §2.3.3, so it must trip the check even with nothing else around it.
        # After identifier splitting `claude-sonnet-4-5` reads `claude sonnet 4 5`
        # and `gemini-2.5-pro` reads `gemini 2 5 pro`.
        re.compile(
            r"\b(claude (opus|sonnet|haiku|fable|instant|\d)|gpt \d\w*|o[134] (mini|pro)|"
            r"gemini \d|gemini (pro|flash|ultra)|llama \d|mistral (large|medium|small)|"
            r"command r\w*|deepseek (v|r)\d)\b",
            re.I,
        ),
        "model identifier (a model change is a change-review trigger)",
    ),
]

# Generated or legal files whose content says nothing about agent behaviour but
# routinely contains matching byte sequences (base64 hashes in lockfiles, "on
# behalf of" in licences).
SKIP_FILES = re.compile(
    r"(^|/)(package-lock\.json|npm-shrinkwrap\.json|yarn\.lock|pnpm-lock\.yaml|"
    r"poetry\.lock|uv\.lock|Pipfile\.lock|Cargo\.lock|Gemfile\.lock|go\.sum|composer\.lock|"
    r"LICEN[CS]E[^/]*|COPYING[^/]*|NOTICE[^/]*)$",
    re.I,
)

DEFAULT_ACK_TRAILER = "AI-Governance-Reviewed: yes"

# `_` is a word character and `-` sits flush against one, so `\bsystem prompt\b`
# would never match `system_prompt`, `systemPrompt`, or `system-prompt`. Splitting
# identifiers once is cheaper and less error-prone than encoding every separator
# variant into every keyword. Dots are split too so module paths like
# `langgraph.prebuilt` still match on the package name.
_ACRONYM_BOUNDARY = re.compile(r"([A-Z]+)([A-Z][a-z])")
_CAMEL_BOUNDARY = re.compile(r"([a-z0-9])([A-Z])")
_WORD_SEPARATORS = re.compile(r"[_\-.]+")


def split_identifiers(text: str) -> str:
    """Split snake_case, kebab-case, dotted and camelCase names so `\\b` matches."""
    text = _ACRONYM_BOUNDARY.sub(r"\1 \2", text)
    text = _CAMEL_BOUNDARY.sub(r"\1 \2", text)
    return _WORD_SEPARATORS.sub(" ", text)


def run_git(args: list[str]) -> str:
    command = "git " + " ".join(args)
    try:
        result = subprocess.run(
            ["git", *args],
            check=False,
            capture_output=True,
            text=True,
            timeout=GIT_TIMEOUT_SECONDS,
        )
    except subprocess.TimeoutExpired:
        raise SystemExit(
            f"{command} timed out after {GIT_TIMEOUT_SECONDS}s"
        ) from None
    if result.returncode != 0:
        raise SystemExit(
            f"{command} failed: {result.stderr.strip() or 'no stderr output'}"
        )
    return result.stdout


def repo_root() -> Path:
    return Path(run_git(["rev-parse", "--show-toplevel"]).strip())


def diff_args(args: argparse.Namespace) -> list[str]:
    if args.base or args.head:
        if not (args.base and args.head):
            raise SystemExit("--base and --head must be supplied together")
        return [f"{args.base}...{args.head}"]
    if args.staged:
        return ["--cached"]
    return []


def added_lines_by_file(args: argparse.Namespace) -> dict[Path, str]:
    """Map each changed path to the text of its added lines only.

    Scanning whole files meant that once a file mentioned "guardrails", every
    later edit to it was flagged. Reading the zero-context diff limits the content
    scan to what this change introduced, and for --staged it reads the staged
    version rather than the working tree. Deleted files map to empty text.
    """
    output = run_git(["diff", "-U0", "--no-color", "--no-ext-diff", *diff_args(args)])
    files: dict[Path, list[str]] = {}
    current: list[str] | None = None
    for line in output.splitlines():
        if line.startswith("diff --git "):
            current = None
        elif line.startswith("+++ "):
            target = line[4:]
            if target == "/dev/null":
                current = None
            else:
                path = Path(target[2:] if target.startswith("b/") else target)
                current = files.setdefault(path, [])
        elif line.startswith("--- a/"):
            # Keep deletions visible to the path rules even with no added text.
            files.setdefault(Path(line[6:]), [])
        elif current is not None and line.startswith("+"):
            current.append(line[1:])
    return {path: "\n".join(lines) for path, lines in files.items()}


def acknowledged(args: argparse.Namespace, trailer: str) -> bool:
    """True if any commit in base...head carries the review acknowledgement trailer."""
    if not (args.base and args.head):
        return False
    log = run_git(["log", "--format=%B", f"{args.base}..{args.head}"])
    wanted = trailer.lower()
    return any(line.strip().lower() == wanted for line in log.splitlines())


def load_config(root: Path, config_path: str) -> dict:
    path = Path(config_path)
    if not path.is_absolute():
        path = root / path
    if not path.exists():
        return {"aiGovernance": {"frameworks": [], "reviewPolicy": "warn"}}
    try:
        with path.open("r", encoding="utf-8") as handle:
            return json.load(handle)
    except json.JSONDecodeError as exc:
        raise SystemExit(f"{path}: invalid JSON ({exc})") from None
    except OSError as exc:
        raise SystemExit(f"{path}: cannot read config ({exc})") from None


def section(config: dict) -> dict:
    value = config.get("aiGovernance", {})
    if not isinstance(value, dict):
        raise SystemExit("aiGovernance must be an object")
    return value


def policy_from(args: argparse.Namespace, config: dict) -> str:
    policy = args.review_policy or section(config).get("reviewPolicy", "warn")
    if policy not in VALID_POLICIES:
        raise SystemExit(
            f"Unsupported review policy {policy!r}; expected one of: "
            f"{', '.join(sorted(VALID_POLICIES))}"
        )
    return policy


def frameworks_from(config: dict) -> list[str]:
    configured = section(config).get("frameworks", [])
    if not isinstance(configured, list):
        raise SystemExit("aiGovernance.frameworks must be a list")
    unknown = [code for code in configured if code not in VALID_FRAMEWORKS]
    if unknown:
        raise SystemExit(
            f"Unknown framework code(s): {', '.join(sorted(unknown))}; "
            f"expected one of: {', '.join(sorted(VALID_FRAMEWORKS))}"
        )
    return configured


def tier_from(config: dict) -> str:
    tier = section(config).get("riskTier", "unassessed")
    if tier not in VALID_TIERS:
        raise SystemExit(
            f"Unsupported riskTier {tier!r}; expected one of: "
            f"{', '.join(sorted(VALID_TIERS))}"
        )
    return tier


def classify(rel_path: Path, added_text: str) -> list[tuple[str, str]]:
    rel = rel_path.as_posix()
    if SKIP_FILES.search(rel):
        return []

    findings: list[tuple[str, str]] = []
    for pattern, layer, reason in PATH_RULES:
        if pattern.search(rel):
            findings.append((layer, reason))

    if added_text and len(added_text) <= 500_000:
        text = split_identifiers(added_text)
        for pattern, reason in CONTENT_RULES:
            if pattern.search(text):
                findings.append(("content-scan", reason))

    return list(dict.fromkeys(findings))


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Flag changed files that probably need an agentic-AI governance review."
    )
    parser.add_argument("--config", default=DEFAULT_CONFIG)
    parser.add_argument("--staged", action="store_true")
    parser.add_argument("--base")
    parser.add_argument("--head")
    parser.add_argument(
        "--review-policy",
        choices=sorted(VALID_POLICIES),
        help="Override .ai-governance.json reviewPolicy.",
    )
    parser.add_argument(
        "--ack-trailer",
        default=DEFAULT_ACK_TRAILER,
        help="Commit trailer in base...head that acknowledges a governance review "
             f"and lifts a block (default: {DEFAULT_ACK_TRAILER!r}).",
    )
    args = parser.parse_args()

    root = repo_root()
    config = load_config(root, args.config)
    frameworks = frameworks_from(config)
    tier = tier_from(config)
    policy = policy_from(args, config)

    flagged = []
    for rel_path, added_text in added_lines_by_file(args).items():
        findings = classify(rel_path, added_text)
        if findings:
            flagged.append((rel_path, findings))

    if not flagged:
        print("[ai-gov-check] No agentic-AI changes detected.")
        return 0

    framework_text = ", ".join(frameworks) if frameworks else "not configured"
    print("[ai-gov-check] Agentic-AI changes detected.")
    print(f"[ai-gov-check] Frameworks: {framework_text}; risk tier: {tier}; policy: {policy}")
    print(
        "[ai-gov-check] Ask your coding agent to review these changes with the "
        "imda-ai-governance skill (checklists/change-review.md)."
    )

    for rel_path, findings in flagged:
        reasons = "; ".join(f"{layer}: {reason}" for layer, reason in findings)
        print(f"  - {rel_path.as_posix()} ({reasons})")

    if not frameworks:
        print("[ai-gov-check] No .ai-governance.json frameworks configured yet.")
        print("[ai-gov-check] Set up the project config before relying on this guardrail.")
    if tier == "unassessed":
        print("[ai-gov-check] Risk tier is unassessed; run checklists/new-agent.md section 1.")

    if policy == "block-on-sensitive-change":
        if acknowledged(args, args.ack_trailer):
            print(f"[ai-gov-check] Review acknowledged by commit trailer {args.ack_trailer!r}.")
            return 0
        print("[ai-gov-check] Blocking because reviewPolicy is block-on-sensitive-change.")
        print(f"[ai-gov-check] After the review, add the trailer {args.ack_trailer!r} to a commit.")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
