---
type: learning
date: 2026-06-04
source: https://claude.com/blog/a-harness-for-every-task-dynamic-workflows-in-claude-code
status: in-progress
---

# Learning: Dynamic Workflows in Claude Code

## Gist
The default Claude Code does everything inside ONE context window — it plans and executes
in the same place. That's fine for normal coding, but on big, parallel, or adversarial
tasks it starts failing in predictable ways (gives up early, trusts its own work, forgets
the original goal). **Dynamic workflows** fix this: Claude writes a small JavaScript program
on the fly that spawns and coordinates many subagents, each with its own fresh context
window and a narrow job. The article explains why this helps, the reusable orchestration
patterns (fan-out, adversarial verify, tournament, loop-until-done, etc.), where it shines
(research, migrations, triage, sorting, root-cause), and when NOT to bother (it costs more
tokens; most coding tasks don't need it).

## Mastery checklist
### 1. The problem — what & why
- [ ] Why single-context-window execution breaks on complex tasks
- [ ] The 3 failure modes: agentic laziness, self-preferential bias, goal drift
- [ ] Which task shapes trigger this (long-running, parallel, structured, adversarial)

### 2. The substance — how & why this way
- [ ] What a dynamic workflow actually IS (JS file + subagent-spawning functions)
- [ ] Why separate context windows per subagent is the core fix
- [ ] Dynamic vs static workflows — what "dynamic" buys you (Opus writes a custom harness)
- [ ] The 6 patterns and when each applies
- [ ] Key mechanics: model choice, worktree isolation, the fan-out "barrier", resumability

### 3. The so-what
- [ ] When to use vs NOT use (token cost; "does it really need more compute?")
- [ ] How to invoke + steer (ultracode, quick workflows, /goal, /loop, token budgets)
- [ ] Applying patterns to YOUR work (non-technical use cases too)

## Open gaps
- (none yet)

## Key takeaways (fill as we go)
- (to fill)
