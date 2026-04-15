---
type: source-summary
created: 2026-04-15
last-updated: 2026-04-15
sources:
  - raw/2026-04-15-repo-ralph-orchestrator.md
tags: [wiki, source]
---

# Source: Ralph Orchestrator (GitHub Deep Scan)

## Summary
Mikey O'Brien's production-grade Rust implementation of the [[ralph-wiggum]] technique (2,702 stars). Multi-backend orchestration with hat system, parallel loops, waves, Telegram HITL, web dashboard, and MCP server. Codifies the "Ralph Tenets" as architectural principles.

## Source Details
- **URL**: https://github.com/mikeyobrien/ralph-orchestrator
- **Author**: Mikey O'Brien
- **Stars**: 2,702
- **Language**: Rust (edition 2024) | Version 2.9.2
- **Type**: GitHub repository

## Key Claims
1. Hat system enables lightweight multi-agent coordination through event bus
2. Wave pattern (scatter-gather) breaks "one thing per loop" for parallelizable work
3. Telegram HITL (RObot) = third mode between pure HITL and AFK
4. Parallel loops via git worktrees with merge queue coordination
5. 7+ AI backend support (Claude, Gemini, Codex, Kiro, Amp, Copilot, OpenCode, Roo)
6. Six Ralph Tenets codified from [[geoffrey-huntley]]'s philosophy
7. Anti-patterns: don't build features agents can handle, no complex retry logic, no step-by-step prescriptions

## Pages Created
- [[ralph-orchestrator]] — Entity page with full architecture details

## Pages Updated
- [[ralph-wiggum]] — Added Ralph Orchestrator as production implementation
- [[harness-design]] — Added ralph-orchestrator reference

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-15 | raw/2026-04-15-repo-ralph-orchestrator.md | Initial creation |
