# Disclaimer

> **READ THIS BEFORE USING THIS SKILL FOR ANY GOVERNANCE, RISK OR COMPLIANCE PURPOSE.**

The content in this repository is **engineering reference material**. It is **not legal advice**, **not regulatory advice**, **not professional advice**, and **not a substitute for your organisation's risk, security, legal and compliance functions**.

By installing, accessing, viewing, or otherwise using this skill, you acknowledge that you have read and understood this disclaimer.

## What this skill is

- A working, engineer-facing interpretation of the Infocomm Media Development Authority's (IMDA) *Model AI Governance Framework for Agentic AI*, as it applies to designing, building, testing and operating agentic AI systems
- A supplementary interpretation of IMDA and the AI Verify Foundation's *Model AI Governance Framework for Generative AI* (2024), applied to the model, data and generated content underneath an agent and to generative features that take no actions
- A set of layered patterns, checklists and templates engineers can use when designing agents, reviewing designs, and preparing releases
- A section-by-section map from the framework to those patterns

## What this skill is **not**

- **Not affiliated with IMDA.** The maintainers are not affiliated with, endorsed by, or speaking for IMDA, the Cyber Security Agency of Singapore, GovTech, the AI Verify Foundation, or any other government body. Nothing here is an official interpretation.
- **Not law.** The Model AI Governance Frameworks for Agentic AI and for Generative AI are voluntary guidance. This skill does not create obligations, and alignment with it does not discharge obligations under statutes, regulations, regulator notices, or contracts that do bind you — for example the Personal Data Protection Act 2012, sector-specific rules, or customer agreements.
- **Not authoritative.** Where this skill conflicts with the official framework, **the official framework wins.** The content is a summary written by engineers for engineers; it may be incomplete, inaccurate or out of date.
- **Not an audit, assessment or certification.** An alignment review produced with this skill is an engineering opinion about a design. It is not an attestation that any system is safe, secure, fair, compliant, or "IMDA-aligned" in any official sense. Do not represent it as one.
- **Not a security assessment.** The skill points to security practices but is no substitute for threat modelling, penetration testing and red teaming by qualified people.
- **Not insurance.** No indemnity, warranty or compensation is provided if you suffer loss in connection with its use.

## How this skill operates

- **Documentation first.** The skill itself is a collection of markdown files.
- **One optional local script.** The repository also ships `scripts/ai-governance-check-changed-files.py`, a changed-file tripwire that runs only when you invoke it, reads your local git diff, prints to your terminal, and sends nothing anywhere. Release tooling under `scripts/` and `.github/` is for maintaining this repository.
- **No data collection, no telemetry.** Reading or applying the skill transmits nothing to the maintainers. Analysis runs inside your own agent session and your own repository.
- If a downstream tool wraps this skill in a system that does collect or transmit data, disclosure of that collection is the downstream tool's responsibility.

## Use at your own risk

You accept full responsibility for any decision you make in reliance on this content. You agree that:

1. You will independently verify any framework section reference or quotation against the official IMDA publication before relying on it.
2. You will involve your organisation's risk, security, legal and compliance owners before treating a design as approved or a risk as accepted.
3. You will not represent or hold out this skill, or any review produced with it, as an official, authoritative or certified assessment to your users, customers, investors, regulators or anyone else.
4. You waive any claim against the maintainers and contributors of this repository arising from your use of, or reliance on, the content.

## Authoritative sources

