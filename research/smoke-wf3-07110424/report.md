# AI coding agent 的上下文窗口管理入门 深度调研报告
> depth: quick · generated: 2026-07-11 · tools: WebSearch, WebFetch | skipped: last30days, bird, summarize（VPS-only）
> ⚠️ 互动数据：X/YouTube 全部为「推断·未实测」（本机无 bird/summarize scanner），已逐条标注
> ⚠️ headless run（WF3 driver 调起）：plan checkpoint 已跳过；消歧自决 = Claude Code 主锚 + Codex/Cursor 跨工具对照

## TL;DR
- **这话题 vault 存量极厚，且已有一篇成稿** —— `drafts/claude-code-context-management-guide.md` 已经吃透「每回合 5 选项决策框架」这个纯 Claude Code 角度。**再写一篇同角度 = 自我重复。**
- 有增量的切口只有一个方向：**把「入门」做成跨工具（Claude Code × OpenAI Codex × Cursor）的对照**。三家用不同机制解同一个「上下文有限、会腐烂」的问题，而现有稿只讲了 Anthropic 一家。
- 事实轴的底层地基今年也被外部补强了：Chroma 的 **context rot 实证**（18 个模型全都随长度退化）+ Anthropic 官方 **"attention budget"** 框架，是给「入门」读者一句话讲清「为什么不能无脑塞满」的最佳权威引用。
- 增长轴时机：不是爆点、是长青常青款。可写，但必须靠「跨工具对照 + 官方实证背书」建立差异化，否则淹没在一堆 Claude-Code-only 教程里。

## 0. Vault 已有锚点（查内）

> ⚠️ **重复预警**：`drafts/claude-code-context-management-guide.md`（2026-04-16）已成稿，标题
> 《Claude Code 用得好不好，不在于提示词，而在于每次对话后你做的那个决定》，完整覆盖
> **continue / rewind / compact / clear / subagent 五选项框架** + context rot + Tw93 噪音拆解 +
> 7 层系统。**新稿若重复这个角度 = 无增量，Gate 1 应拒。** 见 §7 与 outline `prior_coverage`。

内部锚点清单（Tier-1，可直接引用免重复核验）：
- [[context-management]] — 7 层记忆架构 + Thariq 5 选项 + Pachaar 30% 中段衰减；本话题主锚页。
- [[context-rot]] — 「越满越笨」；resolver 90 天衰减曲线也复用这个词。
- [[context-noise-governance]] — Tw93「不是容量问题、是噪音问题」+ MCP 工具定义 token 成本拆解。
- [[context-anxiety]] — agent 提前收尾的失败模式；[[task-budgets]] 是模型侧解药。
- [[prompt-cache-optimization]] — 200x cost cliff（$0.003 hit vs $0.60 miss @200K）；跨工具都吃这条。
- [[session-memory]] / [[forked-agent-pattern]] — subagent-as-context-isolation 的底层。
- [[source-thariq-session-management-1m]] — 5 选项框架的原始出处（Tier-1 源页）。

旧判断回收（作者过去对这话题下过的立场）：
- 「1M context 不是让你不用管 context，是给你更多时间在变笨前主动干预」——现有 draft 的收尾金句 + [[context-management]] 都持此立场。**新稿要么推进、要么换角度，不能复述。**
- 「context 的问题是噪音不是容量」（Tw93 框架，作者已采纳为判断）。

已表达角度清单（供 outline `prior_coverage` 逐条声明）：
1. **五回合决策框架（纯 Claude Code）** → `drafts/claude-code-context-management-guide.md` ——【已写透，勿重复】
2. 7 层记忆系统逆向工程 → [[context-management]] wiki 页（偏架构/深水区，非「入门」）
3. context engineering 三层模型（Immediate/Session/Persistent）→ [[four-files-context-architecture]]（Khairallah 角度）

## 1. 这个话题是什么 — 事实轴

