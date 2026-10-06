# Checklist — Adding a Tool, API, MCP Server, Data Source or Computer-Use Access

> ⚠ **Reference material only — not legal or regulatory advice.** See [DISCLAIMER.md](https://github.com/AltByteSG/imda-ai-governance-skill/blob/main/DISCLAIMER.md). Verify against the official IMDA publication and involve your risk and compliance owners.

Use whenever an agent gains a new capability. A new tool changes the agent's action-space `[MGF §1.1.3]`, so it is also a change-review trigger — run [`change-review.md`](change-review.md) alongside this for deployed agents.

## 1. Does the agent need it?

- [ ] The task requires it; a narrower tool or curated data source wouldn't do `[MGF §2.1.2]` (the framework's example: a coding assistant with curated documentation may not need broad web search).
- [ ] Should it go to this agent, or a separate narrower agent?

## 2. Classify the capability

- [ ] **System reached:** sandbox / internal / external `[MGF §1.1.3]`.
- [ ] **Read or write.** If write: what can it change, and is that reversible?
- [ ] **Data exposed:** sensitive or personal data returned to the agent? Minimise fields.
- [ ] **Untrusted content:** does its output include content outsiders can influence (web, email, documents, third-party API text)? If yes, it's a new taint source — update the threat model ([layer 02](../layers/02-use-case-and-risk.md#threat-modelling)).
- [ ] **Re-tier:** does this capability raise the agent's tier? An agent's tier follows its highest-impact action.

## 3. Bound it ([layer 03](../layers/03-architecture-and-bounding.md), [layer 04](../layers/04-identity-and-authorisation.md), [layer 05](../layers/05-technical-controls.md))

- [ ] Strict input schema; server-side validation `[MGF §2.3.1]`.
- [ ] Narrow operation (`archive_ticket(id)` not `run_query(sql)`).
- [ ] Least-privilege scope via the agent's own identity; ≤ delegating user's permissions; enforced at the resource.
- [ ] No write access to sensitive tables unless strictly required `[MGF §2.3.1]`.
- [ ] Hard limits on consequential parameters; rate limit to protect the connected system.
- [ ] Added to the approval matrix at the right level ([layer 06](../layers/06-human-oversight.md)).
- [ ] Credentials injected by the runtime, never in prompt or memory.

## 4. MCP servers specifically

- [ ] Server is on, or added through review to, the allowlist `[MGF §2.3.1]`.
- [ ] Provenance known: who maintains it, how it's updated. A third-party server is a third party — run [`third-party-agent.md`](third-party-agent.md) section 3.
- [ ] Version pinned; tool descriptions reviewed (they act as instructions to your agent) and re-reviewed on update.
- [ ] Routed through the MCP gateway if one exists; traffic logged; sensitive-data filtering applied `[MGF §2.3.1]`.
- [ ] Code execution offered by the server is sandboxed.
- [ ] Remote server authenticates with scoped, short-lived credentials.

## 5. Computer-use or browser access

- [ ] Treated as high action-space by default `[MGF §1.1.3]`.
- [ ] Dedicated VM or browser profile; no personal sessions or stored credentials.
- [ ] Site allowlist; navigation to arbitrary URLs blocked (the framework's computer-use sandbox found agents following attacker-supplied URLs).
- [ ] User takes over for sign-in and secrets `[MGF §2.3.1]`.
- [ ] Step-level screenshots or action logs.

## 6. Test it ([layer 07](../layers/07-testing-and-evaluation.md))

- [ ] Tool-calling tests: right tool, inputs, order; no misuse.
- [ ] Bounds tests: attempt out-of-scope and over-limit calls; confirm they're blocked.
- [ ] Injection tests through the new tool's output if it returns untrusted content.
- [ ] Robustness: timeouts, errors, malformed responses.

## 7. Monitor and disclose

- [ ] Tool calls appear in traces with arguments and policy decision ([layer 08](../layers/08-monitoring-and-operations.md)).
- [ ] Alerts for denied calls, failure loops, volume spikes.
- [ ] Agent card, registry entry and capability statement for users updated ([layer 09](../layers/09-end-user-transparency.md)).
