---
type: source-summary
created: 2026-05-14
last-updated: 2026-05-14
sources:
  - raw/2026-05-14-anthropic-claude-code-hooks-guide.md
  - raw/2026-05-14-anthropic-claude-code-hooks-reference.md
tags: [claude-code, official-docs, hooks, automation, deterministic, lifecycle]
---

# Source: Hooks (guide + reference)

## Summary
Official Anthropic docs on **hooks in [[claude-code]]** — user-defined shell commands, HTTP endpoints, or LLM prompts that execute automatically at specific points in Claude Code's lifecycle. Provides **deterministic control** over behavior, ensuring certain actions always happen rather than relying on the LLM to choose to run them. The official mechanism behind [[zero-friction-capture|our Pipeline B]] (`SessionEnd`/`PreCompact` capture) — and the integration point [[claude-memory-compiler]] uses.

## Three hook types

| Type | When to use |
| :--- | :--- |
| **Command hook** | Deterministic rule (run linter on every Edit) |
| **Prompt-based hook** | Decision that requires judgment but is faster as a single LLM call |
| **Agent-based hook** | Decision that needs full agent reasoning loop (PR review on Stop) |

For deterministic rules, prefer command hooks (faster, no extra LLM token cost). Prompt/agent hooks for judgment calls.

## Hook lifecycle — three cadences

When event fires and matcher matches, Claude Code passes JSON context. Command hooks get input on stdin; HTTP hooks get POST body.

| Cadence | Events |
| :--- | :--- |
| **Once per session** | `SessionStart`, `SessionEnd` |
| **Once per turn** | `UserPromptSubmit`, `Stop`, `StopFailure` |
| **Every tool call** | `PreToolUse`, `PostToolUse` |

Plus subagent + worktree + agent-team specific events:
- `SubagentStart`, `SubagentStop` (also `Stop` in subagent → auto-converted to `SubagentStop`)
- `WorktreeCreate`, `WorktreeRemove` (replace default git worktree logic — supports SVN/Perforce via `WorktreeCreate` hook in [[source-claude-code-worktrees-docs|worktrees]])
- `TeammateIdle`, `TaskCreated`, `TaskCompleted` (from [[source-claude-code-agent-teams-docs|agent teams]])
- `PreCompact` (fires before context compaction — what our Pipeline B uses)
- `Notification` (when Claude wants attention)

## Exit code semantics

| Exit code | Meaning |
| :--- | :--- |
| `0` | Pass — hook approved |
| `2` | **Block** — stderr fed back to Claude as feedback |
| Other | Treated as failure, but doesn't block (unless event-specific behavior says otherwise) |

The `exit 2` pattern is the **deterministic guardrail mechanism**: validation scripts can refuse Bash commands, block file writes, prevent task completion, etc.

## Configure hook location

Three places:
1. `~/.claude/settings.json` — user-level
2. `.claude/settings.json` — project-level (checked into repo)
3. `.claude/settings.local.json` — project-local (not in repo)

Plus subagent frontmatter `hooks:` field (scoped to subagent lifecycle).
Plus skill frontmatter `hooks:` field (scoped to skill invocation).
Plus plugin `hooks/hooks.json`.

## PreToolUse / PostToolUse with matchers

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          { "type": "command", "command": "npx prettier --write" }
        ]
      }
    ]
  }
}
```

Matcher is a regex against tool name. Multiple matcher blocks allowed per event.

## Async hooks

For long-running checks, declare `async: true` so Claude Code doesn't block waiting. Hook starts in background; results come back via a separate `notifications/hook_result` event. Useful for heavy linters or CI checks that take seconds.

## HTTP hooks

Instead of command, use:
```json
{
  "type": "http",
  "url": "https://hook.example.com/validate",
  "method": "POST"
}
```

POST body is the same JSON command hooks get on stdin. Response body parsed for `{"decision": "approve|block", "reason": "..."}`. Same `decision` schema as command hook stdout.

## MCP tool hooks

`matcher: "mcp__servername__toolname"` matches against MCP tool names. Lets you gate or post-process external tool calls (e.g., log every Linear API call your MCP integration makes).

## Hooks in skills and agents

[[source-claude-code-subagents-docs|Subagent frontmatter]] `hooks:` field declares hooks that fire only while that subagent is active (auto-cleaned when finished).

[[agent-skills-standard|Skill frontmatter]] `hooks:` field same idea — fires only during skill invocation.

## Connection to our Pipeline B

Our existing Pipeline B (in LoreAI + blog2video) uses:
- `SessionEnd` hook → triggers `scripts/flush.py` → writes session knowledge to `raw/`
- `PreCompact` hook → captures soon-to-be-lost context before compaction
- `CLAUDE_INVOKED_BY` env var prevents recursion when hooks themselves launch Claude

Official docs validate this approach. **No conflicts** — Pipeline B uses the documented schema.

## Windows + PowerShell

Add `shell: powershell` to hook entry. Write hook scripts in PowerShell. Documented because cross-platform support matters for team distribution.

## Cross-vendor parity update (2026-05-14)

**OpenAI Codex Hooks reached General Availability on 2026-05-14** (see [[source-openai-codex-hooks-docs]]). Functional parity assessment:

| Dimension | Anthropic | Codex |
|---|---|---|
| Lifecycle events | PreToolUse / PostToolUse / Stop / SessionEnd / PreCompact / UserPromptSubmit | SessionStart / PreToolUse / PermissionRequest / PostToolUse / UserPromptSubmit / Stop |
| Block mechanism | exit 2 → stderr feedback | exit 2 → stderr feedback (identical) |
| Config layers | user / project / plugin | user / project / plugin / **enterprise (managed via `requirements.toml`)** |
| Tool-call deny via hook | JSON output | JSON `permissionDecision: deny/allow` + `updatedInput` |
| Async / HTTP / MCP hooks | Multiple hook types | Only `type: "command"` GA (prompt / agent reserved) |

**Differentiator**: Anthropic has more hook types (HTTP, MCP); Codex has `PermissionRequest` as separate event + enterprise-managed hook policy. **For PM long-horizon use cases the functional surface is equivalent** — see [[pm-long-horizon-methodology]] for vendor-selection matrix.

## Connections
- Related: [[claude-code]], [[zero-friction-capture]], [[claude-memory-compiler]], [[source-claude-code-subagents-docs]], [[source-claude-code-agent-teams-docs]], [[source-claude-code-worktrees-docs]], [[source-claude-code-plugins-docs]], [[agent-skills-standard]], [[two-pipeline-architecture]], [[source-openai-codex-hooks-docs]]
- Validates [[two-pipeline-architecture|Pipeline B]] approach — `SessionEnd`/`PreCompact` are documented hooks, not undocumented internals
- Closes a long-standing gap: previous wiki content referenced hooks loosely ("26 hook event types, 4 handler types in [[claude-code]]") — this is now the canonical spec
- Cross-vendor sibling: [[source-openai-codex-hooks-docs]] — Codex Hooks GA 2026-05-14, functional parity

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-05-14 | raw/2026-05-14-anthropic-claude-code-hooks-guide.md | Initial creation from official hooks guide |
| 2026-05-14 | raw/2026-05-14-anthropic-claude-code-hooks-reference.md | Added complete event schemas + advanced features (async, HTTP, MCP tool hooks) |
| 2026-05-20 | raw/2026-05-14-openai-codex-hooks-docs.md | Added cross-vendor parity table — Codex Hooks GA 2026-05-14 = functional parity for PM long-horizon use cases |
