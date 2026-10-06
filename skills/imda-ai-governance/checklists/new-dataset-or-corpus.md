# Checklist — Adding a Fine-Tuning Set, RAG Corpus or Index, or Evaluation Set

> ⚠ **Reference material only — not legal or regulatory advice.** See [DISCLAIMER.md](https://github.com/AltByteSG/imda-ai-governance-skill/blob/main/DISCLAIMER.md). Verify against the official IMDA publication and involve your risk and compliance owners.

Use whenever you add, or materially change, data that shapes what a model says: a fine-tuning or adapter dataset, a RAG corpus and its index, a few-shot example bank, or an evaluation set. Layer: [layer 10](../layers/10-data-and-grounding.md). Framework basis: `[MGF-GenAI Data, p.9–11]` — see [`frameworks/sg-mgf-genai/dimensions/02-data.md`](../frameworks/sg-mgf-genai/dimensions/02-data.md).

For a deployed agent or feature, a new data source is also a change-review trigger — run [`change-review.md`](change-review.md) alongside this. If the corpus is reached through a tool the agent calls, run [`new-tool-or-integration.md`](new-tool-or-integration.md) too.

Items are numbered so a review can cite them. Items marked **(M+)** apply at medium tier and above.

## 1. Purpose and ownership

- [ ] 1.1 Dataset type recorded: fine-tune / RAG corpus / few-shot bank / eval set.
- [ ] 1.2 Purpose and the features or agents that use it written down.
- [ ] 1.3 Owner named, accountable for content, refresh and deletion.
- [ ] 1.4 Entry added to the dataset register ([layer 10](../layers/10-data-and-grounding.md#keep-a-dataset-register)).
- [ ] 1.5 For personal or fast-changing content, retrieval preferred over fine-tuning (retrieval can be deleted from; a fine-tune generally can't).

## 2. Provenance and rights

- [ ] 2.1 Every source listed with retrieval date.
- [ ] 2.2 Licence or rights basis recorded per source: owned / licensed / public with terms / user-provided under T&C.
- [ ] 2.3 Terms checked for text-and-data-mining, storage and model-use restrictions; unknown licence escalated, not ingested.
- [ ] 2.4 Vendor or partner contracts permit this use (fine-tuning or retrieval, not just display).
- [ ] 2.5 Provenance (source id, URI, licence tag, version) stored as metadata on every chunk or record.

## 3. Personal and confidential data

- [ ] 3.1 PII scan run at ingestion; unexpected hits fail the build.
- [ ] 3.2 Identifiers not needed for the purpose removed, redacted or pseudonymised; PET chosen and recorded `[MGF-GenAI Data, p.10]`.
- [ ] 3.3 Personal data assessed with the `personal-data-protection` skill (if installed) or your DPO; link recorded.
- [ ] 3.4 Confidential or access-restricted documents carry access labels, and retrieval filters by the requesting user's rights (M+).
- [ ] 3.5 Synthetic or de-identified data used for eval and test sets where real personal data isn't needed.

## 4. Quality, annotation and cleaning

- [ ] 4.1 Cleaning pipeline in code: de-duplication, format and language filters, inappropriate-content and toxicity filters `[MGF-GenAI Data, p.11]`.
- [ ] 4.2 Annotation guidelines versioned with the data; inter-annotator agreement measured on a sample `[MGF-GenAI Data, p.11]`.
- [ ] 4.3 Representation checked against the population the feature serves; gaps and any debiasing recorded.
- [ ] 4.4 Eval sets held out from fine-tuning and few-shot data; contamination check run.
- [ ] 4.5 Spot-check of a random sample by a person who knows the domain, with findings recorded.

## 5. Security and poisoning

- [ ] 5.1 Source added to the threat model as an untrusted source; for agents, source → sink paths traced ([layer 02](../layers/02-use-case-and-risk.md#threat-modelling)).
- [ ] 5.2 Who can write to each source identified; open-write sources (wikis, shared drives, uploads, tickets) justified or excluded.
- [ ] 5.3 Ingestion scans for embedded instructions, hidden text and anomalies; suspicious items quarantined `[MGF-GenAI Security, p.22]`.
- [ ] 5.4 Indexes separated by trust level where sources differ (M+).
- [ ] 5.5 Fine-tuning snapshot hashed and stored immutably; the hash is recorded against the checkpoint.

## 6. Freshness and deletion

- [ ] 6.1 Refresh cadence and maximum staleness stated.
- [ ] 6.2 Expiry metadata on time-bound content; retrieval filters expired chunks deterministically.
- [ ] 6.3 Source deletions propagate to vector store, keyword index, caches and derived sets within a stated lag.
- [ ] 6.4 Deletion tested: a known record deleted at source is no longer retrievable after the lag.

## 7. Evaluate and document

- [ ] 7.1 Evals re-run with the new data: factuality / faithfulness, PII leakage, bias, toxicity ([layer 07](../layers/07-testing-and-evaluation.md#benchmarks-evaluation-dimensions-and-external-assurance)).
- [ ] 7.2 After a fine-tune, safety suite re-run on the new checkpoint and compared with the base model.
- [ ] 7.3 Datasheet written (motivation, composition, collection, processing, uses, maintenance) and linked from the register.
- [ ] 7.4 [`SYSTEM_CARD.md`](../templates/SYSTEM_CARD.md.template) section 1 ("Data used") updated; agent card updated if an agent uses it.
