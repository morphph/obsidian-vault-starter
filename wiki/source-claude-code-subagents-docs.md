---
type: source-summary
created: 2026-05-14
last-updated: 2026-05-14
sources:
  - raw/2026-05-14-anthropic-claude-code-subagents.md
tags: [claude-code, official-docs, subagents, agent-tool, frontmatter, hooks, memory, fork]
---

# Source: Create custom subagents

## Summary
Official Anthropic doc on **custom subagents in [[claude-code]]** — the canonical "subagent" spec. Subagents are specialized AI assistants that handle specific tasks in their own context, with custom system prompt, specific tool access, and independent permissions. Claude delegates based on task description + `description` frontmatter. Full schema of the 17 frontmatter fields, the four discovery scopes, the `/agents` interface, and the experimental [[forked-agent-pattern|forked subagent pattern]] (`CLAUDE_CODE_FORK_SUBAGENT=1`).

## Built-in subagents (canonical)

| Agent | Model | Tools | Purpose |
| :--- | :--- | :--- | :--- |
| **Explore** | Haiku | Read-only | Codebase exploration. Thoroughness levels: quick / medium / very thorough |
| **Plan** | Inherits | Read-only | Used during plan mode for codebase research |
| **general-purpose** | Inherits | All tools | Complex multi-step tasks needing exploration + action |
| **statusline-setup** | Sonnet | — | When `/statusline` invoked |
| **claude-code-guide** | Haiku | — | When you ask questions about Claude Code features |

Subagents cannot spawn other subagents.

## Scope priority (highest → lowest)

| Location | Scope |
| :--- | :--- |
| Managed settings | Organization-wide (highest priority) |
| `--agents` CLI flag | Current session |
| `.claude/agents/` | Current project |
| `~/.claude/agents/` | All your projects |
| Plugin `agents/` directory | Where plugin enabled (lowest priority) |

> [!note]
> Plugin subagents **do not support** `hooks`, `mcpServers`, or `permissionMode` frontmatter fields — security-driven restriction.

## Frontmatter reference — 17 fields

Required: `name`, `description`. Notable optional:
- `tools` / `disallowedTools` — restrict access
- `model` — `sonnet`/`opus`/`haiku`/full ID/`inherit`
- `permissionMode` — `default`/`acceptEdits`/`auto`/`dontAsk`/`bypassPermissions`/`plan`
- `maxTurns` — agentic turn cap
- `skills` — preload at startup (full content injected, not just description)
- `mcpServers` — inline def OR reference by name; inline servers connect on subagent start
- `hooks` — lifecycle hooks scoped to subagent (PreToolUse, PostToolUse, Stop→SubagentStop)
- `memory` — persistent directory: `user`/`project`/`local` scope, MEMORY.md curated
- `background` — always run as background task
- `effort` — `low`/`medium`/`high`/`xhigh`/`max`
- `isolation: worktree` — temporary [[source-claude-code-worktrees-docs|git worktree]], auto-cleanup if no changes
- `initialPrompt` — auto-submitted as first user turn when subagent runs as main session

## Three invocation patterns (escalating)

1. **Natural language**: name the subagent in prompt; Claude decides
2. **@-mention**: `@"code-reviewer (agent)"` — guarantees this subagent runs
3. **Session-wide**: `claude --agent <name>` — system prompt + tools + model REPLACE Claude Code defaults

The `--agent` choice persists when you resume the session.

## Foreground vs background subagents

- **Foreground**: blocks main conversation. Permission prompts pass through to you.
- **Background**: concurrent. Inherits granted permissions, **auto-denies any tool call that would prompt**. If background subagent fails on missing permission, retry as foreground.

`Ctrl+B` to background a running task. Disable via `CLAUDE_CODE_DISABLE_BACKGROUND_TASKS=1`.

## Forked subagents (experimental)

`CLAUDE_CODE_FORK_SUBAGENT=1`. A **fork inherits the entire conversation so far** — same system prompt, tools, model, message history as main session. Drops input isolation but keeps tool output isolation (only final result returns to main context).

- Claude spawns a fork whenever it would use `general-purpose`
- Every subagent spawn runs in background
- `/fork <directive>` spawns one manually
- A fork **cannot spawn further forks**
- **Reuses parent's prompt cache** — cheaper than fresh subagent

## Persistent memory (`memory` field)

Subagent gets `MEMORY.md` directory. System prompt includes first 200 lines or 25KB of MEMORY.md. Read/Write/Edit auto-enabled. Compounds knowledge across sessions.

Recommended scope: `project` (shareable via VC). `user` for cross-project. `local` for project-specific but not in VC.

## Per-tool-call permission validation (PreToolUse hooks)

Conditional rules beyond tool allowlist. Example: subagent with `tools: Bash` + `PreToolUse` hook that validates each Bash command (e.g., only `SELECT` queries):

```bash
COMMAND=$(echo "$INPUT" | jq -r '.tool_input.command')
if echo "$COMMAND" | grep -iE '\b(INSERT|UPDATE|DELETE|DROP)\b'; then
  echo "Blocked" >&2; exit 2
fi
```

Exit code 2 → blocks, sends stderr back to Claude.

## Restrict subagent spawning

In a `claude --agent` main session: `tools: Agent(worker, researcher)` allowlists which subagent types can be spawned. Without `Agent`, no spawning. `Agent` (no parens) = all allowed.

Note: **Task tool was renamed to Agent in v2.1.63.** Existing `Task(...)` references still work as aliases.

## Connections
- Related: [[claude-code]], [[multi-agent-architecture]], [[forked-agent-pattern]], [[source-claude-code-agents-overview]], [[source-claude-code-agent-teams-docs]], [[source-claude-code-worktrees-docs]], [[source-claude-code-hooks-docs]], [[agent-skills-standard]]
- Resolves: many vague mentions of "subagent" in [[claude-code]] now have canonical spec
- Pairs with [[source-claude-code-agent-teams-docs]] — subagent definitions can be referenced when spawning teammates (the `tools` and `model` carry over, body appended)

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-05-14 | raw/2026-05-14-anthropic-claude-code-subagents.md | Initial creation from official subagents docs |
