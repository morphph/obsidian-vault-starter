---
type: draft
status: practice-guide
created: 2026-05-17
last-updated: 2026-05-17
target-audience: vfan (personal practice first, blog after validation)
source-policy: only Matt Pocock's own published material (his GitHub repos, AI Hero blog, his own X posts) — no third-party walkthroughs or community extensions
based-on:
  - wiki/idea-to-afk-agent-flow.md
  - wiki/mattpocock-skills-library.md
  - wiki/sandcastle.md
  - wiki/grill-with-docs.md
  - raw/2026-05-17-mattpocock-*.md
  - raw/2026-05-17-aihero-*.md
  - raw/2026-05-17-repo-mattpocock-*.md
tags: [drafts, practice-guide, afk, matt-pocock, chinese]
---

# Matt Pocock 的 Idea→AFK Agent 流程详解（中文实操指南）

> 📌 **使用说明**：这是你个人的 practice guide，不是发表文章。先按此跑通一次，验证有效后再演化成博客。
>
> 🔍 **来源纯度政策**：本文档**只引用 Matt Pocock 本人的官方源**——他的 GitHub 仓库（mattpocock/skills, mattpocock/sandcastle）、他的 AI Hero 博客（即他自己的网站）、他本人的 X 推文。第三方解读和社区扩展（如 Amplitude、Tessmann、Alexander Gekov、Aditya Puri 等）已经从 ingest 中清除，本文档不引用。
>
> 配套 wiki 索引页：[[idea-to-afk-agent-flow]]（英文 reference）

## 核心洞察

如果只记一句话：**你不应该直接写 AFK agent**。

绝大多数人一听到"自主执行的 agent"就开始想"我要写一个 loop 跑 prompt"——结果就是 loop 跑了一晚上，醒来发现 commit 了 50 个垃圾文件。

Matt 的方法论的精髓是：**从想法到 AFK 之间有 5 个不能跳的步骤**（他的 chapter creator 推文里完整呈现了这 5 步）。每一步都让 prompt 离"可以无人值守"更近一点。真正的 AFK 不是入口，而是奖励——是 prompt 通过前 4 步收敛后才给的。

---

## 5 个阶段

### Phase 0 — 前置条件

开始前你需要：

1. 在目标 repo 里跑 `npx skills@latest add mattpocock/skills` → 然后 `/setup-matt-pocock-skills`（一次性配好 issue tracker、triage label、文档位置）
2. 仓库根目录有 `CLAUDE.md` / `AGENTS.md`（项目级规则）
3. 至少一个 sandbox 选项（Docker Desktop 或 Podman，本地最常用；并行多 agent 用 Vercel Firecracker）
4. `npm install --save-dev @ai-hero/sandcastle && npx sandcastle init`（如果你要用 Matt 的 AFK 框架）

**给 vfan 的建议**：你的 obsidian-vault-starter 不需要 sandbox（不是 coding 项目），但 LoreAI / blog2video 应该把 Sandcastle 装上。

---

### Phase 1 — Discovery（用 /grill-with-docs 探查需求）

**Source**：Matt 的 `mattpocock/skills` 仓库里 `skills/engineering/grill-with-docs/SKILL.md`（他自己写的 skill）；他自己 AI Hero 站上的 "Ubiquitous Language → /grill-with-docs" 文章。

**目标**：把"我想要 X"（模糊愿望）变成"agent 可以照着做的 spec"。

**机制**（直接来自 Matt 的 SKILL.md）：
- 调用 `/grill-with-docs`（编程类）或 `/grill-me`（非编程类）
- Agent **一次问一个问题**，每个问题给一个推荐答案
- 如果问题可以**从代码里找答案**，agent 自己去探查，不问你
- 你回答后 agent 立即更新 `CONTEXT.md`（如果有新词被定下来）
- 重大决策符合**三重门槛**（难逆转 + 没上下文会奇怪 + 真的有 trade-off），agent 才提议写 ADR
- 预期 16–50 个问题（来自 Matt 的 AI Hero "5 Agent Skills" 文章），30–90 分钟

**产出 3 件东西**：
1. 你脑中清晰的 plan
2. 更新后的 `CONTEXT.md`（项目专属词汇表）
3. 可能的新 ADR（在 `docs/adr/`）

