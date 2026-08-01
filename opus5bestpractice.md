# Claude Opus 5 深度调研报告

> 调研日期：2026-07-29 | 基于25+条搜索查询、覆盖X/Twitter、YouTube、官方文档、博客

---

## 1. Opus 5概述

### 发布时间与基本信息

Claude Opus 5 于 **2026年7月24日（周四）** 由 Anthropic 正式发布。它是 Claude 5 系列的第四个模型（此前已发布 Mythos 5、Fable 5、Sonnet 5）。

### 核心规格

| 项目 | 规格 |
|------|------|
| 模型ID | `claude-opus-5` |
| 上下文窗口 | **1M tokens**（默认即最大） |
| 最大输出 | 128K tokens（Batch API可达300K） |
| 定价 | $5/M 输入 · $25/M 输出（与Opus 4.8相同） |
| Thinking | 默认开启，不可在xhigh effort下关闭 |
| Fast模式 | 2.5倍速度，2倍价格 |
| 可用平台 | Claude Pro/Max/Team/Enterprise、Claude API、AWS Bedrock、Google Cloud、Microsoft Foundry |

### 定位

Opus 5 定位为 **"每天都用的模型"** —— 接近 Fable 5 的前沿智能，但价格只有一半。它是 Claude Max 的新默认模型，也是 Claude Pro 上可用的最强模型。

### 模型家族定位

| 模型 | 定位 | 价格（输入/输出，$/M tokens） |
|------|------|------|
| **Haiku** | 轻量快速 | 最低 |
| **Sonnet 5** | 性价比平衡 | $2-3/$10-15 |
| **Opus 5** | 日常主力、长程agent | $5/$25 |
| **Fable 5** | 前沿旗舰、最难任务 | $10/$50 |
| **Mythos 5** | 安全受限的顶级能力 | 受限访问 |

