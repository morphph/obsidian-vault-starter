---
type: concept
created: 2026-04-06
last-updated: 2026-04-16
sources:
  - raw/2026-04-06-claude-reviews-claude-overview.md
  - raw/2026-04-06-anthropic-harness-design-long-running-apps.md
  - raw/2026-04-07-anatomy-of-agent-harness.md
  - raw/2026-04-08-troyhua-claude-code-7-layers-memory.md
  - raw/2026-04-16-thariq-claude-code-session-management-1m.md
tags: [wiki, architecture, agentic]
---

# Context Management

## Summary
The system for handling LLM context window limits in [[claude-code|Claude Code]]. Uses a **7-layer memory architecture** spanning from sub-millisecond token pruning to multi-hour background "dreaming" consolidation. Each layer is progressively more expensive but more powerful, designed so **Layer N prevents Layer N+1 from firing**. Treats the context window as the "scarcest resource." Directly addresses [[context-anxiety]].

> [!note] Layer count varies by source
> Official Anthropic docs don't use numbered layers — they describe two memory systems (CLAUDE.md + auto memory). The "7-layer" breakdown here comes from [[troy-hua]]'s reverse-engineering of Claude Code internals (135K-view analysis). Earlier sources like "Claude Reviews Claude" counted 4 layers at a coarser granularity. Other community analyses count 3 or 5. All describe the same system at different zoom levels.

## Details

### The 7 Layers

| Layer | Name | Cost | When |
|-------|------|------|------|
| 1 | **Tool Result Storage** | Disk I/O only | Every tool result, immediately |
| 2 | **Microcompaction** | Zero to minimal | Every turn, before API call |
| 3 | **[[session-memory]]** | One forked agent call | Periodically (post-sampling hook) |
| 4 | **Full Compaction** | One full API call | Context exceeds threshold, session memory unavailable |
| 5 | **Auto Memory Extraction** | One forked agent call | End of each complete query loop |
| 6 | **[[dreaming]]** | One forked agent call (multi-turn) | Background, after sufficient time + sessions |
| 7 | **Cross-Agent Communication** | Varies | Agent spawning, background tasks, coordination |

### Layer 1: Tool Result Storage
- Large tool results (grep 100KB+, file reads 50KB+) written to disk, only a ~2KB preview enters context
- Decisions frozen in `ContentReplacementState` — same result gets same preview on every API call, preserving [[prompt-cache-optimization|prompt cache]] hits
- Per-tool thresholds remotely tunable via GrowthBook feature flags

### Layer 2: Microcompaction
Three distinct mechanisms:
- **Time-based:** After 1h idle, clears old tool results (prompt cache expired anyway, so no cost to rewriting)
- **Cached microcompact:** Uses `cache_edits` API to delete tool results from server-side cache without invalidating the prefix — most technically interesting
- **API-level:** `context_management` parameter tells the server to handle clearing natively

Only these tools' results get cleared: FileRead, Bash/Shell, Grep, Glob, WebSearch, WebFetch, FileEdit, FileWrite. MCP tool results are never cleared.

### Layer 3: Session Memory
See [[session-memory]] — continuously maintains structured notes about the conversation. When compaction is needed, the summary already exists (no API call).

### Layer 4: Full Compaction
- Triggers when context exceeds `effective_window - 13K` and session memory compaction unavailable
- **Circuit breaker:** 3 consecutive failures → stops for rest of session. Added after discovering 250K wasted API calls/day globally from runaway retry loops
- 9-section summary with `<analysis>` scratchpad (stripped before entering context)
- Post-compact: re-injects top 5 recently-read files, skills, plans, deferred tools, re-runs SessionStart hooks

### Layer 5: Auto Memory Extraction
- Builds durable cross-session knowledge in `~/.claude/projects/<path>/memory/`
- Four memory types: user, feedback, project, reference
- Mutually exclusive with main agent — if main agent already wrote memories this turn, extraction skipped
- MEMORY.md index: hard limit 200 lines / 25KB

### Layer 6: Dreaming
See [[dreaming]] — cross-session memory consolidation running in background. 4-phase process (orient → gather → consolidate → prune).

