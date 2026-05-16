# Claude Code Official Docs — Orchestrate teams of Claude Code sessions

Captured 2026-05-14 from https://code.claude.com/docs/en/agent-teams.md

> Coordinate multiple Claude Code instances working together as a team, with shared tasks, inter-agent messaging, and centralized management.

> [!warning]
> Agent teams are experimental and disabled by default. Enable them by adding `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS` to your settings.json or environment. Agent teams have known limitations around session resumption, task coordination, and shutdown behavior.

Agent teams let you coordinate multiple Claude Code instances working together. One session acts as the team lead, coordinating work, assigning tasks, and synthesizing results. Teammates work independently, each in its own context window, and communicate directly with each other.

Unlike subagents, which run within a single session and can only report back to the main agent, you can also interact with individual teammates directly without going through the lead.

> [!note]
> Agent teams require Claude Code v2.1.32 or later. Check your version with `claude --version`.

## When to use agent teams

Agent teams are most effective for tasks where parallel exploration adds real value. The strongest use cases are:

* **Research and review**: multiple teammates can investigate different aspects of a problem simultaneously, then share and challenge each other's findings
* **New modules or features**: teammates can each own a separate piece without stepping on each other
* **Debugging with competing hypotheses**: teammates test different theories in parallel and converge on the answer faster
* **Cross-layer coordination**: changes that span frontend, backend, and tests, each owned by a different teammate

Agent teams add coordination overhead and use significantly more tokens than a single session. They work best when teammates can operate independently. For sequential tasks, same-file edits, or work with many dependencies, a single session or subagents are more effective.

### Compare with subagents

Subagents only report results back to the main agent and never talk to each other. In agent teams, teammates share a task list, claim work, and communicate directly with each other.

|  | Subagents | Agent teams |
| :--- | :--- | :--- |
| Context | Own context window; results return to the caller | Own context window; fully independent |
| Communication | Report results back to the main agent only | Teammates message each other directly |
| Coordination | Main agent manages all work | Shared task list with self-coordination |
| Best for | Focused tasks where only the result matters | Complex work requiring discussion and collaboration |
| Token cost | Lower: results summarized back to main context | Higher: each teammate is a separate Claude instance |

Use subagents when you need quick, focused workers that report back. Use agent teams when teammates need to share findings, challenge each other, and coordinate on their own.

## Enable agent teams

```json
{
  "env": {
    "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"
  }
}
```

## Start your first agent team

```text
I'm designing a CLI tool that helps developers track TODO comments across
their codebase. Create an agent team to explore this from different angles: one
teammate on UX, one on technical architecture, one playing devil's advocate.
```

The lead's terminal lists all teammates. Use Shift+Down to cycle through teammates and message them directly.

## Control your agent team

### Choose a display mode

* **In-process**: all teammates run inside your main terminal. Use Shift+Down to cycle through teammates.
* **Split panes**: each teammate gets its own pane. Requires tmux, or iTerm2.

The default is `"auto"`, which uses split panes if you're already running inside a tmux session, and in-process otherwise.

```json
{
  "teammateMode": "in-process"
}
```

```bash
claude --teammate-mode in-process
```

### Specify teammates and models

```text
Create a team with 4 teammates to refactor these modules in parallel.
Use Sonnet for each teammate.
```

Teammates don't inherit the lead's `/model` selection by default. Set "Default teammate model" in `/config`.

### Require plan approval for teammates

```text
Spawn an architect teammate to refactor the authentication module.
Require plan approval before they make any changes.
```

The teammate works in read-only plan mode until the lead approves their approach.

### Talk to teammates directly

* **In-process mode**: Shift+Down to cycle through teammates, type to send a message. Enter to view a teammate's session, Escape to interrupt. Ctrl+T toggles task list.
* **Split-pane mode**: click into a teammate's pane.

### Assign and claim tasks

