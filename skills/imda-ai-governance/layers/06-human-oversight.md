# Layer 06 — Human Oversight

> ⚠ **Reference material only — not legal or regulatory advice.** See [DISCLAIMER.md](../../../DISCLAIMER.md). Verify against the official IMDA publication and involve your risk and compliance owners.

Where humans approve, what they see when they do, and how you know the approvals still mean something. Framework basis: `[MGF §1.1.3]`, `[MGF §2.2.2]`.

## Build an action → approval matrix

`[MGF §2.2.2]` names four kinds of checkpoint: **high-stakes**, **irreversible**, **outlier / atypical**, and **user-defined**. `[Practice]` List every tool action and assign it a level:

| Level | When | Example |
|---|---|---|
| **None** | Read-only, low sensitivity, easily reversible | Read a file, search a knowledge base |
| **Sampled after the fact** | Low tier, reversible, high volume | Password resets (the Dayos tier 1 pattern) |
| **Approve before execution** | Writes that matter; external communication; moderate sensitivity | Update a record, send an email, merge a PR |
| **Approve with written justification** | High stakes, irreversible, high-risk domain | Payment above threshold, permanent deletion, hiring or credit decision |
| **Agent may not do this** | Too risky for the current maturity | Production deployments, permission changes (Dayos tier 3) |

Add two dynamic triggers on top of the static matrix:

- **Atypical behaviour** — access outside normal scope, parameters far from the norm (the framework's example: a route twice the median). Route to approval even if the action is normally free.
- **User-defined limits** — let users tighten their own thresholds (e.g. "ask me before any purchase over $50") `[MGF §2.2.2, §2.4.2]`. `[Practice]` Users can add checkpoints on top of the organisation's, never remove or loosen them.

## Enforce approvals in the system, not the prompt

The OpenClaw guidance says it directly: enforce human approval through **system-level controls** rather than prompt-layer guardrails, which may be bypassed or "forgotten". `[Practice]` The tool call is held by the runtime or policy engine until an approval record exists for *that* call with *those* arguments. The model is never the component that decides whether approval was obtained.

- Approval binds to the exact action and arguments. Changing the amount after approval invalidates it.
- Approvals expire. A stale approval is not reusable for a later run.
- Approvals are logged with approver identity, time, decision, and justification where required.

## Fail closed

`[MGF §2.2.2]`: deny by default when approval infrastructure fails — supervisors unreachable, or the agent attempts a new action with no approval policy. `[Practice]` Test both paths explicitly ([layer 07](07-testing-and-evaluation.md)):

- Approval service down or timing out → the action does not happen; the run pauses or ends with a clear status.
- Tool or action not in the policy → denied or escalated, never allowed.

## Make the approval request worth reading

`[MGF §2.2.2]`: keep requests **contextual and digestible while making the risk clear**; include useful data like the risk or a confidence score; match the input to the decision. `[Practice]` A good approval request contains:

1. **What** will happen, in one plain sentence — not a raw tool call. The Tencent pattern: translate a shell command into what it does and its side effects ("creates a compressed backup… read-only on the database").
2. **Why** the agent wants to do it — the step in the plan it serves.
3. **Risk** — why this needed approval (irreversible? external? above threshold? atypical?).
4. **Key parameters** — recipient, amount, records affected — visible without expanding anything.
5. **Confidence or uncertainty** where meaningful.
6. **Options** — approve, reject, **edit** (for plans and drafts), and a justification field for high-risk actions.

Avoid: walls of logs, raw JSON, approval prompts so frequent they become a reflex.

## Fight automation bias

`[MGF §2.2.2]` expects oversight effectiveness to be audited. `[Practice]` Instrument the approval path and report, per queue and per approver:

- **Override rate** — share of requests rejected or modified. A rate near zero over a long period suggests rubber-stamping; investigate before concluding the agent is perfect.
- **Time to decision** — very short review times on complex requests suggest the reviewer isn't reading.
- **Outlier approvers** — individuals whose patterns differ sharply from peers.
- **Approval volume per approver per hour** — fatigue is a capacity problem; reduce request volume by moving genuinely low-risk actions down the matrix (or into a sandbox, as GovTech did) rather than asking people to approve faster.

Feed this into the periodic audit ([layer 08](08-monitoring-and-operations.md)) and act on it.

`[Practice]` Consider **seeded checks**: occasionally present a known-bad request in a test queue (with consent and clear labelling) to measure whether approvers catch it.

## Approvers need the right expertise and training

`[MGF §2.2.2]`: approvers should have domain expertise and training on agent failure modes, and should know that **chain-of-thought is not necessarily a faithful explanation** of what the agent did. `[Practice]`:

- Each approval queue states the expertise required. A PR-merge approval for agent-written code needs someone who can review that code.
- Show what the agent *did* (tool calls, diffs, data touched) alongside what it *said* it did.
- Avoid anthropomorphic framing in approval UIs ("I'm confident you'll agree…"); `[MGF §2.2.2]` notes it can sway oversight.

## Choose the involvement level per action, not per agent

`[MGF §1.1.3]` describes four involvement levels. `[Practice]` The same agent can be "human approves" for payments and "human observes" for lookups. Writing it per action avoids the two failure modes: approving everything (fatigue) and approving nothing (unbounded).
