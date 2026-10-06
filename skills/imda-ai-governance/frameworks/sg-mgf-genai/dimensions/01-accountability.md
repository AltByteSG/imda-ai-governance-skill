# Accountability (p.6–8)

> ⚠ **Reference material only — not legal or regulatory advice.** See [DISCLAIMER.md](https://github.com/AltByteSG/imda-ai-governance-skill/blob/main/DISCLAIMER.md). Verify against the official IMDA and AI Verify Foundation publication and involve your risk and compliance owners.
>
> **How to read this file:** the expectation paragraphs restate the framework, with its dimension and page (page references come from an extracted summary — spot-check them against the PDF). The **Engineering effect** and **Evidence** paragraphs are this skill's interpretation — treat them as `[Practice]`, not as IMDA requirements.

The dimension asks who answers for a generative system when it goes wrong. Its answer has two parts: allocate responsibility **up front** according to control, and put **safety nets** in place for what slips through. For agents, the agentic framework's value-chain and oversight expectations apply on top — see [agentic §2.2](../../sg-mgf-agentic/dimensions/02-human-accountability.md).

## Ex ante — allocation up front

### Responsibility follows control

**Expectation:** allocate responsibility according to the *"control that each stakeholder has"* in the development chain, extending the cloud industry's *"shared responsibility models"* to AI development, and taking account of model type — closed-source, open-source or open-weights `[MGF-GenAI Accountability, p.7]`. Model developers are expected to lead such shared-responsibility frameworks `[MGF-GenAI Accountability, p.8]`.

**Engineering effect:** write down the split. For each layer — base model, fine-tune, system prompt, grounding corpus, input / output filters, application, hosting — record who controls it and therefore who owns its failures. With a closed API model you control far less than with open weights you host, and your controls (filters, evaluation, monitoring) have to compensate. Where the agentic framework already covers this for agents, use its value-chain roles `[MGF §2.2.1]` rather than a second scheme.

**Evidence:** a responsibility table in the [system card](../../../templates/SYSTEM_CARD.md.template) (or the agent card for agents); the model provider's published responsibility or usage terms, linked. See [layer 01](../../../layers/01-accountability.md).

### Download models from reputable platforms

**Expectation:** application deployers that download models should *"download models from reputable platforms"* `[MGF-GenAI Accountability, p.8]`.

**Engineering effect:** model weights are a supply-chain dependency. `[Practice]` pin the model by source, version and checksum; prefer the publisher's official repository; scan weights and loaders before use (see [06-security](06-security.md) on malicious code in models); route new model sources through the same approval as a new third-party library.

**Evidence:** the model's source, version and hash in the system card or lockfile; the approval record for the source.

## Ex post — safety nets

**Expectation:** indemnity and insurance as supplementary safety nets; updating legal frameworks; exploring *"no-fault insurance"* `[MGF-GenAI Accountability, p.8]`.

**Engineering effect:** addressed to **policymakers and the insurance market**. Engineering hook: when adopting a vendor model, `[Practice]` record whether the vendor offers indemnity (e.g. for IP claims on outputs) and what conditions it attaches — conditions often require you to keep the vendor's filters on, which is a build constraint. See [agentic §2.2.1 external parties](../../sg-mgf-agentic/dimensions/02-human-accountability.md).

**Evidence:** the vendor terms reviewed, and any indemnity conditions reflected in configuration.
