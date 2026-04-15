---
type: concept
created: 2026-04-15
last-updated: 2026-04-15
sources:
  - raw/2026-04-15-tips-ai-coding-ralph-wiggum.md
  - raw/2026-04-15-ghuntley-ralph-wiggum-original.md
  - raw/2026-04-15-anthropic-ralph-wiggum-plugin.md
  - raw/2026-04-15-ghuntley-how-to-ralph-wiggum.md
  - raw/2026-04-15-anthropic-claude-code-sandboxing.md
  - raw/2026-04-15-humanlayer-brief-history-of-ralph.md
  - raw/2026-04-15-devinterrupted-inventing-ralph-wiggum-loop.md
  - raw/2026-04-15-aihero-getting-started-with-ralph.md
  - raw/2026-04-15-mattpocockuk-ralph-wiggum-xthread.md
tags: [wiki, architecture, agentic, automation]
---

# Ralph Wiggum

## Summary
Autonomous AI coding loop pattern created by [[geoffrey-huntley|Geoffrey Huntley]] (June 2025), named after the Simpsons character who never stops trying. At its simplest: `while :; do cat PROMPT.md | claude-code ; done`. The agent chooses the task, not the human. Human defines the end state; Ralph gets there. Went viral late 2025; Anthropic shipped an official [[claude-code|Claude Code]] plugin in December 2025. Core philosophy: **"The loop is the hero, not the model."**

## Details

### Core Mechanism
- **Evolution of AI coding**: vibe coding → planning → multi-phase plans → Ralph. Each step adds more agent autonomy.
- **Simplest form** ([[geoffrey-huntley|Huntley]]): `while :; do cat PROMPT.md | claude-code ; done`
- Each iteration:
  1. Reads plan file (PRD / `IMPLEMENTATION_PLAN.md`) to see what needs doing
  2. Reads progress file (`progress.txt`) to see what's done
  3. Agent decides what to do next (highest priority, not first in list)
  4. Explores codebase, implements feature
  5. Runs [[verification-loops|feedback loops]] (types, linting, tests)
  6. Commits code, appends to progress file
  7. Emits `<promise>COMPLETE</promise>` when all work is done
- **Key insight**: The agent chooses the task, not the human.

### Two Implementations

| Approach | Architecture | Context | Creator |
|----------|-------------|---------|---------|
| **Bash loop** (original) | External `while` loop restarts Claude each iteration | Fresh context per iteration | [[geoffrey-huntley]] |
| **Stop hook plugin** (official) | Plugin intercepts exit, feeds same prompt back | Same session, continuous | [[anthropic|Anthropic]] / [[boris-cherny]] |

The bash loop vs Stop hook is a **fundamental architectural debate**. Huntley designed for fresh context per iteration (avoids [[context-anxiety|context rot]]). The plugin keeps one session (simpler, but accumulates context). Dex Horthy (HumanLayer) still prefers "5-line bash loops" over the official plugin.

### Three-Phase Methodology (Huntley's Playbook)
1. **Requirements Definition**: Human + LLM collaborate on Jobs-to-Be-Done (JTBD), generate `specs/*` files
2. **Planning Mode**: Claude analyzes specs vs existing code → `IMPLEMENTATION_PLAN.md` (disposable, regenerate when wrong)
3. **Building Mode**: Claude implements from plan, runs tests, commits, updates plan

Key files: `PROMPT_plan.md`, `PROMPT_build.md`, `AGENTS.md` (~60 lines), `IMPLEMENTATION_PLAN.md`, `specs/*`

### Two Modes of Operation
- **HITL (human-in-the-loop)**: Run once, watch, intervene. Best for learning, prompt refinement, risky/architectural tasks. Script: `ralph-once.sh`
- **AFK (away from keyboard)**: Run in a loop with capped iterations (5-10 small, 30-50 large). Best for bulk work, low-risk tasks after foundation is solid. Script: `afk-ralph.sh`
- **Progression**: Start HITL to build trust → go AFK once prompt is solid → review commits when you return

