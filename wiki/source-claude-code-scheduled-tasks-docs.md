---
type: source-summary
created: 2026-05-14
last-updated: 2026-05-14
sources:
  - raw/2026-05-14-anthropic-claude-code-scheduled-tasks.md
tags: [claude-code, official-docs, loop, scheduled-tasks, cron, session-scoped]
---

# Source: Run prompts on a schedule (in-session `/loop` + cron)

## Summary
Official Anthropic doc on **`/loop` and session-scoped scheduled tasks** in [[claude-code]] — re-run a prompt on an interval, poll for status, set one-time reminders. Tasks are **session-scoped**: live in current conversation, restored on `--resume`/`--continue` if unexpired. Requires v2.1.72+. **The local/in-session counterpart to [[source-claude-code-routines-docs|cloud Routines]]** — three scheduling tiers covering different durability needs.

## The three scheduling tiers — comparison

|  | [[source-claude-code-routines-docs\|Cloud Routines]] | Desktop scheduled tasks | `/loop` (this doc) |
| :--- | :--- | :--- | :--- |
| Runs on | Anthropic cloud | Your machine | Your machine |
| Requires machine on | No | Yes | Yes |
| Requires open session | **No** | No | **Yes** |
| Persistent across restarts | Yes | Yes | Restored on `--resume` if unexpired |
| Access to local files | No (fresh clone) | Yes | Yes |
| MCP servers | Connectors per task | Config + connectors | Inherits from session |
| Permission prompts | None (autonomous) | Configurable | Inherits from session |
| Minimum interval | 1 hour | 1 minute | 1 minute |

> [!tip]
> Cloud Routines for unattended. Desktop scheduled tasks when need local files. `/loop` for quick polling during a session.

## `/loop` — three usage modes

| Provided | Example | Behavior |
| :--- | :--- | :--- |
| Interval + prompt | `/loop 5m check the deploy` | Fixed schedule (cron) |
| Prompt only | `/loop check the deploy` | **Claude picks interval dynamically** each iteration |
| Interval only / nothing | `/loop` or `/loop 15m` | Built-in maintenance prompt (or your `loop.md`) |

Can pass other commands: `/loop 20m /review-pr 1234`.

### Dynamic interval mode

When you omit the interval, Claude picks a delay 1 min – 1 hour based on context: short while build finishing, longer when quiet. The chosen delay + reason printed each iteration. **Claude may use the [[claude-code-monitor-tool|Monitor tool]] directly** instead of polling — more token-efficient than re-running prompts.

A dynamic loop appears in scheduled task list normally. 7-day expiry applies. No jitter rules.

> [!note]
> On Bedrock/Vertex/Foundry, prompt with no interval runs on **fixed 10-minute schedule** (model fallback).

### Built-in maintenance prompt

Bare `/loop` runs prompt that:
1. Continues any unfinished work
2. Tends to current branch's PR (review comments, failed CI, merge conflicts)
3. Runs cleanup passes (bug hunts, simplification) when nothing pending

**Irreversible actions (push/delete) only proceed when continuing something transcript already authorized.**

### `loop.md` override

`.claude/loop.md` (project, takes precedence) or `~/.claude/loop.md` (user). Plain markdown, no required structure. Edits take effect on next iteration. Truncated at 25,000 bytes.

## One-time reminders (natural language)

```text
remind me at 3pm to push the release branch
in 45 minutes, check whether the integration tests passed
```

Claude pins fire time to specific minute/hour using cron. Auto-deletes after firing.

## Cron tool reference (`CronCreate`/`CronList`/`CronDelete`)

| Tool | Purpose |
| :--- | :--- |
| `CronCreate` | Schedule task. 5-field cron + prompt + recurs/once flag |
| `CronList` | List all with IDs (8 chars) |
| `CronDelete` | Cancel by ID |

Max 50 scheduled tasks per session.

5-field cron format. Standard wildcards/steps/ranges/lists. **Day-of-week: 0 or 7 = Sunday through 6 = Saturday.** Extended syntax (`L`, `W`, `?`, name aliases) NOT supported. When both day-of-month AND day-of-week constrained, date matches if **either** matches (vixie-cron semantics).

## How tasks run — the fire mechanics

- Scheduler checks every second
- Tasks fire **between turns**, not mid-response
- If Claude busy when due, waits until current turn ends
- Times in **local timezone** (not UTC)

### Jitter (deterministic offset)

To avoid every session hitting API at same wall-clock moment:
- Recurring: up to 30 min after scheduled time (or half interval if sub-hourly)
- One-shot at `:00`/`:30`: up to 90 seconds early

Offset derived from task ID — same task always gets same offset. **If exact timing matters, pick minute that's not `:00` or `:30`** (e.g., `3 9 * * *` instead of `0 9 * * *`).

### Seven-day expiry

Recurring tasks auto-expire 7 days after creation. Fires one final time, then deletes. **Bounds how long a forgotten loop runs.** For longer: cancel + recreate, or use [[source-claude-code-routines-docs|Routines]]/Desktop.

## Limitations

- Tasks only fire while Claude Code is running AND idle
- **No catch-up for missed fires** — fires once when Claude becomes idle, not once per missed interval
- Starting fresh conversation clears all session-scoped tasks
- Background Bash and monitor tasks **never restored** on resume
- Disable entirely: `CLAUDE_CODE_DISABLE_CRON=1`

## Connection to our `/schedule` skill

The local `/schedule` skill I have access to creates [[source-claude-code-routines-docs|cloud Routines]], not `/loop` tasks. **Two different scheduling systems share the term `/schedule`** — the cron tools above (`CronCreate`/`CronList`/`CronDelete`) drive `/loop`; the `/schedule` skill drives cloud Routines.

## Connections
- Related: [[claude-code]], [[source-claude-code-routines-docs]], [[claude-code-monitor-tool]], [[claude-code-goal]], [[source-claude-code-channels-docs]], [[ralph-wiggum]]
- Sibling to [[claude-code-monitor-tool]] — both poll-vs-event-driven primitives, both session-scoped
- Resolves "what is `/loop`" — previously vague mention in [[claude-code]] now has canonical spec

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-05-14 | raw/2026-05-14-anthropic-claude-code-scheduled-tasks.md | Initial creation from official scheduled tasks docs |
