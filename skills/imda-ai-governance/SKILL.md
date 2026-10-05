---
name: imda-ai-governance
description: Engineering reference for aligning agentic AI systems with Singapore IMDA's Model AI Governance Framework for Agentic AI (v1.5, 2026). Use when designing, reviewing or changing anything that builds or deploys an AI agent — agent architecture and design docs, tool / MCP / API integrations, agent identity and permissions, human-approval flows, guardrails, evals and pre-deployment tests, monitoring and logging, rollout and change management, third-party agent platforms, or end-user disclosure for agents.
---

# IMDA AI Governance — Layered Reference for Agentic Systems

> # ⚠ Reference material, not legal or regulatory advice
>
> This skill is **engineering reference material**. It is not legal advice, not regulatory advice, and not an assessment or certification of any kind. The maintainers are **not affiliated with, endorsed by, or speaking for** the Infocomm Media Development Authority (IMDA) or any other Singapore government agency.
>
> **The Model AI Governance Framework (MGF) for Agentic AI is voluntary guidance.** It describes emerging good practice; most of it is phrased as what organisations *"should consider"*. This skill does not turn it into law, and alignment with it does not discharge obligations under statutes that *do* bind you (the PDPA, sector rules such as MAS notices, contract terms). Always (a) verify any section reference or quotation against the official IMDA publication, and (b) involve your organisation's risk, security, legal and compliance owners before treating a design as approved.
>
> **Source-text posture:** this skill **does not reproduce or republish the framework**. It provides engineer-facing interpretation, short attributed quotations of operative phrases, and section references, with a pointer to the official source. See [DISCLAIMER.md](../../DISCLAIMER.md), including [§ Copyright in source materials](../../DISCLAIMER.md#copyright-in-source-materials).

This skill helps engineers make sure that what they design and build — architecture, agent design, permissions, approval flows, tests, monitoring, rollout plans, user-facing disclosures, internal guidelines — lines up with IMDA's MGF for Agentic AI. It is organised by **where in the system the expectation lands**, not by framework section number, so an engineer can work from the thing in front of them (a tool definition, an approval dialog, a deploy plan) rather than from the PDF.

Two conventions run through every file:

- **`[MGF §x.y]`** marks something the framework itself says, with the section it comes from. That is the alignment bar.
- **`[Practice]`** marks an engineering pattern this skill recommends to *meet* that bar. It is not an IMDA requirement and can be substituted by anything that achieves the same outcome.

Keep that distinction in every review you write. A reviewer who presents a `[Practice]` item as "IMDA requires X" is overstating the framework.

## Step 1 — Establish scope and the project's governance config

**On first use in a project, check for `.ai-governance.json` at the project root.** If present, load the listed frameworks' `frameworks/<code>/README.md`, and read `riskTier` and `agentRegistry` before doing anything else. If absent, establish three things with the user:

1. **Is this agentic?** The framework targets systems that plan and take actions over multiple steps towards a goal, built on SLM / LLM / MLLM models `[MGF §1.1]`. A single-shot chat completion with no tools is mostly out of scope — the earlier MGF (2020) and the generative-AI guidance apply instead.
2. **What is the organisation's role in the value chain?** Model developer, tooling provider, platform provider, system provider / app developer, deployer, or several `[MGF §2.2.1]`. A team building an agent and running it in-house is both system provider and deployer.
3. **What is the agent's current risk tier?** If nobody has assessed it, say so and run [`checklists/new-agent.md`](checklists/new-agent.md) section 1 first. Every later decision — how many approval checkpoints, how much testing, how gradual the rollout — is calibrated to it.

Then suggest creating `.ai-governance.json` so future sessions and the changed-file guardrail don't re-ask:

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

`riskTier` is one of `unassessed`, `low`, `medium`, `high` (see [layer 02](layers/02-use-case-and-risk.md#tiering)). `agentRegistry` is the folder holding one [`AGENT_CARD.md`](templates/AGENT_CARD.md.template) per agent. If the project cannot take that file, record the same facts in the project's `AGENTS.md`, `CLAUDE.md` or equivalent instruction file.

Framework codes: `sg-mgf-agentic` (populated). Status of related Singapore frameworks lives in [`frameworks/_index.md`](frameworks/_index.md).

## Step 2 — Pick the right entry point

**You're reviewing something that already exists** — a design doc, architecture diagram, ADR, internal guideline, PR or running system — and want to know whether it is aligned:

| Task | Checklist |
|---|---|
| Review a design, architecture or guideline for alignment, and write up the gaps | [`checklists/design-review.md`](checklists/design-review.md) → output in the shape of [`ALIGNMENT_REVIEW.md.template`](templates/ALIGNMENT_REVIEW.md.template) |

**You're starting work on something.** Open the matching checklist:

| Task | Checklist |
|---|---|
| Designing a new agent, or a new agentic feature in an existing product | [`checklists/new-agent.md`](checklists/new-agent.md) |
| Giving an agent a new tool, API, MCP server, data source, or computer-use / browser access | [`checklists/new-tool-or-integration.md`](checklists/new-tool-or-integration.md) |
| Adopting a third-party agent, agent platform, or SaaS product with embedded agents | [`checklists/third-party-agent.md`](checklists/third-party-agent.md) |
| Getting an agent ready to ship (release gate) | [`checklists/pre-deployment.md`](checklists/pre-deployment.md) |
| Changing a deployed agent — model, prompt, tools, autonomy, workflow | [`checklists/change-review.md`](checklists/change-review.md) |
| An agent did something it shouldn't have | [`checklists/agent-incident.md`](checklists/agent-incident.md) |

**You want depth on a specific layer.** Open the matching layer file:

| Layer | What it covers |
|---|---|
| [01 Accountability](layers/01-accountability.md) | Who owns what across the value chain, vendor terms, adaptive governance, residual-risk sign-off |
| [02 Use case and risk](layers/02-use-case-and-risk.md) | Suitability, impact and likelihood factors, tiering, threat modelling and taint tracing |
| [03 Architecture and bounding](layers/03-architecture-and-bounding.md) | Action-space, autonomy, SOP-driven workflows, sandboxes, blast radius, kill switch, multi-agent topology |
| [04 Identity and authorisation](layers/04-identity-and-authorisation.md) | Agent identity, delegation, least privilege, session-bound scopes, central registry |
| [05 Technical controls](layers/05-technical-controls.md) | Structural vs prompt-layer controls; planning, tool, protocol / MCP, multi-agent and runtime controls |
| [06 Human oversight](layers/06-human-oversight.md) | Approval checkpoints, approval UX, automation bias, fail-closed approvals |
| [07 Testing and evaluation](layers/07-testing-and-evaluation.md) | Task, policy, tool-call and robustness tests; workflow-level and multi-agent tests; repeated runs |
| [08 Monitoring and operations](layers/08-monitoring-and-operations.md) | What to log, alerts, interventions, immutable trails, gradual rollout, change management, incidents |
| [09 End-user transparency](layers/09-end-user-transparency.md) | Agent disclosure, capability statements, escalation contacts, training, tradecraft retention |

Layer files say **how** to build it. What the framework expects, section by section, lives in [`frameworks/sg-mgf-agentic/dimensions/`](frameworks/sg-mgf-agentic/dimensions/); use [`framework-map.md`](frameworks/sg-mgf-agentic/framework-map.md) to cite a section in a PR description or review.

## Load-bearing principles (commit to memory)

These recur across the framework and settle most design arguments. Each links to the section that carries it.

| Principle | What it means for a design | Source |
|---|---|---|
| **Bound by design, not by prompt** | If an agent must not do something, make it impossible at the tool, permission or workflow layer. A system-prompt instruction is the weakest control available and is not sufficient on its own for higher-risk actions. | `[MGF §2.1.2, §2.3.1]` |
| **Risk = impact × likelihood, assessed per agent** | Impact grows with domain criticality, sensitive-data access, external access, write scope and irreversibility. Likelihood grows with autonomy, task complexity, untrusted inputs, third-party opacity and system complexity. | `[MGF §2.1.1]` |
| **Least privilege, scoped and non-transferable** | Minimum tools and data for the task; authorisations time- or session-bound; an agent never holds more than the human who delegated to it. | `[MGF §2.1.2]` |
| **Every agent has an identity and an owner** | Unique, verifiable identity; tied to a human, team or supervising agent; capacity recorded; issued from a central registry to stop sprawl. | `[MGF §2.1.2]` |
| **Humans approve the irreversible and the high-stakes** | Define checkpoints for high-stakes, irreversible, atypical and user-defined actions; make approval requests short and clear; deny by default when approval infrastructure fails. | `[MGF §2.2.2]` |
| **Oversight decays — measure it** | Track override rates and review times; low override rates and fast approvals can signal rubber-stamping. | `[MGF §2.2.2]` |
| **Test the workflow, not just the answer** | Test task execution, policy compliance, tool calls (right tool, permission, input, order) and robustness, across whole trajectories, repeatedly, in realistic environments, individually and as a multi-agent system. | `[MGF §2.3.2]` |
| **Roll out gradually, monitor continuously** | Stage by users, tools and systems; log and trace every step; define alerts and the intervention each one triggers; keep failure trajectories undeletable. | `[MGF §2.3.3]` |
| **Changes get risk-categorised review** | Model updates, tool changes, autonomy changes, domain shifts and regulatory changes are triggers; review depth scales with the change. | `[MGF §2.3.3]` |
| **Tell users what the agent is and can do** | Declare the agent at the point of interaction, state its range of actions and data use, and name a human to escalate to. | `[MGF §2.4]` |

## How to use the layer ↔ framework split

The pattern is **design once against the layers, then check against the framework**:

1. Establish scope, role and risk tier (Step 1).
2. Walk the relevant `layers/` to plan or critique the implementation.
3. Walk `frameworks/sg-mgf-agentic/dimensions/01–04` and confirm each expectation that applies is met, partly met, not met, or not applicable — with evidence (a file, a config, a test, a dashboard), not intent.
4. Record the outcome where the next engineer will find it: the agent's [`AGENT_CARD.md`](templates/AGENT_CARD.md.template), the PR description, or an alignment review.

When reviewing, **report against what exists, not what the author meant**. A design doc that says "the agent will only read" while the tool grants write scope is a finding. A guardrail that lives only in the system prompt, protecting an irreversible action, is a finding. "We'll add monitoring later" for an agent heading to production is a finding.

## Interactions with other obligations

- **Personal data.** Agents that touch personal data also carry PDPA (or other data-protection) obligations, which are law, not guidance. The MGF points to the organisation's data privacy policies and explicit consent where needed `[MGF §2.4.2]`; it does not replace them. If the `personal-data-protection` skill is installed, run it alongside this one.
- **Cybersecurity.** The MGF defers to CSA's *Draft Addendum on Securing Agentic AI* and GovTech's *Agentic Risk & Capability Framework* for control catalogues `[MGF §2.3.1]`. This skill does not reproduce them.
- **Sector rules.** Financial services, healthcare and public-sector deployments typically have binding rules on outsourcing, model risk and technology risk that sit above this framework.

## Framework version

[`frameworks/sg-mgf-agentic/README.md`](frameworks/sg-mgf-agentic/README.md) records which version of the framework the content reflects, when it was last verified, and what to watch for. The framework calls itself a living document and is updated as practice develops; check IMDA for a newer version before relying on a section number. See the upstream [CHANGELOG.md](../../CHANGELOG.md) and pin to a tag if you need stability.
