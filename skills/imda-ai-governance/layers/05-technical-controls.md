# Layer 05 — Technical Controls

> ⚠ **Reference material only — not legal or regulatory advice.** See [DISCLAIMER.md](../../../DISCLAIMER.md). Verify against the official IMDA publication and involve your risk and compliance owners.

The controls that sit around the model at design time and run time. Framework basis: `[MGF §2.1.2]`, `[MGF §2.3.1]`. For comprehensive catalogues the framework points to CSA's *Draft Addendum on Securing Agentic AI* and GovTech's *Agentic Risk & Capability Framework*.

## Pick the strongest control type the risk allows

`[MGF §2.3.1]` distinguishes control types and prefers deterministic ones for higher-risk actions. `[Practice]` Rank them and use the strongest that fits:

| Rank | Type | Example | Reliability |
|---|---|---|---|
| 1 | **Architectural** — capability not present | Agent has no delete tool; sensitive values never enter context | Cannot be bypassed by the model |
| 2 | **Structural / rule-based** — enforced by the system | Tool-layer allowlist; read-only scope; schema validation; transaction ceiling; workflow ordering in code | Deterministic; consistent for all users |
| 3 | **Human approval** — enforced gate | Tool call blocks until an approver signs | Strong if oversight stays effective ([layer 06](06-human-oversight.md)) |
| 4 | **Model-based** — classifiers, judges | Harmful-content filter; LLM judge on output faithfulness | Probabilistic; right where rules can't express the risk |
| 5 | **Prompt-layer** — instructions | "Do not email external domains" | Weakest; may be bypassed or "forgotten" (OpenClaw case, `[MGF §2]`); inconsistently defined across users `[MGF §2.3.1]` |

**Review rule:** for every risk rated medium or high in [layer 02](02-use-case-and-risk.md), the primary control should be rank 1–3. A rank 4–5 control on its own is acceptable only where the framework allows it — risks hard to express in rules — and should be layered with monitoring or human review `[MGF §2.1.2]`.

Keep a **controls inventory** per agent (the agent card has a section for it): control, type, risk addressed, where enforced, how tested.

## Planning controls

`[MGF §2.3.1]` sample controls, with `[Practice]` notes:

- **Self-check against instructions** before executing a plan — useful, but model-based; don't rely on it for high-risk steps.
- **Summarise understanding and ask for clarification** before proceeding on ambiguous goals. Semantic misalignment is a named risk source `[MGF §1.2.1]`.
- **Log plan and reasoning** where the user can see and verify it. Show the plan before execution for medium and high tiers; let the user edit it `[MGF §2.2.2]`.
- **Detect plan drift** `[Practice]` — compare executed steps against the approved plan; a step outside it triggers re-approval.

## Tool controls

`[MGF §2.3.1]`:

- **Strict input formats** — typed schemas, enums for categorical arguments, length and range limits, server-side validation. The tool rejects malformed calls; it doesn't "do its best".
- **Least privilege enforced through authentication and authorisation** — see [layer 04](04-identity-and-authorisation.md).
- **No write access to sensitive tables unless strictly required.**
- **User takeover for sensitive inputs** (passwords, API keys).

`[Practice]` additions:

- **Separate read tools from write tools** so they can be scoped and approved separately.
- **Make destructive tools explicit and narrow.** `delete_draft(id)` beats `run_sql(query)`.
- **Return minimal data** from read tools — the fields needed, not the whole record.
- **Treat tool outputs as untrusted input.** Content returned by a tool (a web page, an email body, an API error) can carry instructions. Don't let it reach a write tool without passing a boundary ([layer 03](03-architecture-and-bounding.md#functional-boundaries-and-multi-agent-topology)).

## Protocol and MCP controls

`[MGF §2.3.1]`:

- **Standardised protocols** where applicable — e.g. agentic-commerce protocols for financial transactions rather than a bespoke "pay" tool.
- **MCP server allowlist** — the agent can talk only to approved servers.
- **Sandbox code execution.**
- **MCP as a governance layer** — filter sensitive data, log all agent-to-system interactions, enforce the allowlist at a gateway.

`[Practice]`:

- **Pin MCP server versions** and review tool-description changes; a changed description is changed instructions to your agent.
- **First-use trust** for new servers (the Tencent case study gates newly connected servers behind explicit trust).
- **Prefer a central MCP gateway** over agents connecting directly, so allowlisting, auth, logging and data filtering live in one place (the GovTech case study moved to a managed gateway).
- **Remote MCP servers authenticate with OAuth-based authorisation** where supported, not static keys.

