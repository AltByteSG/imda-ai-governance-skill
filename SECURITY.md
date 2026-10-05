# Security Policy

This repository is **documentation plus one optional local script** — there is no service to attack and no user data held by the project. The content shapes how engineers govern AI agents, so accuracy and integrity matter.

## Where to report

Everything goes through this repository's GitHub issues and pull requests.

| Concern | What to do |
|---|---|
| **Content that could lead an engineer into an unsafe design** (e.g. a recommendation that weakens an approval checkpoint, a wrong section reference that changes the expectation, guidance that would open an injection path) | Open an issue with the `governance-concern` label. Cite the framework section or authoritative source. |
| **Suspected malicious pull request** (e.g. a PR that subtly weakens guidance, or changes the checker to skip files) | Comment on the PR. Maintainers review every PR before merge. |
| **A bug in `scripts/ai-governance-check-changed-files.py`** that causes missed detections | Open an issue with a minimal reproduction. |
| **Compromised maintainer account / repo takeover** | Report to **GitHub Support** at [support.github.com](https://support.github.com). |
| Typo, formatting, broken link, stale reference | Open an issue or PR. |
| Disagreement with interpretation of the framework | Open an issue with sources. |

## What to expect

- `governance-concern` issues are triaged ahead of typo and formatting reports.
- We aim to respond to high-priority reports within **5 business days** and publish a correction within **30 days** of confirming the issue. These are targets, not commitments.

## What we ask of reporters

- **For high-priority content issues, please don't escalate publicly before opening an issue and giving maintainers a reasonable chance to fix it.**
- **Cite authoritative sources.** "Section 2.2.2 says X but the file says Y" is actionable in minutes.
- **Be specific.** Filename, line number, and the exact framework wording.

## What this repository is **not**

- **Not a vulnerability disclosure programme** for any product or agent that uses this skill. Contact that product's vendor.
- **Not an incident hotline.** If an agent in your organisation has caused harm, follow your own incident process and any statutory duties (e.g. PDPA breach notification) — see [`checklists/agent-incident.md`](skills/imda-ai-governance/checklists/agent-incident.md).
- **Not IMDA.** For feedback on the framework itself, use IMDA's channel: [go.gov.sg/mgfagentic-feedback](https://go.gov.sg/mgfagentic-feedback).

## Disclaimer

Reporting an issue creates no contractual or professional advisory relationship. See [`DISCLAIMER.md`](DISCLAIMER.md).