**关键纪律**（Matt 在 SKILL.md 明确写）：`CONTEXT.md` **只能是词汇表**，绝对不能放实现细节、spec、笔记。引用原文："CONTEXT.md should be totally devoid of implementation details. Do not treat CONTEXT.md as a spec, a scratch pad, or a repository for implementation decisions. It is a glossary and nothing else."

**Matt 给的具体例子**（来自他的 mattpocock/skills README）：
- **BEFORE**: "There's a problem when a lesson inside a section of a course is made 'real' (i.e. given a spot in the file system)"
- **AFTER**: "There's a problem with the materialization cascade"

**为什么这一步不能跳**：你以为你知道你要什么，但 16–50 个澄清问题会让你发现至少 5 个没想清楚的关键决策。skip 这一步，AFK agent 会把这 5 个决策猜错，你回来要返工。

---

### Phase 2 — Prompt Prototyping（草拟"给 AFK agent 的 prompt"）

**Source**：Matt 的 chapter creator X 推文 step 3。

**目标**：写出 v0 版本的 system prompt，它最终会驱动 AFK agent。

**机制**（直接来自 Matt 推文原话）：
- 对 agent 说一个关键句：**"let's prototype the prompt I'll eventually pass to the AFK agent"**（Matt 原话："let's prototype the prompt passed to the agent"）
- 这个措辞很重要——你在告诉它"我要的是 prompt 本身作为产物"，不是要它直接做这个任务
- Matt 推文原话："not really knowing what to expect" —— 不预设具体形态，让 agent 推断你需要什么 dev infrastructure
- Agent 会按 Phase 1 的 plan 写 prompt 草稿
- 同时定义两件事：
  - **Completion signal**：agent 完成所有任务后输出的字符串（Sandcastle 默认 `<promise>COMPLETE</promise>`）
  - **Verification**："完成"是什么样的？怎么判断？

**产出**：v0 prompt 文件 + 明确的退出条件 + 明确的验证标准

---

### Phase 3 — Live-Data Interactive Surface（让 agent 给你建一个调试 UI）

**Source**：Matt 的 chapter creator X 推文 step 4；Matt 的 mattpocock/skills 仓库里的 `/prototype` skill。

**目标**：搭一个一次性的调试界面，能用你**真实的生产数据**跑 prompt 看输出。

**机制**：
- Matt 的 `/prototype` skill 描述（原文）：*"Build a throwaway prototype to flesh out a design — either a runnable terminal app for state/business-logic questions, or several radically different UI variations toggleable from one route."*
- Matt 推文 step 4：agent 给他建了一个 TUI（用 EffectTS），指向他的真实数据
- 这个 UI 指向你**真实**的数据（不是 mock 数据）
- 你能看到：每条真实输入 → prompt → 真实输出
- 这个 UI 是一次性的，prompt 调好就扔掉

**为什么用 TUI 而不是 HTML**：dev loop 里 terminal 更快，prompt iteration 不需要好看的 UI。

**实操选择**：根据数据类型选；视觉/版面输出用 HTML，文本/状态/列表用 TUI。

---

### Phase 4 — System Prompt Iteration（迭代到收敛）

**Source**：Matt 的 chapter creator X 推文 step 5 ("I iterated on the system prompt until it was awesome")；Matt 的 `/tdd` skill。

**目标**：让 prompt 的输出可靠到可以无人值守跑。

**3 种迭代模式**（基于 Matt 的 TDD 哲学综合）：
1. **Failure-driven**：找一个输出差的真实输入，加一条规则到 prompt
2. **Edge-case driven**：脑暴可能的难案例，测试，修
3. **Voice-driven**：调整 tone / style（最主观，最难量化）

**两种验证策略**：
- **机器可验证的任务**（如代码、JSON 输出）：用 Matt 的 `/tdd` skill——red-green-refactor，先写 test 再实现
- **主观任务**（如内容创作）：用 Matt 推文里的"until it's awesome"——靠你自己的品味判断

**停止条件**：你愿意让这个 prompt 整晚无人值守跑。如果想到要 24 小时盯着，就还没到。

---

