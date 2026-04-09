# Claude Managed Agents — Official Documentation Suite

Source: platform.claude.com/docs/en/managed-agents/
Date: 2026-04-09 (launch day, beta)
Pages: overview, quickstart, agent-setup, environments, tools, events-and-streaming, define-outcomes, multi-agent, memory, API reference

## Overview

Claude Managed Agents provides the harness and infrastructure for running Claude as an autonomous agent. Instead of building your own agent loop, tool execution, and runtime, you get a fully managed environment where Claude can read files, run commands, browse the web, and execute code securely. The harness supports built-in prompt caching, compaction, and other performance optimizations.

### Core Concepts

| Concept | Description |
|---------|-------------|
| **Agent** | The model, system prompt, tools, MCP servers, and skills |
| **Environment** | A configured container template (packages, network access) |
| **Session** | A running agent instance within an environment, performing a specific task and generating outputs |
| **Events** | Messages exchanged between your application and the agent (user turns, tool results, status updates) |

### When to Use

- Long-running execution (minutes or hours, multiple tool calls)
- Cloud infrastructure (secure containers, pre-installed packages, network access)
- Minimal infrastructure (no need to build agent loop, sandbox, or tool execution)
- Stateful sessions (persistent file systems and conversation history)

### Messages API vs Managed Agents

| | Messages API | Claude Managed Agents |
|---|---|---|
| What it is | Direct model prompting access | Pre-built, configurable agent harness in managed infra |
| Best for | Custom agent loops and fine-grained control | Long-running tasks and asynchronous work |

### Rate Limits

| Operation | Limit |
| --- | --- |
| Create endpoints (agents, sessions, environments) | 60 requests/min |
| Read endpoints (retrieve, list, stream) | 600 requests/min |

## How It Works

1. **Create an agent** — Define model, system prompt, tools, MCP servers, skills. Create once, reference by ID.
2. **Create an environment** — Configure cloud container with packages, network access, mounted files.
3. **Start a session** — Launch session referencing agent + environment.
4. **Send events and stream responses** — Send user messages as events. Claude autonomously executes tools and streams results via SSE.
5. **Steer or interrupt** — Send additional user events to guide agent mid-execution, or interrupt.

## Agent Setup (agent-setup)

### Agent Configuration Fields

| Field | Description |
| --- | --- |
| `name` | Required. Human-readable name. |
| `model` | Required. Claude model (all 4.5+ supported). |
| `system` | System prompt defining behavior/persona. |
| `tools` | Pre-built agent tools, MCP tools, custom tools. |
| `mcp_servers` | MCP servers for third-party capabilities. |
| `skills` | Domain-specific context with progressive disclosure. |
| `callable_agents` | Other agents this agent can invoke (research preview). |
| `description` | What the agent does. |
| `metadata` | Arbitrary key-value pairs. |

### Create Agent API

```
POST /v1/agents
```

Example (Python):
```python
agent = client.beta.agents.create(
    name="Coding Assistant",
    model="claude-sonnet-4-6",
    system="You are a helpful coding agent.",
    tools=[{"type": "agent_toolset_20260401"}],
)
```

The `agent_toolset_20260401` enables all pre-built tools (bash, file ops, web search, etc.).

For fast mode with Opus: `model={"id": "claude-opus-4-6", "speed": "fast"}`.

### Update Agent

Generates a new version. Pass current `version` for optimistic concurrency. Omitted fields are preserved. Scalar fields replaced. Array fields fully replaced. Metadata merged at key level.

### Agent Lifecycle

- **Update** — new version
- **List versions** — full version history
- **Archive** — read-only, new sessions blocked, existing sessions continue

## Environments (environments)

### Configuration Options

**Packages** — pre-install via package managers:
| Field | Package manager |
| --- | --- |
| `apt` | System packages |
| `cargo` | Rust |
| `gem` | Ruby |
| `go` | Go modules |
| `npm` | Node.js |
| `pip` | Python |

