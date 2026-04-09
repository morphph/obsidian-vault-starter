---
type: concept
created: 2026-04-09
last-updated: 2026-04-09
sources:
  - raw/2026-04-09-rohit-harness-from-claude-code-leaks.md
tags: [wiki, architecture, agentic]
---

# Infrastructure Layer

## Summary
The "4th layer" of agent systems, beyond the commonly cited three (model weights, context, harness). Infrastructure encompasses multi-tenancy, RBAC, resource isolation, state persistence, and distributed coordination. Rohit (@rohit4verse) argues this is "where products die" — Claude Code is the first agent system that takes all four layers seriously.

## Details
- **The standard 3-layer model:** Model Weights → Context → Harness
- **The missing 4th layer:** Infrastructure — everything needed to run agents in production with multiple users, sessions, and environments
- **Princeton NLP's SWE-agent proof:** Same GPT-4, better environment design → 64% improvement. Performance gains live in layers 3 and 4, not layer 1.

### What Infrastructure Includes (from Claude Code)
- **Multi-tenancy:** CLAUDE.md 4-level hierarchy = RBAC for agent behavior (Enterprise → Project → User → Local). Conflicts resolve deterministically.
- **State persistence across sessions:** Compaction (within-session), CLAUDE.md (across-sessions), task list (across-agents)
- **Resource isolation:** Git worktrees per agent, `siblingAbortController` contains failures, enterprise deny rules
- **Distributed coordination:** File-based locking on task list (30 retries, 5-100ms backoff), prompt cache sharing parent↔child, heartbeat keepalives, worktree management for concurrent repo access

### Why It Matters
- "Most teams talk about the first three layers because they are interesting to think about. The fourth is where products die."
- "Distributed systems engineering is becoming a core competency for agent builders"
- Retrofitting infrastructure is 10x harder than designing for it from day one
- Teams that stop at the harness build demos. Teams that build infrastructure build products.

## Connections
- Related: [[harness-design]], [[claude-code]], [[permission-system]], [[forked-agent-pattern]], [[context-management]]
- The CLAUDE.md hierarchy simultaneously serves as [[prompt-cache-optimization]] (static system prompt) and infrastructure (RBAC)

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-09 | raw/2026-04-09-rohit-harness-from-claude-code-leaks.md | Initial creation — Rohit's "Layer 4" thesis |