### Phase 5 — AFK Handoff（交给自主 agent）

**Source**：Matt 的 mattpocock/sandcastle 仓库 README 和 API 文档。

**目标**：把收敛后的 prompt 推到生产，agent 自己跑。

**两种规模选择**（来自 Sandcastle API）：

#### 选项 A — 单次 one-shot（Matt 的 chapter creator 用的）
```typescript
import { run, claudeCode } from "@ai-hero/sandcastle";
import { docker } from "@ai-hero/sandcastle/sandboxes/docker";

await run({
  agent: claudeCode("claude-opus-4-7"),
  sandbox: docker(),
  promptFile: ".sandcastle/prompt.md",
  completionSignal: "<promise>COMPLETE</promise>",
  idleTimeoutSeconds: 600,
});
```

适合：scope 清晰、一次完成的任务（如"处理所有视频，生成 chapters"）。

#### 选项 B — Continuous loop（Sandcastle 的 `maxIterations`）
```typescript
await run({
  agent: claudeCode("claude-opus-4-7"),
  sandbox: docker(),
  promptFile: ".sandcastle/prompt.md",
  maxIterations: 20,
  completionSignal: "<promise>COMPLETE</promise>",
});
```
适合：backlog 里有多个任务，agent 自己挑下一个做。

---

## 关键 Pattern：Interactive → AFK Escalation

**Source**：Matt 的 mattpocock/sandcastle 仓库的 `createWorktree()` API。

Sandcastle 的 `createWorktree()` API 把这个升级路径做成代码：
```typescript
await using wt = await createWorktree({
  branchStrategy: { type: "branch", branch: "agent/feature-x" }
});

// 第一阶段：人工驱动的交互会话（Phase 1-4）
await wt.interactive({
  agent: claudeCode("claude-opus-4-7"),
  prompt: "Let's design this together"
});

// 第二阶段：同一个 worktree 现在交给 AFK agent（Phase 5）
await wt.run({
  agent: claudeCode("claude-opus-4-7"),
  sandbox: docker(),
  prompt: "Implement",
  maxIterations: 3
});
```

**别跳过 interactive 阶段**，这是 prompt 收敛的地方。Sandcastle 的 API 设计本身就是 Matt 把"interactive→AFK 升级"模式硬编码进框架的证据。

---

## 实操 Checklist（给你立即可执行）

### Setup（一次性）
- [ ] 选一个目标 repo（建议从 LoreAI 或 blog2video 开始，因为它们已经在生产）
- [ ] `cd` 到该 repo，跑 `npx skills@latest add mattpocock/skills`
- [ ] 启动 Claude Code，跑 `/setup-matt-pocock-skills`
- [ ] 装 Sandcastle：`npm install --save-dev @ai-hero/sandcastle && npx sandcastle init`
- [ ] 配 `.sandcastle/.env` 里的 `ANTHROPIC_API_KEY`
- [ ] 确认 Docker Desktop 在跑（或装 Podman）

### 第一个 AFK 流程（建议从小任务开始）
**选题建议**：选一个**你能清晰说清"done"是什么样的**、**有真实数据可测**、**做错不致命**的任务。例子：
- LoreAI：自动给现有 glossary 词条补 FAQ section
- blog2video：自动给某类文章生成 chapter markers（**这正是 Matt 在推文里做的同一个任务**，方法论可以 1:1 复制）
- 任何项目：自动给 untested 函数补 unit tests

**6 步实操**：
- [ ] **Phase 1**：跑 `/grill-with-docs <your idea>`，回答 30–50 个问题，写下 plan + CONTEXT.md
- [ ] **Phase 2**：对 agent 说"let's prototype the prompt I'll pass to the AFK agent"，得到 v0 prompt
- [ ] **Phase 3**：让 agent 给你建 TUI 或 HTML debugger，连真实数据
- [ ] **Phase 4**：迭代 prompt，跑 ≥10 条真实输入，每次失败就改 prompt
- [ ] **Phase 5**：prompt 移到 `.sandcastle/prompt.md`，配置 `sandcastle.run({ maxIterations })`，开跑
- [ ] **回来后**：review commits，merge 通过验证的

---

## 6 个最常见的坑（来自 Matt 的方法论 + 5-skill 闭环逻辑）

