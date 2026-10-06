# Security (p.21–22)

> ⚠ **Reference material only — not legal or regulatory advice.** See [DISCLAIMER.md](https://github.com/AltByteSG/imda-ai-governance-skill/blob/main/DISCLAIMER.md). Verify against the official IMDA and AI Verify Foundation publication and involve your risk and compliance owners.
>
> **How to read this file:** the expectation paragraphs restate the framework, with its dimension and page (page references come from an extracted summary — spot-check them against the PDF). The **Engineering effect** and **Evidence** paragraphs are this skill's interpretation — treat them as `[Practice]`, not as IMDA requirements.

The dimension asks for existing security practice to be adapted to generative AI and for new safeguards where the old ones don't fit. For agents, the agentic framework's threat modelling and controls go further ([agentic §2.1.1](../../sg-mgf-agentic/dimensions/01-assess-and-bound.md), [agentic §2.3.1](../../sg-mgf-agentic/dimensions/03-technical-controls.md)) and defer to CSA's agentic addendum; use them, and treat this file as the model-layer baseline.

## Adapt "security-by-design"

**Expectation:** design security into every phase of the software development lifecycle, refined for the characteristics of generative AI, including its probabilistic nature `[MGF-GenAI Security, p.22]`.

**Engineering effect:** the normal secure-SDLC gates apply, plus: `[Practice]` treat prompts, model outputs and retrieved documents as untrusted input; never pass model output to an interpreter, query or shell without validation; and test controls repeatedly, since the same input can produce different outputs.

**Evidence:** the threat model covering prompt injection, data leakage through outputs and poisoned grounding data; secure-SDLC sign-off for the release. See [layer 02](../../../layers/02-use-case-and-risk.md) and [layer 05](../../../layers/05-technical-controls.md).

## Develop new security safeguards

### Input filters

**Expectation:** *"Input Filters"* to detect unsafe prompts `[MGF-GenAI Security, p.22]`.

**Engineering effect:** an input classifier or rule set in the request path, before the model, enforced in code. Pair it with the output filters from [03-trusted-development-and-deployment](03-trusted-development-and-deployment.md). For agents this is one runtime control among those in `[MGF §2.3.1]`.

**Evidence:** the filter's configuration, what it blocks or flags, its false-positive / false-negative rates on the eval set, and the logs of blocked inputs.

### Digital forensics for generative AI

**Expectation:** *"Digital Forensics Tools for Generative AI"*, including identifying malicious code within models `[MGF-GenAI Security, p.22]`.

**Engineering effect:** `[Practice]` scan model artefacts before loading (prefer safe serialisation formats over ones that execute code on load), and keep enough logging — prompts, outputs, model version, filter decisions — to reconstruct what happened after an incident.

**Evidence:** the model-artefact scanning step in the pipeline; log retention covering inputs, outputs and model version. See [layer 08](../../../layers/08-monitoring-and-operations.md).

### Threat modelling with MITRE ATLAS

**Expectation:** use MITRE ATLAS for threat modelling `[MGF-GenAI Security, p.22]`.

**Engineering effect:** `[Practice]` reference ATLAS techniques in the threat model so coverage can be checked; for agents, combine with the agentic threat-modelling and taint-tracing expectation `[MGF §2.1.1]`.

**Evidence:** a threat model that maps identified threats to ATLAS techniques and to the controls that address them.