> 来源：[Introducing Claude Opus 5 - Anthropic](https://www.anthropic.com/news/claude-opus-5)

---

## 2. Opus 5最擅长什么

### 核心强项

1. **长程Agentic编码** —— 在Frontier-Bench v0.1上，Opus 5得分43.3%，超过Fable 5（33.7%），是Opus 4.8的两倍以上。在大型代码库中处理架构、部署、设计级UI表现出色。

2. **自我验证与纠错** —— Opus 5会自动检查自己的工作并迭代修正，无需提示。在测试中，它自己编写了计算机视觉pipeline来从原始像素中提取几何信息，填补空缺并修正错误。

3. **新颖问题求解** —— 在ARC-AGI 3上得分是第二名的3倍，展示了极强的新颖问题解决能力。

4. **业务自动化** —— 在Zapier AutomationBench上，通过率约为第二名的1.5倍，即使在最低effort设置下也超过所有其他模型。

5. **Computer Use** —— 在OSWorld 2.0上，以Fable 5三分之一的成本超过其最佳结果。

6. **代码审查** —— CodeRabbit测试显示，Opus 5的精确度（39.3%）是有史以来最高的，是一个"精度专家"。

7. **金融研究** —— 在数值推理、表格工作和批判性思维方面表现突出。

8. **视觉输出** —— 前端动画、游戏、3D工作的质量有显著提升。

9. **Prompt注入防护** —— Boris Cherny称这是"我们迄今为止最不容易被prompt注入的模型"。

### 最佳使用场景

- 长时间运行的multi-step agent任务
- 复杂的代码重构和全功能开发
- 大型代码库中的架构决策
- 需要高精度判断的知识工作（金融、法律、医疗）
- 需要自我验证的自主工作流
- 日常coding：bug修复、小功能开发

> 来源：[ClaudeDevs on X](https://x.com/ClaudeDevs/status/2080703247665574315) · [Anthropic官方发布](https://www.anthropic.com/news/claude-opus-5) · [Boris Cherny on X](https://x.com/bcherny/status/2080713091688583312)

---

## 3. Opus 5 vs Fable 5 vs Sonnet 5 决策框架

### 三句话总结

- **Sonnet 5** = 执行层（快速、便宜、够用就好）
- **Opus 5** = 判断层（日常主力、复杂任务的最佳性价比）
- **Fable 5** = 升级层（最难、最模糊、重做成本最高的任务）

### 决策矩阵

| 场景 | 推荐模型 | 理由 |
|------|----------|------|
| 日常bug修复和小功能 | **Opus 5** | 性价比最高的日常驱动 |
| 大量重复性任务/批处理 | **Sonnet 5** | 价格低，规模化成本可控 |
| 长程agent工作（几小时） | **Opus 5** | 自我验证能力强，保持一致 |
| 极度复杂/模糊的架构决策 | **Fable 5** | 边际思考最全面 |
| 代码审查 | **Opus 5** | 精确度最高，低effort也稳定 |
| 前端UI/视觉复制 | **Opus 5** | 视觉能力强提升 |
| 最复杂的全栈应用构建 | **Fable 5** | 在最难测试中仍领先 |
| 文档/spreadsheet生成 | **Opus 5** | 复杂公式和slide结构能力强 |
| 法律agent工作 | **Fable 5** | 在Legal Agent Benchmark上领先 |
| DeepSWE v1.1（深度SWE） | **Fable 5** | 72.7% vs Opus更低分 |
| 日常内容撰写 | **Sonnet 5** | 快速足够 |

### Jason Zook的实战总结（高互动帖子）

> **Fable 5** — 当你需要模型思考比你更多的边界情况时。大的、复杂的功能/问题。也是很好的审查者。
>
> **Opus 5** — 其他所有事情。Bug修复、随机小功能，Opus 5都做得很好。我停止了完全信任Opus 4.8（我会直接用Fable），但我信任Opus 5。Opus 5是一个很好的日常驱动。

### 成本对比

| 模型 | 输入价格 | 输出价格 | CursorBench每任务成本 |
|------|----------|----------|----------------------|
| Sonnet 5 | $2-3/M | $10-15/M | 最低 |
| Opus 5 | $5/M | $25/M | ~$8.23（Max effort） |
| Fable 5 | $10/M | $50/M | ~$17.32（Max effort） |

> 来源：[Jason Zook on X](https://x.com/jasondoesstuff/status/2081312609622479215) · [BridgeMind on X](https://x.com/bridgemindai/status/2080707321806868774) · [Composio comparison](https://composio.dev/content/opus-vs-fable)

---

## 4. X平台Top高互动内容

### 官方与核心帖子

| 作者 | 内容摘要 | 链接 |
|------|----------|------|
| **@claudeai** (官方) | Opus 5在coding和知识工作评估上是新SOTA | [链接](https://x.com/claudeai/status/2080699497064083942) |
| **@ClaudeDevs** (官方开发者) | Opus 5是Opus类别的step-change，擅长长程项目、大代码库 | [链接](https://x.com/ClaudeDevs/status/2080703247665574315) |
| **@bcherny** (Boris Cherny, Claude Code创建者) | Opus 5是最不容易被prompt注入的模型，用日常积累的能力做编码、数据分析、设计 | [链接](https://x.com/bcherny/status/2080713091688583312) |
| **@trq212** (Thariq, Anthropic工程师) | 我们删除了Claude Code系统提示的~80%，这是我们学到的 | [链接](https://x.com/trq212/status/2080710971228918066) |

### 高互动用户帖子

| 作者 | 核心内容 | 链接 |
|------|----------|------|
| **@danshipper** (Dan Shipper, Every) | "Opus 5难以爱上"——与现有工作流不兼容，但删除旧skills后效果极好 | [链接](https://x.com/danshipper/status/2080700057892815114) |
| **@mikeyk** (Mike Krieger, Instagram联合创始人) | Opus 5迅速成为日常驱动，可以连续工作数小时 | [链接](https://x.com/mikeyk/status/2080702940445397167) |
| **@clairevo** (claire vo) | "我讨厌用它，但在盲测中它排名第一" | [链接](https://x.com/clairevo/status/2080703735878336983) |
| **@jasondoesstuff** (Jason Zook) | Opus 5 vs Fable 5使用场景详细对比 | [链接](https://x.com/jasondoesstuff/status/2081312609622479215) |
| **@levie** (Aaron Levie, Box CEO) | Opus 5在Box企业AI Agent上取得显著性能提升 | [链接](https://x.com/levie/status/2080704871934931221) |
| **@sairahul1** (Rahul) | 转发Anthropic官方Opus 5 prompting指南的关键要点 | [链接](https://x.com/sairahul1/status/2081737872579908017) |
| **@ArtificialAnlys** (Artificial Analysis) | Opus 5是Intelligence Index上最高分模型，成本比Fable 5低26% | [链接](https://x.com/ArtificialAnlys/status/2080734447717298483) |
| **@AnatoliKopadze** | "你唯一需要的Opus 5 context engineering文章" | [链接](https://x.com/AnatoliKopadze/status/2080730708918538538) |
| **@kenbwork** (Kenny Workman) | Opus 5在9项生物学基准测试中表现最佳 | [链接](https://x.com/kenbwork/status/2080727200299622509) |
| **@jerhadf** (jeremy, Anthropic) | Opus 5在medium effort下的FrontierCode分数反而比higher effort更高 | [链接](https://x.com/jerhadf/status/2080806399794163798) |

### X平台Top Tips汇总

1. **完整任务一次给出** —— 不要分步喂指令（@sairahul1）
2. **默认用low/medium effort** —— 只在需要时提升到xhigh（@sairahul1）
3. **删除旧的verification指令** —— Opus 5自己会验证（@trq212）
4. **让它拥有工作** —— 停止微观管理（@sairahul1）
5. **明确要求简短回复** —— effort控制思考量而非输出长度（官方指南）
6. **删除旧的skills重新开始** —— 旧工作流会与Opus 5冲突（@danshipper）

> 来源：以上各链接

---

## 5. YouTube Top视频

| 视频标题 | 链接 | 核心内容 |
|----------|------|----------|
| **"I hate Opus 5. It's the best model, anyway."** (claire vo) | [YouTube](https://www.youtube.com/watch?v=dfre9hN0HCs) | 盲测排名第一但使用体验有摩擦；Opus 5的"neurotic personality"；最终使用建议 |
| **"Opus 5: No-Hype Full Review & Testing"** | [YouTube](https://www.youtube.com/watch?v=z_7J_iKuSzU) | 无炒作的完整评测和实际测试 |
| **"We Tested Claude Opus 5. It's Frustrating with Flashes of Brilliance."** (Every/Dan Shipper团队) | [YouTube](https://www.youtube.com/watch?v=tqF8Ffv7tDs) | 一周深度测试coding和知识工作，分析痛点和亮点 |
| **"I Tested Opus 5 vs. Fable 5. What You Need to Know."** | [YouTube](https://www.youtube.com/watch?v=2J3uX8iRNng) | 直接对比两模型在真实工作流中的表现 |
| **"I Tested Opus 5 vs Fable 5 on 3 Brutal Builds"** | [YouTube](https://www.youtube.com/watch?v=TnfcPbmP-U8) | 三个高难度项目的头对头对比 |
| **"Anthropic Just Revealed How to Prompt Opus 5"** | [YouTube](https://www.youtube.com/watch?v=Z8CtXdQExek) | 解读Anthropic官方prompting指南 |
| **"Claude Opus 5 in 8 Minutes"** | [YouTube](https://www.youtube.com/watch?v=zClso50g9aM) | 8分钟快速了解Opus 5 |
| **"Claude Opus 5 is INSANE!"** | [YouTube](https://www.youtube.com/watch?v=9fCAjISsKCo) | 首日印象与能力展示 |
| **"What did Anthropic do?! (Opus 5)"** | [YouTube](https://www.youtube.com/watch?v=tHQ34j8_toI) | 深度分析Anthropic做了什么以及为什么 |
| **"The end of 'walls of rules' in Claude Opus 5"** (YouTube Short) | [YouTube](https://www.youtube.com/shorts/sJDh9d01oZs) | 解释Anthropic删除80%系统提示的意义 |
| **"Claude Opus 5 is a freak"** | [YouTube](https://www.youtube.com/watch?v=RCsBJz4W4bA) | 全面评测和测试 |

> 注：以上视频均在Opus 5发布后5天内发布（2026年7月24-29日）

---

## 6. Web博客/文档Top文章

### 官方文档（必读）

| 文章 | 链接 | 核心内容 |
|------|------|----------|
| **Introducing Claude Opus 5** (Anthropic官方) | [链接](https://www.anthropic.com/news/claude-opus-5) | 完整发布公告、benchmark数据、客户评价 |
| **Prompting Claude Opus 5** (官方文档) | [链接](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5) | **最重要的使用指南**：8个行为变化和对应策略 |
| **What's new in Claude Opus 5** (官方文档) | [链接](https://platform.claude.com/docs/en/about-claude/models/whats-new-opus-5) | API变更和能力概述 |
| **Opus 5 System Card** (PDF) | [链接](https://www-cdn.anthropic.com/c5fbac3f0b1280a933ebd26d3cb8bb9f5bdeaf48/Claude%20Opus%205%20System%20Card.pdf) | 40页系统卡，包含安全、对齐、能力评估细节 |

### 第三方优质文章

| 文章 | 链接 | 核心内容 |
|------|------|----------|
| **Opus 5 in Claude Code: 8 tips from Anthropic** (wmedia.es) | [链接](https://wmedia.es/en/tips/claude-code-opus-5-prompting-tips) | 将官方指南翻译成Claude Code中的具体操作 |
| **Context Engineering for Claude 5 Models** (Thariq/Anthropic) | [链接](https://x.com/trq212/status/2080710971228918066) | 删除80%系统提示的6个关键转变 |
| **Claude Opus 5 review: brilliant but annoying** (Lenny's Newsletter) | [链接](https://www.lennysnewsletter.com/p/claude-opus-5-review-this-model-is) | 产品经理视角的深度评测 |
| **Opus 5: The System Card** (Zvi Mowshowitz) | [链接](https://thezvi.substack.com/p/claude-opus-5-the-system-card) | 系统卡的深度分析 |
| **Opus 5 Benchmarks Explained** (Vellum) | [链接](https://www.vellum.ai/blog/claude-opus-5-benchmarks-explained) | 所有benchmark的详细解读 |
| **Opus 5 vs Fable 5 Comparison** (Composio) | [链接](https://composio.dev/content/opus-vs-fable) | 编码和工具调用的详细对比 |
| **AI Model Routing in 2026** (MindStudio) | [链接](https://www.mindstudio.ai/blog/ai-model-routing-fable-5-opus-sonnet-haiku) | 模型路由决策框架 |
| **Claude Opus 5 Is Most Efficient at Medium Effort** (SitePoint) | [链接](https://www.sitepoint.com/claude-opus-5-medium-effort-frontiercode-benchmark/) | Medium effort为何反而更好 |

---

## 7. 在Claude Code中使用Opus 5的Best Practice

### 7.1 模型切换

```bash
# 在Claude Code中切换到Opus 5
/model opus

# 或指定完整模型名
/model claude-opus-5

# API调用时使用
claude-opus-5
```

Opus 5在Claude Code v2.1.219+中默认可用。如果你在Max计划上，它已经是默认模型。

### 7.2 Effort级别策略（最重要的成本控制杆）

这是与Opus 4.8**最大的行为差异**。

| Effort级别 | 何时使用 | 典型场景 |
|------------|----------|----------|
| **low** | 简单任务、快速迭代 | 小bug修复、格式调整、简单问答 |
| **medium** | 日常开发的最佳平衡点 | 常规功能开发、代码审查 |
| **high**（默认） | 大多数复杂任务 | 多文件重构、架构决策 |
| **xhigh** | 最难的任务 | 全功能端到端开发、深度debug |

**关键发现：** Anthropic工程师Jeremy发现，Opus 5在medium effort下的FrontierCode得分反而**高于**higher effort。这意味着过度思考反而有害。

### 7.3 CLAUDE.md优化（必须做的8件事）

基于Anthropic官方指南和Thariq的context engineering文章：

**要删除的4项：**

1. **删除"最后验证步骤"指令** —— Opus 5自己会验证，额外指令导致过度验证和浪费token
2. **删除"double-check"/"re-verify"指令** —— 同上原因
3. **删除"只报告高严重性问题"的代码审查指令** —— Opus 5会字面遵守，报告更少。改为要求报告所有问题，单独过滤
4. **删除MAX_THINKING_TOKENS=0设置** —— 在Opus 5上，xhigh + thinking disabled直接报400错误

**要添加的2项：**

5. **添加subagent委托上限** ——
```markdown
Delegate to a subagent only for large tasks that are genuinely independent and
parallelizable. Don't delegate work you can finish in a handful of tool calls,
and don't use subagents to verify your own work.
```

6. **添加简洁性要求** ——
```markdown
Keep responses focused, brief, and concise. Keep disclaimers and caveats short,
and spend most of the response on the main answer.
```

**要调整的2项：**

7. **完整规格一次给出** —— 不要分步喂指令，让Opus 5拿到完整任务自己跑
8. **Effort起点从xhigh改为high/medium** —— 检查settings.json和环境变量中的旧设置

### 7.4 Prompting核心原则

Boris Cherny（Claude Code创建者）的核心观点：

> "Opus 5用一天完成过去你团队一个月的工作。大多数人会继续用错它。"

**6个关键转变（Thariq）：**
1. 规则 -> 判断（Rules become judgment）
2. 示例 -> 界面设计（Examples become interface design）
3. 前置上下文 -> 通过skills渐进披露（Upfront context -> progressive disclosure）
4. 系统提示和工具描述中的重复指令 -> 合并到工具定义中
5. 手动CLAUDE.md记忆 -> 自动记忆
6. 简单markdown规格 -> 更丰富的引用（代码、测试套件、rubrics）

### 7.5 Fast模式使用建议

- Fast模式速度提升~2.5倍，价格2倍
- **必须在对话开始时就启用** —— 中途启用会对整个对话上下文收取未缓存的输入token价格
- 适合需要快速迭代的场景

### 7.6 Context管理建议

- 把不变的内容（代码库、风格指南）放在**最前面**
- 把易变内容（当前问题、最新diff）放在**最后面**
- 这样做可以最大化prompt cache命中率，显著节约$5/M的输入成本

> 来源：[官方Prompting Guide](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5) · [wmedia 8 tips](https://wmedia.es/en/tips/claude-code-opus-5-prompting-tips) · [Thariq Context Engineering](https://x.com/trq212/status/2080710971228918066)

---

## 8. 成本优化策略

### 8.1 Effort级别是最大的成本控制杆

Opus 5的性价比关键在于effort管理：

- **默认从medium开始**，不是xhigh
- low/medium的质量在大多数任务上足够好
- 只在真正需要深度推理时才升级到xhigh
- `thinking at low` 比 `thinking disabled` 在同等成本下表现更好

### 8.2 Prompt Caching

- Opus 5支持最高**90%的prompt缓存折扣**
- 策略：把系统提示和CLAUDE.md等不变内容放在prompt最前面
- 每次对话的变化部分放在最后

### 8.3 Batch Processing

- 通过Message Batches API可获得**50%折扣**
- 适合非实时任务：代码审查、文档生成、批量分析

### 8.4 避免过度验证（免费省钱）

- 删除CLAUDE.md中的verification指令 = 直接减少无用token消耗
- Dan Shipper的Every团队经验：删除旧skills后，Opus 5变得"戏剧性地更好"

### 8.5 控制Subagent委托

- Opus 5比Opus 4.8更容易主动委托subagent
- 不加限制的委托会成倍增加成本
- 在CLAUDE.md中明确限制委托条件

### 8.6 模型路由策略

- 简单任务 -> Sonnet 5（$2-3/M）
- 日常开发 -> Opus 5 medium effort
- 最难任务 -> Opus 5 xhigh 或 Fable 5
- 批量处理 -> Opus 5 Batch API

### 8.7 实际成本参考

| 场景 | 模型+设置 | 每任务成本 |
|------|----------|-----------|
| CursorBench Max effort | Opus 5 | ~$8.23 |
| CursorBench Max effort | Fable 5 | ~$17.32 |
| CursorBench Extra High | Opus 5 | ~$4（实际表现接近Fable 5 Extra High） |
| AA-Briefcase Max effort | Opus 5 | ~$17.79 |
| AA-Briefcase Max effort | Fable 5 | ~$22.30 |

> Opus 5的效率增益（更少重试、更少token、更低延迟）意味着在实践中它可能比标价更低的模型还便宜。

> 来源：[BridgeMind on X](https://x.com/bridgemindai/status/2080707321806868774) · [Artificial Analysis](https://x.com/ArtificialAnlys/status/2080734447717298483) · [Anthropic官方](https://www.anthropic.com/news/claude-opus-5)

---

## 9. 对你的个性化建议（Growth Expert/PM转型AI Builder）

作为一个非工程师背景、用Claude Code做LoreAI (loreai.dev) 的AI Builder，以下是5条最应该用Opus 5做的事：

### 1. 用Opus 5做产品架构和全功能开发

**为什么：** Opus 5最擅长的就是"拿到完整任务规格自己跑"。作为PM，你最大的优势是写清楚产品需求（PRD）。把完整的功能需求一次性交给Opus 5，让它从设计到实现到测试一站式完成。这正好是你擅长写需求+它擅长执行的完美组合。

**怎么做：** 在提示中用一段完整的需求描述，包括用户故事、验收标准、技术约束。然后让Opus 5自己规划和执行。不要分步指导它怎么写代码。

### 2. 用Opus 5做代码审查和质量保障

**为什么：** 作为非工程师，代码审查是你最需要AI帮助的环节。Opus 5的代码审查精度是所有模型中最高的（39.3%），而且在low effort下准确度就够用。这意味着你可以频繁、低成本地审查代码质量。

**怎么做：** 在Claude Code中用 `/code-review` 功能。不要在提示中加"只报告高严重性问题"——让它报告所有发现，你再自己决定处理哪些。

### 3. 用Opus 5做LoreAI的长程Agent任务

**为什么：** LoreAI作为一个AI产品，很可能涉及复杂的多步骤工作流。Opus 5在长程agent任务上的表现超过所有其他模型，包括Fable 5。它的自我验证能力意味着你可以把更多的工作委托给它。

**怎么做：** 设置Claude Code的auto mode，让Opus 5自主运行。用medium effort作为默认值控制成本。只在涉及支付、数据迁移等高风险操作时暂停手动确认。

### 4. 用Opus 5做产品文档和spreadsheet工作

**为什么：** Opus 5生成复杂spreadsheet（含非平凡公式）和结构化slide deck的能力是Opus家族中最强的。作为Growth Expert/PM，你的大量工作涉及数据分析、报告和演示。

**怎么做：** 直接让Opus 5生成完整的分析spreadsheet或产品deck。提供你期望的模板或风格。注意Opus 5写的文件会比预期长——明确告诉它你需要的长度。

### 5. 用Opus 5的medium effort作为默认节奏

**为什么：** 成本控制对独立Builder至关重要。Opus 5在medium effort下的表现出人意料地好——Anthropic自己的工程师发现medium effort的FrontierCode得分甚至高于higher effort。这意味着你大部分时间不需要为最高质量付费。

**怎么做：**
- 日常开发：medium effort
- 代码审查：low effort
- 复杂功能/重构：high effort
- 最关键的架构决策：xhigh effort

### 额外建议：立刻做的3件事

1. **清理你的CLAUDE.md** —— 用以下命令检查是否有需要删除的旧指令：
```bash
grep -rns -i "verify\|double-check\|re-check" \
  ~/.claude/CLAUDE.md ./CLAUDE.md ./.claude/agents/ ./.claude/skills/
```

2. **删除旧的skills和workflows** —— 如果你从Opus 4.8时代带过来的skills不工作了，不要修补，直接删除重建。Dan Shipper的经验表明这是解决Opus 5"不听话"的关键。

3. **在CLAUDE.md中添加这两段**：
```markdown
Keep responses focused, brief, and concise. Keep disclaimers and caveats short,
and spend most of the response on the main answer.

Delegate to a subagent only for large tasks that are genuinely independent and
parallelizable. Don't delegate work you can finish in a handful of tool calls.
```

---

## 附录：关键数据速查

### Benchmark成绩

| 评估 | Opus 5 | Fable 5 | Opus 4.8 | GPT-5.6 Sol |
|------|--------|---------|----------|-------------|
| Frontier-Bench v0.1 | **43.3%** | 33.7% | ~21% | - |
| ARC-AGI 3 | **30.2%** | - | - | 7.8% |
| OSWorld 2.0 | **70.6%** | 更高成本 | - | - |
| BrowseComp | **90.8%** | - | - | - |
| AutomationBench | **26.0%** | - | - | - |
| Intelligence Index (AA) | **61** | 60 | - | 59 |

### 关键人物

| 人物 | 身份 | 关注价值 |
|------|------|----------|
| **Boris Cherny** (@bcherny) | Claude Code创建者 | Claude Code使用哲学、系统设计 |
| **Thariq Shihipar** (@trq212) | Anthropic工程师 | Context engineering、系统提示设计 |
| **Dan Shipper** (@danshipper) | Every创始人 | 实战工作流、踩坑经验 |
| **Jason Zook** (@jasondoesstuff) | 独立开发者 | 模型选择实战建议 |
| **claire vo** (@clairevo) | ChatPRD创始人/PM | PM视角的模型评测 |
| **Mike Krieger** (@mikeyk) | Instagram联合创始人 | 技术领袖的使用心得 |

---

> 本报告基于2026年7月29日的公开信息编写。Opus 5发布仅5天，社区实践经验仍在快速积累中。建议持续关注上述关键人物的后续分享。
