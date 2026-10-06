# Checklist — Agent Incident

> ⚠ **Reference material only — not legal or regulatory advice.** See [DISCLAIMER.md](https://github.com/AltByteSG/imda-ai-governance-skill/blob/main/DISCLAIMER.md). Verify against the official IMDA publication and involve your risk and compliance owners.

Use when an agent took, or tried to take, an action outside its intended scope: an erroneous, unauthorised or biased action, a data exposure or wrongful modification, or disruption to a connected system `[MGF §1.2.2]` — including near-misses that a control caught.

> **If personal data may be involved, statutory breach-notification duties can start immediately and run in parallel to this checklist** (in Singapore, the PDPA's data-breach assessment and notification requirements). Bring in your DPO at step 1, not at the end.

## 1. Contain (minutes)

- [ ] Stop the affected runs; pull the kill switch if the cause is unknown or still active `[MGF §2.3.3]`.
- [ ] Revoke or narrow the agent's credentials if misuse or compromise is possible.
- [ ] Route work to the fallback path ([layer 09](../layers/09-end-user-transparency.md#tradecraft-and-continuity)).
- [ ] Preserve traces and logs — they must not be deleted or rotated out `[MGF §2.3.3]`.
- [ ] Notify the agent's technical owner, use-case owner, and security if compromise is suspected; DPO if personal data is involved.

## 2. Scope (hours)

- [ ] Which runs, users, records, systems and external parties were affected? Use run ids from traces.
- [ ] Which actions are reversible? Reverse them where safe.
- [ ] Did external communications or transactions go out? Who needs to be told?
- [ ] Is the cause still exploitable (e.g. an injection payload still sitting in a source the agent reads)?

## 3. Diagnose

Trace back through the trajectory ([layer 08](../layers/08-monitoring-and-operations.md#what-to-log)) and classify the root cause by component `[MGF §1.2.1]`:

- [ ] **Planning** — misread intent, plan drift.
- [ ] **Tools** — wrong tool, wrong input, hallucinated tool, over-broad tool.
- [ ] **Protocols** — compromised or misbehaving MCP server or peer agent.
- [ ] **Injection** — untrusted content redirected the agent; identify the source → sink path.
- [ ] **Permissions** — the agent could do something it should never have been able to do.
- [ ] **Oversight** — an approval was required and missing, or given without effective review (check override rate and time to decision for that approver / queue).
- [ ] **Multi-agent** — cascade, miscoordination, conflicting objectives.
- [ ] **Change** — a recent model, prompt or tool change; a provider-side model update.

Ask specifically: **which control should have stopped this, and why didn't it?** If the answer is "the prompt told it not to", the fix is a stronger control type ([layer 05](../layers/05-technical-controls.md#pick-the-strongest-control-type-the-risk-allows)).

## 4. Fix and verify

- [ ] Fix at the strongest control rank available, not by adding prompt text.
- [ ] Add the incident as a regression test case ([layer 07](../layers/07-testing-and-evaluation.md#after-deployment)).
- [ ] Run [`change-review.md`](change-review.md) for the fix — usually material or critical.
- [ ] Re-enable gradually, not straight back to full exposure.

## 5. Learn

- [ ] Re-assess the tier and residual risk; earlier dimensions are revisited when anomalies are found `[MGF §2]`.
- [ ] Update threat model, alert catalogue and approval matrix.
- [ ] Tell affected users what happened and how to reach a human ([layer 09](../layers/09-end-user-transparency.md)).
- [ ] Record the incident on the agent card with a link to the write-up.
- [ ] Check it against your threshold for **external** reporting (regulator, sector body, affected partners) `[MGF-GenAI Incident Reporting, p.17–18]`, and against any statutory notification duty (for example a PDPA data-breach notification), which is law, not guidance.
- [ ] If the incident came from an outside report, credit and update the reporter, and publish the fix within your disclosure window ([layer 08](../layers/08-monitoring-and-operations.md)).
