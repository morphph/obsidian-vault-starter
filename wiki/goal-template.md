---
type: concept
created: 2026-05-18
last-updated: 2026-05-18
sources:
  - raw/2026-05-17-nurijanian-goal-for-product-managers.md
tags: [wiki, concept, template, claude-code-goal, agent-design]
---

# Goal Template (6-Section Practical Template)

## Summary
[[george-nurijanian|George]] 在 [[source-nurijanian-goal-for-pms|/goal for PMs]] 给的实操模板，把 [[agent-ready-requirements|agent-ready requirements]] 落到可直接 copy-paste 给 `/goal` 命令的 markdown 形态。6 个 section：target / source of truth / acceptance criteria / validation / boundaries / loop behavior。每个 section 都是 agent 决策时必查的字段。

## Details

### 完整模板

```
/goal [specific target state]

Source of truth:
- read [spec file]
- follow [implementation plan]
- update [status file]

Acceptance criteria:
- [observable behavior 1]
- [observable behavior 2]
- [negative case]
- [non-regression condition]

Validation:
- [test command]
- [lint/typecheck/build command]
- [browser/visual/manual evidence if needed]

Boundaries:
- only edit [paths]
- do not change [systems]
- preserve [contract/data/API behavior]

Loop behavior:
- after each meaningful change, run the relevant validation
- update the status file with changed files, result, and remaining risk
- stop after [N turns/time] if blocked and report the blocker
```

### 每个 section 的角色

1. **/goal [target state]** —— **finish line** 一句话。loop 何时算成功的 north star
2. **Source of truth** —— **durable files**。loop 每个 turn 重新加载（不依赖 conversation memory）
3. **Acceptance criteria** —— **evaluable conditions**。evaluator 用这些判断是否完成
4. **Validation** —— **proof commands**。生成可被 agent 跑 + 输出可观测的证据
5. **Boundaries** —— **scope fence**。防止 agent 漫游到不相关代码
6. **Loop behavior** —— **operating protocol**。规定 status file 怎么写 + 何时 stop

### 5 个 "natural fit" 应用场景

George 明确说 `/goal` 在这 5 类任务上最强：

| 场景 | Goal 例子 |
|---|---|
| **Migration work** | `/goal migrate all imports from legacyAuth to authClient in app/auth. No legacyAuth imports remain. npm test -- auth exits 0. Stop after 15 turns.` |
| **Backlog clearing** | `/goal resolve every failing test marked @auth-regression. Each fix smallest production change. Do not delete tests. Update docs/status-auth.md after each.` |
| **File splitting** | `/goal split app/components/AccountSettings.tsx into modules under 250 lines. Behavior must stay same. Existing tests must pass. No module mixes billing / profile / notification.` |
| **Brute-force testing** | `/goal exhaust attack vectors / login flows / search cases / forms / permissions until queue empty.` |
| **Exploration（输出 bounded）** | `/goal explore three approaches for project search faster. For each: short note with complexity / risks / files / validation. Do not edit production code. Stop after producing docs/search-options.md` |

### Anti-pattern：用 exploration loop 跑 production work

George 明确警告：
> "The dangerous version is asking an exploratory loop to silently become a production loop."

Exploration goal 应该输出 **learning（notes / docs）**，不是 production code。混在一起 = 后悔莫及。

### 套用到 vfan 项目（blog2video chapter generator 例子）

```
/goal 给 raw/2026-05-18-source-article.md 生成 chapter markers

Source of truth:
- read docs/chapter-spec.md
- follow docs/chapter-implementation-plan.md
- update docs/status-chapters-{date}.md

Acceptance criteria:
- 每个 chapter 30-60 秒内容覆盖
- 每个 chapter 三段结构：hook + 论点 + 例证
- 最后 chapter 必须以 CTA 结尾
- 总长不超过文章总长 1/3
- negative case: 不允许出现 summary / overview 这类元描述

Validation:
- npm run test:chapter-format（格式检查）
- 人工抽查 3 段（论点完整性）

Boundaries:
- 只输出到 docs/output/chapters.md
- 不修改 raw/ 任何文件
- 不修改 docs/chapter-spec.md（spec 不是产物）

Loop behavior:
- 每生成一段验证一次
- 失败时记录到 status file，retry 一次
- 5 个 chapter 全过后 emit <promise>COMPLETE</promise>
- stop after 15 turns if blocked
```

### 跟其他模板的关系

- **[[mattpocock-skills-library|Matt Pocock 的 SKILL.md]]**：定义 agent **是什么**（持久角色）
- **本 goal template**：定义这次任务**做什么**（具体 run）
- **配合使用**：先建 SKILL.md 定义"你是 chapter generator"，再用 goal template 每次 invoke 时定义"这次给哪篇文章做"

### 跟 Khairallah 4-Component Contract 的兄弟关系

[[source-eng-khairallah-3-ai-hires|Khairallah 的 4-component contract]] (Role + Tools + Knowledge Base + Workflow) 是 **agent build-time spec**。
本 goal template 是 **agent run-time goal**。
两者配合：
- Khairallah 定义 "agent 是什么" + "怎么工作"
- George 定义 "这次跑 / 何时停 / 怎么验证完成"

## Connections
- 出处：[[source-nurijanian-goal-for-pms]]
- 作者：[[george-nurijanian]]
- 配对概念：[[agent-ready-requirements]]（写 spec 的标准）
- 相关命令：[[claude-code-goal]]
- 兄弟模式：[[source-eng-khairallah-3-ai-hires]] 的 4-component contract
- 替代方案 / 配合：[[mattpocock-skills-library]] SKILL.md, [[sandcastle]] promptFile
- 执行框架：[[sandcastle]]（落到代码）, [[ralph-wiggum]]（loop 哲学）
- 配套实操：[[agentic-loop-tracking-files]]（status file 详细模式）

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-05-18 | raw/2026-05-17-nurijanian-goal-for-product-managers.md | Initial creation — 6-section practical /goal template + 5 natural-fit scenarios |
