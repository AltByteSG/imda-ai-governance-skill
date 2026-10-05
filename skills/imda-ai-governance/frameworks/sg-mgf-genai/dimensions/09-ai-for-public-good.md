# AI for Public Good (p.28–30)

> ⚠ **Reference material only — not legal or regulatory advice.** See [DISCLAIMER.md](../../../../../DISCLAIMER.md). Verify against the official IMDA and AI Verify Foundation publication and involve your risk and compliance owners.
>
> **How to read this file:** the expectation paragraphs restate the framework, with its dimension and page (page references come from an extracted summary — spot-check them against the PDF). The **Engineering effect** and **Evidence** paragraphs are this skill's interpretation — treat them as `[Practice]`, not as IMDA requirements.

Mostly addressed to **governments, industry and organisations as employers**. A few items have an engineering hook.

| Sub-heading | Addressed to | Engineering hook |
|---|---|---|
| **Democratising access** — human-centric design; digital literacy; SME adoption `[MGF-GenAI AI for Public Good, p.29]` | Governments, industry | Educate end users on safe chatbot use, *"sensitising them against anthropomorphising AI"* `[MGF-GenAI AI for Public Good, p.29]`. `[Practice]` avoid UI copy and personas that imply the system is a person; say what it is and its limits. See [layer 09](../../../layers/09-end-user-transparency.md) and, for agents, [agentic §2.4](../../sg-mgf-agentic/dimensions/04-end-user-responsibility.md). |
| **Public service delivery** — public sector adoption, data sharing, compute `[MGF-GenAI AI for Public Good, p.30]` | Government | None for private-sector teams. |
| **Workforce** — upskilling; redesigning jobs `[MGF-GenAI AI for Public Good, p.30]` | Employers | Overlaps with tradecraft retention in [agentic §2.4.3](../../sg-mgf-agentic/dimensions/04-end-user-responsibility.md). |
| **Sustainability** — energy-efficient compute; track the *"carbon footprint of generative AI ... for model training and inference"*; green computing and data centres `[MGF-GenAI AI for Public Good, p.30]` | Industry, infrastructure providers | `[Practice]` record estimated training and inference energy or emissions where your provider publishes them, in the [system card](../../../templates/SYSTEM_CARD.md.template) (this also feeds disclosure area (b) in [03](03-trusted-development-and-deployment.md)); prefer the smallest model that passes the evals. |

**Evidence:** user-facing copy that does not anthropomorphise; the energy / emissions estimate in the system card, or "not published by provider".
