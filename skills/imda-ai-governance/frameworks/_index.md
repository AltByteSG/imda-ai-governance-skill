# Frameworks — Index

> ⚠ **Reference material only — not legal or regulatory advice.** See [DISCLAIMER.md](../../../DISCLAIMER.md). Verify against the official IMDA publication and involve your risk and compliance owners.

The `frameworks/` folder mirrors the `jurisdictions/` folder of a statute-based skill: each populated framework has a `README.md` with version metadata, a `dimensions/` folder that maps the framework's expectations onto the universal layers, and a `framework-map.md` for reverse lookup by section number.

| Code | Framework | Publisher | Status |
|---|---|---|---|
| `sg-mgf-agentic` | Model AI Governance Framework for Agentic AI, v1.5 (published 20 May 2026, updated 5 June 2026) | IMDA | Populated |
| `sg-mgf-genai` | Model AI Governance Framework for Generative AI (2024) | IMDA / AI Verify Foundation | Not populated |
| `sg-mgf-2020` | Model AI Governance Framework, 2nd Edition (2020) | IMDA / PDPC | Not populated |

## Which framework applies

- **The system plans and acts over multiple steps with tools** (agents, agentic workflows, coding assistants, computer-use agents, multi-agent systems): `sg-mgf-agentic`. The agentic framework explicitly builds on MGF (2020) rather than replacing it `[MGF §2]`, so the earlier framework's baseline practices (transparency, fairness, explainability, internal governance) still apply underneath.
- **The system generates content but takes no actions** (a chat assistant without tools, a summariser, a RAG Q&A bot): the agentic framework is mostly out of scope. Use the generative-AI and 2020 frameworks, which this skill does not yet populate.
- **Both** — common, since many products grow tools over time. Treat the agentic framework as additive: once an assistant gets its first write-capable tool, it is in scope.

## Related Singapore material the agentic MGF points to

The framework defers to these for depth. This skill references them but does not summarise them.

| Document | Publisher | What it adds |
|---|---|---|
| Draft Addendum on Securing Agentic AI | Cyber Security Agency of Singapore (CSA) | Threat modelling and taint tracing for agentic systems; security control catalogue |
| Agentic Risk & Capability Framework | GovTech Singapore | Capability-based risk and control catalogue |
| Starter Kit for Testing of LLM-based Applications for Safety and Reliability | IMDA / AI Verify Foundation | Baseline LLM testing practice that agent testing extends |
| Guide to Cyber Threat Modelling | CSA | Threat modelling method referenced for risk assessment |
| OpenClaw responsible-deployment case study (May 2026) | IMDA | Worked application of the four dimensions to an open-source agent platform |

## Adding a framework

A new framework folder needs the same shape as `sg-mgf-agentic/`: `README.md` with version and verification metadata, `dimensions/` mapping each part of the framework to the layers, and `framework-map.md` for reverse lookup. Layer files stay framework-agnostic; framework-specific expectations go in the framework folder. See [CONTRIBUTING.md](../../../CONTRIBUTING.md).
