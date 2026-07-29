# Claude Opus 5 Best Practice 深度调研报告

> 调研日期：2026-07-29
> 调研范围：Anthropic 官方公告与文档、Claude Code release、System Card、独立评测、
> practitioner 文章、X 原帖
> 面向读者：会用 Claude Code / API、但不是资深系统工程师的 AI builder
> 截止时间：2026-07-29；这是发布五天后的快照

## Executive Summary

**Claude Opus 5 是面向复杂日常工作的 expert model，不是所有任务的自动最优解。**
Anthropic 将它定位为“接近 Fable 5 的前沿智能、价格减半”，同时强调 everyday use。
这意味着：把它作为困难 coding、长程 agent 和高判断密度工作的主力候选是合理的；是否替代
Sonnet 5 或升级到 Fable 5，仍应由你自己的任务评测决定，而不是由一张公开 benchmark 决定。
[Anthropic 发布公告](https://www.anthropic.com/news/claude-opus-5)

截至本次调研，最可靠的使用策略不是“默认 medium”，而是：

1. 以官方默认 `high` 做 control，在代表性任务上跑 effort sweep；
2. 给完整任务规格，同时明确 scope、输出长度、进度汇报和 subagent 上限；
3. 删除重复要求模型“再检查一遍”的提示脚手架，但保留 tests、验收标准和高风险人审；
4. 固定同一缓存会话的 effort 与 speed，分别用 prompt caching、Batch、Fast 解决不同成本问题；
5. 用可逆的 AB test 清理旧 prompts / skills，不要整套删除重建。

黄金案例在结构、可扫读性和具体操作上是很好的标杆，但其中“2026-07-24 是周四”、
“CodeRabbit 39.3% 证明 low effort 足够”、“默认 medium”、“旧 Skills 应直接删除”以及
“Auto mode 仅在支付/迁移时暂停”等说法没有被原始证据支持。后文给出可执行的修正版。

## 先改这 7 件事

| 表面 | 什么时候做 | 具体动作 | 边界 |
|---|---|---|---|
| Claude Code / API | 首次迁移 | 先用 `high` 跑一组真实任务作为 control | 不把单项 benchmark 当默认值 |
| Prompt | 多文件、重构、E2E | 一次给完整目标、约束、验收标准 | 窄任务要显式禁止 scope creep |
| 输出 | 回复或 artifact 太长 | 单独规定简洁度、更新频率、文件长度 | effort 不可靠地控制可见字数 |
| 验证 | 旧 prompt 有多次 re-check | 删除重复“double-check”指令 | 保留测试、静态检查、领域 Gate |
| Delegation | agent 数量失控 | 只对真正独立的大 lane 开 subagent，并设硬上限 | 不让 subagent 做自我复核 |
| 成本 | 大量重复前缀 | 静态内容放前，变化内容放后，启用缓存 | 同会话改 effort / speed 会 cache miss |
| 高风险动作 | 生产、付费、删改数据 | canary、rollback、权限边界、人工确认 | Auto mode 不是安全保证 |

## 1. Opus 5 到底是什么

Claude Opus 5 于 **2026-07-24（周五）**发布。API model ID 是
`claude-opus-5`；Anthropic 把它描述为接近 Fable 5 前沿智能、但价格只有一半，并将其定位成
可每天使用的复杂任务模型。[发布公告](https://www.anthropic.com/news/claude-opus-5)

### 当前技术契约

| 项目 | 截止 2026-07-29 的事实 | 使用时要记住 |
|---|---|---|
| 上下文 | 1M tokens | 默认就是 1M，没有另一个小窗口变体 |
| 同步最大输出 | 128k tokens | thinking 与可见输出共享 `max_tokens` 上限 |
| Batch 最大输出 | 300k tokens | 需 Batches API、beta header，且有平台与数据保留限制 |
| 标准价格 | $5 / MTok input，$25 / MTok output | 真实成本还受新 tokenizer、重试和 tool calls 影响 |
| 默认 effort | `high` | 五档：`low / medium / high / xhigh / max` |
| Thinking | adaptive、默认开启 | 关闭只允许 high 及以下；xhigh/max 会返回 400 |
| Knowledge cutoff | May 2026 | 当前事实仍需外部检索 |

以上规格来自
[Models overview](https://platform.claude.com/docs/en/about-claude/models/overview)、
[What’s new](https://platform.claude.com/docs/en/about-claude/models/whats-new-opus-5) 和
[Batch processing](https://platform.claude.com/docs/en/build-with-claude/batch-processing)。

### 与 Sonnet 5、Fable 5 怎么选

| 决策信号 | Sonnet 5 | Opus 5 | Fable 5 |
|---|---|---|---|
| 主要目标 | 高吞吐、成本敏感 | 复杂任务的速度/智能平衡 | 已知极难任务的最高能力上限 |
| 先试场景 | 高频轻中度任务 | 多文件 coding、长程 agent、复杂判断 | Opus 在真实 eval 上仍不过关 |
| 不该仅凭什么选择 | “更便宜所以总成本最低” | “是 Opus 所以所有任务更好” | “更强所以每个任务都值得” |

这是决策框架，不是厂商规格。官方也建议以 custom evals 选择模型；同一个领域内，任务难度、
重试率和一次成功率往往比“金融/科学/写作”这类标签更有区分力。
[官方模型选择说明](https://claude.com/blog/claude-models-explained-choosing-the-best-model-for-your-use-case)

## 2. 核心机制：模型、effort、thinking 不是一回事

可以把模型理解成“能力上限”，effort 理解成“这次允许它花多少功夫”。提高 effort 会影响
推理、工具使用、检查和 token 消耗，但**不会稳定地让最终回答更短或更长**。可见输出的长度和
进度播报应该直接写进 prompt。

官方建议从默认 `high` 开始，再按照自己的 eval 上调或下调；困难 coding / agentic task 可试
`xhigh`，`max` 只在不限制 token 开销确实有价值时使用。如果 low 或 medium 在你的任务集上
保持质量，就大胆降档。[Effort 文档](https://platform.claude.com/docs/en/build-with-claude/effort)

一项 FrontierCode 结果在 medium 达峰，只能证明某个 benchmark 的 effort 曲线可能非单调，
不能证明“medium 是所有日常任务的最佳默认”。正确做法是跑一轮小型 sweep：

| 记录项 | 为什么必须测 |
|---|---|
| pass rate / acceptance rate | 判断质量是否真的达标 |
| 重试次数 | 低价模型或低 effort 可能因返工更贵 |
| tool calls / elapsed time | 识别探索过度或提前停止 |
| input / output / thinking tokens | 计算真实成本 |
| precision / recall / nitpicks | code review 不能只看一个精度数字 |

## 3. Prompt 与工作流的变化

### 3.1 完整规格 upfront，但不要写成规则迷宫

对多文件修改、大型重构和 E2E，先给完整的目标、上下文、约束和验收标准，再让模型执行。
对窄任务明确文件范围和“不要顺手重构”的边界。Opus 5 更容易主动扩展 scope，也更容易主动
spawn subagents；这两件事都应显式校准。
[Opus 5 Prompting Guide](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5)

一个可复用的任务契约：

```text
Goal: <最终结果>
In scope: <允许改动的文件/系统>
Out of scope: <不要顺手做的事>
Acceptance: <测试、检查、人工 Gate>
Progress: <何时汇报；平时保持简短>
Delegation: <只对独立 lane 使用，最多 N 个>
Deliverable: <文件、格式、长度>
```

### 3.2 删除冗余验证提示，不等于删除质量保障

官方认为 Opus 5 已有更强的 self-verification，因此旧 prompt 中反复出现的
“final verification”“double-check”“再用 subagent 复核”可能浪费 token，甚至制造重复劳动。
应删除的是**提示层的重复自我复核**。

以下东西不要因此删除：

- 可执行 tests、lint、typecheck 和验收脚本；
- 生产变更的 canary、rollback 与权限限制；
- 医疗、法律、金融等高风险结论的人审；
- 数据删除、迁移、付费、对外发布等不可逆 Gate。

System Card 同时指出：Opus 5 总体更准确，但事实性陈述的幻觉率略高于 Opus 4.8。更强的
agentic 能力不是免检通行证。
[Opus 5 System Card](https://www.anthropic.com/claude-opus-5-system-card)

### 3.3 逐项审计 CLAUDE.md、Skills 与 plugins

Anthropic 为 5 系列模型删去了 Claude Code system prompt 的 80% 以上，并报告其内部 coding
eval 没有可测质量损失。其建议方向是从密集规则转向 judgment、从重复背景转向 progressive
disclosure、从记忆堆积转向按需加载。
[Context engineering 文章](https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models)

但这不支持“一次删除全部旧 Skills”。官方 Prompting Guide 明确说 Opus 5 对现有 Opus 4.8
prompts 通常可直接工作。安全的迁移方式是：

1. 冻结一组代表任务和验收结果；
2. 删除一类已知冗余：重复验证、过度 verbosity、无限 delegation；
3. 对清理前后跑同一组任务；
4. 只有在通过率不降且 token / latency 改善时才保留清理；
5. 保留仓库 gotchas、接口契约、真实 tests 和安全规则。

## 4. Claude Code 的具体落地

Claude Code `v2.1.219` 加入 Opus 5，并将它设为默认 **Opus model**；这不等于每个账户的
整体默认模型。以 `/model` 里实际可见的选项为准。
[Claude Code v2.1.219 release](https://github.com/anthropics/claude-code/releases/tag/v2.1.219)

建议迁移顺序：

1. 升级并确认版本至少包含 `v2.1.219`；
2. 用 `/model` 选择账户可用的 Opus 5；
3. 用 `/effort` 从 `high` control 开始；
4. 记录真实任务的成功率、重试、token、tool calls 和耗时；
5. 只有在低档保持质量时下调 effort；
6. 对 nested subagents 失控的工作流，除 prompt 上限外，评估
   `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH=1`。

`/fast` 只改变速度，不改变模型权重或智能。Claude Code 最好在会话开始启用，因为中途切换会让
整个上下文以 Fast 的未缓存输入价重新计费；它不是语法上的“只能开场启用”。
[Claude Code Fast mode](https://code.claude.com/docs/en/fast-mode)

## 5. API：把三个成本工具分开用

| 工具 | 优化目标 | Opus 5 价格 | 关键限制 |
|---|---|---|---|
| Prompt caching | 重复前缀成本 | hit $0.50/MTok；5m write $6.25；1h write $10 | 静态前缀放前；effort/speed 变化会失效 |
| Message Batches | 非实时吞吐成本 | $2.50 input / $12.50 output | 50% 折扣；不支持 Fast；300k 需 beta |
| Fast mode | output token 生成速度 | $10 input / $50 output | research preview；最高 2.5x OTPS；非 TTFT |

来源：
[Pricing](https://platform.claude.com/docs/en/about-claude/pricing)、
[Prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)、
[Batch processing](https://platform.claude.com/docs/en/build-with-claude/batch-processing)、
[Fast mode](https://platform.claude.com/docs/en/build-with-claude/fast-mode)。

Prompt cache 的“最高节省 90%”只指 cache hit 相对标准输入价；首次写入反而有 1.25x 或 2x
乘数。Fast 的“最高 2.5x”是 output tokens per second，不是 time-to-first-token 或整个任务
时长。Batch 的 300k 输出还要求 `output-300k-2026-03-24` beta header，并非同步 API 的默认
上限。

## 6. 社区讨论：首周没有一个统一结论

社区证据更适合回答“哪里值得自己测试”，不适合代替官方契约或泛化成所有用户的默认值。

### “先拆旧脚手架”派

Every 团队首周报告 Opus 5 会与他们为旧模型构建的 skills / plugins 发生冲突，后续甚至以
“Sometimes You Have to Delete Everything”为题描述重构经历。这是高信号 practitioner
experience，但仍是单一团队、特定历史配置的案例，不能推出所有用户都应清空配置。
[Every 首评](https://every.to/vibe-check/opus-5)、
[Every 后续](https://every.to/context-window/sometimes-you-have-to-delete-everything)

### “很强但很烦”派

Claire Vo 用七个模型做个人盲测，把 Opus 5 排到第一，尤其肯定 front-end design，同时批评
其互动感和个性。这个结果说明模型可能在作品质量上领先、在协作体验上仍需 prompt 校准；样本
规模和评分设计使它只能作为 practitioner evidence。
[ChatPRD 评测](https://www.chatprd.ai/how-i-ai/my-surprising-verdict-on-claude-opus-5)

### Code review 的关键反证

CodeRabbit 在约 100 个 verified issue patterns 上评测三种 effort。Opus 5 `xhigh` 的
actionable-comment precision 是 39.3%，高于其 production baseline 35.2%；但 known-issue
coverage 是 55.2% 对 61.1%，full-stream precision 是 28.6% 对 32.8%，nitpicks 是 92 对
23。CodeRabbit 的结论是：它适合作为 precision-oriented second reviewer，不适合作为唯一
safety net。[CodeRabbit 完整评测](https://www.coderabbit.ai/blog/opus-5-model-review)

这组数据直接否定两个常见误读：39.3% 不是 `low` effort，也不能单独证明它是最佳通用代码
审查器。Code review 必须同时测 precision、recall / coverage 和噪声。

### X：代表性原帖，而不是“平台 Top”

本轮通过 X 官方 oEmbed 直接观察原帖正文，但 oEmbed 不返回互动指标。因此以下帖子只能说明
发布首周有哪些高信号观点，不能按“高互动 Top-N”排名：

- [Thariq Shihipar](https://x.com/trq212/status/2080710971228918066) 是 Anthropic 工程师，
  其“删除约 80% system prompt”的帖子应回到
  [完整官方文章](https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models)
  理解，不能把下游转述算作独立确认。
- [Dan Shipper](https://x.com/danshipper/status/2080700057892815114) 报告 Opus 5 会争辩、
  提前停止、与既有 skills/plugins 配合不佳；X、Every 文章和 Every 视频属于同一证据链。
- [Claire Vo](https://x.com/clairevo/status/2080703735878336983) 的核心分歧是“使用体验讨厌，
  盲测产出第一”；这是一项个人品味权重很高的六类任务测试，不是通用排行榜。
- [Ethan Mollick](https://x.com/emollick/status/2080709278441033746) 提供了黄金案例遗漏的反例：
  短任务可匹配或超过 Fable，长任务却可能不够 ambitious、交付不完整。
- [Mike Krieger](https://x.com/mikeyk/status/2080702940445397167) 称它很快成为日常主力，
  但他当时是 Anthropic Labs 负责人、前 CPO，应归类为机构内部采用，不是独立用户证据。

### YouTube：传播量与证据质量要分开

对黄金案例列出的 11 个视频，本轮在 2026-07-29 16:42 +08:00 读取了 YouTube 页面指标。
其中观看量最高的是
[AI Search 的视频](https://www.youtube.com/watch?v=RCsBJz4W4bA)（398,935 views），
而方法最可复核的是
[Pat Simmons 的对比](https://www.youtube.com/watch?v=z_7J_iKuSzU)（65,924 views）：
它公开同 prompt、成品、token、成本和时间。两者分别是传播信号和研究质量信号，不应混成
一个 “Top”。

Pat 的五个构建合计成本为 Opus 5 $111.84、Fable 5 $156.04、Opus 4.8 $120.86；在这个
特定 harness 中 Opus 5 比 Fable 低约 28%，而不是标准 token 牌价所暗示的固定 50%。
这正说明 per-task cost 必须绑定任务、effort、工具调用和重试。
[配套方法与结果](https://www.aiformortals.co/blog/opus-5-vs-opus-4-8-vs-fable-5)

## 7. 对 AI builder 的实际价值

### 如果你是独立 builder

先把 Opus 5 用在“失败一次代价高”的复杂任务：跨文件重构、难 debug、长程 agent、带工具的
研究。轻量改字、批量转换和高吞吐任务先与 Sonnet 5 对比总任务成本。

### 如果你维护长期工作流

不要凭一次惊艳 demo 重写整个系统。保留 deterministic driver、tests、数据 Gate 和 rollback；
只把模型层的冗余提示、上下文堆积和无限 delegation 拿出来逐项 AB。

### 如果你处理高风险领域

不要从 vendor benchmark 推出医疗、法律或金融的生产安全性。用领域数据、权限隔离、可追溯
来源、人工复核和可逆部署决定是否上线。

## 8. 一套两小时可完成的校准实验

1. 选 8–12 个真实任务：简单修改、复杂 coding、debug、review、研究各至少两个。
2. 固定模型、prompt、工具和验收标准，以 `high` 建 control。
3. 对成本敏感任务跑 `medium` / `low`；对失败任务跑 `xhigh`，必要时再跑 `max`。
4. 每次记录 pass、重试、token、tool calls、耗时；review 另记 precision、coverage、nitpicks。
5. 清理一种旧 scaffold 后重跑，不要同时删除所有 rules / skills。
6. 选出按任务类型的路由，而不是一个全局默认。
7. 先在非生产 canary 上使用；生产、付费、删除、迁移和对外发布保留人工 Gate。

### 什么证据会改变本报告的建议

- 你的代表任务显示 `medium` 在质量不降时稳定降低总成本：可把该类任务默认降到 medium。
- Opus 5 在固定 harness 下仍无法通过，而 Fable 5 明显提高一次成功率：升级该类任务。
- 清理某项 skill 后通过率下降：恢复它；“更少上下文”不是目的，任务成功才是。
- Fast 的端到端时延收益不足以抵消 2x 价格：不用 Fast，即使 output tokens/sec 更快。
- 后续官方默认值、价格、beta 或 Claude Code 命令变化：以新文档和 `/model` 实际状态为准。

## 关键资源索引

### Start here

- [Anthropic：Claude Opus 5 发布公告](https://www.anthropic.com/news/claude-opus-5)
- [Opus 5 Prompting Guide](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5)
- [Effort 文档](https://platform.claude.com/docs/en/build-with-claude/effort)

### Primary and official sources

- [Models overview](https://platform.claude.com/docs/en/about-claude/models/overview)
- [What’s new in Opus 5](https://platform.claude.com/docs/en/about-claude/models/whats-new-opus-5)
- [Pricing](https://platform.claude.com/docs/en/about-claude/pricing)
- [Opus 5 System Card](https://www.anthropic.com/claude-opus-5-system-card)
- [Claude Code v2.1.219](https://github.com/anthropics/claude-code/releases/tag/v2.1.219)

### Independent practice and counter-evidence

- [CodeRabbit：Opus 5 model review](https://www.coderabbit.ai/blog/opus-5-model-review)
- [Claire Vo 的个人盲测](https://www.chatprd.ai/how-i-ai/my-surprising-verdict-on-claude-opus-5)
- [Artificial Analysis：Max vs Medium](https://artificialanalysis.ai/models/comparisons/claude-opus-5-vs-claude-opus-5-medium)
