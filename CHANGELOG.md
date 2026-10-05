# Changelog

All notable changes to this skill are documented here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and the project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

Each release records the framework version reflected in the content. When IMDA publishes a new version of the framework, a new minor release is cut. Pin to a specific tag in a submodule if you want to control upgrade timing.

## Unreleased

— No unreleased changes.

## [0.2.0] — 2026-10-05

Framework content is unchanged from 0.1.0 and still reflects the **Model AI Governance Framework for Agentic AI, version 1.5**.

### Changed — marketplace renamed to match the repo

The marketplace in [`.claude-plugin/marketplace.json`](.claude-plugin/marketplace.json) is now `imda-ai-governance-skill` instead of `altbyte-plugins`. The old name was shared with the `personal-data-protection-skill` repo, so the two marketplaces could not be added side by side. Install with:

```bash
claude plugin marketplace add AltByteSG/imda-ai-governance-skill
claude plugin install imda-ai-governance@imda-ai-governance-skill
```

If you installed from `main` before this change, switch once:

```bash
claude plugin uninstall imda-ai-governance@altbyte-plugins
claude plugin marketplace remove altbyte-plugins
claude plugin marketplace add AltByteSG/imda-ai-governance-skill
claude plugin install imda-ai-governance@imda-ai-governance-skill
```

## [0.1.0] — 2026-10-05

First release. Written against the **Model AI Governance Framework for Agentic AI, version 1.5** (IMDA, published 20 May 2026, updated 5 June 2026). Structure and packaging follow the sibling [`personal-data-protection-skill`](https://github.com/AltByteSG/personal-data-protection-skill): a layered skill, a framework folder in place of jurisdiction folders, entry-point checklists, templates, dual Claude Code / Codex manifests, and `AGENTS.md` routing.

### Added — skill content

- [`SKILL.md`](skills/imda-ai-governance/SKILL.md) and the mirrored [`AGENTS.md`](AGENTS.md): scope and project config (`.ai-governance.json`), entry points, and the ten load-bearing principles with section references.
- **Nine layer files** under [`layers/`](skills/imda-ai-governance/layers/), organised by where an expectation lands: accountability, use case and risk, architecture and bounding, identity and authorisation, technical controls, human oversight, testing and evaluation, monitoring and operations, end-user transparency.
- **Framework notes** under [`frameworks/sg-mgf-agentic/`](skills/imda-ai-governance/frameworks/sg-mgf-agentic/): version metadata and what v1.5 changed; one file per dimension plus foundations, each expectation paired with the evidence a reviewer should ask for; a section-to-layer map; and engineering takeaways from the framework's case studies.
- **Seven checklists**: alignment review of an existing design or system, new agent, new tool or integration (including MCP and computer use), third-party agent, pre-deployment release gate, change review, and agent incident.
- **Templates**: `AGENT_CARD.md` (per-agent governance record), `ALIGNMENT_REVIEW.md` (review report), and a Claude Code PostToolUse nudge hook.

### Added — conventions

- `[MGF §x.y]` marks what the framework says; `[Practice]` marks what the skill recommends to meet it. The framework is voluntary and mostly phrased as what organisations "should consider"; reviews written with the skill are instructed not to present `[Practice]` items as IMDA requirements.
- A three-tier risk model (low / medium / high) set by the agent's highest-impact action. The framework prescribes no tiers; this is labelled as the skill's own heuristic, drawn from the framework's case studies.

### Added — tooling

- [`scripts/ai-governance-check-changed-files.py`](scripts/ai-governance-check-changed-files.py): deterministic changed-file tripwire for pre-commit and CI, with tests. Scans only added lines; flags agent and orchestration code, MCP config, prompts, approval and guardrail logic, evals, agent-framework and oversight keywords, and model identifiers (a model swap is a change-review trigger); skips lockfiles and licences; validates `.ai-governance.json`; in block mode, a `AI-Governance-Reviewed: yes` commit trailer lifts the block.
- Release workflow and `scripts/release_notes.py`, carried over from the sibling skill.
