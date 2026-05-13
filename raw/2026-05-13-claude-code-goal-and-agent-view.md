# Claude Code — Two New Features: `/goal` and Agent View

Captured 2026-05-13 from official Anthropic docs.

Sources:
- `/goal` reference: https://code.claude.com/docs/en/goal
- Agent view reference: https://code.claude.com/docs/en/agent-view
- Announcement blog (agent view): https://claude.com/blog/agent-view-in-claude-code

Both features change how long Claude can run unattended:
- `/goal` removes per-turn prompting inside a single session.
- **Agent view** removes the need to babysit individual terminals when running many sessions in parallel — one screen for all background sessions, dispatch new ones, peek and reply inline, attach when you want the full conversation.

---

## Feature 1: `/goal` — Keep Claude working toward a goal

> "The `/goal` command sets a completion condition and Claude keeps working toward it without you prompting each step. After each turn, a small fast model checks whether the condition holds. If not, Claude starts another turn instead of returning control to you. The goal clears automatically once the condition is met."

### Mechanics

- One goal per session. Setting a new goal replaces the old one.
- Setting a goal **starts a turn immediately** with the condition as the directive — no separate prompt needed.
- After every turn, the evaluator (a small fast model — Haiku by default) reads the conversation and returns yes/no + a short reason.
  - `no` → Claude does another turn, with the reason injected as guidance.
  - `yes` → goal clears, achievement entry recorded in the transcript.
