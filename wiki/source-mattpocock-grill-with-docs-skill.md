---
type: source-summary
created: 2026-05-17
last-updated: 2026-05-17
sources:
  - raw/2026-05-17-mattpocock-grill-with-docs-skill.md
tags: [wiki, source, claude-code, skill, ddd]
---

# Source: /grill-with-docs SKILL.md (mattpocock/skills)

## Summary
The actual SKILL.md file for `/grill-with-docs` — Matt's keystone skill. Combines an interactive grilling session with DDD-style ubiquitous language documentation (CONTEXT.md + ADRs).

## 要点解读

### 1. 一次问一个问题 —— 强制同步对话节奏
SKILL.md 第一条规则：`Ask the questions one at a time, waiting for feedback on each question before continuing`。这避免了 agent 一次抛出一堆问题（用户看到一墙文字直接放弃）。**为什么重要：**人脑同时处理多个嵌套决策容易出错；一次一个问题强制每个决策都有明确答案。**实操建议：**写自己的 grilling skill 时一定要加上这条，否则就退化成模糊的 spec 文档。

### 2. 优先 explore codebase, 而不是 ask user
`If a question can be answered by exploring the codebase, explore the codebase instead.` —— 这是减少用户摩擦的关键。如果你问"这个函数返回什么类型"——别问，去读代码。只问那些真正需要用户判断的设计决策。

### 3. CONTEXT.md 是 glossary, 不是 spec
明确规定：`CONTEXT.md should be totally devoid of implementation details. Do not treat CONTEXT.md as a spec, a scratch pad, or a repository for implementation decisions. It is a glossary and nothing else.` —— 这条原则非常严格。CONTEXT.md 是 ubiquitous language 字典：每个词的定义、与其他词的区分。**为什么严格：**一旦放进去实现细节，文档就会快速腐烂；保持纯字典属性它可以活很久。

### 4. ADR 三重门槛 —— 防止 ADR 泛滥
Architectural Decision Records 只有在 3 条都满足时才创建：
1. **Hard to reverse** —— 改回去成本很高
2. **Surprising without context** —— 未来读者会问"为什么这么做"
3. **Result of a real trade-off** —— 有真实备选方案，做了取舍

少了任何一条都不写。**为什么重要：**ADR 太多 = 没人读。三重门槛保证只有真正值得记录的决策被记录。

### 5. 多 bounded context 支持（CONTEXT-MAP.md 模式）
如果仓库有多个领域（如 ordering + billing），根目录放 CONTEXT-MAP.md，每个子目录放自己的 CONTEXT.md。这是 DDD 的 bounded context 原则的文件系统实现。**实操：**单体仓库一开始用单 CONTEXT.md 就够；规模化后再拆。

## Connections
- [[grill-with-docs]] (concept page)
- [[context-md-pattern]] (the file format)
- [[mattpocock-skills-library]]
- Related: [[sprint-contracts]], [[four-files-context-architecture]]

## Source Log
| Date | Action |
|------|--------|
| 2026-05-17 | Initial ingest of SKILL.md |
