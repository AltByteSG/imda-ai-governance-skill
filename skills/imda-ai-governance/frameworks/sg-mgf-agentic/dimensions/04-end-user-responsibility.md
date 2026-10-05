# §2.4 — Enable End-User Responsibility

> ⚠ **Reference material only — not legal or regulatory advice.** See [DISCLAIMER.md](../../../../../DISCLAIMER.md). Verify against the official IMDA publication and involve your risk and compliance owners.

Dimension 4 places part of trustworthy deployment on end users, and makes it the organisation's job to equip them: **transparency** for everyone, plus **education** for people who integrate agents into their work.

## §2.4 — Baseline for all users

**Expectation:**

- **Transparency** — users are informed of the agent's capabilities (scope of access to the user's data, actions it can take) and the contact points to escalate to if it malfunctions.
- **Education** — users are educated on proper use and oversight (range of actions, common failure modes such as hallucination, data usage policies) and on the potential **loss of tradecraft** as agents take over functions.

## §2.4.1 — Two user archetypes

| Archetype | Typical agents | Focus |
|---|---|---|
| **Users who interact with agents** | Customer service, sales, HR agents acting for the organisation — mostly external-facing | Transparency |
| **Users who integrate agents into their work** | Coding assistants, enterprise workflow automation acting for the user — mostly internal | Transparency plus education and training |

## §2.4.2 — Users who interact with agents

**Expectation:** share information covering:

- **The user's responsibilities** — e.g. double-check information the agent provides. Where appropriate, let users set their own approval thresholds and boundaries beyond organisation-defined limits.
- **Interaction** — declare in the user interface, **at the point of interaction**, that the user is dealing with an agent, *"rather than writing it only in separate documentation."*
- **Range of actions and decisions** the agent is authorised to perform and make.
- **Data** — how user data is collected, stored and used by the agent in line with the organisation's privacy policies, and **explicit consent** where necessary.
- **Human accountability and escalation** — the human contact points responsible for the agent, for malfunctions or disagreement with a decision.

**Engineering effect:** these are UI and content requirements. Each one needs a place in the interface or the conversation, not just in a help-centre page.

**Evidence:** screenshots or copy for the agent disclosure, the capability statement ("can / cannot do"), the data notice, and the escalation path — and a test that the disclosure renders on every channel the agent runs on (web, app, Slack, Teams, voice). See [layer 09](../../../layers/09-end-user-transparency.md).

## §2.4.3 — Users who integrate agents into their work

**Expectation:** in addition to the above, education and training on:

- **Foundational knowledge** — relevant use cases and where agent use should be restricted (e.g. not for confidential data); how to instruct agents; the agent's range of actions and potential impact.
- **Effective oversight** — common failure modes (hallucinations, loops after errors); ongoing support and refreshers; **feedback loops** so overrides and wrong actions are reported and used to improve the agent.
- **Tradecraft and business continuity** (new in v1.5) — as agents take over entry-level tasks, skills can degrade; users may no longer be able to perform critical processes manually when agents fail or are unavailable. Identify each job's core capabilities and give enough training and exposure to retain them.

**Engineering effect:** two things land on the build. First, an in-product way to report a bad action or override, wired to somewhere that gets triaged. Second, a **manual fallback path** for any business-critical process the agent performs — documented and periodically exercised — because "turn the agent off" is only a safe intervention if the work can continue without it.

**Evidence:** the feedback / override reporting path and its triage owner; the documented manual fallback for each critical process; onboarding material that covers restricted uses and failure modes.