1. **跳过 Phase 1** — 直接说"帮我建 X"。你会多迭代 10 次。
2. **跳过 Phase 3** — 不用真实数据直接跑 AFK loop。输出会无声降质。Matt 推文 step 3-4 明确证明必须先有 live-data prototype。
3. **没定义 completion signal** — agent 跑到 timeout 才结束，不知道自己什么时候完成。Sandcastle 默认 `<promise>COMPLETE</promise>`，要在 prompt 里要求 agent 输出这个。
4. **没 verification gate** — agent 标记"done"但实际没验证。用 Matt 的 `/tdd` skill 强制 test pass 才算完成。
5. **把 CONTEXT.md 当 spec 用** — 2 周就腐烂。强制只能放 glossary entries。引用 Matt SKILL.md 原文："It is a glossary and nothing else."
6. **HITL/AFK 不分** — 把需要 taste 的工作（如 UX 文案、API 设计）丢进 loop，agent 会自信地输出垃圾。用 Matt 的 `/to-issues` skill 给每个 issue 打标签。

---

## 给你（vfan）的具体建议

基于你的情况（Singapore growth marketer + AI content builder, LoreAI + blog2video, 偏好零摩擦自动化）：

### 短期（本周）
- 选 **blog2video 的 chapter 生成**作为第一个 AFK 实验——这正是 Matt 在 tweet 里做的同一个任务，方法论可以 1:1 复制
- 不需要先学完所有 5 个 skill，先掌握 `/grill-with-docs` + Sandcastle 这两个
- 第一次跑只用 Phase 1-4，先不上 Phase 5——熟悉了再 AFK

### 中期（接下来 2-4 周）
- 把 Matt 5-skill 闭环（grill → to-prd → to-issues → tdd → improve-architecture）跑通一个完整 feature
- 给 LoreAI 也走一遍同样流程，比较两个项目的差异

### 长期（成功后）
- 你说"如果 work 了就写博客"——那篇博客的角度可以是：
  - **创作者视角**：把 Matt 的 engineering-focused 方法论翻译成内容创作者能用的版本
  - **bilingual 套利**：中文圈对这套方法论几乎没覆盖，是先发优势
  - **具体案例**：用你自己的 blog2video / LoreAI 实验作为 case study，比抽象方法论可信 10 倍

---

## 配套资料（全部 Matt 官方）

**Wiki 索引**：
- 主索引：[[idea-to-afk-agent-flow]]（英文结构化 reference）
- 关键概念：[[grill-with-docs]] · [[sandcastle]] · [[mattpocock-skills-library]] · [[hitl-vs-afk-classification]] · [[vertical-slicing]] · [[context-md-pattern]]
- 人物：[[matt-pocock]]
- 关联：[[ralph-wiggum]]（社区起源；Matt 的方法论建立在此之上但不等同）

**Matt 官方外部资料**（已 ingest）：
- [mattpocock/skills](https://github.com/mattpocock/skills) — 87K⭐ Matt 自己的 skills repo
- [mattpocock/sandcastle](https://github.com/mattpocock/sandcastle) — 4.5K⭐ Matt 自己的 AFK 框架
- [/grill-with-docs SKILL.md](https://github.com/mattpocock/skills/blob/main/skills/engineering/grill-with-docs/SKILL.md) — Matt 写的实际 skill
- [AI Hero: Skills Changelog](https://www.aihero.dev/skills-changelog-ubiquitous-language-grill-with-docs) — Matt 自己的博客
- [AI Hero: 5 Agent Skills I Use Every Day](https://www.aihero.dev/5-agent-skills-i-use-every-day) — Matt 自己的博客
- Matt 的 chapter creator X 推文（截图，原 URL 未保留）

**已删除的第三方源**（防止以后混淆）：
- ~~Amplitude blog (102 features case study)~~ — 第三方营销内容
- ~~Meag Tessmann Medium (Agent Teams + Ralph hybrid)~~ — 独立社区实验
- ~~Alexander Gekov DEV.to (2026 year of Ralph)~~ — 综述类二手内容
- ~~Aditya Puri Medium (5 skills walkthrough)~~ — 第三方解读
