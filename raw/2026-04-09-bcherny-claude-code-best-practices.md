# Boris Cherny's Claude Code Best Practices — Complete Guide

**Source:** 3 threads by @bcherny on X
- https://x.com/bcherny/status/2007179832300581177 (personal setup, 15 tips)
- https://x.com/bcherny/status/2017742741636321619 (team tips, 10 practices)
- https://x.com/bcherny/status/2038454336355999749 (hidden features, 15 features, 2.3M views)
**Author:** Boris Cherny (@bcherny) — Creator of Claude Code, Anthropic, 388K followers
**Published:** 2026-03 to 2026-04
**Fetch method:** Playwright MCP (profile) + WebFetch (twitter-thread.com) + WebSearch
**Cross-referenced with:** Anthropic official docs (code.claude.com/docs)

---

## Thread 1: Boris's Personal Setup (15 Tips)

### Parallel Sessions
- Runs 5 Claudes in parallel in terminal with numbered tabs + system notifications
- Also runs 5-10 concurrent sessions on claude.ai/code
- Uses iOS app for additional instances
- "My setup might be surprisingly vanilla! Claude Code works great out of the box."

### Model Selection
- Uses Opus 4.5 with thinking for everything
- "It's the best coding model I've used"
- Even though bigger and slower than Sonnet, usually faster overall due to better steering and tool use

### Team Knowledge Management
- Team maintains shared CLAUDE.md checked into git
- Whole team contributes multiple times a week
- During code reviews, tag @.claude to update CLAUDE.md via GitHub Action
- "After every correction, end with: 'Update your CLAUDE.md so you don't make that mistake again.'"

### Plan Mode Workflow
- Sessions typically start in Plan mode (Shift+Tab twice)
- Goes back and forth with Claude until plan looks good
- Then switches to auto-accept edits mode
- Claude usually completes in one shot after good planning
- Pro move: one Claude writes plan, second Claude reviews like a staff engineer

### Slash Commands
- Uses slash commands for every "inner loop" workflow done many times a day
- `/commit-push-pr` used dozens of times daily
- Stored in `.claude/commands/`, committed to git for team reuse
- Uses inline bash in commands for efficiency

### Subagents
- Uses subagents: code-simplifier, verify-app
- "Append 'use subagents' to any request where you want Claude to throw more compute at the problem"
- Routes permission requests to Opus 4.5 for attack scanning and auto-approval
- Keeps main agent's context focused

### Hooks
- PostToolUse hooks for auto-formatting
- Pre-configured permissions in `.claude/settings.json`
- Notification hooks for desktop alerts

### Verification
- "Give Claude a way to verify its work" — most critical practice
- Chrome extension for frontend work
- "Once you do that, Claude will iterate until the result is great"
- Repeats iterations until quality meets standards

## Thread 2: Team Tips (10 Practices)

### Tip 1: Do More in Parallel
- "Spin up 3–5 git worktrees at once, each running its own Claude session in parallel"
- Team's biggest productivity unlock
- Shell aliases (za, zb, zc) for quick switching
- Some maintain dedicated analysis worktrees for logs/BigQuery

### Tip 2: Start Complex Tasks in Plan Mode
- Pour energy into detailed planning → Claude executes in one attempt
- Have one Claude write plan, spawn second Claude to review like staff engineer
- When issues arise, return to planning rather than continuing with flawed approach

### Tip 3: Invest in CLAUDE.md
- "After every correction, end with: 'Update your CLAUDE.md so you don't make that mistake again.'"
- Claude excels at self-directed rule creation
- Ruthlessly edit over time until error rates measurably drop
- Some maintain task-specific notes directories

### Tip 4: Create Reusable Skills
- "If you do something more than once a day, turn it into a skill or command"
- Tech debt identification, context syncing from multiple tools, analytics workflows
- Commit to git for project reuse

### Tip 5: Let Claude Fix Bugs Independently
- Slack MCP integration — paste bug threads, say "fix"
- Claude can troubleshoot failing CI tests and docker logs without micromanagement
- "Surprising capability with distributed systems"

### Tip 6: Level Up Prompting
- Ask Claude to "grill" changes before PRs
- Ask it to prove implementations work via behavior diffs
- Request elegant reimplementations after mediocre solutions
- Provide detailed specs reducing ambiguity beforehand

### Tip 7: Terminal & Environment Setup
- Team endorses Ghostty terminal
- Customize status bars using /statusline
- Voice dictation: "You speak 3x faster than you type, and your prompts get way more detailed"

### Tip 8: Use Subagents
- "Append 'use subagents' to any request where you want Claude to throw more compute at the problem"
- Offload tasks to keep main agent's context focused
- Route permission requests to Opus 4.5 for attack scanning and auto-approval

### Tip 9: Use Claude for Data & Analytics
- Use "bq" CLI through Claude Code for BigQuery
- "Personally, I haven't written a line of SQL in 6+ months"
- Works with any database with CLI, MCP, or API access

### Tip 10: Learning with Claude
- Enable "Explanatory" or "Learning" output styles
- Request HTML presentations of unfamiliar code
- Ask for ASCII diagrams of protocols and codebases
- Build spaced-repetition skills for knowledge retention

## Thread 3: Hidden Features (15 Features, 2.3M views)

### Mobile & Session Mobility
- iOS/Android app via Code tab — code without opening laptop
- `claude --teleport` or `/teleport` — continue cloud session locally
- `/remote-control` — control local session from phone/web
- Enable "Remote Control for all sessions" in config

### Automation
- `/loop` — run tasks at intervals (e.g., `/loop 5m /babysit`, `/loop 30m /slack-feedback`)
- `/schedule` — schedule Claude to run automatically, up to a week
- Cowork Dispatch — secure remote control for Claude Desktop app (Slack, email, file management)

### Development Features
- Chrome extension — Claude verifies its own frontend output visually
- Desktop app auto-starts and tests web servers with browser preview
- `/branch` — fork current session to explore alternatives
- `/btw` — side query while agent continues working

### Parallel & Scale
- Git worktrees: `claude -w` for new worktree sessions
- `/batch` — distributed changesets across dozens/hundreds/thousands of worktree agents
- Boris has "dozens of Claudes running at all times"

### Advanced
- `--bare` flag — 10x faster SDK startup for non-interactive use
- `--add-dir` — grant access to multiple repos simultaneously
- `--agent` — custom system prompts and tools from `.claude/agents/`
- `/voice` — voice input. Boris: "I do most of my coding by speaking to Claude"
