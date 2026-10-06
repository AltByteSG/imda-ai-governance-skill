# Singapore MGF for Agentic AI — Section ↔ Layer Cross-Reference

> ⚠ **Reference material only — not legal or regulatory advice.** See [DISCLAIMER.md](https://github.com/AltByteSG/imda-ai-governance-skill/blob/main/DISCLAIMER.md). Verify against the official IMDA publication and involve your risk and compliance owners.

Reverse lookup. Use when citing a section in a PR description, design review, or audit response. For day-to-day work, use the layer files and dimension files instead. Section numbers are those of v1.5 (20 May 2026, updated 5 June 2026).

## §1 — Introduction to Agentic AI

| Section | Topic | Dimension file | Layer |
|---|---|---|---|
| §1.1 | Definition and scope of agentic AI | [00-foundations](dimensions/00-foundations.md) | — |
| §1.1.1 | Core components (model, instructions, memory, planning, tools, protocols, controls, logging) | [00-foundations](dimensions/00-foundations.md) | [03](../../layers/03-architecture-and-bounding.md), [05](../../layers/05-technical-controls.md), [08](../../layers/08-monitoring-and-operations.md) |
| §1.1.2 | Multi-agent patterns (sequential, supervisor, swarm) | [00-foundations](dimensions/00-foundations.md) | [03](../../layers/03-architecture-and-bounding.md) |
| §1.1.3 | Action-space vs autonomy; levels of human involvement; computer-use agents | [00-foundations](dimensions/00-foundations.md) | [03](../../layers/03-architecture-and-bounding.md), [06](../../layers/06-human-oversight.md) |
| §1.2.1 | Sources of risk by component | [00-foundations](dimensions/00-foundations.md) | [02](../../layers/02-use-case-and-risk.md) |
| §1.2.2 | Types of risk (erroneous, unauthorised, biased, data breach, disruption) | [00-foundations](dimensions/00-foundations.md) | [02](../../layers/02-use-case-and-risk.md), [07](../../layers/07-testing-and-evaluation.md) |
| §1.2.3 | Systemic and multi-agent risks | [00-foundations](dimensions/00-foundations.md) | [02](../../layers/02-use-case-and-risk.md), [03](../../layers/03-architecture-and-bounding.md), [04](../../layers/04-identity-and-authorisation.md) |

## §2 — The framework

| Section | Topic | Dimension file | Layer |
|---|---|---|---|
| §2 | Four dimensions; iterative application | [README](README.md) | — |
| §2.1.1 | Risk vs benefit; deterministic alternative | [01-assess-and-bound](dimensions/01-assess-and-bound.md) | [02](../../layers/02-use-case-and-risk.md) |
| §2.1.1 | Impact and likelihood factors | [01-assess-and-bound](dimensions/01-assess-and-bound.md) | [02](../../layers/02-use-case-and-risk.md) |
| §2.1.1 | Threat modelling and taint tracing | [01-assess-and-bound](dimensions/01-assess-and-bound.md) | [02](../../layers/02-use-case-and-risk.md) |
| §2.1.2 | Limits on tools and systems (least privilege, functional boundaries) | [01-assess-and-bound](dimensions/01-assess-and-bound.md) | [03](../../layers/03-architecture-and-bounding.md), [04](../../layers/04-identity-and-authorisation.md) |
| §2.1.2 | Limits on autonomy (SOPs) | [01-assess-and-bound](dimensions/01-assess-and-bound.md) | [03](../../layers/03-architecture-and-bounding.md) |
| §2.1.2 | Limits on area of impact; taking agents offline; self-contained environments | [01-assess-and-bound](dimensions/01-assess-and-bound.md) | [03](../../layers/03-architecture-and-bounding.md), [08](../../layers/08-monitoring-and-operations.md) |
| §2.1.2 | Prefer deterministic limits; bound by design | [01-assess-and-bound](dimensions/01-assess-and-bound.md) | [05](../../layers/05-technical-controls.md) |
| §2.1.2 | Agent identity (unique, accounted for, capacity, centrally managed) | [01-assess-and-bound](dimensions/01-assess-and-bound.md) | [04](../../layers/04-identity-and-authorisation.md) |
| §2.1.2 | Agent authorisation (scoped, time-bound, non-transferable, bounded by human) | [01-assess-and-bound](dimensions/01-assess-and-bound.md) | [04](../../layers/04-identity-and-authorisation.md) |
| §2.1.2 | Residual risk acceptance | [01-assess-and-bound](dimensions/01-assess-and-bound.md) | [01](../../layers/01-accountability.md) |
| §2.2.1 | Agentic value chain and roles | [02-human-accountability](dimensions/02-human-accountability.md) | [01](../../layers/01-accountability.md) |
| §2.2.1 | Responsibilities within the organisation | [02-human-accountability](dimensions/02-human-accountability.md) | [01](../../layers/01-accountability.md) |
| §2.2.1 | Adaptive governance capability | [02-human-accountability](dimensions/02-human-accountability.md) | [01](../../layers/01-accountability.md), [08](../../layers/08-monitoring-and-operations.md) |
| §2.2.1 | External parties: contracts, third-party opacity | [02-human-accountability](dimensions/02-human-accountability.md) | [01](../../layers/01-accountability.md) |
| §2.2.2 | Approval checkpoints (high-stakes, irreversible, atypical, user-defined) | [02-human-accountability](dimensions/02-human-accountability.md) | [06](../../layers/06-human-oversight.md) |
| §2.2.2 | Form of approval requests | [02-human-accountability](dimensions/02-human-accountability.md) | [06](../../layers/06-human-oversight.md) |
| §2.2.2 | Auditing oversight effectiveness; override rate; response time; reviewer training and expertise | [02-human-accountability](dimensions/02-human-accountability.md) | [06](../../layers/06-human-oversight.md), [08](../../layers/08-monitoring-and-operations.md) |
| §2.2.2 | Automated monitoring; deny by default on approval failure | [02-human-accountability](dimensions/02-human-accountability.md) | [06](../../layers/06-human-oversight.md), [08](../../layers/08-monitoring-and-operations.md) |
| §2.3 | Lifecycle structure; change management and version control | [03-technical-controls](dimensions/03-technical-controls.md) | [08](../../layers/08-monitoring-and-operations.md) |
| §2.3.1 | Structural vs model-based vs prompt-layer controls; runtime controls | [03-technical-controls](dimensions/03-technical-controls.md) | [05](../../layers/05-technical-controls.md) |
| §2.3.1 | Planning, tool, protocol and multi-agent controls | [03-technical-controls](dimensions/03-technical-controls.md) | [05](../../layers/05-technical-controls.md) |
| §2.3.1 | MCP as a governance layer | [03-technical-controls](dimensions/03-technical-controls.md) | [05](../../layers/05-technical-controls.md) |
| §2.3.2 | Pre-deployment testing for agents | [03-technical-controls](dimensions/03-technical-controls.md) | [07](../../layers/07-testing-and-evaluation.md) |
| §2.3.3 | Gradual deployment | [03-technical-controls](dimensions/03-technical-controls.md) | [08](../../layers/08-monitoring-and-operations.md) |
| §2.3.3 | Continuous testing and monitoring; alerts; interventions; log immutability | [03-technical-controls](dimensions/03-technical-controls.md) | [08](../../layers/08-monitoring-and-operations.md) |
| §2.3.3 | Robust change management (triggers, risk categories) | [03-technical-controls](dimensions/03-technical-controls.md) | [08](../../layers/08-monitoring-and-operations.md) |
| §2.4 | Transparency and education baseline | [04-end-user-responsibility](dimensions/04-end-user-responsibility.md) | [09](../../layers/09-end-user-transparency.md) |
| §2.4.1 | User archetypes | [04-end-user-responsibility](dimensions/04-end-user-responsibility.md) | [09](../../layers/09-end-user-transparency.md) |
| §2.4.2 | Disclosure to users who interact with agents | [04-end-user-responsibility](dimensions/04-end-user-responsibility.md) | [09](../../layers/09-end-user-transparency.md) |
| §2.4.3 | Training; feedback loops; tradecraft and business continuity | [04-end-user-responsibility](dimensions/04-end-user-responsibility.md) | [09](../../layers/09-end-user-transparency.md), [08](../../layers/08-monitoring-and-operations.md) |

## Annexes

| Section | Topic | Notes |
|---|---|---|
| Annex A | Further resources | Reading list; no expectations |
| Annex B | Call for feedback and case studies | [go.gov.sg/mgfagentic-feedback](https://go.gov.sg/mgfagentic-feedback) |
