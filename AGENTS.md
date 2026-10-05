# AGENTS.md — IMDA AI Governance Skill (Agentic AI)

> ⚠ **Reference material only — not legal or regulatory advice.** See [DISCLAIMER.md](DISCLAIMER.md). Not affiliated with or endorsed by IMDA. The Model AI Governance Framework for Agentic AI is voluntary guidance; verify against the official IMDA publication and involve your risk and compliance owners.
>
> **Source-text posture:** this skill **does not reproduce or republish the framework**. It provides engineer-facing interpretation, short attributed quotations of operative phrases, and section references, with a pointer to the official source. See [DISCLAIMER.md § Copyright in source materials](DISCLAIMER.md#copyright-in-source-materials).

This file is the **Codex CLI / Cursor / Copilot-friendly entry point** to the same content surfaced to Claude Code via [`skills/imda-ai-governance/SKILL.md`](skills/imda-ai-governance/SKILL.md). The two files mirror each other; if you edit one, mirror the change to the other.

The skill content lives under [`skills/imda-ai-governance/`](skills/imda-ai-governance/) — required by the Claude Code plugin format. All internal links in this file point into that subdirectory.

If you are an agent and the user is designing, reviewing or changing anything that builds or deploys an AI agent — agent architecture or design docs, tool / MCP / API integrations, agent identity and permissions, human-approval flows, guardrails, evals and pre-deployment tests, monitoring and logging, rollout and change management, third-party agent platforms, or end-user disclosure for agents — follow the steps below.

Two conventions run through the layer files, checklists and templates (framework notes restate the framework and say where they add interpretation): **`[MGF §x.y]`** marks what the framework itself says, with its section; **`[Practice]`** marks an engineering pattern the skill recommends to meet it, which is not an IMDA requirement. Keep that distinction in anything you write for the user.

## Step 1 — Establish scope and the project's governance config

**On first use in a project, check for `.ai-governance.json` at the project root.** If present, load the listed frameworks' `skills/imda-ai-governance/frameworks/<code>/README.md`, and read `riskTier` and `agentRegistry` first. If absent, establish with the user:

1. **Is this agentic?** Systems that plan and take actions over multiple steps towards a goal, built on SLM / LLM / MLLM models `[MGF §1.1]`. A chat completion with no tools is mostly out of scope.
2. **The organisation's value-chain role(s):** model developer, tooling provider, platform provider, system provider / app developer, deployer `[MGF §2.2.1]`.
3. **The agent's risk tier.** If unassessed, run [`checklists/new-agent.md`](skills/imda-ai-governance/checklists/new-agent.md) section 1 first.

Then suggest creating `.ai-governance.json`:

```json
{
  "aiGovernance": {
    "frameworks": ["sg-mgf-agentic"],
    "role": ["system-provider", "deployer"],
    "riskTier": "unassessed",
    "agentRegistry": "docs/agents/",
    "reviewPolicy": "warn"
  }
}
```

`riskTier` is one of `unassessed`, `low`, `medium`, `high` (see [layer 02](skills/imda-ai-governance/layers/02-use-case-and-risk.md#tiering)). `agentRegistry` is the folder holding one [`AGENT_CARD.md`](skills/imda-ai-governance/templates/AGENT_CARD.md.template) per agent. If the project cannot take that file, record the same facts in the project's `AGENTS.md`, `CLAUDE.md` or equivalent.

| Code | Framework | Status |
|---|---|---|
| `sg-mgf-agentic` | Model AI Governance Framework for Agentic AI, v1.5 (IMDA, 20 May 2026, updated 5 June 2026) | ✅ populated |
| `sg-mgf-genai` | Model AI Governance Framework for Generative AI (2024) | not populated |
| `sg-mgf-2020` | Model AI Governance Framework, 2nd Edition (2020) | not populated |

See [`skills/imda-ai-governance/frameworks/_index.md`](skills/imda-ai-governance/frameworks/_index.md).

## Step 2 — Pick the right entry point

**You're reviewing something that already exists** (design doc, architecture, guideline, PR, running system):

| Task | Checklist |
|---|---|
| Review for alignment and write up the gaps | [`checklists/design-review.md`](skills/imda-ai-governance/checklists/design-review.md) → output shaped like [`ALIGNMENT_REVIEW.md.template`](skills/imda-ai-governance/templates/ALIGNMENT_REVIEW.md.template) |

**You're starting work on something:**

| Task | Checklist |
|---|---|
| New agent or agentic feature | [`checklists/new-agent.md`](skills/imda-ai-governance/checklists/new-agent.md) |
| New tool, API, MCP server, data source, or computer-use access | [`checklists/new-tool-or-integration.md`](skills/imda-ai-governance/checklists/new-tool-or-integration.md) |
| Third-party agent, platform, or SaaS with embedded agents | [`checklists/third-party-agent.md`](skills/imda-ai-governance/checklists/third-party-agent.md) |
| Release gate | [`checklists/pre-deployment.md`](skills/imda-ai-governance/checklists/pre-deployment.md) |
| Changing a deployed agent | [`checklists/change-review.md`](skills/imda-ai-governance/checklists/change-review.md) |
| Agent incident | [`checklists/agent-incident.md`](skills/imda-ai-governance/checklists/agent-incident.md) |

**You want depth on a specific layer:**

| Layer | What it covers |
|---|---|
| [01 Accountability](skills/imda-ai-governance/layers/01-accountability.md) | Owners across the value chain, vendor terms, adaptive governance, residual-risk sign-off |
| [02 Use case and risk](skills/imda-ai-governance/layers/02-use-case-and-risk.md) | Suitability, impact and likelihood factors, tiering, threat modelling and taint tracing |
| [03 Architecture and bounding](skills/imda-ai-governance/layers/03-architecture-and-bounding.md) | Action-space, autonomy, SOP workflows, sandboxes, blast radius, kill switch, multi-agent topology |
| [04 Identity and authorisation](skills/imda-ai-governance/layers/04-identity-and-authorisation.md) | Agent identity, delegation, least privilege, session-bound scopes, central registry |
| [05 Technical controls](skills/imda-ai-governance/layers/05-technical-controls.md) | Structural vs prompt-layer controls; planning, tool, MCP, multi-agent and runtime controls |
| [06 Human oversight](skills/imda-ai-governance/layers/06-human-oversight.md) | Approval checkpoints, approval UX, automation bias, fail-closed approvals |
| [07 Testing and evaluation](skills/imda-ai-governance/layers/07-testing-and-evaluation.md) | Task, policy, tool-call and robustness tests; workflow and multi-agent tests; repeated runs |
| [08 Monitoring and operations](skills/imda-ai-governance/layers/08-monitoring-and-operations.md) | Logging, alerts, interventions, immutable trails, gradual rollout, change management, incidents |
| [09 End-user transparency](skills/imda-ai-governance/layers/09-end-user-transparency.md) | Agent disclosure, capability statements, escalation, training, tradecraft retention |

Framework expectations by section live in [`frameworks/sg-mgf-agentic/dimensions/`](skills/imda-ai-governance/frameworks/sg-mgf-agentic/dimensions/); reverse lookup in [`framework-map.md`](skills/imda-ai-governance/frameworks/sg-mgf-agentic/framework-map.md).

## Load-bearing principles

| Principle | What it means for a design | Source |
|---|---|---|
| **Bound by design, not by prompt** | If an agent must not do something, make it impossible at the tool, permission or workflow layer. | `[MGF §2.1.2, §2.3.1]` |
| **Risk = impact × likelihood, per agent** | Impact: domain, sensitive data, external access, write scope, irreversibility. Likelihood: autonomy, complexity, untrusted inputs, third-party opacity, system complexity. | `[MGF §2.1.1]` |
| **Least privilege, scoped and non-transferable** | Minimum tools and data; time- or session-bound; as a rule of thumb, no more than the delegating human. | `[MGF §2.1.2]` |
| **Every agent has an identity and an owner** | Unique, verifiable, tied to an accountable owner, capacity recorded, centrally registered. | `[MGF §2.1.2]` |
| **Humans approve the irreversible and the high-stakes** | Checkpoints for high-stakes, irreversible, atypical and user-defined actions; digestible requests; deny by default when approvals fail. | `[MGF §2.2.2]` |
| **Oversight decays — measure it** | Track override rates and review times. | `[MGF §2.2.2]` |
| **Test the workflow, not just the answer** | Task, policy, tool-call and robustness; whole trajectories; repeated; realistic; multi-agent. | `[MGF §2.3.2]` |
| **Roll out gradually, monitor continuously** | Stage by users, tools, systems; trace every step; alert with defined interventions; keep failure trails. | `[MGF §2.3.3]` |
| **Changes get risk-categorised review** | Model, tool, autonomy, domain and regulatory changes are triggers. | `[MGF §2.3.3]` |
| **Tell users what the agent is and can do** | Disclose at the point of interaction; capabilities; data use; human escalation. | `[MGF §2.4]` |

## How to use the layer ↔ framework split

1. Establish scope, role and risk tier.
2. Walk the relevant `skills/imda-ai-governance/layers/` to plan or critique the implementation.
3. Walk `skills/imda-ai-governance/frameworks/sg-mgf-agentic/dimensions/01–04` and confirm each applicable expectation with evidence, not intent.
4. Record the outcome in the agent's `AGENT_CARD.md`, the PR description, or an alignment review.

When reviewing, **report against what exists, not what the author meant**. A design doc that says "the agent will only read" while the tool grants write scope is a finding. A guardrail that lives only in the system prompt, protecting an irreversible action, is a finding. "We'll add monitoring later" for an agent heading to production is a finding.

## Interactions with other obligations

- **Personal data.** Agents that touch personal data also carry PDPA (or other data-protection) obligations, which are law, not guidance. The MGF points to the organisation's data privacy policies and explicit consent where needed `[MGF §2.4.2]`; it does not replace them. If the `personal-data-protection` skill is installed, run it alongside this one.
- **Cybersecurity.** The MGF defers to CSA's *Draft Addendum on Securing Agentic AI* and GovTech's *Agentic Risk & Capability Framework* for control catalogues `[MGF §2.3.1]`. This skill does not reproduce them.
- **Sector rules.** Financial services, healthcare and public-sector deployments typically have binding rules on outsourcing, model risk and technology risk that sit above this framework.

## Differences from the Claude Code version

The content (`layers/`, `frameworks/`, `checklists/`, `templates/`) is identical between agents. The only Claude-specific element is `templates/ai-governance-nudge.sh.template`, a PostToolUse hook. Codex CLI, Cursor and Copilot can use the changed-file checker in [`scripts/ai-governance-check-changed-files.py`](scripts/ai-governance-check-changed-files.py) instead — see the README.

## Framework version + verification dates

[`frameworks/sg-mgf-agentic/README.md`](skills/imda-ai-governance/frameworks/sg-mgf-agentic/README.md) records the framework version reflected and when it was last verified. The framework is a living document; check IMDA for a newer version before citing a section number. See [CHANGELOG.md](CHANGELOG.md) and pin to a tag if you need stability.
