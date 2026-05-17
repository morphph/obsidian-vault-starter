---
type: synthesis
created: 2026-05-17
last-updated: 2026-05-17
sources:
  - raw/2026-05-17-mattpocock-chapter-creator-thread.md
  - raw/2026-05-17-repo-mattpocock-skills.md
  - raw/2026-05-17-mattpocock-grill-with-docs-skill.md
  - raw/2026-05-17-aihero-grill-with-docs-changelog.md
  - raw/2026-05-17-repo-mattpocock-sandcastle.md
  - raw/2026-05-17-amplitude-ralph-loop-102-features.md
  - raw/2026-05-17-tessmann-agent-teams-ralph-hybrid.md
  - raw/2026-05-17-alexandergekov-year-of-ralph-loop.md
  - raw/2026-05-17-adityapuri-matt-pocock-5-skills.md
  - raw/2026-05-17-aihero-5-agent-skills.md
tags: [wiki, synthesis, workflow, afk, ralph, runbook]
---

# Idea → AFK Agent Flow

## Summary
End-to-end methodology for turning a fuzzy idea into an autonomous agent that ships work while you're away — built from Matt Pocock's 6-step chapter-creator tweet, his skills library, Sandcastle framework, and 2026 Ralph evolution. Core insight: **you do not write the AFK agent first.** You crystallize requirements → prototype the prompt interactively → build a live-data feedback surface → iterate to convergence → only then promote to AFK.

## The 5 Phases

### Phase 0 — Pre-conditions
Before starting, three things must exist:
1. **A repo with `/setup-matt-pocock-skills` run once** (or your equivalent skill loadout)
2. **CLAUDE.md / AGENTS.md** with project standards
3. **A sandbox option** (Docker / Podman / Vercel via Sandcastle, or bare worktree for trusted work)

### Phase 1 — Discovery (`/grill-with-docs`)
**Goal:** Convert "I want X" into a written spec the agent can execute against.

**Input:** fuzzy wish
**Output:** clarified plan + updated CONTEXT.md + maybe new ADR

**Mechanic:**
- Run `/grill-with-docs` (or `/grill-me` for non-code)
- Agent asks one question at a time, with its recommended answer
- Agent explores codebase first; only asks user when truly necessary
- CONTEXT.md updated inline as terms resolve
- ADR offered only when (hard-to-reverse + surprising + real trade-off) all true
- Expect 16–50 questions; ~30–90 minutes

**Failure mode:** treating CONTEXT.md as spec. Keep it as glossary only.

### Phase 2 — Prompt Prototyping
**Goal:** First-draft the prompt that will eventually drive the AFK agent.

**Input:** clarified plan from Phase 1
**Output:** v0 system/user prompt + a stated end-condition

**Mechanic:**
- Tell the agent literally: *"let's prototype the prompt I'll eventually pass to the AFK agent"*
- This phrasing matters — it signals you want the *prompt as artifact*, not the implementation
- The agent will typically counter-suggest scaffolding to test the prompt (this is the bridge to Phase 3)
- Define explicit completion signal (e.g., `<promise>COMPLETE</promise>`)
- Define explicit verification (what does "done" look like?)

### Phase 3 — Live-Data Interactive Surface
**Goal:** Watch your prompt run on real data with tight feedback.

**Input:** v0 prompt + your real production data
**Output:** debugging UI (TUI or HTML) you can iterate against

**Mechanic:**
- Agent builds a throwaway debugging surface:
  - **TUI** for state/business-logic prompts (Matt used EffectTS)
  - **HTML page** for output-format prompts ([[throwaway-editors]] pattern)
- Surface points at your *real* data, not synthetic
- You see prompt input + prompt output for each real record
- Surface is disposable — built to be thrown away when prompt converges

**Why this matters:** seeing live output beats reading specs by 10×. You can't predict what the prompt does without watching it.

### Phase 4 — System Prompt Iteration
**Goal:** Get prompt output reliable enough for unattended execution.

**Input:** v0 prompt + live-data surface
**Output:** v∞ prompt that converges on quality

**Mechanic:**
- Edit prompt → observe output on live data → adjust
- Three iteration patterns:
  - **Failure-driven:** find an input where output is bad, add rule to prompt
  - **Edge-case driven:** brainstorm hard cases, test, fix
  - **Voice-driven:** tone/style refinement (most subjective)
- For machine-verifiable work, can add formal eval (LLM-as-judge, score threshold)
- For subjective work, "until it's awesome" by your taste is fine
- Capture lessons as guardrails (`.ralph/guardrails.md` per [[ralph-wiggum]]) so future contexts inherit them

**Stop condition:** you'd be comfortable letting this prompt run unattended overnight.

### Phase 5 — AFK Handoff
**Goal:** Promote converged prompt to autonomous execution.

