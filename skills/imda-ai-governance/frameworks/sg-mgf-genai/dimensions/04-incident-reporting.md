# Incident Reporting (p.16–18)

> ⚠ **Reference material only — not legal or regulatory advice.** See [DISCLAIMER.md](../../../../../DISCLAIMER.md). Verify against the official IMDA and AI Verify Foundation publication and involve your risk and compliance owners.
>
> **How to read this file:** the expectation paragraphs restate the framework, with its dimension and page (page references come from an extracted summary — spot-check them against the PDF). The **Engineering effect** and **Evidence** paragraphs are this skill's interpretation — treat them as `[Practice]`, not as IMDA requirements.

The dimension covers finding problems before they cause harm (vulnerability reporting) and handling them when they do (incident reporting). The agentic framework's monitoring, alerting and incident expectations ([agentic §2.3.3](../../sg-mgf-agentic/dimensions/03-technical-controls.md)) cover the same ground for agents; this file adds what is specific to generative output.

## Vulnerability reporting — incentive to act pre-emptively

**Expectation:** vulnerability reporting as part of proactive security; bug bounties and white-hat researchers; a window of about 90 days to patch, publish and credit; safety vulnerability reporting channels in AI systems; ongoing monitoring to detect malfunctions `[MGF-GenAI Incident Reporting, p.17]`.

**Engineering effect:**

- **A reporting channel that accepts AI-safety issues**, not only classic security bugs — jailbreaks, harmful outputs, data leakage through prompts. `[Practice]` extend the existing `SECURITY.md` / disclosure policy to name these, and add an in-product "report this response" path.
- **A disclosure clock.** `[Practice]` track AI-safety reports against the same ~90-day patch-and-publish window as security reports.
- **Output monitoring** for malfunctions — spikes in filter hits, refusals, user reports, hallucination flags. See [layer 08](../../../layers/08-monitoring-and-operations.md).

**Evidence:** the published reporting channel and its scope; the triage owner; time-to-fix for past reports; monitoring dashboards and alerts on output quality.

## Incident reporting

**Expectation:** define *"severe AI incidents"* and materiality thresholds; report to ISAC-like bodies; harmonise with existing reporting regimes; keep it proportionate `[MGF-GenAI Incident Reporting, p.17–18]`.

**Engineering effect:** the thresholds and external reporting bodies are for **policymakers and industry bodies** to set. Engineering hook: `[Practice]` define internally what counts as a severe incident for this system (e.g. personal data disclosed in output, harmful content to a minor, a widely shared fabricated claim), so on-call knows when to escalate, and route it through the existing incident process (and any regulator reporting that already binds you). For agents, use [`checklists/agent-incident.md`](../../../checklists/agent-incident.md).

**Evidence:** the severity definitions for generative incidents; the runbook entry; post-incident records.
