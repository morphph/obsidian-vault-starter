---
type: concept
created: 2026-04-07
last-updated: 2026-04-07
sources:
  - raw/2026-04-07-repo-claude-memory-compiler.md
tags: [wiki, harness-engineering, pattern]
---

# Zero-Friction Capture

## Summary
Design pattern where knowledge capture happens automatically without user action. The user never has to "stop and write things down" — the harness captures, extracts, and files knowledge as a side effect of normal work. Critical for builders who are in flow state and won't interrupt themselves to journal.

## Details
- **The problem:** Manual capture (like /build-log or /log) requires the user to pause, context-switch, and describe what they learned. Most people abandon this within weeks.
- **The solution:** Hook-based automatic extraction. Claude Code hooks (SessionEnd, PreCompact) fire without user action.
- **Key architecture:** Fast hook (local I/O only, <10s) → spawns detached background process → LLM extraction (slow, uses Agent SDK)
- **Why separate hook from extraction:** Hooks must return fast or Claude Code blocks. LLM extraction takes 10-30s. Solution: hook writes context to temp file, spawns background process, exits immediately.
- **Recursion prevention:** Background process sets `CLAUDE_INVOKED_BY` env var. Hooks check this and exit if set. Prevents: hook → Agent SDK → Claude Code → hook → infinite loop.
- **Deduplication:** Track session_id + timestamp, skip if same session flushed within 60 seconds (prevents duplicate captures from PreCompact + SessionEnd).
- **PreCompact is essential:** Long sessions trigger multiple auto-compactions. Without PreCompact hook, intermediate insights are lost to summarization before SessionEnd fires.
- Implemented in [[claude-memory-compiler]]

## Connections
- Related: [[harness-design]], [[claude-code]], [[claude-memory-compiler]], [[time-gated-compilation]]
- Solves the friction problem that killed the old /build-log command in this vault

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-07 | raw/2026-04-07-repo-claude-memory-compiler.md | Initial creation |
