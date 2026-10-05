# Layer 01 — Accountability and Ownership

> ⚠ **Reference material only — not legal or regulatory advice.** See [DISCLAIMER.md](../../../DISCLAIMER.md). Verify against the official IMDA publication and involve your risk and compliance owners.

The non-technical scaffolding an engineer needs to know exists, because the rest of the build depends on it: who approved the use case, who owns the agent, who accepted the residual risk, and what the vendors are on the hook for. Framework basis: `[MGF §2.1.2]` (residual risk), `[MGF §2.2.1]`.

## Every agent has a named owner

`[MGF §2.2.1]` expects responsibilities allocated across the lifecycle. `[Practice]` Make that concrete per agent, in its [`AGENT_CARD.md`](../templates/AGENT_CARD.md.template):

| Role | Answers for | Typical holder |
|---|---|---|
| **Use-case owner** | The agent should exist, for this purpose, at this tier; human oversight is in place | Business or product lead |
| **Technical owner** | Design, controls, tests, monitoring, change management | Engineering lead of the building team |
| **Risk / security reviewer** | Threat model, control adequacy, red-team results | Security or technology-risk team |
| **Approver(s)** | Decisions at the human checkpoints | Named role or queue, with required expertise |
| **Escalation contact** | What end users contact when the agent misbehaves | Support / operations, reachable |

An agent where any of these is "TBD" at launch has an accountability gap the framework would flag.

## Use-case approval and residual-risk acceptance

`[MGF §2.2.1]` puts permitted use cases — **including limits on agent data access** — with key decision makers, and `[MGF §2.1.2]` expects residual risk to be evaluated and accepted. `[Practice]`:

- Record the approval: who, when, at which tier, with which data-access limits.
- Record residual risk in plain words ("the agent may send an incorrectly worded reply to a customer; mitigated by X; accepted by Y on date Z").
- Tie acceptance to a version. A material change ([layer 08](08-monitoring-and-operations.md#change-management)) re-opens it.

## Value-chain role

`[MGF §2.2.1]` lists model developers, tooling providers, platform providers, system providers / app developers, deployers and end users. `[Practice]` Record which roles you hold. If you **only deploy** a vendor's agent, your work concentrates on [layer 02](02-use-case-and-risk.md), [layer 06](06-human-oversight.md), [layer 08](08-monitoring-and-operations.md), [layer 09](09-end-user-transparency.md) and the vendor checks below. If you **build** it, everything applies.

## Vendors, platforms, model providers and tool hosts

`[MGF §2.2.1]` expects obligations clarified in contracts and third-party opacity addressed. `[Practice]` For every external party in the agent's path (model API, agent platform, hosted MCP server, SaaS with embedded agents):

- **Contract or T&C coverage** of security arrangements, performance guarantees, and data protection (retention, training use, sub-processors, location).
- **Disclosures** on what the vendor's agent can do and how it handles data.
- **Technical features**: scoped API keys, per-agent identity tokens, tool-call and access logs you can export.
- **Model change notice**: how you find out when the vendor changes the model behind an API. Unannounced model swaps are a change-management trigger you can't see without it.
- **Decision when they fall short**: substitute, build in-house, or **scope the use case down** (e.g. remove sensitive data) — and write down which.

Run [`checklists/third-party-agent.md`](../checklists/third-party-agent.md) for the full pass.

## Security baseline from the security team

`[MGF §2.2.1]` gives cybersecurity teams the job of baseline guardrails, secure-by-design templates, red teaming and threat modelling. `[Practice]` If templates exist, start from them and record deviations. If they don't, say so in the review — it is an organisational gap, not one the product team should silently absorb.

## Adaptive governance

`[MGF §2.2.1]` expects internal capability to keep up with new agent modalities and evaluation methods. `[Practice]` Assign someone to watch for (a) new versions of this framework, (b) model or platform changes from your providers, (c) new attack classes against agents. Each is a change-review trigger.

## Internal usage policy for agent users

For agents your own staff use (coding assistants, internal automation), `[MGF §2.2.1]` and `[MGF §2.4.3]` expect usage policies, training, and timely reporting of issues. `[Practice]` The policy should name restricted uses (e.g. no confidential data in a given tool), the approval behaviours users must not bypass, and where to report a bad agent action. See [layer 09](09-end-user-transparency.md).
