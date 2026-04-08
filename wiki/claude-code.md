---
type: entity
created: 2026-04-06
last-updated: 2026-04-08
sources:
  - raw/2026-04-06-claude-reviews-claude-overview.md
  - raw/2026-04-06-anthropic-harness-design-long-running-apps.md
  - raw/2026-04-07-repo-claude-memory-compiler.md
  - raw/2026-04-08-troyhua-claude-code-7-layers-memory.md
tags: [wiki, product, tool, agentic]
---

# Claude Code

## Summary
[[Anthropic]]'s official CLI tool for agentic coding. Internally structured around six foundational pillars: System Prompt, Tool System, Query Loop, Context Management, Multi-Agent Coordination, and Security & Permissions. Embodies the [[harness-design]] principle: "LLM as reasoning center; Harness provides perception, action, memory, and constraints."

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
- **Hook system extensibility:** [[claude-memory-compiler]] uses SessionEnd, PreCompact, and SessionStart hooks for [[zero-friction-capture]] — demonstrates hooks as the integration point for persistent memory. 20 hook event types available.
- **Claude Agent SDK:** Companion to Claude Code — runs LLM operations programmatically. Used by [[claude-memory-compiler]] for background knowledge extraction. Covered under existing Claude subscription.
- **Key internal systems revealed by [[troy-hua]]'s reverse-engineering:**
  - **[[session-memory]]** — Forked subagent continuously maintains structured notes; when compaction needed, summary already exists (no API call)
  - **[[dreaming]]** — Background cross-session memory consolidation, modeled after biological sleep. 4-phase process with PID-based locking
  - **[[forked-agent-pattern]]** — Foundation for all background operations. Isolated context with cloned state, but shares prompt cache prefix
  - **[[prompt-cache-optimization]]** — Obsessive cache preservation across all systems. Cache hit vs miss at 200K = $0.003 vs $0.60

## Connections
- Related: [[Anthropic]], [[harness-design]], [[query-loop]], [[context-management]], [[permission-system]], [[multi-agent-architecture]], [[claude-memory-compiler]], [[zero-friction-capture]], [[session-memory]], [[dreaming]], [[forked-agent-pattern]], [[prompt-cache-optimization]], [[troy-hua]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-06 | raw/2026-04-06-claude-reviews-claude-overview.md | Initial creation — full architecture from 17-chapter analysis |
| 2026-04-06 | raw/2026-04-06-anthropic-harness-design-long-running-apps.md | Context from harness design usage |
| 2026-04-07 | raw/2026-04-07-repo-claude-memory-compiler.md | Added hook system extensibility, Agent SDK |
| 2026-04-08 | raw/2026-04-08-troyhua-claude-code-7-layers-memory.md | Added session memory, dreaming, forked agent pattern, prompt cache optimization |
