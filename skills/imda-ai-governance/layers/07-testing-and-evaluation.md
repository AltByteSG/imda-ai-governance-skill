# Layer 07 — Testing and Evaluation

> ⚠ **Reference material only — not legal or regulatory advice.** See [DISCLAIMER.md](../../../DISCLAIMER.md). Verify against the official IMDA publication and involve your risk and compliance owners.

How to show, before launch and after every material change, that the agent does the task, follows policy, uses tools correctly, and stays inside its bounds. Framework basis: `[MGF §2.3.2]`, with continuous testing in `[MGF §2.3.3]`. The framework builds on IMDA's *Starter Kit for Testing of LLM-based Applications for Safety and Reliability* for baseline LLM testing.

## What to test

`[MGF §2.3.2]` names four new dimensions. `[Practice]` Each should have its own named suite:

| Suite | Question | Typical assertions |
|---|---|---|
| **Task execution** | Does the agent complete the task correctly end to end? | Final state matches expected; outputs correct; no extraneous side effects |
| **Policy compliance** | Does it follow the SOP and route for approval when required? | Required steps present and in order; approval requested for every action in the matrix; no action executed without approval; refusal on out-of-policy requests |
| **Tool calling** | Right tool, right permissions, right inputs, right order? | Tool sequence matches; arguments valid and minimal; no calls to unlisted tools; no hallucinated tools |
| **Robustness** | How does it behave on errors and edge cases? | Tool timeouts, malformed responses, empty results, contradictory data, rate-limit errors → safe stop or correct retry, not loops or invention |

Add from the threat model ([layer 02](02-use-case-and-risk.md#threat-modelling)):

| Suite | Question |
|---|---|
| **Adversarial / injection** | Can content in each untrusted source make the agent call a write tool, exfiltrate data, or skip approval? Test each source → sink path. |
| **Bounds and controls** | Do the limits actually hold? Attempt disallowed actions directly (the OpenClaw advice: try what should be blocked). Over-limit amounts, unlisted recipients, out-of-scope records, unknown tools. |
| **Fail-closed** | Approval service down; policy missing for an action; kill switch triggered mid-run. |
| **Fairness** | For agents whose actions affect people differently (hiring, credit, support prioritisation, procurement), does outcome or treatment differ across groups? Biased actions are a named harm `[MGF §1.2.2]`. |

### Access-boundary tests

`[Practice]` For any agent serving more than one user or role, follow the CDL x Knovel method from the framework: a **matrix of user accounts × data domains**; multi-turn conversations that drift towards out-of-scope domains; comparison of restricted users' outputs with authorised users'; and attempts to get the agent to "helpfully" complete partially redacted data or prompts.

## How to test

`[MGF §2.3.2]`:

- **Whole workflows, not just final outputs.** Assert on the trajectory — plan, every tool call, every intermediate result.
- **Individually and together.** In multi-agent systems, test the system: miscoordination, conflicting goals, and what happens to the others when one agent is compromised (inject a malicious message from agent A and check B and C).
- **Realistic environments.** Mirror production integrations, APIs and sandboxes — but balance realism against giving an untested agent real-world reach. `[Practice]` Use production-like sandboxes and recorded or mocked external services for anything irreversible.
- **Repeatedly, across varied data.** Agent behaviour is stochastic. `[Practice]` Run each scenario multiple times (state the count — e.g. 5–20 depending on tier and cost) and report pass rate, not a single pass. Include perturbations (rephrasings, reordered inputs, noisy data) to check stability. Generate datasets that cover the conditions the agent will meet, including rare high-impact ones.
- **Mixed evaluators.** Deterministic assertions for structured tool calls; LLM-as-judge or human review for unstructured reasoning; still review whole trajectories holistically. `[Practice]` Calibrate any LLM judge against human labels on a sample before trusting it.
- **Log reasoning at each step during testing.** The framework's computer-use case found a data-minimisation failure only by reading step-level reasoning.
- **Humans in the loop while testing broad-action-space agents** such as computer-use agents.

## Pass criteria and the release gate

`[Practice]` Set thresholds **before** running, per suite and tier — e.g. policy-compliance and bounds suites must pass every run for medium and high tiers (a single unapproved irreversible action is a release blocker), while task-execution can have a target success rate. Record results with the model version, prompt version and tool versions they were run against; results don't transfer across versions. See [`checklists/pre-deployment.md`](../checklists/pre-deployment.md).

## Red teaming

`[MGF §2.2.1]` gives cybersecurity teams responsibility for regular red teaming. `[Practice]` For high-tier agents, red-team before first production exposure and after material changes, covering injection through every untrusted source, privilege escalation through delegation, memory poisoning, and malicious or compromised MCP servers. GovTech red-teamed its MCP guardrails before widening rollout.

## After deployment

`[MGF §2.3.3]`: keep testing post-deployment to catch model drift and environmental change. `[Practice]`:

- Re-run the regression suite on a schedule and on every change trigger ([layer 08](08-monitoring-and-operations.md#change-management)).
- Turn production incidents and human overrides into new test cases — the feedback loop `[MGF §2.3.3, §2.4.3]`.
- Treat a provider's silent model update as a change: re-run evals when the model behind an API changes, if you can detect it, and pin versions where you can.
