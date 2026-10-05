# Checklist — Alignment Review of a Design, Architecture or Guideline

> ⚠ **Reference material only — not legal or regulatory advice.** See [DISCLAIMER.md](../../../DISCLAIMER.md). Verify against the official IMDA publication and involve your risk and compliance owners.

Use when asked whether something that already exists — a design doc, architecture diagram, ADR, RFC, internal engineering guideline, agent configuration, PR, or a running system — is aligned with the MGF for Agentic AI, and with the MGF for Generative AI where it applies. The output is a findings report in the shape of [`ALIGNMENT_REVIEW.md.template`](../templates/ALIGNMENT_REVIEW.md.template).

**The agentic framework is the primary bar.** Step 3 walks its four dimensions and the systemic items. The generative-AI supplement (items G.0–G.9) covers the model, data and generated-content layer underneath the agent.

**For a generative system that takes no actions**, skip the agentic dimensions. The bar is G.0–G.9 plus the items in [`new-genai-feature.md`](new-genai-feature.md), cited with an **NG** prefix (NG 3.2) so they can't be confused with this file's numbers. Where an NG item and a G item ask the same thing, score the NG item and mark the G item *Covered by NG n.n*.

Item numbers (1.1, S.5, G.3, NG 3.2) are stable: use them in the review's appendix and when citing an item in a finding.

## How to run the review

### 1. Gather the material and say what you reviewed

List every artefact read (paths, links, versions). If the review is of a design doc only, say so: findings about intent are weaker than findings about code and config. Where both exist, **check the code and config against the doc** — a mismatch is a finding in its own right, scored by the severity of whichever version is worse (a doc saying "read-only" over a tool with write scope is scored as the write scope).

