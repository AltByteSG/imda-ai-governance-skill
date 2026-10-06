# Singapore MGF for Generative AI — Dimension ↔ Layer Cross-Reference

> ⚠ **Reference material only — not legal or regulatory advice.** See [DISCLAIMER.md](https://github.com/AltByteSG/imda-ai-governance-skill/blob/main/DISCLAIMER.md). Verify against the official IMDA and AI Verify Foundation publication and involve your risk and compliance owners.

Reverse lookup. The framework has no section numbers, so cite by dimension and page: `[MGF-GenAI <Dimension>, p.N]`. Page numbers are those of the PDF dated 19 June 2024, taken from an extracted summary — spot-check before citing in an audit response. "Agentic" points to the overlapping dimension file of the primary framework, where one exists.

| Dimension | Sub-heading | Page | Dimension file | Layer(s) | Agentic overlap |
|---|---|---|---|---|---|
| Executive Summary | — | p.3 | [README](README.md) | — | — |
| Accountability | Design; ex ante — allocation up front (control, shared responsibility, model types) | p.6–7 | [01-accountability](dimensions/01-accountability.md) | [01](../../layers/01-accountability.md) | [§2.2.1](../sg-mgf-agentic/dimensions/02-human-accountability.md) |
| Accountability | Reputable model platforms; developers lead shared responsibility | p.8 | [01-accountability](dimensions/01-accountability.md) | [01](../../layers/01-accountability.md), [05](../../layers/05-technical-controls.md) | [§2.2.1](../sg-mgf-agentic/dimensions/02-human-accountability.md) |
| Accountability | Ex post — safety nets (indemnity, insurance) *[policy]* | p.8 | [01-accountability](dimensions/01-accountability.md) | [01](../../layers/01-accountability.md) | — |
| Data | Trusted use of personal data; PETs *[mostly policy]* | p.10 | [02-data](dimensions/02-data.md) | [10](../../layers/10-data-and-grounding.md) | [§2.1.2](../sg-mgf-agentic/dimensions/01-assess-and-bound.md) |
| Data | Balancing copyright with data accessibility *[policy]* | p.11 | [02-data](dimensions/02-data.md) | [10](../../layers/10-data-and-grounding.md) | — |
| Data | Facilitating access to quality data (governance, annotation, cleaning, trusted datasets) | p.11 | [02-data](dimensions/02-data.md) | [10](../../layers/10-data-and-grounding.md) | — |
| Trusted Development and Deployment | Builds on MGF 2019 / 2020 | p.13 | [README](README.md) | — | — |
| Trusted Development and Deployment | Development — baseline safety practices (RLHF, use-case risk, filters, RAG) | p.13 | [03-trusted-development-and-deployment](dimensions/03-trusted-development-and-deployment.md) | [02](../../layers/02-use-case-and-risk.md), [05](../../layers/05-technical-controls.md), [10](../../layers/10-data-and-grounding.md) | [§2.1.1](../sg-mgf-agentic/dimensions/01-assess-and-bound.md), [§2.3.1](../sg-mgf-agentic/dimensions/03-technical-controls.md) |
| Trusted Development and Deployment | Disclosure — "food labels" (seven areas; model risk thresholds) | p.14 | [03-trusted-development-and-deployment](dimensions/03-trusted-development-and-deployment.md) | [09](../../layers/09-end-user-transparency.md), [01](../../layers/01-accountability.md) | [§2.4](../sg-mgf-agentic/dimensions/04-end-user-responsibility.md) |
| Trusted Development and Deployment | Evaluation; starting point for standardised safety evaluations | p.14–15 | [03-trusted-development-and-deployment](dimensions/03-trusted-development-and-deployment.md) | [07](../../layers/07-testing-and-evaluation.md) | [§2.3.2](../sg-mgf-agentic/dimensions/03-technical-controls.md) |
| Incident Reporting | Vulnerability reporting; monitoring for malfunctions | p.17 | [04-incident-reporting](dimensions/04-incident-reporting.md) | [08](../../layers/08-monitoring-and-operations.md) | [§2.3.3](../sg-mgf-agentic/dimensions/03-technical-controls.md) |
| Incident Reporting | Incident reporting (severe incidents, ISAC-like bodies) *[mostly policy]* | p.17–18 | [04-incident-reporting](dimensions/04-incident-reporting.md) | [08](../../layers/08-monitoring-and-operations.md) | [§2.3.3](../sg-mgf-agentic/dimensions/03-technical-controls.md) |
| Testing and Assurance | How to test — standardisation *[ecosystem]* | p.20 | [05-testing-and-assurance](dimensions/05-testing-and-assurance.md) | [07](../../layers/07-testing-and-evaluation.md) | [§2.3.2](../sg-mgf-agentic/dimensions/03-technical-controls.md) |
| Testing and Assurance | Who to test — trusted accreditation *[ecosystem]* | p.20 | [05-testing-and-assurance](dimensions/05-testing-and-assurance.md) | [07](../../layers/07-testing-and-evaluation.md) | — |
| Security | Adapt "security-by-design" | p.22 | [06-security](dimensions/06-security.md) | [02](../../layers/02-use-case-and-risk.md), [05](../../layers/05-technical-controls.md) | [§2.1.1](../sg-mgf-agentic/dimensions/01-assess-and-bound.md), [§2.3.1](../sg-mgf-agentic/dimensions/03-technical-controls.md) |
| Security | New safeguards (input filters, forensics, MITRE ATLAS) | p.22 | [06-security](dimensions/06-security.md) | [05](../../layers/05-technical-controls.md), [08](../../layers/08-monitoring-and-operations.md) | [§2.3.1](../sg-mgf-agentic/dimensions/03-technical-controls.md) |
| Content Provenance | Watermarking, cryptographic provenance | p.23–25 | [07-content-provenance](dimensions/07-content-provenance.md) | [09](../../layers/09-end-user-transparency.md) | — |
| Content Provenance | Labelling edits; end-user awareness | p.25 | [07-content-provenance](dimensions/07-content-provenance.md) | [09](../../layers/09-end-user-transparency.md) | — |
| Safety and Alignment R&D | Alignment, interpretability, emergent capabilities *[ecosystem]* | p.27 | [08-safety-and-alignment-rnd](dimensions/08-safety-and-alignment-rnd.md) | [07](../../layers/07-testing-and-evaluation.md), [08](../../layers/08-monitoring-and-operations.md) | [§2.3.3](../sg-mgf-agentic/dimensions/03-technical-controls.md) |
| AI for Public Good | Democratising access; user education against anthropomorphising | p.29 | [09-ai-for-public-good](dimensions/09-ai-for-public-good.md) | [09](../../layers/09-end-user-transparency.md) | [§2.4](../sg-mgf-agentic/dimensions/04-end-user-responsibility.md) |
| AI for Public Good | Public service delivery *[government]* | p.30 | [09-ai-for-public-good](dimensions/09-ai-for-public-good.md) | — | — |
| AI for Public Good | Workforce | p.30 | [09-ai-for-public-good](dimensions/09-ai-for-public-good.md) | — | [§2.4.3](../sg-mgf-agentic/dimensions/04-end-user-responsibility.md) |
| AI for Public Good | Sustainability (carbon footprint of training and inference) | p.30 | [09-ai-for-public-good](dimensions/09-ai-for-public-good.md) | [01](../../layers/01-accountability.md) | — |
| Conclusion; Further Development | — | p.31, p.34 | [README](README.md) | — | — |

*[policy]*, *[government]* and *[ecosystem]* mark sub-headings addressed mainly to someone other than the build team; the dimension file names who, and the engineering hook if there is one.
