# Content Provenance (p.23–25)

> ⚠ **Reference material only — not legal or regulatory advice.** See [DISCLAIMER.md](../../../../../DISCLAIMER.md). Verify against the official IMDA and AI Verify Foundation publication and involve your risk and compliance owners.
>
> **How to read this file:** the expectation paragraphs restate the framework, with its dimension and page (page references come from an extracted summary — spot-check them against the PDF). The **Engineering effect** and **Evidence** paragraphs are this skill's interpretation — treat them as `[Practice]`, not as IMDA requirements.

The dimension is about letting people tell where content came from and whether AI made or edited it. It is partly ecosystem work (standards, public awareness) and partly a build requirement for anyone publishing generated content. The agentic framework has no direct equivalent; its user-disclosure expectation ([agentic §2.4](../../sg-mgf-agentic/dimensions/04-end-user-responsibility.md)) covers telling users they are dealing with an agent, not marking the content itself.

## Watermarking and cryptographic provenance

**Expectation:** use digital watermarking and cryptographic provenance in appropriate contexts `[MGF-GenAI Content Provenance, p.23–24]`; publishers to embed and display watermarks; implement them securely against bad actors `[MGF-GenAI Content Provenance, p.25]`.

**Engineering effect:** if the system generates images, audio, video or text that leaves the product (published, downloaded, shared), `[Practice]` decide per output type whether to attach a watermark or signed provenance manifest, and whether the UI shows it. "Appropriate contexts" is a judgement — record it. Keep signing keys in the same key management as other production secrets, and test that provenance survives your own export pipeline (resizing, re-encoding).

**Evidence:** the per-output-type provenance decision in the [system card](../../../templates/SYSTEM_CARD.md.template); the signing / watermarking configuration; a test that exported content still carries it.

## Labelling edits

**Expectation:** standardise the *"types of edits to be labelled"* `[MGF-GenAI Content Provenance, p.25]`.

**Engineering effect:** standardisation is for **standards bodies and industry**. Engineering hook: `[Practice]` if your product lets users edit content with AI (in-painting, rewrite, summarise), record which edit types you label and keep it consistent across features.

**Evidence:** the list of labelled edit types.

## Awareness and simplified provenance for end users

**Expectation:** raise awareness, and simplify provenance details for end users `[MGF-GenAI Content Provenance, p.25]`.

**Engineering effect:** awareness campaigns are for **governments and industry**. Engineering hook: where provenance is shown, `[Practice]` show it in plain language ("made with AI", "edited with AI") rather than raw metadata. See [layer 09](../../../layers/09-end-user-transparency.md).

**Evidence:** screenshots of the provenance indicator.
