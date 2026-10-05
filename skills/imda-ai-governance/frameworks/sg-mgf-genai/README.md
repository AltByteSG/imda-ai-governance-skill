# Singapore MGF for Generative AI — Framework Notes

> ⚠ **Reference material only — not legal or regulatory advice.** See [DISCLAIMER.md](../../../../DISCLAIMER.md). Verify against the official IMDA publication and involve your risk and compliance owners.

| | |
|---|---|
| **Framework** | Model AI Governance Framework for Generative AI |
| **Version reflected** | Final version announced by IMDA on 30 May 2024; PDF dated 19 June 2024 |
| **Last verified** | 2026-10-05, **against an extracted summary of the PDF — page references are to be spot-checked against the PDF** |
| **Publisher** | Infocomm Media Development Authority (IMDA) and the AI Verify Foundation, Singapore |
| **Legal status** | Voluntary guidance. Not legislation; no penalties attach to it directly |
| **Source** | [Framework PDF (19 June 2024)](https://aiverifyfoundation.sg/wp-content/uploads/2026/06/Model-AI-Governance-Framework-for-Generative-AI-19-June-2024.pdf); [IMDA factsheet](https://www.imda.gov.sg/resources/press-releases-factsheets-and-speeches/factsheets/2024/gen-ai-and-digital-foss-ai-governance-playbook) |
| **Citation form** | The framework has no section numbers — cite as `[MGF-GenAI <Dimension>, p.N]`, e.g. `[MGF-GenAI Data, p.11]`. "Trusted Development and Deployment" is shortened to `Trusted Development` |

> **Source copyright:** the framework is published by IMDA and the AI Verify Foundation and remains their material. Quotations in this skill are short operative phrases reproduced with attribution for educational and engineering reference; they are **not** licensed under this repository's MIT licence. See [DISCLAIMER.md § Copyright in source materials](../../../../DISCLAIMER.md#copyright-in-source-materials).

## How this relates to the agentic framework

- **The agentic framework (`sg-mgf-agentic`) stays primary.** If the system plans and acts with tools, start there. Cite it as `[MGF §x.y]`; never mix the two citation forms.
- **This framework covers the layer underneath an agent:** the model, the data it was trained, fine-tuned or grounded on, and the content it generates. Use it to check model selection, data and corpus governance, output filtering, model disclosure, evaluation and content provenance — the parts the agentic framework assumes are already in place.
- **For generative systems that take no actions** (a chat assistant without tools, a summariser, a RAG Q&A bot) this is the **main** framework.
- **It builds on the 2019 Model AI Governance Framework and its 2020 update** `[MGF-GenAI Trusted Development, p.13]`, so those baseline practices still apply underneath both.
- Much of the framework is addressed to **policymakers, governments and the wider ecosystem**, not to builders. The dimension files say so in one line and give the engineering hook only where one exists.

## The nine dimensions

| File | Dimension (pages) | Topic | Lands on engineers? |
|---|---|---|---|
| [01-accountability.md](dimensions/01-accountability.md) | Accountability (p.6–8) | Shared responsibility by control; model sourcing; indemnity and insurance | Partly |
| [02-data.md](dimensions/02-data.md) | Data (p.9–11) | Personal data, copyright, data quality, annotation, cleaning | Yes |
| [03-trusted-development-and-deployment.md](dimensions/03-trusted-development-and-deployment.md) | Trusted Development and Deployment (p.12–15) | Baseline safety practices, "food label" disclosure, evaluation | Yes |
| [04-incident-reporting.md](dimensions/04-incident-reporting.md) | Incident Reporting (p.16–18) | Vulnerability reporting, monitoring, severe-incident thresholds | Yes |
| [05-testing-and-assurance.md](dimensions/05-testing-and-assurance.md) | Testing and Assurance (p.19–20) | Third-party testing, standard benchmarks, accreditation | Partly |
| [06-security.md](dimensions/06-security.md) | Security (p.21–22) | Security-by-design across the SDLC, input filters, model forensics, MITRE ATLAS | Yes |
| [07-content-provenance.md](dimensions/07-content-provenance.md) | Content Provenance (p.23–25) | Watermarking, cryptographic provenance, labelling edits | Partly |
| [08-safety-and-alignment-rnd.md](dimensions/08-safety-and-alignment-rnd.md) | Safety and Alignment R&D (p.26–27) | Alignment research, interpretability, emergent capabilities | Mostly not |
| [09-ai-for-public-good.md](dimensions/09-ai-for-public-good.md) | AI for Public Good (p.28–30) | Access, user education, public sector, workforce, sustainability | Mostly not |

The reverse lookup (dimension / sub-heading / page → dimension file → layer) is at [framework-map.md](framework-map.md).

## What's intentionally not covered

- **Executive Summary (p.3), Conclusion (p.31) and Further Development (p.34)** — framing, no expectations.
- **Recommendations to policymakers and governments** (how personal data law applies, copyright dialogue, legal-framework updates, no-fault insurance, national datasets, public-sector compute) beyond one line naming who they're addressed to.
- **Ecosystem building** (standards bodies, tester accreditation, AI safety institutes, international cooperation) — no build artefact follows from it.
- **The detailed standards and catalogues the framework points to** (ISO/IEC, IEEE, MITRE ATLAS). Use them directly.

## Mental model: what an engineer should take from this framework

- **The unit of risk is the output and the data behind it.** Where the agentic framework asks "what can this do?", this one asks "what was it trained or grounded on, what can it say, and can anyone tell it was generated?"
- **Responsibility follows control** `[MGF-GenAI Accountability, p.7]`. You own what you can change: your prompts, filters, fine-tunes, grounding corpus and deployment — not the base model's pre-training, but you do own the choice of model and where you got it.
- **Disclose like a food label** `[MGF-GenAI Trusted Development, p.14]`. Seven areas, from data used to user-data protection. In this skill that is the [system card](../../templates/SYSTEM_CARD.md.template).
- **Evaluate with both benchmarks and red teaming** `[MGF-GenAI Trusted Development, p.14]`, and keep evaluating after release.
- **Filters on the way in and the way out** `[MGF-GenAI Trusted Development, p.13; Security, p.22]` are baseline, not an extra.

## Cross-references

- [`../sg-mgf-agentic/README.md`](../sg-mgf-agentic/README.md) — the primary framework.
- [`../../layers/10-data-and-grounding.md`](../../layers/10-data-and-grounding.md) — data, corpus and grounding practice.
- [`../../checklists/new-genai-feature.md`](../../checklists/new-genai-feature.md) and [`../../checklists/new-dataset-or-corpus.md`](../../checklists/new-dataset-or-corpus.md) — entry points.
- [`../../templates/SYSTEM_CARD.md.template`](../../templates/SYSTEM_CARD.md.template) — where the disclosure evidence ends up.
