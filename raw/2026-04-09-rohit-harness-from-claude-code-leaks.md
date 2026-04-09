# How I Built Harness for My Agent Using Claude Code Leaks

**Source:** https://x.com/rohit4verse/status/2041548810804211936
**Author:** Rohit (@rohit4verse) — Engineer, FullStack + Applied AI, Agentic AI
**Published:** 2026-04-08
**Engagement:** 20 replies, 91 reposts, 752 likes, 2,403 bookmarks, 298K views
**Fetch method:** Playwright MCP (accessibility tree, focus mode)

---

Anthropic just taught you how to build the best AI agent harness.

Claude Code's source is sitting in the open: 55 directories, 331 modules, the most battle-tested agent architecture in production today. I pulled apart every file. Every architectural decision. Every retry path, every compaction strategy, every permission stage.

This is not a teardown. It is a blueprint.

Here is every principle inside it, and how you use each one to build your own harness that survives production.

## What Claude Code's Architecture Reveals About the Industry's Favorite Framework

You have heard the three layers: model weights, context, harness. The industry repeats them at every conference, in every tutorial, in every framework README.

- **Model Weights**: the frozen intelligence, the thing you call via API.
- **Context**: the prompt, the conversation history, the retrieved documents.
- **Harness**: the scaffolding around the model. Tools, loops, error handling.

The framing is correct as far as it goes. The SWE-agent paper from Princeton NLP showed a 64% relative improvement on SWE-bench by changing nothing but the interface design. Same GPT-4. Same tasks. Only the environment changed. Performance gains live in layers 2 and 3, not layer 1.

Then you open Claude Code's source and realise Anthropic is not building for the model. They are building for the system.

Inside Claude Code, a four-level CLAUDE.md hierarchy lets enterprise admins enforce policies via MDM, project maintainers set conventions, and individual developers override locally. A disk-backed task list with file-based locking keeps parallel sub-agents from corrupting each other's state. Git worktree isolation gives five agents five branches on the same repo with zero conflicts. A permission pipeline cascades deny rules from enterprise to project to user to session.

None of that is harness. None of that is context. None of that is weights.

That is **infrastructure**: multi-tenancy, RBAC, resource isolation, state persistence, distributed coordination.

**The real framework has four layers:**
1. **Model Weights**: frozen intelligence.
2. **Context**: runtime input.
3. **Harness**: the agent's designed environment.
4. **Infrastructure**: multi-tenancy, RBAC, resource isolation, state persistence, distributed coordination.

Most teams talk about the first three because they are interesting to think about. The fourth is where products die. Claude Code is the first agent system I have seen that takes all four seriously, and the architecture shows it at every level.

## The Core Agent Loop: An Async Generator, Not a While Loop

The heart of Claude Code lives in `query.ts`: 1,729 lines of TypeScript. The most important decision is in the function signature: `async function*`.

That `function*` carries more weight than it looks. An async generator yields values over time, pauses on demand, and lets any caller break out at any point.

An agent loop is not a request-response cycle. It is a long-running, streaming, cancellable process. The generator gives you all of those properties without bolting anything on.

Compare it to what most tutorials teach — a simple `while(true)` loop. This works in a tutorial. It collapses in production for five reasons:

1. **No streaming.** The user watches a blank screen for 10-30 seconds while the model generates. Claude Code's generator yields StreamEvent objects as tokens arrive. Users who can see what an agent is doing trust it more. Users who trust it give it more autonomy.

2. **No cancellation.** Ctrl+C in the while-loop version requires a separate abort mechanism wired in from outside. With a generator, the caller stops calling `.next()`. The finally block runs, cleanup happens. Claude Code threads AbortSignal through every layer.

3. **No composability.** The REPL UI consumes the generator. Sub-agents consume it. Tests consume it. One `query()` function, three callers, zero duplication.

4. **No backpressure.** If the model generates faster than the terminal renders, the while-loop buffers everything in memory. A generator pauses production when the consumer stops pulling.

5. **No error recovery inside the loop.** This is where it gets serious.

### Five Phases Per Iteration

Each iteration of Claude Code's agent loop runs through five phases:

**Phase 1: Setup.** Before calling the model, the loop applies tool result budgets, runs compaction strategies if the conversation is long, and validates token counts.

**Phase 2: Model Invocation.** The loop calls `queryModelWithStreaming()` through a dependency-injected interface, wrapped in a retry system that handles ten error classes. The streaming tool executor starts executing tools **during this phase**, before the model finishes generating.

**Phase 3: Error Recovery & Compaction.** The loop checks for recoverable errors after the model responds. prompt-too-long? Compact and retry. max_output_tokens hit? Escalate from 32K to 64K and retry. Context overflow? Run reactive compaction on media-heavy messages.

**Phase 4: Tool Execution.** Tools not yet executed by the streaming executor run here. Results yield to the UI as they complete. Haiku generates tool use summaries asynchronously so the main model does not burn tokens on bookkeeping.

**Phase 5: Continuation Decision.** The model's `stop_reason` tells the loop whether more tool calls are needed. The turn counter checks maxTurns. Hooks can request a stop. Abort signals are checked.

