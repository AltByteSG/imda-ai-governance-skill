# Trusted Development and Deployment (p.12–15)

> ⚠ **Reference material only — not legal or regulatory advice.** See [DISCLAIMER.md](../../../../../DISCLAIMER.md). Verify against the official IMDA and AI Verify Foundation publication and involve your risk and compliance owners.
>
> **How to read this file:** the expectation paragraphs restate the framework, with its dimension and page (page references come from an extracted summary — spot-check them against the PDF). The **Engineering effect** and **Evidence** paragraphs are this skill's interpretation — treat them as `[Practice]`, not as IMDA requirements.

This is the dimension that lands most on builders: baseline safety practices during development, "food label" disclosure, and evaluation. For agents, the agentic framework's controls and testing expectations ([agentic §2.3](../../sg-mgf-agentic/dimensions/03-technical-controls.md)) sit on top of these — they test the workflow; this tests the model and its outputs.

## Development — baseline safety practices

**Expectation:** baseline practices include fine-tuning such as RLHF; risk assessment in the *"context of the use case"*; *"input and output filters"*; and RAG and few-shot learning to reduce hallucinations `[MGF-GenAI Trusted Development, p.13]`.

**Engineering effect:**

- **Risk assessment per use case**, not per model. The same model in a children's tutor and an internal code helper carries different risk. For agents, use the agentic risk factors `[MGF §2.1.1]` ([layer 02](../../../layers/02-use-case-and-risk.md)) and add the content-harm view from this framework.
- **Input and output filters** in the request path, enforced in code, not only in the system prompt. See [layer 05](../../../layers/05-technical-controls.md) and [06-security](06-security.md).
- **Grounding** (RAG, few-shot) where factuality matters, with the corpus governed as in [02-data](02-data.md) and [layer 10](../../../layers/10-data-and-grounding.md).
- **Fine-tuning** (RLHF or similar) mainly lands on model developers; if you fine-tune, you inherit the evaluation duty below.

**Evidence:** the use-case risk assessment; filter configuration and where it runs; the grounding design; fine-tuning records if any.

## Disclosure — "food labels"

**Expectation:** disclose in seven areas `[MGF-GenAI Trusted Development, p.14]`:

| Area | What an engineer fills in `[Practice]` |
|---|---|
| (a) Data used | Training / fine-tuning / grounding sources, at the level you know them |
| (b) Training infrastructure, incl. estimated environmental impact | Compute used for any training or fine-tuning you ran; provider's figure for the base model if published |
| (c) Evaluation results | Benchmarks and red-team findings, with dates and model versions |
| (d) Mitigations and safety measures | Filters, grounding, refusals, human review |
| (e) Risks and limitations | Known failure modes, languages and domains not supported |
| (f) Intended use | In-scope and out-of-scope uses |
| (g) User data protection | What user input is stored, for how long, whether it is used for training |

Calibrate disclosure against protecting proprietary information, give baseline transparency to all parties, and use *"model risk thresholds"* so that higher-risk systems get more oversight `[MGF-GenAI Trusted Development, p.14]`.

**Engineering effect:** keep one [system card](../../../templates/SYSTEM_CARD.md.template) per generative system (or extend the agent card), versioned with the code. User-facing disclosure is covered by [layer 09](../../../layers/09-end-user-transparency.md) and, for agents, [agentic §2.4](../../sg-mgf-agentic/dimensions/04-end-user-responsibility.md).

**Evidence:** the system card with all seven areas filled or marked "not known — reason"; the risk tier that decides how much oversight applies.

## Evaluation

**Expectation:** use both benchmarking and red teaming; a baseline set of safety tests `[MGF-GenAI Trusted Development, p.14]`; evaluations covering *"robustness, factuality, propensity to bias, toxicity generation and data governance"*, plus sector-specific evaluations where relevant `[MGF-GenAI Trusted Development, p.15]`.

**Engineering effect:** an eval suite per system with one section per named area, run in CI on every model, prompt, filter or corpus change, and a red-team pass before first release and on material change. For agents this is the model-and-output layer beneath the workflow tests `[MGF §2.3.2]`. See [layer 07](../../../layers/07-testing-and-evaluation.md).

**Evidence:** the eval suite and latest results by area (robustness, factuality, bias, toxicity, data governance, sector-specific); red-team report; the release gate thresholds.
