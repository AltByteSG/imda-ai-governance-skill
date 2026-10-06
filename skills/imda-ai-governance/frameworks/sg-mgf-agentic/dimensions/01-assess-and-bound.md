# §2.1 — Assess and Bound the Risks Upfront

> ⚠ **Reference material only — not legal or regulatory advice.** See [DISCLAIMER.md](https://github.com/AltByteSG/imda-ai-governance-skill/blob/main/DISCLAIMER.md). Verify against the official IMDA publication and involve your risk and compliance owners.
>
> **How to read this file:** the expectation paragraphs restate the framework, with its section. The **Engineering effect** and **Evidence** paragraphs are this skill's interpretation — treat them as `[Practice]`, not as IMDA requirements.

Dimension 1 is the design-time dimension: decide whether an agent is the right tool at all, then shrink what it can do until the remaining risk is acceptable. Most expensive misalignments are introduced here and found much later.

Each expectation below gives the framework's position, what it means for the build, and the **evidence** a reviewer should ask to see.

## §2.1.1 — Determine suitable use cases

### Weigh risk against benefit, and consider not using an agent

**Expectation:** identify and assess risk against benefit before development or deployment; risk is a function of likelihood and impact. The framework is explicit that *"not all use cases are suitable for agents, and some may be better served by deterministic workflows."*

**Engineering effect:** "why is this an agent and not a workflow?" is a legitimate review question with a required answer. If every step is known in advance, a deterministic pipeline that calls a model at specific points is lower-risk than a planning agent.

**Evidence:** a written risk assessment per agent (the [`AGENT_CARD.md`](../../../templates/AGENT_CARD.md.template) risk section is enough), naming the alternative considered.

### Score impact and likelihood on the framework's factors

**Expectation:** the framework lists non-exhaustive factors.

| Impact factors | Likelihood factors |
|---|---|
| Domain and use-case error tolerance; number and criticality of business processes supported | Level of autonomy (SOP vs own judgement) |
| Access to sensitive data — worse with persistent memory across sessions | Task complexity (number of steps, analysis per step) |
| Access to external systems (leakage to third parties, overloading them) | Exposure to external systems and who maintains them (prompt injection) |
| Scope of actions: read vs write; few tools vs many / computer use | Agent provided or operated by an external party (limited visibility and control) — new in v1.5 |
| Reversibility, including downstream obligations like contracts | System complexity: multiple agents, autonomous handoffs, feedback loops — new in v1.5 |

**Engineering effect:** every factor is a design property you can change. Removing write scope, removing persistent memory, replacing web access with a curated corpus, or replacing free planning with an SOP each moves the score.

**Evidence:** the factor-by-factor assessment, and the tier it produced. See [layer 02](../../../layers/02-use-case-and-risk.md).

### Threat-model the agent, including taint tracing

**Expectation:** threat modelling makes the risk assessment more rigorous; common threats include memory poisoning, tool misuse and privilege compromise. For complex systems, use **taint tracing** to map how untrusted data moves through workflows. The threat model should be regularly updated. The framework points to CSA's Draft Addendum on Securing Agentic AI for method.

**Evidence:** a threat model that names the agent's untrusted input sources (web pages, emails, documents, tool outputs, other agents) and traces each to the tools it could influence. A threat model with no data-flow from untrusted input to write-capable tools is incomplete.

## §2.1.2 — Bound risks through design

### Limit access to tools and systems (least privilege)

**Expectation:** least-privilege policies giving agents only the minimum tools and data needed. Structuring agents around functional boundaries (e.g. separating IT helpdesk from HR self-service) acts as a natural constraint.

**Evidence:** the tool list per agent with each tool's scope; justification for every write-capable or external tool.

### Limit autonomy with SOPs

**Expectation:** define SOPs the agent is constrained to follow, rather than letting it define every step.

**Evidence:** the workflow definition (graph, state machine, step list) that encodes the SOP in code, not only in the prompt.

### Limit the area of impact and be able to take the agent offline

**Expectation:** design mechanisms and procedures to take agents offline and limit their scope of impact when they malfunction — including self-contained environments with limited network and data access, particularly for high-risk tasks such as code execution.

**Evidence:** a kill switch that has been exercised; sandbox configuration for code execution; network egress policy.

### Prefer deterministic limits

**Expectation:** *"prefer deterministic rather than non-deterministic limits, and bound by design."* Rather than prompting the agent not to use a tool, impose access controls so it cannot call it. Where limits are non-deterministic, layer on monitoring or human review.

**Evidence:** for each limit claimed in the design, where it is enforced. A limit enforced only by a prompt, on a higher-risk action, with no compensating monitor or approval, is a gap.

### Agent identity

**Expectation:** in the interim while standards mature, an agent's identity should be:

- **Unique** — its own cryptographically verifiable identity.
- **Accounted for** — tied to a supervising agent, human user, or department.
- **Differentiated by capacity** — whether acting independently or on behalf of a specific user, recorded for audit.
- **Catalogued and centrally managed** — issued and tracked by a central system to prevent sprawl, detect anomalies and remove unneeded identities.

**Evidence:** the agent's identity in the registry; how it authenticates to each tool (not a shared human or service account); audit logs that distinguish "agent acting for user X" from "agent acting on its own".

### Agent authorisation

**Expectation:** authorisations should generally be **scoped, time- or session-bound, non-transferable, least-privilege by default**, with explicit escalation paths. An agent's permissions should be **bounded by the authorising human's permissions** — a user should not be able to give an agent more than they have — and delegations should be recorded.

**Evidence:** token lifetimes and scopes; the check that intersects agent permissions with the delegating user's; the delegation record. See [layer 04](../../../layers/04-identity-and-authorisation.md).

### Evaluate residual risk

**Expectation:** some risk always remains; organisations should evaluate whether residual risk is tolerable and can be accepted.

**Evidence:** a named person or forum that accepted the residual risk for this agent at this tier, with a date — and a trigger for re-acceptance when the agent changes.