**定义（给入门读者的一句话）**：上下文窗口（context window）是模型一次推理能「看到」的全部 token —— 系统提示 + 对话历史 + 所有工具调用与输出 + 读过的文件。**上下文管理 = 在这个有限、且会随填满而退化的窗口里，主动决定留什么、丢什么、隔离什么。**

逐条核验：
- **上下文是「有限且边际递减」的资源，不是越大越好** — source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents（Anthropic, 2025-09-29）— ✅ verified（官方原文用 "finite resource with diminishing marginal returns" / "attention budget"）。
- **Context rot 是实证现象，不是玄学：18 个主流模型（GPT-4.1 / Claude 4 / Gemini 2.5 / Qwen3）全都随输入变长而退化，即使任务很简单** — source: https://www.trychroma.com/research/context-rot（Chroma, 2025-07-14）— ✅ verified（fetch 原文）。**这是给「越满越笨」这句话最硬的量化背书。**
- **退化早在触顶之前就开始** — source: 同上 Chroma — ✅ verified（模型在"打乱的 haystack"上反而比"连贯长文"表现好；单个干扰项随长度放大伤害）。
- **成本层面：一次 prompt cache hit vs miss 差 ~200x**（$0.003 vs $0.60 @200K context）— source: [内部/Tier-1: [[prompt-cache-optimization]]]，溯源自 raw/2026-04-08-troyhua…；跨工具通用 — ✅ verified（内部）。
- **三家工具、同一个问题，不同机制**（见 §2 对照）—— Claude Code：/compact·/clear·/rewind·subagent + 7 层自动系统；Codex：`/responses/compact` 端点 + `encrypted_content` 保留潜在理解；Cursor：Rules（常驻，永远吃 token）vs Skills（动态加载，保持窗口干净）。source: 见 §2 各自官方链接 — ✅ verified（Anthropic/Chroma fetch；Codex/Cursor 经 WebSearch，官方页 403/thin 未能直取全文，标 ⚠️ 部分未逐字核验）。

## 2. 焦点实体深挖 — 三家 coding agent 的上下文机制对照（跨工具）

消歧自决的落点：本话题不锁死单一工具，用三家对照做「入门」的增量。核验纪律同 §1。

| 维度 | Claude Code | OpenAI Codex | Cursor |
|------|-------------|--------------|--------|
| 压缩 | `/compact`（有损，可加方向）+ 7 层自动微压缩 | `/responses/compact` 端点，返回 `type=compaction` item，带**不透明 `encrypted_content`** 保留模型潜在理解 | 对话过长则窗口填满直到无空间回应（docs 语） |
| 清空/新开 | `/clear`（你写 brief，精准） | 新 thread | 新 chat |
| 回退 | `/rewind`（esc esc，移除失败尝试） | — | — |
| 隔离 | subagent 独立 context window | —（Codex 侧本次未取到对等原语） | Skills 动态加载 vs Rules 常驻 |
| 缓存纪律 | prompt cache 前缀稳定 | **prefix caching：中途改 AGENTS.md 会失效系统提示缓存** | `.cursor/rules/*.mdc` `alwaysApply:true` 常驻吃 token |

- **Codex 独有点**：`encrypted_content` compaction —— 压缩不是「总结成文字」，而是保留一个不透明的潜在状态 item。source: https://openai.com/index/unrolling-the-codex-agent-loop/（Michael Bolin, 2026-01-23）— ⚠️ 页面 403，事实经 WebSearch 交叉，未逐字核验。
- **Cursor 独有点**：Rules vs Skills = 「常驻成本 vs 动态加载」，是 Claude just-in-time retrieval 的跨工具平行版，对入门读者是很直观的对照。source: https://cursor.com/docs + https://cursor.com/blog/agent-best-practices — ⚠️ docs 重定向/thin，经 WebSearch，未逐字核验。

