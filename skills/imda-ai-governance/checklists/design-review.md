# Checklist — Alignment Review of a Design, Architecture or Guideline

> ⚠ **Reference material only — not legal or regulatory advice.** See [DISCLAIMER.md](../../../DISCLAIMER.md). Verify against the official IMDA publication and involve your risk and compliance owners.

Use when asked whether something that already exists — a design doc, architecture diagram, ADR, RFC, internal engineering guideline, agent configuration, PR, or a running system — is aligned with the MGF for Agentic AI. The output is a findings report in the shape of [`ALIGNMENT_REVIEW.md.template`](../templates/ALIGNMENT_REVIEW.md.template).

## How to run the review

### 1. Gather the material and say what you reviewed

List every artefact read (paths, links, versions). If the review is of a design doc only, say so: findings about intent are weaker than findings about code and config. Where both exist, **check the code and config against the doc** — mismatches are findings in their own right.

### 2. Describe the system in the framework's terms

Before judging anything, write down (from the material, marking anything inferred):

- [ ] Is it agentic per `[MGF §1.1]`? If not, stop and say which other guidance applies.
- [ ] The eight components `[MGF §1.1.1]`: model, instructions, memory, planning, tools, protocols, controls, logging — where each lives.
- [ ] Multi-agent pattern, if any `[MGF §1.1.2]`.
- [ ] **Action-space** and **autonomy** `[MGF §1.1.3]`, with the human-involvement level per significant action.
- [ ] Value-chain role(s) of the organisation `[MGF §2.2.1]`.
- [ ] Risk tier — from the material if assessed; otherwise your provisional tier using [layer 02](../layers/02-use-case-and-risk.md#tiering), clearly marked provisional.

If the material doesn't let you fill these in, that is the first finding: the design doesn't describe the agent well enough to govern it.

### 3. Walk the four dimensions

For each item below, record **Aligned / Partly aligned / Not aligned / Not applicable / Cannot determine**, with evidence (file and line, config key, diagram element, quote from the doc). Calibrate expectations to the tier: a low-tier internal summariser does not need what a high-tier payment agent needs.

**Dimension 1 — Assess and bound** ([dimension notes](../frameworks/sg-mgf-agentic/dimensions/01-assess-and-bound.md))

- [ ] Risk assessment exists and uses impact and likelihood factors `[MGF §2.1.1]`; the deterministic-workflow alternative was considered.
- [ ] Threat model names untrusted inputs and traces them to write-capable tools `[MGF §2.1.1]`.
- [ ] Least-privilege tool set; functional boundaries between agents `[MGF §2.1.2]`.
- [ ] Autonomy constrained by SOP encoded in the workflow where appropriate `[MGF §2.1.2]`.
- [ ] Blast radius bounded: sandboxing, limits, kill switch `[MGF §2.1.2]`.
- [ ] Limits are deterministic where risk is high; non-deterministic limits have compensating monitoring or approval `[MGF §2.1.2]`.
- [ ] Unique, accounted-for, centrally registered agent identity; capacity recorded `[MGF §2.1.2]`.
- [ ] Scoped, time-bound, non-transferable authorisation; bounded by the delegating human `[MGF §2.1.2]`.
- [ ] Residual risk named and accepted by someone with authority `[MGF §2.1.2]`.

**Dimension 2 — Human accountability** ([dimension notes](../frameworks/sg-mgf-agentic/dimensions/02-human-accountability.md))

- [ ] Named owners for use case, build, risk review, approvals, escalation `[MGF §2.2.1]`.
- [ ] Vendor and tool-host obligations covered by contract; opacity addressed or use case scoped down `[MGF §2.2.1]`.
- [ ] Approval checkpoints defined for high-stakes, irreversible, atypical and user-defined actions `[MGF §2.2.2]`.
- [ ] Approvals enforced at system level, bound to the action, logged.
- [ ] Approval requests are digestible and state the risk; high-risk approvals need justification `[MGF §2.2.2]`.
- [ ] Oversight effectiveness measured (override rate, response time, outliers) `[MGF §2.2.2]`.
- [ ] Approvers have the needed expertise and training `[MGF §2.2.2]`.
- [ ] Fails closed when approval infrastructure is unavailable or an action has no policy `[MGF §2.2.2]`.

**Dimension 3 — Technical controls and processes** ([dimension notes](../frameworks/sg-mgf-agentic/dimensions/03-technical-controls.md))

- [ ] Controls inventory with control types; structural controls on higher-risk actions `[MGF §2.3.1]`.
- [ ] Planning, tool, protocol / MCP and multi-agent controls appropriate to the design `[MGF §2.3.1]`.
- [ ] Runtime controls: rate limits, budgets, input / output validation `[MGF §2.3.1]`.
- [ ] Test plan covers task execution, policy compliance, tool calling, robustness; whole workflows; multi-agent level; realistic environment; repeated runs `[MGF §2.3.2]`.
- [ ] Gradual rollout plan by users, tools and systems `[MGF §2.3.3]`.
- [ ] Logging across interaction, tool and reasoning layers; tamper-evident `[MGF §2.3.3]`.
- [ ] Alert catalogue with an intervention per alert `[MGF §2.3.3]`.
- [ ] Post-deployment testing and feedback loops `[MGF §2.3.3]`.
- [ ] Change triggers and risk-categorised change review; behaviour-shaping artefacts version-controlled `[MGF §2.3, §2.3.3]`.

**Dimension 4 — End-user responsibility** ([dimension notes](../frameworks/sg-mgf-agentic/dimensions/04-end-user-responsibility.md))

- [ ] Agent disclosed at the point of interaction on every surface `[MGF §2.4.2]`.
- [ ] Capability statement: can / cannot / needs approval `[MGF §2.4.2]`.
- [ ] Data use explained; consent where needed `[MGF §2.4.2]`.
- [ ] Human escalation contact `[MGF §2.4.2]`.
- [ ] User-settable limits where appropriate `[MGF §2.4.2]`.
- [ ] For internal users: training, feedback path, manual fallback for critical processes `[MGF §2.4.3]`.

**Systemic and multi-agent** (if more than one agent) ([foundations](../frameworks/sg-mgf-agentic/dimensions/00-foundations.md#123--systemic-and-multi-agent-risks-new-in-v15))

- [ ] Cascading errors contained by validation between steps `[MGF §1.2.3]`.
- [ ] Conflicting objectives resolved deterministically or by a human.
- [ ] Shared memory and context limited; structured inter-agent messages `[MGF §2.3.1]`.
- [ ] System-level tests for emergent behaviour and a compromised agent `[MGF §2.3.2]`.

### 4. Write findings, not a checklist dump

For each item not aligned or partly aligned, write a finding:

- **Title** — the gap in one line.
- **Severity** — `[Practice]` *High* (an irreversible or high-stakes action lacks a structural control or approval; no way to stop the agent; agent can exceed the delegating user's permissions; injection path from untrusted input to a consequential tool), *Medium* (expectation partly met, or met only by prompt or intent; missing measurement), *Low* (documentation, naming, or evidence gaps where the control likely exists).
- **Framework reference** — `[MGF §x.y]` and a short paraphrase. Don't overstate: the framework says organisations *should consider*; frame findings as misalignment with recommended practice, not breach.
- **Evidence** — what in the material shows the gap.
- **Recommendation** — the smallest change that closes it, preferring stronger control types ([layer 05](../layers/05-technical-controls.md#pick-the-strongest-control-type-the-risk-allows)). Mark it `[Practice]` if it's this skill's suggestion rather than the framework's.

Order findings by severity. Lead the report with a one-paragraph verdict and the top three things to fix.

### 5. Be explicit about limits

State what you couldn't verify (e.g. "contract terms not reviewed", "runtime config not provided", "no eval results available"), and that the review is engineering alignment with voluntary guidance — not a legal opinion, audit, or certification.
