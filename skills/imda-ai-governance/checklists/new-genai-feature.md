# Checklist — New Generative AI Feature (No Tools or Actions)

> ⚠ **Reference material only — not legal or regulatory advice.** See [DISCLAIMER.md](https://github.com/AltByteSG/imda-ai-governance-skill/blob/main/DISCLAIMER.md). Verify against the official IMDA publication and involve your risk and compliance owners.

Use for a generative feature that produces content but takes no actions: a chat assistant without tools, a summariser, a RAG Q&A bot, a drafting or content-generation feature. The output is a filled-in [`SYSTEM_CARD.md`](../templates/SYSTEM_CARD.md.template). Framework basis: the Model AI Governance Framework for Generative AI (`sg-mgf-genai`) — see [`frameworks/sg-mgf-genai/README.md`](../frameworks/sg-mgf-genai/README.md).

Items are numbered so a review can cite them (e.g. "fails 4.3"). Items marked **(M+)** apply at medium tier and above; **(H)** at high tier.

## 0. Do this first: is it actually agentic?

The agentic framework is primary. If any answer below is "yes", **stop and use [`new-agent.md`](new-agent.md)** — it covers this checklist's model-level items by reference to the same layers.

- [ ] 0.1 Can the model's output decide whether, or with what arguments, a tool, API, function or MCP server that changes state is called (writes, sends, books, pays, deletes, files a ticket)?
- [ ] 0.2 Does it choose its own steps or tools across more than one model call towards a goal `[MGF §1.1]`?
- [ ] 0.3 Does the model choose what is sent, or to whom, when it acts towards anyone else (an email, a message, a post), even as a "draft" that is auto-sent?
- [ ] 0.4 Is a tool, plug-in or "actions" capability on the roadmap for this feature? If so, design for [`new-agent.md`](new-agent.md) now; the first write-capable tool brings it into scope.
- [ ] 0.5 Read-only retrieval (search over a fixed corpus) does **not** by itself make it agentic. Nor does a fixed pipeline that always does the same thing with the output (a scheduled job that posts whatever was generated): the model isn't choosing the action `[MGF §1.1]`. Publishing generated content without review is still a finding, under 6.x here and G.8 in a design review. Record the answer to 0.1–0.4 in the system card's **Agentic?** field.

## 1. Use case, owner and risk ([layer 01](../layers/01-accountability.md), [layer 02](../layers/02-use-case-and-risk.md))

- [ ] 1.1 Purpose, users and out-of-scope uses written in a few sentences.
- [ ] 1.2 Technical owner and use-case owner named; approval to build recorded.
- [ ] 1.3 Risk tier assigned. Without actions, impact comes from the domain (advice in health, finance, legal, hiring), who reads the output (public vs internal), sensitive data in prompts or corpus, and whether people act on the output without checking. `[Practice]` As a rule of thumb, take the highest row that applies:

  | Tier | Typical generative feature |
  |---|---|
  | **High** | Output published externally under your name; advice people act on in a high-stakes domain; personal, confidential or regulated data in the corpus or prompts |
  | **Medium** | Internal users rely on the output for work decisions; internal-only confidential data; generated content shared beyond the requester |
  | **Low** | Internal drafting or summarising over non-sensitive data, always reviewed by the person who asked |

- [ ] 1.4 Model-level threats added to the threat model: prompt attacks, RAG / data poisoning, extraction, inversion, malicious weights as applicable ([layer 02](../layers/02-use-case-and-risk.md#model-level-threats)).
- [ ] 1.5 Residual risk written in plain words and accepted by the use-case owner.

## 2. Model and provider ([layer 01](../layers/01-accountability.md#model-provider-terms-and-shared-responsibility), [layer 05](../layers/05-technical-controls.md#model-supply-chain))

- [ ] 2.1 Model and exact version pinned; no floating alias in production config.
- [ ] 2.2 Shared-responsibility split recorded for the model type (closed / open / open-weights) `[MGF-GenAI Accountability, p.7]`.
- [ ] 2.3 Model obtained from a reputable, allowlisted source `[MGF-GenAI Accountability, p.8]`; self-hosted weights checksum- or signature-verified, in a safe format.
- [ ] 2.4 Provider terms checked: data retention, training on your inputs, sub-processors, region, model-change notice.
- [ ] 2.5 Indemnity and insurance questions asked and answers recorded, including "none" `[MGF-GenAI Accountability, p.8]`.

## 3. Data and grounding ([layer 10](../layers/10-data-and-grounding.md))

- [ ] 3.1 Every fine-tuning set, RAG corpus, few-shot bank and eval set has passed [`new-dataset-or-corpus.md`](new-dataset-or-corpus.md).
- [ ] 3.2 Retrieval enforces the requesting user's access rights at query time (M+).
- [ ] 3.3 Personal data in prompts, corpus or logs assessed with the `personal-data-protection` skill (if installed) or your DPO.
- [ ] 3.4 Staleness and deletion propagation defined for every index, with a stated maximum lag.

## 4. Baseline safety controls ([layer 05](../layers/05-technical-controls.md#genai-baseline-safety))

- [ ] 4.1 Grounding: answers cite sources; behaviour when retrieval finds nothing is "don't know" or escalate, not free generation `[MGF-GenAI Trusted Development, p.13]`.
- [ ] 4.2 Input filters for unsafe prompts and injection `[MGF-GenAI Security, p.22]`.
- [ ] 4.3 Output filters for harmful content, PII and secrets; thresholds tuned on your data.
- [ ] 4.4 If you fine-tune: safety examples included, and the safety suite re-run on each checkpoint.
- [ ] 4.5 Structured outputs validated against a schema before display or downstream use.
- [ ] 4.6 Any downstream system that consumes the output treats it as untrusted input. (If the output triggers an action automatically, return to section 0.)

## 5. Evaluation ([layer 07](../layers/07-testing-and-evaluation.md#benchmarks-evaluation-dimensions-and-external-assurance))

- [ ] 5.1 Suites for robustness, factuality, bias, toxicity and data governance on use-case data `[MGF-GenAI Trusted Development, p.15]`; sector-specific evals where they exist.
- [ ] 5.2 Pass thresholds set before running; multiple runs per scenario; results recorded against exact model, prompt, corpus and filter versions.
- [ ] 5.3 Benchmarks run on every change; red teaming before first external exposure (M+).
- [ ] 5.4 External or third-party testing considered and the decision recorded (H).

## 6. Users and content ([layer 09](../layers/09-end-user-transparency.md))

- [ ] 6.1 Users told at the point of interaction that they are using AI, and what it is for and not for.
- [ ] 6.2 Generated content labelled where it is shown or sent to people; C2PA-style provenance and watermarking for published media; provenance preserved through edits `[MGF-GenAI Content Provenance, p.23–25]`.
- [ ] 6.3 Data notice: what is stored, for how long, who receives it, whether it trains models.
- [ ] 6.4 No human persona; help text discourages anthropomorphising and says the system can be wrong `[MGF-GenAI AI for Public Good, p.29]`.
- [ ] 6.5 "Report a problem" path from the UI, captured with a trace id.

## 7. Operations ([layer 08](../layers/08-monitoring-and-operations.md))

- [ ] 7.1 Prompts, outputs, retrieved chunk ids and filter decisions logged with personal-data hygiene; enough retained to reproduce an output (forensic retention).
- [ ] 7.2 Alerts on filter-block spikes, quality drift and abuse patterns (including systematic querying for extraction).
- [ ] 7.3 Public vulnerability and safety reporting channel covers this feature; disclosure window stated `[MGF-GenAI Incident Reporting, p.17]`.
- [ ] 7.4 Severity thresholds for external incident reporting defined; statutory clocks noted.
- [ ] 7.5 Change triggers agreed: model or version, prompt, fine-tune, corpus, filter changes go through [`change-review.md`](change-review.md).
- [ ] 7.6 `[Practice]` (optional) compute or energy per feature recorded; smallest adequate model chosen.

## 8. Record and sign off

- [ ] 8.1 [`SYSTEM_CARD.md`](../templates/SYSTEM_CARD.md.template) filled in, all seven disclosure areas `[MGF-GenAI Trusted Development, p.14]`.
- [ ] 8.2 `.ai-governance.json` lists `sg-mgf-genai` in `frameworks`, and `riskTier` is set.
- [ ] 8.3 Before release, run the applicable parts of [`pre-deployment.md`](pre-deployment.md) (paperwork, tests, runtime readiness).
