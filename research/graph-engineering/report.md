# Graph Engineering 深度调研报告

> 调研日期：2026-07-29  
> 调研范围：原始文章、X 时间线、官方工程文档、框架文档、研究论文、实践者与批评者文章  
> 面向读者：能使用 Claude Code / Codex / API，但不是资深系统工程师的 AI builder  
> 截止时间：2026-07-29

## Executive Summary

**Graph Engineering（图工程）是把多个 agent loop、确定性函数、工具、人工审批和
验证器组织成一张可执行、可观察、可恢复的图。** 节点负责工作，边规定下一步和权限，
显式状态承载跨节点信息，runtime 负责调度、并行、汇合、暂停与恢复。

这个名字在 2026 年 7 月突然流行，但底层做法不是新发明。LangGraph、AutoGen 等框架
早已用图或状态机编排 agent；Anthropic 在 2024 年已经公开总结了 chaining、routing、
parallelization、orchestrator-workers 和 evaluator-optimizer 等图形化工作模式。
2026 年真正变化的是：一个节点现在可以是一段能力较强、运行时间较长的 agent loop，
因此工程重点开始从“让一个 agent 做对”上移到“让多个自治步骤作为一个系统协作”。

本轮最重要的事实校正是：**Peter Steinberger 的 2026 年 7 月 18 日帖子引爆了讨论，
但没有提出一个新框架，也没有创造图编排。Josh Simmons 的 7 月 4 日文章是本次检索中
最早可追踪、明确用完整名称定义 agent orchestration 的材料；但这仍不足以证明他
“发明”了术语或底层实践。** 2024 年 2 月已有 `flow (/graph) engineering` 的相关
表述，说明语义前身更早存在；由于社交检索并不完备，最严谨的说法是
“本次检索中最早可追踪的显式定义”，而不是绝对的“首创者”。

对 builder 的实用结论不是“赶快搭一支 agent 舰队”，而是：

1. 一个 agent 能稳定完成时，保留一个 loop。
2. 当任务出现可独立并行的责任、必须强制的审批、不同权限边界、局部重试或断点恢复时，
   才把这些边界画成图。
3. 当多个 agent 会修改同一份文件或共享可变状态时，把
   **single writer + read-only specialists + explicit verifier** 作为保守默认值，
   避免并行 writer 做出隐含且冲突的决定。
4. 先定义 state、node contract、edge condition 和失败路径，再决定是否需要 LangGraph
   或其他框架。

## 1. Graph Engineering 是什么

### 最简单的定义

**Graph Engineering 是设计和运行 agent 系统的控制拓扑：谁工作、谁检查、信息如何流动、
何时分支或汇合、哪里必须暂停，以及失败后从哪里恢复。**

一个最小的执行图包含四层：

| 层 | 它回答的问题 | 例子 |
|---|---|---|
| Node | 谁或什么做这一小段工作？ | agent loop、普通函数、检索、测试、人工审批 |
| Edge | 哪个结果允许走向哪里？ | tests pass → merge；needs evidence → research |
| State | 节点之间传递和持久化什么？ | 任务、证据、版本、预算、审批结果、错误 |
| Runtime | 图如何真正运行？ | 调度、并行、汇合、checkpoint、retry、resume、trace |