Where something the design relies on is not in the material (a referenced file, an internal module the code imports, a vendor's enforcement, an external policy engine), don't guess: record the item as *Cannot determine* and list it under open questions.

### 2. Describe the system in the framework's terms

Before judging anything, write down (from the material, marking anything inferred):

- Is it agentic per `[MGF §1.1]` (it plans and chooses actions over multiple steps)? If not, say so and review against the generative supplement only. For a generative-only system, describe it as: model and source; data sources and retrieval; outputs and where they go; channels and users.
- The eight components `[MGF §1.1.1]`: model, instructions, memory, planning, tools, protocols, controls, logging — where each lives.
- Multi-agent pattern, if any `[MGF §1.1.2]`.
- **Action-space** and **autonomy** `[MGF §1.1.3]`, with the human-involvement level per significant action.
- Value-chain role(s) of the organisation `[MGF §2.2.1]`.
- Risk tier — from the material if assessed; otherwise your provisional tier using [layer 02](../layers/02-use-case-and-risk.md#tiering), clearly marked provisional. If the material states a tier you think is too low, keep theirs in the header, state your provisional tier beside it with the factor that drives the difference, and make it a finding (`[MGF §2.1.1]`). Don't silently overrule an assessed tier.

**Nobody to ask?** Reviews often run without the author present. Don't stop to ask: infer role and tier from the material, mark them *provisional*, and carry on. The questions you would have asked go under open questions.

Record the skill version (from the **Skill version** line at the top of [SKILL.md](../SKILL.md)), the framework versions you reviewed against, and each applied framework's last-verified date from its README.

If the material doesn't let you fill these in, that is the first finding: the design doesn't describe the agent well enough to govern it.

### 3. Walk the dimensions

For each item, record **Aligned / Partly aligned / Not aligned / Not applicable / Cannot determine**, with evidence, in the appendix of the review template (file and line, config key, diagram element, quote from the doc). Calibrate to the tier: a low-tier internal summariser does not need what a high-tier payment agent needs.

Where an item mixes a framework expectation with a `[Practice]` suggestion, score it on the framework part. A gap only in the `[Practice]` part makes the item *Aligned*, with the suggestion noted in the evidence column.

Items are deliberately separate: an approval that is enforced in code (2.5, aligned) can still fail open (2.9, not aligned). Score each on its own question; don't let one result carry over to the other.

#### Dimension 1 — Assess and bound ([dimension notes](../frameworks/sg-mgf-agentic/dimensions/01-assess-and-bound.md))

- **1.1** Risk assessment exists and uses impact and likelihood factors `[MGF §2.1.1]`; the deterministic-workflow alternative was considered.
- **1.2** Threat model names untrusted inputs and traces them to write-capable tools `[MGF §2.1.1]`.
- **1.3** Least-privilege tool set; functional boundaries between agents `[MGF §2.1.2]`.
- **1.4** Autonomy constrained by SOP encoded in the workflow where appropriate `[MGF §2.1.2]`.
- **1.5** Blast radius bounded: sandboxing, limits, kill switch `[MGF §2.1.2]`.
- **1.6** Limits are deterministic where risk is high; non-deterministic limits have compensating monitoring or approval `[MGF §2.1.2]`.
- **1.7** Unique, accounted-for, centrally registered agent identity; capacity recorded `[MGF §2.1.2]`.
- **1.8** Scoped, time-bound, non-transferable authorisation with explicit escalation paths; as a rule of thumb no greater than the delegating human's; delegations recorded `[MGF §2.1.2]`.
- **1.9** Residual risk named and accepted by someone with authority `[MGF §2.1.2]`.

#### Dimension 2 — Human accountability ([dimension notes](../frameworks/sg-mgf-agentic/dimensions/02-human-accountability.md))

- **2.1** Responsibilities allocated within the organisation across the agent lifecycle `[MGF §2.2.1]`; `[Practice]` concretely, named owners for use case, build, risk review, approvals and user escalation.
- **2.2** Internal capability to track agentic developments and adapt governance `[MGF §2.2.1]`.
- **2.3** Vendor and tool-host obligations covered by contract; opacity addressed or use case scoped down `[MGF §2.2.1]`.
- **2.4** Approval checkpoints defined for high-stakes, irreversible, atypical and user-defined actions `[MGF §2.2.2]`.
- **2.5** Approvals enforced through system-level controls rather than prompt-layer guardrails `[MGF §2.3.1]` (also the OpenClaw case study, [case-studies](../frameworks/sg-mgf-agentic/case-studies.md)); `[Practice]` bound to the exact action and logged.
- **2.6** Approval requests are digestible and state the risk; high-risk approvals need justification `[MGF §2.2.2]`.
- **2.7** Oversight effectiveness measured (override rate, response time, outliers) `[MGF §2.2.2]`.
- **2.8** Approvers have the needed expertise and training `[MGF §2.2.2]`.
- **2.9** Automated monitoring complements human oversight, including denying action by default when approval infrastructure fails or an action has no approval policy `[MGF §2.2.2]`.

#### Dimension 3 — Technical controls and processes ([dimension notes](../frameworks/sg-mgf-agentic/dimensions/03-technical-controls.md))

- **3.1** Structural / rule-based controls on higher-risk actions; model-based controls where rules can't express the risk `[MGF §2.3.1]`; `[Practice]` recorded in a controls inventory.
- **3.2** Planning, tool, protocol / MCP and multi-agent controls appropriate to the design `[MGF §2.3.1]`.
- **3.3** Runtime controls such as rate limits on tool use and input validation `[MGF §2.3.1]`; `[Practice]` per-run budgets.
- **3.4** Test plan covers task execution, policy compliance, tool calling, robustness; whole workflows; multi-agent level; realistic environment; repeated runs across varied datasets `[MGF §2.3.2]`.
- **3.5** Evaluation method suited to each part while still evaluating trajectories holistically `[MGF §2.3.2]`.
- **3.6** Where the agent's actions affect people, biased or unfair actions — a risk type the framework names `[MGF §1.2.2]` — are considered; `[Practice]` covered by tests or monitoring.
- **3.7** Threat model regularly updated `[MGF §2.1.1]`; `[Practice]` regular red teaming, which the framework illustrates as a cybersecurity-team responsibility `[MGF §2.2.1]`.
- **3.8** Gradual rollout plan by users, tools and systems `[MGF §2.3.3]`.
- **3.9** Logging and monitoring across user-agent, agent-tool and reasoning layers; integrated with observability; problematic trajectories cannot be deleted `[MGF §2.3.3]`.
- **3.10** Alert catalogue with an intervention per alert `[MGF §2.3.3]`.
- **3.11** Audits at regular intervals; human review for emergent behaviour; post-deployment testing; feedback loops `[MGF §2.3.3]`.
- **3.12** Change triggers and risk-categorised change review; behaviour-shaping artefacts version-controlled `[MGF §2.3, §2.3.3]`.

#### Dimension 4 — End-user responsibility ([dimension notes](../frameworks/sg-mgf-agentic/dimensions/04-end-user-responsibility.md))

- **4.1** Agent disclosed in the UI at the point of interaction `[MGF §2.4.2]`, and not presented as a human (no human name or persona) — the generative-AI framework warns against encouraging users to anthropomorphise AI `[MGF-GenAI AI for Public Good, p.29]`; `[Practice]` on every surface the agent runs on, including emails and messages it sends.
- **4.2** Capability statement: can / cannot / needs approval `[MGF §2.4.2]`.
- **4.3** Data use explained; consent where needed `[MGF §2.4.2]`.
- **4.4** Human escalation contact `[MGF §2.4.2]`.
- **4.5** User-settable limits where appropriate `[MGF §2.4.2]`.
- **4.6** For internal users: training on use cases, instructing agents, range of actions and failure modes; feedback path; skills retention when agents take over tasks `[MGF §2.4.3]`; `[Practice]` a documented manual fallback for critical processes.

#### Systemic and multi-agent ([foundations](../frameworks/sg-mgf-agentic/dimensions/00-foundations.md#123--systemic-and-multi-agent-risks-new-in-v15))

Items S.1–S.4 apply only with more than one agent; for a single agent mark them N/A. **S.5** applies to every agent.

- **S.1** Cascading errors contained by validation between steps `[MGF §1.2.3]`.
- **S.2** Conflicting objectives between agents resolved deterministically or by a human `[MGF §1.2.3]`.
- **S.3** Shared memory and context limited; structured inter-agent messages `[MGF §2.3.1]`.
- **S.4** System-level tests for emergent behaviour and a compromised agent `[MGF §2.3.2]`.
- **S.5** Speed and volume bounded: an agent acting faster or more often than a human could has throttles or circuit breakers `[MGF §1.2.3]`.

#### Generative-AI supplement ([framework notes](../frameworks/sg-mgf-genai/README.md))

The model, data and output layer under the agent. Many items overlap the agentic items above; where they do, score the agentic item and mark the supplement item *Covered by n.n*.

- **G.0** *(generative-only systems; for agents this is 1.1, 1.9 and 2.1)* Use-case risk assessment in context, a named owner, and residual risk accepted `[MGF-GenAI Trusted Development, p.13; Accountability, p.7]`.
- **G.1** Model provenance: models come from reputable sources, versions are pinned, and the split of responsibilities with the model provider is understood `[MGF-GenAI Accountability, p.7–8]`.
- **G.2** Training, fine-tuning, RAG and eval data (including ad-hoc eval sets such as a sample of past tickets) have documented sources, licence or copyright position, personal-data handling, and quality controls `[MGF-GenAI Data, p.10–11]` ([layer 10](../layers/10-data-and-grounding.md)).
- **G.3** Baseline safety controls fit the use: grounding / RAG against hallucination, input and output filters `[MGF-GenAI Trusted Development, p.13]`.
- **G.4** Disclosure exists for the system (a system card covering data, evaluations, mitigations, risks and limits, intended use, user-data protection) `[MGF-GenAI Trusted Development, p.14]` ([template](../templates/SYSTEM_CARD.md.template)).
- **G.5** Evaluation includes benchmarks and red teaming across robustness, factuality, bias and toxicity `[MGF-GenAI Trusted Development, p.14–15]`.
- **G.6** A route for outsiders to report vulnerabilities or unsafe behaviour, and a severity threshold for reporting incidents externally `[MGF-GenAI Incident Reporting, p.17]`.
- **G.7** Model-level threats in the threat model: unsafe prompts filtered, downloaded models checked for malicious code, MITRE ATLAS used as a threat reference `[MGF-GenAI Security, p.22]`; `[Practice]` data / RAG poisoning and extraction covered.
- **G.8** Generated content published beyond the person it was made for (images, audio, video, public posts and documents) is labelled, and where appropriate carries watermarks or provenance metadata `[MGF-GenAI Content Provenance, p.23–25]`. Messages the system sends to a user are disclosure, scored under 4.1.
- **G.9** *(generative-only systems; for agents this is 3.8–3.11)* Ongoing monitoring to detect malfunctions `[MGF-GenAI Incident Reporting, p.17]`; `[Practice]` logging of prompts, retrieved sources and outputs, and a staged launch.

### 4. Write findings, not a checklist dump

For each item not aligned or partly aligned, write a finding:

- **Title** — the gap in one line.
- **Severity** — `[Practice]` use the rubric below.
- **Framework reference** — `[MGF §x.y]` or `[MGF-GenAI …]` and a short paraphrase. Don't overstate: the frameworks say organisations *should consider*; frame findings as misalignment with recommended practice, not breach.
- **Items** — the checklist item numbers it covers.
- **Evidence** — what in the material shows the gap.
- **Recommendation** — the smallest change that closes it, preferring stronger control types ([layer 05](../layers/05-technical-controls.md#pick-the-strongest-control-type-the-risk-allows)). Mark it `[Practice]` if it's this skill's suggestion rather than the framework's.

**Severity rubric** `[Practice]`:

| Severity | Use when |
|---|---|
| **High** | An irreversible or high-stakes action lacks a structural control or approval; there is no way to stop the agent; the agent can exceed the delegating user's permissions; an injection path runs from untrusted input to a consequential tool; approvals fail open; or a **medium- or high-tier** system has no meaningful pre-deployment testing or no logging. For generative systems also: personal, confidential or regulated data can be retrieved or generated for people not entitled to it; unverified model artefacts are executed (pickle weights, remote code); untrusted content can steer output that is published under your name. |
| **Medium** | An expectation is partly met, or met only by prompt or intent; measurement is missing; a control exists but has a bypass that needs effort; or an expectation is not met at all but the harm is recoverable (for example no disclosure to users, or no staged rollout on a low-tier system). |
| **Low** | Documentation, naming or evidence gaps that don't hide a missing control. |
| **Conditional** | When the gap depends on material you couldn't see, give the severity it would have if the missing material doesn't close it, and say so: "High unless `workflow.py` binds the amount". |

Legal exposure the frameworks leave to law — copyright and licences, personal-data obligations — is scored by its engineering gap (no provenance record, no access control) and flagged for legal review; don't rule on the law.

**Keep it readable.**

- Order findings by severity. Lead with a one-paragraph verdict and the top three things to fix.
- Merge findings that share a root cause or a fix (one finding, several item numbers) rather than one finding per item.
- If there are more than five Low findings, list them as one-line bullets under a single "Minor gaps" finding instead of full blocks.
- A well-built system should produce a short review. The appendix carries the item-by-item detail; the findings section carries only what someone has to act on.

### 5. Be explicit about limits

State what you couldn't verify (e.g. "contract terms not reviewed", "runtime config not provided", "no eval results available"), and that the review is engineering alignment with voluntary guidance — not a legal opinion, audit, or certification. Personal-data obligations are law, not guidance: if the system handles personal data and the `personal-data-protection` skill isn't available, say that a data-protection review is still needed rather than attempting one here.
