# §1 — Foundations: What the Framework Means by an Agent, and Its Risks

> ⚠ **Reference material only — not legal or regulatory advice.** See [DISCLAIMER.md](https://github.com/AltByteSG/imda-ai-governance-skill/blob/main/DISCLAIMER.md). Verify against the official IMDA publication and involve your risk and compliance owners.

Section 1 sets no expectations of its own, but every later section depends on its vocabulary. Use it to describe the system under review in the framework's terms before checking anything else; a review that can't name the agent's components, action-space and autonomy can't assess the rest.

## §1.1 — Scope: what counts as agentic

**Definition (paraphrased):** agents have some degree of independent planning, decision-making and action-taking over multiple steps towards a user-defined goal; agentic AI systems consist of one or more agents operating individually or collaboratively. The framework focuses on agents built on SLMs, LLMs or MLLMs, while noting that rule-based agents exist.

**Engineering effect:** the test is *actions over multiple steps*, not the word "agent" in the product name. A workflow engine that calls an LLM once per step to choose the next tool is in scope. A chat UI with no tools is not.

## §1.1.1 — The eight core components

The framework lists eight components. A design review should be able to point at where each one lives in the system — a missing or implicit component is usually where the gap is.

| # | Component | What to locate in the design |
|---|---|---|
| 1 | Model | Which model(s), which provider, which version is pinned |
| 2 | Instructions | System prompts, role definitions, behavioural constraints — and where they are versioned |
| 3 | Memory | Short- and long-term stores; what persists across sessions and users |
| 4 | Planning and reasoning | Whether the model plans freely or follows a fixed workflow |
| 5 | Tools | Every tool, its scope (read / write), and the system it reaches |
| 6 | Protocols | MCP, A2A, agentic-commerce protocols in use; which servers / peers |
| 7 | Controls | Access controls, guardrails, human approvals |
| 8 | Logging and monitoring | What is recorded across all components, and who watches it |

Components 7 and 8 were added in v1.5 as **core** components, not optional extras. A design that has no controls or logging section is describing something the framework would consider incomplete.

## §1.1.2 — Multi-agent patterns

Three patterns: **sequential** (each agent's output feeds the next), **supervisor** (a coordinator calls specialists as tools), and **swarm** (agents work concurrently and hand off). The framework notes no single correct architecture and that well-defined tasks suit sequential designs while open-ended ones may suit swarms.

**Engineering effect:** splitting work across agents lets each agent's tools and permissions be scoped separately. A review should check whether that benefit was actually taken, or whether every agent in the system has the same broad tool set.

## §1.1.3 — Action-space vs autonomy

| Dial | Set by | Ranges from → to |
|---|---|---|
| **Action-space** | Tools and the permissions on them | Sandbox only → internal systems → external systems; read → write; a few defined tools → computer-use (anything a human can do on screen) |
| **Autonomy** | Instructions and human involvement | Detailed SOP → own judgement; and *agent proposes, human operates* → *agent and human collaborate* → *agent operates, human approves* → *agent operates, human observes* |

**Engineering effect:** state both dials explicitly in the design, using the framework's four human-involvement levels by name. Computer-use agents deserve explicit call-out: the framework notes they significantly increase what the agent can access and do because they do not depend on defined tools.

See [layer 03](../../../layers/03-architecture-and-bounding.md).

## §1.2.1 — Sources of risk

Agents inherit traditional software vulnerabilities (e.g. SQL injection) and LLM risks (hallucination, bias, data leakage, prompt injection), but these surface through new components:

- **Planning** — a plan that can't achieve the task, contradicts the user's intent, or drifts from an earlier plan.
- **Tools** — calling non-existent tools, the wrong tool, the right tool with wrong input, or in a biased way; injection via tool outputs leading to exfiltration.
- **Protocols** — poorly deployed or compromised protocol endpoints, e.g. an untrusted MCP server that exfiltrates data.

## §1.2.2 — Types of harm

Five outcome types to use as the impact vocabulary in risk assessments and test plans: **erroneous actions**, **unauthorised actions** (outside permitted scope, including skipping a required escalation), **biased or unfair actions**, **data breaches** (exposure *or wrongful modification*), and **disruption to connected systems**.

## §1.2.3 — Systemic and multi-agent risks (new in v1.5)

- **Speed and volume** — agents act faster than real-time oversight can catch; requiring constant human approval invites automation bias and alert fatigue.
- **Cascading effects** — an early error (e.g. a hallucinated figure) propagates into downstream actions.
- **Shared context** — multi-agent systems pass context and memory between agents, raising the chance that sensitive data is logged, handed to a less secure agent, or exposed through injection.
- **Agent sprawl** — uncontrolled proliferation without central management.
- **Collaborative failures** — miscoordination, conflict between agents optimising different goals, and collusion-like convergence.
- **Emergent behaviour** — outcomes not predictable from testing agents individually; harder still across organisational boundaries without white-box access.

**Engineering effect:** each of these maps to a control elsewhere — rate limits and circuit breakers ([layer 05](../../../layers/05-technical-controls.md)), validation between steps ([layer 03](../../../layers/03-architecture-and-bounding.md)), limited shared memory, a central agent registry ([layer 04](../../../layers/04-identity-and-authorisation.md)), and system-level tests ([layer 07](../../../layers/07-testing-and-evaluation.md)). A multi-agent design that addresses none of them has not engaged with §1.2.3.
