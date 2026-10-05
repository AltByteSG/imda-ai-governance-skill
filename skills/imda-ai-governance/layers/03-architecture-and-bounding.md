# Layer 03 — Architecture and Bounding

> ⚠ **Reference material only — not legal or regulatory advice.** See [DISCLAIMER.md](../../../DISCLAIMER.md). Verify against the official IMDA publication and involve your risk and compliance owners.

System-level decisions that set the ceiling on what an agent can do, whatever the model decides. Framework basis: `[MGF §1.1]`, `[MGF §2.1.2]`, `[MGF §2.3.1]`.

## State both dials explicitly

`[MGF §1.1.3]` separates **action-space** (tools and permissions) from **autonomy** (instructions and human involvement). `[Practice]` Every design document should contain both, in this form:

- **Action-space:** systems reached (sandbox / internal / external), per-tool read or write, whether computer-use or browser control is involved.
- **Autonomy:** SOP-driven or judgement-driven, and which of the framework's four involvement levels applies — *agent proposes, human operates*; *agent and human collaborate*; *agent operates, human approves*; *agent operates, human observes*. Different actions in the same agent can sit at different levels; say which.

If a reviewer can't find these two paragraphs, they should ask for them before reviewing anything else.

## Encode the SOP in the workflow, not the prompt

`[MGF §2.1.2]` recommends SOPs that constrain the agent; `[MGF §2.3.1]` notes that building a required sequence into the workflow is more robust than prompting for it. `[Practice]`:

- Express the workflow as a graph, state machine or step list in code. Let the model choose *within* a step, not which step comes next, unless open-ended planning is the point.
- Put validation between steps. Errors cascade `[MGF §1.2.3]`; a schema check or a deterministic sanity check (e.g. an inventory figure within historical bounds) between steps stops one hallucination becoming ten actions.
- Cap iterations, retries and total tool calls per run. Loops after errors are a named failure mode `[MGF §2.4.3]`.

## Functional boundaries and multi-agent topology

`[MGF §2.1.2]` suggests structuring agents around functional boundaries; `[MGF §1.1.2]` notes multi-agent setups let each agent's tools be scoped separately. `[Practice]`:

- **Prefer several narrow agents over one broad one.** Give each only its function's tools. The OpenClaw case explicitly advises against a single "all-powerful" agent.
- **Separate reading untrusted content from acting.** A "reader" agent that processes web pages or emails and returns structured data to an "actor" agent that holds write tools breaks the injection path ([layer 02](02-use-case-and-risk.md#threat-modelling)). The actor should accept only the typed schema, never free text instructions `[MGF §2.3.1]`.
- **Choose the pattern deliberately.** Sequential for well-defined procedures, supervisor where a coordinator delegates, swarm only where open-ended exploration is the point `[MGF §1.1.2]` — and swarm designs warrant heavier system-level testing.
- **Give agents with conflicting objectives a tiebreaker.** If a refund agent and a revenue-protection agent can disagree `[MGF §1.2.3]`, define in code which wins or route the conflict to a human.

## Bound the blast radius

`[MGF §2.1.2]` expects mechanisms to limit impact and take agents offline. `[Practice]`:

- **Sandbox code execution.** Containers or micro-VMs with no ambient credentials, restricted filesystem, and network egress denied by default with an explicit allowlist.
- **Separate environments.** Agents under development never hold production credentials. Test against production-like sandboxes `[MGF §2.3.2]`.
- **Hard limits on consequential parameters.** Transaction ceilings, maximum records per update, recipient allowlists for outbound messages, rate limits on external calls (so the agent can't overwhelm a connected system — a named harm `[MGF §1.2.2]`).
- **Reversibility by design.** Prefer soft-delete, drafts, staged changes and two-phase commit to direct irreversible actions. An agent that writes a draft for a human to send is a lower tier than one that sends.
- **Kill switch.** A per-agent and global stop that halts in-flight runs, revokes the agent's credentials, and is reachable by the on-call engineer without a deploy. Exercise it before launch.
- **Fallback.** When the agent is off, the work routes somewhere — a human queue or the old deterministic path. See [layer 09](09-end-user-transparency.md#tradecraft-and-continuity).

## Keep sensitive data out of the agent's context where you can

`[MGF §2.1.1]` rates sensitive-data access and persistent memory as impact factors. `[Practice]` The strongest control is architectural: if the agent doesn't need to see a value, pass an opaque reference and let a trusted service resolve it at execution time (the Terminal 3 case study does exactly this for salaries and bank details). Where the agent must see it:

- Minimise what enters the context — and test that it doesn't copy extraneous personal data into outputs (the computer-use case study found exactly that failure).
- Scope memory per user and per purpose; don't let one user's data persist into another's session.
- Set retention on long-term memory and make it deletable.
- In multi-agent systems, **limit shared memory** `[MGF §2.3.1]` and don't pass full context to agents that don't need it.

## Computer-use and browser agents

`[MGF §1.1.3]` notes computer-use agents can take any action a human can on screen. `[Practice]` Treat them as high action-space by default: dedicated VM or browser profile with no personal sessions, site allowlists, no stored credentials (hand control to the user for sign-in and secrets `[MGF §2.3.1]`), and screenshot or step logs for every action.

## Third-party agents inside your estate

`[MGF §2.1.1]` treats agents provided by external parties as higher likelihood. `[Practice]` Follow the MSD pattern: contain vendor-embedded agents to their own platform by default; grant cross-system reach only through an integration you control and log.
