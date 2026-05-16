# Claude Code Official Docs — Run prompts on a schedule

Captured 2026-05-14 from https://code.claude.com/docs/en/scheduled-tasks.md

> Use /loop and the cron scheduling tools to run prompts repeatedly, poll for status, or set one-time reminders within a Claude Code session.

> [!note]
> Scheduled tasks require Claude Code v2.1.72 or later.

Scheduled tasks let Claude re-run a prompt automatically on an interval. Use them to poll a deployment, babysit a PR, check back on a long-running build, or remind yourself.

Tasks are session-scoped: they live in the current conversation and stop when you start a new one. Resuming with `--resume` or `--continue` brings back any task that hasn't expired. For scheduling that survives independently, use Routines, Desktop scheduled tasks, or GitHub Actions.

## Compare scheduling options

|  | Cloud (Routines) | Desktop | `/loop` |
| :--- | :--- | :--- | :--- |
| Runs on | Anthropic cloud | Your machine | Your machine |
| Requires machine on | No | Yes | Yes |
| Requires open session | No | No | Yes |
| Persistent across restarts | Yes | Yes | Restored on `--resume` if unexpired |
| Access to local files | No (fresh clone) | Yes | Yes |
| MCP servers | Connectors per task | Config files + connectors | Inherits from session |
| Permission prompts | No (autonomous) | Configurable | Inherits from session |
| Customizable schedule | Via `/schedule` | Yes | Yes |
| Minimum interval | 1 hour | 1 minute | 1 minute |

## Run a prompt repeatedly with /loop

| What you provide | Example | What happens |
| :--- | :--- | :--- |
| Interval and prompt | `/loop 5m check the deploy` | Runs on fixed schedule |
| Prompt only | `/loop check the deploy` | Runs at interval Claude chooses each iteration |
| Interval only, or nothing | `/loop` | Built-in maintenance prompt runs, or your `loop.md` if exists |

You can also pass another command as prompt: `/loop 20m /review-pr 1234`.

### Run on a fixed interval

```text
/loop 5m check if the deployment finished and tell me what happened
```

Interval can lead as `30m` or trail as `every 2 hours`. Units: `s`, `m`, `h`, `d`. Seconds rounded up to nearest minute. Intervals that don't map cleanly (7m, 90m) rounded.

### Let Claude choose the interval

When you omit interval, Claude picks delay between 1 min and 1 hour based on what it observed. Short while build finishing, longer when quiet.

```text
/loop check whether CI passed and address any review comments
```

When dynamic, Claude may use the Monitor tool directly. Monitor runs background script and streams each output line back.

Dynamically scheduled loop appears in scheduled task list. 7-day expiry applies. Jitter rules don't apply.

> [!note]
> On Bedrock, Vertex AI, and Microsoft Foundry, prompt with no interval runs on fixed 10-minute schedule.

### Run the built-in maintenance prompt

`/loop` alone runs built-in prompt that, in order:
* continue any unfinished work
* tend to current branch's PR (review comments, failed CI, merge conflicts)
* run cleanup passes (bug hunts, simplification) when nothing pending

Irreversible actions (push, delete) only proceed when continuing something the transcript authorized.

### Customize default prompt with loop.md

| Path | Scope |
| :--- | :--- |
| `.claude/loop.md` | Project-level (takes precedence) |
| `~/.claude/loop.md` | User-level |

Plain Markdown, no required structure. Edits take effect on next iteration. Truncated at 25,000 bytes.

### Stop a loop

`Esc` to stop while waiting for next iteration. Tasks scheduled by asking Claude directly aren't affected by Esc — delete them manually. In self-paced mode, Claude can end loop on its own.

## Set a one-time reminder

Natural language:
```text
remind me at 3pm to push the release branch
in 45 minutes, check whether the integration tests passed
```

Claude pins fire time to specific minute/hour using cron expression.

## Manage scheduled tasks

```text
what scheduled tasks do I have?
cancel the deploy check job
```

Under the hood Claude uses:

| Tool | Purpose |
| :--- | :--- |
| `CronCreate` | Schedule new task. 5-field cron, prompt, recurs or fires once. |
| `CronList` | List all tasks with IDs, schedules, prompts |
| `CronDelete` | Cancel by ID |

8-character ID. Up to 50 tasks per session.

## How scheduled tasks run

Scheduler checks every second. Scheduled prompt fires BETWEEN your turns, not mid-response. If Claude busy when due, waits until current turn ends.

Times in your local timezone. `0 9 * * *` = 9am wherever you're running Claude Code, not UTC.

### Jitter

Deterministic offset to avoid every session hitting API at same wall-clock moment:
* Recurring tasks: up to 30 min after scheduled time (or half the interval, for sub-hourly)
* One-shot at top/bottom of hour: up to 90 seconds early

Offset derived from task ID. If exact timing matters, pick minute that's not `:00` or `:30`.

### Seven-day expiry

Recurring tasks auto-expire 7 days after creation. Fires one final time, then deletes. Bounds how long forgotten loop runs. Cancel and recreate, or use Routines/Desktop for durable scheduling.

## Cron expression reference

Standard 5-field: `minute hour day-of-month month day-of-week`. Wildcards (`*`), single (`5`), steps (`*/15`), ranges (`1-5`), comma-separated (`1,15,30`).

| Example | Meaning |
| :--- | :--- |
| `*/5 * * * *` | Every 5 minutes |
| `0 * * * *` | Every hour on the hour |
| `0 9 * * *` | Every day at 9am local |
| `0 9 * * 1-5` | Weekdays at 9am local |

Day-of-week: 0 or 7 for Sunday through 6 for Saturday. Extended syntax (L, W, ?, name aliases) NOT supported. When both day-of-month and day-of-week constrained, date matches if either matches (vixie-cron semantics).

## Disable scheduled tasks

`CLAUDE_CODE_DISABLE_CRON=1` to disable scheduler entirely.

## Limitations

* Tasks only fire while Claude Code running and idle
* No catch-up for missed fires
* Starting fresh conversation clears all session-scoped tasks
* Background Bash and monitor tasks never restored on resume

For cron-driven automation that needs to run unattended:
* Routines: Anthropic-managed infrastructure
* GitHub Actions: schedule trigger in CI
* Desktop scheduled tasks: local on your machine
