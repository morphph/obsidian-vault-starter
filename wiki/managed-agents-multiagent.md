---
type: concept
created: 2026-04-09
last-updated: 2026-04-09
sources:
  - raw/2026-04-09-anthropic-managed-agents-docs.md
tags: [concept, agents, multi-agent]
---

# Managed Agents Multi-Agent

## Summary
Research preview feature of [[claude-managed-agents]] enabling one coordinator agent to delegate to specialized agents within a single session. Each agent runs in its own context-isolated thread but shares the same container and filesystem. One level of delegation only.

## Details

### Architecture
- **Coordinator** — primary agent, runs in primary thread (session-level event stream)
- **Callable agents** — declared via `callable_agents` field on coordinator config
- **Threads** — each agent gets its own context-isolated event stream with own conversation history
- All agents share same container and filesystem, but NOT context or tools
- Threads are persistent: coordinator can send follow-ups and agent retains prior turn history

### Delegation Model
- Only one level deep: coordinator → callees. Callees cannot call further agents.
- Each callable agent uses its own configuration (model, system prompt, tools, MCP servers, skills)
- Tools and context are NOT shared between agents

### Good Delegation Targets
- **Code review** — focused system prompt + read-only tools
- **Test generation** — writes and runs tests without touching production code
- **Research** — web tools, summarizes findings back to coordinator

### Thread Events
| Type | Description |
| --- | --- |
| `session.thread_created` | Coordinator spawned new thread |
| `session.thread_idle` | Agent thread finished current work |
| `agent.thread_message_sent` | Agent sent message to another thread |
| `agent.thread_message_received` | Agent received message from another thread |

### Session Status
- Aggregation: if any thread is `running`, session status = `running`
- Primary thread shows condensed view of all activity
- Drill into individual threads for specific agent's reasoning and tool calls

### Connection to Existing Concepts
- Implements [[multi-agent-architecture]] as a first-party platform feature
- Thread model parallels the [[forked-agent-pattern]] from Claude Code (isolated context + shared filesystem)
- Coordinator pattern aligns with [[harness-design]]'s planner/generator/evaluator roles

## Connections
- Related: [[claude-managed-agents]], [[multi-agent-architecture]], [[harness-design]], [[forked-agent-pattern]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-09 | raw/2026-04-09-anthropic-managed-agents-docs.md | Initial creation from multi-agent documentation |
