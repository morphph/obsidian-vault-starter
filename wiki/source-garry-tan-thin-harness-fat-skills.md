---
type: source-summary
created: 2026-04-19
last-updated: 2026-04-19
sources:
  - raw/2026-04-11-garry-tan-thin-harness-fat-skills.md
tags: [wiki, source, agentic, harness, skills]
---

# Source: Garry Tan — Thin Harness, Fat Skills

## Summary
Long-form X article by [[garry-tan|Garry Tan]] (YC President & CEO), 2026-04-11. ~2,500 words, 3,847 likes, 10,838 bookmarks, 1.4M views. Field-guide framing of [[harness-design]] aimed at AI builders: explains the 100x productivity gap as architectural, defines five primitives ([[skill-as-method-call|skills]], harness, [[resolvers]], [[latent-vs-deterministic]], [[diarization]]), and demonstrates them on a real YC Startup School use case. Most accessible synthesis of the harness pattern published to date.

## Source
- **URL**: https://x.com/garrytan/status/2042925773300908103 (links to X long-form article)
- **Posted**: 2026-04-11 11:20:34 UTC
- **Author**: Garry Tan (@garrytan, 756K followers)
- **Engagement** (at fetch time): 3,847 likes · 401 RT · 140 quotes · 10,838 bookmarks · 1.4M views · 129 replies
- **Fetch method**: api.fxtwitter.com (WebFetch and Playwright failed; fxtwitter API exposed the full article body)

## 要点解读

### 1. 核心论断：100x 生产力差距来自架构，不是模型智力
Steve Yegge 说用 AI 编码 agent 的人比 Cursor/chat 用户快 10x-100x。但 2x 的人和 100x 的人用的是同一个 Claude。差别是"包裹模型的东西"（harness）。3/31/2026 Anthropic 误把 [[claude-code]] 全部 51.2 万行源码发到 npm，Garry 读了源码后确认：秘密不在模型，而在 wrapper —— live repo context、prompt cache、purpose-built tools、context bloat 控制、结构化 session memory、并行 sub-agents。

### 2. 三层架构（一张索引卡能写下）
- **顶层 Fat Skills**：markdown 写的可复用过程，封装判断、流程、领域知识。**90% 的价值在这里。**
- **中层 Thin Harness**：约 200 行 CLI，JSON 进文本出，默认只读。负责跑 loop / 读写文件 / 管理 context / 安全。
- **底层 Deterministic**：QueryDB / ReadDoc / Search / Timeline。
方向性原则：智能向上推到 skills，执行向下推到确定性工具，harness 保持薄。每次模型升级，所有 skills 自动变强，确定性层保持可靠。

### 3. Skill = 方法调用（最反直觉的点）
skill 文件描述"怎么做判断"（例：`/investigate` 有 7 步：scope dataset → build timeline → diarize → synthesize → argue both sides → cite sources），参数决定"对谁做"（TARGET / QUESTION / DATASET）。同一个 `/investigate`：给 210 万封举报邮件 → 医学研究分析师；给空壳公司 + FEC 数据 → 金融取证员。同样七步，调用参数换了世界。**这不是 prompt engineering，是用 markdown 当编程语言、人类判断当 runtime 的软件设计。**

### 4. 最常犯的错：latent vs deterministic 混淆
- **Latent（智能所在）**：判断、综合、模式识别。例：给 8 个人排晚宴座位，考虑性格和社交动态。
- **Deterministic（信任所在）**：同输入同输出。SQL、编译代码、算术。例：给 800 人排座位 → 这是组合优化，LLM 会产生看着合理但完全错的座位表。
最烂的系统把工作放错一侧。最好的系统对这条线极其苛刻。这与 [[ryan-sarver|Ryan Sarver]] 早一周提出的 [[llm-judgment-vs-scripts]] 是同一条线，不同框架。

### 5. Resolver + Diarization
- **Resolver**：context 的路由表。Garry 坦白自己 CLAUDE.md 曾 20000 行，模型注意力直接崩溃，Claude Code 让他砍回 200 行 +"指针"。skill description 字段就是 resolver —— 用户意图自动匹配 skill。这个 wiki 的 `.claude/rules/` 用 `paths:` glob 也是 resolver 模式。
- **Diarization（档案化）**：让 AI 对知识工作真正有用的步骤。模型读完一个主题的全部材料，写一页结构化档案。关键输出是 SAYS vs ACTUALLY BUILDING 的差距（例：Maria 说做 AI observability，但 80% commit 在 billing 模块 → 实际是 FinOps 工具）。**RAG / embedding 都做不到** —— 必须模型自己读完所有材料并保持矛盾在脑里。

### 6. 铁律 ——"我问你两次，你就失败了"
Garry 给自己 OpenClaw 的指令，反响最大（先前推文 1000 赞 + 2500 收藏）：
> 任何会重复出现的任务，第一次手动在 3-10 个样本上做、拿给我看、我同意后固化成 skill 文件、该上 cron 就上 cron。如果我要问你第二次，你就失败了。
为什么重要：每个 skill 是**永久升级**，不退化不遗忘，3 点钟自动跑。换新模型时 latent 那层自动变强，deterministic 那层保持可靠。系统会复利。Build it once. It runs forever.

## Worked example: YC Startup School (July 2026)
Chase Center, 6,000 founders. Stack:
- `/enrich-founder` — nightly cron pulls 全部源（GitHub / 申请书 / advisor 1:1 transcript / X / Claude Code transcripts），diarize 到一页档案
- `/match-breakout` (1,200 founders, 30/room, sector clusters)
- `/match-lunch` (600, 8/table, serendipity, no repeats)
- `/match-live` (200ms nearest-neighbor, exclude met-before)
- `/improve` 读 NPS，diarize 那些"OK"评价（不是差的，是差点对的），提取规则，**自动写回 skill 文件**。July: 12% "OK" → 下次：4%。

## Pages created from this source
- [[garry-tan]] — entity
- [[thin-harness-fat-skills]] — concept (the slogan/architecture)
- [[skill-as-method-call]] — concept (skills take parameters)
- [[diarization]] — concept (model reads everything → structured profile)
- [[resolvers]] — concept (routing table for context)
- [[latent-vs-deterministic]] — concept (the line that matters most)

## Pages updated from this source
- [[harness-design]] — added Garry's three-layer formulation and 3/31 npm leak event
- [[openclaw]] — added Garry as practitioner; "if I ask twice you failed" rule
- [[claude-code]] — added 3/31/2026 npm source leak event; CLAUDE.md 20K→200 line case study
- [[llm-judgment-vs-scripts]] — cross-linked to [[latent-vs-deterministic]] as Garry's reformulation

## Connections
- Related: [[garry-tan]], [[thin-harness-fat-skills]], [[skill-as-method-call]], [[diarization]], [[resolvers]], [[latent-vs-deterministic]], [[harness-design]], [[llm-judgment-vs-scripts]], [[openclaw]], [[claude-code]]