### PRD & Scope Definition
- **PRD as living TODO**: JSON with `passes: false` field. Ralph marks `passes: true` when complete. Can adjust mid-flight.
- **Scope definition is critical**: Vague tasks → agent loops forever or takes shortcuts. Must specify files, stop condition, edge cases.
- **JTBD → Story Map → SLC**: Structure releases around Simple/Lovable/Complete (not MVP) aligned with audience needs.

### Technical Principles (Huntley)
- **One thing per loop**: Each iteration addresses exactly one feature. Conserves ~170K token context window.
- **Context stack allocation**: Every loop maintains `@fix_plan.md`, `@specs/*`, `@AGENT.md`
- **Subagent parallelization**: Up to 500 for research, only 1 for validation/testing
- **Deterministic backpressure**: Tests, builds, lints force fixing before committing
- **Self-learning agent**: Agent updates `@AGENT.md` when discovering better build/execution approaches
- **Prompt language patterns**: "study" (not "read"), "don't assume not implemented", "using parallel subagents", "capture the why"
- **Avoid placeholders**: `"DO NOT IMPLEMENT PLACEHOLDER OR SIMPLE IMPLEMENTATIONS. WE WANT FULL IMPLEMENTATIONS."`

### Feedback Loops ([[verification-loops]])
- TypeScript types, unit tests, Playwright MCP, ESLint, pre-commit hooks
- Best setup blocks commits unless everything passes — agent can't declare victory with red tests
- "These aren't AI-specific techniques. They're just good engineering. Ralph makes them non-negotiable." ([[matt-pocock]])
- Advanced: **LLM-as-judge** for subjective criteria (tone, aesthetics) with binary pass/fail

### Small Steps & Context Rot
- [[context-anxiety|Context rot]]: LLM output degrades as context fills. Smaller tasks = tighter feedback loops = higher quality.
- Each iteration has startup costs (pick task, explore repo), but larger tasks → more context → lower quality.
- Bias small, especially for AFK runs.

### Security — [[claude-code-sandboxing|Sandboxing]]
- With `--dangerously-skip-permissions` or `--permission-mode acceptEdits`, the sandbox becomes the **only security boundary**
- **Docker sandboxes** (`docker sandbox run claude`): Essential for AFK. Mounts only project directory. Requires Docker Desktop 4.50+.
- OS-level enforcement: Seatbelt (macOS), bubblewrap (Linux). Reduces permission prompts by 84%.
- HITL sandboxes optional; AFK sandboxes essential.

### [[software-entropy|Software Entropy]]
- "The repo wins" — agents amplify existing code quality. Thousands of lines of evidence beat a few lines of instruction.
- Ralph accelerates entropy: dozens of commits/hour vs human 1-2/day.
- Keep codebase clean before letting Ralph loose. Communicate repo type (prototype vs production vs library).

### Quickstart (from [[matt-pocock]])
```bash
# Step 1: Install Claude Code
curl -fsSL https://claude.ai/install.sh | bash

# Step 2: Docker sandbox
docker sandbox run claude

# Step 3: Create PRD + progress
# Use plan mode (shift-tab) → save as PRD.md
touch progress.txt

# Step 4: HITL script (ralph-once.sh)
claude --permission-mode acceptEdits "@PRD.md @progress.txt \
1. Read the PRD and progress file. \
2. Find the next incomplete task and implement it. \
3. Commit your changes. \
4. Update progress.txt with what you did. \
ONLY DO ONE TASK AT A TIME."

# Step 5: AFK loop (afk-ralph.sh) — cap iterations!
./afk-ralph.sh 20
```

### Alternative Loop Types
- **Test Coverage Loop** — find uncovered lines, write tests, iterate to target (16% → 100%)
- **Duplication Loop** — `jscpd` finds clones, refactor into shared utilities
- **Linting Loop** — fix one error per iteration, verify between
- **Entropy Loop** — scan for code smells, clean up one per iteration (software entropy in reverse)
- Any task describable as "look at repo, improve something, report findings" fits the Ralph pattern

