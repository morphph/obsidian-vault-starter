---
type: source-summary
created: 2026-05-17
last-updated: 2026-05-17
sources:
  - raw/2026-05-17-amplitude-ralph-loop-102-features.md
tags: [wiki, source, ralph, case-study, dispatcher]
---

# Source: Amplitude — What I Learned Pointing a Ralph Loop at My Product for a Week

## Summary
Empirical case study: Claude Code + browser use + Amplitude's Opportunity Finder shipped **102 features in 7 days** to a ski-touring app, each with a browser-recorded GIF as verification.

## 要点解读

### 1. Loop 本身不重要，dispatcher 和 verification gate 才重要
这是文章最强的一点。`while true; do agent; done` 谁都会写——它本身只是引擎。真正决定产出质量的是：
- **Dispatcher**（Opportunity Finder）：从分析数据、session 录屏、客户反馈、agent traces、竞品差距里排序出"接下来该做什么"
- **Verification gate**（browser GIF）：每个 feature 必须录制 GIF 证明端到端能用

没有这两件，loop 就是无意义的算力消耗。**实操建议：**你要做 AFK loop 时，先想清楚 dispatcher（任务从哪来？怎么排序？）和 verification（怎么证明做完了？），再写 loop 代码。

### 2. Self-instrumentation 让 loop 有了"记忆"
Agent 自己接入 Amplitude 事件、session replay、自定义指标。每个 feature 上线即开始上报。下一轮 loop 不再从假设出发，而是从行为证据出发。**为什么这是 game-changer：**没 telemetry 的 loop 每轮都从同一个起点（mode collapse）；有 telemetry 的 loop 会逐步偏好那些真正有效果的 feature 形态——这是真的 learning，不是 vibes。

### 3. Browser verification 抓到的 bug 是 unit test 抓不到的
Claude Code 真的去点击新建的 feature，录 GIF。这种合成流量暴露了：handler 错位、form 提交错误、state update 没生效。这些都是 unit test 无法捕获的集成层 bug。**实操：**每个 AFK feature 加 Playwright/Chrome MCP 的"自己点一遍"步骤，并保存 artifact。

### 4. Auto-merge policy 是 risk gradient
- **小 UI 加法 + 明确成功指标** → auto-merge
- **触碰数据** → 总是人工 gate

这是务实的 risk 管理：80% 的低风险变更自动 ship，20% 高风险变更人工 review。**实操建议：**给你的 PR 类型打标签，定义清楚哪类可以 auto-merge，避免一刀切的"全部人工 review"或"全部自动 merge"。

### 5. 最关键的洞察：execution 变得 abundant，瓶颈转向 taste
当 1 周能 ship 102 个 feature，建得快不再是优势——**选什么建、判断哪个真有效**才是稀缺的。人的角色从"写代码"变成"判断哪些 opportunity 值得做，哪些 shipped feature 真的移动了指标"。**对个人创作者的启示：**你的瓶颈也会从"产能"变成"品味"和"选题"。提前思考这件事——什么是你的 Opportunity Finder？什么是你的成功指标？

## Connections
- [[ralph-wiggum]] (evolved with dispatcher pattern)
- [[opportunity-finder-pattern]] (new concept page)
- [[verification-loops]], [[silent-fallback-antipattern]]
- [[idea-to-afk-agent-flow]] (case study for Phase 5 at scale)

## Source Log
| Date | Action |
|------|--------|
| 2026-05-17 | Initial ingest |
