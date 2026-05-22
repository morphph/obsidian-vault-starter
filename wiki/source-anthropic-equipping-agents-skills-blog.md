---
type: source-summary
created: 2026-05-22
last-updated: 2026-05-22
sources:
  - raw/2026-05-22-anthropic-equipping-agents-skills-blog.md
tags: [wiki, source, anthropic, skills, foundational]
---

# Source: Anthropic — Equipping Agents for the Real World with Agent Skills

## Summary
The **original Anthropic Engineering announcement** for Agent Skills (2025-10-16, by Barry Zhang + Keith Lazuka + Mahesh Murag). The piece that introduced the SKILL.md concept publicly, ~5 months before the official docs (2026-04-21) or [[anthropics-skills-repo|github.com/anthropics/skills]] became canonical references. Establishes the **"onboarding guide for a new hire" framing**, the **three-tier progressive disclosure** as #1 design principle, **"effectively unbounded" context** as the philosophical claim that makes skill libraries scalable, and the **"sorting via token vs algorithm"** example as the official statement of [[latent-vs-deterministic]]. Ends with the **recursive meta-skill vision** ("agents to create, edit, and evaluate Skills on their own") that [[skillify-meta-skill|Garry's /skillify]] and [[anthropic-skill-creator]] subsequently implement. **Foundational text — everything else in the Skills wiki stands on this.**

## Source Metadata
- **URL:** https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills
- **Authors:** Barry Zhang (PM, Claude API) · Keith Lazuka (engineer, also maintains [[anthropics-skills-repo]]) · Mahesh Murag (researcher)
- **Posted:** 2025-10-16
- **Format:** Anthropic Engineering blog post
- **Fetch method:** WebFetch (static page)

---

## 要点解读（12-Section Comprehensive Study Guide）

### 1. 元信息
- **作者**：Barry Zhang + Keith Lazuka + Mahesh Murag —— **三人组合是产品 + 工程 + 研究的共识签名**。Keith 是 [[anthropics-skills-repo]] 的实际 maintainer
- **来源**：anthropic.com/engineering（Anthropic 官方工程博客）
- **发表时间**：**2025-10-16** ⭐⭐⭐ **关键发现**——比我们 wiki 里所有其他 Skills 内容早 5-7 个月。Skills 是 2025 年末就公开的设计，整个 2026 上半年的讨论都在消化这一篇
- **在 Anthropic 整体输出中的位置**：**Skills 概念的奠基石**。后续 docs 是 spec；这篇是 thesis

### 2. 核心论点
让 agent 具备专门能力的正确范式不是建造 custom agent（每个用例一个），而是给 agent 装载可组合的 Skills（一个 agent 多种能力）。**因为** procedural knowledge 天然就该被打包成"新员工 onboarding guide"那样的可复用单位，**所以** Skills 的核心设计是 progressive disclosure 三层结构 + bundled code 处理 deterministic 部分。

一句话：**"Skills 是给 agent 写'员工手册'的方式——三层渐进披露让上下文'实际上无限'，bundled 代码让确定性工作走代码不走 LLM。"**

### 3. 论证结构
```
1. 问题：custom agents 不可扩展
2. 方案：能力打包成 Skills，类比 onboarding guide
3. 机制：progressive disclosure 三层（metadata → SKILL.md → bundled files）
4. 深化：scripts 是 deterministic 替代品（sorting via token 比 algorithm 贵）
5. 实践：4 步方法论（evaluation / structure / Claude perspective / iterate）
6. 边界：安全 + 终局愿景（agent 自己写/改/评估 skills）
```

### 4. 关键概念字典

> **Onboarding Guide for a New Hire（新员工手册类比）**
> Anthropic 官方对 Skills 的核心类比。决定了写 skill 的视角——不是 prompt（工作描述）、不是 tool docs（工具说明书）、是 onboarding（价值观 + 流程 + 工具 + 文化）。延伸：好的 onboarding 分阶段告知，正是 progressive disclosure 的来源

> **Progressive Disclosure（渐进披露）—— 三层架构**
> metadata（永远在 context）→ SKILL.md body（触发时加载）→ bundled files（按需读取）。**原文 #1 设计原则**。让 "amount of context bundled into a skill effectively unbounded"

> **PDF Skill as Worked Example**
> Anthropic 唯一给的具体例子。结构：`pdf/SKILL.md` 引用 `reference.md` + `forms.md` + Python 脚本。**写自己 skill 时直接对照**

> **Bundled Code as Deterministic Reliability**
> Skills 可以在 `scripts/` 捆绑可执行代码。原文金句："sorting a list via token generation is far more expensive than simply running a sorting algorithm." 这是 [[latent-vs-deterministic]] 的官方版

> **Iterate with Claude（与 Claude 协同迭代）**
> 在做任务时让 Claude 把成功/失败方法**当场**写进 skill。**这是官方版的 "post-execution skillification"** —— [[skillify-meta-skill|Garry Tan 的 /skillify]] 和 [[anthropic-skill-creator]] 是这条方法论的实施化

