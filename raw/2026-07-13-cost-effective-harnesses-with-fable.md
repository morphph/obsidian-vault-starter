# Cost effective harnesses with Fable

**Source:** https://x.com/rlancemartin/status/2075641284635799865?s=46
**Fetch method:** Playwright MCP

*By Lance Martin (@RLanceMartin) — 6:00 PM · Jul 10, 2026*

![Image](https://pbs.twimg.com/media/HM4MapNbUAAJ6RK?format=jpg&name=small)

There is a lot of interest in [cost effective use](https://x.com/brian_armstrong/status/2070670644577280109?s=20) of Fable 5. Agent harnesses will get better at knowing when to use frontier intelligence. I wanted to share some tests I've run to better understand when and how to use Fable 5.

---

## The task shape

Many tasks have **asymmetry** in the intelligence needed across their tokens. Harnesses can recognize this and pick when to use Fable 5. A [few patterns](https://x.com/ClaudeDevs/status/2074606058128224365?s=20) have emerged, but we'll likely see more over time:

- Use Fable 5 as an **orchestrator** that delegates to lower cost workers.
- Use Fable 5 as an **advisor** that lower cost executors ask for advice.
- Use Fable 5 as a **verifier** to check work (e.g., in a [/goal](https://code.claude.com/docs/en/goal) or [Outcomes](https://platform.claude.com/docs/en/managed-agents/define-outcomes) loop).

![Image](https://pbs.twimg.com/media/HM4OJKca4AAf2WZ?format=jpg&name=small)

For example, [@mitchellh](https://x.com/mitchellh) called out an orchestrator-verifier approach:

> **Mitchell Hashimoto** (@mitchellh · Jul 2): I'm having a lot success using Fable xhigh as a planner/architect, using GPT 5.5 xhigh (subscription) as a coder, then Fable xhigh again as a judge. At API pricing, planning+judge costs are in the ~few dollar range compared to typical $50+ full round trips. I've seen some [...]

I explored this on [Parameter Golf](https://github.com/openai/parameter-golf), an ML engineering challenge similar to [@karpathy](https://x.com/@karpathy)'s [autoresearch](https://github.com/karpathy/autoresearch): let an agent edit training code, launch training, see results, and decide what experiment to run next.

The goal is to train the best model that fits in a 16MB artifact in < 10 minutes on 8xH100s. I [previously](https://x.com/RLanceMartin/status/2064397389189071163?s=20) showed that Fable 5 is strong at this task. So, I wanted to see if I could use Fable 5 only for experimental design and Sonnet 5 as a worker to absorb the implementation tokens.

I set this up with [Claude Managed Agents](https://platform.claude.com/docs/en/managed-agents/overview) with access to a [@modal](https://x.com/@modal) self-hosted 8xH100 sandbox and a Sonnet 5 executor that can call Fable 5. I instructed Sonnet 5 to consult Fable 5 as an advisor on the initial plan and later at 2 checkpoints during the 20 experiments.

The results below show validation loss (bits per byte) across 3 configurations (where lower is better): Fable 5 and Sonnet 5 together got ~90% of Fable-5-solo's improvement at ~34% of the token cost.

![Image](https://pbs.twimg.com/media/HM4UbBPbIAAGSIL?format=jpg&name=small)

The upfront advising step was **not** the primary benefit. Fable 5's initial ranking was anti-correlated with what worked. The value came from the advisory checkpoints. Sonnet 5 tends to get caught hill-climbing on marginal gains with no tendency to step back and re-rank. Fable's checkpoints provide steering and re-prioritization.

The **distribution** of judgment mattered in this case: upfront planning wasn't sufficient, but sprinkling Fable 5 as an advisor across the task at fixed points helped steer it in more promising directions. In hindsight this matches the task's shape: this type of experimentation is exploratory and each result reshapes what's worth trying next. Judgment needs to be scattered across it rather than front-loaded.

## The cost of delegation

Even if a task has intelligence asymmetry that the harness can exploit, it doesn't always pay to offload it. Sometimes **we just do things ourselves** because there's a coordination cost involved in delegation.

[@brada](https://x.com/@brada) and I saw this when testing Fable 5 with [BrowseComp](https://openai.com/index/browsecomp/), an eval for multi-constraint web search. It's a good task shape for Fable 5 to plan and delegate to Sonnet 5 workers that search, open pages, and cross-reference until the constraints pin a unique answer.

On BrowseComp200, an easy subset with ~0.37M tokens of reading per problem, Fable 5 alone was **cheaper** than mixing Fable 5 with Sonnet 5. Orchestration added a **60% markup** for no benefit in performance. But on the full BrowseComp eval set (~31M tokens of reading per problem), orchestration paid off. Fable 5 orchestrator with Sonnet 5 workers landed at 96% of the score at 46% of the cost.

![Image](https://pbs.twimg.com/media/HM4QnPyasAACCgS?format=jpg&name=small)

The token cost arbitrage gained by delegation to workers needs to offset the **coordination cost**. In this case, coordination cost has a few components:

- **Boundary duplication** - every token that crosses between models is billed at least twice: the lead *writes* a brief, the worker *reads* it; the worker *writes* a report, the lead *reads* it.
- **Fan-out overlap** – In many harnesses, workers don't communicate and many partially overlap in their research. [@walden_yan](https://x.com/@walden_yan) wrote a [nice article](https://cognition.com/blog/dont-build-multi-agents) on this problem last year.

This means the cost benefit of cheap workers has to offset a coordination cost that is roughly fixed per handoff. In this case, the worker benefit scales with the tokens each worker absorbs.

## Cost effective harnesses

Here are the types of guidance that I've been giving Fable 5 when writing cost effective harnesses for various tasks; Fable is effective at understanding how and when to utilize its own intelligence with some of the this guidance:

**1. Examine the task shape.** Assess the intelligence needed across the task. Judgement scattered across the task, as we saw in Parameter Golf, can benefit from a cheap executor and a Fable 5 advisor. Judgement upfront or to review work can benefit from a Fable 5 orchestrator or verifier.

**2. Use delegation heuristics.** Sometimes we can provide Claude with priors for worker delegation. [@theo](https://x.com/theo) has an example [here](https://x.com/theo/status/2072482460122964067/photo/1) where various models are ranked according to "taste" and "intelligence"; these can help the harness decide when to incorporate each one.

**3. Assess the cost of coordination.** Delegation comes with a cost. As I saw with BrowseComp, make sure that you are delegating a large enough volume of tokens to offset the coordination cost. Because Fable 5 can be more **token efficient** than a model with a lower $ / token, the benefit of delegation should be carefully considered.

**4. Ensure prompt caching.** Models maintain their own prompt caches, and getting this wrong is an easy way for delegation costs to blow up. As [@cognition](https://x.com/@cognition) calls out [here](https://cognition.com/blog/devin-fusion), sub-agents should maintain a prompt cache across calls. Route calls to the **same** worker so its cache accumulates, rather than spawning a fresh worker per request and re-paying the context write every time. In my experiments, [Claude Managed Agents](https://platform.claude.com/docs/en/managed-agents/overview) has [sub-agents](https://platform.claude.com/docs/en/managed-agents/multi-agent) that supported this natively, but I've seen cases where a low prompt cache hit rate offsets the cost benefit of using a lower $ / token worker.

---

As [@trq212](https://x.com/trq212) shared [here](https://x.com/trq212/status/2061907337154367865?s=20), Claude can write its own [harness](https://code.claude.com/docs/en/glossary#agentic-harness) on the fly based upon the task. Some of the considerations in this article can help Claude write cost effective harnesses that selectively apply frontier intelligence.