> [!warning] 未逐字核验的两条
> Codex 与 Cursor 的官方页在本次 quick 扫描中分别返回 403 / 重定向变薄，事实由 WebSearch 摘要交叉得到。
> 写稿前若要把这两条作为硬 claim，**须 ingest 原文逐字核验**（见 ingest-candidates #2 #4）。

## 3. X / Twitter — Top 3（增长轴 · 渠道层）
> ⚠️ 互动数据「推断·未实测」（本机无 bird）

### #1 Thariq（Anthropic, Claude Code team）— 5 选项框架的原始出处
- 链接：https://claude.com/blog/using-claude-code-session-management-and-1m-context （官方博客承载）· 关联 X long-post
- 格式：long-post / 官方博客 · 互动：高「推断·未实测」
- 核心内容：rewind 而非纠正（纠正会把失败尝试留在窗口污染）；~50% 或每完成一个任务就 `/compact`，别等自动触发；无关工作之间 `/clear` 换干净前缀。
- **写作风格拆解**：第一人称、习惯清单式、每条给「什么时候用」——正是「入门」文该学的可执行密度。

### #2 Boris Cherny（@bcherny，Claude Code 创造者）— 隐藏特性 + subagent 用法
- 链接：https://x.com/bcherny/status/2038454336355999749 · 格式：thread · 互动：高「推断·未实测」
- 核心内容：凡是不需要父 agent 推理的活（批量机械、限定范围调研、可并行）都丢给 subagent → 父 context 保持干净；具名 subagent（code-simplifier / verify-app）。
- **写作风格拆解**：vanilla 实操、"here goes" 列表节奏、无术语堆砌。

### #3 Simon Willison（@simonw）— context-engineering 词汇脚手架
- 链接：https://simonwillison.net/tags/context-engineering/ · 格式：link-blog / long-article · 互动：高「推断·未实测」
- 核心内容：context quarantine / pruning / summarization 三分类，给入门读者一套干净词汇。
- **写作风格拆解**：解释型、建分类法、大量外链——适合做「概念地图」型开头。

## 4. Web / 博客 — Top 4（增长轴 · 渠道层）

### #1 Anthropic — "Effective context engineering for AI agents"（标杆结构）
- 链接：https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents · 作者：Anthropic Applied AI（Rajasekaran 等）· 2025-09-29
- 核心：context = 有限「attention budget」；context rot 系于 transformer n² 两两关系；6 大机制（compaction / 结构化笔记 NOTES.md / sub-agent / 工具结果清理 / just-in-time 检索）。
- **写作风格拆解**：分层教学、逐段递进复杂度、权威但对话感、以具体案例（Claude Code、Pokémon）落地——**入门稿直接学这个骨架**。

### #2 OpenAI — "Unrolling the Codex agent loop"（跨工具对照源）
- 链接：https://openai.com/index/unrolling-the-codex-agent-loop/ · 作者：Michael Bolin · 2026-01-23
- 核心：Codex 超阈值即压缩，`/responses/compact` 返回带 `encrypted_content` 的 item；prefix caching；实操铁律「中途别改 AGENTS.md，会失效缓存」。
- **写作风格拆解**：执行循环级深挖、工程师口吻、"hard-earned lessons"——做「另一家怎么解」的对照段最佳。

### #3 Chroma — "Context Rot: How Increasing Input Tokens Impacts LLM Performance"（实证背书）
- 链接：https://www.trychroma.com/research/context-rot · 作者：Kelly Hong / Anton Troynikov / Jeff Huber · 2025-07-14
- 核心：18 模型全退化；语义匹配比词面退化更快；打乱 haystack 反优于连贯长文；对话历史任务差距大（Claude 尤甚）。
- **写作风格拆解**：技术学术、实验方法论、意外发现框架——**作为「为什么」的量化脊梁引用，不作为入门文体范本**。