> **"Effectively Unbounded" Context**
> Progressive disclosure 让 skill 总量不再受 context window 限制。核心是"按需"。重塑了"skill 多大算合理"的直觉

### 5. 框架与心智模型

**核心框架：写 skill 的 4 步官方方法论**

```
1. Start with evaluation  — 跑代表性任务，看 agent 卡在哪
2. Structure for scale    — SKILL.md 大了就拆；代码兼做 tool 和 docs
3. Think from Claude's perspective — 监控使用，特别看 name + description 触发对不对
4. Iterate with Claude    — 任务中让 Claude 自己抓 successful approaches 回写 skill
```

**与其他版本对比**：

| 来源 | 阶段 | 起点 | 强项 |
|---|---|---|---|
| **本篇（2025-10-16）** | 4 步 | Evaluation 驱动 | 简洁 + 原则导向 |
| Khairallah | 4 阶段 | 重复任务发现 | mass-audience 易懂 |
| Garry 10 步 | 10 步 | 失败响应 | 测试齐全 |
| [[anthropic-skill-creator]] | 7 步循环 | 用户意图 | ML 严谨（train/test） |

### 6. 关键数据与例证

| 数据 | 支撑 | 用途 |
|---|---|---|
| **2025-10-16 发表** | Skills 是 2025 年末公开设计 | 验证 wiki 知识源头时序 |
| **PDF skill 唯一具体例** | Skills 是 minimal viable abstraction | 学写法只需读 PDF skill |
| **Three-tier progressive disclosure** | well-organized manual 类比 | 解释给非技术人时这个类比最易懂 |
| **"effectively unbounded" context** | 物理不无限，按需加载实际不限 | 论证 skill 库可以做大 |
| **"sorting via token vs algorithm"** | deterministic vs latent 具体性能例 | 引用时的官方背书弹药 |
| **3 位作者：PM + engineer + researcher** | 多方共识设计 | 反驳"PM 拍脑袋"质疑 |

### 7. 关键引语

> "Skills are a simple concept with a correspondingly simple format."
> Skills 是简单概念配简单格式。
> ⭐ 设计哲学陈述

> "Progressive disclosure is the core design principle that makes Agent Skills flexible and scalable."
> 渐进披露是让 Agent Skills 灵活可扩展的核心设计原则。
> ⭐ 官方点名 #1 设计原则

> "Like a well-organized manual that starts with a table of contents, then specific chapters, and finally a detailed appendix, skills let Claude load information only as needed."
> ⭐ 给非技术人解释 progressive disclosure 的最佳类比

> "Sorting a list via token generation is far more expensive than simply running a sorting algorithm."
> ⭐ Latent vs deterministic 的官方版具体例

> "The amount of context that can be bundled into a skill is effectively unbounded."
> ⭐ 重塑了"skill 多大算合理"的直觉

> "Will help you discover what context Claude actually needs, instead of trying to anticipate it upfront."
> ⭐ 反 over-engineering 的官方立场

> "Install skills only from trusted sources."
> ⭐ 安全戒律

> "Agents to create, edit, and evaluate Skills on their own, letting them codify their own patterns of behavior into reusable capabilities."
> ⭐ Anthropic 自己写下的 recursive meta-skill 愿景——后续被 /skillify 和 skill-creator 实施化

### 8. 实操指南

**官方 4 步方法论（直接抄）**：
- [ ] **Start with evaluation**：跑 5-10 个代表性任务，记录 agent 缺什么
- [ ] **Structure for scale**：SKILL.md 大了拆；互斥流程拆到不同文件；代码既是 tool 也是 docs
- [ ] **Think from Claude's perspective**：监控使用 + 重点看 description 触发对不对
- [ ] **Iterate with Claude**：任务中让 Claude 自己抓 successful/failed approaches 回写 skill；出错让 Claude 反思

**推荐组合方法（融合 4 个来源）**：
1. Evaluation first（本篇）— 看缺口准
2. Three-Question Test（Khairallah）— what/when/perfect-output
3. 写 SKILL.md draft — pushy description + imperative + explain why
4. Iterate with Claude in-task（本篇）
5. Three-Scenario Test（Khairallah）— happy + edge + stress
6. Bundle repeated work（skill-creator）— 3 次都自己写脚本就该 bundle
7. 20-query trigger eval（skill-creator）— production-grade 才上
8. Check-resolvable + DRY（Garry）— 多 skill 后做

### 9. 对比与反对意见

| 对比 | Anthropic 立场 | 隐含信念 |
|---|---|---|
| vs Custom Agents（每用例一个） | 反对—不可扩展 | 一 agent 多 skill > 多 agent |
| vs 巨大 system prompt | 反对—上下文成本高 | Progressive disclosure > 一次塞满 |
| vs MCP servers | **complement** 不是替代 | MCP 给外部工具，Skills 给内部 workflow |
| vs anticipating context upfront | 反对—你猜不准 | In-task iterate > pre-design |
| vs "skills 越大越好" | 隐含反对 | 模块化 > 堆积 |
| vs 信任所有 skill 源 | 反对—装可信源 | 安全前置 |

