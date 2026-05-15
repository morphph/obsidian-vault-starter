---
type: concept
created: 2026-05-13
last-updated: 2026-05-15
sources:
  - raw/2026-05-13-claude-code-goal-and-agent-view.md
  - raw/2026-05-11-chrishayduk-using-codex-goals-effectively.md
tags: [claude-code, autonomy, hooks, evaluator, session-control]
---

# /goal — Session-scoped autonomous turn-loop

## Summary
[[claude-code]] slash command that sets a completion condition; a small fast model (Haiku default) evaluates the transcript after every turn and decides whether to start another turn or return control. Implemented as a **session-scoped prompt-based Stop hook**. Removes per-turn human prompting for tasks with a verifiable end state — the natural complement to auto-mode (which removes per-tool prompting).

## Details

- **Set:** `/goal <condition>`. Starts a turn immediately with the condition as the directive; no separate prompt needed.
- **Status:** `/goal` with no args. Shows condition, duration, turns evaluated, token spend, evaluator's last reason.
- **Clear:** `/goal clear` (aliases: stop / off / reset / none / cancel). `/clear` also wipes it.
- **One goal per session.** A new `/goal` replaces the old one. Active indicator: `◎ /goal active`.
- **Condition limit:** 4,000 characters.
- **Resume:** condition carries across `--resume` / `--continue`; turn count, timer, and token baseline reset.
- **Non-interactive:** `claude -p "/goal <condition>"` runs the loop to completion in one invocation. Ctrl+C to stop.

### Evaluator characteristics
- The evaluator reads only the **conversation transcript** — it does NOT call tools, read files, or run commands.
- Returns yes/no + short reason. "No" injects the reason as guidance for the next turn. "Yes" clears the goal and records an achieved entry.
- Runs on the small fast model configured for your provider (Haiku default). Evaluator token cost is negligible vs. main turns.

### Writing an effective condition
Three components (from official docs):
1. **One measurable end state** — test result, build exit code, file count, empty queue.
2. **A stated check** — how Claude should prove it. e.g., "`npm test` exits 0" or "`git status` is clean".
3. **Constraints that matter** — invariants. e.g., "no other test file is modified".

The condition must be **checkable from the transcript** since the evaluator has no tools. Bound runtime by adding `or stop after N turns` or a wall-clock clause.

### Requirements / when it's blocked
- Runs only in **trusted workspaces** (trust dialog accepted).
- Blocked when `disableAllHooks` is set at any settings level.
- Blocked when `allowManagedHooksOnly` is set in managed settings.
  In each case the command tells you why.

## Comparison with other session-running primitives

| Approach | Next turn starts when | Stops when |
|----------|----------------------|------------|
| `/goal` | Previous turn finishes | Model confirms condition met |
| `/loop` | Time interval elapses | You stop it, or Claude judges work done |
| Custom Stop hook | Previous turn finishes | Your own script/prompt decides |
| Auto-mode alone | (per-tool, not per-turn) | Claude judges work done |

`/goal` is a **shortcut for the Stop-hook + model-evaluator pattern** that would otherwise need bespoke config. Use a custom Stop hook when you need deterministic (script-based) checks; use `/goal` when the check is naturally model-evaluated.

## Use cases (from docs)
- Migrating a module to a new API until every call site compiles and tests pass.
- Implementing a design doc until all acceptance criteria hold.
- Splitting a large file into focused modules until each is under a size budget.
- Working through a labeled issue backlog until the queue is empty.

## Anti-patterns
- **Vague conditions** ("make the code better") — the evaluator can't judge subjective state.
- **Conditions that need tool calls to verify** — evaluator only reads transcript; if Claude doesn't run the verifying command, the goal can never resolve.
- **No turn/time bound on long tasks** — runaway loops; add `or stop after 20 turns` for safety.
- **Single short edit** — overhead of evaluator > benefit. Use for substantive work only.

## Cross-vendor convergence: Codex has the same primitive

OpenAI's Codex now ships a `/goal` command with **near-identical semantics** to Claude Code's `/goal`. [[chris-hayduk|Chris Hayduk]] (FDE Life Sciences @ OpenAI) published a 188K-view playbook on 2026-05-11 ([[source-chrishayduk-codex-goals-effectively]]) whose three tips apply equally to both vendors:

1. **Specify a clear, quantitative goal.** Same two failure modes Chris reports on Codex (model gives up early / model flails forever) match this page's "vague conditions" anti-pattern. The 200-item checklist trick — extracting qualitative rules into a markdown checkbox file the model marks off as it goes — is a canonical "qualitative → quantitative" conversion useful in either vendor. See [[sprint-contracts]] for the underlying pattern.
2. **Make the feedback loop tight.** Chris's protein-structure example reduced scoring from days to minutes by using a smaller model + subsampled dataset. The cost of slow scoring is amplified by the loop — same eval that costs N seconds in a single chat call costs N × (turns) seconds across the loop. See [[verification-loops]].
3. **Give the agent markdown files for tracking.** Three files: **PLAN.md** (direction), **EXPERIMENTS.md** (curated attempt log — "the most important of the three"), **SCRATCHPAD.md** (chronological real-time thoughts). Pre-create them, mention them in the goal condition, let the agent read/write across compactions. See [[agentic-loop-tracking-files]] — this is the **anti-anti-pattern** for runaway loops + lost state.

**Takeaway:** the `/goal` design has converged across Claude Code and Codex; the playbook for using it well is vendor-agnostic.

## Connections
- Related: [[claude-code]], [[orchestration-loop]], [[verification-loops]], [[adaptive-thinking]], [[task-budgets]], [[quality-gate-loop]], [[chris-hayduk]], [[agentic-loop-tracking-files]], [[sprint-contracts]]
- Extends [[verification-loops]] — same agent + verifier pattern at the turn granularity instead of within a task.
- Sibling to [[task-budgets]] (Opus 4.7 model-side context-anxiety remedy): `/goal` is the *harness*-side answer; `task-budgets` is the *model*-side answer.
- Complements [[plan-mode-as-tools]] philosophy: state transitions and completion checks belong in tool calls / hooks, not in prompt rewrites.
- Pairs with auto-mode for fully unattended runs — [[ralph-wiggum]] for the heavyweight long-running version.
- Pairs with [[claude-code-agent-view]] for parallel unattended runs — agent view = orchestration screen, `/goal` = per-session loop driver.
- Cross-vendor sibling: Codex `/goal` — see [[chris-hayduk]]'s playbook ([[source-chrishayduk-codex-goals-effectively]]).

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-05-13 | raw/2026-05-13-claude-code-goal-and-agent-view.md | Initial creation from official `/goal` docs at code.claude.com/docs/en/goal |
| 2026-05-15 | raw/2026-05-11-chrishayduk-using-codex-goals-effectively.md | Cross-vendor convergence section: Codex `/goal` is nearly identical; Chris Hayduk's 3-tip playbook applies to both vendors (quantitative goal, tight feedback loop, three-file tracking pattern) |
