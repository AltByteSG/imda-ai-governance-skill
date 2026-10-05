# Layer 10 — Data and Grounding

> ⚠ **Reference material only — not legal or regulatory advice.** See [DISCLAIMER.md](../../../DISCLAIMER.md). Verify against the official IMDA publication and involve your risk and compliance owners.

The data underneath the model: fine-tuning sets, RAG corpora and their indexes, few-shot example banks, and evaluation datasets. An agent's behaviour is bounded by its tools ([layer 03](03-architecture-and-bounding.md)); its *answers* are bounded by this data. Framework basis: the GenAI framework's Data dimension `[MGF-GenAI Data, p.9–11]` and, for disclosure, `[MGF-GenAI Trusted Development, p.14]`. For an agent, this layer supplements the agentic layers; it does not replace any of them. Framework notes: [`frameworks/sg-mgf-genai/dimensions/02-data.md`](../frameworks/sg-mgf-genai/dimensions/02-data.md).

Most teams don't pre-train models. This layer is about the data **you** choose, ingest and maintain. For the base model's training data, rely on what the model provider discloses and record it in the [`SYSTEM_CARD.md`](../templates/SYSTEM_CARD.md.template).

## Keep a dataset register

`[MGF-GenAI Data, p.11]` names "best practices in data governance" and data quality control. `[Practice]` One register entry (or datasheet — see below) per dataset, corpus or index, covering:

| Field | Example |
|---|---|
| **Purpose and use** | Fine-tune / RAG corpus / few-shot bank / eval set; which features use it |
| **Owner** | Team accountable for content, refresh and deletion |
| **Sources** | Systems, URLs, vendors, user uploads — with the date each was pulled |
| **Licence and rights basis** | Owned / licensed (terms link) / public with terms / user-provided under T&C |
| **Personal data** | None / present — categories, PETs applied, link to the PDPA assessment |
| **Processing** | Cleaning, filtering, de-duplication, annotation, chunking and embedding model |
| **Version and refresh** | Snapshot id or index build id; refresh cadence; staleness rule |
| **Known gaps and biases** | Under-represented languages, groups, time periods |

An index without a register entry is an unowned corpus — the data counterpart of agent sprawl.

## Provenance, licence and copyright

`[MGF-GenAI Data, p.11]` treats copyright as an open policy question; it does not settle what you may use. `[Practice]` Make the rights question a build gate, not a later clean-up:

- **Record where every document came from** at ingestion time, as metadata on each chunk (source URI, retrieval date, licence tag). You cannot answer a takedown or a licence query for an index that dropped its provenance.
- **Check terms before scraping or ingesting** third-party content. Website terms, robots directives, API terms and licences can restrict text-and-data-mining or storage. Unknown licence = don't ingest, or escalate to legal.
- **Vendor and partner data** — confirm the contract permits use for fine-tuning or retrieval, not just display.
- **Model-provider data** — record what the provider says about the base model's training data and any IP indemnity ([layer 01](01-accountability.md#model-provider-terms-and-shared-responsibility)).

## Personal data in datasets and indexes

`[MGF-GenAI Data, p.10]` says personal-data law applies to generative AI and points to privacy-enhancing technologies (PETs). This skill does not restate the law: **run the `personal-data-protection` skill** (if installed) for PDPA purpose, consent, retention and transfer questions. `[Practice]` engineering defaults:

- **Minimise before ingesting.** Strip or tokenise identifiers the feature doesn't need. Detect PII at ingestion (pattern and NER-based scanners) and fail the build on unexpected hits.
- **Pick the PET to the use** — redaction or pseudonymisation for RAG and fine-tuning text; synthetic data for evals and tests; aggregation or differential privacy where you only need statistics. Record which PET and why.
- **Don't fine-tune on personal data you can't later remove.** Deleting a record from a fine-tuned model generally means retraining. Prefer retrieval (deletable) over fine-tuning (baked in) for personal or fast-changing content.
- **Enforce access at retrieval.** A RAG index built from documents with different access rights must filter by the requesting user's permissions at query time, not rely on the prompt. This is the confused-deputy problem from [layer 04](04-identity-and-authorisation.md#no-more-than-the-delegating-human) in data form.

## Quality, annotation and cleaning

`[MGF-GenAI Data, p.11]`: data quality control; annotate datasets "consistently and accurately"; data cleaning such as debiasing and removing inappropriate content. `[Practice]`:

- **Annotation guidelines in the repo**, versioned with the dataset. Measure inter-annotator agreement on a sample and re-train annotators (or fix the guideline) when it drops.
- **Cleaning pipeline as code** — de-duplication, language and format filters, toxicity and inappropriate-content filters, PII scan — so it re-runs identically on refresh.
- **Representation check** — compare the dataset's distribution (languages, regions, user groups, topics) with the population the feature serves; record gaps. Debiasing is a choice to record, not an implicit property of a "clean" set.
- **Eval sets are held out** from fine-tuning and few-shot banks, and checked for contamination (overlap with training or retrieval content).

## Document it

`[MGF-GenAI Trusted Development, p.14]` lists "data used" as the first disclosure area. `[Practice]` Write a short datasheet per dataset — motivation, composition, collection, processing, uses, distribution, maintenance — and link it from the dataset register and the [`SYSTEM_CARD.md`](../templates/SYSTEM_CARD.md.template).

## Staleness and deletion propagation

`[Practice]` Retrieval data goes stale and gets deleted at the source; the index must follow:

- **Every chunk carries a source id and version.** Updates and deletions at the source trigger re-index or tombstone of the matching chunks — on an event or a short schedule, with a stated maximum lag.
- **Expiry metadata** for time-bound content (policies, prices, rates); retrieval filters out expired chunks deterministically ([layer 05](05-technical-controls.md#fix-data-problems-deterministically)).
- **Deletion reaches every copy** — vector store, keyword index, caches, eval snapshots, backups on their retention cycle, and any fine-tuning set built from it. Test it: delete a known record and assert it is no longer retrievable.

## Poisoning of RAG and fine-tuning data

`[Practice]` Data poisoning is a standard GenAI threat, catalogued in MITRE ATLAS, which the framework points to for threat modelling `[MGF-GenAI Security, p.22]`. A document that reaches the index is an untrusted source for every query that retrieves it. `[Practice]`:

- **Add each ingestion source to the threat model** as an untrusted source ([layer 02](02-use-case-and-risk.md#threat-modelling)); for an agent, trace whether retrieved text can reach a write tool.
- **Restrict who can write to the corpus** — public wikis, shared drives, ticket bodies and user uploads are writable by many. Prefer curated sources; separate indexes by trust level.
- **Scan at ingestion** for embedded instructions, hidden text and anomalous content; quarantine rather than silently index.
- **Treat retrieved text as data, not instructions**, and apply the boundary controls in [layer 05](05-technical-controls.md#tool-controls).
- **Verify fine-tuning data integrity** — hash the snapshot used, keep it immutable, and re-run safety evals after every fine-tune ([layer 07](07-testing-and-evaluation.md#benchmarks-evaluation-dimensions-and-external-assurance)).

## Checklist

Run [`checklists/new-dataset-or-corpus.md`](../checklists/new-dataset-or-corpus.md) whenever you add or materially change a dataset, corpus or index. A new RAG source on a deployed agent is also a change-review trigger ([layer 08](08-monitoring-and-operations.md#change-management)).
