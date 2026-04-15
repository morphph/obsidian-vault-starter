---
type: concept
created: 2026-04-15
last-updated: 2026-04-15
sources:
  - raw/2026-04-15-tips-ai-coding-ralph-wiggum.md
tags: [wiki, architecture, agentic, automation]
---

# Ralph Wiggum

## Summary
Autonomous AI coding pattern created by Geoffrey Huntley: run the same prompt in a loop against a PRD + progress file, letting the agent choose which task to work on next. Represents the next evolution beyond multi-phase plans — from human-directed to agent-directed task selection.

## Details
- **Evolution of AI coding**: vibe coding → planning → multi-phase plans → Ralph. Each step adds more agent autonomy and reduces human prompt-writing.
- **Core mechanism**: A bash loop runs an AI coding CLI (e.g., [[claude-code|Claude Code]]) repeatedly with the same prompt. Each iteration:
  1. Reads a plan file (PRD) to see what needs to be done
  2. Reads a progress file to see what's already done
  3. Agent decides what to do next (highest priority, not first in list)
  4. Explores codebase, implements feature
  5. Runs [[verification-loops|feedback loops]] (types, linting, tests)
  6. Commits code, appends to progress file
  7. Emits `<promise>COMPLETE</promise>` when all work is done
- **Key insight**: The agent chooses the task, not the human. Human defines the end state; Ralph gets there.
- **Two modes**:
  - **HITL (human-in-the-loop)**: Run once, watch, intervene. Best for learning, prompt refinement, risky tasks.
  - **AFK (away from keyboard)**: Run in a loop with capped iterations (5-10 small tasks, 30-50 large). Best for bulk work, low-risk tasks.
  - Progression: start HITL to build trust in prompt, then go AFK.
- **PRD as living TODO**: Structure items as JSON with `passes: false` field (from [[anthropic|Anthropic]]'s research on long-running agents). Ralph marks `passes: true` when complete. Can adjust mid-flight — set back to false, add new items.
- **Progress file**: `progress.txt` committed to repo. Short-circuits exploration — agent reads it, sees what's done, jumps to next task. Contains: tasks completed, decisions made, blockers, files changed. Delete after sprint.
- **Scope definition is critical**: Vague tasks → agent loops forever or takes shortcuts. Must specify files to include, stop condition, edge cases. Example: Ralph skipped "internal commands" when told to test "user-facing" ones.
- **Feedback loops are non-negotiable**: TypeScript types, unit tests, Playwright MCP, ESLint, pre-commit hooks. Best setup blocks commits unless everything passes.
- **Small steps over big chunks**: [[context-rot]] degrades output quality as context fills. Smaller tasks = tighter feedback loops = higher quality. Bias small, especially AFK.
- **Prioritize risky tasks first**: Architectural work and integration points before polish and quick wins. Use HITL for risky tasks, AFK for solid foundation work.
- **[[software-entropy]]**: Agents amplify what they see. Poor code → poorer code. "The repo wins" — thousands of lines of evidence beat a few lines of instruction. Keep codebase clean before letting Ralph loose.
- **Docker sandboxes**: Essential for AFK safety. `docker sandbox run claude` isolates agent — can edit project files but not home directory, SSH keys, or system files. HITL sandboxes optional.
- **Alternative loop types**:
  - Test Coverage Loop — find uncovered lines, write tests, iterate to target (used to go from 16% to 100%)
  - Duplication Loop — `jscpd` finds clones, refactor into shared utilities
  - Linting Loop — fix one error per iteration, verify between
  - Entropy Loop — scan for code smells, clean up one per iteration (software entropy in reverse)
- **Cost**: Configurable to budget. HITL still valuable even without AFK. Author on Anthropic 5x Max (~$90/mo). Local/open-source models not yet good enough.
- **"Golden age"**: AI does magical things faster than humans, but market still pays human wages. Market hasn't adjusted yet.

## Connections
- Related: [[harness-design]], [[orchestration-loop]], [[verification-loops]], [[context-anxiety]], [[software-entropy]], [[claude-code]], [[anthropic]], [[matt-pocock]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-15 | raw/2026-04-15-tips-ai-coding-ralph-wiggum.md | Initial creation — full pattern from Matt Pocock's 11 tips article |