LangGraph 的官方解释把 graph 拆成 `State`、`Nodes` 和 `Edges`，并强调 node 可以是普通
代码、单次模型调用、工具调用或一个完整 agent；edge 可以确定，也可以根据 state
动态选择。概念上的 control graph 只需要 nodes 与 edges；要让它实际运行，还需要
runtime 和运行时 state；只有需要 checkpoint、跨进程 resume 或长期等待时，
**durable state** 才成为必要条件。三者不能混为一谈。
[LangGraph Graph API](https://docs.langchain.com/oss/python/langgraph/graph-api)；
[LangChain 的 2026 年回顾](https://www.langchain.com/blog/3-years-of-graph-engineering-with-langgraph)

### 必要消歧：至少有两种 Graph Engineering

当前社区把两个不同对象用了同一个名字：

| 用法 | 被工程化的对象 | 核心问题 |
|---|---|---|
| Agent execution graph | 工作、控制流与责任关系 | 谁运行、何时运行、失败怎么办 |
| Knowledge graph engineering | 实体、事实与语义关系 | 系统知道什么、关系如何建模与检索 |

知识图谱工程在本轮话题出现之前已经是成熟术语；例如 2023 年论文已经直接讨论
“LLM-assisted Knowledge Graph Engineering”。
[Meyer 等，2023](https://arxiv.org/abs/2307.06917)

两者可以同时出现：执行图中的 research node 可以查询知识图谱，但“知识如何连接”和
“工作如何流转”仍是两个不同的设计问题。把两者混成一个定义，会让读者误以为
GraphRAG、Obsidian wikilink、agent delegation 和 checkpointing 是同一种能力。

本报告后文使用第一种含义：**agent execution graph**。

## 2. 它从哪里来，为什么现在出现

### 起源不是一个人的“发明”

需要把三件事分开：

- **旧实践：** 状态机、DAG、工作流引擎、多 agent 协作和图调度已有多年历史。
- **术语形成：** 社区逐渐用 graph/flow engineering 描述 agent 控制流设计。
- **传播事件：** 2026 年 7 月的一组 X 帖子让 `Graph Engineering` 成为流行标签。

本次检索能追踪到的关键节点如下：

| 日期 | 事件 | 证据强度 |
|---|---|---|
| 2024-01-23 | LangGraph 已把 multi-agent workflow 表示为 nodes、edges 和 graph state | LangChain 当时的官方文章 |
| 2024-02-29 | Itamar Friedman 在回应 LangChain 时写到从 prompt engineering 转向 `flow (/graph) engineering` | 更早的语义前身，但不是完整独立短语；原帖 URL 可定位，正文由来源时间线复核 |
| 2026-04-13 | 预印本从 scheduler 角度比较 agent loop 与 structured graph，并调查 70 个开源项目 | 原始论文；属于 position paper，没有实验结果 |
| 2026-07-04 | Josh C. Simmons 发表系统化文章，明确命名 `graph engineering` | 原始文章 |
| 2026-07-11 | Mike 发出 prompt → context → harness → loop → graph 的层级帖子 | 原始 X URL可定位；正文由来源时间线复核 |
| 2026-07-18 | Peter Steinberger 问：“Are we still talking loops or did we shift to graphs yet?” | 原始 X URL；帖子只有问题，没有定义 |
| 2026-07-18 | Hamel Husain、Shubham Saboo、Carlos E. Perez 等快速扩展这个叙事 | 原始 X URL与同期文章 |
| 2026-07-22 | LangChain 用“3 Years of Graph Engineering”回应，承认 buzzword，同时阐述既有实践 | 官方文章 |

关于社交帖时间线与早期用例，本报告使用
[AI Builder Club 的逐项来源审计](https://www.aibuilderclub.com/blog/graph-engineering-peter-steinberger)
作为索引，并保留其指向的
[Itamar Friedman 原帖](https://x.com/itamar_mar/status/1763168555539812407)、
[Mike 原帖](https://x.com/michaelmasson55/status/2075913998449701170)和
[Peter Steinberger 原帖](https://x.com/steipete/status/2078277297791189132)。
由于 X 当前限制正文与实时指标读取，不能把该时间线升级成“穷尽式起源证明”。

因此，最稳妥的历史结论是：

> Josh Simmons 的文章是本次检索中最早可追踪的显式、完整定义；
> Steinberger 的帖子是显著放大器；目前没有证据支持任何一人“发明”了底层实践，
> 也没有足够完整的社交档案支持绝对的“术语首创者”结论。

### 为什么是 2026 年 7 月

这是一次 **naming event（命名事件）**。下面不是已经被单一研究证明的因果链，而是
本报告综合 Anthropic 的 agent 生产复盘、LangGraph 的历史和 7 月传播材料后提出的解释：

1. **单节点能力提高。** 一个 coding/research agent 已经能在内部运行多轮工具 loop，
   “节点能不能做事”不再是唯一瓶颈。
2. **任务跨度变长。** 多文件、多来源、人工审批、长时间等待和局部失败需要显式状态与
   恢复，而不是全部塞在一个 transcript 中。
3. **并行能力可用。** 多个独立研究方向或互不重叠的任务可以并行，但需要 fan-out、
   fan-in 和结果仲裁。
4. **框架先于术语成熟。** LangGraph、AutoGen GraphFlow 以及 Anthropic 的
   orchestrator-workers 已提供现成机制，社区只是在寻找一个总括名称。
5. **术语传播具有自我强化。** “prompt → context → harness → loop → graph”的梯子
   很容易被压缩成帖子、课程和产品定位，因此传播速度远高于实证积累速度。

其中前三点有
[Anthropic 的 multi-agent 生产复盘](https://www.anthropic.com/engineering/multi-agent-research-system)
作为机制与边界证据；第四点可由 2024 年的 LangGraph 与 Anthropic 官方材料直接确认；
第五点是对 7 月密集发布序列的研究者综合，而不是可单独验证的因果事实。

## 3. 核心机制：不要只画组织架构图

可以把 Graph Engineering 类比成设计一条“有自主员工的生产线”，但必须保留一个边界：
传统机器按照固定规则执行，agent node 会解释任务、调用工具并作出不可完全预测的判断。
因此你不仅要设计工序，还要设计哪些判断能交给模型、哪些必须由代码或人决定。

### 三个关键认知

#### 认知一：Graph 是控制流，Loop 是节点内部的执行纪律

Anthropic 把 agent 描述为根据环境反馈使用工具的 loop；它同时公开了 prompt chaining、
routing、parallelization、orchestrator-workers 和 evaluator-optimizer 等组合模式。
[Anthropic: Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents)

所以“loop 已死，graph 接班”是错误二分：

- 一个 loop 是带回边的最小 graph。
- 一个 graph 通常包含多个 loop。
- Graph 解决跨步骤的依赖、路由和责任；Loop 解决一个节点如何持续尝试直到通过验证。

#### 认知二：State 与 contract 比 agent 数量更重要

一个可靠节点至少需要明确：

- 输入 schema 与允许读取的上下文；
- 输出 artifact 与完成条件；
- 是否允许产生副作用；
- 可用工具和权限；
- token、时间与金钱预算；
- retry 是否安全、如何做到 idempotent；
- 失败时走向哪个节点；
- 谁能批准下一条 edge。

如果这些内容仍藏在 orchestrator 的自然语言记忆里，那么增加 subagent 只是把一个不透明
loop 变成多个不透明 loop。图工程的价值来自 **把隐含决定变成可检查的结构**。

#### 认知三：图的价值取决于任务的可分解性

Google Research 在 180 个 agent 配置上的控制实验发现：集中式 multi-agent 在可并行
金融分析任务上相对 single-agent 提升 80.9%，但所有 multi-agent 变体在强顺序规划任务
上下降 39%–70%；独立并行 agent 的错误放大最高达到 17.2 倍，而带 orchestrator 的
集中式结构将其限制在 4.4 倍。该实验不是对所有真实生产任务的普适定律，但它有力反驳了
“agent 越多越好”。
[Google Research, 2026](https://research.google/blog/towards-a-science-of-scaling-agent-systems-when-and-why-agent-systems-work/)

这给出一个简单判据：

> 先问工作能否被切成低依赖、可独立验证的部分；不能，就不要为了并行而并行。

## 4. 与相邻概念的关系

| 概念 | 主要对象 | 典型失败 | 与 Graph Engineering 的关系 |
|---|---|---|---|
| Prompt engineering | 一次指令 | 意图表达不清 | node 内部输入的一部分 |
| Context engineering | 当前模型看到的信息 | 缺失、污染、过载 | 设计 node context 与跨 edge 传递 |
| Harness engineering | agent 的工具、环境、权限和运行脚手架 | 工具误用、环境不可靠 | 每个 node 的运行容器与系统能力 |
| Loop engineering | 单个 agent 的 observe-act-verify 循环 | 漂移、无限重试、错误停止 | graph 中自治 node 的内部机制 |
| Workflow / state machine | 预定义控制路径与状态转移 | 过度僵化、分支爆炸 | graph engineering 的直接工程祖先 |
| Multi-agent orchestration | 多个 agent 的协作 | 上下文碎片、冲突决定、成本 | graph 的一种节点配置，不是 graph 的全部 |
| Knowledge graph | 知识实体与关系 | 实体消歧、陈旧、错误传播 | 可作为 state/retrieval 层，但不等于执行图 |

Anthropic 对 workflow 与 agent 的区分很有帮助：workflow 由预定义代码路径编排，
agent 则由模型动态决定过程。一个实际 Graph Engineering 系统通常混合两者——把
审批、权限、预算和确定性检查固化为 edge，把开放探索留给 agent node。

## 5. 社区讨论地图

### 阵营一：Graph 是 agent 系统的下一层工程对象

Josh Simmons 的文章把重点放在 typed edges、checkpointed state、局部恢复、预算和
trajectory evaluation 上。这一派认为，单个 agent loop 变可靠后，新的瓶颈是多个
执行单元之间的调度与治理。
[原文](https://www.drjoshcsimmons.com/writing/we-are-entering-the-graph-engineering-phase)

这一定义对生产系统最有用，因为它不要求每个 node 都是 agent，也不把 graph 限制为 DAG。

### 阵营二：这基本就是既有的 graph workflow / state machine

LangChain 的立场最直接：这个词有 buzzword 成分，但把 agent 表示成图确实有用；
LangGraph 已经做了三年。它同时提醒：

- production agent graph 通常有 cycle，不只是 DAG；
- loop 本身就是简单 graph；
- 有些开放任务不适合预先固定 edge；
- 真正可能变新的，是现在一个 node 可以容纳完整 coding agent。

这不是完全否定新术语，而是把“新发明”降级为“新的工程关注点和传播标签”。

### 阵营三：重点不应是更多 agent，而应是上下文与单一写入权

Cognition 在 2025 年批评 naive multi-agent 的两个问题：子 agent 得不到完整决策上下文；
多个 writer 会做出彼此冲突的隐含决定。2026 年的更新并没有完全撤回该观点，而是认可了
更窄的一类模式：**多个 agent 提供 read-only intelligence，但 writes 保持
single-threaded**。
[Cognition, 2025](https://cognition.com/blog/dont-build-multi-agents)；
[2026 更新](https://cognition.com/blog/multi-agents-working)

这不是对 Graph Engineering 的反证，反而是一个重要设计约束：graph 的目标不是把每件事
拆给不同 writer，而是显式管理信息、决策权和副作用。

### 阵营四：Graph 还可能指 knowledge/memory graph

部分社区文章把 agent execution graph、GraphRAG、Obsidian 链接和 temporal memory
放进同一个总框架。这能启发组合架构，但会模糊证据：知识图谱确实有多年研究与 benchmark，
却不能用来证明 multi-agent orchestration 本身有效。

在没有明确限定时，看到 “Graph Engineering improves retrieval / multi-hop QA” 应先问：
它测的是知识图谱，还是执行图？

### 最强争议与未决问题

1. **静态还是动态？** 静态图可验证，但开放研究和复杂 coding 的子任务往往只有运行时才
   能发现。LangChain 甚至表示早期 deep research 从预定义 graph 转向更 agentic 的核心
   loop。
2. **谁拥有 state？** transcript、共享文件、数据库和 typed state 各有一致性与上下文
   成本，目前没有统一答案。
3. **谁可以写？** parallel read 通常安全；parallel write 容易制造冲突和隐含决定。
4. **如何评估路径？** 最终输出正确不等于执行路径合理；但“正确 trajectory”也未必唯一。
5. **成本是否值得？** 某些 multi-agent graph 可能增加 token、延迟和协调成本；
   checkpoint、可观察性与恢复能力本身也有实现成本。具体净收益取决于任务可并行性、
   节点类型和失败频率，不能从“用了 graph”直接推出。

## 6. 代表性来源与实践证据

### 术语与传播

- **Josh C. Simmons，2026-07-04，本次检索中最早可追踪的显式定义者。** 给出
  nodes、typed edges、checkpointed state、human nodes 和 budget-in-state 的完整
  主张。它是立场文章，引用的 scheduler paper 本身明确没有生产实现或实验结果。
  [原文](https://www.drjoshcsimmons.com/writing/we-are-entering-the-graph-engineering-phase)
- **Peter Steinberger，2026-07-18，amplifier。** 原帖只有一个问题，不包含定义或发布。
  X 实时 engagement 当前不可直接核验；第三方快照显示这是高传播帖子，但不在报告中给出
  “Top”排名。[原帖](https://x.com/steipete/status/2078277297791189132)
- **LangChain，2026-07-22，institutional adopter/critic。** 既借用新标签重新解释
  LangGraph，也明确承认它是 buzzword 和既有实践。
  [原文](https://www.langchain.com/blog/3-years-of-graph-engineering-with-langgraph)

### 官方机制与生产经验

- **Anthropic，2024-12-19。** 给出从 chain、route、parallelize 到
  orchestrator-workers、evaluator-optimizer 的模式，并坚持“从最简单方案开始”。
  [Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents)
- **Anthropic，2025-06-13。** 多 agent research 内部评测相对 single-agent baseline
  提升 90.2%，但 multi-agent 约使用普通 chat 15 倍 token；Anthropic 也明确说高依赖
  任务和多数 coding 任务未必适合。
  [工程复盘](https://www.anthropic.com/engineering/multi-agent-research-system)
- **LangGraph。** 官方将 node、edge、state、checkpoint、interrupt 和动态 routing
  作为核心运行原语；这证明图编排可实际实现，但厂商自述的下载量和案例不等于独立效果
  benchmark。
- **AutoGen GraphFlow。** 官方文档支持 sequential、parallel、conditional 和 loop，
  同时仍标为 experimental，并建议只有在需要严格顺序和条件控制时采用。
  [官方文档](https://microsoft.github.io/autogen/dev/user-guide/agentchat-user-guide/graph-flow.html)

### 研究与反证

- **Hu Wei，2026。** 将 agent loop 描述为 single-ready-unit scheduler，并调查 70 个
  开源项目；论文明确是 position paper 和 design proposal，没有生产实现或实证性能
  结果。因此它支持概念框架与项目分类，不能支持“graph 已被实验验证优于 loop”。
  [arXiv:2604.11378](https://arxiv.org/abs/2604.11378)
- **Google Research，2026。** 180 个配置的实验表明 multi-agent 的收益高度依赖任务
  是否可并行、工具密度与协调架构，是当前最有力的“不要默认加 agent”证据之一。
  [研究摘要与论文入口](https://research.google/blog/towards-a-science-of-scaling-agent-systems-when-and-why-agent-systems-work/)
- **Cognition，2025–2026。** 来自 coding agent 实践者的反方与修正：read-only
  specialist 有价值，parallel writer 仍容易因上下文不完整和隐含决定冲突而失败。

## 7. 对 AI builder 的实际价值

### 先说结论

Graph Engineering 最有价值的地方不是让你学会一个新框架，而是迫使你回答四个问题：

1. 我的系统中有哪些不同责任和副作用？
2. 哪些依赖、批准和失败路径不能只靠模型“记得”？
3. 哪些部分真正可以独立并行？
4. 运行中断后，什么 state 足以让它安全恢复？

如果这四个问题没有答案，画 graph 只会把混乱可视化；如果答案很清楚，很多时候一个
简单 driver、状态文件和几个函数就已经够用，不一定需要专用框架。

### 三种值得使用的场景

#### 场景 A：只读并行研究

把来源起源、社区争议、机制和反证分给独立 researcher，主 agent 统一核对并写结论。
这类工作分支低耦合，结果可以在汇合点独立审查，是 multi-agent 的强适配场景。

#### 场景 B：有明确闸门的内容或软件生产

例如 research → human selects topic → draft → evidence review → publish。价值来自：

- 人的选择是显式 node；
- 未通过证据检查不能走向 publish；
- draft 失败只重跑 draft/review，不重跑 research；
- 每一步交付物是持久 state，不依赖一个对话记住全部历史。

#### 场景 C：权限和副作用必须隔离

一个 node 只读搜索，一个 node 可写草稿，一个 node 可以部署但必须人工批准。此时 graph
表达的是 authority boundary，而不只是执行顺序。

### 什么时候不要使用

- 一个 agent 在一个上下文内已经稳定完成；
- 工作高度顺序化，后一步必须理解前一步的全部隐含决定；
- 没有独立 verifier，只有多个 agent 互相认同；
- 共享 state 没有 schema 或版本；
- 每个节点都能写同一份文件或生产系统；
- token、延迟和协调成本高于任务价值；
- 任务结构在运行前完全不可知，却被强行塞进静态 DAG。

## 8. 建议的第一步

不要先安装框架。选一条真实工作链，用 20 分钟画一张 **control graph**：

1. 写出最终要保留的 artifact。
2. 列出真正不同的责任，而不是给同一职责换角色名。
3. 给每个 node 写：input、output、verifier、side effect、owner。
4. 标出三个 edge：成功、证据不足、失败/超预算。
5. 标出唯一 writer 和所有 human authority points。
6. 找出可以只读并行的部分；其余保持单线程。
7. 只有当手写 driver 无法满足 checkpoint、dynamic routing 或 observability 时，再评估
   LangGraph、AutoGen GraphFlow 或其他 runtime。

一个实用的最小形状是：

```text
request
  ├─> read-only researcher A ─┐
  ├─> read-only researcher B ─┼─> single synthesizer
  └─> read-only critic ───────┘          |
                                     verifier
                                      /     \
                                  pass       revise
                                    |
                              human approval
```

这已经是一张概念 control graph；要成为可执行、可恢复的系统，还需要定义运行时 state、
调度、持久化和失败语义。它没有为了“多 agent”而制造多个 writer，也没有把人工判断
藏在图外。

## 最容易被误传的三件事

1. **“Josh Simmons 无争议地首创了 Graph Engineering。”**  
   他是本次检索中最早可追踪的完整显式定义者，但更早存在相关语义用例，且公开检索无法
   穷尽已删除、私密或未索引材料。应保留检索边界。
2. **“Peter Steinberger 发明了 Graph Engineering。”**  
   他的帖子是 12 个英文词的问题，不包含该术语、定义或新能力发布；作用是放大。
3. **“Graph 已经证明比 Loop 更好。”**  
   两者不是互斥架构。现有证据表明 graph/multi-agent 在可并行任务上可能显著获益，
   在强顺序任务上也可能显著变差。

## 关键资源索引

### Start here

- [Josh C. Simmons: We Are Entering the Graph Engineering Phase](https://www.drjoshcsimmons.com/writing/we-are-entering-the-graph-engineering-phase)
- [LangChain: 3 Years of Graph Engineering with LangGraph](https://www.langchain.com/blog/3-years-of-graph-engineering-with-langgraph)
- [Louis Bouchard: Graph Engineering Explained — What Actually Changed](https://www.louisbouchard.ai/graph-engineering-explained/)

### Primary and official sources

- [Anthropic: Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents)
- [Anthropic: How We Built Our Multi-Agent Research System](https://www.anthropic.com/engineering/multi-agent-research-system)
- [AutoGen GraphFlow](https://microsoft.github.io/autogen/dev/user-guide/agentchat-user-guide/graph-flow.html)
- [Peter Steinberger's July 18 post](https://x.com/steipete/status/2078277297791189132)

### Selected independent explanations

- [CodesDevs: What Is Graph Engineering for AI Agents?](https://codesdevs.io/notes/graph-engineering-ai-agents/)
- [AI Builder Club: Peter Steinberger's “Loops or Graphs?” timeline](https://www.aibuilderclub.com/blog/graph-engineering-peter-steinberger)

### Criticism and counter-evidence

- [Google Research: Towards a Science of Scaling Agent Systems](https://research.google/blog/towards-a-science-of-scaling-agent-systems-when-and-why-agent-systems-work/)
- [Cognition: Don't Build Multi-Agents](https://cognition.com/blog/dont-build-multi-agents)
- [Cognition: Multi-Agents — What's Actually Working](https://cognition.com/blog/multi-agents-working)

### Papers and adjacent meanings

- [From Agent Loops to Structured Graphs](https://arxiv.org/abs/2604.11378)
- [LLM-assisted Knowledge Graph Engineering](https://arxiv.org/abs/2307.06917)
