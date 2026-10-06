# §2.3 — Implement Technical Controls and Processes

> ⚠ **Reference material only — not legal or regulatory advice.** See [DISCLAIMER.md](https://github.com/AltByteSG/imda-ai-governance-skill/blob/main/DISCLAIMER.md). Verify against the official IMDA publication and involve your risk and compliance owners.
>
> **How to read this file:** the expectation paragraphs restate the framework, with its section. The **Engineering effect** and **Evidence** paragraphs are this skill's interpretation — treat them as `[Practice]`, not as IMDA requirements.

Dimension 3 is where most engineering work sits. The framework structures it across the lifecycle: controls during design and development, testing before deployment, gradual rollout with monitoring when deploying, and change management throughout `[MGF §2.3]`.

## §2.3.1 — During design and development, use technical controls

### Control the agent-specific surface, on top of baseline controls

**Expectation:** in addition to baseline software and LLM controls, add controls for new agentic components (planning, reasoning, tools), the larger attack surface and new protocols, and multi-agent interactions.

### Choose the right kind of control

**Expectation (new in v1.5):**

- **Prefer structural, rule-based controls** that operate at the system level through predefined logic, *"especially for higher-risk actions"* — e.g. block a tool at the tool layer or allow it read-only, rather than instructing the agent not to use it; build a required sequence into the workflow rather than prompting the agent to follow it.
- **Prompt-layer safeguards** tend to be inconsistently defined across users, unlike system-level safeguards that can be consistently enforced.
- **Model-based safeguards** are appropriate where risks are hard to define with fixed rules, e.g. harmful-content detection.
- **Runtime controls** — monitoring and intervening during execution, such as rate limits on tool use and validation of inputs and responses before they are acted on — because design-time controls won't catch everything.

**Evidence:** a controls inventory stating, for each control, its type (structural / model-based / prompt-layer / runtime) and the risk it addresses. See [layer 05](../../../layers/05-technical-controls.md).

### Sample controls by component

The framework's illustrative list (it points to CSA's Addendum and GovTech's ARC for comprehensive catalogues):

| Component | Sample controls |
|---|---|
| **Planning** | Prompt the agent to reflect on whether its plan adheres to instructions; have it summarise its understanding and ask for clarification before proceeding; log plan and reasoning for the user to verify |
| **Tools** | Strict input formats; least privilege enforced through robust authentication and authorisation; no write access to sensitive database tables unless strictly required; **hand control to the user for entering sensitive data** such as passwords and API keys |
| **Protocols** | Use standardised protocols where applicable (e.g. agentic commerce protocols for financial transactions); for MCP, **allowlist trusted servers** and **sandbox code execution** |
| **Multi-agent** | Communicate through **structured schemas** (typed function calls) rather than free text; **limit shared memory** between agents |

### MCP as a governance layer

**Expectation:** because MCP sits between the agent and enterprise systems, it can act as a governance layer — filtering sensitive data, logging all agent-to-system interactions, allowlisting trusted servers.

**Evidence:** an MCP gateway or equivalent choke point, with the allowlist and logging configuration.

## §2.3.2 — Before deploying, test agents

**Expectation:** existing software and LLM testing still applies (the framework points to IMDA's Starter Kit for Testing of LLM-based Applications), adapted for agents:

- **Test for new risks:** overall **task execution**; **policy compliance** (follows SOPs, routes for human approval when required); **tool calling** (right tools, right permissions, right inputs, right order); **robustness** to errors and edge cases.
- **Test entire workflows**, including reasoning and tool calls, not just final outputs.
- **Test agents individually and together**, including emergent behaviours and the effect of one compromised agent on others.
- **Test in real or realistic environments** that mirror production (tool integrations, external APIs, sandboxes), calibrated against the risk of giving an untested agent real-world reach.
- **Test repeatedly and across varied datasets** — behaviour is stochastic; run at scale to surface low-probability, high-impact behaviours; re-run the same inputs (and minor perturbations) to check stability.
- **Evaluate at scale** with methods suited to each part — deterministic checks for structured tool calls, LLM or human evaluation for unstructured reasoning — while still evaluating the trajectory holistically, often with LLM-as-judge plus human review.

**Evidence:** the eval suite and its results, with run counts; tool-call assertions; policy and approval-routing tests; multi-agent tests; the environment description. See [layer 07](../../../layers/07-testing-and-evaluation.md) and [`checklists/pre-deployment.md`](../../../checklists/pre-deployment.md).

## §2.3.3 — When deploying, continuously monitor and test

### Gradual deployment

**Expectation:** roll out gradually to control exposure, by **users** (trained or experienced first), **tools and protocols** (e.g. allowlisted MCP servers first), and **systems** (lower-risk internal systems first).

**Evidence:** the rollout plan with stages and the criteria for moving between them.

### Continuous testing and monitoring

**Expectation:** monitor and log post-deployment, with reporting and failsafe mechanisms, so the organisation can **intervene in real time** (stop the workflow and escalate on detected failure, e.g. attempted unauthorised access), **debug** (trace every step and agent-to-agent interaction) and **audit at regular intervals**. Key considerations:

- **What to log** — derived from monitoring objectives; prioritise high-risk activities such as database updates and financial transactions.
- **Monitor on multiple layers** — user-agent interaction, agent-tool invocation, model reasoning.
- **Define alert thresholds** — programmatic thresholds (unauthorised access, too many repeated tool calls in a window), anomaly detection, agents monitoring agents.
- **Define the intervention per alert type** — proportionate human review; low-priority alerts reviewed on schedule; high-priority alerts pause the agent until reviewed; termination and fallback for catastrophic malfunction or compromise.
- **Human review** to catch emergent behaviour not previously accounted for.
- **Integrate with observability platforms**, including standards like OpenTelemetry.
- **Log immutability** — problematic trajectories and failures cannot be deleted.
- **Feedback loops** from monitoring into training data and evaluations.
- **Keep testing after deployment** to catch model drift and environmental change.

**Evidence:** the logging schema; the alert catalogue with an intervention per alert; retention and immutability settings; a post-deployment eval schedule. See [layer 08](../../../layers/08-monitoring-and-operations.md).

### Robust change management (new in v1.5)

**Expectation:**

- **Define triggers for change review** — technical (model updates, tool modifications), environmental (domain shifts, business context changes), performance (anomalous behaviour, degraded performance), regulatory (changes in compliance requirements).
- **Categorise changes by risk** — minor changes such as prompt refinements get lighter review; material changes such as model updates or autonomy adjustments get full governance review; critical changes affecting high-stakes decisions may mandate immediate re-assessment of risk.

**Evidence:** the change-category table and the review each category requires; version control over prompts, tool definitions and model pins. See [`checklists/change-review.md`](../../../checklists/change-review.md).
