---
type: source-summary
created: 2026-07-13
last-updated: 2026-07-15
sources:
  - raw/2026-07-13-cost-effective-harnesses-with-fable.md
tags: []
---

# 精读：Cost effective harnesses with Fable

## 精读

**作者**：Lance Martin (@RLanceMartin) — 做 agent harness 与 evals 实验的研究者，本文分享他为「低成本用 Fable 5」跑过的一批测试
**来源**：X · 2026-07-10 · [原文](https://x.com/rlancemartin/status/2075641284635799865?s=46)
**原文字数**：约 900 words · **译读预读时长**：约 6 分钟
**一句话主旨**：任务在不同 token 上所需的智能是**不对称**的，harness 应识别这种不对称、只在该用前沿智能的地方调用 Fable 5——但委派本身有一份大致固定的协调成本，只有当被委派的 token 量大到足以抵消它时，混合便宜 worker 才真正省钱。

---

### 开篇（原文无小标题，此为段落主题）

关于如何**低成本地使用 (cost effective use)** Fable 5，大家的兴趣很浓。Agent harness 会越来越懂得什么时候该动用前沿智能 (frontier intelligence)。我想分享一批我自己跑过的测试，好更清楚地理解 Fable 5 该在何时、以何种方式使用。

### The task shape（任务的形状）

很多任务在它们的 token 上，所需的智能是**不对称的 (asymmetry)**——并不是每个 token 都需要同等的智能。harness 可以识别出这种不对称，挑准时机才上 Fable 5。目前已经浮现出**几种模式**，随着时间推移我们大概还会看到更多：

- 把 Fable 5 当**编排者 (orchestrator)**，把活委派给成本更低的 worker。
- 把 Fable 5 当**顾问 (advisor)**，让成本更低的执行者在需要时向它请教。
- 把 Fable 5 当**校验者 (verifier)** 来检查工作成果（例如放在 `/goal` 或 Outcomes 循环里）。

举个例子，[@mitchellh](https://x.com/mitchellh)（Mitchell Hashimoto）就提到过一种编排者-校验者的组合：

> **Mitchell Hashimoto**（@mitchellh · Jul 2）："I'm having a lot success using Fable xhigh as a planner/architect, using GPT 5.5 xhigh (subscription) as a coder, then Fable xhigh again as a judge. At API pricing, planning+judge costs are in the ~few dollar range compared to typical $50+ full round trips."
> （我用 Fable xhigh 当规划者/架构师、用 GPT 5.5 xhigh（订阅）当写代码的、再用 Fable xhigh 当裁判，效果很好。按 API 定价，规划+裁判的成本就在**几美元**这个量级，而典型的整轮跑一趟要 **$50 以上**。）

我在 [Parameter Golf](https://github.com/openai/parameter-golf) 上探索了这个思路——这是一个 ML 工程挑战，和 [@karpathy](https://x.com/@karpathy) 的 [autoresearch](https://github.com/karpathy/autoresearch) 类似：让一个 agent 改训练代码、启动训练、看结果，再决定下一个实验该跑什么。目标是在 8xH100 上、10 分钟以内，训练出一个能塞进 16MB 制品的最佳模型。我[之前](https://x.com/RLanceMartin/status/2064397389189071163?s=20)展示过 Fable 5 单干这个任务就很强，所以这次我想看看，能不能**只用 Fable 5 来做实验设计**，而让 Sonnet 5 当 worker 去吸收实现环节的 token。

我用 [Claude Managed Agents](https://platform.claude.com/docs/en/managed-agents/overview) 把这套搭了起来：接一个 [@modal](https://x.com/@modal) 自托管的 8xH100 sandbox，再配一个能调用 Fable 5 的 Sonnet 5 执行者。我让 Sonnet 5 在**初始计划**上、以及之后 20 个实验中的 **2 个 checkpoint** 上，把 Fable 5 当顾问来请教。

下面的结果给出了 3 种配置下的 validation loss（bits per byte，越低越好）：**Fable 5 和 Sonnet 5 一起，拿到了 Fable-5-单干约 90% 的改进，而 token 成本只有约 34%。**（原文配图：三种配置 validation loss 的对比图。）

前期那一步「事先咨询」**并不是**主要收益来源。Fable 5 一开始给出的排名，其实和真正管用的东西是**反相关**的。价值来自那几个**顾问 checkpoint**。Sonnet 5 容易卡在对边际收益的爬坡 (hill-climbing) 上，没有退一步、重新排序的倾向；而 Fable 的 checkpoint 提供了转向和重新排优先级的能力。

> "The **distribution** of judgment mattered in this case: upfront planning wasn't sufficient, but sprinkling Fable 5 as an advisor across the task at fixed points helped steer it in more promising directions."
> （这个案例里，判断力的**分布**才是关键：前期规划并不够用，而把 Fable 5 当顾问、在固定的点上**撒 (sprinkle)** 进任务全程，能把它导向更有希望的方向。）

事后回看，这和任务的形状是吻合的：这类实验本身是探索性的，每一个结果都会重塑「接下来什么值得试」。所以判断力需要**散布在任务全程**，而不是前置堆在开头。

> [!note] 白板图示：一张图讲清「任务形状不对称 → 三种放置 Fable 5 的模式 → 两个案例证明委派何时省钱/何时白费 → 四条 harness 指南」的完整论证链

![[cost-effective-harnesses-with-fable-diagram.png]]

### The cost of delegation（委派的成本）

即便一个任务存在 harness 能利用的智能不对称，把它卸载出去也**不总是划算**。有时候我们**干脆自己做 (we just do things ourselves)**，因为委派本身牵扯一份**协调成本 (coordination cost)**。

我和 [@brada](https://x.com/@brada) 在用 [BrowseComp](https://openai.com/index/browsecomp/)（一个多约束网页搜索的 eval）测 Fable 5 时，就看到了这一点。这个任务形状本来很适合让 Fable 5 去规划、再委派给 Sonnet 5 worker——它们负责搜索、打开页面、交叉比对，直到约束条件把答案唯一地锁定下来。

在 **BrowseComp200**（一个较简单的子集，每题约 **0.37M tokens** 的阅读量）上，**Fable 5 单干反而更便宜**。编排在这里加了 **60% 的溢价 (markup)**，性能上却没换来任何好处。但在**完整的 BrowseComp** eval 集（每题约 **31M tokens** 的阅读量）上，编排就划算了：Fable 5 编排者配 Sonnet 5 worker，落在了 **96% 的分数、46% 的成本**。（原文配图：两种规模下成本/性能的对比图。）

委派给 worker 换来的 **token 成本套利**，必须能抵消这份**协调成本**。在这个案例里，协调成本有几个组成部分：

- **边界重复 (Boundary duplication)**——每个在模型之间穿越的 token 至少被计费两次：lead *写*一份简报，worker *读*它；worker *写*一份报告，lead 再*读*它。
- **扇出重叠 (Fan-out overlap)**——在很多 harness 里，worker 之间并不通信，很多人的研究会部分重叠。[@walden_yan](https://x.com/@walden_yan) 去年写过一篇[很好的文章](https://cognition.com/blog/dont-build-multi-agents)专讲这个问题。

这意味着，便宜 worker 带来的成本收益，必须抵消一份**大致按每次 handoff 固定**的协调成本。而在这个案例里，worker 的收益是随**每个 worker 吸收的 token 量**而扩展的。

### Cost effective harnesses（低成本 harness 的写法）

下面是我在给各类任务写低成本 harness 时，一直喂给 Fable 5 的几类指导；有了其中一些指导，Fable 本身就很擅长理解该如何、何时动用它自己的智能：

**1. 审视任务形状 (Examine the task shape)。** 评估任务全程各处所需的智能。像我们在 Parameter Golf 里看到的那样，**判断力散布在任务中**的，能受益于「便宜执行者 + Fable 5 顾问」。而判断力集中在**前期**、或用于**复核成果**的，则能受益于 Fable 5 编排者或校验者。

**2. 用委派启发式 (Use delegation heuristics)。** 有时我们可以给 Claude 一些委派 worker 的先验。[@theo](https://x.com/theo) 有个[例子](https://x.com/theo/status/2072482460122964067/photo/1)，把各种模型按「品味 (taste)」和「智能 (intelligence)」排名；这类排名能帮 harness 决定何时纳入哪一个。

**3. 评估协调成本 (Assess the cost of coordination)。** 委派是有代价的。就像我在 BrowseComp 上看到的，要确保你委派出去的 token 量**足够大**，能抵消协调成本。因为 Fable 5 可能比一个 $/token 更低的模型还要更 **token 高效 (token efficient)**，所以委派的收益需要仔细掂量。

**4. 保证 prompt caching (Ensure prompt caching)。** 各个模型维护自己的 prompt cache，而搞错这一点，是让委派成本爆炸的一条捷径。正如 [@cognition](https://x.com/@cognition) [指出](https://cognition.com/blog/devin-fusion)的，子 agent 应当**跨调用维持 prompt cache**。要把调用路由到**同一个** worker，让它的 cache 累积起来，而不是每次请求都开一个全新的 worker、每次都重付一遍 context 的写入。在我的实验里，[Claude Managed Agents](https://platform.claude.com/docs/en/managed-agents/overview) 的 [sub-agents](https://platform.claude.com/docs/en/managed-agents/multi-agent) 原生就支持这点；但我也见过**低 prompt cache 命中率把低 $/token worker 的成本优势抵消掉**的情况。

### 结尾（原文无小标题，此为段落主题）

正如 [@trq212](https://x.com/trq212) [分享](https://x.com/trq212/status/2061907337154367865?s=20)过的，Claude 能根据任务**当场自己写出 harness (write its own harness on the fly)**。本文里的这些考量，能帮 Claude 写出那种**有选择地施加前沿智能**的低成本 harness。

---

## 精读收尾

- **一句话总结**：任务的智能是不对称的——把 Fable 5 当编排者/顾问/校验者按需撒进去，但委派有一份固定协调成本，只有被委派的 token 量大到能抵消它时才省钱（BrowseComp：0.37M token 反亏 60%，31M token 省到 46% 成本）。
- **关键引语**：
  - "Many tasks have **asymmetry** in the intelligence needed across their tokens."（很多任务在其 token 上所需的智能是不对称的。）
  - "The **distribution** of judgment mattered... sprinkling Fable 5 as an advisor across the task at fixed points helped steer it."（判断力的分布才是关键——把 Fable 5 当顾问撒到任务全程能起到导向作用。）
  - "Sometimes **we just do things ourselves** because there's a coordination cost involved in delegation."（有时我们干脆自己做，因为委派牵扯协调成本。）
  - "Every token that crosses between models is billed at least twice."（每个在模型间穿越的 token 至少被计费两次。）
  - "Fable 5 can be more **token efficient** than a model with a lower $ / token."（Fable 5 可能比一个 $/token 更低的模型更 token 高效。）
- **与 vault 的连接**：
  - [[prompt-cache-optimization]] — 指南 #4 是同一条铁律的实操版：子 agent 跨调用维持 cache、路由到同一 worker，否则低 $/token 的成本优势被 cache miss 抵消。
  - [[agent-vs-workflow]] — 三种模式（orchestrator/advisor/verifier）是 orchestrator-workers 与 evaluator-optimizer 两种 canonical pattern 的成本视角续写。
  - [[claude-managed-agents]] / [[managed-agents-multiagent]] — 两个实验都跑在 Managed Agents 上，其 sub-agents 原生支持跨调用 prompt cache，正是本文成本论证的基础设施。
  - [[verification-loops]] / [[claude-code-goal]] — verifier 模式对应 `/goal`/Outcomes 循环里的 LLM-as-judge。
- **视频适配自评**：**非常适合**做白板讲解视频。论证结构高度可图示——「不对称」是一个可空间化的核心隐喻，三种放置模式 + 一条「套利 vs 协调成本」的天平公式 + 两个走向相反的案例（60% 亏 vs 46% 省），讲解张力足；数字对比（90%/34%、96%/46%、60% markup）天然是画面锚点。