**Networking**:
- `unrestricted` — Full outbound access (default), safety blocklist applied
- `limited` — Restrict to `allowed_hosts` list, with `allow_mcp_servers` and `allow_package_managers` booleans

### Environment Lifecycle

- Persist until archived/deleted
- Multiple sessions can reference same environment
- Each session gets own isolated container instance
- Not versioned

## Tools (tools)

### Built-in Agent Tools

| Tool | Name | Description |
|---|---|---|
| Bash | `bash` | Execute bash commands |
| Read | `read` | Read filesystem files |
| Write | `write` | Write filesystem files |
| Edit | `edit` | String replacement in files |
| Glob | `glob` | File pattern matching |
| Grep | `grep` | Regex text search |
| Web fetch | `web_fetch` | Fetch URL content |
| Web search | `web_search` | Search the web |

### Configuring the Toolset

Enable all with `agent_toolset_20260401`. Disable specific tools:
```json
{"type": "agent_toolset_20260401", "configs": [{"name": "web_fetch", "enabled": false}]}
```

Enable only specific tools:
```json
{"type": "agent_toolset_20260401", "default_config": {"enabled": false}, "configs": [{"name": "bash", "enabled": true}]}
```

### Custom Tools

Define custom tools with name, description, and input_schema. Claude emits structured requests, your code runs the operation, result flows back.

Best practices:
- Provide extremely detailed descriptions (3-4+ sentences)
- Consolidate related operations into fewer tools
- Use meaningful namespacing in tool names
- Design responses to return only high-signal information

## Events and Streaming (events-and-streaming)

### User Events

| Type | Description |
| --- | --- |
| `user.message` | User message with text content |
| `user.interrupt` | Stop agent mid-execution |
| `user.custom_tool_result` | Response to custom tool call |
| `user.tool_confirmation` | Approve/deny tool call (when policy requires) |
| `user.define_outcome` | Define outcome for agent to work toward |

### Agent Events

| Type | Description |
| --- | --- |
| `agent.message` | Text content response |
| `agent.thinking` | Thinking content (extended thinking) |
| `agent.tool_use` | Pre-built tool invocation |
| `agent.tool_result` | Pre-built tool result |
| `agent.mcp_tool_use` | MCP tool invocation |
| `agent.mcp_tool_result` | MCP tool result |
| `agent.custom_tool_use` | Custom tool invocation |
| `agent.thread_context_compacted` | Context compaction occurred |
| `agent.thread_message_sent` | Multiagent message sent |
| `agent.thread_message_received` | Multiagent message received |

### Session Events

| Type | Description |
| --- | --- |
| `session.status_running` | Agent actively processing |
| `session.status_idle` | Agent finished, waiting for input (includes `stop_reason`) |
| `session.status_rescheduled` | Transient error, retrying |
| `session.status_terminated` | Unrecoverable error |
| `session.error` | Error with typed object and `retry_status` |
| `session.outcome_evaluated` | Outcome evaluation terminal |
| `session.thread_created` | Multiagent thread spawned |
| `session.thread_idle` | Multiagent thread finished |

### Span Events

| Type | Description |
| --- | --- |
| `span.model_request_start` | Model inference started |
| `span.model_request_end` | Model inference completed (includes token counts) |
| `span.outcome_evaluation_start` | Outcome evaluation started |
| `span.outcome_evaluation_ongoing` | Outcome evaluation heartbeat |
| `span.outcome_evaluation_end` | Outcome evaluation completed |

### Stop Reasons

| Reason | Meaning |
| --- | --- |
| `end_turn` | Agent naturally completed |
| `max_tokens` | Hit max tokens in single turn |
| `requires_action` | Needs user input (custom tool result, tool confirmation) |

### Streaming Protocol

SSE (Server-Sent Events) via `GET /v1/sessions/{id}/stream`. Accept: `text/event-stream`.

### Interrupting

