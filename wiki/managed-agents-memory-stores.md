---
type: concept
created: 2026-04-09
last-updated: 2026-04-09
sources:
  - raw/2026-04-09-anthropic-managed-agents-docs.md
tags: [concept, agents, memory]
---

# Managed Agents Memory Stores

## Summary
Research preview feature of [[claude-managed-agents]] that gives agents persistent memory across sessions. Workspace-scoped collections of text documents that agents automatically check before starting work and write to when done. Every mutation creates an immutable version for auditing.

## Details

### How It Works
- **Memory store** — workspace-scoped collection, created with `name` + `description`
- Agent automatically checks stores before starting task, writes durable learnings when done — no additional prompting needed
- Attach up to 8 memory stores per session via `resources[]` array
- Access modes: `read_write` (default) or `read_only`
- Individual memories capped at 100KB (~25K tokens)

### Memory Tools (auto-injected when stores attached)
| Tool | Description |
| --- | --- |
| `memory_list` | List memories, filter by path prefix |
| `memory_search` | Full-text search across contents |
| `memory_read` | Read a memory's contents |
| `memory_write` | Create or overwrite at path |
| `memory_edit` | Modify existing memory |
| `memory_delete` | Remove a memory |

### Use Patterns
- **Shared reference material** — read-only store across many sessions (standards, conventions)
- **Per-user/team/project stores** — map to your product's structure
- **Different lifecycles** — some stores outlive sessions, archived on own schedule
- **Seed with content** — pre-load before any agent runs

### Versioning & Audit
- Every mutation creates immutable **memory version** (`memver_...`)
- Operations: `created`, `modified`, `deleted`
- Filter versions by memory_id, operation, session_id, api_key_id, time range
- **Redact** — scrub content from historical version while preserving audit trail (for compliance: PII, leaked secrets, user deletion requests)

### Optimistic Concurrency
- `precondition: {type: "not_exists"}` — create-only guard, 409 if already exists
- `precondition: {type: "content_sha256", content_sha256: "..."}` — safe edits, 409 on mismatch

### Connection to Existing Concepts
- Platform-level implementation of [[session-memory]] and [[dreaming]] concepts from Claude Code
- Memory stores are the API equivalent of Claude Code's file-based `.claude/` memory system
- Validates [[context-management]]'s principle: memory must live outside the context window

## Connections
- Related: [[claude-managed-agents]], [[session-memory]], [[dreaming]], [[context-management]], [[claude-memory-compiler]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-09 | raw/2026-04-09-anthropic-managed-agents-docs.md | Initial creation from memory documentation |
