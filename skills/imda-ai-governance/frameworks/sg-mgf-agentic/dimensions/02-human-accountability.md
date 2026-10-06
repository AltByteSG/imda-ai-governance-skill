# §2.2 — Make Humans Meaningfully Accountable

> ⚠ **Reference material only — not legal or regulatory advice.** See [DISCLAIMER.md](https://github.com/AltByteSG/imda-ai-governance-skill/blob/main/DISCLAIMER.md). Verify against the official IMDA publication and involve your risk and compliance owners.
>
> **How to read this file:** the expectation paragraphs restate the framework, with its section. The **Engineering effect** and **Evidence** paragraphs are this skill's interpretation — treat them as `[Practice]`, not as IMDA requirements.

The framework's position is that **deploying organisations and the humans overseeing agents remain accountable for the agents' actions**. Dimension 2 is about making that accountability real: clear owners across the value chain, and human oversight designed so that it still works after the hundredth approval.

## §2.2.1 — Clear allocation of responsibilities

### Know your position in the value chain

**Expectation:** the simplified value chain is model developers, tooling providers (e.g. MCP, APIs), platform providers, system providers / app developers, deployers and end users. Organisations may hold several roles at once — building and deploying your own agent makes you system provider *and* deployer. (The platform / system-provider split is new in v1.5.)

**Engineering effect:** `[Practice]` the framework does not split duties by role, but in practice the role decides which expectations land on your team: building the agent puts design, testing and controls with you; deploying it puts use-case approval, oversight, monitoring and user communication with you. Most product teams do both.

**Evidence:** the role(s) recorded in `.ai-governance.json` or the agent card.

### Allocate responsibilities inside the organisation

**Expectation:** the framework illustrates (not prescribes) four groups:

| Group | Illustrative responsibilities |
|---|---|
| **Key decision makers** (board, C-suite, department heads) | Goals for agent use; **permitted use cases, including limits on agent data access**; governance approach, risk frameworks, escalation processes |
| **Product teams** (PMs, designers, AI and software engineers) | Agent design and requirements, feature controls and phased rollouts; development, pre-deployment testing and post-deployment monitoring; educating users |
| **Cybersecurity teams** | Baseline security guardrails and secure-by-design templates; regular red teaming and threat modelling |
| **Users** | Responsible use; training; following usage policies; reporting bugs and issues |

**Engineering effect:** product teams carry the bulk of dimension 3. If the security team has published agent guardrail templates, the design should use them or explain why not.

**Evidence:** a named owner per agent; the approving forum for the use case; who runs red-teaming.

### Build adaptive governance capability

**Expectation:** teams should build internal capability to understand improvements and limitations in agentic technology (e.g. new modalities like computer use, new evaluation frameworks) so governance can adapt quickly.

**Evidence:** someone owns tracking framework and model changes; change triggers in [layer 08](../../../layers/08-monitoring-and-operations.md#change-management) include regulatory and technology changes.

### Allocate responsibilities with external parties

**Expectation:** when working with model developers, agentic AI providers, or hosts of external MCP servers or tools:

- **Clarify obligations in contracts and T&Cs** — especially security arrangements, performance guarantees and data protection. Where gaps exist, reassess whether the deployment still meets risk tolerance.
- **Address third-party opacity** — require disclosures on agent capabilities and data handling; request and evaluate technical features such as scoped API keys, per-agent identity tokens, and logging of tool calls and access history. Where those are lacking, consider alternatives, in-house solutions, or **scoping the use case down** (e.g. no sensitive data).

**Evidence:** the vendor assessment from [`checklists/third-party-agent.md`](../../../checklists/third-party-agent.md); the contract clauses; the compensating scope-down decision if the vendor fell short.

### Give end users enough to hold you accountable

**Expectation:** users should get sufficient information to hold the organisation accountable and to understand their own responsibilities — detailed under §2.4.

## §2.2.2 — Design for meaningful human oversight

The framework's three-part model: define checkpoints → train and audit approvers → complement with automated monitoring.

### Define checkpoints that require human approval

**Expectation:** checkpoints or action boundaries requiring approval, especially before sensitive actions:

- **High-stakes actions and decisions** — editing sensitive data, final decisions in high-risk domains (healthcare, legal), actions that may trigger liability.
- **Irreversible actions** — permanently deleting data, sending communications, making payments.
- **Outlier or atypical behaviour** — accessing systems outside work scope; choices far from the norm (the framework's example: a delivery route twice the median distance).
- **User-defined** — users may set their own boundaries beyond organisation-defined ones (e.g. purchases above an amount).

**Evidence:** the action-to-approval matrix for the agent, enforced in code at the tool or workflow layer. See [layer 06](../../../layers/06-human-oversight.md).

### Make approval requests usable

**Expectation:** keep requests **contextual and digestible while making the risk clear** — short and clear rather than raw logs, but including useful data such as the associated risk or a confidence score. Match the **form of input** to the decision: approve / reject for simple actions; edit-the-plan for complex ones; **written justification** for high-risk approvals.

**Evidence:** the approval UI or message format; screenshots or samples.

### Keep oversight effective over time

**Expectation:** measures against alert fatigue, automation bias and anthropomorphic influence:

- **Audit oversight effectiveness** by tracking **human override rate** (low may signal rubber-stamping) and **review response time** (short may signal automation bias or fatigue), and by finding **outlier reviewers** whose patterns deviate from the norm.
- **Train overseers** on common failure modes — inconsistent reasoning, outdated policies — and on the fact that **chain-of-thought is not necessarily a faithful explanation** of the agent's actions.
- **Ensure reviewers have the domain expertise** to evaluate what they approve (the framework's example: people "vibe coding" may lack the expertise to review the generated code).

**Evidence:** an oversight dashboard or periodic report with override rates and response times; reviewer training material; a statement of what expertise each approval queue requires.

### Complement with automated monitoring — and fail closed

**Expectation:** automated real-time monitoring to escalate anomalies: alerts on logged events (attempted unauthorised access, repeated failed tool calls), anomaly detection on trajectories, agents monitoring agents, and **denying action by default when approval infrastructure fails** — when supervisors are unreachable, or when the agent attempts a new action with no approval policy.

**Evidence:** alert rules on logged events; and, for the deny-by-default measure, the behaviour of the approval path when the approver service is down or times out (`[Practice]` it should block, not proceed) and the handling of tools or actions not in the approval policy (deny, not allow).
