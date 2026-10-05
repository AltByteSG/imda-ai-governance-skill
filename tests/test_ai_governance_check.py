#!/usr/bin/env python3
"""Tests for scripts/ai-governance-check-changed-files.py.

Runnable either with pytest or directly: `python3 tests/test_ai_governance_check.py`.
The script name contains dashes, so it is loaded by path rather than imported.
"""

from __future__ import annotations

import importlib.util
import json
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
                 "tool_calls", "toolCalls", "function_call", "computer_use",
                 "interrupt_before", "kill_switch", "on_behalf_of", "agentId"):
        assert _matches(name), name


def test_protocol_terms_are_detected():
    for text in ("register the MCP server", "mcp_server", "Model Context Protocol",
                 "an A2A handoff", "Agent2Agent"):
        assert _matches(text), text


def test_ordinary_code_is_not_flagged():
    # `agent` alone would match user_agent, and `tool`/`policy` alone would match
    # half of any codebase. None of these should trip the scanner.
    for text in ("user_agent = request.headers['User-Agent']",
                 "def calculate_total(items): return sum(items)",
                 "build tooling for the docs site",
                 "cache_policy = 'no-store'",
                 "functional programming"):
        assert not _matches(text), text


# --- path rules -------------------------------------------------------------

def _path_layers(rel: str) -> list[str]:
    with tempfile.TemporaryDirectory() as tmp:
        return [layer for layer, _ in gov.classify(Path(tmp), Path(rel))]


def test_agent_paths_are_classified():
    assert "03-architecture-and-bounding" in _path_layers("src/agents/billing.py")
    assert "05-technical-controls" in _path_layers("src/tools/refund.ts")
    assert "05-technical-controls" in _path_layers(".mcp.json")
    assert "06-human-oversight" in _path_layers("app/approvals/queue.py")
    assert "07-testing-and-evaluation" in _path_layers("evals/policy_compliance.yaml")
    assert "08-monitoring-and-operations" in _path_layers("prompts/support.md")


def test_unrelated_paths_are_not_classified():
    for rel in ("src/billing/invoice.py", "README.md", "web/styles/main.css",
                "src/user_agent_parser.py"):
        assert _path_layers(rel) == [], rel


def test_content_scan_reads_file():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        (root / "svc.py").write_text("graph = StateGraph(); graph.interrupt_before = ['pay']")
        assert ("content-scan", "agentic-AI keyword") in gov.classify(root, Path("svc.py"))


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
