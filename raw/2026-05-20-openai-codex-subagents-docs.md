# OpenAI Codex Subagents (Documentation)

**Source:** https://developers.openai.com/codex/subagents
**Publisher:** OpenAI Developers (official docs)
**Fetch date:** 2026-05-20
**Fetch method:** WebFetch

---

## Core concept

> "Codex can run subagent workflows by spawning specialized agents in parallel and then collecting their results in one response."

Enabled by default. "Codex only spawns a new agent when you explicitly ask it to do so." Each subagent does independent model + tool work → token cost increases.

## Three built-in agents

- **default** — general-purpose fallback
- **worker** — execution-focused (implementation)
- **explorer** — read-heavy codebase exploration

## Global configuration (under `[agents]`)

| Field | Type | Purpose |
|---|---|---|
| `max_threads` | number | Concurrent agent thread cap (default: **6**) |
| `max_depth` | number | Nesting depth (default: 1) |
| `job_max_runtime_seconds` | number | Per-worker timeout for CSV batch jobs |

## Custom agent (TOML)

Required:
- `name` — identifier for spawning
- `description` — human-facing guidance for Codex
- `developer_instructions` — core behavioral instructions

Optional:
- `nickname_candidates` (UI labels)
- `model`
- `model_reasoning_effort`
- `sandbox_mode`
- `mcp_servers`
- `skills.config`

Storage:
- Personal: `~/.codex/agents/`
- Project: `.codex/agents/`

## Sandbox & approvals

Subagents inherit parent session's sandbox policy. In interactive CLI:
- Approval requests from inactive threads surface with source label
- Press `o` to open that thread before deciding
- Runtime overrides (`/permissions`, `--yolo`) propagate to children

## CSV batch (`spawn_agents_on_csv`, experimental)

Repeated audits across many similar items.

Parameters:
- `csv_path` — source CSV
- `instruction` — worker prompt template using `{column_name}` placeholders
- `id_column` — optional stable IDs
- `output_schema` — fixed JSON shape for worker returns
- `output_csv_path`, `max_concurrency`, `max_runtime_seconds` — job control

> "Each worker must call `report_agent_job_result` exactly once."

## Example: PR Review setup

```toml
# .codex/config.toml
[agents]
max_threads = 6
max_depth = 1
```

Three specialized agents:
- `pr_explorer` (read-only mapping)
- `reviewer` (correctness/security, `gpt-5.4`)
- `docs_researcher` (API verification via MCP)

## Example: Frontend debugging

- `code_mapper` (read-only code tracing)
- `browser_debugger` (reproduction with Chrome DevTools MCP)
- `ui_fixer` (targeted implementation)

## Management commands

- `/agent` — switch between active threads, inspect ongoing work
- Direct natural language to steer / stop / close running subagents

---

## Comparison with Claude Code

| Dimension | Codex Subagents | Claude Code Subagents |
|---|---|---|
| Spawn model | Explicit request, parallel | Explicit request, parallel |
| Built-in agents | 3 (default / worker / explorer) | General-purpose / specialized |
| Config format | TOML in `.codex/agents/` | Markdown in `.claude/agents/` |
| Sandbox inheritance | Yes | Yes |
| Per-agent sandbox override | Yes (`sandbox_mode` per agent) | Yes (worktree isolation) |
| Concurrency control | `max_threads` (default 6) | Worktree-based, not bounded |
| CSV batch primitive | `spawn_agents_on_csv` (experimental) | Not directly equivalent (would write a loop) |
| Skills integration | Yes (per-agent `skills.config`) | Yes |
| MCP per agent | Yes | Yes |

**Differentiator:** Codex's `spawn_agents_on_csv` + `report_agent_job_result` provides a structured batch primitive Anthropic doesn't ship as a first-class concept; useful for repeated audits.