Tasks have three states: pending, in progress, completed. Tasks can depend on other tasks. The lead assigns explicitly, or teammates self-claim. Task claiming uses file locking to prevent race conditions.

### Shut down teammates / Clean up the team

```text
Ask the researcher teammate to shut down
Clean up the team
```

> [!warning]
> Always use the lead to clean up. Teammates should not run cleanup.

### Enforce quality gates with hooks

* **TeammateIdle**: exit code 2 to send feedback and keep teammate working
* **TaskCreated**: exit code 2 to prevent creation
* **TaskCompleted**: exit code 2 to prevent completion

## How agent teams work

### Architecture

| Component | Role |
| :--- | :--- |
| Team lead | Main Claude Code session that creates the team |
| Teammates | Separate Claude Code instances |
| Task list | Shared list of work items |
| Mailbox | Messaging system for communication |

Teams and tasks stored locally:
* Team config: `~/.claude/teams/{team-name}/config.json`
* Task list: `~/.claude/tasks/{team-name}/`

### Use subagent definitions for teammates

```text
Spawn a teammate using the security-reviewer agent type to audit the auth module.
```

The teammate honors that definition's `tools` allowlist and `model`. The definition's body is appended to the teammate's system prompt as additional instructions.

> [!note]
> The `skills` and `mcpServers` frontmatter fields are not applied when a subagent definition runs as a teammate.

### Permissions

Teammates start with the lead's permission settings. If the lead runs with `--dangerously-skip-permissions`, all teammates do too.

### Context and communication

Each teammate has its own context window. When spawned, a teammate loads CLAUDE.md, MCP servers, and skills. The lead's conversation history does not carry over.

* **Automatic message delivery**: messages delivered automatically
* **Idle notifications**: teammate auto-notifies lead when stopping
* **Shared task list**: all agents see task status
* **Teammate messaging**: send message to one specific teammate by name

### Token usage

Significantly more tokens than a single session. Each teammate has its own context window.

## Use case examples

### Run a parallel code review

```text
Create an agent team to review PR #142. Spawn three reviewers:
- One focused on security implications
- One checking performance impact
- One validating test coverage
Have them each review and report findings.
```

### Investigate with competing hypotheses

```text
Users report the app exits after one message instead of staying connected.
Spawn 5 agent teammates to investigate different hypotheses. Have them talk to
each other to try to disprove each other's theories, like a scientific
debate. Update the findings doc with whatever consensus emerges.
```

## Best practices

* **Give teammates enough context** — include task-specific details in spawn prompt
* **Choose appropriate team size** — start with 3-5 teammates. Having 5-6 tasks per teammate keeps everyone productive
* **Size tasks appropriately** — self-contained units with clear deliverable
* **Wait for teammates to finish** — sometimes the lead starts implementing instead of waiting
* **Start with research and review** — clear boundaries, no code writing
* **Avoid file conflicts** — partition work so each teammate owns different files
* **Monitor and steer** — check in on teammates' progress

## Troubleshooting

* Teammates not appearing: Shift+Down to cycle in in-process mode
* Too many permission prompts: pre-approve common operations
* Teammates stopping on errors: give additional instructions or spawn replacement
* Lead shuts down before work is done: tell it to keep going
* Orphaned tmux sessions: `tmux ls`, `tmux kill-session -t <session-name>`

## Limitations

* **No session resumption with in-process teammates**: `/resume` and `/rewind` do not restore in-process teammates
* **Task status can lag**: teammates sometimes fail to mark tasks complete
* **Shutdown can be slow**
* **One team at a time**: a lead can only manage one team
* **No nested teams**: teammates cannot spawn their own teams
* **Lead is fixed**: cannot promote a teammate to lead
* **Permissions set at spawn**: all teammates start with lead's permission mode
* **Split panes require tmux or iTerm2**

## Next steps

* Lightweight delegation: subagents
* Manual parallel sessions: Git worktrees
