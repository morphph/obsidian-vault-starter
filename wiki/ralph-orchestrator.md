---
type: entity
created: 2026-04-15
last-updated: 2026-04-15
sources:
  - raw/2026-04-15-repo-ralph-orchestrator.md
tags: [wiki, tool, agentic, automation]
---

# Ralph Orchestrator

## Summary
Production-grade Rust implementation of the [[ralph-wiggum]] technique (2,702 stars). Extends the basic bash loop into a full multi-backend, multi-agent orchestration framework with hat system, parallel loops via git worktrees, intra-loop parallelism (waves), Telegram HITL (RObot), web dashboard, and MCP server mode. Supports 7+ AI backends (Claude, Gemini, Codex, Kiro, Amp, Copilot, OpenCode, Roo).

## Details

### Core Features
- **Multi-backend support**: Claude Code, Kiro, Gemini CLI, Codex, Amp, Copilot CLI, OpenCode, Roo — `ralph init --backend <name>`
- **Hat system**: Specialized agent personas coordinating through an event bus. Each hat has triggers, publications, optional concurrency, and instructions. Lightweight [[multi-agent-architecture]] without separate processes.
- **Backpressure gates**: Tests, lint, typecheck, LLM-as-judge. Don't prescribe how — create gates that reject bad work. Systematic [[verification-loops]].
- **Memories & Tasks**: Persistent learning across sessions (`.ralph/agent/memories.md`) and runtime work tracking (`.ralph/agent/tasks.jsonl`). "Disk is state, Git is memory."
- **5 built-in presets**: `code-assist`, `debug`, `research`, `review`, `pdd-to-code-assist`

### Parallel Execution
- **Parallel loops**: Multiple orchestration loops on same repo via `git worktree`. Primary loop holds `.ralph/loop.lock`, worktree loops have isolated filesystems with symlinked memories/specs/tasks. Primary processes merge queue on completion.
- **Agent Waves**: Intra-loop parallelism. Hat with `concurrency > 1` spawns N parallel workers within one iteration. Scatter-gather pattern with optional aggregation. Breaks the "one thing per loop" constraint for parallelizable work (e.g., reviewing multiple files).

### Human-in-the-Loop
- **RObot (Telegram)**: Agents emit `human.interact` events → question sent via Telegram → loop blocks until response or timeout. Humans can send proactive guidance anytime (`human.guidance` injected as `## ROBOT GUIDANCE` in prompt). A third mode between pure HITL and pure AFK.
- Parallel loop message routing via reply-to, `@loop-id` prefix, or default to primary
- Commands: `/status`, `/tasks`, `/restart` for real-time visibility

### Interface Modes
- **CLI**: `ralph run`, `ralph plan`, `ralph task`, `ralph loops`, `ralph wave`
- **Web Dashboard (Alpha)**: React + Vite + TailwindCSS frontend, Rust RPC API backend. Monitor and manage loops visually.
- **TUI**: ratatui-based terminal UI
- **MCP Server**: `ralph mcp serve` — runs over stdio for MCP-compatible clients. Scoped to single workspace root per instance.

### The Ralph Tenets (codified in CLAUDE.md)
1. **Fresh Context Is Reliability** — Each iteration clears context. Optimize for "smart zone" (40-60% of ~176K tokens).
2. **Backpressure Over Prescription** — Gates reject bad work; don't prescribe steps.
3. **The Plan Is Disposable** — Regeneration costs one planning loop. Cheap.
4. **Disk Is State, Git Is Memory** — Memories and Tasks are the handoff mechanisms.
5. **Steer With Signals, Not Scripts** — The codebase is the instruction manual.
6. **Let Ralph Ralph** — Sit *on* the loop, not *in* it. Tune like a guitar.

### Anti-Patterns
- Building features into the orchestrator that agents can handle
- Complex retry logic (fresh context handles recovery)
- Detailed step-by-step instructions (use backpressure instead)
- Scoping work at task selection time (scope at plan creation)

### Architecture
- **Rust workspace**: 9 crates (cli, core, adapters, telegram, tui, e2e, proto, bench, api)
- **Web**: Fastify + tRPC + SQLite (legacy Node backend), migrating to Rust RPC API
- **Testing**: Replay-based smoke tests (JSONL fixtures), E2E framework with mock mode
- **Installation**: npm (`@ralph-orchestrator/ralph-cli`), Cargo, or GitHub Releases

### Quick Start
```bash
ralph init --backend claude
ralph plan "Add user authentication with JWT"
ralph run -p "Implement the feature in specs/user-authentication/"
```

## Connections
- Related: [[ralph-wiggum]], [[geoffrey-huntley]], [[claude-code]], [[multi-agent-architecture]], [[verification-loops]], [[context-anxiety]], [[harness-design]], [[orchestration-loop]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-15 | raw/2026-04-15-repo-ralph-orchestrator.md | Initial creation — full GitHub Deep Scan |