- A `◎ /goal active` indicator shows duration while running.
- `/goal` with no args = status (condition, time, turns evaluated, token spend, evaluator's last reason).
- `/goal clear` (aliases: stop / off / reset / none / cancel) to abort early. `/clear` also removes the goal.
- Up to 4,000 characters for the condition.
- Resumes with `--resume` / `--continue` (condition preserved, but turn count, timer, token baseline reset).
- Works in non-interactive mode: `claude -p "/goal CHANGELOG.md has an entry for every PR merged this week"`. Ctrl+C to stop.

### Implementation detail

`/goal` is a wrapper around a **session-scoped prompt-based Stop hook**. The evaluator is part of the hook system, so:
- It runs only in trusted workspaces (trust dialog accepted).
- Unavailable when `disableAllHooks` is set at any settings level, or when `allowManagedHooksOnly` is set in managed settings.
- The evaluator does NOT call tools — it can only judge what Claude has surfaced in the conversation.

### How to write an effective condition

The doc is explicit: the condition must be checkable from the **transcript**, because the evaluator can't run commands or read files independently. Three components of a good condition:

1. **One measurable end state** — test result, build exit code, file count, empty queue.
2. **A stated check** — how Claude should prove it. e.g., "`npm test` exits 0" or "`git status` is clean".
3. **Constraints that matter** — invariants that must not change on the way there. e.g., "no other test file is modified".

To bound runtime: add a turn or time clause, e.g., `... or stop after 20 turns`. Claude reports progress against the clause each turn.

### Comparison with other autonomous workflows

| Approach     | Next turn starts when      | Stops when                                      |
| ------------ | -------------------------- | ----------------------------------------------- |
| `/goal`      | The previous turn finishes | A model confirms the condition is met           |
| `/loop`      | A time interval elapses    | You stop it, or Claude decides the work is done |
| Stop hook    | The previous turn finishes | Your own script or prompt decides               |
| Auto mode    | (per tool call, not turn)  | Claude judges work done                         |

### Cost note

Evaluator tokens are billed on the small fast model (Haiku default) — "typically negligible compared to main-turn spend."

---

## Feature 2: Agent View — One screen for all background sessions

> "Agent view, opened with `claude agents`, is one screen for all your background sessions: what's running, what needs your input, and what's done. Dispatch new sessions, watch their state at a glance instead of scrolling through transcripts, and step in only when one needs you."

**Announced:** 2026-05-11 as Research Preview. Requires Claude Code v2.1.139+. Available on Pro, Max, Team, Enterprise, and Claude API plans.

### Core problem solved

> "When running agents in parallel before, you've probably had to manage multiple terminal tabs, a tmux grid, and an overloaded mental ledger of what you need to tackle next."

Agent view replaces the tmux-grid pattern. One TUI table; rows are sessions; status icons and last-activity timestamps show progress; you only step in when a row needs you.

### Mechanics

#### Opening it
- From shell: `claude agents`
- From any session: `←` on an empty prompt (backgrounds current session + opens agent view with it pre-selected)
- Press `Esc` to return to shell — **sessions keep running** while you're away

#### Layout

Sessions are grouped by **state**, with the ones that need you at the top:
- **Pinned** (anything you pinned with `Ctrl+T`)
- **Ready for review** (has an open PR)
- **Needs input** (waiting on permission or question)
- **Working** (actively running)
- **Completed** (finished/failed/stopped)

Each row shows: state icon, session name, current activity / last response / PR URL, last interaction time, optional PR status dot.

Toggle grouping between state and directory with `Ctrl+S`.

#### State icons

| State       | Icon          | Meaning                                                              |
| ----------- | ------------- | -------------------------------------------------------------------- |
| Working     | Animated      | Actively running tools or generating                                 |
| Needs input | Yellow        | Waiting on a question or permission                                  |
| Idle        | Dimmed        | Nothing to do, ready for next prompt                                 |
| Completed   | Green         | Task finished successfully                                           |
| Failed      | Red           | Ended with error                                                     |
| Stopped     | Grey          | Stopped with `Ctrl+X` or `claude stop`                               |

Plus icon **shape** = process status:
- `✻` or `✽` = process alive, replies immediately
- `∙` = process exited; you can still peek/reply/attach; Claude restarts from where it left off
- `✢` = a `/loop` session sleeping between iterations; row shows run count + countdown

#### Pull request status dot
| Color  | Meaning                                       |
| ------ | --------------------------------------------- |
| Yellow | Waiting on checks/review, or checks failed    |
| Green  | Checks passed, no blocking review             |
| Purple | Merged                                        |
| Grey   | Draft or closed                               |

#### Row summary
Generated by a **Haiku-class model**. Refreshes at most once every 15 seconds while a session is working, plus once at each turn end. Billed under the session's normal data usage terms.

### Three ways to interact with a session

1. **Peek** (`Space`) — opens a side panel showing the session's most recent output OR the question it's waiting on, OR PRs it opened. Type a reply, press `Enter`, sent without leaving agent view. For multi-choice questions: number keys pick an option. Press `Tab` for a suggested reply you can edit. Prefix with `!` to send a Bash command. `↑`/`↓` peek at adjacent rows; `→` attaches.

2. **Attach** (`Enter` or `→`) — agent view is replaced by the full session, exactly as `claude` in that directory. Claude posts a recap of what happened while you were away. Every shortcut + command works as normal. `←` on empty prompt detaches and returns to agent view.

3. **Background again** (`/bg` inside a session, or `←` on empty prompt) — sends it back to the table.

Detaching never stops a session. To end a session from inside it: `/stop`. From shell: `claude stop <id>`.

### Dispatch new agents — three entry points

#### From agent view
Type prompt in the bottom input, press `Enter`. Each prompt starts its **own session** — typing again launches a second one, not a follow-up. Session auto-named from the prompt; rename with `Ctrl+R`.

Prompt prefixes / mentions:
| Input                             | Effect                                                                       |
| --------------------------------- | ---------------------------------------------------------------------------- |
| `<agent-name> <prompt>`           | First word matches a subagent → runs as the session's main agent             |
| `@<agent-name>`                   | Mention a subagent anywhere                                                  |
| `@<repo>`                         | Run in a sibling repository under the directory you opened agent view from   |
| `/<skill>`                        | Suggest skills as the dispatch                                               |
| `#<number>` or PR URL             | If a session is already on that PR, select it instead of dispatching         |
| `Shift+Enter`                     | Dispatch and immediately attach                                              |

Paste an image into the prompt to attach a screenshot/diagram.

#### From inside a session
- `/bg` (or `/background`) — moves the current conversation to a background session.
- `/bg <extra prompt>` — moves to background AND gives one more instruction.
- Caveat: backgrounding starts a fresh process that resumes from saved conversation. Running subagents and background commands do NOT transfer. Claude asks to confirm if any are running.

#### From the shell
```bash
claude --bg "investigate the flaky SettingsChangeDetector test"
claude --agent code-reviewer --bg "address review comments on PR 1234"
```
After backgrounding, Claude prints the short ID and commands:
- `claude attach <id>` — open in this terminal
- `claude logs <id>` — show recent output
- `claude stop <id>` — stop session
- `claude respawn <id>` — restart a stopped session with conversation intact
- `claude respawn --all` — restart everything (e.g., after machine sleep)
- `claude rm <id>` — remove from list, cleans up worktree if no uncommitted changes

### Filtering

Type in the dispatch input to filter:
| Filter                  | Shows                                                                  |
| ----------------------- | ---------------------------------------------------------------------- |
| `a:<name>`              | Sessions running the named agent                                       |
| `s:<state>`             | Sessions in state (e.g., `s:working`; `s:blocked` = all waiting on you) |
| `#<number>` or PR URL   | The session working on that PR                                         |

### Keyboard shortcuts (most useful)

| Shortcut              | Action                                                                              |
| --------------------- | ----------------------------------------------------------------------------------- |
| `↑` / `↓`             | Move between rows                                                                   |
| `Space`               | Peek panel                                                                          |
| `Enter`               | Attach to selected (or dispatch if input has text)                                  |
| `Shift+Enter`         | Dispatch and attach immediately                                                     |
| `→`                   | Attach                                                                              |
| `Alt+1..9`            | Attach to session 1–9 in current group                                              |
| `Tab`                 | On empty input: browse subagents. Otherwise apply highlighted suggestion            |
| `Ctrl+S`              | Switch grouping: state ↔ directory                                                  |
| `Ctrl+T`              | Pin/unpin selected session                                                          |
| `Ctrl+R`              | Rename                                                                              |
| `Ctrl+G`              | Open dispatch prompt in `$EDITOR`                                                   |
| `Ctrl+X`              | Stop session; press again within 2s to **delete**                                   |
| `Shift+↑` / `Shift+↓` | Reorder                                                                             |
| `←`                   | (on empty prompt) Detach OR background current session + open agent view           |
| `?`                   | All shortcuts                                                                       |

### File-edit isolation (important)

Every background session runs in your working directory. **Before editing files, Claude moves the session into an isolated git worktree under `.claude/worktrees/`**, so parallel sessions can read the same checkout but each writes to its own. Skipped when:
- Already under `.claude/worktrees/`
- Not in a git repo
- Writes outside the working directory

**Outside a git repo, parallel sessions writing to the same files conflict.** Avoid this.

The worktree is removed when you delete the session, so **commit or push before deleting**. To make a subagent always isolated, set `isolation: worktree` in its frontmatter.

### Hosting model — the supervisor process

- A per-user **supervisor process** hosts all background sessions, separate from your terminal.
- Starts automatically the first time you background a session or open agent view.
- Same credentials as your interactive sessions; no additional network connections beyond the model API.
- Each background session = its own Claude Code process, managed by the supervisor.
- Auto-stop: after a session sits unattached for ~1 hour, its process is stopped to free resources. Transcript + state persist on disk. Reattach → fresh process from where it left off (slight delay).
- Supervisor watches the Claude Code binary for auto-updates and restarts into the new version without losing sessions.

### State persistence

| Path                             | Contents                                                                  |
| -------------------------------- | ------------------------------------------------------------------------- |
| `~/.claude/daemon.log`           | Supervisor log                                                            |
| `~/.claude/daemon/roster.json`   | Running background sessions, used to reconnect after restart              |
| `~/.claude/jobs/<id>/state.json` | Per-session state shown in agent view                                     |

`CLAUDE_CONFIG_DIR` overrides the location — separate supervisor instance with its own sessions.

### Per-session model and permissions

- Header shows the **dispatch default** model — every new session uses this unless overridden.
- Override per-session: `--model` with `claude --bg`, or `/model` inside an attached session (persists across respawns), or via a subagent's `model` frontmatter.
- A dispatched session reads settings and permission mode from its directory, same as `claude` in that directory.
- `bypassPermissions` or `auto` via `--permission-mode` is refused until you've accepted that mode interactively at least once — guard against unwatched sessions.

### Real-world usage patterns (from announcement blog)

- **Concurrent scaling**: dispatch many ideas at once, each optionally paired with skills → multiple PRs to review.
- **Long-running management**: PR monitoring and dashboard-update jobs; rows show next run times.
- **Session navigation**: switching between related tasks while maintaining context.
- **Progress tracking**: status indicators + titles let you see which sessions produced PRs.

### Turn off / opt out

- `disableAgentView` setting = true
- `CLAUDE_CODE_DISABLE_AGENT_VIEW` env var
- Admins can enforce via managed settings

### Limitations (research preview)

- **Rate limits apply per session** — 10 sessions in parallel = 10× quota burn.
- **Sessions are local** — stop on sleep/shutdown. Use `claude respawn --all` to bring them back.
- **Worktrees are deleted with the session** — merge/push before deletion.
- Earlier versions don't open agent view in Bedrock/Vertex/Foundry environments — run `claude update`.
- Prompts under 4 characters rejected as "too short" (anti-stray-keystroke guard).

### Comparison with other parallel-execution primitives

| Primitive          | Best for                                              |
| ------------------ | ----------------------------------------------------- |
| Agent view         | Running many independent Claude Code sessions side by side, with peek/reply/attach UI |
| Subagents          | One session dispatching specialized sub-tasks within its own turn |
| Agent teams        | Multiple sessions that need to coordinate / message each other |
| Worktrees          | Filesystem isolation for parallel edits (used under the hood by agent view) |
| Claude Code on web | Sessions hosted on Anthropic infra, not your machine  |

---

## How `/goal` and Agent View fit together

- **Agent view** = the orchestration screen for many sessions.
- **`/goal`** = the loop driver inside one session.

Pattern: dispatch many `/goal` sessions in agent view. Each row works toward its condition without your input. The row updates as the evaluator decides yes/no. You only step in when a row says `Needs input` or `Completed`. The combination is **the closest thing to fire-and-forget parallel agents** Claude Code currently ships.

Concrete example:
```bash
claude --bg "/goal investigate flaky tests in test/auth, fix any race conditions you can identify, all 12 tests in test/auth pass, no other test file modified — or stop after 15 turns"
claude --bg "/goal migrate src/legacy/* from callback style to async/await; every call site builds; tsc exits 0; no behavior change in tests — or stop after 25 turns"
claude --bg "/goal triage all open issues labeled 'bug', for each one write a short root-cause hypothesis as a comment, until the labeled queue is empty — or stop after 20 turns"
```
Open `claude agents`, three rows running. Pin (`Ctrl+T`) the one you care about most. Peek (`Space`) to check progress without losing focus. Reply inline if one needs you. The supervisor keeps everything alive across terminal closes.
