# Testing and Assurance (p.19–20)

> ⚠ **Reference material only — not legal or regulatory advice.** See [DISCLAIMER.md](../../../../../DISCLAIMER.md). Verify against the official IMDA and AI Verify Foundation publication and involve your risk and compliance owners.
>
> **How to read this file:** the expectation paragraphs restate the framework, with its dimension and page (page references come from an extracted summary — spot-check them against the PDF). The **Engineering effect** and **Evidence** paragraphs are this skill's interpretation — treat them as `[Practice]`, not as IMDA requirements.

This dimension is mostly about building an **ecosystem** of third-party testing. It overlaps with the evaluation expectations in [03-trusted-development-and-deployment](03-trusted-development-and-deployment.md); the engineering work lives there and in [layer 07](../../../layers/07-testing-and-evaluation.md).

## How to test — standardisation

**Expectation:** in the near term, third-party testing using the same benchmarks as internal testing; common benchmarks, methodologies and tooling; codify them through standards bodies such as ISO/IEC and IEEE `[MGF-GenAI Testing and Assurance, p.20]`.

**Engineering effect:** standards work is for the **ecosystem**. Engineering hook: `[Practice]` build your eval suite so an outside tester could rerun it — benchmarks named and versioned, prompts and datasets reproducible, harness scripted rather than manual, and prefer common open benchmarks and tooling over bespoke ones where they fit.

**Evidence:** an eval suite that runs from a single documented command, with benchmark names and versions recorded alongside results.

## Who to test — trusted accreditation

**Expectation:** a pool of qualified third-party testers, with eventual accreditation `[MGF-GenAI Testing and Assurance, p.20]`.

**Engineering effect:** addressed to the **ecosystem and accreditation bodies**. Engineering hook: for higher-risk systems, `[Practice]` budget for an independent test or red-team engagement and make the system testable by outsiders (a test environment, test credentials, logging that the tester can read).

**Evidence:** the external test report, if commissioned, and the findings tracked to closure.
