---
type: source-summary
created: 2026-05-10
last-updated: 2026-05-10
sources:
  - raw/2026-04-30-thariq-prompt-caching-is-everything.md
tags: [wiki, source, claude-code, prompt-cache, anthropic]
---

# Source: Thariq — Lessons from Building Claude Code: Prompt Caching is Everything

## Summary
**Anthropic engineering blog post** by [[thariq|Thariq Shihipar]] (Claude Code team), 2026-04-30. Third Thariq longform in our wiki (after [[source-thariq-session-management-1m|Session Management]] and [[source-thariq-html-effectiveness|HTML Effectiveness]]). Operational deep-dive on prompt caching as the central architecture concern of Claude Code: prefix matching, the four-layer ordering rule, `<system-reminder>` as cache-preserving update mechanism, `defer_loading` for MCP tools, [[plan-mode-as-tools|Plan Mode as tools]] (not as prompt rewrites), cache-safe forking for compaction, and **SEV-level alerting on cache hit rate**.

## Source
- **URL:** https://claude.com/blog/lessons-from-building-claude-code-prompt-caching-is-everything
- **Posted:** 2026-04-30
- **Author:** Thariq Shihipar (Member of Technical Staff, Claude Code team)
- **Format:** ~1,500-word engineering blog post
- **Fetch method:** WebFetch (static content, single redirect)

## 要点解读

### 1. **核心论断：cache 不是优化，是 agent 的物理学**
开篇引用工程界老话 "cache rules everything around me"，然后下了一个非常重的判断：
> "**At Claude Code, we build our entire harness around prompt caching.** A high prompt cache hit rate decreases costs and helps us create more generous rate limits for our subscription plans, **so we run alerts on our prompt cache hit rate and declare SEVs if they're too low.**"

关键信号：**Anthropic 内部把 cache hit rate 当 SLO 来看待，掉了就是事故（SEV）**。这跟我们之前 [[prompt-cache-optimization]] 已经讲的"200x 成本差"是同一回事，但提升到了**运营级别的 first-class 关注**。

对 builder 的启示：如果你建 long-running agentic 产品，cache hit rate 应该是和 uptime / latency 同级的核心指标，不是工程师内部的二级关注。

### 2. **四层 prompt 排序规则 —— 这是被低估的硬规则**
官方明确给出 Claude Code 的 prompt layout：
> 1. **Static system prompt & Tools**（globally cached —— 跨所有用户、所有 session 共享）
> 2. **CLAUDE.md**（cached within a project）
> 3. **Session context**（cached within a session）
> 4. **Conversation messages**

Static-first 原则。**最大化 prefix 共享率。**

更有价值的是 Thariq 列了团队**踩过的坑**：
- 在 static system prompt 里塞了精确到秒的 timestamp → 每次都 miss
- tool order 排序非确定 → cache 漂移
- 改了 tool 的 parameters（比如 Agent tool 能 call 的子 agent 列表）→ 整段 invalidate

**对本 vault 的启示：** 我们 `.claude/commands/` 现在是按字母排序的，工具描述是静态的，CLAUDE.md 是稳定的。这都是好的。但如果未来加了动态 tool 配置（比如根据当前 wiki 状态调整某 command 的可用性），就要警惕这条。

### 3. **`<system-reminder>` —— 用 message 而不是 system prompt 传更新**
最实用的工程模式（这个我之前没特意 highlight）：
> "It may be tempting to update the prompt, but that would result in a cache miss... In Claude Code, **we add a `<system-reminder>` tag in the next user message or tool result with the updated information for the model**, which helps preserve the cache."

**这就是为什么 Claude Code 系统提示里反复出现 `<system-reminder>` 标签** —— 它不是装饰，是**用 user message 通道注入"伪 system 信息"的 cache 友好做法**。

通用规则：**任何时变信息（时间戳、文件状态、用户偏好变化）都应该走 message 通道，不走 system prompt 通道。**

### 4. **Plan Mode 作为 tool —— 非常优雅的设计模式**
全文最反直觉、最有迁移价值的一段。直觉做法：用户按 Plan Mode → harness 把 tool set 过滤成只读 → cache miss。

Claude Code 团队的做法：**tool set 永不变。** `EnterPlanMode` 和 `ExitPlanMode` 自己就是 tool。用户切换 plan mode 时，下一轮 user message 里加一段 system reminder："你现在在 plan mode，去探索别改文件，做完调用 ExitPlanMode。"

