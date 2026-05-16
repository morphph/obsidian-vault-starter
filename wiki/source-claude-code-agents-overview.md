---
type: source-summary
created: 2026-05-14
last-updated: 2026-05-14
sources:
  - raw/2026-05-14-anthropic-claude-code-agents-overview.md
tags: [claude-code, official-docs, parallel-work, subagents, agent-view, agent-teams, worktrees]
---

# Source: Run agents in parallel (overview)

## Summary
Official Anthropic doc at `code.claude.com/docs/en/agents` that **compares the four ways Claude Code parallelizes work**: subagents, agent view, agent teams, worktrees — plus the *planned* `/batch` primitive. The canonical "which one do I use when" reference page for [[claude-code]]'s parallel-execution surface. Anchors the entire "Agents and parallel work" section in the official docs sidebar.

## The four-axis comparison

| Approach | What it gives you | Use it when |
| :--- | :--- | :--- |
| [[source-claude-code-subagents-docs\|Subagents]] | Delegated workers inside one session, own context, return summary | Side task would flood main conversation with logs/search results |
| [[claude-code-agent-view\|Agent view]] | One screen to dispatch + monitor background sessions (`claude agents`). Research preview | Several independent tasks; hand off + check status |
| [[source-claude-code-agent-teams-docs\|Agent teams]] | Coordinated sessions with shared task list + inter-agent messaging, managed by lead. **Experimental, disabled by default** | Claude splits project into pieces, assigns, keeps workers in sync |
| [[source-claude-code-worktrees-docs\|Worktrees]] | Separate git checkouts so parallel sessions never touch each other's files | Several sessions yourself, or subagents edit overlapping files |
| `/batch` (planned) | One large change split into 5–30 worktree-isolated subagents each opening a PR | Repo-wide migration or mechanical refactor in one instruction |

In every approach the workers are Claude sessions. Other tools come in as MCP servers.

## The 3 decision questions

1. **Who coordinates?** Inside one conversation → subagents. Independent tasks you check back on → agent view. Claude plans/assigns/supervises → agent teams.
2. **Do workers need to talk?** Subagents report back; agent view reports only to you; agent-team teammates message each other directly + share task list.
3. **Same files?** Isolate with worktrees. Agent teams DON'T auto-isolate teammates — partition the work.

## "Check on running work" — three commands, easy to confuse

| Command | What it shows |
| :--- | :--- |
| `claude agents` | [[claude-code-agent-view\|Agent view]]: every background session, its state, which need input |
| `/agents` | Subagents in current session: Running tab + Library tab for create/edit. **Despite the name, separate from `claude agents`** |
| `/tasks` | Everything running in the background of current session |

This naming overlap is a known footgun — flagged in the official doc itself.

## Combinability

- Agent view automatically moves each dispatched session into its own worktree when it edits files
- A session can spawn subagents that each get their own worktree
- These compose

## Connections
- Related: [[claude-code]], [[claude-code-agent-view]], [[multi-agent-architecture]], [[forked-agent-pattern]], [[3-agent-starter-team]], [[ralph-wiggum]]
- Pairs with all four sub-topic source pages: [[source-claude-code-subagents-docs]], [[source-claude-code-agent-teams-docs]], [[source-claude-code-worktrees-docs]], [[claude-code-agent-view]]
- The overview that should have shipped with [[source-claude-code-goal-and-agent-view-docs]] — agent view + `/goal` are the loop driver, this is the surface map.

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-05-14 | raw/2026-05-14-anthropic-claude-code-agents-overview.md | Initial creation from official overview |
