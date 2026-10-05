#!/usr/bin/env python3
"""Tests for scripts/ai-governance-check-changed-files.py.

Runnable either with pytest or directly: `python3 tests/test_ai_governance_check.py`.
The script name contains dashes, so it is loaded by path rather than imported.
"""

from __future__ import annotations

import importlib.util
import json
import os
import subprocess
import tempfile
from pathlib import Path


def _load():
    path = (Path(__file__).resolve().parent.parent / "scripts"
            / "ai-governance-check-changed-files.py")
    spec = importlib.util.spec_from_file_location("ai_gov_check", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


gov = _load()
KEYWORDS = gov.CONTENT_RULES[0][0]


def _matches(text: str) -> bool:
    return bool(KEYWORDS.search(gov.split_identifiers(text)))


def _expect_exit(fn):
    try:
        fn()
    except SystemExit:
        return
    raise AssertionError("expected SystemExit")


# --- content scan -----------------------------------------------------------

def test_framework_imports_are_detected():
    for line in ("from langgraph.graph import StateGraph",
                 "import crewai",
                 "from langchain_core.tools import tool",
                 "from claude_agent_sdk import query",
                 "from autogen import AssistantAgent"):
        assert _matches(line), line


def test_identifier_spellings_are_detected():
    for name in ("system_prompt", "systemPrompt", "system-prompt",
                 "max_iterations", "maxIterations", "recursion_limit",
                 "human_in_the_loop", "humanInTheLoop", "requires_approval",
                 "tool_calls", "toolCalls", "computer_use",
                 "interrupt_before", "kill_switch", "agentId"):
        assert _matches(name), name


def test_protocol_terms_are_detected():
    for text in ("register the MCP server", "mcp_server", "Model Context Protocol",
                 "Agent2Agent"):
        assert _matches(text), text


def test_newer_agent_sdks_are_detected():
    for line in ("from agents import Agent, Runner",
                 "from pydantic_ai import Agent",
                 "from google.adk.agents import LlmAgent",
                 "import smolagents"):
        assert _matches(line), line


def test_model_identifiers_are_detected():
    # A one-line model swap is a material change (MGF 2.3.3) and must be flagged.
    for line in ('MODEL_NAME = "claude-sonnet-4-5"', 'model="gpt-4o"',
                 'model: "gemini-2.5-pro"', "o3-mini", "claude-opus-5"):
        assert _content_reasons(line), line


def test_ordinary_code_is_not_flagged():
    # `agent` alone would match user_agent, and `tool`/`policy` alone would match
    # half of any codebase. None of these should trip the scanner.
    for text in ("user_agent = request.headers['User-Agent']",
                 "def calculate_total(items): return sum(items)",
                 "build tooling for the docs site",
                 "cache_policy = 'no-store'",
                 "functional programming",
                 "# this function calls the payment API",
                 "performed on behalf of the licensor",
                 "OAuth token exchange endpoint",
                 "sha512-a2A9xQ==",
                 "model_name = 'Invoice'"):
        assert not _content_reasons(text), text


# --- path rules -------------------------------------------------------------

def _content_reasons(text: str) -> list[str]:
    return [reason for layer, reason in gov.classify(Path("src/x.py"), text)
            if layer == "content-scan"]


def _path_layers(rel: str) -> list[str]:
    return [layer for layer, _ in gov.classify(Path(rel), "")]


def test_agent_paths_are_classified():
    assert "03-architecture-and-bounding" in _path_layers("src/agents/billing.py")
    assert "03-architecture-and-bounding" in _path_layers("src/agent_tools/refund.ts")
    assert "05-technical-controls" in _path_layers(".mcp.json")
    assert "06-human-oversight" in _path_layers("app/approvals/queue.py")
    assert "07-testing-and-evaluation" in _path_layers("evals/policy_compliance.yaml")
    assert "08-monitoring-and-operations" in _path_layers("prompts/support.md")


def test_unrelated_paths_are_not_classified():
    for rel in ("src/billing/invoice.py", "README.md", "web/styles/main.css",
                "src/user_agent_parser.py", ".github/actions/setup/action.yml",
                "src/store/actions/cart.ts", "tools/build.sh", "webpack/plugins/x.js",
                "infra/iam/policies/read.json", "docs/privacy/policy.md",
                "benchmarks/latency.py"):
        assert _path_layers(rel) == [], rel


def test_lockfiles_and_licences_are_skipped():
    for rel in ("package-lock.json", "web/yarn.lock", "uv.lock", "LICENSE", "LICENSE.md"):
        assert gov.classify(Path(rel), "langgraph guardrails claude-sonnet-4-5") == [], rel


def test_content_scan_uses_added_text():
    findings = gov.classify(Path("svc.py"), "graph.interrupt_before = ['pay']")
    assert ("content-scan", "agentic-AI keyword") in findings


# --- diff parsing and acknowledgement --------------------------------------

def _git(cwd: Path, *args: str) -> str:
    return subprocess.run(["git", *args], cwd=cwd, check=True, capture_output=True,
                          text=True).stdout


def _repo(tmp: Path) -> None:
    _git(tmp, "init", "-q")
    _git(tmp, "config", "user.email", "t@example.com")
    _git(tmp, "config", "user.name", "t")
    (tmp / "svc.py").write_text("# uses guardrails\nprint(1)\n")
    _git(tmp, "add", ".")
    _git(tmp, "commit", "-qm", "init")


class _Args:
    base = None
    head = None
    staged = True


def test_only_added_lines_are_scanned():
    # The file already mentions guardrails; an unrelated edit must not be flagged.
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        _repo(root)
        (root / "svc.py").write_text("# uses guardrails\nprint(2)\n")
        _git(root, "add", ".")
        cwd = os.getcwd()
        os.chdir(root)
        try:
            added = gov.added_lines_by_file(_Args)
        finally:
            os.chdir(cwd)
        assert added == {Path("svc.py"): "print(2)"}, added
        assert gov.classify(Path("svc.py"), added[Path("svc.py")]) == []


def test_ack_trailer_lifts_block():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        _repo(root)
        base = _git(root, "rev-parse", "HEAD").strip()
        (root / "svc.py").write_text("model = 'gpt-4o'\n")
        _git(root, "commit", "-qam", "Swap model\n\nAI-Governance-Reviewed: yes")

        class Args:
            pass

        Args.base, Args.head, Args.staged = base, "HEAD", False
        cwd = os.getcwd()
        os.chdir(root)
        try:
            assert gov.acknowledged(Args, gov.DEFAULT_ACK_TRAILER)
            assert not gov.acknowledged(Args, "Something-Else: yes")
        finally:
            os.chdir(cwd)


# --- config -----------------------------------------------------------------

def _config(tmp: Path, body: dict) -> dict:
    (tmp / ".ai-governance.json").write_text(json.dumps(body))
    return gov.load_config(tmp, ".ai-governance.json")


def test_missing_config_defaults_to_warn_and_unassessed():
    with tempfile.TemporaryDirectory() as tmp:
        config = gov.load_config(Path(tmp), ".ai-governance.json")
        assert gov.frameworks_from(config) == []
        assert gov.tier_from(config) == "unassessed"

        class Args:
            review_policy = None

        assert gov.policy_from(Args, config) == "warn"


def test_valid_config_is_accepted():
    with tempfile.TemporaryDirectory() as tmp:
        config = _config(Path(tmp), {"aiGovernance": {
            "frameworks": ["sg-mgf-agentic"], "riskTier": "high",
            "reviewPolicy": "block-on-sensitive-change"}})
        assert gov.frameworks_from(config) == ["sg-mgf-agentic"]
        assert gov.tier_from(config) == "high"


def test_unknown_framework_is_rejected():
    with tempfile.TemporaryDirectory() as tmp:
        config = _config(Path(tmp), {"aiGovernance": {"frameworks": ["sg-mgf-agentc"]}})
        _expect_exit(lambda: gov.frameworks_from(config))


def test_unknown_tier_is_rejected():
    with tempfile.TemporaryDirectory() as tmp:
        config = _config(Path(tmp), {"aiGovernance": {"riskTier": "critical"}})
        _expect_exit(lambda: gov.tier_from(config))


def test_invalid_json_is_rejected():
    with tempfile.TemporaryDirectory() as tmp:
        (Path(tmp) / ".ai-governance.json").write_text("{not json")
        _expect_exit(lambda: gov.load_config(Path(tmp), ".ai-governance.json"))


def test_example_config_is_valid():
    root = Path(__file__).resolve().parent.parent
    config = gov.load_config(root, ".ai-governance.example.json")
    assert gov.frameworks_from(config)
    gov.tier_from(config)


if __name__ == "__main__":
    passed = 0
    for name, fn in sorted(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()
            passed += 1
            print(f"  PASS {name}")
    print(f"\n{passed} passed")
