# Checklist — Adopting a Third-Party Agent, Agent Platform or Embedded SaaS Agent

> ⚠ **Reference material only — not legal or regulatory advice.** See [DISCLAIMER.md](../../../DISCLAIMER.md). Verify against the official IMDA publication and involve your risk and compliance owners.

Use when the agent, or a component it depends on, is provided or operated by someone else: an agent platform, a vendor's agent, agentic features switched on inside a SaaS product, a hosted MCP server, or a model API. The framework treats external provision as raising likelihood of harm because visibility and control are limited `[MGF §2.1.1]`, and expects obligations and opacity to be addressed `[MGF §2.2.1]`.

## 1. Classify the dependency

- [ ] What is it: model provider / tooling provider (MCP, API) / platform provider / system provider / packaged agent `[MGF §2.2.1]`.
- [ ] What can it do in your environment: read, write, act externally, on which systems?
- [ ] What data reaches it, and does it persist (memory, logs, training)?
- [ ] Your tier for the use case ([layer 02](../layers/02-use-case-and-risk.md)), including the external-provision factor.

## 2. Transparency from the vendor `[MGF §2.2.1]`

- [ ] Disclosure of agent capabilities — actions it can take, tools it uses, autonomy level.
- [ ] Data handling — what's stored, where, how long, sub-processors, whether used for training, deletion on request.
- [ ] Model change policy — notice before model or behaviour changes.
- [ ] Testing and evaluation evidence the vendor can share.
- [ ] Incident notification commitments.

## 3. Technical security and control features `[MGF §2.2.1]`

- [ ] Strong authentication with **scoped API keys** or equivalent; least-privilege configuration possible.
- [ ] **Per-agent identity tokens** so actions are attributable.
- [ ] **Logging of tool calls and access history** that you can export into your own monitoring.
- [ ] Ability to require human approval for actions you classify as high-stakes.
- [ ] Ability to restrict tools, connectors and data sources; MCP allowlisting.
- [ ] Kill switch you control.
- [ ] Secure defaults — or, if permissive by default (as the framework's OpenClaw case notes), a hardening configuration you've applied and verified.

## 4. Contract and terms `[MGF §2.2.1]`

- [ ] Security arrangements.
- [ ] Performance guarantees.
- [ ] Data protection terms (and a data-processing agreement where personal data is involved — a statutory requirement under the PDPA in many cases, not just good practice).
- [ ] Where gaps exist: reassess whether the deployment still meets risk tolerance.

## 5. Decide, and contain

- [ ] If features are lacking: alternative vendor, in-house build, or **scope the use case down** (e.g. no sensitive data, read-only, internal only) `[MGF §2.2.1]`. Record the decision.
- [ ] **Containment by default** `[Practice]`: vendor-embedded agents act only within their own platform; cross-system reach only through integrations you control and log (the framework's MSD case study).
- [ ] Dedicated identity and credentials for the vendor agent in your systems ([layer 04](../layers/04-identity-and-authorisation.md)).

## 6. Test it yourself

- [ ] Run the bounds, access-boundary and injection suites from [layer 07](../layers/07-testing-and-evaluation.md) against your configuration — the vendor's testing covered their ecosystem, not your cross-platform use (the MSD case study notes cross-platform actions are where untested risk concentrates).
- [ ] Attempt disallowed actions to confirm restrictions hold.

## 7. Operate and record

- [ ] Vendor logs flowing into your monitoring and alerts ([layer 08](../layers/08-monitoring-and-operations.md)).
- [ ] Vendor model or feature updates registered as change triggers.
- [ ] Registry entry and agent card with the vendor named as a dependency; residual risk accepted by the use-case owner.
- [ ] Users told they are dealing with an agent and how to escalate ([layer 09](../layers/09-end-user-transparency.md)).