### #4 Cursor — Context Management docs（第三家对照）
- 链接：https://cursor.com/docs · https://cursor.com/blog/agent-best-practices · docs register
- 核心：每请求装配 always-on（系统提示 + `.cursor/rules/*.mdc alwaysApply:true`）+ conditional（选区 / @提及 / 历史）；Rules 常驻吃 token vs Skills 动态加载保持窗口干净。
- **写作风格拆解**：docs 体、规范化 best-practice bullet。

## 5. YouTube — Top 4（增长轴 · 渠道层）
> ⚠️ 观看/互动「推断·未实测」（本机无 summarize/last30days）

- **"AI Mastery No.5: Claude Code Subagents for context management"** — https://www.youtube.com/watch?v=_MxOO4M9PT0 · ~2026-03-03 · 实操（subagent 做隔离）。
- **"Context compaction for solving context window limits in a coding agent"** — https://www.youtube.com/watch?v=EOIiUr6Im_Y · ~2026-04-11 · build-along（自己实现压缩）。
- **"Context Management masterclass — Technical Deep Dive"** — https://www.youtube.com/watch?v=mM_Wxemh3lU · ~2026-06 下旬 · 理论倾向深挖。
- **Simon Willison — "Engineering practices that make coding agents work"（Pragmatic Summit）** — https://www.youtube.com/watch?v=owmJyKVu5f8 · 演讲 · 理论+实操。
- 倾向总结：YouTube 侧整体偏实操/走查；理论集中在 masterclass 与 Willison 演讲。

## 6. 核心洞察 + 最佳实践

洞察：
1. **「有限 + 会腐烂」是入门读者唯一必须先装进脑子的底层事实** —— 有了它，五个操作才不是死记硬背。[外部: anthropic.com/…/effective-context-engineering-for-ai-agents] + [外部: trychroma.com/research/context-rot]。
2. **同一问题、三家不同解，恰恰是「入门」的最佳教学装置** —— 对照比单讲一家更快让读者建立心智模型。[外部: openai.com/…/unrolling-the-codex-agent-loop] [外部: cursor.com/docs] [内部/Tier-1: [[context-management]]]。
3. **缓存纪律是隐形的第 6 个操作** —— Codex「别中途改 AGENTS.md」、Claude 保持前缀稳定，都是同一条「保护 prompt cache」在不同工具的投影，成本差 ~200x。[外部: openai.com/…/unrolling-the-codex-agent-loop] [内部/Tier-1: [[prompt-cache-optimization]]]。
4. **subagent 的核心价值是上下文隔离，不是并行** —— 跨工具（Claude subagent / Cursor Skills 动态加载）都在做「把中间过程挡在主窗口外」。[内部/Tier-1: [[session-memory]]] [外部: x.com/bcherny/status/2038454336355999749]。

最佳实践清单（给入门读者）：
1. 先建立心智：context 有限且越满越笨 → 目标是「信噪比」不是「填满」。
2. 学会「每回合停 2 秒」的决策反射（continue / rewind / compact / clear / subagent —— 这条已在现有 draft 讲透，新稿引用而非复述）。
3. 关掉不常用的 MCP server / 常驻 Rules（省下 10-25K 隐形 token）。[内部/Tier-1: [[context-noise-governance]]]。
4. 主动 compact（别等自动），并加方向说明。
5. 大量中间输出的活丢给 subagent。
6. 保护 prompt cache：别在 session 中途改系统级文件（CLAUDE.md / AGENTS.md / Rules）。

> **溯源标注纪律（全报告适用）**：每个论断已标 `[内部/Tier-1: 页名]` 或 `[外部: URL]`。
> 下游 writer **只许穿透引用这些原始出处**，不得引用本报告（防「报告引报告」自举塌缩）。

## 7. 对内容创作的启示 — 增长轴 → 排序的内容角度
**这是两轴相乘的地方，也是 /draft 的入口。**

