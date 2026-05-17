---
type: source-summary
created: 2026-05-17
last-updated: 2026-05-17
sources:
  - raw/2026-05-17-aihero-grill-with-docs-changelog.md
tags: [wiki, source, claude-code, ddd]
---

# Source: AI Hero — Skills Changelog: Ubiquitous Language → /grill-with-docs

## Summary
Matt Pocock's writeup of why he deprecated `/ubiquitous-language` and merged it into `/grill-with-docs`. The "why" doc behind the keystone skill.

## 要点解读

### 1. 为什么要合并而不是保留两个 skills
原来 `/ubiquitous-language` 是独立 skill，专门维护项目词汇表；`/grill-me` 是另一个 skill，做提问。Matt 发现两件事其实是同一件——你 grill 别人的时候，自然会发现需要新词或者要澄清旧词。如果分成两步，你要 grill 完再切到另一个 skill 写文档，断了上下文。合并后，一边问一边写，效率更高。

### 2. 单一 ubiquitous language 不符合现实
旧 skill 假设整个项目有一套词汇 —— 但真实系统通常有多个 bounded context（订单 vs 计费），每个 context 有自己的词汇。新 skill 支持每个 context 一个 CONTEXT.md + 根目录 CONTEXT-MAP.md。这是 Eric Evans DDD 的真实实现。**实操：**给团队仓库做 grill 之前，先想清楚有几个 bounded context。

### 3. Conway's Law 在 AI 时代的回响
系统架构反映组织沟通模式 —— 不同团队的 bounded context 自然发展出不同语言。这意味着 AI agent 必须能识别自己当前在哪个 context 工作，加载对应的 CONTEXT.md，否则就会用错词。

### 4. CONTEXT.md 给 agent 的 ROI
- **Token 节省：**用 "materialization cascade" 代替一段啰嗦解释
- **命名一致：**variables、files、functions 用 domain 词汇
- **更易导航：**agent 知道"customer" 在哪些文件出现
- **冲突早发现：**agent 说"我理解你说的 X 是 ubiquitous language 里的 Y"，立即对齐

### 5. 实操：grilling 后产出 3 件东西
1. 你脑中的清晰 plan
2. 更新后的 CONTEXT.md（新增或修正的词）
3. 可能新增的 ADR（如果决策符合三重门槛）

这 3 件东西就是接下来写实现 prompt 或者交给 AFK agent 的输入。

## Connections
- [[grill-with-docs]], [[context-md-pattern]], [[mattpocock-skills-library]]
- Related: [[idea-to-afk-agent-flow]] (Phase 1 of the runbook)

## Source Log
| Date | Action |
|------|--------|
| 2026-05-17 | Initial ingest |
