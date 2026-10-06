# Safety and Alignment R&D (p.26–27)

> ⚠ **Reference material only — not legal or regulatory advice.** See [DISCLAIMER.md](https://github.com/AltByteSG/imda-ai-governance-skill/blob/main/DISCLAIMER.md). Verify against the official IMDA and AI Verify Foundation publication and involve your risk and compliance owners.
>
> **How to read this file:** the expectation paragraphs restate the framework, with its dimension and page (page references come from an extracted summary — spot-check them against the PDF). The **Engineering effect** and **Evidence** paragraphs are this skill's interpretation — treat them as `[Practice]`, not as IMDA requirements.

Addressed to **model developers, researchers, AI safety institutes and governments**. It lands on most product teams only indirectly.

**Expectation:** research into better-aligned models (e.g. RLAIF), backward alignment and mechanistic interpretability, testing for *"emergent capabilities"*, AI safety institutes and global cooperation `[MGF-GenAI Safety and Alignment R&D, p.27]`.

**Engineering effect:** no build artefact follows directly. Engineering hooks, all `[Practice]`:

- **When you change base model, re-evaluate**, because a new model can bring capabilities (and failure modes) the old one did not have. For agents, a model update is a change-management trigger `[MGF §2.3.3]` — see [agentic §2.3](../../sg-mgf-agentic/dimensions/03-technical-controls.md) and [layer 08](../../../layers/08-monitoring-and-operations.md).
- **If you train or substantially fine-tune models**, this dimension is addressed to you: record alignment method and capability evaluations in the [system card](../../../templates/SYSTEM_CARD.md.template).

**Evidence:** re-evaluation results attached to each model change.