- **Model AI Governance Framework for Agentic AI** — Infocomm Media Development Authority (IMDA): [www.imda.gov.sg](https://www.imda.gov.sg)
- **Model AI Governance Framework for Generative AI** — IMDA and the AI Verify Foundation: [IMDA factsheet](https://www.imda.gov.sg/resources/press-releases-factsheets-and-speeches/factsheets/2024/gen-ai-and-digital-foss-ai-governance-playbook); [PDF](https://aiverifyfoundation.sg/wp-content/uploads/2026/06/Model-AI-Governance-Framework-for-Generative-AI-19-June-2024.pdf)
- **Feedback channel published in the agentic framework:** [go.gov.sg/mgfagentic-feedback](https://go.gov.sg/mgfagentic-feedback)
- **Companion material** referenced by the framework is published by its respective owners (CSA, GovTech, AI Verify Foundation).

## Currency and accuracy

[`skills/imda-ai-governance/frameworks/sg-mgf-agentic/README.md`](skills/imda-ai-governance/frameworks/sg-mgf-agentic/README.md) and [`skills/imda-ai-governance/frameworks/sg-mgf-genai/README.md`](skills/imda-ai-governance/frameworks/sg-mgf-genai/README.md) record each framework version reflected and when it was last verified. The generative-AI notes were written from an extracted copy of the PDF; their page references are due a check against the original. IMDA describes the framework as a living document. **Use the dates to judge how much trust to extend to the content; never assume currency.**

If you find content that is out of date or inconsistent with the framework, please open an issue or pull request — see [CONTRIBUTING.md](CONTRIBUTING.md). Reporting an issue creates no obligation on the maintainers to fix it within any time, or at all.

## Contributors

Contributors warrant only what [CONTRIBUTING.md](CONTRIBUTING.md#contributor-warranties-and-liability) sets out: authorship or the right to license under MIT, non-infringement, and good-faith reflection of the framework at the time of contribution. They make no warranty as to accuracy, completeness or fitness for purpose. Neither the maintainers nor any individual contributor accepts liability arising from contributed content.

## Copyright in source materials

The MIT licence accompanying this repository ([LICENSE](LICENSE)) covers **only the original commentary, structure, organisation, layered framework, checklists, templates, scripts and analysis** contributed by the maintainers and contributors. It does **not** purport to grant any rights in the framework or other source materials.

Specifically:

1. **The Model AI Governance Framework for Agentic AI is published by IMDA and remains IMDA's material**, and **the Model AI Governance Framework for Generative AI is published by IMDA and the AI Verify Foundation and remains their material**, each subject to its publisher's terms of use. The case studies within it were contributed by, and describe, the named organisations.
2. **Quotations in this skill are short operative phrases, cited and attributed to the relevant framework, reproduced for educational and engineering-reference purposes under fair-dealing principles** (in Singapore, the fair-use provisions of the Copyright Act 2021). The skill does not republish either framework in full, does not reproduce its diagrams, and does not substitute for the official text. Case-study material is summarised as engineering patterns, not reproduced.
3. **Anyone wishing to redistribute quotations** beyond similar non-commercial educational or engineering-reference use, or to reproduce substantial portions of either framework, **must consult the publisher's terms** and obtain permission where required. The MIT licence on this repository does not — and cannot — grant such rights on IMDA's behalf.
4. **The maintainers make no representation** that quotations are reproduced under any specific licence or permission. The fair-dealing basis above is the maintainers' good-faith view, not a legal opinion or warranty.

If you represent IMDA or another rights-holder and believe any content here exceeds fair dealing, please open an issue — see [CONTRIBUTING.md](CONTRIBUTING.md) and [SECURITY.md](SECURITY.md).

## Liability

The maintainers and contributors accept **no liability** for any decision made or action taken in reliance on this content. The MIT licence contains the full warranty disclaimer and limitation of liability — see [LICENSE](LICENSE). To the maximum extent permitted by applicable law, the maintainers' and contributors' aggregate liability for any claim arising from your use of this skill is limited to **zero**.

## Jurisdiction of this disclaimer

This disclaimer is governed by the laws of Singapore, without regard to conflict-of-laws principles. Any dispute arising from or in connection with this disclaimer or the use of this skill is subject to the exclusive jurisdiction of the courts of Singapore.

## Changes to this disclaimer

The maintainers may update this disclaimer at any time without notice. The version in force when you use the skill is the version that applies.
