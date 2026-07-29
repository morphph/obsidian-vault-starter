# Claude Opus 5 Best Practice 深度调研报告

> 调研日期：2026-07-29
> 面向读者：Claude Code / API 用户与 AI builder
> 证据范围：官方技术文档、System Card、Claude Code release、独立评测、X 原帖与 YouTube
> 时效边界：发布五天后的快照；价格、beta、provider 和账户权限需在执行时重查

## Executive Summary

**把 Opus 5 当成复杂日常工作的 expert candidate，而不是新的全局默认。** Anthropic 的精确
定位是：它接近 Fable 5 的前沿智能、价格减半，并为 everyday use 设计；这不等于全面超过
Fable，也不等于比 Sonnet 更适合每个高吞吐任务。
[官方发布](https://www.anthropic.com/news/claude-opus-5)

最稳妥的默认动作只有三个：

1. **从 `high` 建 control。** 官方默认和起始建议都是 high；low/medium/xhigh/max 由自己的
   workload eval 决定，不从一个公开 benchmark 推导全局默认。
2. **减 prompt scaffolding，保留真实 Gate。** 删除重复的“再检查一遍”、冲突规则和无限
   delegation；保留 tests、验收标准、权限、rollback 与高风险人审。
3. **把成本工具按目的分开。** Cache 降重复前缀成本，Batch 降异步吞吐成本，Fast 换取更高
   output-token 速度；三者不是同一个“加速开关”。

如果你现在只有 12 分钟，先执行下面这张表。

## 12 分钟迁移清单

| Surface / scenario | When to use | Action | Evidence | Boundary | Verification |
|---|---|---|---|---|---|
| Claude Code | 想开始试 Opus 5 | 升到含 `v2.1.219` 的版本，在 `/model` 选账户实际可见的 Opus 5 | [release](https://github.com/anthropics/claude-code/releases/tag/v2.1.219) | “default Opus”不是所有账户 overall default | 记录版本与 `/model` 结果 |
| Claude Code / API | 首次跑真实任务 | effort 先设 `high` | [Effort](https://platform.claude.com/docs/en/build-with-claude/effort) | 不把 medium 当通用默认 | 与现有模型跑同一验收任务 |
| Prompt | 多文件、重构、E2E | upfront 给 goal、scope、acceptance、deliverable | [Prompting guide](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5) | 窄任务要写 out-of-scope | 看是否漏项或顺手扩 scope |
| Prompt | 回复和过程太长 | 单独规定 concise、update cadence、artifact length | 同上 | effort 不控制可见字数 | 比较输出长度与信息完整度 |
| Skills / CLAUDE.md | 怀疑旧规则冲突 | 一次只删一种冗余规则，前后 AB | [Context engineering](https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models) | 不批量删除 tests / Gates | 同任务 pass、token、重试均不退化 |
| Subagents | agent 数量或成本失控 | 只对独立大 lane 使用，设数量/深度上限 | [Prompting guide](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5) | 不让 subagent 做自我复核 | 记录 spawn 数、总 token、墙钟时间 |
| 生产/付费/删数据 | 后果不可逆 | canary + rollback + 最小权限 + 人工 Gate | [System Card](https://www.anthropic.com/claude-opus-5-system-card) | Auto mode 不是安全证明 | 演练 rollback，再开放有限权限 |

## 1. 先把技术契约说准确

Claude Opus 5 于 **2026-07-24（周五）**发布，API ID 为 `claude-opus-5`。

| 契约 | 当前值 | Surface 与前提 | 容易误读的地方 |
|---|---|---|---|
| Context | 1M | Claude API model | 默认即 1M |
| 同步输出 | 128k | Messages API | thinking 与可见输出共享 `max_tokens` |
| 批量输出 | 300k | Message Batches + `output-300k-2026-03-24` beta | 不是同步默认；有 provider、ZDR、保留期限制 |
| 标准价 | $5 input / $25 output per MTok | 标准速度 | 牌价减半不保证 per-task 成本减半 |
| Effort | low / medium / high / xhigh / max | API 与 Claude Code；默认 high | thinking disabled 时 xhigh/max 返回 400 |
| Fast | $10 / $50；最高 2.5x OTPS | API research preview；Claude Code 受账户配置影响 | 不是 TTFT 或整任务 2.5x |
| Cache hit | $0.50 input per MTok | 命中已写入前缀 | “省 90%”仅指读取命中；写入有乘数 |
| Batch | $2.50 / $12.50 | 异步 Batches | 不支持 Fast，不等于实时接口折扣 |

来源：
[Models overview](https://platform.claude.com/docs/en/about-claude/models/overview)、
[What’s new](https://platform.claude.com/docs/en/about-claude/models/whats-new-opus-5)、
[Pricing](https://platform.claude.com/docs/en/about-claude/pricing)、
[Batch](https://platform.claude.com/docs/en/build-with-claude/batch-processing)、
[Fast](https://platform.claude.com/docs/en/build-with-claude/fast-mode)。

### 为什么技术契约比发布摘要重要

“300k output”“2.5x faster”“90% cache savings”都是真的，但只在各自限定的 surface 和
计价阶段成立。把 beta Batch 上限写进同步 API，或把 output tokens/sec 写成端到端延迟，会让
看似精确的建议在生产中直接失效。

## 2. Model routing：先问任务，不先问领域

| 任务信号 | 先试 | Confidence | 什么时候不要用 |
|---|---|---:|---|
| 高频、轻中度、吞吐敏感 | Sonnet 5 | medium | 重试或人工返工使总成本上升 |
| 多文件 coding、难 debug、复杂工具链 | Opus 5 high | high | 你的 control 显示 Sonnet 同样过关 |
| 长程、战略、模糊、边界情况很多 | Opus 5 xhigh 与 Fable 5 对照 | medium | 不要假设 Opus 长程必胜；社区有反例 |
| 非实时大批量任务 | Opus 5 Batch | high | 需要实时、ZDR 或 Fast |
| 交付时延直接影响价值 | Opus 5 Fast | medium | 端到端收益不抵 2x 价格 |
| 医疗、法律、金融决策 | 领域模型/流程 + Opus 候选 | low | 没有领域 eval、来源追踪和人审时不上线 |

“Fable 是最大任务、Opus 是其余任务”是一些实践者的个人路由经验，不是产品契约。正确做法是
在同一 harness 上比较一次成功率、重试、token、tool calls、latency 和人工返工。
[官方模型选择说明](https://claude.com/blog/claude-models-explained-choosing-the-best-model-for-your-use-case)

## 3. Effort：不要争论默认值，做 sweep

官方建议从默认 `high` 开始，困难 coding / agentic task 可上 `xhigh`，`max` 只在不限制 token
开销确有价值时使用；如果自己的 eval 证明质量不降，就大量使用 low/medium。
[Effort 文档](https://platform.claude.com/docs/en/build-with-claude/effort)

一项 FrontierCode 在 medium 达峰，只能说明 effort 曲线可能非单调。Artificial Analysis 的
聚合结果又显示 max intelligence index 高于 medium、但 time-to-first-token 更慢。两者共同
支持的是“按 workload sweep”，不是“高 effort 普遍有害”。
[Max vs Medium](https://artificialanalysis.ai/models/comparisons/claude-opus-5-vs-claude-opus-5-medium)

### 两小时 eval 表

选 8–12 个真实任务，每档至少记录：

| 质量 | 成本 | 行为 |
|---|---|---|
| pass / acceptance；review precision + coverage | input/output/thinking tokens；重试成本 | tool calls；elapsed；spawn 数；scope creep |

以 high 为 control。某类任务只有在质量不降、总任务成本下降时才降到 medium/low；失败任务再与
xhigh/Fable 比较。不要在同一个缓存会话里频繁改 effort，因为当前官方文档说这会使缓存前缀
失效。

## 4. Prompt：完整任务契约，轻量上下文

```text
Goal: <最终结果>
In scope: <允许改动>
Out of scope: <禁止顺手扩张>
Acceptance: <tests / rubric / human Gate>
Progress: <何时更新；其余保持简短>
Delegation: <仅独立 lane；最多 N 个>
Deliverable: <格式与长度>
```

Opus 5 对复杂任务更适合 upfront 的完整规格。它也更容易回复过长、扩大 scope 和主动 spawn
subagents，所以要显式限制；这些输出行为不能靠降低 effort 稳定解决。
[Prompting guide](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5)

### 应删除什么

- 重复的 “final verification / double-check / re-verify”；
- 让另一个 subagent 只做模型自我复核；
- 冲突的 verbosity、scope 和 delegation 规则；
- 已被工具接口或按需 skill 覆盖的重复背景。

### 必须保留什么

- 可执行 tests、lint、typecheck、视觉 QA；
- 验收 rubric 与真实业务 Gate；
- 生产 canary、rollback、最小权限；
- 删除、迁移、付款、发布和高风险领域的人审。

Anthropic 报告为 5 系列删去 Claude Code system prompt 80% 以上而内部 coding eval 不降；
这是“rightsize、去冲突、渐进披露”的方向证据，不是“所有人删除 80%”的配额。
[Context engineering](https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models)

## 5. 社区首周：同一模型，三种相反体验

| 观察 | 来源角色 | 能支持什么 | 不能支持什么 |
|---|---|---|---|
| 与旧 skills/plugins 冲突、会提前停止 | [Dan Shipper / Every](https://x.com/danshipper/status/2080700057892815114) | 复杂历史 scaffold 需要 AB | 所有人应清空 Skills |
| 盲测产出第一、直接交互很烦 | [Claire Vo](https://x.com/clairevo/status/2080703735878336983) | 作品质量与协作体验可分离 | 全平台模型排名 |
| 短任务强，长任务不够 ambitious | [Ethan Mollick](https://x.com/emollick/status/2080709278441033746) | “长程全面优于 Fable”的反例 | 所有长任务都更差 |
| 很快成为日常主力 | [Mike Krieger](https://x.com/mikeyk/status/2080702940445397167) | Anthropic 内部采用信号 | 独立用户验证 |

这些 X 原帖通过 first-party oEmbed 观察正文，但互动指标 unavailable，因此只称代表性/高信号，
不称“Top 高互动”。Dan 的 X、Every 文章和 Every 视频是一条 evidence chain，不计三次确认。

### YouTube：最高观看不等于最好证据

黄金案例的 11 个视频中，截至 2026-07-29 16:42 +08:00，
[AI Search 视频](https://www.youtube.com/watch?v=RCsBJz4W4bA)有 398,935 views，是固定清单内
传播量最高；[Pat Simmons 对比](https://www.youtube.com/watch?v=z_7J_iKuSzU)有 65,924 views，
却因为公开同 prompt、输出、token、成本和时间而更可复核。

Pat 的五个构建合计：Opus 5 $111.84、Fable 5 $156.04、Opus 4.8 $120.86。这个 harness 中
Opus 比 Fable 低约 28%，证明“token 牌价半价”不能直接变成“每个任务成本半价”。
[配套结果](https://www.aiformortals.co/blog/opus-5-vs-opus-4-8-vs-fable-5)

## 6. Code review：39.3% 为什么会误导

CodeRabbit 的 39.3% 是 `xhigh` 下 actionable-comment precision，高于其 production baseline
35.2%；但 known-issue coverage 为 55.2% 对 61.1%，full-stream precision 为 28.6% 对
32.8%，nitpicks 为 92 对 23。它的原结论是 precision-oriented second reviewer，而非唯一
safety net。[完整评测](https://www.coderabbit.ai/blog/opus-5-model-review)

所以 code-review 路由必须同时看 precision、coverage 和噪声；也不能用这组 xhigh 数据证明
“low effort 足够”。静态分析、tests 和人工 review 仍是不同证据层。

## 7. 成本优化：三个旋钮，三种工作负载

| 旋钮 | 适合 | 不适合 | 执行验证 |
|---|---|---|---|
| Prompt cache | 长静态 tools/system/examples + 短变化后缀 | 频繁改 effort/speed 的同一会话 | 看 hit rate 与 write amortization |
| Batch | 大量非实时、可等待的任务 | 实时、Fast、ZDR 需求 | 小批 canary 后查结果保留与 provider |
| Fast | output 生成时间直接影响价值 | TTFT 主导、输出短、成本敏感 | 比端到端 p50/p95，不只看 OTPS |

## 8. 生产采用：从假设到 Gate

1. **Baseline：** 冻结代表任务、现有结果和成本。
2. **AB：** 每次只改变模型、effort 或一类 prompt scaffold。
3. **Canary：** 先给只读/低权限、非生产或小流量任务。
4. **Rollback：** 保留旧配置、输出快照和明确回退条件。
5. **Human Gate：** 删除、迁移、付款、外发、医疗/法律/金融结论必须人工确认。
6. **Promote：** 只有 pass、返工、总成本与风险指标都达到门槛才扩大范围。

Auto mode 可以减少权限提示，但它不是业务安全保证。System Card 还指出 Opus 5 总体更准确，
事实性陈述的幻觉率却略高于 Opus 4.8；更强能力不能替代领域控制。
[System Card](https://www.anthropic.com/claude-opus-5-system-card)

## 什么证据会改变这些建议

- 你的任务集显示 medium 在质量不降时稳定更省：把该任务族默认降到 medium。
- Opus high/xhigh 仍失败而 Fable 一次成功率明显更高：升级该任务族，而非全局升级。
- 清理某项 Skill 后 pass 或安全性下降：恢复它；“上下文更少”不是目标。
- Fast 端到端收益不能抵 2x 价格：不用 Fast，即使 OTPS 更高。
- Anthropic 更新默认值、价格、beta、provider 或 Claude Code 权限：以新文档和实际产品状态重验。

## 关键资源

- Start here：[发布公告](https://www.anthropic.com/news/claude-opus-5)；
  [Prompting guide](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5)；
  [Effort](https://platform.claude.com/docs/en/build-with-claude/effort)
- 技术契约：[Models](https://platform.claude.com/docs/en/about-claude/models/overview)；
  [Pricing](https://platform.claude.com/docs/en/about-claude/pricing)；
  [Batch](https://platform.claude.com/docs/en/build-with-claude/batch-processing)；
  [Fast](https://platform.claude.com/docs/en/build-with-claude/fast-mode)
- 反证：[CodeRabbit](https://www.coderabbit.ai/blog/opus-5-model-review)；
  [Artificial Analysis](https://artificialanalysis.ai/models/comparisons/claude-opus-5-vs-claude-opus-5-medium)；
  [Ethan Mollick](https://x.com/emollick/status/2080709278441033746)
