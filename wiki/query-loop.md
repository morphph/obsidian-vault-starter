---
type: concept
created: 2026-04-06
last-updated: 2026-04-09
sources:
  - raw/2026-04-06-claude-reviews-claude-overview.md
  - raw/2026-04-07-anatomy-of-agent-harness.md
  - raw/2026-04-09-rohit-harness-from-claude-code-leaks.md
tags: [wiki, architecture, agentic]
---

# Query Loop

## Summary
The core execution engine of [[claude-code|Claude Code]] — an **async generator** (`async function*`) in `query.ts` (1,729 lines) that drives agentic iteration. Not a naive "LLM in a while loop" but a streaming, cancellable, composable state machine with 5 phases per iteration and first-class error recovery.

## Details
- One of the six foundational pillars of Claude Code architecture
- Works in concert with [[context-management]] to handle long-running sessions
- Claude Code's query loop is an implementation of the broader [[orchestration-loop]] (TAO cycle) pattern — Anthropic calls it a "dumb loop" where intelligence lives in the model

### Why Async Generator, Not While Loop
The `async function*` signature gives 5 properties that a while loop lacks:
1. **Streaming** — yields `StreamEvent` objects as tokens arrive. Users see the model working character by character.
2. **Cancellation** — caller stops calling `.next()`. `AbortSignal` threaded through every layer.
3. **Composability** — REPL UI, sub-agents, and tests all consume the same generator. One function, three callers, zero duplication.
4. **Backpressure** — generator pauses when consumer stops pulling. Memory stays bounded in long sessions.
5. **Error recovery inside the loop** — each phase knows what can go wrong.

### 5 Phases Per Iteration
1. **Setup** — apply tool result budgets, run compaction strategies, validate token counts
2. **Model Invocation** — call `queryModelWithStreaming()` via dependency-injected `QueryDeps` interface. **Streaming tool executor starts executing tools during this phase** before model finishes generating.
3. **Error Recovery & Compaction** — prompt-too-long? compact and retry. max_output_tokens? escalate 32K→64K. Context overflow? reactive compaction on media-heavy messages.
4. **Tool Execution** — tools not yet executed by streaming executor run here. Haiku generates tool use summaries asynchronously.
5. **Continuation Decision** — `stop_reason`, `maxTurns`, hooks, abort signals checked.

### Streaming Tool Executor
Most harnesses wait for model to finish before executing tools. Claude Code parses tool calls incrementally and **starts execution mid-stream** — the instant input JSON is complete.
- Hides 2-5 seconds of latency per multi-tool turn
- Per-tool `siblingAbortController` — tool failure kills siblings, not the parent query
- Stream fallback: if streaming fails, executor discards queued tools + generates synthetic error results
- Results yield in original order regardless of completion order

### Tool Concurrency Classification
- **Read-only** (Glob, Grep, Read, WebFetch): run concurrently, up to 10 in parallel
- **Write** (Bash with mutations, Edit, Write): run serially
- Orchestration in `toolOrchestration.ts` partitions calls into batches → 2-5x speedup, zero race conditions

### Dependency Injection
Loop receives dependencies through `QueryDeps` interface. Inject mock `callModel` → verify context overflow handling, tool failures, cancellation without API. "Most agent harnesses are untestable because they hardcode API calls into the loop."

### Tool Result Budgeting
- Each tool specifies `maxResultSizeChars`
- Exceeding results persist to disk, model gets preview + file path
- `applyToolResultBudget()` runs before each API call

## Connections
- Related: [[claude-code]], [[context-management]], [[harness-design]], [[orchestration-loop]], [[prompt-cache-optimization]], [[forked-agent-pattern]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-06 | raw/2026-04-06-claude-reviews-claude-overview.md | Initial creation |
| 2026-04-07 | raw/2026-04-07-anatomy-of-agent-harness.md | Added TAO cycle context, 7-step breakdown, "dumb loop" philosophy |
| 2026-04-09 | raw/2026-04-09-rohit-harness-from-claude-code-leaks.md | Major: async generator pattern, 5-phase iteration, streaming tool executor, DI, tool concurrency |
