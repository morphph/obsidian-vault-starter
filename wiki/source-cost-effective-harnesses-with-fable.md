---
type: source-summary
created: 2026-07-13
last-updated: 2026-07-13
sources:
  - raw/2026-07-13-cost-effective-harnesses-with-fable.md
tags: []
---

# 精读：Cost effective harnesses with Fable

## 精读

**作者**：Lance Martin (@RLanceMartin) — 研究者，做 agent harness 与 evals 实验，本文分享他跑过的一批测试
**来源**：X (Twitter) · 2026-07-10 · [原文](https://x.com/rlancemartin/status/2075641284635799865?s=46)
**原文字数**：约 900 words · **精读预读时长**：约 6 分钟
**一句话主旨**：任务在不同 token 上所需的智能是**不对称**的，harness 应识别这种不对称、只在该用前沿智能的地方调用 Fable 5——但委派本身有固定的协调成本，只有当被委派的 token 量足够大、能抵消协调成本时，混合便宜 worker 才真正省钱。

---

### 开篇（原文无小标题，此为段落主题）

大家对如何**低成本使用 (cost effective use)** Fable 5 很感兴趣。作者的判断是：agent harness 会越来越懂得**什么时候该动用前沿智能 (frontier intelligence)**。他想分享一批自己跑过的测试，帮助理解 Fable 5 该在何时、以何种方式使用。

### The task shape（任务的形状）

很多任务在其 token 上所需的智能存在**不对称 (asymmetry)**——不是每个 token 都需要顶配智能。harness 可以识别这种不对称，挑准时机才上 Fable 5。目前已经浮现出几种模式（未来还会更多）：

- 把 Fable 5 当**编排者 (orchestrator)**，把活委派给更低成本的 worker。
- 把 Fable 5 当**顾问 (advisor)**，让低成本的执行者在需要时向它请教。
- 把 Fable 5 当**校验者 (verifier)**，用来检查工作成果（例如放在 `/goal` 或 Outcomes 循环里）。

作者举 [@mitchellh](https://x.com/mitchellh)（Mitchell Hashimoto）为例，他用的是编排者-校验者组合：

> **Mitchell Hashimoto**（@mitchellh · Jul 2）："I'm having a lot success using Fable xhigh as a planner/architect, using GPT 5.5 xhigh (subscription) as a coder, then Fable xhigh again as a judge. At API pricing, planning+judge costs are in the ~few dollar range compared to typical $50+ full round trips."
> （用 Fable xhigh 当规划者/架构师，用 GPT 5.5 xhigh 当写代码的，再用 Fable xhigh 当裁判。按 API 定价，规划+裁判的成本在**几美元**这个量级，而典型的整轮跑一趟要 **$50 以上**。）

作者在 [Parameter Golf](https://github.com/openai/parameter-golf) 上做了验证——这是一个 ML 工程挑战，类似 Karpathy 的 autoresearch：让 agent 改训练代码、启动训练、看结果、再决定下一个实验跑什么。**目标是在 8xH100 上、10 分钟以内、训练出一个塞得进 16MB 制品的最佳模型。** 作者之前展示过 Fable 5 单干这个任务就很强；这次他想看能不能只让 Fable 5 负责**实验设计**，而用 Sonnet 5 当 worker 去吸收实现的 token。

他用 [Claude Managed Agents](https://platform.claude.com/docs/en/managed-agents/overview) 搭了这套：接入一个 [@modal](https://x.com/@modal) 自托管的 8xH100 sandbox，配一个能调用 Fable 5 的 Sonnet 5 执行者。他让 Sonnet 5 在**初始计划**阶段、以及后续 20 个实验中的 **2 个 checkpoint** 上，向 Fable 5 作为顾问请教。

结果按 validation loss（bits per byte，越低越好）在 3 种配置上对比：**Fable 5 与 Sonnet 5 合作拿到了 Fable-5-单干约 90% 的改进，成本却只有约 34% 的 token 成本。**

关键洞察在于：**前期那次咨询并不是主要收益来源**。Fable 5 一开始给的排名其实和真正管用的东西是**反相关**的。真正的价值来自**中途那几个咨询 checkpoint**。Sonnet 5 容易陷进去在边际收益上爬坡 (hill-climbing)，没有退一步重新排序的倾向；Fable 的 checkpoint 提供了转向和重新排优先级的能力。

> "The **distribution** of judgment mattered in this case: upfront planning wasn't sufficient, but sprinkling Fable 5 as an advisor across the task at fixed points helped steer it in more promising directions."
> （这个案例里，判断力的**分布**才是关键：前期规划不够用，而把 Fable 5 作为顾问在固定点上**撒 (sprinkle)** 到任务全程，能把它导向更有希望的方向。）

这和任务形状是吻合的：这类实验是探索性的，每个结果都会重塑"接下来值得试什么"。所以判断力需要**散布在任务全程**，而不是前置堆在开头。

> [!note] 白板图示：一张图讲清"任务形状不对称 → 三种放置 Fable 5 的模式 → 两个案例证明委派何时省钱/何时白费 → 四条 harness 指南"的完整论证链

![[cost-effective-harnesses-with-fable-diagram.png]]

### The cost of delegation（委派的成本）

即便任务有 harness 能利用的智能不对称，**委派也不总是划算**。有时候我们**干脆自己做 (we just do things ourselves)**，因为委派本身牵扯**协调成本 (coordination cost)**。

作者和 [@brada](https://x.com/@brada) 用 [BrowseComp](https://openai.com/index/browsecomp/)（一个多约束网页搜索的 eval）测 Fable 5 时看到了这点。这个任务形状本来很适合 Fable 5 去规划、把活委派给搜索/开页面/交叉比对的 Sonnet 5 worker，直到约束条件把答案唯一锁定。

- 在 **BrowseComp200**（一个较简单的子集，每题约 **0.37M tokens** 的阅读量）上，**Fable 5 单干反而更便宜**。编排反倒加了 **60% 的溢价 (markup)**，性能上却毫无收益。
- 但在**完整 BrowseComp** eval 集（每题约 **31M tokens** 的阅读量）上，编排就划算了：Fable 5 编排者配 Sonnet 5 worker，拿到了 **96% 的分数、只花 46% 的成本**。

结论：委派给 worker 换来的 **token 成本套利**，必须能抵消**协调成本**。这里协调成本有几个组成部分：

- **边界重复 (Boundary duplication)**——每个在模型之间穿越的 token 至少被计费两次：lead *写* 一份简报，worker *读* 它;worker *写* 一份报告,lead 再 *读* 它。
- **扇出重叠 (Fan-out overlap)**——很多 harness 里 worker 之间不通信,很多人的研究会部分重叠。[@walden_yan](https://x.com/@walden_yan) 去年写过一篇[好文](https://cognition.com/blog/dont-build-multi-agents)专门讲这个问题。

也就是说,便宜 worker 带来的成本收益,必须抵消一份**大致按每次 handoff 固定**的协调成本。而 worker 的收益是随**每个 worker 吸收的 token 量**扩展的——吸得越多越划算。

### Cost effective harnesses（低成本 harness 的写法）

作者总结了他在给各类任务写低成本 harness 时,喂给 Fable 5 的几类指导(有了这些指导,Fable 本身就很擅长判断该如何、何时动用自己的智能):

**1. 审视任务形状 (Examine the task shape)。** 评估任务全程所需的智能。像 Parameter Golf 那样**判断力散布在任务中**的,适合用便宜执行者 + Fable 5 顾问。判断力集中在**前期**或用于**复核成果**的,适合用 Fable 5 编排者或校验者。

**2. 用委派启发式 (Use delegation heuristics)。** 有时可以给 Claude 一些委派 worker 的先验。[@theo](https://x.com/theo) 有个[例子](https://x.com/theo/status/2072482460122964067/photo/1),把各种模型按"品味 (taste)"和"智能 (intelligence)"排名;这类排名能帮 harness 决定何时纳入哪个模型。

**3. 评估协调成本 (Assess the cost of coordination)。** 委派有代价。就像 BrowseComp 那样,要确保你委派的 token 量**足够大**,能抵消协调成本。因为 Fable 5 可能比一个 $/token 更低的模型还要更 **token 高效 (token efficient)**,所以委派的收益需要仔细权衡。

**4. 保证 prompt caching (Ensure prompt caching)。** 各模型维护自己的 prompt cache,搞错这一点是让委派成本爆炸的一条捷径。正如 [@cognition](https://x.com/@cognition) [指出](https://cognition.com/blog/devin-fusion)的,子 agent 应该**跨调用维持 prompt cache**。要把调用路由到**同一个** worker,让它的 cache 累积起来,而不是每次请求都开一个全新 worker、每次都重付一遍 context 的写入。作者的实验里,Claude Managed Agents 的 [sub-agents](https://platform.claude.com/docs/en/managed-agents/multi-agent) 原生支持这点;但他也见过**低 prompt cache 命中率把低 $/token worker 的成本优势抵消掉**的情况。

### 结尾（原文无小标题，此为段落主题）

正如 [@trq212](https://x.com/trq212) [分享](https://x.com/trq212/status/2061907337154367865?s=20)的,Claude 能根据任务**当场自己写 harness (write its own harness on the fly)**。本文的这些考量,能帮 Claude 写出**有选择地施加前沿智能**的低成本 harness。

---

## 精读收尾

- **一句话总结**：任务的智能是不对称的——把 Fable 5 当编排者/顾问/校验者按需撒进去,但委派有固定协调成本,只有被委派的 token 量大到能抵消它时才省钱(BrowseComp:0.37M token 反亏 60%,31M token 省到 46% 成本)。
- **关键引语**：
  - "Many tasks have **asymmetry** in the intelligence needed across their tokens."（很多任务在其 token 上所需的智能是不对称的。)
  - "The **distribution** of judgment mattered... sprinkling Fable 5 as an advisor across the task at fixed points helped steer it."（判断力的分布才是关键——把 Fable 5 作为顾问撒到任务全程能起到导向作用。)
  - "Sometimes **we just do things ourselves** because there's a coordination cost involved in delegation."（有时我们干脆自己做,因为委派牵扯协调成本。)
  - "Every token that crosses between models is billed at least twice."（每个在模型间穿越的 token 至少被计费两次。)
  - "Fable 5 can be more **token efficient** than a model with a lower $ / token."（Fable 5 可能比一个 $/token 更低的模型更 token 高效。)
- **与 vault 的连接**：
  - [[prompt-cache-optimization]] — 指南 #4 是同一条铁律的实操版:子 agent 跨调用维持 cache、路由到同一 worker,否则低 $/token 的成本优势被 cache miss 抵消。
  - [[agent-vs-workflow]] — 三种模式(orchestrator/advisor/verifier)是 orchestrator-workers 与 evaluator-optimizer 两种 canonical pattern 的成本视角续写。
  - [[claude-managed-agents]] / [[managed-agents-multiagent]] — 作者两个实验都跑在 Managed Agents 上,其 sub-agents 原生支持跨调用 prompt cache 正是本文成本论证的基础设施。
  - [[verification-loops]] / [[claude-code-goal]] — verifier 模式对应 `/goal`/Outcomes 循环里的 LLM-as-judge。
- **视频适配自评**：**非常适合**做白板讲解视频。论证结构高度可图示——"不对称"是一个可空间化的核心隐喻,三种放置模式 + 一条"套利 vs 协调成本"的天平公式 + 两个走向相反的案例(60% 亏 vs 46% 省),讲解张力足;数字对比(90%/34%、96%/46%、60% markup)天然是画面锚点。

### 文末注记（headless 消歧自决）

- **作者身份/stake**：原文未给正式 bio,依据推文内容(自述跑 harness/eval 实验、引用自己此前 Parameter Golf 与 BrowseComp 测试)将其概括为"做 agent harness 与 evals 实验的研究者"。
- **原文字数**:原文为长推文/文章体,无官方字数;约 900 words 为目测估算。
- **"品味/智能排名"**:@theo 的模型排名图原文只给了链接未展开内容,精读按原文措辞保留"taste/intelligence 两轴排名",未擅自补充具体模型。
- **图示嵌入位置**:该图是全文论证的空间化(不对称→模式→案例→指南),按精读约定嵌在信息最完整的 The task shape 章节末(该章已建立不对称与三模式,是图的语义重心),而非分散到各章。
