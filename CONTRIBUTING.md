# Contributing

Thanks for your interest. Contributions of any size are welcome — typo fixes, framework updates, stack-specific examples, real-world patterns.

## What's particularly valuable

In rough priority order:

1. **Framework updates.** When IMDA publishes a new version of the Model AI Governance Framework for Agentic AI or for Generative AI, open a PR updating [`frameworks/sg-mgf-agentic/`](skills/imda-ai-governance/frameworks/sg-mgf-agentic/) or [`frameworks/sg-mgf-genai/`](skills/imda-ai-governance/frameworks/sg-mgf-genai/) (version table, section or page references in `framework-map.md`, changed expectations in `dimensions/`), any affected layer or checklist, and the [CHANGELOG](CHANGELOG.md). Link to IMDA's announcement.
2. **Related Singapore frameworks.** The agentic MGF is primary and the generative-AI MGF (2024) is a supplement. The MGF 2nd Edition (2020) is deliberately not populated: both frameworks build on it and already cover its themes for engineers. A new framework needs the same shape as `sg-mgf-agentic/`: a `README.md` with version metadata, `dimensions/` mapping to the universal layers, and a `framework-map.md` reverse lookup.
3. **Stack-specific implementation examples.** Layer files are deliberately stack-agnostic. Examples such as *"in LangGraph, an approval checkpoint is an `interrupt_before` on the tool node plus a policy check in the tool"* are welcome as labelled examples within a layer file — not by coupling the core text to one framework.
4. **Incident patterns that generalise.** If an agent incident taught you something reusable, the incident checklist or the relevant layer is the right home.

## Out of scope

- **Binding law and other jurisdictions' AI rules** (EU AI Act, US state laws, China's rules). A separate project per regime is a better pattern. Personal-data law for Southeast Asia lives in [`personal-data-protection-skill`](https://github.com/AltByteSG/personal-data-protection-skill).
- **Full control catalogues** that the framework defers to (CSA, GovTech, OWASP). Link to them; don't reproduce them.
- **Promotional content** about products or services.

## How to contribute

1. **Typos and small fixes:** open a PR against `main`.
2. **Framework updates:** open an issue first to confirm the change reflects an official IMDA publication rather than interpretation.
3. **New layer content:** open an issue first to discuss whether it is universal enough for the core layer files.

### PR checklist

- [ ] Consistent with [DISCLAIMER.md](DISCLAIMER.md) — reference material, not legal or regulatory advice; the framework is authoritative.
- [ ] Framework statements carry `[MGF §x.y]` (agentic) or `[MGF-GenAI <dimension>, p.N]` (generative); skill recommendations carry `[Practice]`. Nothing the framework doesn't say is attributed to it.
- [ ] Quotations are short operative phrases with section references; no reproduction of framework diagrams or substantial passages.
- [ ] If updating framework notes, the `Last verified` date is bumped.
- [ ] Materially new content has a [CHANGELOG.md](CHANGELOG.md) entry under `Unreleased`.
- [ ] `ruff check .` and `python3 tests/test_ai_governance_check.py` pass if scripts changed.
- [ ] Headings consistent with existing style; tables render on GitHub; relative links resolve.

## Style

- **Tech-agnostic in the layer files.** No assumption of a specific model provider, agent framework, cloud or language.
- **Engineer-readable framework notes.** Each expectation states the engineering effect and the evidence a reviewer should look for.
- **One-line cross-references.** Layers link to checklists, checklists link to layers and dimensions. Link rather than duplicate.
- **No emojis** in skill files (status ticks in tables excepted).

## Licence

By contributing, you agree your contribution is licensed under the [MIT licence](LICENSE).

## Contributor warranties and liability

By submitting a contribution, you warrant that you authored it (or have the right to license it under MIT), that it does not infringe any third party's rights, and that to the best of your knowledge it reflects the official framework as at the date of contribution. You make **no warranty** as to its accuracy, completeness or fitness for purpose. The maintainers may accept, modify or reject contributions at their discretion; acceptance is not an endorsement of accuracy. Once merged, contributions are governed by [DISCLAIMER.md](DISCLAIMER.md), and **neither the maintainers nor any contributor accepts liability** to third parties who rely on contributed content.

## Code of conduct

Be civil. Disagreements about interpretation are expected and welcome; ad hominem is not.
