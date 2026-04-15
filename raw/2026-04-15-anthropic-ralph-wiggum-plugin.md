# Claude Code Ralph Wiggum Plugin — Official Anthropic Implementation

**Source:** https://github.com/anthropics/claude-code/tree/main/plugins/ralph-wiggum
**Author:** Anthropic (formalized by Boris Cherny, late 2025)
**Fetch method:** WebFetch (GitHub README)
**Date fetched:** 2026-04-15

---

## Overview

The Ralph Wiggum plugin is Anthropic's official implementation of the Ralph technique for iterative, self-referential AI development loops in Claude Code. Named after The Simpsons character, it embodies persistent iteration despite setbacks.

## Core Architecture — Stop Hook (not bash loop)

Unlike the original bash loop, the plugin uses a **Stop hook** that intercepts Claude's exit attempts:

```
You run ONCE:
/ralph-loop "Your task description" --completion-promise "DONE"

Then Claude Code automatically:
1. Works on the task
2. Tries to exit
3. Stop hook blocks exit
4. Stop hook feeds the SAME prompt back
5. Repeat until completion
```

The loop happens **inside your current session** — no external bash loops needed.

## Commands

### /ralph-loop
Start a Ralph loop in your current session.

**Usage:**
```
/ralph-loop "<prompt>" --max-iterations <n> --completion-promise "<text>"
```

**Options:**
- `--max-iterations <n>` — Stop after N iterations (default: unlimited)
- `--completion-promise <text>` — Phrase that signals completion

### /cancel-ralph
Cancel the active Ralph loop.

## Quick Start Example

```bash
/ralph-loop "Build a REST API for todos. Requirements: CRUD operations, input validation, tests. Output <promise>COMPLETE</promise> when done." --completion-promise "COMPLETE" --max-iterations 50
```

Claude will iteratively:
- Implement the API
- Run tests and see failures
- Fix bugs based on test output
- Iterate until all requirements are met
- Output the completion promise when done

## Prompt Writing Best Practices

### Clear Completion Criteria
```
Build a REST API for todos.

When complete:
- All CRUD endpoints working
- Input validation in place
- Tests passing (coverage > 80%)
- README with API docs
- Output: <promise>COMPLETE</promise>
```

### Incremental Goals
```
Phase 1: User authentication (JWT, tests)
Phase 2: Product catalog (list/search, tests)
Phase 3: Shopping cart (add/remove, tests)

Output <promise>COMPLETE</promise> when all phases done.
```

### Self-Correction via TDD
```
Implement feature X following TDD:
1. Write failing tests
2. Implement feature
3. Run tests
4. If any fail, debug and fix
5. Refactor if needed
6. Repeat until all green
7. Output: <promise>COMPLETE</promise>
```

### Safety with Iteration Limits
```bash
/ralph-loop "Try to implement feature X" --max-iterations 20
```

**Important**: Always use `--max-iterations` as a safety net to prevent infinite loops.

## Core Philosophy

1. **Iteration > Perfection** — Don't aim for perfect on first try; let the loop refine
2. **Failures Are Data** — Failures are predictable and informative; use them to tune prompts
3. **Operator Skill Matters** — Success depends on writing good prompts
4. **Persistence Wins** — Keep trying until success; the loop handles retry logic

## When to Use Ralph

**Good for:**
- Well-defined tasks with clear success criteria
- Tasks requiring iteration and refinement (e.g., getting tests to pass)
- Greenfield projects where you can walk away
- Tasks with automatic verification (tests, linters)

**Not good for:**
- Tasks requiring human judgment or design decisions
- One-shot operations
- Tasks with unclear success criteria
- Production debugging

## Real-World Results

- Successfully generated 6 repositories overnight in Y Combinator hackathon testing
- One $50k contract completed for $297 in API costs
- Created entire programming language ("CURSED") over 3 months using this approach

## Key Resources

- Original technique: https://ghuntley.com/ralph/
- Ralph Orchestrator: https://github.com/mikeyobrien/ralph-orchestrator

## Bash Loop vs Stop Hook

The plugin deviates from Geoffrey Huntley's original vision in one key way: the original bash loop creates a **fresh context** each iteration (which Huntley considers critical), while the Stop hook continues within the **same session** context. Community discussion (Issue #125) debated whether this violates the core principle. Dex Horthy (HumanLayer) still prefers "5-line bash loops" for this reason.