**Input:** v∞ prompt + verification gates + dispatcher
**Output:** completed work + audit trail

**Mechanic options (pick by scale):**

**Single one-shot** (Matt's chapter creator):
```typescript
import { run, claudeCode } from "@ai-hero/sandcastle";
import { docker } from "@ai-hero/sandcastle/sandboxes/docker";

await run({
  agent: claudeCode("claude-opus-4-7"),
  sandbox: docker(),
  promptFile: ".sandcastle/prompt.md",
  promptArgs: { ... },
  completionSignal: "<promise>COMPLETE</promise>",
  idleTimeoutSeconds: 600,
});
```

**Continuous loop** (Ralph-style):
- Use `maxIterations: N` with Sandcastle, or a bash `while` loop
- Each iteration: fresh context, reads PRD + progress file
- Stop on completion signal or N iterations

**Production scale** (Amplitude case):
- Add a **dispatcher** that ranks "what to do next" (Opportunity Finder pattern)
- Add **self-instrumentation** so each output reports its own performance
- Add **browser verification** (Playwright/Chrome MCP) recording GIF per ship
- Auto-merge narrow low-risk categories; gate the rest

## The Three Critical Patterns

### Pattern A — Interactive→AFK escalation
Sandcastle's `createWorktree()` materializes this:
1. `wt.interactive()` — run interactive session in worktree (no sandbox)
2. `wt.run({ sandbox: docker() })` — hand same worktree to AFK agent

Don't skip the interactive stage. It's where the prompt converges.

### Pattern B — Machine-verifiable cut
For every task ask: **can a script return pass/fail?**
- Yes → AFK loop
- No → HITL with human review

Tessmann's hybrid (Agent Teams + Ralph) generalizes this: docs/design track stays HITL, code/tests track goes AFK in parallel worktrees.

### Pattern C — Dispatcher beats loop
The bare `while true; do agent; done` is the engine. The dispatcher (Opportunity Finder, ranked backlog, `/to-issues` AFK-labeled queue) is the intelligence. **Build the dispatcher first, the loop second.**

## How To Practice On Your Own Projects

### Project candidate selection
Pick a problem where:
- You can articulate "done" (pass/fail or unambiguous quality bar)
- You have real data to test against
- Cost of bad output is recoverable (not destructive)

Good first AFK projects: content generation (you can read it), refactor passes, test backfill, data labeling, doc generation.

### Setup checklist
- [ ] `npx skills@latest add mattpocock/skills` in target repo
- [ ] Run `/setup-matt-pocock-skills`
- [ ] `npm install --save-dev @ai-hero/sandcastle` + `npx sandcastle init`
- [ ] Configure Docker Desktop (or Podman)
- [ ] Set `.sandcastle/.env` with `ANTHROPIC_API_KEY`

### First-flow checklist (the actual practice)
- [ ] Phase 1: Run `/grill-with-docs` on the idea — write down the resulting plan
- [ ] Phase 2: Ask agent to "prototype the prompt I'll pass to the AFK agent"
- [ ] Phase 3: Let agent build a TUI/HTML debugger pointing at real data
- [ ] Phase 4: Iterate prompt until output quality is reliable on ≥10 real inputs
- [ ] Phase 5: Move prompt to `.sandcastle/prompt.md`, configure `sandcastle.run()`, kick off
- [ ] Review commits when you return; merge what passes verification

### Common pitfalls
1. **Skipping Phase 1** — going straight to "build me X." You'll iterate 10× more.
2. **Skipping Phase 3** — building AFK loop directly against unseen data. Output silently degrades.
3. **No completion signal** — agent runs until timeout instead of finishing.
4. **No verification gate** — agent marks "done" without actually verifying.
5. **Treating CONTEXT.md as a spec** — bloats fast; keep it as glossary only.
6. **HITL/AFK undivided** — don't try to put creative-judgment work in a loop. It will produce confident garbage.

## Connections
- Phase 1: [[grill-with-docs]], [[context-md-pattern]], [[sprint-contracts]], [[four-files-context-architecture]]
- Phase 2: [[prompt-architecture-three-layer]], [[skill-as-method-call]]
- Phase 3: [[throwaway-editors]], [[html-as-output-format]]
- Phase 4: [[verification-loops]], [[quality-gate-loop]], [[iterative-repair-loop]], [[agent-improvement-flywheel]], [[cross-modal-review]]
- Phase 5: [[sandcastle]], [[ralph-wiggum]], [[opportunity-finder-pattern]], [[claude-code-sandboxing]], [[shared-contracts-pattern]]
- Cross-cutting: [[mattpocock-skills-library]], [[hitl-vs-afk-classification]], [[vertical-slicing]], [[matt-pocock]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-05-17 | 10 sources (see frontmatter) | Initial synthesis from Matt's tweet + skills repo + Sandcastle + Ralph 2026 evolution |
