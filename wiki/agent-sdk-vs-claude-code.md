---
type: concept
created: 2026-04-07
last-updated: 2026-04-07
sources:
  - raw/2026-04-07-repo-claude-memory-compiler.md
tags: [wiki, harness-engineering, pattern]
---

# Agent SDK vs Claude Code CLI

## Summary
Claude Code CLI is the interactive tool for humans. Claude Agent SDK is the programmatic interface for code. The decision rule: if a task needs real-time human interaction, use CLI. If it's "unattended" (no human in the loop), use Agent SDK.

## Details
- **Claude Code CLI**: Interactive terminal session. Human types, Claude responds. Has hooks, skills, slash commands, permission prompts. Requires a live session.
- **Claude Agent SDK**: Python library. You give it a prompt + tool permissions, it returns results. Runs headless — no terminal, no user interaction needed. Uses same Claude subscription credits.
- **Why the distinction matters for hooks**: Hooks must complete in <10 seconds, but LLM extraction is slow (30-60s). Solution: hook does fast local I/O, spawns a background Python process, exits. The background process uses Agent SDK (not CLI) because Claude Code is already closed when it runs.
- **Key pattern**: `hook (fast) → spawn detached process → Agent SDK (slow, headless)`

## When to Use Each

| Scenario | Use | Why |
|----------|-----|-----|
| Manual ingest, query, lint | CLI (/ingest, /query, /lint) | Interactive — you're in the loop |
| Background knowledge flush from hooks | Agent SDK (flush.py) | Headless — Claude Code already closed |
| Time-gated auto-compilation | Agent SDK (script) | Unattended — runs on schedule |
| Auto lint weekly | Agent SDK (script) | Unattended — no human needed |
| Telegram bot content extraction | Agent SDK | Unattended — bot receives, processes, saves |
| Weekly knowledge digest report | Agent SDK | Unattended — generates and sends |
| RSS feed filtering | Agent SDK | Unattended — LLM judges relevance |
| Connection discovery during compile | Agent SDK (compile.py) | Unattended — finds cross-concept bridges |

## Connections
- Related: [[claude-code]], [[claude-memory-compiler]], [[zero-friction-capture]], [[harness-design]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-07 | raw/2026-04-07-repo-claude-memory-compiler.md | Initial creation from repo analysis + discussion |