### Results & Economics
- $50,000 contract delivered for $297 in API costs ([[geoffrey-huntley]])
- CURSED programming language built over 3 months (compiler + LLVM, Gen Z syntax)
- 6 repositories shipped overnight (Y Combinator hackathon testing)
- AI Hero CLI: 16% → 100% test coverage ([[matt-pocock]])
- ~90% completion rate through automated loops
- Matt Pocock's X thread: 204K views, 4.8K bookmarks (Jan 5, 2026)

### Timeline
| Date | Milestone |
|------|-----------|
| June 2025 | Huntley first presents Ralph at Twitter agentic coding meetup |
| July 2025 | Official blog launch (`while :; do cat PROMPT.md \| amp ; done`) |
| Aug 2025 | 6 repos shipped overnight; "specification quality = output quality" proven |
| Sep 2025 | CURSED lang launched (compiled to Zig) |
| Oct 2025 | Conference presentations accelerate community adoption |
| Dec 2025 | Anthropic official plugin released (Stop hook architecture) |
| Jan 2026 | Matt Pocock viral thread (204K views); bash vs plugin showdown video |
| 2026+ | Mainstream adoption; workshops, awesome-ralph (849 stars), multiple implementations |

### Future Directions
- **Gas Town** (Steve Yegge concept): "Kubernetes for agents" — distributed orchestration of multiple Ralph loops
- **MEOW** (Molecular Expression of Work): Granular task definitions enabling parallel agent coordination at scale
- Not just one loop, but orchestrated swarms of loops on decomposed tasks

### Limitations
- Works best for **greenfield projects only** — retrofitting existing codebases is problematic
- Codebase will contain garbage and temporary files until production release
- Senior engineer oversight remains essential — amplifies skilled guidance, doesn't replace it
- The "overbaking phenomenon" — leaving Ralph running too long produces unexpected emergent behaviors
- Context compaction in long sessions poses drift risk ("compaction is the devil")

## Connections
- Related: [[harness-design]], [[orchestration-loop]], [[verification-loops]], [[context-anxiety]], [[software-entropy]], [[claude-code]], [[claude-code-sandboxing]], [[anthropic]], [[geoffrey-huntley]], [[matt-pocock]], [[boris-cherny]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-15 | raw/2026-04-15-tips-ai-coding-ralph-wiggum.md | Initial creation — Matt Pocock's 11 tips |
| 2026-04-15 | raw/2026-04-15-ghuntley-ralph-wiggum-original.md | Major expansion — original creator's technical details, $50K→$297, CURSED, operator mindset |
| 2026-04-15 | raw/2026-04-15-anthropic-ralph-wiggum-plugin.md | Added Stop hook architecture, official commands, bash vs plugin debate |
| 2026-04-15 | raw/2026-04-15-ghuntley-how-to-ralph-wiggum.md | Added three-phase methodology, prompt patterns, JTBD/SLC, LLM-as-judge |
| 2026-04-15 | raw/2026-04-15-anthropic-claude-code-sandboxing.md | Added sandboxing as security foundation for AFK |
| 2026-04-15 | raw/2026-04-15-humanlayer-brief-history-of-ralph.md | Added complete timeline Jun 2025 → Jan 2026, overbaking, bash vs plugin debate |
| 2026-04-15 | raw/2026-04-15-devinterrupted-inventing-ralph-wiggum-loop.md | Added philosophy ("loop is hero"), Gas Town, MEOW |
| 2026-04-15 | raw/2026-04-15-aihero-getting-started-with-ralph.md | Added quickstart steps, Docker 4.50+, script templates |
| 2026-04-15 | raw/2026-04-15-mattpocockuk-ralph-wiggum-xthread.md | Added viral X thread content (204K views) |
