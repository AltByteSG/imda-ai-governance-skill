# Layer 04 — Agent Identity and Authorisation

> ⚠ **Reference material only — not legal or regulatory advice.** See [DISCLAIMER.md](../../../DISCLAIMER.md). Verify against the official IMDA publication and involve your risk and compliance owners.

Who the agent is, whom it acts for, and what it is allowed to touch — enforced by the systems it calls, not by its instructions. Framework basis: `[MGF §2.1.2]` (agent identity, authorisation), `[MGF §1.2.3]` (agent sprawl). The framework acknowledges this is an evolving space with gaps in today's identity systems; the practices below are the interim baseline it describes.

## Identity: one per agent, never borrowed

`[MGF §2.1.2]` expects identities that are **unique**, **accounted for**, **differentiated by capacity**, and **catalogued and centrally managed**.

`[Practice]`:

- **Issue each agent its own workload identity** — a service principal, workload identity, client credentials, or a platform-native agent identity. Not a human's account, not a shared "ai-bot" service account used by every agent. The OpenClaw guidance is explicit about dedicated identities and credentials.
- **Make it verifiable.** Prefer credentials that are cryptographically verifiable (signed tokens, mTLS, workload identity federation) over static shared secrets.
- **Bind it to an owner** — the human, team, or supervising agent accountable for it — in the registry.
- **Sub-agents get their own identity** or a derived, narrower credential, so actions remain attributable through recursive delegation.

## Capacity: acting as itself vs acting for a user

`[MGF §2.1.2]` expects the capacity in which an agent acts to be recorded. `[Practice]`:

- When the agent acts **on behalf of a user**, propagate both identities: the user (subject) and the agent (actor). OAuth token exchange with an actor claim, or an equivalent `on_behalf_of` field, achieves this.
- When the agent acts **on its own authority** (scheduled jobs, autonomous triage), record that explicitly.
- Every audit log entry carries **agent id, user id (if any), capacity, and delegation id**. "Done by the AI" is not attributable.

## Authorisation: scoped, short-lived, non-transferable

`[MGF §2.1.2]` expects authorisations to be scoped, time- or session-bound, non-transferable and least-privilege by default, with explicit escalation paths.

`[Practice]`:

- **Narrow scopes per tool.** Read and write as separate scopes. Table-, folder-, or resource-level scoping where the platform supports it.
- **Short-lived tokens** bound to the session or task. No long-lived API keys in agent configuration where a short-lived alternative exists.
- **Non-transferable.** An agent cannot hand its token to another agent or a tool; downstream calls get their own narrower tokens.
- **Escalation is a flow, not a bigger default.** If a task needs elevated permission, the agent requests it and a human (or policy engine) grants a time-boxed elevation — logged.
- **Enforce at the resource.** The database, API or MCP server checks the scope. A tool wrapper that "promises" not to call a write endpoint, with a credential that could, is a prompt-grade control.

## Never more than the delegating human

`[MGF §2.1.2]`: a user should not be able to give an agent permissions greater than their own, and delegations should be recorded.

`[Practice]`:

- **Effective permission = agent's role permissions ∩ delegating user's permissions.** Compute it at token issuance or check it at the resource.
- **Watch for confused-deputy paths:** an agent that holds a broad service credential and answers any user's request will happily read data the requesting user can't. Test this explicitly ([layer 07](07-testing-and-evaluation.md#access-boundary-tests)).
- **Agents serving many users** (a shared assistant in a team channel) must re-evaluate permissions per request, against the requesting user — not against whoever installed the agent.
- **Record the delegation**: who delegated, which scopes, for how long.

## Central registry against sprawl

`[MGF §2.1.2]` and `[MGF §1.2.3]` call for central management of agent identities to prevent sprawl. `[Practice]` A registry entry per agent, with:

- identity, owner, purpose, tier
- tools and scopes granted
- environments it runs in
- model and version pinned
- status (pilot, production, deprecated) and last review date

The registry is where you find agents nobody owns any more — and revoke them. The [`AGENT_CARD.md`](../templates/AGENT_CARD.md.template) template can serve as a file-based registry (`agentRegistry` in `.ai-governance.json`) until the organisation has a platform one.

## Secrets the agent must not hold

`[MGF §2.3.1]`: configure the agent to let the user take over when entering sensitive data such as passwords and API keys. `[Practice]` Credentials are injected at the tool boundary by the runtime, never placed in the prompt, the agent's memory, or its logs. If a browser agent hits a login page, it hands control to the human.
