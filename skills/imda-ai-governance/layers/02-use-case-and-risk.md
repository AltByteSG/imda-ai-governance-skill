# Layer 02 — Use Case Suitability and Risk Assessment

> ⚠ **Reference material only — not legal or regulatory advice.** See [DISCLAIMER.md](https://github.com/AltByteSG/imda-ai-governance-skill/blob/main/DISCLAIMER.md). Verify against the official IMDA publication and involve your risk and compliance owners.

Decide whether to build an agent at all, how risky it is, and how risky it is allowed to be. Framework basis: `[MGF §1.2]`, `[MGF §2.1.1]`.

## First question: does this need an agent?

`[MGF §2.1.1]` notes some use cases are better served by deterministic workflows. `[Practice]` Ask, in order:

1. Are all the steps known in advance? → Build a workflow; call a model at the steps that need language understanding.
2. Is the branching known but the content variable? → Workflow with model-driven classification at branch points.
3. Does the system genuinely need to choose its own steps and tools? → Agent, and continue with this layer.

Record the answer. "We considered a workflow and rejected it because…" is what a reviewer wants to see.

## Assess impact and likelihood

`[MGF §2.1.1]` gives the factors. `[Practice]` Score each on a simple low / medium / high scale and keep the reasoning next to the score:

| Factor | Low | High |
|---|---|---|
| **Domain error tolerance** | Internal summaries, drafts | Payments, healthcare, legal, hiring, credit, safety |
| **Business processes affected** | One non-critical process | Many or critical processes |
| **Sensitive data access** | Public data only | Personal, financial, health, confidential; **persistent memory across sessions** raises it |
| **External system access** | Sandbox / internal only | Third-party APIs, outbound messages, the open web |
| **Action scope** | Read-only; few defined tools | Write access; many tools; computer-use |
| **Reversibility** | Trivially undone | Payments, deletions, external communications, contracts |
| **Autonomy** | Fixed SOP; human approves each step | Own judgement; human observes after the fact |
| **Task complexity** | Single extraction | Multi-step reasoning against nuanced policy |
| **Untrusted input exposure** | Curated internal corpus | Web, email, user uploads, other organisations' agents |
| **Third-party provision** | Built and run in-house | Vendor agent with limited visibility |
| **System complexity** | Single agent, sequential | Multiple agents, autonomous handoffs, feedback loops |

The first six are **impact**; the last five are **likelihood** `[MGF §2.1.1]`.

## Tiering

The framework does not prescribe tiers. `[Practice]` A three-tier model, consistent with the framework's case studies (Dayos, MSD), keeps the rest of the skill calibrated:

| Tier | Typical profile | What it implies downstream |
|---|---|---|
| **Low** | Read-only or easily reversible actions; no sensitive data; internal; SOP-driven | Sampled after-the-fact review; standard eval suite; can roll out broadly after a pilot |
| **Medium** | Writes to internal systems; some sensitive data; partially reversible; some judgement | Human approval before writes that matter; full eval suite including policy and tool-call tests; staged rollout; real-time alerts |
| **High** | Irreversible or external actions; sensitive data at scale; high-stakes domain; high autonomy or complexity | Approval on every high-stakes action with written justification; red-teaming; multi-agent tests if applicable; small pilot with experienced users; pause-on-alert; executive risk acceptance — or **don't automate the action yet** |

**Rule of thumb:** the tier is set by the **highest-impact action** the agent can take, not the typical one. An agent that mostly reads but can issue refunds is tiered by the refunds. Split it into two agents if you want the reader to be low-tier.

Record the tier in `.ai-governance.json` (`riskTier`) for single-agent projects, and in each agent's card for multi-agent systems.

## Threat modelling

`[MGF §2.1.1]` recommends threat modelling (memory poisoning, tool misuse, privilege compromise) and taint tracing, pointing to CSA's Addendum. `[Practice]` For each agent:

1. **List untrusted sources** — anything the agent reads that an outsider can influence: web pages, emails, uploaded documents, tickets, tool outputs, MCP server responses, other agents' messages, and its own long-term memory if anyone else can write to it.
2. **List consequential sinks** — every write-capable tool, every outbound channel, every place data leaves the trust boundary.
3. **Trace taint** — for each source, which sinks can it reach in one or more steps? Every source → sink path is an injection path.
4. **Break or guard each path** — remove the tool, require approval on it, separate the reading agent from the acting agent, constrain the action's parameters, or filter at the boundary.

The classic high-risk shape is an agent that **processes untrusted input**, **has access to sensitive data or systems**, and **can change state or communicate externally**, all in the same session. `[Practice]` Break at least one leg by design, or put a human approval on the session — the approach set out in Meta's *Agents Rule of Two*, which the framework lists in Annex A.

Update the threat model when tools, data sources or agents change ([layer 08](08-monitoring-and-operations.md#change-management)).

## Map harms to tests

Use the framework's five harm types `[MGF §1.2.2]` — erroneous, unauthorised, biased or unfair, data breach, disruption to connected systems — as the columns of the risk register, and make sure each high-rated cell has at least one test in [layer 07](07-testing-and-evaluation.md) and one monitor in [layer 08](08-monitoring-and-operations.md).

## Multi-agent systems

For systems of agents, add the `[MGF §1.2.3]` risks to the register explicitly: cascading errors between steps, conflicting objectives between agents, sensitive data spreading through shared context, sprawl, and emergent behaviour. Each needs an owner and a control.

## Model-level threats

Agent threat modelling above focuses on tools and taint. The model and its data have their own attack surface. The GenAI framework calls for input filters against unsafe prompts and for forensics able to identify malicious code within models, and points to MITRE ATLAS for threat modelling `[MGF-GenAI Security, p.22]`. `[Practice]` ATLAS also covers data poisoning, model inversion and extraction; add a row for each that applies to your threat model:

| Threat | Applies when | Typical control |
|---|---|---|
| **Data / RAG poisoning** | Anyone outside the team can influence fine-tuning data or the retrieval corpus | Curated sources, ingestion scanning, trust-separated indexes ([layer 10](10-data-and-grounding.md#poisoning-of-rag-and-fine-tuning-data)) |
| **Model extraction** | You expose a fine-tuned or proprietary model to many users | Rate limits and quotas per identity; monitor for systematic querying |
| **Model inversion / training-data leakage** | The model was fine-tuned on personal or confidential data | Don't fine-tune on it ([layer 10](10-data-and-grounding.md#personal-data-in-datasets-and-indexes)); output filters; memorisation tests |
| **Malicious code in downloaded models** | You load third-party weights, tokenisers or model code | Safe serialisation formats, scanning, pinned checksums ([layer 05](05-technical-controls.md#model-supply-chain)) |
| **Prompt attacks / jailbreaks** | Any user-facing model | Input and output filters ([layer 05](05-technical-controls.md#genai-baseline-safety)); red teaming ([layer 07](07-testing-and-evaluation.md#red-teaming)) |

The framework points to **MITRE ATLAS** as a threat-modelling reference for AI systems `[MGF-GenAI Security, p.22]`. `[Practice]` Use its tactics and techniques as a prompt list when reviewing the threat model, rather than as a compliance matrix. Framework notes: [`frameworks/sg-mgf-genai/dimensions/06-security.md`](../frameworks/sg-mgf-genai/dimensions/06-security.md).
