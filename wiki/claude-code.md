---
type: entity
created: 2026-04-06
last-updated: 2026-04-15
sources:
  - raw/2026-04-06-claude-reviews-claude-overview.md
  - raw/2026-04-06-anthropic-harness-design-long-running-apps.md
  - raw/2026-04-07-repo-claude-memory-compiler.md
  - raw/2026-04-08-troyhua-claude-code-7-layers-memory.md
  - raw/2026-04-09-bcherny-claude-code-best-practices.md
  - raw/2026-04-09-rohit-harness-from-claude-code-leaks.md
  - raw/2026-04-09-claude-code-official-docs-best-practices.md
  - raw/claude-code-monitor-tool-docs-2026-04.md
  - raw/2026-04-15-anthropic-ralph-wiggum-plugin.md
  - raw/2026-04-15-anthropic-claude-code-sandboxing.md
  - raw/2026-04-16-anthropic-opus-4-7-announcement.md
tags: [wiki, product, tool, agentic]
---

# Claude Code

## Summary
[[Anthropic]]'s official CLI tool for agentic coding, created by [[boris-cherny|Boris Cherny]]. 55 directories, 331 modules. Internally structured around six foundational pillars: System Prompt, Tool System, Query Loop, Context Management, Multi-Agent Coordination, and Security & Permissions. Embodies the [[harness-design]] principle: "LLM as reasoning center; Harness provides perception, action, memory, and constraints."

## Details
- **Six Pillars of Architecture:**
  1. **System Prompt** — Identity, rules, 42+ tool descriptions
  2. **Tool System** — 42 integrated modules, 30+ methods each
  3. **[[query-loop]]** — 12-step state machine driving agentic iteration
  4. **[[context-management]]** — 7-layer memory architecture; context window treated as "scarcest resource"
  5. **[[multi-agent-architecture|Multi-Agent Coordination]]** — Distributed task execution
  6. **[[permission-system|Security & Permissions]]** — Seven-layer defense-in-depth architecture
- **Notable Engineering Patterns:**
  - "35-line Store" — React 19 `useSyncExternalStore` replaces Redux for state management
  - "Fork Ink" — Custom terminal rendering engine with proper event handling
  - "Leaf Module Pattern" — Isolates bootstrap code, prevents circular dependencies via ESLint
- **Scale:** 17-chapter analysis (8,600+ lines), 6 learning tracks (core loop, security, multi-agent, infrastructure, UI, operations)
- Used as the harness in [[harness-design]] experiments — the evaluator agent uses Playwright MCP through Claude Code
- **Hook system extensibility:** [[claude-memory-compiler]] uses SessionEnd, PreCompact, and SessionStart hooks for [[zero-friction-capture]] — demonstrates hooks as the integration point for persistent memory. 26 hook event types, 4 handler types (command, http, prompt, agent).
- **Claude Agent SDK:** Companion to Claude Code — runs LLM operations programmatically. Used by [[claude-memory-compiler]] for background knowledge extraction. Covered under existing Claude subscription.
- **Key internal systems revealed by [[troy-hua]]'s reverse-engineering:**
  - **[[session-memory]]** — Forked subagent continuously maintains structured notes; when compaction needed, summary already exists (no API call)
  - **[[dreaming]]** — Background cross-session memory consolidation, modeled after biological sleep. 4-phase process with PID-based locking
  - **[[forked-agent-pattern]]** — Foundation for all background operations. Isolated context with cloned state, but shares prompt cache prefix
  - **[[prompt-cache-optimization]]** — Obsessive cache preservation across all systems. Cache hit vs miss at 200K = $0.003 vs $0.60
- **Creator's workflow** ([[boris-cherny]]):
  - Runs 5+ parallel sessions + Plan mode → auto-accept for one-shot execution
  - Slash commands for every daily workflow (`.claude/commands/`), committed to git
  - Subagents for focused tasks (code-simplifier, verify-app)
  - Chrome extension for frontend verification — "give Claude a way to verify its work"
  - Voice input (`/voice`) — "I do most of my coding by speaking to Claude"
  - Team invests heavily in shared CLAUDE.md: "After every correction, update CLAUDE.md"
