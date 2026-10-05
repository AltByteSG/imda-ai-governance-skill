# Frameworks — Index

> ⚠ **Reference material only — not legal or regulatory advice.** See [DISCLAIMER.md](../../../DISCLAIMER.md). Verify against the official IMDA publication and involve your risk and compliance owners.

The `frameworks/` folder mirrors the `jurisdictions/` folder of a statute-based skill: each populated framework has a `README.md` with version metadata, a `dimensions/` folder that maps the framework's expectations onto the universal layers, and a `framework-map.md` for reverse lookup by section number.

| Code | Framework | Publisher | Status |
|---|---|---|---|
| `sg-mgf-agentic` | Model AI Governance Framework for Agentic AI, v1.5 (published 20 May 2026, updated 5 June 2026) | IMDA | Populated |
| `sg-mgf-genai` | Model AI Governance Framework for Generative AI (final, announced 30 May 2024) | IMDA / AI Verify Foundation | Populated as a supplement — see [README](sg-mgf-genai/README.md) |
| `sg-mgf-2020` | Model AI Governance Framework, 2nd Edition (2020) | IMDA / PDPC | Not populated |

## Which framework applies

- **The system plans and acts over multiple steps with tools** (agents, agentic workflows, coding assistants, computer-use agents, multi-agent systems): `sg-mgf-agentic`. The agentic framework explicitly builds on MGF (2020) rather than replacing it `[MGF §2]`, so the earlier framework's baseline practices (transparency, fairness, explainability, internal governance) still apply underneath.
- **The system generates content but takes no actions** (a chat assistant without tools, a summariser, a RAG Q&A bot): the agentic framework is out of scope. Use `sg-mgf-genai` as the bar, starting from [`checklists/new-genai-feature.md`](../checklists/new-genai-feature.md). The 2020 framework's baseline also applies; this skill does not yet populate it.
- **An agent** — the agentic framework is primary. `sg-mgf-genai` applies as a supplement to what sits under the agent: the model and where it came from, the data it was tuned or grounded on, disclosure, outside vulnerability reporting, and labelling of generated content. Once an assistant gets its first write-capable tool, the agentic framework takes over as the bar.

## Related Singapore material the agentic MGF points to

The framework defers to these for depth. This skill references them but does not summarise them.

| Document | Publisher | What it adds |
|---|---|---|
| Draft Addendum on Securing Agentic AI | Cyber Security Agency of Singapore (CSA) | Threat modelling and taint tracing for agentic systems; security control catalogue |
| Agentic Risk & Capability Framework | GovTech Singapore | Capability-based risk and control catalogue |
| Starter Kit for Testing of LLM-based Applications for Safety and Reliability | IMDA (named in the framework) | Baseline LLM testing practice that agent testing extends |
| Guide to Cyber Threat Modelling | CSA | Threat modelling method referenced for risk assessment |
| OpenClaw responsible-deployment case study (May 2026) | IMDA | Worked application of the four dimensions to an open-source agent platform |
| AI Verify, Project Moonshot | AI Verify Foundation | Open-source testing toolkits for AI systems and LLM applications, relevant to the generative-AI framework's testing and assurance dimension |
| MITRE ATLAS | MITRE | Adversarial threat landscape for AI systems; named by the generative-AI framework for threat modelling |

## Adding a framework

A new framework folder needs the same shape as `sg-mgf-agentic/`: `README.md` with version and verification metadata, `dimensions/` mapping each part of the framework to the layers, and `framework-map.md` for reverse lookup. Layer files stay framework-agnostic; framework-specific expectations go in the framework folder. See [CONTRIBUTING.md](../../../CONTRIBUTING.md).
