# Changelog

All notable changes to this skill are documented here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and the project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

Each release records the framework version reflected in the content. When IMDA publishes a new version of the framework, a new minor release is cut. Pin to a specific tag in a submodule if you want to control upgrade timing.

## Unreleased

— No unreleased changes.

## [0.3.0] — 2026-10-05

Adds IMDA's **Model AI Governance Framework for Generative AI** (IMDA / AI Verify Foundation, final version announced 30 May 2024) as a **supplement** to the agentic framework, and applies the fixes from the first end-to-end test of the skill. The agentic framework (v1.5) remains the primary bar and its content is unchanged.

### Added — generative-AI supplement (`sg-mgf-genai`)

- [`frameworks/sg-mgf-genai/`](skills/imda-ai-governance/frameworks/sg-mgf-genai/README.md): framework notes for all nine dimensions and a reverse-lookup map. Each expectation is written as what lands on the build and the evidence a reviewer should ask for. Recommendations aimed at policymakers or the wider ecosystem are noted in one line with any engineering hook. The framework has no section numbers, so it is cited as `[MGF-GenAI <dimension>, p.N]`. Page references come from an extracted copy of the PDF and are due a spot-check against the original.
- [`layers/10-data-and-grounding.md`](skills/imda-ai-governance/layers/10-data-and-grounding.md): training, fine-tuning, RAG and evaluation data — provenance and licence, personal data, quality, deletion reaching every index, poisoning.
- Additions to layers 01 (model-provider terms and shared responsibility), 02 (model-level threats), 05 (GenAI baseline safety, model supply chain), 07 (benchmarks, evaluation dimensions, external assurance), 08 (outside vulnerability reporting, external incident thresholds, forensic retention, compute tracking) and 09 (labelling and provenance of generated content).
- [`templates/SYSTEM_CARD.md.template`](skills/imda-ai-governance/templates/SYSTEM_CARD.md.template): the framework's disclosure "food label", for teams deploying models they may not have trained. Agent cards link to it.
- Checklists [`new-genai-feature.md`](skills/imda-ai-governance/checklists/new-genai-feature.md) (generative features that take no actions; redirects to `new-agent.md` if the feature is agentic) and [`new-dataset-or-corpus.md`](skills/imda-ai-governance/checklists/new-dataset-or-corpus.md).
- Design review gains a short generative-AI supplement (items G.0–G.9) and a scorecard row. For generative systems that take no actions, the supplement plus the `new-genai-feature.md` items (cited as NG n.n) are the bar, with generative-specific High triggers in the severity rubric. Pre-deployment, change-review, third-party and incident checklists gain the matching items.
- `.ai-governance.json` accepts `sg-mgf-genai`. Agents list it after `sg-mgf-agentic`; generative features without actions list it alone.

### Changed — from the end-to-end test

A blind review of a sample agent with 13 seeded gaps found all 13 with correct references; a control review of a well-built version found no High issues but was too long. Fixes:

- **Reviews without the author present.** Step 1 now says to infer role and tier, mark them provisional, and carry on, instead of stopping to ask. The clash between "run `new-agent.md` first" and design-review's provisional tier is resolved: designing runs `new-agent.md`; reviewing sets a provisional tier.
- **Skill version is stated in SKILL.md and AGENTS.md**, so reviews can record it. The release check now fails if either disagrees with the manifests.
- **Severity rubric.** Missing pre-deployment testing or logging on a medium- or high-tier system, and approvals that fail open, are now High. A "conditional" severity covers gaps that depend on material the reviewer couldn't see. Doc-versus-code mismatches are scored by the worse of the two.
- **Numbered checklist items** in design review (1.1–4.6, S.1–S.5, G.0–G.9), used by the review template's findings and appendix.
- **Citations fixed.** System-level approval enforcement now cites `[MGF §2.3.1]`; the bias item cites `[MGF §1.2.2, §2.3.2]`; conflicting objectives cites `[MGF §1.2.3]`. A new item S.5 covers speed and volume for every agent, not only multi-agent systems.
- **Shorter reviews.** Merge findings that share a root cause; more than five Low findings collapse into one "Minor gaps" list.
- **Disagreeing with an assessed tier.** Keep the team's tier, state yours beside it with the reason, and raise it as a finding.

### Changed — changed-file tripwire

- Detects agent loops hand-rolled on model SDKs (`anthropic`, `openai` imports, `messages.create`, `chat.completions`, `responses.create`, function calling). The test missed these when no model identifier was in the diff.
- Detects approval logic by identifier (`require_human_approval`, `auto_approve`, `approval_timeout`, human review queues).
- New path rule and keywords for training, fine-tuning, RAG and vector-store data, output and content filters, watermarking and C2PA.
- The Claude Code nudge hook covers the same data paths.

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
