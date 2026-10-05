# Checklist — Change Review for a Deployed Agent

> ⚠ **Reference material only — not legal or regulatory advice.** See [DISCLAIMER.md](../../../DISCLAIMER.md). Verify against the official IMDA publication and involve your risk and compliance owners.

Use for any change to a deployed agent. In complex agent systems small modifications can cascade `[MGF §2.3.3]`; the framework expects defined change triggers and review depth scaled to risk.

## 1. Is this a trigger? `[MGF §2.3.3]`

- [ ] **Technical** — model or model version (including a provider-side change), prompt / instructions, tool added / removed / re-scoped, MCP server added or updated, memory design, orchestration framework or SDK upgrade, new agent in the system.
- [ ] **Environmental** — new user population or channel, new domain, new data source, changed business context.
- [ ] **Performance** — anomalous behaviour, eval regression, incident, oversight-metric drift.
- [ ] **Regulatory** — new law or guidance, a new version of the MGF.

If none apply, this isn't an agent change. Otherwise continue.

## 2. Categorise it `[MGF §2.3.3]`

| Category | Examples | Go to |
|---|---|---|
| **Minor** | Prompt wording within the same scope and tools; UI copy; extra logging | Section 3 |
| **Material** | Model change; new or re-scoped tool; autonomy change; new data source; new user population; new agent in a multi-agent system | Sections 3 and 4 |
| **Critical** | Anything affecting high-stakes decisions or irreversible actions; removing or loosening an approval checkpoint; raising a limit; widening permissions | Sections 3, 4 and 5 |

When unsure between two categories, take the higher.

## 3. Minor — all changes

- [ ] Change is version-controlled (prompts, tool definitions, policies, model pins).
- [ ] Peer review.
- [ ] Regression evals pass at release-gate thresholds ([`pre-deployment.md`](pre-deployment.md) section 2, policy and bounds suites at minimum).
- [ ] Agent card version bumped.

## 4. Material — full governance review

- [ ] Re-tier: does the change alter impact or likelihood ([layer 02](../layers/02-use-case-and-risk.md))?
- [ ] Threat model updated for new tools, sources or agents.
- [ ] Identity and scopes updated and still least-privilege ([layer 04](../layers/04-identity-and-authorisation.md)).
- [ ] Approval matrix reviewed ([layer 06](../layers/06-human-oversight.md)).
- [ ] Full pre-deployment gate run ([`pre-deployment.md`](pre-deployment.md)).
- [ ] Staged rollout for the change, not a direct full release ([layer 08](../layers/08-monitoring-and-operations.md#gradual-rollout)).
- [ ] User-facing capability statement and data notice updated if behaviour or data use changed ([layer 09](../layers/09-end-user-transparency.md)).
- [ ] Technical owner and use-case owner sign off.

## 5. Critical — re-assess risk

- [ ] Immediate risk re-assessment before rollout `[MGF §2.3.3]`.
- [ ] Residual risk re-accepted by the use-case owner, with the risk / security reviewer.
- [ ] Red team where the change opens a new attack path.
- [ ] Rollback plan tested.

## 6. Record

- [ ] Change, category, reviewers, eval results and approval recorded on the agent card or in the PR description, citing `[MGF §2.3.3]`.
