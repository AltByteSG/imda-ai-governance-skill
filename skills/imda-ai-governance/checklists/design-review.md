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

Record the skill version and the framework version you reviewed against.

If the material doesn't let you fill these in, that is the first finding: the design doesn't describe the agent well enough to govern it.

### 3. Walk the four dimensions

For each item below, record **Aligned / Partly aligned / Not aligned / Not applicable / Cannot determine**, with evidence, in the item table of the review template (file and line, config key, diagram element, quote from the doc). Calibrate expectations to the tier: a low-tier internal summariser does not need what a high-tier payment agent needs.

**Dimension 1 — Assess and bound** ([dimension notes](../frameworks/sg-mgf-agentic/dimensions/01-assess-and-bound.md))

- [ ] Risk assessment exists and uses impact and likelihood factors `[MGF §2.1.1]`; the deterministic-workflow alternative was considered.
- [ ] Threat model names untrusted inputs and traces them to write-capable tools `[MGF §2.1.1]`.
- [ ] Least-privilege tool set; functional boundaries between agents `[MGF §2.1.2]`.
- [ ] Autonomy constrained by SOP encoded in the workflow where appropriate `[MGF §2.1.2]`.
- [ ] Blast radius bounded: sandboxing, limits, kill switch `[MGF §2.1.2]`.
- [ ] Limits are deterministic where risk is high; non-deterministic limits have compensating monitoring or approval `[MGF §2.1.2]`.
- [ ] Unique, accounted-for, centrally registered agent identity; capacity recorded `[MGF §2.1.2]`.
- [ ] Scoped, time-bound, non-transferable authorisation with explicit escalation paths; as a rule of thumb no greater than the delegating human's; delegations recorded `[MGF §2.1.2]`.
- [ ] Residual risk named and accepted by someone with authority `[MGF §2.1.2]`.

**Dimension 2 — Human accountability** ([dimension notes](../frameworks/sg-mgf-agentic/dimensions/02-human-accountability.md))

- [ ] Responsibilities allocated within the organisation across the agent lifecycle `[MGF §2.2.1]`; `[Practice]` concretely, named owners for use case, build, risk review, approvals and user escalation.
- [ ] Internal capability to track agentic developments and adapt governance (adaptive governance) `[MGF §2.2.1]`.
- [ ] Vendor and tool-host obligations covered by contract; opacity addressed or use case scoped down `[MGF §2.2.1]`.
- [ ] Approval checkpoints defined for high-stakes, irreversible, atypical and user-defined actions `[MGF §2.2.2]`.
- [ ] Approvals enforced through system-level controls rather than prompt-layer guardrails (OpenClaw case, `[MGF §2]`); `[Practice]` bound to the exact action and logged.
- [ ] Approval requests are digestible and state the risk; high-risk approvals need justification `[MGF §2.2.2]`.
- [ ] Oversight effectiveness measured (override rate, response time, outliers) `[MGF §2.2.2]`.
- [ ] Approvers have the needed expertise and training `[MGF §2.2.2]`.
- [ ] Automated monitoring complements human oversight (alerts on logged events, anomaly detection), including denying action by default when approval infrastructure fails or an action has no approval policy `[MGF §2.2.2]`.

**Dimension 3 — Technical controls and processes** ([dimension notes](../frameworks/sg-mgf-agentic/dimensions/03-technical-controls.md))

- [ ] Structural / rule-based controls on higher-risk actions; model-based controls where rules can't express the risk `[MGF §2.3.1]`; `[Practice]` recorded in a controls inventory with control types.
- [ ] Planning, tool, protocol / MCP and multi-agent controls appropriate to the design `[MGF §2.3.1]`.
- [ ] Runtime controls such as rate limits on tool use and input validation `[MGF §2.3.1]`; `[Practice]` per-run budgets.
- [ ] Test plan covers task execution, policy compliance, tool calling, robustness; whole workflows; multi-agent level; realistic environment; repeated runs across varied datasets `[MGF §2.3.2]`.
- [ ] Evaluation method suited to each part (deterministic for structured tool calls, LLM or human for reasoning) while still evaluating trajectories holistically `[MGF §2.3.2]`.
- [ ] Tests or monitoring cover biased or unfair actions where the agent's actions affect people `[MGF §1.2.2]`.
- [ ] Regular red teaming and threat modelling by the cybersecurity function `[MGF §2.2.1]`; threat model regularly updated `[MGF §2.1.1]`.
- [ ] Gradual rollout plan by users, tools and systems `[MGF §2.3.3]`.
- [ ] Logging and monitoring across user-agent, agent-tool and reasoning layers; integrated with observability platforms; problematic trajectories cannot be deleted `[MGF §2.3.3]`.
- [ ] Alert catalogue with an intervention per alert `[MGF §2.3.3]`.
- [ ] Audits at regular intervals; human review to catch emergent behaviour; post-deployment testing; feedback loops `[MGF §2.3.3]`.
- [ ] Change triggers and risk-categorised change review; behaviour-shaping artefacts version-controlled `[MGF §2.3, §2.3.3]`.

**Dimension 4 — End-user responsibility** ([dimension notes](../frameworks/sg-mgf-agentic/dimensions/04-end-user-responsibility.md))

- [ ] Agent disclosed in the UI at the point of interaction `[MGF §2.4.2]`; `[Practice]` on every surface the agent runs on.
- [ ] Capability statement: can / cannot / needs approval `[MGF §2.4.2]`.
- [ ] Data use explained; consent where needed `[MGF §2.4.2]`.
- [ ] Human escalation contact `[MGF §2.4.2]`.
- [ ] User-settable limits where appropriate `[MGF §2.4.2]`.
- [ ] For internal users: training on use cases, instructing agents, range of actions and failure modes; feedback path; training and work exposure so users keep core skills when agents take over tasks `[MGF §2.4.3]`; `[Practice]` a documented manual fallback for critical processes.

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
