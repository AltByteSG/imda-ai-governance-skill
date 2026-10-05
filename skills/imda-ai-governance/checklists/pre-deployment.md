# Checklist — Pre-Deployment Release Gate

> ⚠ **Reference material only — not legal or regulatory advice.** See [DISCLAIMER.md](../../../DISCLAIMER.md). Verify against the official IMDA publication and involve your risk and compliance owners.

Use before an agent's first production exposure, before each rollout stage widens, and before releasing a material or critical change. Framework basis: `[MGF §2.3.2]`, `[MGF §2.3.3]`. Items marked **(M+)** apply at medium tier and above; **(H)** at high tier.

## 1. Paperwork is current

- [ ] Agent card reflects the version being released: model and version, prompt version, tools and scopes, approval matrix, tier.
- [ ] Threat model updated for any new tool, data source or agent.
- [ ] Residual risk accepted for this version and this rollout stage `[MGF §2.1.2]`.

## 2. Tests passed at the thresholds set in advance ([layer 07](../layers/07-testing-and-evaluation.md))

- [ ] **Task execution** — success rate meets target over the stated number of runs per scenario.
- [ ] **Policy compliance** — SOP followed; approval requested for every action in the matrix; **zero** unapproved executions of approval-gated actions across all runs (M+).
- [ ] **Tool calling** — right tools, inputs, order; no unlisted or hallucinated tools.
- [ ] **Robustness** — safe behaviour on tool errors, timeouts, empty and malformed results; no unbounded loops.
- [ ] **Bounds** — disallowed actions attempted and blocked; limits hold.
- [ ] **Fail-closed** — approval service down → no action; unknown action → denied or escalated; kill switch stops an in-flight run.
- [ ] **Injection** — each untrusted source tested against each consequential sink (M+).
- [ ] **Access boundaries** — user × domain matrix for multi-user agents.
- [ ] **Fairness** — where actions affect people differently.
- [ ] **Multi-agent** — system-level tests including a compromised-agent scenario, if more than one agent.
- [ ] **Red team** completed and findings triaged (H).
- [ ] Results recorded against the exact versions being released.

## 3. Runtime is ready ([layer 08](../layers/08-monitoring-and-operations.md))

- [ ] Traces flowing with run metadata, tool calls, policy decisions and approvals; tamper-evident storage.
- [ ] Alert catalogue live, each alert with an owner and intervention.
- [ ] Kill switch exercised in this environment; on-call knows how to use it.
- [ ] Fallback path for the work while the agent is off.
- [ ] Oversight metrics instrumented (override rate, time to decision).

## 4. Rollout stage is defined

- [ ] Which users, tools / MCP servers and systems are in this stage `[MGF §2.3.3]`.
- [ ] Exit criteria to the next stage, and the rollback trigger.
- [ ] Feature flag in place to roll back without deploy.

## 5. Users are ready ([layer 09](../layers/09-end-user-transparency.md))

- [ ] Agent disclosed at point of interaction on every surface in this stage.
- [ ] Capability statement, data notice and escalation contact published.
- [ ] For internal users: training delivered; feedback path live; manual procedure documented for critical processes.

## 6. Sign-off

- [ ] Technical owner, use-case owner and (M+) risk / security reviewer sign off, recorded on the agent card.
