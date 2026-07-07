---
type: source-summary
created: 2026-07-07
last-updated: 2026-07-07
sources:
  - raw/2026-07-05-building-effective-agents.md
tags: []
---

# 精读：Building Effective AI Agents

## 精读

**作者**：Erik S. 与 Barry Zhang（Anthropic 工程师；文中主张全部来自「与数十个客户团队一起构建 LLM agent」+「Anthropic 自己构建 agent」的一手经验，stake 是让开发者少走弯路）
**来源**：Anthropic Engineering Blog · 2026-07-05（vault raw 抓取日）· [原文](https://www.anthropic.com/engineering/building-effective-agents)
**原文字数**：约 2,400 words · **精读预读时长**：约 12 分钟
**一句话主旨**：最成功的 agent 实现不靠复杂框架，而靠简单、可组合的模式——从「增强型 LLM」这一基础构件出发，按需逐级加复杂度（五种 workflow 模式 → 自主 agent），且只在复杂度能被证明改善结果时才引入。

---

### 1. 开篇（原文无小标题，此为段落主题）

过去一年里，Anthropic 与跨行业的数十个团队一起构建 LLM agent。一个一致的观察：**最成功的实现，用的都不是复杂框架或专门的库，而是简单、可组合的模式（simple, composable patterns）**。这篇文章把他们从客户身上、以及自己构建 agent 中学到的东西分享出来，给开发者一些实操建议。

### 2. What are agents?（什么是 agent？）

"Agent" 这个词有多种定义。有的客户把 agent 理解为「长时间独立运行、用各种工具完成复杂任务的**完全自主系统**」；也有人用它指代那种「遵循预定义流程的、更具规定性（prescriptive）的实现」。Anthropic 把所有这些变体统称为 **agentic systems（智能体系统）**，但在架构上划出一条重要的区分线——workflow 与 agent：

- **Workflow（工作流）**：LLM 和工具通过**预先写好的代码路径（predefined code paths）**被编排的系统。
- **Agent（智能体）**：LLM **动态地自主指挥自己的流程和工具使用（dynamically direct their own processes and tool usage）**、始终掌控如何完成任务的系统。

> **"Workflows are systems where LLMs and tools are orchestrated through predefined code paths. Agents … are systems where LLMs dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks."**
> —— 路径是代码定的，就是 workflow；路径是模型自己定的，就是 agent。这是全文的地基。

文中还预告：附录 1（"Agents in Practice"）会讲两个客户特别受益的领域。

### 3. When (and when not) to use agents（什么时候该用、什么时候不该用 agent）

核心建议：**用 LLM 构建应用时，先找最简单可行的方案，只在需要时才增加复杂度**——这甚至可能意味着「根本不构建 agentic system」。理由是 agentic system 通常拿延迟和成本去换更好的任务表现（trade latency and cost for better task performance），你得判断这笔交易是否划算。

当确实需要更高复杂度时怎么选：

- **Workflow**：为定义清晰的任务提供**可预测性和一致性（predictability and consistency）**。
- **Agent**：当需要**大规模的灵活性与模型驱动的决策（flexibility and model-driven decision-making at scale）**时更优。
- 但对很多应用来说，「用检索 + 上下文示例（in-context examples）去优化单次 LLM 调用」通常就够了。

### 4. When and how to use frameworks（何时、如何使用框架）

有不少框架能让 agentic system 更好实现，文中点名：

- **Claude Agent SDK**；
- **Strands Agents SDK**（AWS 出品）；
- **Rivet**——拖拽式 GUI 的 LLM workflow 构建器；
- **Vellum**——另一个用来构建和测试复杂 workflow 的 GUI 工具。

这些框架的好处是把「调用 LLM、定义与解析工具、串联调用」这些标准的底层活儿简化了，容易上手。但代价是：它们常常**多加一层抽象，遮蔽底层的 prompt 和 response，使调试更难**；还会诱使你在本可更简单时去加复杂度。

> **"Incorrect assumptions about what's under the hood are a common source of customer error."**
> —— 对「引擎盖下发生了什么」的错误假设，是客户出错的常见来源。

建议：**开发者从直接调用 LLM API 开始**（很多模式几行代码就能实现）；若确实要用框架，务必理解其底层代码。最后指向他们的 cookbook 里有示例实现。

### 5. Building blocks, workflows, and agents（构件、工作流与 agent）

本节梳理生产环境中见到的常见模式，方法是**从基础构件「增强型 LLM」出发，复杂度逐级递增**——从简单的组合式 workflow，一路到自主 agent。

#### 5.1 Building block: The augmented LLM（构件：增强型 LLM）

agentic system 的基本构件，是一个被增强（augmented）过的 LLM——增强项包括**检索（retrieval）、工具（tools）、记忆（memory）**。当前的模型能主动使用这些能力：自己生成搜索查询、自己选合适的工具、自己判断该保留哪些信息。

> 图：一个 LLM 连接着 retrieval / tools / memory 三类增强能力（"The augmented LLM"）。

实现上建议聚焦两点：（1）把这些能力**贴合你的具体用例**来裁剪；（2）为 LLM 提供**简单、文档完善的接口**。实现增强的方式很多，其中一条路是他们「近期发布的 **Model Context Protocol（MCP，模型上下文协议）**」——用一个简单的客户端实现，就能接入不断增长的第三方工具生态。全文后续都假设每次 LLM 调用都已具备这些增强能力。

#### 5.2 Workflow: Prompt chaining（工作流：提示词链）

**Prompt chaining（提示词链）**把一个任务拆成一串步骤，每次 LLM 调用处理上一次的输出。可以在中间步骤上加**程序化检查（即图中的 "gate"）**，确保流程没跑偏。

> 图：任务 → LLM 调用①→（gate 检查）→ LLM 调用② → … 的线性链（"The prompt chaining workflow"）。

**何时用**：任务能被干净、清楚地拆成固定子任务时最理想。主目标是**用延迟换更高准确率**——把每次 LLM 调用变成更简单的任务。

有用的例子：
- 先生成营销文案，再翻译成另一种语言。
- 先写文档大纲 → 检查大纲是否满足某些标准 → 再基于大纲写文档。

#### 5.3 Workflow: Routing（工作流：路由）

**Routing（路由）**对输入做分类，然后导向一个专门的后续任务。好处是**关注点分离（separation of concerns）**、能针对性地写更专门的 prompt。没有它的话，为一类输入做优化会伤害另一类输入的表现。

> 图：输入 → 路由/分类 → 分流到多条专门下游路径（"The routing workflow"）。

**何时用**：复杂任务里存在「更适合分开处理的清晰类别」，且分类本身能被准确完成时（由 LLM 或传统分类模型/算法都行）。

有用的例子：
- 把不同类型的客服问题（一般咨询、退款请求、技术支持）导入不同的下游流程、prompt 和工具。
- 把简单/常见问题路由给更小、更省成本的模型（如 **Claude Haiku 4.5**），把困难/罕见问题路由给更强的模型（如 **Claude Sonnet 4.5**），以优化整体表现。

#### 5.4 Workflow: Parallelization（工作流：并行化）

LLM 有时能同时处理一个任务，再用程序把多路输出聚合起来。**Parallelization（并行化）**有两种关键变体：

- **Sectioning（分段）**：把任务拆成互相独立的子任务，并行跑。
- **Voting（投票）**：把同一个任务跑多次，得到多样化的输出。

> 图：一个输入扇出成多个并行 LLM 调用，结果再被聚合（"The parallelization workflow"）。

**何时用**：当拆出的子任务可并行以提速，或需要多个视角/多次尝试来提高结果置信度时有效。对于有多重考量的复杂任务，**让每个考量由单独一次 LLM 调用来处理**，通常表现更好——每个方面都能获得聚焦的注意力。

有用的例子：
- **Sectioning**：
  - 做护栏（guardrails）：一个模型实例处理用户查询，另一个实例专门筛查其中不当内容/请求——这比让同一次 LLM 调用同时兼顾护栏和核心响应，效果更好。
  - 自动化评测（evals）：每次 LLM 调用评估模型在某个 prompt 上表现的一个不同侧面。
- **Voting**：
  - 审代码漏洞：用几个不同的 prompt 分别审查、发现问题就标记。
  - 判断某内容是否不当：多个 prompt 评估不同侧面，或用不同的投票阈值来平衡误报与漏报。

#### 5.5 Workflow: Orchestrator-workers（工作流：编排者—工作者）

在 **orchestrator-workers（编排者—工作者）**里，一个中心 LLM **动态地**拆解任务、把子任务委派给 worker LLM，再综合它们的结果。

> 图：中心 orchestrator 向多个 worker 分派、并汇总结果（"The orchestrator-workers workflow"）。

**何时用**：适合「无法预先预测需要哪些子任务」的复杂任务（比如写代码时，需要改几个文件、每个文件怎么改，往往取决于任务本身）。它与并行化**拓扑相似，但关键区别在灵活性**——子任务不是预先定义好的，而是由 orchestrator 根据具体输入现场决定。

有用的例子：
- 每次都要对多个文件做复杂改动的编码类产品。
- 需要从多个来源收集并分析信息、找可能相关内容的搜索任务。

#### 5.6 Workflow: Evaluator-optimizer（工作流：评估者—优化者）

在 **evaluator-optimizer（评估者—优化者）**里，一次 LLM 调用生成响应，另一次 LLM 调用在**循环中**提供评估与反馈。

> 图：生成器与评估器在反馈环里往返迭代（"The evaluator-optimizer workflow"）。

**何时用**：当我们有**清晰的评估标准**、且**迭代式精修能带来可衡量的价值**时特别有效。两个「适配良好」的信号：其一，当人类清楚表达反馈时，LLM 的响应能被明显改善；其二，LLM 自己也能提供这样的反馈。这类比人类写作者打磨稿子的迭代过程。

有用的例子：
- 文学翻译：译者 LLM 一开始可能抓不住某些微妙之处，而评估者 LLM 能给出有用的批评。
- 复杂搜索任务：需要多轮搜索与分析才能收集全面信息，由评估者决定是否值得继续搜。

#### 5.7 Agents（智能体）

随着 LLM 在几项关键能力上成熟——**理解复杂输入、推理与规划、可靠地用工具、从错误中恢复**——agent 正在生产环境中涌现。agent 的工作起点，是来自人类用户的一条命令、或一次互动式讨论；任务一旦明确，agent 就**独立地规划与运行**，必要时回到人类那里索取更多信息或判断。执行过程中，**关键是让 agent 在每一步都从环境中获得「ground truth（真实反馈）」**（如工具调用结果、代码执行结果）来评估自己的进展；agent 可以在检查点、或遇到阻塞时暂停等人类反馈。任务通常在完成时终止，但常见做法是加**停止条件（如最大迭代次数）**以保持可控。

> **"They are typically just LLMs using tools based on environmental feedback in a loop."**
> —— agent 本质上通常就是「LLM 在一个循环里，基于环境反馈使用工具」。实现往往很直接，所以**清晰、用心地设计工具集及其文档就至关重要**——最佳实践见附录 2。

> 图：agent 在「行动→观察环境反馈→再行动」的循环中自主运转（"Autonomous agent"）。

**何时用 agent**：用于**开放式问题**——难以或无法预测所需步骤数、也无法硬编码固定路径。LLM 可能要运行很多轮，你必须对它的决策有一定程度的信任。agent 的自主性使它非常适合**在可信环境（trusted environments）中扩展任务**。

代价与防护：自主性意味着更高成本、以及**误差累积（compounding errors）**的风险。建议在**沙盒环境中做大量测试**，并配以恰当的护栏。

有用的例子（来自 Anthropic 自己的实现）：
- 一个解决 **SWE-bench** 任务的编码 agent（涉及按任务描述对许多文件做修改）；
- 他们的 **"computer use"** 参考实现——Claude 用一台电脑来完成任务。

> 图：一个编码 agent 的高层流程（"High-level flow of a coding agent"）。

> [!note] 白板图示（S3 预演）：复杂度阶梯
> 一张论证型白板图，把本节的核心论证空间化——**① 增强型 LLM 基础构件 → ② 五种 workflow 模式（prompt chaining / routing / parallelization / orchestrator-workers / evaluator-optimizer）→ ③ 自主 agent 循环**，沿底部「复杂度递增」轴线逐级展开，落点是「只在复杂度能被证明改善结果时才加」。按论证顺序标了 7 个 `customData.step`，可分层动画导出。

![[building-effective-agents-diagram.png]]

### 6. Combining and customizing these patterns（组合与定制这些模式）

这些构件**不是规定动作（aren't prescriptive）**，而是可被开发者塑形、组合以适配不同用例的常见模式。成功的关键——和任何 LLM 特性一样——是**衡量表现并在实现上迭代**。再强调一遍：只在复杂度能被证明改善结果时，才考虑增加它。

### 7. Summary（总结）

> **"Success in the LLM space isn't about building the most sophisticated system. It's about building the right system for your needs."**
> —— LLM 领域的成功不在于构建最复杂的系统，而在于为你的需求构建正确的系统。

路径：从简单的 prompt 开始 → 用全面的评测去优化 → 只有当更简单的方案不够用时，才加入多步的 agentic system。

实现 agent 时遵循三条核心原则：

1. **保持 agent 设计的简单性（Maintain simplicity）。**
2. **优先透明（Prioritize transparency）**——明确展示 agent 的规划步骤。
3. **精心打磨 agent-computer interface（ACI，智能体—计算机接口）**——靠充分的工具文档与测试。

框架能帮你快速起步，但走向生产时，别犹豫去**削减抽象层、用基础组件来构建**。遵循这些原则，你能造出既强大、又可靠、可维护、被用户信任的 agent。

### 8. Acknowledgements（致谢）

由 **Erik S.** 与 **Barry Zhang** 撰写。本文取材于 Anthropic 构建 agent 的经验、以及客户分享的宝贵洞见。

### 9. Appendix 1: Agents in practice（附录 1：实践中的 agent）

与客户的合作揭示了两个特别有前景的 AI agent 应用，它们都印证：**当任务同时需要「对话」与「行动」、有清晰的成功标准、能形成反馈环、并整合有意义的人类监督时，agent 增值最大**。

#### 9.A Customer support（客户支持）

客服把熟悉的聊天机器人界面，和通过工具集成而来的增强能力结合在一起，天然适合更开放式的 agent，因为：

- 支持类交互天然遵循对话流，同时需要访问外部信息与执行动作；
- 可集成工具来拉取客户数据、订单历史、知识库文章；
- 退款、更新工单等动作可被程序化处理；
- 成功可通过「用户定义的问题解决」被清晰衡量。

已有几家公司用「**只对成功解决的问题收费（usage-based pricing）**」的定价模式证明了这条路的可行性——这本身就显示了他们对自家 agent 有效性的信心。

#### 9.B Coding agents（编码 agent）

软件开发领域展现出巨大潜力，能力已从代码补全演进到自主解决问题。agent 在这里特别有效，因为：

- 代码方案可通过**自动化测试**验证；
- agent 能以测试结果为反馈**迭代**方案；
- 问题空间定义良好、结构化；
- 输出质量可被客观衡量。

在他们自己的实现中，agent 现在已能**仅凭 pull request 描述，就解决 SWE-bench Verified 基准里真实的 GitHub issue**。不过——尽管自动化测试有助于验证功能，**人类评审仍然关键**，用来确保方案与更广泛的系统需求对齐。

### 10. Appendix 2: Prompt engineering your tools（附录 2：为你的工具做提示词工程）

无论你构建哪种 agentic system，**工具（tools）都很可能是重要一环**。工具让 Claude 通过在 API 中指定其精确结构与定义，去与外部服务和 API 交互；Claude 若打算调用工具，其 API 响应里会包含一个 tool use block。**工具定义与规格，应当获得和整体 prompt 一样多的提示词工程投入。**

同一个动作往往有多种指定方式。比如指定文件编辑，可以写 **diff**，也可以**重写整个文件**；结构化输出可以把代码放进 markdown，也可以放进 JSON。在软件工程里这些区别是表面的、可无损互转的，但**有些格式对 LLM 来说比另一些难写得多**：写 diff 需要在写新代码前就知道 chunk 头里改了多少行；把代码写进 JSON（相比 markdown）需要额外转义换行和引号。

决定工具格式的建议：

- 给模型足够的 token 去「思考」，别让它把自己写进死角。
- 让格式**贴近模型在互联网文本中自然见过的样子**。
- 确保没有格式「开销」——比如要精确数上千行代码的行数、或对写出的代码做字符串转义。

一条经验法则：想想人们在**人机接口（HCI）**上投入了多少心力，就计划在打造好的**智能体—计算机接口（ACI）**上投入同样多。具体怎么做：

- **站在模型的立场（Put yourself in the model's shoes）**：光看描述和参数，用法是否一目了然，还是需要仔细琢磨？如果你要琢磨，模型多半也要。好的工具定义常包含**示例用法、边界情况、输入格式要求、以及与其他工具的清晰界限**。
- 怎么改参数名或描述能让事情更显然？把它当成**给团队里一个初级开发者写一份出色的 docstring**——在使用许多相似工具时尤其重要。
- **测试模型怎么用你的工具**：在 workbench 里跑很多示例输入，看模型犯什么错，然后迭代。
- **给工具做 Poka-yoke（防呆）**：改动参数，让犯错更难。

> **"While building our agent for SWE-bench, we actually spent more time optimizing our tools than the overall prompt."**
> —— 构建 SWE-bench agent 时，他们花在优化工具上的时间，其实比花在整体 prompt 上还多。

一个具体案例：他们发现，当 agent 移出根目录后，模型用**相对路径（relative filepaths）**的工具会出错。修法是把工具改成**总是要求绝对路径（absolute filepaths）**——之后模型用得毫无瑕疵。这正是 poka-yoke 的示范：不是让模型更聪明，而是让接口更防呆。

---
## 精读收尾

- **一句话总结**：Agent 不神秘——它通常就是「LLM 在循环里基于环境反馈用工具」；成功靠的不是最复杂的框架，而是从增强型 LLM 出发、按需逐级加复杂度（五种 workflow 模式 → 自主 agent），且只在复杂度能被证明改善结果时才加。

- **关键引语**：
  1. **"Workflows are systems where LLMs and tools are orchestrated through predefined code paths. Agents … are systems where LLMs dynamically direct their own processes and tool usage."** —— 路径谁定，谁就定义了 workflow 与 agent 的分界。
  2. **"They are typically just LLMs using tools based on environmental feedback in a loop."** —— agent 的祛魅式定义。
  3. **"Success in the LLM space isn't about building the most sophisticated system. It's about building the right system for your needs."** —— 反复杂度的中心主张。
  4. **"Plan to invest just as much effort in creating good agent-computer interfaces (ACI)"** —— 把 ACI 抬到与 HCI 同等的工程地位。
  5. **"While building our agent for SWE-bench, we actually spent more time optimizing our tools than the overall prompt."** —— 工具工程 > prompt 工程的一手证据。

- **与 vault 的连接**：
  - [[agent-vs-workflow]] —— 这篇正是该 wiki 概念页的原始出处：workflow/agent 分界 + 五种 canonical 模式（Prompt Chaining / Routing / Parallelization / Orchestrator-Workers / Evaluator-Optimizer）都源自本文。
  - [[verification-loops]] —— evaluator-optimizer 模式 + 附录 B「以测试为反馈迭代」是 verification-loops 的祖型论证。
  - [[orchestration-loop]] —— 「LLM 在循环里基于环境反馈用工具」就是 TAO（Thought-Action-Observation）循环的原始表述。
  - [[assumptions-expire]] —— 「只在复杂度能被证明改善结果时才加」「走向生产时削减抽象层」与「脚手架随模型变强而剥离」同源。

- **视频适配自评**：**适合**做白板讲解视频。理由：全文是一条清晰的「复杂度阶梯」——增强型 LLM → 5 种 workflow → 自主 agent，每一层都有独立配图和「何时用」判据，天然可空间化成一张递进图；且每个模式配一个具体例子，讲解张力足。ACI/poka-yoke 那段（绝对路径案例）是很好的收尾「金句 + 反直觉细节」。

---
### 文末注记（headless 消歧自决）

1. **文件结构**：格式模板里元信息头用 `# 精读：{标题}` 作 H1、章节用 `##`；本次按任务要求「正文为 `## 精读` section」执行，故将整体降一级——H1 标题 + `## 精读` 段包裹，元信息头置于段首，原文各章为 `###`，Building blocks 的子模式为 `####`。论证顺序与原文完全一致。
2. **来源日期**：原文 Anthropic 博客的初版早于本 raw；但本 raw 快照已含更新后的模型名（Claude Haiku 4.5 / Sonnet 4.5），属修订版。frontmatter `created/last-updated` 用今日 2026-07-07；「来源」行日期用 raw 文件名日期 2026-07-05 并注明为 vault 抓取日，未杜撰原始发布日。
3. **字数/时长**：原文英文正文约 2,400 words 为估算，预读时长按此估 ~12 分钟。
4. **章节编号**：附录 1/2 计入连续编号（9/10），其子节沿用 9.A/9.B、5.1–5.7 的层级编号，以保留原文嵌套结构。
5. **配图**：原文所有插图均为 workflow 示意图，正文以「图：…」一句话描述其内容，未嵌入 PNG（S1 跑不做图示）。
