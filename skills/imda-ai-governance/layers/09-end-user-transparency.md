# Layer 09 — End-User Transparency and Enablement

> ⚠ **Reference material only — not legal or regulatory advice.** See [DISCLAIMER.md](../../../DISCLAIMER.md). Verify against the official IMDA publication and involve your risk and compliance owners.

What users see and learn, so they can use the agent responsibly and hold the organisation accountable. Framework basis: `[MGF §2.4]`, `[MGF §2.2.1]` (users' responsibilities).

## Disclose the agent at the point of interaction

`[MGF §2.4.2]`: declare upfront in the UI that users are interacting with an agent, at the point of interaction, *"rather than writing it only in separate documentation."* `[Practice]`:

- Visible label on every surface the agent runs on — web, app, email signatures, chat platforms (Slack, Teams, WhatsApp), voice greetings. The Workday case study discloses in Slack and Teams, not only on its own UI.
- Messages and actions the agent takes on a user's behalf towards third parties (emails, tickets, calendar invites) say they were agent-generated where that matters to the recipient.
- No human-sounding persona that implies a person is on the other end.

## State what it can and cannot do

`[MGF §2.4.2]`: inform users of the range of actions and decisions the agent is authorised to make. `[Practice]` A short capability statement, linked from the agent UI:

- **Can:** the actions it takes (e.g. "reschedule your appointment", "draft a reply for you to send").
- **Cannot:** the decisions it does not make (e.g. "does not approve refunds", "does not make hiring decisions" — the Workday factsheet pattern).
- **Needs your approval for:** the checkpoints from the approval matrix that involve the user.

Keep it generated from, or reviewed against, the actual tool list and approval matrix so it doesn't drift.

## Tell users what happens to their data

`[MGF §2.4.2]`: be clear how user data is collected, stored and used by the agent, in line with privacy policies; obtain explicit consent where necessary. `[Practice]`: say whether conversations are retained, whether the agent has long-term memory of the user and how to clear it, which third parties (model providers, tools) receive data, and whether data trains models. This is also where PDPA notice and consent obligations land — they are law, and apply whatever the framework says.

## Name a human to escalate to

`[MGF §2.4.2]`: give users human contact points responsible for the agent, for malfunctions or disputed decisions. `[Practice]` A visible "talk to a person" or "report a problem" path inside the agent experience, routed to a staffed queue — and a way to contest an agent decision that affects them.

## Users' own responsibilities and limits

`[MGF §2.4.2]`: define the user's responsibilities (e.g. double-check information) and, where appropriate, let users set approval thresholds and boundaries beyond organisational limits. `[Practice]` Put user-settable limits in settings ("ask before purchases over…", "never send email without showing me"), enforce them in the policy engine ([layer 06](06-human-oversight.md)), and let users only add stricter limits, never loosen the organisation's.

## Explain recommendations in sensitive workflows

The Workday case study attaches to each recommendation the reasoning, data considered, key factors and uncertainties. `[Practice]` For recommendations that feed decisions about people (hiring, performance, credit, eligibility), show that context and make clear the decision belongs to the human `[MGF §2.2.2, §2.4.2]`.

## Training for users who work with agents

`[MGF §2.4.3]`: for internal users integrating agents into their work, layer on education. `[Practice]` Onboarding content should cover:

- **When to use it and when not to** — restricted uses such as confidential data in a given tool.
- **How to instruct it** — prompting basics for this agent.
- **What it can do and the potential impact** — the capability statement above.
- **Failure modes to watch for** — hallucination, loops after errors, outdated policy, overconfident summaries — and that the agent's explanation of its reasoning may not be faithful `[MGF §2.2.2]`.
- **How to report** an override or wrong action, and that reports are used.
- **Refreshers** when features or failure patterns change.

## Feedback path

`[MGF §2.4.3]`: enable users to report overrides and wrong actions so they improve the agent. `[Practice]` One-click "this was wrong" on agent actions and outputs, captured with the trace id, triaged by the agent's owner, and fed into the test suite ([layer 07](07-testing-and-evaluation.md#after-deployment)).

## Tradecraft and continuity

`[MGF §2.4.3]` (new in v1.5): as agents absorb entry-level tasks, skills erode and the organisation may be unable to perform critical processes manually when the agent fails. `[Practice]`:

- For each business-critical process the agent performs, keep a **documented manual procedure** and an owner.
- **Exercise it** periodically — the kill switch in [layer 08](08-monitoring-and-operations.md) is only safe if work can continue without the agent.
- Identify the core capabilities of affected roles and keep people doing enough of the work to retain them, especially new staff.

## Labelling and provenance of generated content

Disclosing *the agent* (above) is not the same as labelling *what it produces*. The GenAI framework recommends digital watermarking and cryptographic provenance in appropriate contexts, simplified provenance details for end users, and standardising which edits get labelled `[MGF-GenAI Content Provenance, p.23–25]`. `[Practice]`, scaled to where content goes:

- **Simple visible labels** on generated content shown to or sent to people — "AI-generated", "drafted with AI, reviewed by …" — at the point the content appears, not only in a policy page.
- **Cryptographic provenance for published media.** Attach a signed manifest (C2PA-style content credentials) to generated images, audio and video at creation, recording the generator and the edits; sign with a key held by the service, not the model.
- **Watermarking** where the model or provider supports it, for media likely to be redistributed without metadata. Treat it as a probabilistic signal, not proof.
- **Preserve provenance through edits.** Pipelines that resize, transcode or edit generated media must carry the manifest forward and append the edit, not strip it. Test this.
- **Decide what counts as AI-edited** for your product (e.g. a background fill vs a fully generated image) and label consistently.

## Don't encourage users to anthropomorphise

The framework names educating end users on safe chatbot use, "sensitising them against anthropomorphising AI" `[MGF-GenAI AI for Public Good, p.29]`. `[Practice]` Avoid human names, faces and claims of feelings for assistants; say plainly in onboarding and help text that the system can be wrong and has no understanding of the user's situation; and route emotionally sensitive conversations to human help where the use case makes them likely. Framework notes: [`frameworks/sg-mgf-genai/dimensions/07-content-provenance.md`](../frameworks/sg-mgf-genai/dimensions/07-content-provenance.md).
