# Ralph Orchestrator

**Source:** https://github.com/mikeyobrien/ralph-orchestrator
**Author/Org:** Mikey O'Brien
**Stars:** 2,702 | **Language:** Rust | **Last updated:** 2026-04-15
**Version:** 2.9.2
**Fetch method:** GitHub Deep Scan (gh CLI)

## What It Does
"A hat-based orchestration framework that keeps AI agents in a loop until the task is done." An improved, production-grade implementation of the [[ralph-wiggum]] technique for autonomous AI agent orchestration. Extends the basic bash loop into a full multi-backend, multi-agent orchestration system with web dashboard, Telegram HITL, parallel loops, and event-driven coordination.

## Architecture

```
ralph-cli      → CLI entry point, commands (run, plan, task, loops, web)
ralph-core     → Orchestration logic, event loop, hats, memories, tasks
ralph-adapters → Backend integrations (Claude, Kiro, Gemini, Codex, Roo, etc.)
ralph-telegram → Telegram bot for human-in-the-loop communication
ralph-tui      → Terminal UI (ratatui-based)
ralph-e2e      → End-to-end test framework
ralph-proto    → Protocol definitions
ralph-bench    → Benchmarking
ralph-api      → Web RPC API

backend/       → Web server (@ralph-web/server) - Fastify + tRPC + SQLite
frontend/      → Web dashboard (@ralph-web/dashboard) - React + Vite + TailwindCSS
```

### Key Concepts

**Hat System**: Specialized agent personas coordinating through events. Each hat has triggers, publications, optional concurrency, and instructions. Hats are the Ralph equivalent of roles in multi-agent architectures.

**Backpressure**: Gates that reject incomplete work — tests, lint, typecheck, LLM-as-judge. Don't prescribe how; create gates that reject bad work.

**Memories & Tasks**: Persistent learning across sessions (`.ralph/agent/memories.md`) and runtime work tracking (`.ralph/agent/tasks.jsonl`). "Disk is state, Git is memory."

**Parallel Loops**: Multiple orchestration loops via git worktrees. Primary loop holds `.ralph/loop.lock`, worktree loops have isolated filesystems with symlinked memories/specs/tasks.

**Agent Waves**: Intra-loop parallelism. A hat with `concurrency > 1` can process multiple work items in parallel within one iteration. Scatter-gather pattern with optional aggregation.

**RObot (HITL via Telegram)**: Agents emit `human.interact` events → question sent via Telegram → loop blocks until response. Humans can send proactive guidance anytime (`human.guidance`). Parallel loop routing via reply-to or `@loop-id` prefix.

**Web Dashboard (Alpha)**: React + Vite + TailwindCSS frontend with Rust RPC API backend. Monitor and manage orchestration loops visually.

**MCP Server Mode**: `ralph mcp serve` — runs as MCP server over stdio for integration with MCP-compatible clients. Scoped to single workspace root.

## Installation

```bash
# npm (recommended)
npm install -g @ralph-orchestrator/ralph-cli

# Cargo
cargo install ralph-cli

# GitHub Releases
curl --proto '=https' --tlsv1.2 -LsSf \
  https://github.com/mikeyobrien/ralph-orchestrator/releases/latest/download/ralph-cli-installer.sh | sh
```

## Quick Start

```bash
# Initialize with preferred backend
ralph init --backend claude

# Plan a feature (interactive PDD session)
ralph plan "Add user authentication with JWT"
# Creates: specs/user-authentication/requirements.md, design.md, implementation-plan.md

# Implement the feature
ralph run -p "Implement the feature in specs/user-authentication/"
```

## The Ralph Tenets (from CLAUDE.md)

1. **Fresh Context Is Reliability** — Each iteration clears context. Re-read specs, plan, code every cycle. Optimize for the "smart zone" (40-60% of ~176K usable tokens).
2. **Backpressure Over Prescription** — Don't prescribe how; create gates that reject bad work.
3. **The Plan Is Disposable** — Regeneration costs one planning loop. Never fight to save a plan.
4. **Disk Is State, Git Is Memory** — Memories and Tasks are the handoff mechanisms.
5. **Steer With Signals, Not Scripts** — The codebase is the instruction manual.
6. **Let Ralph Ralph** — Sit *on* the loop, not *in* it. Tune like a guitar.

## Anti-Patterns

- Building features into the orchestrator that agents can handle
- Complex retry logic (fresh context handles recovery)
- Detailed step-by-step instructions (use backpressure instead)
- Scoping work at task selection time (scope at plan creation instead)

## Tech Stack

- **Language**: Rust (edition 2024)
- **Frontend**: React + Vite + TailwindCSS
- **Backend**: Fastify + tRPC + SQLite (legacy Node), migrating to Rust RPC API
- **TUI**: ratatui
- **Testing**: Replay-based smoke tests (JSONL fixtures), E2E framework
- **Packaging**: npm, Cargo, GitHub Releases
- **Nix**: devenv.nix for reproducible dev environment

## Multi-Backend Support

| Backend | Type |
|---------|------|
| Claude Code | Primary |
| Kiro | Supported |
| Gemini CLI | Supported |
| Codex | Supported |
| Amp | Supported |
| Copilot CLI | Supported |
| OpenCode | Supported |
| Roo | Supported |

## Key Patterns & Takeaways

1. **Hat system = multi-agent-lite**: Instead of separate processes, hats are persona configs within one orchestrator. Simpler than full multi-agent but enables specialization.
2. **Wave pattern = intra-loop parallelism**: Scatter-gather within a single iteration. Agent emits wave events → N parallel workers → results merged back. Solves the "one thing per loop" limitation for reviewable parallelizable work.
3. **Telegram HITL = remote steering**: Human-in-the-loop without being at the keyboard. Agent blocks on questions, human responds from phone. Proactive guidance injected as `## ROBOT GUIDANCE` in prompt.
4. **Worktree-based parallelism**: Multiple loops on same repo using `git worktree`. Primary loop manages merge queue. Solves the "one loop per repo" limitation.
5. **Event-driven coordination**: Hats trigger on events, publish events. No hardcoded orchestration logic — the event bus handles routing.
6. **PDD (Plan-Driven Development)**: `ralph plan` creates specs first, then `ralph run` implements from specs. Two distinct phases with different prompts.
7. **Diagnostics & auditability**: JSONL logging of agent output, orchestration decisions, and errors. Simon Willison's transcript tool philosophy made concrete.

## Ecosystem Connections

- Implements [[ralph-wiggum]] technique with production-grade tooling
- Hat system is a lightweight [[multi-agent-architecture]]
- Backpressure = [[verification-loops]] made systematic
- Fresh context per iteration addresses [[context-anxiety|context rot]]
- Telegram HITL is the [[ralph-wiggum]] "RObot" mode — between pure HITL and pure AFK
- MCP server mode connects to broader [[claude-code]] MCP ecosystem

## Repo Vitals
- Stars: 2,702 | Forks: not checked
- Language: Rust (edition 2024)
- Version: 2.9.2
- Last commit: "docs(config): document global user config for hooks (#298)"
- Assessment: **Very active** — multiple commits per day, well-maintained, growing community (Discord server)
