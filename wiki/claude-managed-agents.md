---
type: entity
created: 2026-04-09
last-updated: 2026-04-09
sources:
  - raw/2026-04-09-anthropic-managed-agents-docs.md
  - raw/2026-04-09-anthropic-managed-agents-engineering-blog.md
  - raw/2026-04-09-anthropic-agent-capabilities-announcement.md
tags: [product, anthropic, agents, api]
---

# Claude Managed Agents

## Summary
Anthropic's fully managed agent hosting service, launched 2026-04-09 in beta. Provides the harness and infrastructure for running Claude as an autonomous agent — containers, tools, event streaming, and session management — so developers don't build their own agent loop. The hosted counterpart to [[claude-code]] (which is the interactive CLI) and the [[agent-sdk-vs-claude-code|Agent SDK]] (which is the programmatic library).

## Details

### What It Is
- Pre-built, configurable agent harness running in managed cloud infrastructure
- Best for long-running tasks (minutes to hours) and asynchronous work
- Contrast with Messages API (direct prompting, custom agent loops, fine-grained control)

### Core Concepts
- **Agent** — reusable, versioned configuration: model + system prompt + tools + MCP servers + skills
- **Environment** — container template: packages (pip, npm, apt, cargo, gem, go), networking rules, mounted files
- **Session** — running agent instance within an environment, generating outputs
- **Events** — bidirectional messages (user turns, tool results, agent responses, status updates) via SSE streaming

### Architecture (Brain/Hands/Session)
- **Brain** (Claude + Harness) — stateless inference + control loop
- **Hands** (Sandboxes + Tools) — execution environments, called uniformly as `execute(name, input) → string`
- **Session** — append-only event log, durable state outside the harness. Source of truth.
- See [[managed-agents-architecture]] for engineering deep-dive

### Built-in Tools
- Bash, Read, Write, Edit, Glob, Grep, Web Fetch, Web Search
- Enable all via `agent_toolset_20260401`, disable/enable per-tool with `configs`
- Custom tools supported (your code executes, result flows back)
- MCP server integration with OAuth vault

### API Endpoints
- `/v1/agents` — CRUD + archive + version history
- `/v1/environments` — CRUD + archive + delete
- `/v1/sessions` — CRUD + archive + delete
- `/v1/sessions/{id}/events` — send events, list events
- `/v1/sessions/{id}/stream` — SSE streaming
- `/v1/sessions/{id}/threads` — multi-agent threads
- `/v1/memory_stores` — persistent memory across sessions

### Research Preview Features
- [[managed-agents-outcomes]] — rubric-driven self-evaluation with grader agent
- [[managed-agents-multiagent]] — coordinator + specialized agent threads
- [[managed-agents-memory-stores]] — persistent memory stores across sessions

### Pricing & Limits
- Standard Claude token rates + $0.08/session-hour
- Create endpoints: 60 req/min; Read endpoints: 600 req/min
- Beta header required: `managed-agents-2026-04-01`

### SDKs & CLI
- SDKs: Python, TypeScript, Go, Java, C#, Ruby, PHP (all via `anthropic` package)
- CLI: `ant` (Anthropic CLI) — Homebrew, curl, or `go install`

### Performance
- p50 TTFT improved ~60%, p95 TTFT improved >90%
- Containers provisioned lazily (only when tools need them)

### Security
- Credentials never reach code execution sandboxes
- OAuth tokens in secure vault, accessed via proxy
- Git tokens handled during cloning, never exposed to running code

## Connections
- Related: [[anthropic]], [[claude-code]], [[agent-sdk-vs-claude-code]], [[harness-design]], [[multi-agent-architecture]], [[context-management]], [[managed-agents-architecture]], [[managed-agents-outcomes]], [[managed-agents-multiagent]], [[managed-agents-memory-stores]], [[infrastructure-layer]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-09 | raw/2026-04-09-anthropic-managed-agents-docs.md | Initial creation from full documentation suite (10 pages) |
| 2026-04-09 | raw/2026-04-09-anthropic-managed-agents-engineering-blog.md | Architecture details (brain/hands/session decoupling) |
| 2026-04-09 | raw/2026-04-09-anthropic-agent-capabilities-announcement.md | Launch context and companion features |