Error recovery lives inside the loop, not around it. Each phase knows what can go wrong and has a specific recovery path.

### Dependency Injection Makes It Testable

The loop receives its dependencies through a `QueryDeps` interface. Inject a mock `callModel` that yields predetermined events, and you can verify context overflow handling, tool failures, and cancellation without touching the real API. Most agent harnesses are untestable because they hardcode API calls into the loop. Claude Code's loop is a pure state machine with injected effects.

## Tool Execution: Why Concurrency Classification Changes Everything

Claude Code ships 45+ built-in tools. How they execute is the point.

Most harnesses run tools one by one or all in parallel. Claude Code **classifies every tool by concurrency behavior**:
- **Read-only tools** (Glob, Grep, Read, WebFetch) run concurrently, up to 10 in parallel
- **Write tools** (Bash with mutations, Edit, Write) run serially

The orchestration layer in `toolOrchestration.ts` partitions tool calls into batches. Speed of parallelism and safety of serial execution, at the same time. 2-5x speedup on multi-tool turns.

### The Streaming Tool Executor

Most harnesses wait for the model to finish generating before executing any tools. Claude Code starts execution mid-stream.

For a turn with three tool calls, that hides 2-5 seconds of latency. The model generates the description of its next step while the first tool already runs.

Hard cases handled:
- If a tool in a parallel batch fails, a per-tool `siblingAbortController` kills sibling processes. The parent query controller stays alive.
- If the stream fails and falls back to non-streaming, the executor discards queued tools and generates synthetic error results.
- Results yield in the original order even if tool 2 finishes before tool 1.

### Tool Result Budgeting

A Bash command that dumps 1MB of logs would fill the context window. Claude Code runs a budgeting system:
- Each tool specifies `maxResultSizeChars`
- Results exceeding the limit persist to disk
- The model receives a file path reference plus a preview
- `applyToolResultBudget()` runs before each API call

## Prompt Engineering at Scale: The System Prompt Is a Caching Problem

The system prompt is not a string. It is a structured array of sections with caching metadata.

The `SYSTEM_PROMPT_DYNAMIC_BOUNDARY` marker splits the prompt into two zones:
- **Above**: identical across all users, all sessions → hitting the prompt cache globally. ~80% of the prompt.
- **Below**: memoized (computed once per session) or volatile (recomputed every turn)

Volatile sections are minimized because each change breaks the cache for everything after it.

No agent tutorial or framework discusses designing the prompt for cache efficiency. At scale, this determines whether your agent costs $0.02 per session or $0.20.

### The CLAUDE.md Hierarchy

A four-level instruction hierarchy acts as composable memory:
1. Enterprise (`/etc/claude-code/CLAUDE.md`) — enforced via MDM
2. User (`~/.claude/CLAUDE.md`) — personal preferences
3. Project (`.claude/CLAUDE.md`) — team conventions
4. Local (`CLAUDE.local.md`) — private overrides

Higher levels override lower ones. An `@include` directive enables composition.

### Why Context Injection Lives Outside the System Prompt

User context (git status, CLAUDE.md contents, current date) is injected as the **first user message**, wrapped in `<system-reminder>` tags. Context changes every turn. Putting it in the system prompt would invalidate the cache. Moving it to a user message keeps the system prompt cache-stable turn after turn.

## Context Window Management: Four Compaction Strategies

Most harnesses truncate old messages or crash. Claude Code supports unlimited conversation length through four strategies, ordered cheapest to most expensive:

**Strategy 1: Microcompact** — Runs every turn. If a tool result has not changed since last call, replaces with cached reference. Cost: near zero.

**Strategy 2: Snip Compact** — Fires when approaching limits. Removes messages from beginning while preserving a "protected tail" of recent messages. No model call required. Lossy but fast.

**Strategy 3: Auto Compact** — Triggered when token usage crosses threshold and snip is insufficient. Separate model call summarizes prior conversation. Tracks compaction state to prevent loops.

**Strategy 4: Context Collapse** — For long-running sessions, via feature flag. Multi-phase staged compression: collapse tool results first, then thinking blocks, then entire sections. The expensive option.

Cheapest strategy runs first. Most expensive fires only when nothing else works.

## The Permission System: Seven Stages of Trust

Most harnesses ship a binary toggle: allow or deny. Claude Code runs a seven-stage pipeline.

Rules use glob-like pattern matching on tool name and input. "Allow git commands and npm test, prompt for everything else."

Permission modes create progressive trust:
- New users start in default, approving each action
- As confidence builds, they move to acceptEdits or bypassPermissions
- No binary choice between safety and speed. A spectrum.

Hooks serve as the escape hatch — your script receives tool call details and returns `{"decision": "approve"}` or `{"decision": "block"}`.

## Error Recovery: The 823-Line Retry System

`services/api/withRetry.ts` is 823 lines. Every line exists because of a production failure.