## Multi-agent controls

`[MGF §2.3.1]`:

- **Structured schemas between agents** — typed function calls rather than free text, to stop instructions leaking from one agent to another.
- **Limit shared memory** between agents.

`[Practice]`: validate every inter-agent message against its schema at the receiving side; give each agent its own identity so cross-agent calls are authorised and logged ([layer 04](04-identity-and-authorisation.md)); bound handoff depth and fan-out.

## Runtime controls

`[MGF §2.3.1]`: monitor and intervene during execution — **rate limits** on tool use, **input and output validation** before results are acted on.

`[Practice]`:

- Per-run budgets: max steps, max tool calls, max tokens, max wall-clock, max spend.
- Per-tool rate limits and circuit breakers that trip on repeated failure (and alert — see [layer 08](08-monitoring-and-operations.md)).
- Policy engine at the tool boundary that evaluates each call against the agent's policy (who, what tool, what arguments, what tier) and returns allow / ask / deny. **Unknown actions default to deny or ask, never allow** `[MGF §2.2.2]`.
- Re-escalate when a previously allowed pattern turns suspicious (the Tencent pattern): allowlists match intent, not just prefix.

## Output and reflection controls

The framework's case studies show model-based verification used well: reflection loops with LLM-judge and metric checks and a **hard iteration cap that terminates the run** (Cyber Sierra), and built-in verification steps with retry limits (Ant International). `[Practice]` If you use reflection, cap it and fail closed — an unbounded "try again" loop is a runtime risk in itself.

## Fix data problems deterministically

`[Practice]` When an agent errs because its sources are stale, duplicated or ambiguous, fix the source structure (versioning, expiry metadata, a curated index) rather than adding prompt instructions. The Cyber Sierra case study replaced "be careful about expired documents" with a context graph that only surfaces current documents.

## GenAI baseline safety

The model-level controls underneath every agent, and the main controls for a generative feature that takes no actions. The GenAI framework lists them as baseline safety practices `[MGF-GenAI Trusted Development, p.13]`. They are mostly rank 4 (model-based) in the table above, so they supplement — never replace — architectural and structural controls on actions.

- **Ground to reduce hallucination.** RAG and few-shot examples are named for this `[MGF-GenAI Trusted Development, p.13]`. `[Practice]` Retrieve from a curated, versioned corpus ([layer 10](10-data-and-grounding.md)); return citations with answers; when retrieval finds nothing relevant, answer "I don't know" or escalate rather than generate from the base model; test faithfulness to sources ([layer 07](07-testing-and-evaluation.md#benchmarks-evaluation-dimensions-and-external-assurance)).
- **Input and output filters** `[MGF-GenAI Trusted Development, p.13]`, `[MGF-GenAI Security, p.22]`. `[Practice]` Input: unsafe-prompt and injection classifiers, length limits, blocked topics for the use case. Output: harmful-content, PII and secret detectors, and schema validation for structured output. Log every filter decision; tune thresholds on your own eval set, not the vendor's defaults.
- **Safety fine-tuning when you fine-tune.** Fine-tuning (including RLHF) is the framework's route to safer behaviour `[MGF-GenAI Trusted Development, p.13]`, and a task fine-tune can also erode the base model's safety behaviour. `[Practice]` Include refusal and safety examples in fine-tuning data, and re-run the safety suite on every fine-tuned checkpoint before use.

## Model supply chain

Deployers should download models from reputable platforms `[MGF-GenAI Accountability, p.8]`, and the framework calls for tools to identify malicious code within models `[MGF-GenAI Security, p.22]`. `[Practice]`:

- **Pin the exact model version** — API model id with date or version, or the weights' commit hash. No floating "latest" aliases in production config.
- **Verify integrity** — record and check checksums or signatures of weights, tokenisers and adapters at load time; fail closed on mismatch.
- **Prefer safe formats** (e.g. safetensors) over formats that execute code on load (pickle-based); scan anything else before loading, in a sandbox.
- **Allowlist sources and publishers**; mirror approved artefacts to an internal registry so production never pulls from the public internet.
- **Track models like dependencies** — in the SBOM or an equivalent inventory, with licence and the [`SYSTEM_CARD.md`](../templates/SYSTEM_CARD.md.template) linked. A model change is a change-review trigger ([layer 08](08-monitoring-and-operations.md#change-management)).
