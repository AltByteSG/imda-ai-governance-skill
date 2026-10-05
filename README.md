# imda-ai-governance-skill

> ⚠ **Engineering reference material — not legal or regulatory advice.** This skill helps engineers align agentic AI systems with Singapore IMDA's *Model AI Governance Framework for Agentic AI*, with IMDA's *Model AI Governance Framework for Generative AI* as a supplement. It is **not** authoritative guidance, **not** an audit or certification, and **not affiliated with or endorsed by IMDA**. The framework itself is voluntary. Always verify against the official IMDA publication and involve your risk, security and compliance owners. See [DISCLAIMER.md](DISCLAIMER.md).
>
> **Source-text posture:** this skill **does not reproduce or republish the framework**. It provides engineer-facing interpretation, layered patterns, short attributed quotations of operative phrases, and section references, with a pointer to the official source. See [DISCLAIMER.md § Copyright in source materials](DISCLAIMER.md#copyright-in-source-materials).

An agentic-AI governance reference for engineers — packaged as both a [Claude Code skill](https://docs.claude.com/en/docs/claude-code/skills) and a Codex plugin, with `AGENTS.md` routing for Cursor and Copilot — organised by where in the system each expectation lands rather than by framework section number.

**Status:** Model AI Governance Framework for Agentic AI **v1.5** (IMDA, published 20 May 2026, updated 5 June 2026) populated as the primary framework. Model AI Governance Framework for Generative AI (IMDA / AI Verify Foundation, 2024) populated as a supplement covering the model, data and generated-content layer under an agent, and generative features that take no actions. Repo ships dual plugin manifests — [`.claude-plugin/`](.claude-plugin/) (Claude Code / Cowork via `/plugin install`) and [`.codex-plugin/`](.codex-plugin/) (Codex) — plus [`AGENTS.md`](AGENTS.md) routing for Cursor / Copilot.

**Audience:** engineers, architects and tech leads building or deploying AI agents — agentic features, coding assistants, workflow automation, customer-facing agents, multi-agent systems, computer-use agents — who need their design, architecture, internal guidelines and implementation to line up with the framework. Tech-agnostic: works whatever the model provider, agent framework (LangGraph, CrewAI, an agent SDK, your own loop), cloud or language.

## What it covers

| Framework | Publisher | Status |
|---|---|---|
| Model AI Governance Framework for Agentic AI, v1.5 | IMDA (Singapore) | ✅ Populated |
| Model AI Governance Framework for Generative AI (2024) | IMDA / AI Verify Foundation | ✅ Populated as a supplement |
| Model AI Governance Framework, 2nd Edition (2020) | IMDA / PDPC | Not populated |

**Not in scope:** binding law. Alignment with this voluntary framework does not discharge obligations under the PDPA, sector rules (e.g. MAS), or contracts. For personal data, pair this skill with a data-protection reference such as [`personal-data-protection-skill`](https://github.com/AltByteSG/personal-data-protection-skill). Other jurisdictions' AI rules (EU AI Act, etc.) are out of scope.

## Why this exists

The framework is written for organisations. Engineers need answers like *"I'm giving this agent a refund tool — what has to be true before it ships?"* or *"Is this architecture doc aligned?"*, not a four-dimension overview. This skill bridges the two:

- **Layered guidance** by where in the system the expectation lands — accountability, risk, architecture and bounds, identity, controls, human oversight, testing, operations, user transparency, data and grounding.
- **Framework notes** per dimension, each expectation paired with the **evidence** a reviewer should ask to see.
- **Entry-point checklists** for alignment reviews, new agents, new tools and MCP servers, third-party agents, the release gate, change review and incidents — plus generative features without tools, and new datasets or RAG corpora.
- **Templates**: a per-agent **Agent Card**, a per-system **System Card** (the generative-AI framework's disclosure "food label"), and an **Alignment Review** report.
- **A section map** for citing `[MGF §x.y]` in PR descriptions and design reviews.
- A strict separation between what the frameworks say (`[MGF §x.y]` for agentic, `[MGF-GenAI <dimension>, p.N]` for generative) and what the skill recommends (`[Practice]`), so reviews don't overstate either framework.

## Use cases

### 1. Architecture review before build — a customer-support agent that can issue refunds

A team's design doc describes a support agent with tools to read orders, read the customer's email history, send replies and issue refunds up to $500. The doc says "the agent is instructed never to refund more than the order value." Running [`checklists/design-review.md`](skills/imda-ai-governance/checklists/design-review.md) produces:

- **High:** the refund limit is prompt-only on an irreversible action — move it into the tool as a hard ceiling `[MGF §2.1.2, §2.3.1]`; refunds above a threshold need human approval `[MGF §2.2.2]`.
- **High:** the agent reads untrusted email content and holds a refund tool in the same context — an injection path from customer email to money movement `[MGF §2.1.1]`. Split reader and actor, or gate refunds on approval.
- **Medium:** the agent uses a shared service account; no per-agent identity or user-capacity in logs `[MGF §2.1.2]`.
- **Medium:** no disclosure at the point of interaction and no human escalation path for customers `[MGF §2.4.2]`.

### 2. Internal coding-assistant rollout with MCP

A platform team wants to roll an agentic coding assistant out to 400 engineers with a dozen community MCP servers enabled. The skill steers them to the framework's gradual-rollout pattern `[MGF §2.3.3]`: a pilot with trained users, built-in tools only and low-risk repos; an MCP allowlist behind a gateway with pinned versions and logged traffic `[MGF §2.3.1]`; checkpoints for higher-stakes actions `[MGF §2.2.2]`, with approval defaults tiered by action as in the framework's Tencent case study (read free, edits per session, shell and network gated); and oversight metrics so they can tell when approvals have become rubber stamps.

### 3. Swapping the model under a production agent

A provider releases a new model and an engineer opens a PR changing one line. The changed-file tripwire flags it; [`checklists/change-review.md`](skills/imda-ai-governance/checklists/change-review.md) classifies a model change as **material** `[MGF §2.3.3]`: re-run the policy, tool-calling and bounds suites at release-gate thresholds, refresh the agent card, and roll out in stages rather than flipping it for everyone.

## Install

Skill content lives under [`skills/imda-ai-governance/`](skills/imda-ai-governance/), with plugin manifests in [`.claude-plugin/`](.claude-plugin/) and [`.codex-plugin/`](.codex-plugin/).

### Claude Code / Claude Cowork — via this repo's marketplace

```bash
claude plugin marketplace add AltByteSG/imda-ai-governance-skill
claude plugin install imda-ai-governance@imda-ai-governance-skill
```

The repo carries a [`marketplace.json`](.claude-plugin/marketplace.json) so it works as a single-plugin marketplace. Verify with `claude plugin list`.

### Codex / Cursor / Copilot

```bash
git clone https://github.com/AltByteSG/imda-ai-governance-skill.git ~/.tools/imda-ai-governance-skill
```

Then add a line to your project's `AGENTS.md` / `.cursorrules` / `.github/copilot-instructions.md`:

```markdown
For agentic AI governance (IMDA MGF for Agentic AI), follow
~/.tools/imda-ai-governance-skill/AGENTS.md
```

### Pin a specific upstream version

```bash
cd <clone-path> && git checkout v0.3.0
```

## Adapt to your project

Templates ship in [`skills/imda-ai-governance/templates/`](skills/imda-ai-governance/templates/). Setup instructions are in each file's header.

- **[`AGENT_CARD.md.template`](skills/imda-ai-governance/templates/AGENT_CARD.md.template)** — *any agent.* One per agent, kept in the folder named by `agentRegistry`. Holds ownership, components, action-space and autonomy, tools and permissions, risk assessment, controls inventory, residual-risk acceptance, approval matrix, test results, operations and change history — the evidence the framework expects.
- **[`SYSTEM_CARD.md.template`](skills/imda-ai-governance/templates/SYSTEM_CARD.md.template)** — *any generative system.* One per system: data used, evaluations, mitigations, risks and limits, intended use, user-data protection. Agent cards link to it.
- **[`ALIGNMENT_REVIEW.md.template`](skills/imda-ai-governance/templates/ALIGNMENT_REVIEW.md.template)** — *any agent.* The output shape for a design or architecture review.
- **[`ai-governance-nudge.sh.template`](skills/imda-ai-governance/templates/ai-governance-nudge.sh.template)** — **Claude Code only.** A `PostToolUse` hook that nudges Claude into the skill when it edits agent code, tools, prompts, policies, MCP config or evals.

### Project config

Save as `.ai-governance.json` in the consuming project (see [`.ai-governance.example.json`](.ai-governance.example.json)):

```json
{
  "aiGovernance": {
    "frameworks": ["sg-mgf-agentic", "sg-mgf-genai"],
    "role": ["system-provider", "deployer"],
    "riskTier": "medium",
    "agentRegistry": "docs/agents/",
    "reviewPolicy": "warn"
  }
}
```

- `frameworks` — primary first: `sg-mgf-agentic` for agents, with `sg-mgf-genai` as the supplement; `sg-mgf-genai` alone for generative features that take no actions. Unknown codes are rejected by the checker so a typo can't silently yield zero coverage.
- `role` — your value-chain role(s): `model-developer`, `tooling-provider`, `platform-provider`, `system-provider`, `deployer`. Read by the agent, not the script.
- `riskTier` — `unassessed`, `low`, `medium`, `high`. For multi-agent systems, the highest tier; per-agent tiers live in agent cards.
- `agentRegistry` — where agent cards live.
- `reviewPolicy` — `warn` or `block-on-sensitive-change`.

### Guardrail: pre-commit / CI changed-file check

Use the skill as the reasoning layer and [`scripts/ai-governance-check-changed-files.py`](scripts/ai-governance-check-changed-files.py) as a deterministic tripwire. The script does not judge alignment; it only flags changes that probably touch an agent — agent and orchestration code, MCP config, prompts, approval and guardrail logic, evals, agent-framework imports, tool-use and oversight keywords, and model identifiers — so someone runs the change-review checklist. It scans only the lines a change adds, and skips lockfiles and licences.

Copy the script into the consuming project, then wire it into pre-commit:

```yaml
repos:
  - repo: local
    hooks:
      - id: ai-governance-check
        name: Agentic AI governance changed-file check
        entry: python3 scripts/ai-governance-check-changed-files.py --staged
        language: system
        pass_filenames: false
```

Install the hook:

```bash
pip install pre-commit
pre-commit install
```

Or CI, against the pull-request diff:

```yaml
name: AI Governance Check

on:
  pull_request:

jobs:
  ai-governance:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - name: Run agentic AI changed-file check
        run: |
          python3 scripts/ai-governance-check-changed-files.py \
            --base origin/${{ github.base_ref }} \
            --head HEAD \
            --review-policy block-on-sensitive-change
```

Suggested flow:

1. Engineer edits an agent.
2. Pre-commit warns that agent-related files changed.
3. Engineer asks their coding agent to run the change review with this skill and records the category on the agent card.
4. In `block-on-sensitive-change` mode with `--base`/`--head`, CI blocks agent changes until a commit in the range carries the trailer `AI-Governance-Reviewed: yes` (change it with `--ack-trailer`).

## Versioning

Releases are tagged; see [CHANGELOG.md](CHANGELOG.md). [`frameworks/sg-mgf-agentic/README.md`](skills/imda-ai-governance/frameworks/sg-mgf-agentic/README.md) and [`frameworks/sg-mgf-genai/README.md`](skills/imda-ai-governance/frameworks/sg-mgf-genai/README.md) record which framework version the content reflects and when it was last verified. IMDA describes the framework as a living document; when it publishes a new version, the skill is updated and a new minor version released.

## Sources

### Singapore — Model AI Governance Framework for Agentic AI

- **Publisher:** Infocomm Media Development Authority (IMDA) — [www.imda.gov.sg](https://www.imda.gov.sg) (search *"Model AI Governance Framework for Agentic AI"*)
- **Version reflected:** 1.5, published 20 May 2026, updated 5 June 2026
- **Feedback and case-study submissions:** [go.gov.sg/mgfagentic-feedback](https://go.gov.sg/mgfagentic-feedback)
- **Referenced companion material:** CSA *Draft Addendum on Securing Agentic AI*; GovTech *Agentic Risk & Capability Framework*; IMDA *Starter Kit for Testing of LLM-based Applications for Safety and Reliability*; IMDA OpenClaw case study (May 2026)

### Singapore — Model AI Governance Framework for Generative AI

- **Publisher:** IMDA and the AI Verify Foundation — announced in IMDA's [factsheet of 30 May 2024](https://www.imda.gov.sg/resources/press-releases-factsheets-and-speeches/factsheets/2024/gen-ai-and-digital-foss-ai-governance-playbook); [PDF](https://aiverifyfoundation.sg/wp-content/uploads/2026/06/Model-AI-Governance-Framework-for-Generative-AI-19-June-2024.pdf) hosted by the AI Verify Foundation
- **Version reflected:** the final 2024 framework (nine dimensions). It has no section numbers, so the skill cites it by dimension and page.
- **Role in this skill:** supplement to the agentic framework

## Disclaimer

See [DISCLAIMER.md](DISCLAIMER.md). **This skill is reference material, not legal or regulatory advice, and is not endorsed by IMDA.**

## Privacy

See [PRIVACY.md](PRIVACY.md). **This project collects no data.**

## Contributing

Contributions welcome — see [CONTRIBUTING.md](CONTRIBUTING.md). Particularly valued: updates when IMDA publishes a new version; stack-specific examples for the layer files (kept as labelled examples, not coupled to the core text); and incident patterns that generalise.

## Licence

[MIT](LICENSE) — covers the original commentary, structure and templates only, not the framework text. Attribution appreciated but not required.
