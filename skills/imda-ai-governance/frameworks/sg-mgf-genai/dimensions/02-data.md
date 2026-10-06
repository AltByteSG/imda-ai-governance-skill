# Data (p.9–11)

> ⚠ **Reference material only — not legal or regulatory advice.** See [DISCLAIMER.md](https://github.com/AltByteSG/imda-ai-governance-skill/blob/main/DISCLAIMER.md). Verify against the official IMDA and AI Verify Foundation publication and involve your risk and compliance owners.
>
> **How to read this file:** the expectation paragraphs restate the framework, with its dimension and page (page references come from an extracted summary — spot-check them against the PDF). The **Engineering effect** and **Evidence** paragraphs are this skill's interpretation — treat them as `[Practice]`, not as IMDA requirements.

Data is the input that most shapes what a generative system says. The dimension covers personal data, copyright and data quality. Much of it is addressed to policymakers; the data-quality part lands squarely on teams that train, fine-tune, evaluate or ground models. The agentic framework treats data mainly as something an agent *accesses* (least privilege, [agentic §2.1.2](../../sg-mgf-agentic/dimensions/01-assess-and-bound.md)); this dimension is about data the model *learns from or is grounded on*. Practice for both lives in [layer 10](../../../layers/10-data-and-grounding.md).

## Trusted use of personal data

**Expectation:** policymakers to *"articulate how existing personal data laws apply to generative AI"*, clarify consent requirements and give guidance on business practices; advance understanding of Privacy Enhancing Technologies (PETs) applied to AI `[MGF-GenAI Data, p.10]`.

**Engineering effect:** addressed to **policymakers**. Engineering hook: personal data law (PDPA or equivalent) already binds you regardless. `[Practice]` know whether personal data is in any training, fine-tuning, evaluation or grounding set, on what basis it is used, and whether a PET (de-identification, synthetic data, differential privacy) would serve. If the `personal-data-protection` skill is installed, run it.

**Evidence:** a personal-data entry per dataset or corpus (present / absent, basis, minimisation or PET applied). See [new-dataset-or-corpus checklist](../../../checklists/new-dataset-or-corpus.md).

## Balancing copyright with data accessibility

**Expectation:** open dialogue on copyright and data access `[MGF-GenAI Data, p.11]`.

**Engineering effect:** addressed to **policymakers and rights holders**. Engineering hook: `[Practice]` record the source and licence of every dataset and corpus you add, so the question can be answered when legal asks.

**Evidence:** source and licence fields in the dataset record.

## Facilitating access to quality data

### Data quality and governance

**Expectation:** data quality control measures and *"best practices in data governance"*; annotate training datasets *"consistently and accurately"*; use data analysis tools for *"data cleaning (e.g., debiasing and removing inappropriate content)"* `[MGF-GenAI Data, p.11]`.

**Engineering effect:** applies to anything you train or fine-tune on, and `[Practice]` equally to RAG corpora and evaluation sets, since they shape outputs just as directly. Each dataset needs an owner, provenance, a cleaning step (deduplication, removal of inappropriate content, bias checks) and, where labelled, an annotation guideline with an agreement check.

**Evidence:** per dataset or corpus — owner, source, version, cleaning steps run and their results, annotation guideline and inter-annotator agreement where relevant. Captured in the [system card](../../../templates/SYSTEM_CARD.md.template) "Data used" section.

### Trusted datasets

**Expectation:** expand the pool of trusted datasets; governments to curate representative local datasets `[MGF-GenAI Data, p.11]`.

**Engineering effect:** addressed to **governments**. Engineering hook: where such a curated local dataset exists for your domain, `[Practice]` consider it for evaluation of local-context performance.
