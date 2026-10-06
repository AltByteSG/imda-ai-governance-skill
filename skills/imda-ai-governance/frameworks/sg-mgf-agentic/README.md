# Singapore MGF for Agentic AI — Framework Notes

> ⚠ **Reference material only — not legal or regulatory advice.** See [DISCLAIMER.md](https://github.com/AltByteSG/imda-ai-governance-skill/blob/main/DISCLAIMER.md). Verify against the official IMDA publication and involve your risk and compliance owners.

| | |
|---|---|
| **Framework** | Model AI Governance Framework for Agentic AI |
| **Version reflected** | Version 1.5, published 20 May 2026 (updated 5 June 2026) |
| **Last verified** | 2026-10-05 |
| **Publisher** | Infocomm Media Development Authority (IMDA), Singapore — [www.imda.gov.sg](https://www.imda.gov.sg) |
| **Legal status** | Voluntary guidance. Not legislation; no penalties attach to it directly |
| **Previous version** | Version 1.0. v1.5 incorporated feedback from 60+ companies |
| **Feedback channel** | [go.gov.sg/mgfagentic-feedback](https://go.gov.sg/mgfagentic-feedback) |
| **Pending changes** | The framework describes itself as a living document. Check IMDA for a newer version before citing a section number |

> **Source copyright:** the framework is published by IMDA and remains IMDA's material. Quotations in this skill are short operative phrases reproduced with attribution for educational and engineering reference; they are **not** licensed under this repository's MIT licence. Case studies in the framework belong to the organisations that contributed them. See [DISCLAIMER.md § Copyright in source materials](https://github.com/AltByteSG/imda-ai-governance-skill/blob/main/DISCLAIMER.md#copyright-in-source-materials).

## What v1.5 changed (and why reviewers should care)

Teams that aligned to v1.0 should re-check these areas, because v1.5 added expectations that did not exist before:

- **Controls and logging are now core agent components** `[MGF §1.1.1]`. A design that treats guardrails and observability as optional add-ons no longer matches the framework's own definition of an agent.
- **Systemic and multi-agent risks** `[MGF §1.2.3]` — speed and volume, cascading effects, agent sprawl, miscoordination, conflict, collusion, emergent behaviour.
- **New risk factors** `[MGF §2.1.1]` — third-party provision of the agent, and overall system complexity.
- **Value chain split** `[MGF §2.2.1]` — platform providers are now separate from system providers / app developers.
- **Automation-bias metrics** `[MGF §2.2.2]` — human override rate and review response time (the section also covers outlier reviewers and reviewer training).
- **Choosing controls** `[MGF §2.3.1]` — structural / rule-based vs model-based or prompt-layer, and runtime controls.
- **Change management** `[MGF §2.3, §2.3.3]` — defined change triggers and risk-categorised review.
- **Tradecraft and business continuity** `[MGF §2.4.3]` — skills erosion as a continuity risk.

## The four dimensions

The framework is organised around four dimensions, meant to be applied iteratively — an anomaly found in monitoring sends you back to re-assess and re-bound `[MGF §2]`.

| File | Framework section | Topic |
|---|---|---|
| [00-foundations.md](dimensions/00-foundations.md) | §1 | What counts as an agent, its components, action-space vs autonomy, risk sources and types, systemic risks |
| [01-assess-and-bound.md](dimensions/01-assess-and-bound.md) | §2.1 | Use-case suitability, risk factors, threat modelling, agent limits, agent identity and authorisation, residual risk |
| [02-human-accountability.md](dimensions/02-human-accountability.md) | §2.2 | Responsibilities inside and outside the organisation, meaningful human oversight |
| [03-technical-controls.md](dimensions/03-technical-controls.md) | §2.3 | Design-time controls, pre-deployment testing, gradual rollout, monitoring, change management |
| [04-end-user-responsibility.md](dimensions/04-end-user-responsibility.md) | §2.4 | Transparency for users who interact with agents; training for users who work with them |

The reverse lookup (section → layer + dimension file) is at [framework-map.md](framework-map.md). Engineering takeaways from the framework's case studies are at [case-studies.md](case-studies.md).

## What's intentionally not covered

- **Annex A (further resources) and Annex B (call for feedback)** — pointers only, no expectations.
- **The detailed control catalogues the framework defers to** (CSA's Addendum, GovTech's ARC, OWASP agentic guidance). Use them directly.
- **Organisational policy-setting by leadership** (strategic goals for agent use) beyond what an engineer needs to know exists. Covered at the level of "is there an owner who signed this off", not how to run a board.

## Mental model: what makes this framework distinctive

If you've worked with model-centric AI governance (model cards, fairness metrics, content filters), recalibrate on these points:

- **The unit of risk is the action, not the output.** A wrong answer from a chatbot is a quality problem; a wrong action from an agent — a payment, a deletion, an email sent — is an incident. Almost every expectation follows from "what can this agent *do*, and can it be undone".
- **Action-space and autonomy are separate dials** `[MGF §1.1.3]`. Action-space is set by tools and permissions; autonomy by instructions and human involvement. A design review should state both explicitly, and a change to either is a change to the risk.
- **Deterministic beats probabilistic wherever the stakes are high.** The framework's most repeated design preference is to enforce limits at the system level rather than asking the model to behave `[MGF §2.1.2, §2.3.1]`, and to layer monitoring or human review wherever a limit has to be non-deterministic.
- **Human-in-the-loop is not a checkbox.** The framework treats an approval step that people rubber-stamp as a failed control, and expects its effectiveness to be measured over time `[MGF §2.2.2]`.
- **Residual risk is explicit.** After bounding and controls, someone decides whether what remains is tolerable `[MGF §2.1.2]`. A design with no named acceptance of residual risk has skipped a step.

## Cross-references

- [`../../checklists/`](../../checklists/) — entry points for common engineering tasks.
- [`../../templates/AGENT_CARD.md.template`](../../templates/AGENT_CARD.md.template) — the per-agent record most of the evidence ends up in.
- [`../../templates/ALIGNMENT_REVIEW.md.template`](../../templates/ALIGNMENT_REVIEW.md.template) — the shape of an alignment review.
