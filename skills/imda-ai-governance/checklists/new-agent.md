# Checklist — Designing a New Agent or Agentic Feature

> ⚠ **Reference material only — not legal or regulatory advice.** See [DISCLAIMER.md](https://github.com/AltByteSG/imda-ai-governance-skill/blob/main/DISCLAIMER.md). Verify against the official IMDA publication and involve your risk and compliance owners.

Use when starting a new agent, or when an existing feature gains its first ability to take actions. The output is a filled-in [`AGENT_CARD.md`](../templates/AGENT_CARD.md.template) and a design that will pass [`design-review.md`](design-review.md).

> Walk this checklist against the layer files (`../layers/`) for **how** to build, and against `../frameworks/sg-mgf-agentic/dimensions/` for **what** the framework expects.

## 1. Should this be an agent, and how risky is it? ([layer 02](../layers/02-use-case-and-risk.md))

**Do this first.** The tier decides how much of the rest of this checklist applies, and several answers change what you build rather than what you check.

- [ ] Goal and users written down in two sentences.
- [ ] Deterministic workflow considered; reason for choosing an agent recorded `[MGF §2.1.1]`.
- [ ] Impact factors scored: domain error tolerance, sensitive data, external access, action scope, reversibility.
- [ ] Likelihood factors scored: autonomy, task complexity, untrusted input exposure, third-party provision, system complexity.
- [ ] Tier assigned by the **highest-impact action**. If one action drives the tier up, consider removing it or splitting it into a separate agent.
- [ ] Threat model: untrusted sources → consequential sinks traced; each path broken or guarded.
- [ ] Use-case owner identified and approval obtained, including limits on data access `[MGF §2.2.1]`.

## 2. Architecture and bounds ([layer 03](../layers/03-architecture-and-bounding.md))

- [ ] Action-space written down: systems, read / write per tool, computer-use or not.
- [ ] Autonomy written down: SOP vs judgement; human-involvement level per action.
- [ ] Workflow encoded in code where steps are known; validation between steps; iteration and tool-call caps.
- [ ] Narrow agents along functional boundaries; reader / actor separation where untrusted content is processed.
- [ ] Sandbox for code execution; egress denied by default.
- [ ] Hard limits on consequential parameters (amounts, record counts, recipients, rates).
- [ ] Reversible designs preferred (drafts, staging, soft delete).
- [ ] Sensitive data kept out of context where possible; memory scoped and with retention.
- [ ] Kill switch and fallback path designed.

## 3. Identity and permissions ([layer 04](../layers/04-identity-and-authorisation.md))

- [ ] Dedicated, verifiable identity for the agent (and each sub-agent).
- [ ] Owner bound in the registry.
- [ ] Capacity (own authority vs on behalf of user) carried into every call and log.
- [ ] Scoped, short-lived, non-transferable credentials per tool.
- [ ] Effective permissions ≤ delegating user's; checked at the resource.
- [ ] Escalation flow for elevated permissions; no standing elevated access.
- [ ] Secrets injected at the tool boundary; user takeover for credentials.

## 4. Controls ([layer 05](../layers/05-technical-controls.md))

- [ ] Controls inventory started; every medium / high risk has a rank 1–3 control.
- [ ] Tool schemas strict; read and write tools separated; destructive tools narrow.
- [ ] Tool outputs treated as untrusted.
- [ ] MCP servers allowlisted, pinned, ideally behind a gateway; code execution sandboxed.
- [ ] Inter-agent messages typed; shared memory limited.
- [ ] Runtime budgets, rate limits, circuit breakers; unknown actions deny or ask.

## 5. Human oversight ([layer 06](../layers/06-human-oversight.md))

- [ ] Action → approval matrix, covering high-stakes, irreversible, atypical and user-defined triggers.
- [ ] Approvals enforced by the runtime, bound to exact arguments, logged.
- [ ] Fail-closed behaviour defined.
- [ ] Approval request format designed (what, why, risk, parameters, options).
- [ ] Approver expertise stated per queue.
- [ ] Oversight metrics planned (override rate, time to decision).

## 6. Testing plan ([layer 07](../layers/07-testing-and-evaluation.md))

- [ ] Suites planned: task, policy, tool-calling, robustness, adversarial, bounds, fail-closed, fairness where relevant, access-boundary for multi-user agents.
- [ ] Pass thresholds set per suite before testing.
- [ ] Realistic environment identified; irreversible externals mocked or sandboxed.
- [ ] Run count per scenario stated.

## 7. Operations plan ([layer 08](../layers/08-monitoring-and-operations.md))

- [ ] Rollout stages with exit criteria.
- [ ] Trace schema; tamper-evident storage; personal-data hygiene in traces.
- [ ] Alert catalogue with interventions and owners.
- [ ] Audit cadence set by tier.
- [ ] Change triggers and categories agreed.

## 8. Users ([layer 09](../layers/09-end-user-transparency.md))

- [ ] Disclosure at point of interaction on every surface.
- [ ] Capability statement (can / cannot / needs approval).
- [ ] Data notice and consent where needed (and PDPA obligations if personal data is involved).
- [ ] Human escalation path.
- [ ] For internal users: training content, feedback path, manual fallback for critical processes.

## 9. Record and sign off

- [ ] [`AGENT_CARD.md`](../templates/AGENT_CARD.md.template) filled in and stored in the agent registry folder.
- [ ] Residual risk written in plain words and accepted by the use-case owner `[MGF §2.1.2]`.
- [ ] `.ai-governance.json` updated (`riskTier`, `agentRegistry`).
