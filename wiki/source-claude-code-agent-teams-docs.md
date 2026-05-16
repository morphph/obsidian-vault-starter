---
type: source-summary
created: 2026-05-14
last-updated: 2026-05-14
sources:
  - raw/2026-05-14-anthropic-claude-code-agent-teams.md
tags: [claude-code, official-docs, agent-teams, experimental, multi-agent, coordination]
---

# Source: Orchestrate teams of Claude Code sessions (Agent Teams)

## Summary
Official Anthropic doc on **agent teams** — a research-preview parallel-execution model where multiple Claude Code sessions work as a coordinated team with a lead, shared task list, and inter-agent messaging. **Experimental and disabled by default** (`CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`). Requires v2.1.32+. The big architectural step beyond subagents and [[claude-code-agent-view|agent view]]: teammates **communicate with each other**, not just back to a coordinator.

## How agent teams differ from subagents

|  | Subagents | Agent teams |
| :--- | :--- | :--- |
| Context | Own window; results return to caller | Own window; **fully independent** |
| Communication | Report results to main agent only | **Teammates message each other directly** |
| Coordination | Main agent manages all work | **Shared task list with self-coordination** |
| Best for | Focused tasks where only result matters | Complex work requiring discussion + collaboration |
| Token cost | Lower (results summarized back) | **Higher (each teammate = separate Claude instance)** |

Strongest use cases: research/review with multiple lenses, new modules each owned by different teammates, debugging with competing hypotheses, cross-layer coordination.

## Architecture — 4 components

| Component | Role |
| :--- | :--- |
| **Team lead** | Main session that creates team, spawns teammates, coordinates |
| **Teammates** | Separate Claude Code instances each working on assigned tasks |
| **Task list** | Shared work items teammates claim and complete |
| **Mailbox** | Messaging system for inter-agent communication |

State stored locally:
- Team config: `~/.claude/teams/{team-name}/config.json` (don't edit by hand — overwritten on state update)
- Task list: `~/.claude/tasks/{team-name}/`

No project-level equivalent. A `.claude/teams/teams.json` in your project is just an ordinary file, not config.

## Display modes — in-process vs split panes

- **In-process** (default in non-tmux terminals): all teammates in main terminal. `Shift+Down` to cycle. `Enter` view, `Esc` interrupt, `Ctrl+T` toggle task list.
- **Split panes** (default in tmux): each teammate gets own pane. Requires tmux OR iTerm2 with `it2` CLI.

`teammateMode: "auto"` (default), `"in-process"`, or `"tmux"`. Per-session override: `claude --teammate-mode in-process`.

## Use subagent definitions for teammates

Reference any subagent type when spawning. The teammate honors that definition's `tools` allowlist and `model`. **The definition's body is APPENDED to the teammate's system prompt as additional instructions** — not replacing it.

> [!warning]
> **`skills` and `mcpServers` frontmatter fields are NOT applied when subagent definition runs as a teammate.** Teammates load skills + MCP servers from project + user settings, same as regular session.

This crosses with [[source-claude-code-subagents-docs|subagent definitions]] — same file, two different runtime modes.

## Permissions inheritance

Teammates start with lead's permission settings. If lead has `--dangerously-skip-permissions`, **all teammates do too**. Permission mode at spawn time is fixed; can be changed per-teammate after spawning.

## Plan approval gating

For complex/risky tasks:
```text
Spawn an architect teammate to refactor the authentication module.
Require plan approval before they make any changes.
```

Teammate works in read-only plan mode → submits plan to lead → lead approves or rejects with feedback. Lead makes approval decisions autonomously; give it criteria in your prompt.

## Quality gate hooks (new event types)

- `TeammateIdle` — exit code 2 sends feedback + keeps teammate working
- `TaskCreated` — exit code 2 prevents creation
- `TaskCompleted` — exit code 2 prevents completion

See [[source-claude-code-hooks-docs]] for the broader hook system.

## Known limitations (research preview)

- **No session resumption** of in-process teammates with `/resume` or `/rewind`
- Task status can lag; teammates sometimes fail to mark complete (blocks dependents)
- Shutdown can be slow
- **One team at a time** per lead
- **No nested teams** — teammates can't spawn their own
- Lead is fixed for team's lifetime (can't promote/transfer)
- Permissions set at spawn (can change after, can't set per-teammate at spawn)
- Split panes don't work in VS Code integrated terminal, Windows Terminal, or Ghostty

## Best practices (extracted)

- Give teammates enough context — they DON'T inherit lead's conversation history
- Start with 3–5 teammates. 5–6 tasks per teammate.
- Self-contained task sizing
- Wait for teammates to finish — sometimes lead starts implementing instead
- Start with research/review (clear boundaries, no code conflicts)
- **Partition work to avoid file conflicts** — agent teams DON'T auto-isolate via worktrees (unlike agent view)
- Monitor and steer

## Why this exists — and the gap it fills

Agent teams sit between [[source-claude-code-subagents-docs|subagents]] (one session, helpers report back) and [[claude-code-agent-view|agent view]] (many sessions, you orchestrate). It's the **"Claude orchestrates the team itself"** mode — closest to a multi-agent system in the GAN-inspired [[harness-design]] sense, but with self-coordination instead of fixed orchestration.

## Connections
- Related: [[claude-code]], [[multi-agent-architecture]], [[harness-design]], [[source-claude-code-subagents-docs]], [[claude-code-agent-view]], [[source-claude-code-agents-overview]], [[3-agent-starter-team]]
- This is the official "agent team" primitive that [[3-agent-starter-team|Khairallah's 3-agent starter]] pattern can now run natively on
- Pairs with [[source-claude-code-worktrees-docs]] for file isolation (which agent teams DON'T provide)

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-05-14 | raw/2026-05-14-anthropic-claude-code-agent-teams.md | Initial creation — new experimental concept, no prior wiki coverage |
