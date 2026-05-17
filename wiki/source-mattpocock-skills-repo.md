---
type: source-summary
created: 2026-05-17
last-updated: 2026-05-17
sources:
  - raw/2026-05-17-repo-mattpocock-skills.md
tags: [wiki, source, claude-code, skills, matt-pocock]
---

# Source: mattpocock/skills (GitHub Deep Scan)

## Summary
Matt Pocock's open-sourced personal `.claude/` skills directory — 86,997 stars, 7,583 forks. "Skills for Real Engineers — not vibe coding." Distributed via `npx skills@latest add mattpocock/skills`.

## 要点解读

### 1. 整套 skills 的设计哲学：encode engineering fundamentals, not vibe coding
Matt 明确反对 GSD / BMAD / Spec-Kit 那种"自己拥有整个流程"的做法 —— 那些工具会拿走开发者的控制权，出 bug 时无从调试。他的 skills 设计原则是 **small, composable, model-agnostic**：每个 skill 只解决一个小问题，可以自由组合，不绑定特定模型。背后是几十年工程实践（DDD、XP、TDD、Pragmatic Programmer），把这些原则压缩成可重用的 prompt。**实操建议：复用他的 skills 时不要囫囵吞下整个流程，挑你当前痛点对应的那 1-2 个 skill 装上即可。**

### 2. 四大失败模式定义了 skill 的边界
Matt 把 AI coding 的失败归为 4 类：
- **Agent 没做我想要的** → 通信差（解：`/grill-me`, `/grill-with-docs`）
- **Agent 太啰嗦** → 没共同语言（解：CONTEXT.md ubiquitous language，内嵌在 `/grill-with-docs`）
- **代码跑不起来** → 缺反馈循环（解：`/tdd`, `/diagnose`）
- **写成了一坨泥** → 不投资设计（解：`/to-prd`, `/zoom-out`, `/improve-codebase-architecture`）

这个分类法本身就有价值——遇到 agent 出错时，先归类，再选 skill。

### 3. Engineering skills 都带 supporting MD 文件 —— progressive disclosure 实操样本
看文件树就能看出 Matt 的 skill 结构：每个核心 skill 不只有一个 SKILL.md，还配多个支持文档（如 `/tdd` 配了 deep-modules.md, interface-design.md, mocking.md, refactoring.md, tests.md）。这是 progressive disclosure 的实战模板——SKILL.md 简短描述触发条件，详细规则放在子文件里，agent 按需加载。**实操建议：写自己的 skill 时也用这个结构，不要把所有内容塞进一个 SKILL.md。**

### 4. `.out-of-scope/` 文件夹是治理创新
仓库根下有 `.out-of-scope/` 文件夹，专门放"我决定不做的功能 + 原因"。比如 `mainstream-issue-trackers-only.md` 解释为什么不支持 Jira。这是非常值得抄的治理模式——避免 issue 区反复讨论同一个被拒绝的功能。**实操建议：在你自己的 repo 加一个 `.out-of-scope/` 文件夹，记录被拒绝的功能。**

### 5. 完整工作流是 5 步闭环（核心订阅价值）
按使用顺序: `/grill-with-docs` → `/to-prd` → `/to-issues` → `/tdd` → `/improve-codebase-architecture`。每一步的输出是下一步的输入。第 5 步的反馈循环（架构清理 → 下次 grill 更好）是整条流水线持续工作的关键，跳过这一步流水线就会逐步腐烂。

## Connections
- [[mattpocock-skills-library]] (entity), [[matt-pocock]], [[grill-with-docs]], [[claude-code]]
- Related concepts: [[skill-as-method-call]], [[thin-harness-fat-skills]], [[agent-skills-standard]]

## Source Log
| Date | Action |
|------|--------|
| 2026-05-17 | Initial deep scan + ingest |