Send `user.interrupt` to halt the agent. Use to redirect work, cancel long-running tasks, or refine instructions.

### Tool Confirmation

Permission policy can be `always_allow` or `always_ask`. When `always_ask`, agent pauses with `requires_action` stop reason; you send `user.tool_confirmation` with `allow` or `deny`.

## Define Outcomes (define-outcomes) [Research Preview]

The `outcome` elevates a session from conversation to work. You define what the end result should look like and how to measure quality. The agent works toward that target, self-evaluating and iterating until the outcome is met.

### How It Works

- Define a rubric (markdown document with per-criterion scoring)
- Send `user.define_outcome` event with description, rubric, and optional `max_iterations` (default 3, max 20)
- Harness provisions a separate grader with its own context window
- Grader evaluates artifact against rubric, returns per-criterion breakdown
- Agent iterates until satisfied or max iterations reached

### Outcome Evaluation Results

| Result | Next |
| --- | --- |
| `satisfied` | Session → idle |
| `needs_revision` | Agent starts new iteration |
| `max_iterations_reached` | One final revision, then idle |
| `failed` | Session → idle (rubric/task mismatch) |
| `interrupted` | User interrupted during evaluation |

### Retrieving Deliverables

Agent writes to `/mnt/session/outputs/`. Fetch via Files API scoped to session.

## Multi-Agent (multi-agent) [Research Preview]

Multi-agent orchestration lets one agent coordinate with others. Agents run in parallel with isolated context.

### How It Works

- All agents share same container and filesystem
- Each agent runs in own **thread** (context-isolated event stream with own conversation history)
- Coordinator reports in primary thread
- Threads are persistent (follow-ups retain history)
- Each agent uses own configuration (model, system, tools)
- Only one level of delegation (coordinator → callees, callees cannot call further)

### Declare Callable Agents

```python
orchestrator = client.beta.agents.create(
    name="Engineering Lead",
    model="claude-sonnet-4-6",
    system="Coordinate engineering work...",
    tools=[{"type": "agent_toolset_20260401"}],
    callable_agents=[
        {"type": "agent", "id": reviewer_id, "version": 1},
        {"type": "agent", "id": test_writer_id, "version": 1},
    ],
)
```

### Session Threads

- Session-level stream = primary thread (condensed view of all activity)
- Thread streams show individual agent's reasoning and tool calls
- Session status aggregates all threads

### Multiagent Event Types

| Type | Description |
| --- | --- |
| `session.thread_created` | New thread spawned |
| `session.thread_idle` | Thread finished |
| `agent.thread_message_sent` | Message sent to another thread |
| `agent.thread_message_received` | Message received from another thread |

## Memory (memory) [Research Preview]

Memory stores let agents carry learnings across sessions: user preferences, project conventions, prior mistakes, domain context.

### Memory Store

Workspace-scoped collection of text documents optimized for Claude. When attached to a session, agent automatically checks stores before starting and writes learnings when done.

### Create Memory Store

```python
store = client.beta.memory_stores.create(
    name="User Preferences",
    description="Per-user preferences and project context.",
)
```

### Attach to Session

```python
session = client.beta.sessions.create(
    agent=agent.id,
    environment_id=environment.id,
    resources=[{
        "type": "memory_store",
        "memory_store_id": store.id,
        "access": "read_write",
        "prompt": "Check before starting any task.",
    }],
)
```

Max 8 memory stores per session. Individual memories capped at 100KB (~25K tokens).

### Memory Tools (auto-available when stores attached)

| Tool | Description |
| --- | --- |
| `memory_list` | List memories, filter by path prefix |
| `memory_search` | Full-text search |
| `memory_read` | Read contents |
| `memory_write` | Create/overwrite at path |
| `memory_edit` | Modify existing |
| `memory_delete` | Remove |

### Audit & Versioning

Every mutation creates immutable **memory version** (`memver_...`). Supports:
- List versions (filter by memory_id, operation, session_id, time range)
- Retrieve version (full content)
- Redact version (scrub content, preserve audit trail)
- Optimistic concurrency via `content_sha256` preconditions