- **429 (Rate Limited):** Check Retry-After header. Under 20s? Retry, keep fast mode. Over 20s? Enter 30-min cooldown. overage-disabled? Permanently disable fast mode.
- **529 (Server Overloaded):** Track consecutive counts. Three in a row with fallback model? Switch models. Background task? Bail. Foreground? Retry with backoff.
- **400 (Context Overflow):** Parse error for token counts. Recalculate: available = limit - input - 1000 safety buffer. Minimum floor 3,000 output tokens.
- **401/403 (Auth):** Clear API key cache. Force-refresh OAuth tokens. Retry with new credentials.
- **Network Errors (ECONNRESET, EPIPE, timeout):** Disable keep-alive socket pooling. Retry with new connection.

Backoff formula: `delay = min(500ms × 2^attempt, 32s) + random(0, 0.25 × baseDelay)`

For unattended sessions (CI/CD, background agents): persistent retry mode, indefinite retries, max 5-min backoff, 6-hour reset cap, 30-second heartbeat emissions.

Streaming reliability: 90-second idle timeout watchdog, 45-second warning, 30-second stall detection, non-streaming fallback preserving retry state.

## Sub-Agent Architecture: Parallelism With Isolation

Claude Code spawns sub-agents: independent instances of the agent loop, each with own context, tools, and working directory.

Each sub-agent gets isolated context. Aborting parent cascades to children. But child cannot mutate parent's state. File state caches cloned to prevent cross-contamination.

### Git Worktree Isolation

Sub-agents that modify code get their own worktree:
- `getOrCreateWorktree(repoRoot, slug)` → validate → check existing → git fetch → git worktree add → symlink large dirs → copy config → return `{ path, branch, headCommit }`
- Node_modules symlinked, not copied. Five parallel agents don't need five copies.

### Three Spawn Backends

1. **In-process** (direct Node.js, fastest, shared memory)
2. **Tmux pane** (terminal multiplexer isolation, each agent visible)
3. **Remote** (CCR environment, full machine isolation)

Task coordination uses disk-backed task list with file-based locking at `~/.claude/tasks/<taskListId>/<taskId>.json`. Lock contention handled with exponential backoff (30 retries, 5-100ms).

## The Fourth Layer: Infrastructure

Everything above describes the harness. Layer 3. Now look at what Claude Code builds around it.

**Multi-Tenancy:** CLAUDE.md hierarchy = RBAC for agent behavior. Enterprise → Project → User → Local. Conflicts resolve deterministically.

**State Persistence Across Sessions:** Compaction → within-session. CLAUDE.md → across-sessions. Task list → across-agents.

**Resource Isolation:** Git worktrees per agent. siblingAbortController contains failures. Enterprise deny rules prevent unauthorized access.

**Distributed Coordination:** File-based locking on task list. Prompt cache sharing between parent/child. Heartbeat keepalives. Worktree management for concurrent repo access.

## Extensibility: Four Mechanisms, Zero Source Modifications

1. **Skills** (Markdown Files as Commands) — YAML frontmatter, 5 sources (bundled, project, user, plugin, MCP), path-based discovery
2. **Hooks** (Event-Driven Automation) — 6 types (shell, LLM eval, agentic verification, HTTP, TypeScript callbacks, in-memory), fires on PreToolUse, PostToolUse, SessionStart, FileChanged, Stop
3. **MCP** (Model Context Protocol) — 5 transport types (stdio, SSE, HTTP streaming, WebSocket, in-process), 3 config levels
4. **Plugins** — directories containing skills, agents, hooks, config. Top-level composition mechanism.

Principle: composition over modification. Extend by adding, not changing.

## The UI Is a Trust Mechanism

Custom fork of Ink (React for terminals): 251KB of rendering engine.

- Real-time streaming character by character
- Animated spinners interpolate from normal to error-red based on stall duration
- Diff rendering with syntax highlighting, 3 lines context, word-level markers
- Multi-agent status trees
- 6 themes including color-blind friendly
- Status line: model name, cost in USD, context %, rate limit %

Users who can see what an agent is doing give it more autonomy. More autonomy = more useful work. The UI is a force multiplier.

## What You Take From This

1. **Async generators for the agent loop.** Streaming, cancellation, composability, backpressure.
2. **Concurrency classification for tools.** Read-only parallel, write serial. 2-5x speedup.
3. **Tool execution during streaming.** Start execution the instant input JSON is complete.
4. **System prompt designed for the cache boundary.** Static first, dynamic last. Highest-leverage cost optimization.
5. **A compaction hierarchy, not a single strategy.** Cheap first, expensive last.
6. **Error recovery as first-class state in the loop.** Each error type gets its own recovery strategy.
7. **Layer 4 from day one.** State, permissions, coordination, isolation. Retrofitting is 10x harder.
8. **Extension points that require no code changes.** If users fork to customize, your architecture has a gap.

**The Model Is Commodity. The Environment Determines Outcomes.**

Princeton NLP proved it with SWE-agent: same model, better environment, 64% improvement. Anthropic proves it daily with Claude Code: a 55-directory, 331-module TypeScript application that turns the same Claude model into a coding agent that runs unattended for hours, recovers from API outages, manages its own context, and coordinates multiple parallel sub-agents.

Four layers. Most of the industry optimizes layer 1. The teams winning are investing in layers 3 and 4.