- **[[infrastructure-layer]]** — Beyond harness: multi-tenancy, RBAC, state persistence, distributed coordination. "Where products die."
- **Agent loop architecture** (Rohit): `async function*` generator in `query.ts` (1,729 lines) — streaming, cancellation, composability, backpressure. 5-phase iteration per turn. Dependency injection via QueryDeps makes it testable.
- **Streaming tool executor:** Tools start executing mid-stream before the model finishes generating. 2-5s latency savings per multi-tool turn. Tool concurrency classification: read-only parallel (up to 10), write serial.
- **823-line retry system:** Per-error-class recovery (429, 529, 400, 401, network). Error recovery is a first-class state in the loop, not outer try-catch.
- **4 extensibility mechanisms:** Skills (markdown, replaces Commands), Hooks (26 events, 4 handler types), MCP (3 transports: HTTP/SSE/stdio, 3 scopes), Plugins (composition)
- **Session mobility:** `/teleport` (cloud→terminal), `/remote-control` (phone→local CLI), Cowork Dispatch (mobile→Desktop app)
- **Automation features:** `/loop` (recurring tasks), `/schedule` (cloud cron), `/batch` (parallel worktree changes), `/branch` (fork conversation), `/btw` (side queries)
- **[[claude-code-monitor-tool|Monitor tool]]** (v2.1.98, April 9 2026): Event-driven background monitoring — runs a shell command whose stdout wakes the session. Replaces polling with event-driven automation. Two patterns: stream filters (`tail -f | grep --line-buffered`) and poll-and-if loops. Zero token cost when idle. Not available on Bedrock/Vertex/Foundry.
- **Input modes:** `/voice` (push-to-talk, 20 languages), Chrome extension (live debugging, GIF recording), `--bare` (10x faster headless startup)
- **[[ralph-wiggum|Ralph Wiggum]] plugin** (Dec 2025): Official autonomous loop implementation using Stop hook architecture. `/ralph-loop` starts the loop, `/cancel-ralph` stops it. Plugin intercepts exit attempts and feeds same prompt back — loop runs inside the session without external bash scripts. Formalized by [[boris-cherny]]. Community debate: bash loop (fresh context per iteration) vs Stop hook (same session) — see [[ralph-wiggum#Two Implementations]].
- **[[claude-code-sandboxing|Native sandboxing]]**: OS-level filesystem + network isolation using Seatbelt (macOS) / bubblewrap (Linux). Reduces permission prompts by 84%. Two modes: auto-allow (best for autonomous/AFK) and regular permissions. Docker sandboxes (`docker sandbox run claude`) provide maximum isolation for AFK [[ralph-wiggum|Ralph]] loops. Open-sourced as `@anthropic-ai/sandbox-runtime`.
- **`/ultrareview` command** (2026-04-16, shipped with [[claude-opus-4-7]]): dedicated code-review session, Pro/Max subscribers get 3 free per month. Official "AI code review" as first-class primitive — pairs naturally with [[ralph-wiggum|Ralph]] loops (generate → ultrareview → fix). Max tier also gets extended auto mode.

## Connections
- Related: [[Anthropic]], [[boris-cherny]], [[harness-design]], [[query-loop]], [[context-management]], [[permission-system]], [[multi-agent-architecture]], [[claude-memory-compiler]], [[zero-friction-capture]], [[session-memory]], [[dreaming]], [[forked-agent-pattern]], [[prompt-cache-optimization]], [[infrastructure-layer]], [[troy-hua]], [[claude-code-monitor-tool]], [[ralph-wiggum]], [[claude-code-sandboxing]], [[geoffrey-huntley]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-06 | raw/2026-04-06-claude-reviews-claude-overview.md | Initial creation — full architecture from 17-chapter analysis |
| 2026-04-06 | raw/2026-04-06-anthropic-harness-design-long-running-apps.md | Context from harness design usage |
| 2026-04-07 | raw/2026-04-07-repo-claude-memory-compiler.md | Added hook system extensibility, Agent SDK |
| 2026-04-08 | raw/2026-04-08-troyhua-claude-code-7-layers-memory.md | Added session memory, dreaming, forked agent pattern, prompt cache optimization |
| 2026-04-09 | raw/2026-04-09-bcherny-claude-code-best-practices.md | Added Boris Cherny as creator, team practices, hidden features |
| 2026-04-09 | raw/2026-04-09-rohit-harness-from-claude-code-leaks.md | Added async generator loop, streaming tool executor, 823-line retry, infrastructure layer |
| 2026-04-09 | raw/2026-04-09-claude-code-official-docs-best-practices.md | Corrected hook count (26), added session mobility, automation features, input modes |
| 2026-04-11 | raw/claude-code-monitor-tool-docs-2026-04.md | Added Monitor tool — event-driven background monitoring |
| 2026-04-15 | raw/2026-04-15-anthropic-ralph-wiggum-plugin.md | Added Ralph Wiggum plugin — Stop hook autonomous loop |
| 2026-04-15 | raw/2026-04-15-anthropic-claude-code-sandboxing.md | Added native sandboxing — OS-level isolation for autonomous coding |
| 2026-04-17 | raw/2026-04-16-anthropic-opus-4-7-announcement.md | Added `/ultrareview` command shipped with Opus 4.7 |
