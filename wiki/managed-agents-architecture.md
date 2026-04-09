---
type: concept
created: 2026-04-09
last-updated: 2026-04-09
sources:
  - raw/2026-04-09-anthropic-managed-agents-engineering-blog.md
  - raw/2026-04-09-anthropic-managed-agents-docs.md
tags: [architecture, agents, anthropic]
---

# Managed Agents Architecture

## Summary
The engineering design behind [[claude-managed-agents]]: decouple the brain (Claude + harness), the hands (sandboxes + tools), and the session (append-only event log). Each component can fail or be replaced independently. The session — not the harness, not the container — is the source of truth.

## Details

### Three-Component Decoupling
- **Brain** — Claude model + stateless harness loop. Calls model, routes tool calls. Can be restarted without losing state.
- **Hands** — Containers, sandboxes, custom tools. Called uniformly: `execute(name, input) → string`. Provisioned lazily.
- **Session** — Append-only event log stored outside the harness. Accessed via `getEvents()` for positional slices. Durable state that outlives any harness instance.

### Session as Source of Truth
- Context durably stored in session log, lives outside Claude's context window
- `emitEvent(id, event)` writes durable transaction records
- Enables replay, auditing, and recovery from component failures
- Harness interrogates context by selecting positional slices of event stream

### Lazy Provisioning
- Containers provisioned only when tools actually need them
- Eliminates cold-start penalty for sessions that don't need containers
- p50 TTFT improved ~60%, p95 TTFT improved >90%

### Credential Isolation
- Credentials never reach code execution sandboxes
- Three auth patterns:
  1. Bundle credentials with resources during sandbox init (e.g., git clone)
  2. OAuth tokens in secure vault, accessed via dedicated proxy
  3. MCP tools called through proxy that takes session-associated token

### Uniform Tool Interface
- Every tool — container command, API call, MCP server — follows same `execute(name, input) → string` pattern
- Simplifies harness logic; tools are interchangeable execution targets

### Connection to Harness Design Theory
- Validates the [[harness-design]] principle: "LLM as reasoning center; harness provides perception, action, memory, constraints"
- The "managed" version makes the [[infrastructure-layer]] (Rohit's 4th layer) Anthropic's problem, not the developer's
- Session model maps to [[orchestration-loop]]: events are the observation-action-thought cycle made durable

## Connections
- Related: [[claude-managed-agents]], [[harness-design]], [[infrastructure-layer]], [[orchestration-loop]], [[context-management]], [[anthropic]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-09 | raw/2026-04-09-anthropic-managed-agents-engineering-blog.md | Initial creation from engineering blog |
| 2026-04-09 | raw/2026-04-09-anthropic-managed-agents-docs.md | Added API surface and tools details |