### 时机窗口
不是爆点、是**长青常青款**（evergreen）：context 管理是每个 coding-agent 用户反复撞的墙，搜索/AI 引用需求稳定。但正因常青，**Claude-Code-only 教程已经很多**（含我们自己那篇）。**唯一还开着的窗口 = 跨工具 + 官方实证背书的差异化**。现在写没有时间压力，但角度必须选对，否则无增量。

### 排序的内容角度（每个 = 一个内容赌注）

#### 角度1（推荐）《三家 AI coding agent 怎么管上下文：Claude Code × Codex × Cursor 入门对照》
- 缺口：现有 draft 只讲 Claude Code 一家；外部内容也大多单工具。跨工具「同问题 / 不同解」的入门对照是空位。
- 受欢迎度证据：三家官方都各有深度原文（§4 #1/#2/#4，实测发布日期齐）；subagent/context 类 YouTube 实操需求稳定（§5，「推断」）。
- 参考写法：骨架学 Anthropic §4#1 的分层教学；对照段学 Codex §4#2 的「另一家怎么解」；开头概念地图学 Simon Willison §3#3 的三分类。
- 渠道 + 形式：博客长文（中文主体，GEO 优化）。
- 依赖：§2 对照表 + §1 全部 claim；ingest 候选 #1/#2/#4 须先逐字核验（§2 warning）。

#### 角度2《为什么 context 越满越笨：一篇给非工程师的 context rot 实证解读》
- 缺口：现有 draft 只用一句话带过 context rot；没人把 Chroma 的 18 模型实证做成中文入门。
- 受欢迎度证据：Chroma 原文是被反复引用的一手研究（§4#3）。
- 参考写法：把学术实证「翻译」成 audience-profile 的浅读者语言；前置结论 + 统计数字（GEO）。
- 渠道 + 形式：博客中长文 / 可拆 X 长文。
- 依赖：§1 Chroma + Anthropic 两条 claim。

#### 角度3《上下文管理里最省钱的一招：保护 prompt cache（跨工具）》
- 缺口：缓存纪律散落各处，没被单独拎成一篇；200x 成本差是强钩子。
- 受欢迎度证据：Codex「别改 AGENTS.md」+ 内部 200x cliff（§6 洞察3）。
- 参考写法：单点深挖 + 可核验数字（GEO 统计数据规则）。
- 渠道 + 形式：X 长文 / 博客短文。
- 依赖：[[prompt-cache-optimization]] + Codex 原文。

### 关键人物值得跟踪
| 人物 | 角色 | 关注理由 |
|------|------|----------|
| Thariq | Anthropic Claude Code team | 5 选项框架原始出处，session 管理权威 |
| Michael Bolin | OpenAI Codex lead | Codex 循环/压缩机制的一手作者 |
| Kelly Hong / Jeff Huber | Chroma | context rot 实证研究作者 |
| Boris Cherny | Claude Code 创造者 | subagent/隐藏特性一手实践 |
| Simon Willison | 独立开发者 | context-engineering 词汇与品味标杆 |

### 内容形式参考库
- 长文学谁：Anthropic《Effective context engineering》——分层教学骨架。
- 实证解读学谁：Chroma《Context Rot》——数据脊梁（内容学它、文体别学它）。
- 对照段学谁：OpenAI《Unrolling the Codex agent loop》——「另一家怎么解」。
- X 学谁：Boris Cherny——vanilla 实操清单节奏。

## 附录：关键时间线
| 日期 | 事件 |
|------|------|
| 2025-07-14 | Chroma 发布《Context Rot》实证研究（18 模型）——本话题事实脊梁 |
| 2025-09-29 | Anthropic《Effective context engineering for AI agents》——attention budget 官方框架 |
| 2026-01-23 | OpenAI《Unrolling the Codex agent loop》——Codex 压缩 + prefix caching |
| 2026-04-16 | Thariq session-management-1M（vault 5 选项框架源）+ 我们据此写成 `drafts/claude-code-context-management-guide.md` |
| 2026-07-11 | 本次调研（quick，headless）——识别跨工具对照为唯一增量角度 |
