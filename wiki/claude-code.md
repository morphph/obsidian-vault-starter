---
type: entity
created: 2026-04-06
last-updated: 2026-05-10
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
  - raw/2026-04-11-garry-tan-thin-harness-fat-skills.md
tags: [wiki, product, tool, agentic]
---

# Claude Code

## Summary
[[anthropic|Anthropic]]'s official CLI tool for agentic coding, created by [[boris-cherny|Boris Cherny]]. 55 directories, 331 modules. Internally structured around six foundational pillars: System Prompt, Tool System, Query Loop, Context Management, Multi-Agent Coordination, and Security & Permissions. Embodies the [[harness-design]] principle: "LLM as reasoning center; Harness provides perception, action, memory, and constraints."

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
- **2026-03-31 npm source leak**: Anthropic accidentally published the entire Claude Code source — 512,000 lines — to the npm registry. Read by [[garry-tan|Garry Tan]] and others; provided public confirmation that the [[harness-design|harness]] (live repo context, prompt cache, purpose-built tools, context bloat minimization, structured session memory, parallel sub-agents) is what produces the productivity gap, not the model. Catalyst for [[thin-harness-fat-skills]].
- **CLAUDE.md as resolver, not knowledge dump** ([[garry-tan]] case study): Garry's CLAUDE.md grew to 20,000 lines and degraded model attention so badly that Claude Code itself told him to cut it back. Fix was ~200 lines of pointers to documents — the [[resolvers|resolver]] pattern. Validates [[context-noise-governance]] and [[documentation-layers]] at the personal-config layer.
- **AutoDream as primitive self-healing resolver** ([[garry-tan]] 2026-04-15): Garry identifies Claude Code's [[dreaming|AutoDream]] memory-consolidation system as already a primitive version of a self-healing [[resolvers|resolver]] — it reviews accumulated context and compresses during idle time. Apply the same principle to the resolver specifically and you get a routing table that **improves with use** from observed task-dispatch traffic. See [[context-rot]] for the failure mode this defends against.
- **Agent Skills open standard** (2026-04-21 official docs): Claude Code skills follow the [[agent-skills-standard|Agent Skills standard]] at agentskills.io — **works across multiple AI tools**. Claude Code extends it with invocation control (`disable-model-invocation`, `user-invocable`), subagent execution (`context: fork`), and dynamic context injection (`` !`command` `` preprocessing). The `description` field is officially the resolver entry: *"Claude uses this to decide when to apply the skill."* Custom commands have been merged into skills — `.claude/commands/deploy.md` and `.claude/skills/deploy/SKILL.md` both create `/deploy`.
- **Skill description budget (the context-rot mechanism)**: Combined `description` + `when_to_use` is truncated at **1,536 characters per skill** in the listing. Total listing budget is **1% of the context window** (fallback 8,000 chars). If skills accumulate past this budget, descriptions get silently truncated and Claude can't see the trigger keywords → routing fails. Escape hatch: `SLASH_COMMAND_TOOL_CHAR_BUDGET` env var.
- **Skill invocation lifecycle**: When invoked, `SKILL.md` content enters the conversation as a single message and stays for the session. Claude Code does not re-read the file. Auto-compaction carries invoked skills forward within a 25K-token shared budget (5K per skill, most recent first). Older skills can be dropped entirely after compaction.
- **HTML as primary output format** ([[thariq]] 2026-05-08, 3.5M views): the Claude Code team itself is converging on **HTML over Markdown** for specs, plans, code reviews, reports — anything a human reads but doesn't edit. Drivers: (a) 100-line markdown threshold past which people stop reading; (b) Opus 4.7's 1M context makes HTML's 2-4× token cost negligible; (c) HTML's information density (CSS / SVG / interactive JS); (d) **output format as agent governance** — "I feel more in the loop with Claude" because HTML is actually read while markdown is skimmed. Companion pattern: [[throwaway-editors]] — single-purpose HTML files purpose-built for one task with a copy-as-prompt export. See [[html-as-output-format]].
- **Cache hit rate as SLO** ([[thariq]] 2026-04-30, official Anthropic engineering blog): the Claude Code team **declares SEVs when prompt cache hit rate drops too low** — cache health is operationalized like uptime, not optimized like a perf metric. The harness is "built around prompt caching from day one." See [[prompt-cache-optimization]] for the 4-layer ordering rule + production cache-break bug catalog.
- **Plan Mode is implemented as tools** ([[plan-mode-as-tools]]): the tool set never changes when the user toggles Plan Mode. `EnterPlanMode` and `ExitPlanMode` are themselves tools; the mode is communicated via `<system-reminder>` in the next user message. **This preserves cache** AND **lets the model autonomously enter Plan Mode when it detects a hard problem**. Generalizable: state transitions belong in tool calls, not prompt rewrites.
- **`defer_loading: true` for MCP tools**: lightweight stubs (tool name only) keep the cached prefix stable; full schemas load via tool search when the model selects them. Solves the "dozens of MCP tools" problem without removing tools mid-conversation (which would invalidate cache).
- **Compaction is cache-safe forking**: when context fills, Claude Code uses the *exact same* system prompt, user context, and tool definitions as the parent — appends only the compaction prompt as a new user message. The parent's prefix is reused. Requires reserving a **compaction buffer** (room for compact message + summary output) before triggering. Now exposed as a primitive in Anthropic's API.

## Connections
- Related: [[anthropic|Anthropic]], [[boris-cherny]], [[harness-design]], [[query-loop]], [[context-management]], [[permission-system]], [[multi-agent-architecture]], [[claude-memory-compiler]], [[zero-friction-capture]], [[session-memory]], [[dreaming]], [[forked-agent-pattern]], [[prompt-cache-optimization]], [[infrastructure-layer]], [[troy-hua]], [[claude-code-monitor-tool]], [[ralph-wiggum]], [[claude-code-sandboxing]], [[geoffrey-huntley]], [[garry-tan]], [[thin-harness-fat-skills]], [[resolvers]]

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
| 2026-04-19 | raw/2026-04-11-garry-tan-thin-harness-fat-skills.md | Added 3/31/2026 npm source leak event and CLAUDE.md 20K→200 resolver case study |
| 2026-04-19 | raw/2026-04-15-garry-tan-resolvers-routing-table-for-intelligence.md | Noted AutoDream as primitive self-healing resolver; links to context-rot |
| 2026-04-21 | raw/2026-04-21-anthropic-agent-skills-docs.md | Added Agent Skills open standard; 1,536-char description cap + 1% context-window budget + SLASH_COMMAND_TOOL_CHAR_BUDGET; skill invocation lifecycle (single message, 25K compaction budget) |
| 2026-05-09 | raw/2026-05-08-thariq-unreasonable-effectiveness-of-html.md | Added HTML-as-output-format insight (Claude Code team converging on HTML > Markdown for plans/specs/reviews); throwaway editors as companion pattern |
| 2026-05-10 | raw/2026-04-30-thariq-prompt-caching-is-everything.md | Added cache-hit-rate-as-SLO; Plan Mode as tools design pattern; `defer_loading` for MCP; compaction as cache-safe forking + compaction buffer requirement |