**隐含承认的限制**：
- 没具体讲怎么测 skill 效果（被 skill-creator 补全）
- 没讲多 skill 协同/冲突（被 gbrain RESOLVER.md 补全）
- 没讲 description 怎么写（被 skill-creator "pushy" 和 trigger eval 补全）
- 这是奠基，deliberately vague——为后续生态留发展空间

### 10. 与 wiki 知识的连接

**强连接（这篇是源头）**：
- [[agent-skills-standard]] — 该标准的原始构思来源
- [[anthropics-skills-repo]] — Keith Lazuka 既是本文作者也是 repo maintainer
- [[anthropic-skill-creator]] — "Iterate with Claude" + 4 改进原则是这篇方法论的实施化
- [[skillify-meta-skill]] — Garry Tan 的 `/skillify` 是本文末尾愿景 "agents create/edit Skills on their own" 的开源实施
- [[latent-vs-deterministic]] — "sorting via token vs algorithm" 是该 line 的官方背书
- [[llm-judgment-vs-scripts]] — 同上，Ryan Sarver 命名版本

**强化已有概念**：
- 强化 [[agent-skills-standard]]：原始设计意图（onboarding guide 类比 + 三层结构 + effectively unbounded 哲学）
- 强化 [[latent-vs-deterministic]]：sorting 例子的官方背书
- 强化 [[skillify-meta-skill]]：原文愿景直接预告 /skillify 类 meta-skill 的必然性

**挑战/补充**：奠基文，更多是被后续补全。一个轻微张力：本文"start with evaluation"vs Khairallah"start with repeated task"——两者兼容（Khairallah 是简化版）

**扩展方向**：
- ⚪ 可选：anthropic.com/news/skills（产品发布稿）
- ⚪ 可选：Anthropic 官方 PDF "Complete Guide to Building Skills for Claude"
- ⚪ 可选：agentskills.io 开放标准
- ⚪ 单独 deep-read `skills/pdf/SKILL.md`（本文唯一具体例）

### 11. 对用户（vfan）的启示

**短期（本周）**：
1. **回填理解层**：整套 Skills wiki 知识链从 source 到实施现在齐了。值得回头读 [[agent-skills-standard]] / [[anthropic-skill-creator]] / [[anthropics-skills-repo]] / [[skillify-meta-skill]]，对照本篇看每个观点的源头
2. **用 4 步方法论审视 `/ingest`**：evaluation-first 吗？name+description 触发率高吗？有没有需要 bundle 的 deterministic 代码？iterate with Claude 是否有渠道？
3. **加 in-task capture 习惯**：每次重要任务结束前问"如果让你把这次写进 skill，你会加什么？"——zero-friction 把任务变成 skill 升级

**中期（接下来 2-4 周）**：
1. **写中文文章"Anthropic 怎么定义 Skills"**：从这篇 2025-10-16 奠基文出发，串到 docs spec → Garry → Anthropic skill-creator → Matt Pocock → Khairallah。**这条时间线在中文圈不存在**
2. **把 LoreAI glossary generator 做成正经 skill**：参考 PDF skill 结构
3. **试 in-task iterate**：每次 `/ingest` 后让 Claude 反思 skill 改进——验证 zero-overhead 优化方式

**长期**：
1. **Anthropic 自己说的终局是"agent 自己写/改/评估 skills"**——你已经在做的事和终局对齐。**早一步做的事，2-3 年后会是主流认知**
2. **bilingual 套利**：把"Anthropic Skills 设计哲学溯源"做中文系列。中文圈对这条时间线几乎空白

### 12. 一句话总结

**"Skills 是给 agent 写'新员工手册'的方式——progressive disclosure 三层让上下文'实际上无限'，bundled 代码处理确定性部分，最终 agent 自己学会写自己的 skill。"**

或更短：**"Onboarding guide for new hires，但收件人是 LLM。"**

---

## Pages Updated
- [[agent-skills-standard]] — 加 onboarding-guide 类比 + effectively unbounded 哲学 + PDF skill 范例 + 原始 4 步方法论
- [[skillify-meta-skill]] — 加"agents create/edit/evaluate Skills on their own"愿景作为 /skillify 的官方种子
- [[anthropic-skill-creator]] — 标注其 "Iterate with Claude" 是本文方法论的实施化版本
- [[latent-vs-deterministic]] — 加 "sorting via token vs algorithm" 官方例
- [[anthropic]] — 注册本文为 Anthropic 关于 Skills 的奠基文献
- [[index]], [[log]]

## Connections
- Related: [[agent-skills-standard]], [[anthropic-skill-creator]], [[anthropics-skills-repo]], [[skillify-meta-skill]], [[latent-vs-deterministic]], [[llm-judgment-vs-scripts]], [[anthropic]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-05-22 | raw/2026-05-22-anthropic-equipping-agents-skills-blog.md | Initial creation — full 12-section study guide for Anthropic's foundational Skills announcement (2025-10-16) |
