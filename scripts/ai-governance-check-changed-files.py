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

PATH_RULES = [
    (
        re.compile(r"(^|/)(\.mcp\.json|mcp\.json|mcp[_-]?servers?|mcp)(/|\.|$)", re.I),
        "05-technical-controls",
        "MCP server configuration or integration",
    ),
    (
        re.compile(r"(^|/)(agents?|sub[_-]?agents?|orchestrat\w*|crews?|swarms?)(/|\.|$)", re.I),
        "03-architecture-and-bounding",
        "agent or orchestration code",
    ),
    (
        re.compile(r"(^|/)(tools|toolkits?|actions|skills|plugins)(/|\.|$)", re.I),
        "05-technical-controls",
        "agent tool or action definitions",
    ),
    (
        re.compile(r"(^|/)(prompts?|system[_-]?prompts?|instructions)(/|\.|$)", re.I),
        "08-monitoring-and-operations",
        "agent instructions (a change-review trigger)",
    ),
    (
        re.compile(r"(^|/)(guardrails?|policies|policy|approvals?|hitl)(/|\.|$)", re.I),
        "06-human-oversight",
        "guardrail, policy, or approval logic",
    ),
    (
        re.compile(r"(^|/)(evals?|evaluations?|red[_-]?team\w*|benchmarks?)(/|\.|$)", re.I),
        "07-testing-and-evaluation",
        "agent evaluation or red-team suite",
    ),
    (
        re.compile(r"(^|/)(memory|memories|vector[_-]?store|embeddings?)(/|\.|$)", re.I),
        "03-architecture-and-bounding",
        "agent memory or retrieval store",
    ),
]

CONTENT_RULES = [
    (
        re.compile(
            r"\b("
            # Agent frameworks and SDKs. Matched as words after identifier
            # splitting, so `from langgraph.graph import` and `LangGraph` both hit.
            r"langgraph|langchain|crewai|autogen|semantic kernel|llama ?index|"
            r"agents sdk|agent sdk|claude agent sdk|openai agents|strands agents|"
            r"bedrock agent\w*|vertex ai agent\w*|agentcore|"
            # Protocols. The camelCase split turns `A2A` into `A2 A`, hence the
            # optional space.
            r"mcp server|model context protocol|mcp client|a2 ?a|agent2 ?agent|"
            r"agentic commerce|"
            # Tool-use surface.
            r"tool use|tool call\w*|function call\w*|tool choice|bind tools|"
            r"computer use|browser use|"
            # Autonomy and loop control.
            r"max iterations|max steps|max turns|recursion limit|"
            r"system prompt|"
            # Oversight and guardrails.
            r"human in the loop|hitl|requires approval|approval required|"
            r"interrupt before|interrupt after|guardrails?|kill switch|"
            # Identity and delegation.
            r"on behalf of|agent id|agent identity|token exchange"
            r")\b",
            re.I,
        ),
        "agentic-AI keyword",
    )
]

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


def changed_files(args: argparse.Namespace) -> list[Path]:
    if args.base or args.head:
        if not (args.base and args.head):
            raise SystemExit("--base and --head must be supplied together")
        output = run_git(["diff", "--name-only", f"{args.base}...{args.head}"])
    elif args.staged:
        output = run_git(["diff", "--cached", "--name-only"])
    else:
        output = run_git(["diff", "--name-only"])

    return [Path(line) for line in output.splitlines() if line.strip()]


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


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return ""


def classify(root: Path, rel_path: Path) -> list[tuple[str, str]]:
    rel = rel_path.as_posix()
    findings: list[tuple[str, str]] = []

    for pattern, layer, reason in PATH_RULES:
        if pattern.search(rel):
            findings.append((layer, reason))

    full_path = root / rel_path
    if full_path.is_file() and full_path.stat().st_size <= 500_000:
        text = split_identifiers(read_text(full_path))
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
    args = parser.parse_args()

    root = repo_root()
    config = load_config(root, args.config)
    frameworks = frameworks_from(config)
    tier = tier_from(config)
    policy = policy_from(args, config)

    flagged = []
    for rel_path in changed_files(args):
        findings = classify(root, rel_path)
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
        print("[ai-gov-check] Blocking because reviewPolicy is block-on-sensitive-change.")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