### Layer 7: Cross-Agent Communication
- [[forked-agent-pattern]] underpins all background operations
- Agent tool for spawning sub-agents, SendMessage for inter-agent messaging
- Routing: in-process (queue), process-based (file mailbox), cross-session (bridge/UDS)

### Design Principles
- **Layered defense, cheapest first** — each layer prevents the next from firing
- **[[prompt-cache-optimization|Prompt cache preservation]]** — extraordinary lengths to keep API prefixes byte-identical
- **Isolation with sharing** — forked agents get cloned state but share cache prefix
- **Circuit breakers everywhere** — 3-strike compaction, 10-min dream throttle, PID mutex, sequential wrappers
- **Graceful degradation** — each layer fails silently, next layer catches
- **Feature flags as kill switches** — nearly every system gated by GrowthBook

### Context Thresholds
- Default context window: 1M tokens (upgraded April 2026; previously 200K expandable with `[1m]` suffix)
- Effective window: context window - 20K (reserved for compaction output)
- Autocompact threshold: effective window - 13K
- Token estimation: 4 bytes/token (text), 2 bytes/token (JSON), 2K flat (images)

### Mitigation strategies (from harness design research)
- Context resets (clear + restart with structured handoffs) — better for [[claude-model-family|Claude Sonnet 4.5]]
- Automatic compaction — works for Claude Opus 4.6
- The right strategy depends on model capability level

### Session Management with 1M Context (Thariq, Anthropic)
- **Every turn is a branching point** — after Claude finishes, you have 5 options: continue, rewind (`esc esc`), `/clear`, `/compact`, or spawn a subagent. Most users only continue; the other four are core context management.
- **Rewind is THE habit** — "If I had to pick one habit that signals good context management, it's rewind." Better than correction: instead of "that didn't work, try X" (which leaves failed attempt in context), rewind to before the attempt and re-prompt with learnings. Use "summarize from here" before rewind to capture learnings as a handoff message.
- **Compact vs Clear**:
  - `/compact` = let Claude decide what matters (lossy, can steer with instructions: `/compact focus on auth, drop test debugging`)
  - `/clear` = you decide what matters (write your own brief, start fresh — precise but more work)
- **Bad compact root cause**: Model can't predict your next direction + context rot means model is at its least intelligent when compacting. Solution: proactively compact while context is healthy, with direction description.
- **Subagents as context management**: Fresh context window isolates intermediate output. Mental test: "Will I need the tool output again, or just the conclusion?" Three patterns: verify work against spec, research another codebase then implement, write docs from git changes.
- **1M context = more time to intervene proactively**, not unlimited space. New task → new session. Related tasks → keep session (avoids re-reading files). Long session → proactive compact with direction.

### Additional insights (from Pachaar/Chawla)
- **Performance impact:** Degrades 30%+ when key content falls in mid-window positions — prioritize beginning and end positioning
- **Four production strategies:** compaction (summarizing history), observation masking (hiding old outputs), just-in-time retrieval (dynamic loading), subagent delegation (condensed summaries)
- **Prompt construction:** hierarchical assembly — system prompt → tool definitions → memory files → conversation history → user message. Priority stacking keeps critical info accessible.

## Connections
- Related: [[claude-code]], [[context-anxiety]], [[query-loop]], [[claude-model-family]], [[session-memory]], [[dreaming]], [[forked-agent-pattern]], [[prompt-cache-optimization]], [[orchestration-loop]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-06 | raw/2026-04-06-claude-reviews-claude-overview.md | Initial creation — four-layer compression system |
| 2026-04-06 | raw/2026-04-06-anthropic-harness-design-long-running-apps.md | Added mitigation strategies from harness design research |
| 2026-04-07 | raw/2026-04-07-anatomy-of-agent-harness.md | Added 30% degradation stat, 4 strategies, prompt construction hierarchy |
| 2026-04-08 | raw/2026-04-08-troyhua-claude-code-7-layers-memory.md | Major upgrade: 4 layers → 7 layers with full technical breakdown |
| 2026-04-16 | raw/2026-04-16-thariq-claude-code-session-management-1m.md | Added session management strategies: 5 branching options, rewind, compact vs clear, bad compact analysis |