为什么这个比"过滤 tool"更好（除了 cache）：
> "Because EnterPlanMode is a tool the model can call itself, **it can autonomously enter plan mode when it detects a hard problem**, without any cache break."

Tool-as-state 让模型自己也能控制状态，不只是 harness 单向控制。

**通用原则（我新建了 [[plan-mode-as-tools]] 概念页抓住这个）：**
> **State transitions belong in tool calls, not in prompt rewrites.**
> 永远不要为了表达"模式切换"而改 tool set / system prompt。改成一个**改变行为而不是改变能力**的 tool 调用。

这是 Liskov-style 的 agent 设计规则：**capability surface 不能在 conversation 中段变窄**。

### 5. **`defer_loading` —— 兼顾大量 MCP tools 与 cache 稳定**
具体的 API 参数披露：
> "Instead of removing tools, we send lightweight stubs (just the tool name, with **`defer_loading: true`**) that the model can 'discover' via tool search when needed. The full tool schemas are only loaded when the model selects them."

**为什么这条对本 vault 重要：** 我们的 `.claude/commands/` 已经接近 10 个 slash command，每个 description 又长又详细。如果将来 wiki 里有 MCP servers 集成（比如 [[claude-managed-agents]] 时代），可能需要类似机制。这条是 future-proofing 的工程参考。

### 6. **Compaction 的 cache-safe forking —— 一个反直觉的成本陷阱**
天真做法：context 满了 → 起一个新 API call，system prompt 写"summarize this"，把 conversation 全塞进去 → **整段 conversation 走 uncached rate**。
> "The longer the conversation (i.e., the more you need compaction in the first place), **the more expensive that one call becomes**."

正确做法：
> "We use the **exact same** system prompt, user context, system context, and tool definitions as the parent conversation. We prepend the parent's conversation messages, then append the compaction prompt as a new user message at the end."

副作用：需要预留 **compaction buffer** —— context window 里要留够空间装 compaction prompt + summary output。

**关键教训：** 任何"side computation"（compaction / summarization / skill execution）都必须 piggyback parent 的 prefix。差一个 token 就全失效。

### 7. **不要 mid-session 切换模型**
> "If you're 100k tokens into a conversation with Opus and want to ask a question that is fairly easy to answer, **it would actually be more expensive to switch to Haiku than to have Opus answer**, because we would need to rebuild the prompt cache for Haiku."

如果非要切：用 sub-agent。Opus 准备 hand-off message → Haiku 起新 session 处理。Claude Code 的 Explore agents 就是这么用 Haiku 的。

**这条澄清了一个常见误解：** 想"用便宜模型省钱"经常是错的，因为 cache 的成本结构。Opus 答 100K token 的简单问题（cache hit）可能比 Haiku 答（cache miss + 重建 prefix）还便宜。

## 5 个总结性 lessons（直接引用）

1. **Prompt caching is a prefix match.** Any change anywhere in the prefix invalidates everything after it. Design your entire system around this constraint.

2. **Use messages instead of system prompt changes.** Insert time-varying info via `<system-reminder>` in user messages.

3. **Don't change tools or models mid-conversation.** Use tools to model state transitions (Plan Mode pattern). Defer tool loading instead of removing.

4. **Monitor your cache hit rate like you monitor uptime.** We alert on cache breaks and treat them as incidents.

5. **Fork operations need to share the parent's prefix.** Compaction, summarization, skill execution — all must use identical cache-safe parameters.

## Pages created from this source
- [[plan-mode-as-tools]] — concept (state-as-tool-call design pattern)
- [[source-thariq-prompt-caching-is-everything]] — this page

## Pages updated from this source
- [[prompt-cache-optimization]] — major expansion: 4-layer ordering rule, `<system-reminder>` mechanism, `defer_loading`, cache-safe compaction forking, SEV-level cache hit rate alerting, model-swap caveat
- [[thariq]] — added third article (third Anthropic-team contribution)
- [[claude-code]] — Plan Mode as tools, defer_loading, compaction buffer
- [[index]], [[log]] — added new pages

## Connections
- Related: [[plan-mode-as-tools]], [[prompt-cache-optimization]], [[thariq]], [[claude-code]], [[forked-agent-pattern]], [[context-management]], [[session-memory]], [[anthropic]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-05-10 | raw/2026-04-30-thariq-prompt-caching-is-everything.md | Initial creation |
