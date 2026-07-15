---
type: source-summary
created: 2026-07-15
last-updated: 2026-07-15
sources:
  - raw/2026-07-14-agent-harness-real-code-waku.md
tags: []
---

# 精要：You Can Learn AI Agent Harness In Real Code In 20 Min

## 精要

**作者/讲者**：Sean（Shen Sean Chan；频道 Sean's AI Stories，人在伦敦，做 AI agent 内容与开源）
**来源**：YouTube · 2026-07-14 · [视频](https://www.youtube.com/watch?v=rvRyBhILrls)
**篇幅**：20:49 · 2,520 次观看（抓取时） · **精要预读时长**：约 6 分钟
**一句话主旨**：用一个开源本地 agent 项目 **Waku-Agent** 的真实代码，把「agent harness」这个 buzzword 拆成可运行的**四大支柱——harness/loop、memory、eval、LLM ops**：一次请求从 gateway 进来 → 过 **retrieval gate** 决定要不要取记忆 → 装配 **三类记忆**（语义/情景/程序）当 context → agent 跑 **loop** 调工具直到完成 → 全程 **trace + eval**，事后把耐久事实**固化进语义记忆**。全部跑在本地、你自己拥有。

> ⚠️ 本精要基于**自动字幕**校正而来。原字幕把 "AI agent" 听成 "Asian"、"LLM" 听成 "LM"、"Claude Code" 听成 "clock code"、"Supabase" 听成 "Superbase"、"LLM as judge" 听成 "valve"，人名/repo 名拼写不稳——下面按上下文校正，存疑处标注。

---

### 1. 核心论点（Thesis）

「Agent harness / loop / memory / eval」听着像一堆 buzzword，但把它们放进真实代码就一目了然。讲者原话：**"just remember that it's all buzzwords. What I literally demoed just now is exactly what these things mean."**（记住这些都是行话；我刚演示的，就是这些词的确切含义。）他用自建开源项目 Waku-Agent 走一遍 demo + 代码，证明一个「个人 AI 助理」的完整 harness 可以简单到 clone 一个 repo 就跑起来，且**完全本地、数据在你自己机器上**——"you literally own this agent, just like Hermes, just like OpenClaw"。

### 2. 内容骨架（＝覆盖度自检）

1. **Demo（前半）**：一句「找齐剩下的世界杯比赛并加进我日历」→ 展示 retrieval gate、loop 引擎、工具调用、成本/trace、语义记忆（Sergey/Raj 是谁）、Telegram 网关、加记忆、语音模式。
2. **代码走查（后半）**：quick start（clone→localhost）→ database（SQL 表）→ **soul.md**（系统 prompt）→ **memory.md**（耐久事实）→ **traces**（token/成本/延迟）→ **eval**（deterministic + LLM-as-judge）→ **skills = 程序记忆**（schedule_meeting、现场新建一个 skill）→ settings（API keys）→ agent loop（max iterations=10）→ 三类记忆回顾 → ops/runtime/tools/主类 Waku。
3. **架构总回顾**：gateway → retrieval gate → memory → agent loop + tools → 返回 + trace + eval → 语义记忆固化。

### 3. 关键概念 & 框架 / 心智模型

> **Agent harness 四大支柱（four pillars）**
> - **是什么**：harness/loop、memory、eval、外加 **LLM ops**（tracing/dashboard/prompt 发布）。这是全片的骨架心智模型。
> - **为什么重要**：给「agent 系统」一个可核对的清单——任何 agent 产品都能对着这四项自查缺哪块。

> **Loop 引擎（agent loop）**
> - **是什么**：agent 反复「思考→调工具→观察」直到达成目标；本项目默认 **max iterations = 10**。
> - **怎么用**：demo 里「查世界杯 + 加日历」就是 loop 调 `search_web` 与 `create_event` 两个工具跑完的。对应 vault 的 [[orchestration-loop]]（TAO 循环）。

> **Retrieval gate（检索闸）**
> - **是什么**：agent 动手前，一道闸**先判断这次要不要去取记忆**——不是每个 query 都需要检索（demo 里"加世界杯"不需检索，"Sergey 是谁"才触发检索）。
> - **为什么重要**：省 token、避免无谓 RAG；本质是"在个人规模上，先判断再检索"，呼应 [[index-over-rag]]。

> **三类记忆（memory taxonomy）**——全片最可迁移的部分：
> - **语义记忆 (semantic)**：耐久事实。如"Sergey 是爱游泳、常做好吃的的密友"。系统在察觉出现耐久事实时**自动 consolidate** 存入。
> - **情景记忆 (episodic)**：带日期的事件。如日历上的世界杯比赛、和 Sam Altman 的会。
> - **程序记忆 (procedural) = skills**：agent"该怎么做事"。如 `schedule_meeting` skill：解析相对日期 → 查记忆里与会者偏好 → 调 `create_event`。**skill 就是 markdown 文件（skill.md），新建一个文件夹即可加**——和 Claude Code 的 skills / [[thin-harness-fat-skills]] 同一套路。

> **Eval（两种）**
> - **deterministic（确定性规则）**：手写硬规则，如"检查 Apple Calendar 工具是否正常""working memory 是否正常"。
> - **LLM-as-judge（AI 当裁判）**：用 Anthropic 模型评定质性问题——"这个回复好不好？健康不健康？"。**每次 agent 回复后顺着 trace 自动跑 eval**。直接对应 [[verification-loops]]（rules-based + LLM-as-judge）。

> **soul.md**：项目的**系统 prompt**，可在 dashboard 里改、实时热更（demo：加一句"道谢时说 muchas gracias"，立即生效）。

### 4. 关键数据与事实

- **四大支柱**：harness/loop · memory · eval · LLM ops。
- **agent loop 默认 max iterations = 10**。
- **三类记忆**：semantic（耐久事实，自动 consolidate）/ episodic（带日期事件）/ procedural（skills）。
- **retrieval gate** 决定检索 or 跳过；demo 里"查世界杯"任务耗时**约 100 秒**。
- **网关三种**：内置 chat UI · Telegram（用 BotFather 建 bot）· 语音模式（唤醒词 **"Waku Waku"**，日语「ワクワク」＝兴奋；项目原名 Jarvis，因太普通改名）。
- **工具**：Apple Calendar、`search_web`（Tavily API）、写 note，未来接 MCP。
- **API keys（settings 必填）**：Anthropic + Gemini + Tavily（web search）。
- **本地优先**：trace/记忆全存本机（`.waku` 目录、SQLite 表、traces 文件）；要上云可接 Supabase 或 Langfuse。
- repo：**waku-agent**，作者 GitHub **Shen Sean Chan**（demo 端口 localhost:778，因 777 被占）。

### 5. 金句

- "just remember that it's all **buzzwords**. What I literally demoed just now is exactly what these things mean."（这些都是行话；我刚演示的就是它们的确切含义。）
- "All we're doing right now is **preparing the right context** for the agent."（我们做的一切，就是给 agent 准备好对的 context。）—— 一句话点破 memory+gate 的意义。
- "you literally **own this agent**, just like Hermes, just like OpenClaw. But it's very simple and straightforward."（你是真正拥有这个 agent……而且它极简单直接。）
- "for the episodic memory... it's basically a **dated event** ... the semantic memory is basically **consolidated** every single time when it feels like there's some durable facts."（情景记忆是带日期的事件；语义记忆则在察觉耐久事实时被固化。）

### 6. 可执行要点（Takeaways）

1. **拿四大支柱当自查清单**：审任何 agent 系统（含你自己的 LoreAI / blog2video pipeline）——harness/loop、memory、eval、LLM ops，缺哪块补哪块。
2. **记忆按三类分库 + 一道 retrieval gate + 事后 consolidation**，是一套可直接抄的个人助理记忆设计；语义记忆的自动固化≈ vault 里的 [[dreaming]] 思路。
3. **skills 用 markdown 文件夹装（= 程序记忆）**：新建 `skills/<name>/skill.md` 写清"解析日期→查记忆→调工具"即可扩展 agent 行为，可让 Claude Code 代写。
4. **eval 廉价化**：deterministic 硬规则挡明确项 + LLM-as-judge 评质性项，挂在每次回复后的 trace 上自动跑——低成本持续 eval。
5. **个人助理优先本地**：trace/记忆存本机，需要协作再接 Supabase/Langfuse。

### 7. 收尾

---
## 精要收尾
- **一句话总结**：一个 20 分钟的真实代码走查，把「agent harness」拆成 harness/loop + 三类记忆 + eval + LLM ops，用开源本地项目 Waku-Agent 演示"请求→检索闸→记忆→loop 调工具→trace+eval→固化语义记忆"的完整回路。
- **与 vault 的连接**：
  - [[harness-design]] / [[orchestration-loop]] — 本片是"harness + loop"这对概念的**可运行实例**（loop 默认 10 轮、调工具直到达标）。
  - [[verification-loops]] — eval 文件夹 = 该页描述的"rules-based + LLM-as-judge"的落地代码版。
  - [[dreaming]] / [[context-management]] — 语义记忆"察觉耐久事实即 consolidate"是跨会话记忆固化的轻量实现；三类记忆是分层记忆的具体切法。
  - [[thin-harness-fat-skills]] — skills=程序记忆、以 markdown 文件夹承载，与"胖 skills 薄 harness"同构。
- **视频适配自评**：**适合**做白板讲解视频——架构回路（gateway→gate→memory→loop→tools→trace/eval→consolidate）与"四支柱/三记忆"高度可空间化，是清晰的概念图；但**代码逐行走查那半段不适合**图示，做视频应只取架构与心智模型层，跳过 IDE 操作细节。
- **覆盖度自检**：骨架三段均已覆盖——demo 段（gate/loop/工具/成本/语义记忆/Telegram/语音）、代码段（soul.md/memory.md/traces/eval/skills/settings/loop/三类记忆）、总回顾。**中段代码走查**（database、traces、eval 两类、skills 现场新建）已在 §3/§4 逐项落点，未略过。有意省略：demo 里的日常闲聊（世界杯球队偏好、朋友介绍等叙事填充）。