## API Reference Summary

### Endpoints

**Agents:**
- `POST /v1/agents` — Create agent
- `GET /v1/agents` — List agents
- `GET /v1/agents/{id}` — Retrieve agent
- `POST /v1/agents/{id}` — Update agent
- `POST /v1/agents/{id}/archive` — Archive agent
- `GET /v1/agents/{id}/versions` — List versions

**Environments:**
- `POST /v1/environments` — Create
- `GET /v1/environments` — List
- `GET /v1/environments/{id}` — Retrieve
- `POST /v1/environments/{id}` — Update
- `POST /v1/environments/{id}/archive` — Archive
- `DELETE /v1/environments/{id}` — Delete

**Sessions:**
- `POST /v1/sessions` — Create session
- `GET /v1/sessions` — List sessions
- `GET /v1/sessions/{id}` — Retrieve session
- `POST /v1/sessions/{id}` — Update session
- `POST /v1/sessions/{id}/archive` — Archive
- `DELETE /v1/sessions/{id}` — Delete

**Events:**
- `POST /v1/sessions/{id}/events` — Send events
- `GET /v1/sessions/{id}/events` — List events
- `GET /v1/sessions/{id}/stream` — Stream events (SSE)

**Threads (multi-agent):**
- `GET /v1/sessions/{id}/threads` — List threads
- `GET /v1/sessions/{id}/threads/{tid}/stream` — Stream thread events
- `GET /v1/sessions/{id}/threads/{tid}/events` — List thread events

**Memory Stores:**
- `POST /v1/memory_stores` — Create store
- `GET /v1/memory_stores` — List stores
- `GET /v1/memory_stores/{id}` — Retrieve store
- `POST /v1/memory_stores/{id}/memories` — Write memory
- `GET /v1/memory_stores/{id}/memories` — List memories
- `GET /v1/memory_stores/{id}/memories/{mid}` — Retrieve memory
- `PATCH /v1/memory_stores/{id}/memories/{mid}` — Update memory
- `DELETE /v1/memory_stores/{id}/memories/{mid}` — Delete memory
- `GET /v1/memory_stores/{id}/memory_versions` — List versions
- `GET /v1/memory_stores/{id}/memory_versions/{vid}` — Retrieve version
- `POST /v1/memory_stores/{id}/memory_versions/{vid}/redact` — Redact version

### Required Headers

All requests:
- `anthropic-version: 2023-06-01`
- `anthropic-beta: managed-agents-2026-04-01`
- `x-api-key: $ANTHROPIC_API_KEY`

Research preview features additionally require:
- `anthropic-beta: managed-agents-2026-04-01-research-preview`

### Session Object Schema

```json
{
  "id": "string",
  "type": "session",
  "status": "rescheduling|running|idle|terminated",
  "agent": { "id", "name", "version", "model", "tools", "system", ... },
  "environment_id": "string",
  "title": "string",
  "metadata": {},
  "resources": [],
  "stats": { "active_seconds", "duration_seconds" },
  "usage": { "input_tokens", "output_tokens", "cache_creation", "cache_read_input_tokens" }
}
```

### Supported Models

- claude-opus-4-6 (most intelligent)
- claude-sonnet-4-6 (best speed/intelligence balance)
- claude-haiku-4-5 (fastest)
- claude-opus-4-5, claude-sonnet-4-5

### Pricing

Standard token rates + $0.08/session-hour.

### SDKs

Python, TypeScript, Go, Java, C#, Ruby, PHP — all via `anthropic` package.

### CLI Tool

`ant` (Anthropic CLI) — install via Homebrew, curl, or Go.

### Branding Guidelines

Allowed: "Claude Agent", "Claude", "{YourAgent} Powered by Claude"
Not permitted: "Claude Code", "Claude Cowork", Claude Code ASCII art
