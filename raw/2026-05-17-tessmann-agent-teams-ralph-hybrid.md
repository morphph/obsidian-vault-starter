# When Agent Teams Meet the Ralph Wiggum Loop

**Source:** https://medium.com/@himeag/when-agent-teams-meet-the-ralph-wiggum-loop-4bbcc783db23
**Author:** Meag Tessmann
**Fetch method:** WebFetch
**Fetched:** 2026-05-17

## Core Concept

Hybrid architecture combining:
1. **Agent Teams** — parallel AI instances on creative work (docs, design, strategy)
2. **Ralph Wiggum Loop** — autonomous iteration until tests pass, mechanical tasks

**Decision rule:** "Is the output machine-verifiable? If yes, loop. If no, get a human."

## Why Each Pattern Alone Fails

**Agent Teams** excel at creative decisions but break when an agent's first attempt has errors. Fixing a typo requires human intervention — expensive and slow.

**Ralph Loops** automate repetitive work but lack judgment. Will confidently mark tasks complete even when output requires human taste (UX copy, API design).

## The Hybrid Architecture

```
Feature Plan → Team Planner Agent (human approval)
    ├─ Docs Track (single-shot agents, human review)
    │  └─ flows-writer → test-writer
    └─ Code Track (Ralph loops in git worktrees, autonomous)
       └─ Multiple isolated worktrees with PLAN.md + loop.sh
            ↓
Build Validator Agent → Human Review → Ship
```

Both tracks run simultaneously. A `/build-feature` custom skill orchestrates without writing code.

## Critical Innovation: Shared Contracts

Breakthrough after parallel agents created incompatible test IDs (`inline-quick-add` vs `quick-add-inline`).

Solution: **Shared Contracts** — a section the planner generates BEFORE work begins, specifying exact values multiple teammates must use.

Example structure:
```markdown
## Shared Contracts

### Test IDs: InlineQuickAdd
| Element | Test ID | Used by |
|---------|---------|---------|
| Toggle button | inline-quick-add-toggle | component-builder, test-writer |
```

Three enforcement rules:
1. Only planners define contracts
2. Every test ID a test references must appear in contracts
3. Only define IDs for elements that actually exist

## Lessons About Autonomous Agents

### Git Commits
Agents staged changes reliably but rarely committed. Prompt engineering failed three times. A 4-line bash safety net succeeded.

> "Know what the model is reliable at (writing code, reading errors) and what it isn't (mechanical housekeeping). Use bash for the latter."

### Prompt Format Matters
Narrative prompts ("if everything passes") gave agents too much interpretation room. Structured rules with **explicit negation** proved harder to ignore:
> "Do NOT mark [x] unless BOTH commands exit with code 0"

### Skipped Tests Hide Failures
Tests with defensive guards (`test.skip(!element)`) reported false success. Solution: skipped tests now trigger validation failures.

### Task Reordering
Agents tackle tasks in interesting order, not specified order. Solution: `HARD STOP` markers force commits between tasks.

## Real Performance Data

First deployment: 10 tasks across 3 parallel worktrees
- **Model:** Claude Sonnet (cost-effective for targeted work)
- **Iterations per worktree:** 3–4
- **Cost per iteration:** ~$1–2
- **Total run cost:** ~$15–25
- **Wall clock time:** Under one hour
- **Success rate:** 10/10 tasks completed

## Open Questions Acknowledged

1. Agents have no awareness of each other — coordination is purely structural. Works for cleanly decomposable features; may fail for components requiring real-time negotiation.
2. Judgment boundary is currently binary (autonomous vs human review). Some work needs occasional taste decisions mid-iteration. No clean pattern for agents requesting help.

## Deliverable

`claude-agent-team-kit` GitHub template:
- ~200 lines bash
- ~270 lines skill definition
- Orchestration skills + team brief examples + 13 lessons learned
- Defaults: Node.js (adapts to Python/Rust/Go in ~10 min)

## Connections to Wiki

- Strong overlap with [[multi-agent-architecture]] and [[ralph-wiggum]]
- Shared Contracts pattern is new — relates to [[sprint-contracts]] (success criteria defined upfront)
- The machine-verifiable / not-verifiable cut formalizes [[llm-judgment-vs-scripts]]
- Cost data is rare and valuable — $15-25 for 10-task feature is a useful anchor
