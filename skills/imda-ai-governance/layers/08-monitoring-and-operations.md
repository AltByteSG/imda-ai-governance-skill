# Layer 08 — Monitoring, Rollout and Operations

> ⚠ **Reference material only — not legal or regulatory advice.** See [DISCLAIMER.md](https://github.com/AltByteSG/imda-ai-governance-skill/blob/main/DISCLAIMER.md). Verify against the official IMDA publication and involve your risk and compliance owners.

Running the agent safely once it's live: staged rollout, logging, alerting, intervention, incident handling and change management. Framework basis: `[MGF §2.2.2]` (automated monitoring), `[MGF §2.3]`, `[MGF §2.3.3]`.

## Contents

- Gradual rollout
- What to log
- Make the trail tamper-evident
- Alerts, and the intervention each one triggers
- Kill switch, termination and fallback
- Periodic audit
- Feedback loops
- Change management
- Incidents
- Vulnerability and safety reporting channel
- Severity thresholds for external reporting
- Forensic retention
- Compute and energy per feature

## Gradual rollout

`[MGF §2.3.3]`: roll out gradually by **users**, **tools and protocols**, and **systems**. `[Practice]` Write the rollout plan as stages with explicit exit criteria:

| Stage | Users | Tools / protocols | Systems | Exit criteria (examples) |
|---|---|---|---|---|
| Pilot | Small group of trained, experienced users | Built-in tools only; no third-party MCP | Low-risk, internal | Error and override rates within target for N weeks; no high-severity incidents; oversight metrics healthy |
| Expand | Wider internal users | Allowlisted MCP servers / integrations | More systems, still non-critical | As above, plus red-team findings closed |
| General | Target population (incl. external if applicable) | Full approved set | Production systems in scope | Sign-off from use-case owner on residual risk at this exposure |

The GovTech case study is the reference shape: internal staff, no MCP, low-risk systems first; build central logging and a governed MCP path in parallel; widen only after red-teaming.

Use feature flags so a stage can be rolled back without a deploy.

## What to log

`[MGF §2.3.3]`: decide what to log from your monitoring objectives; prioritise high-risk activities; monitor on multiple layers. `[Practice]` For every run, capture a trace with:

- **Run metadata** — run id, agent id and version, model and version, prompt version, tool versions, user id and capacity ([layer 04](04-identity-and-authorisation.md)), tier.
- **User-agent layer** — the request, and what the agent told the user.
- **Reasoning / plan layer** — plan, plan revisions, decisions at branch points.
- **Agent-tool layer** — every tool call with arguments, result status, latency, and whether it was allowed, asked or denied by policy.
- **Approvals** — requested, decided, by whom, justification.
- **Inter-agent messages** in multi-agent systems.

Use OpenTelemetry or your existing tracing stack so agent traces join the rest of your observability `[MGF §2.3.3]`. Apply the same personal-data hygiene to traces as to any other log: minimise and redact, because prompts and tool results often carry personal data.

## Make the trail tamper-evident

`[MGF §2.3.3]`: problematic trajectories and failures cannot be deleted. `[Practice]` Ship traces to append-only or write-once storage outside the agent's own reach (the agent must not hold a credential that can modify its logs). Retain failure and incident trajectories for longer than routine traces. Log **blocked** attempts too — the Terminal 3 case study records out-of-scope actions that were stopped, because they are evidence.

## Alerts, and the intervention each one triggers

`[MGF §2.2.2, §2.3.3]`: programmatic thresholds, anomaly detection, agents monitoring agents; and a defined intervention per alert type, proportionate to risk. `[Practice]` Keep an alert catalogue:

| Alert | Detection | Intervention |
|---|---|---|
| Attempted unauthorised access / denied tool call | Policy engine deny event | Pause run; notify owner; review same day |
| Repeated failed tool calls / loop | N failures or N identical calls in window | Stop run; return safe failure to user |
| Excess volume | Tool-call or spend rate above threshold | Throttle; pause agent if sustained |
| Atypical action parameters | Outlier vs historical distribution | Route to approval ([layer 06](06-human-oversight.md)) |
| Approval infrastructure unavailable | Health check | Agent fails closed; page on-call |
| Injection indicators | Classifier or canary hit on untrusted input | Quarantine run; security review |
| Drop in override rate or review time | Oversight metrics | Oversight audit ([layer 06](06-human-oversight.md#fight-automation-bias)) |
| Quality drift | Scheduled eval regression | Change review; consider rollback |

Every alert has an owner and an on-call path. Low-priority alerts can batch for scheduled review; high-priority ones halt the agent until a human looks `[MGF §2.3.3]`.

## Kill switch, termination and fallback

`[MGF §2.1.2, §2.3.3]`: be able to take agents offline; for catastrophic malfunction or compromise, terminate and fall back. `[Practice]` The runbook names who can pull the switch, how (without a deploy), what it revokes (credentials, queued actions), and where work goes while the agent is off. Exercise it at least once before general rollout.

## Periodic audit

`[MGF §2.3.3]`: audit at regular intervals. `[Practice]` On a cadence set by tier (e.g. monthly for high, quarterly for medium), review: a sample of trajectories (the Dayos pattern audits sampled reasoning chains), oversight metrics, alert history, incidents, open threat-model items, registry accuracy (owner still valid, scopes still needed), and whether the tier is still right.

## Feedback loops

`[MGF §2.3.3, §2.4.3]`: feed monitoring insights and user overrides back into evaluation and improvement. `[Practice]` Every incident and every meaningful override produces either a new test case, a control change, or a recorded decision that no change is needed.

## Change management

`[MGF §2.3, §2.3.3]` (new in v1.5): define triggers for change review and categorise changes by risk. `[Practice]`:

**Triggers** (from the framework's four categories):

- *Technical* — model or model-version change (including a provider's), prompt or instruction change, tool added / removed / re-scoped, MCP server change, memory design change, framework or SDK upgrade.
- *Environmental* — new user population, new domain, new data source, new business context.
- *Performance* — anomalous behaviour, eval regression, incident.
- *Regulatory* — new law, regulator guidance, or a new version of this framework.

**Categories:**

| Category | Examples | Review |
|---|---|---|
| **Minor** | Prompt wording within the same scope; UI copy; logging additions | Peer review + regression evals |
| **Material** | Model change; new or re-scoped tool; autonomy change; new data source; new user population | Full governance review: update agent card, threat model, eval run at the release-gate thresholds, owner sign-off |
| **Critical** | Anything touching high-stakes decisions or irreversible actions; removing an approval checkpoint; raising a limit | Immediate risk re-assessment and residual-risk re-acceptance before rollout |

**Version control everything that shapes behaviour** — prompts, tool definitions, policies, approval matrices, model pins — so a trace can be tied to exactly what produced it, and a change can be rolled back. See [`checklists/change-review.md`](../checklists/change-review.md).

## Incidents

`[Practice]` An agent incident is any action outside intended scope, any harm from the five types in `[MGF §1.2.2]`, or any control failure, even if caught. Run [`checklists/agent-incident.md`](../checklists/agent-incident.md). If personal data was involved, statutory breach-notification clocks (e.g. PDPA) may apply in parallel and are **not** optional.

## Vulnerability and safety reporting channel

The GenAI framework treats vulnerability reporting as proactive security — including channels for reporting safety issues in AI systems, and bug bounties for white-hat researchers `[MGF-GenAI Incident Reporting, p.17]`. `[Practice]`:

- **Publish a channel** that accepts AI-specific reports — jailbreaks, harmful or biased outputs, prompt-injection paths, data leakage — not only classic security bugs. Link it from `SECURITY.md` / `security.txt` and from the product's "report a problem" path ([layer 09](09-end-user-transparency.md#name-a-human-to-escalate-to)).
- **State a disclosure window.** The framework cites roughly 90 days to patch, publish and credit `[MGF-GenAI Incident Reporting, p.17]`. Triage reports into the incident process and the test suite.

## Severity thresholds for external reporting

The framework expects "severe AI incidents" to be defined by materiality thresholds and reported proportionately, harmonised with existing regimes `[MGF-GenAI Incident Reporting, p.17–18]`. `[Practice]` Write the thresholds **before** an incident: which severities go to whom (regulator, sector body, customers, model provider), within what time, and who decides. Statutory clocks (e.g. PDPA breach notification, sector rules) take precedence. Add them to [`checklists/agent-incident.md`](../checklists/agent-incident.md)'s triage step for your organisation.

## Forensic retention

The framework calls for digital forensics tools for generative AI `[MGF-GenAI Security, p.22]`. `[Practice]` For any output that may need investigating, keep enough to reproduce it: model id and version, system prompt and template version, retrieved chunk ids and index build, filter decisions, sampling parameters, and the output. Retain incident-linked records with the tamper-evident trail above.

## Compute and energy per feature

The framework asks for the carbon footprint of generative AI training and inference to be tracked `[MGF-GenAI AI for Public Good, p.30]`. `[Practice]` (optional): record tokens, GPU-hours or provider-reported energy per feature alongside cost; use it when choosing between models, and prefer the smallest model that passes the evals. Report it in the system card's infrastructure section.
