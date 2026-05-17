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
  - raw/2026-05-17-aihero-5-agent-skills.md
tags: [wiki, synthesis, workflow, afk, ralph, runbook]
---

# Idea → AFK Agent Flow

## Summary
End-to-end methodology for turning a fuzzy idea into an autonomous agent — synthesized strictly from Matt Pocock's own published material: his 6-step chapter-creator tweet, his skills library (`mattpocock/skills`), his Sandcastle framework (`@ai-hero/sandcastle`), and his AI Hero blog. Core insight: **you do not write the AFK agent first.** You crystallize requirements → prototype the prompt interactively → build a live-data feedback surface → iterate to convergence → only then promote to AFK.

> **Source policy:** This page cites only Matt Pocock's official material (his GitHub repos, his AI Hero blog, his own X posts). Third-party walkthroughs and adjacent community patterns are intentionally excluded — see [[ralph-wiggum]] for unfiltered community evolution.

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

**Mechanic** (from Matt's SKILL.md):
- Run `/grill-with-docs` (or `/grill-me` for non-code)
- Agent asks one question at a time, with its recommended answer
- Agent explores codebase first; only asks user when truly necessary
- CONTEXT.md updated inline as terms resolve
- ADR offered only when (hard-to-reverse + surprising + real trade-off) all true
- Expect 16–50 questions per Matt's AI Hero article; ~30–90 minutes

**Failure mode:** treating CONTEXT.md as spec. Matt's rule: keep it as glossary only.

### Phase 2 — Prompt Prototyping
**Goal:** First-draft the prompt that will eventually drive the AFK agent.

**Input:** clarified plan from Phase 1
**Output:** v0 system/user prompt + a stated end-condition

**Mechanic** (from Matt's chapter-creator tweet, step 3):
- Tell the agent literally: *"let's prototype the prompt I'll eventually pass to the AFK agent"*
- This phrasing matters — it signals you want the *prompt as artifact*, not the implementation
- The agent will typically counter-suggest scaffolding to test the prompt (this is the bridge to Phase 3)
- Define explicit completion signal (Sandcastle default: `<promise>COMPLETE</promise>`)
- Define explicit verification (what does "done" look like?)

### Phase 3 — Live-Data Interactive Surface
**Goal:** Watch your prompt run on real data with tight feedback.

**Input:** v0 prompt + your real production data
**Output:** debugging UI you can iterate against

**Mechanic** (from Matt's chapter-creator tweet steps 4-5, and his `/prototype` skill):
- Matt's `/prototype` skill description: "Build a throwaway prototype to flesh out a design — either a runnable terminal app for state/business-logic questions, or several radically different UI variations toggleable from one route."
- Matt's chapter-creator tweet (step 4): agent built a TUI in EffectTS pointing at his live data
- Surface points at your *real* data, not synthetic
- You see prompt input + prompt output for each real record
- Surface is disposable — built to be thrown away when prompt converges

**Why this matters:** Matt's own observation — seeing live output beats reading specs. You can't predict what the prompt does without watching it.

### Phase 4 — System Prompt Iteration
**Goal:** Get prompt output reliable enough for unattended execution.

**Input:** v0 prompt + live-data surface
**Output:** v∞ prompt that converges on quality

**Mechanic** (from Matt's chapter-creator tweet step 5: "I iterated on the system prompt until it was awesome"):
- Edit prompt → observe output on live data → adjust
- Three iteration patterns (synthesized from Matt's TDD philosophy):
  - **Failure-driven:** find an input where output is bad, add rule to prompt
  - **Edge-case driven:** brainstorm hard cases, test, fix
  - **Voice-driven:** tone/style refinement (most subjective)
- For machine-verifiable work, Matt's `/tdd` skill applies — write the success test first
- For subjective work, "until it's awesome" by your taste is fine (Matt's phrasing)

**Stop condition:** you'd be comfortable letting this prompt run unattended overnight.

### Phase 5 — AFK Handoff
**Goal:** Promote converged prompt to autonomous execution.

**Input:** v∞ prompt + verification gates
**Output:** completed work + audit trail

**Mechanic options (from Sandcastle docs):**

**Single one-shot** (Matt's chapter-creator pattern):
```typescript
import { run, claudeCode } from "@ai-hero/sandcastle";
import { docker } from "@ai-hero/sandcastle/sandboxes/docker";

await run({
  agent: claudeCode("claude-opus-4-7"),
  sandbox: docker(),
  promptFile: ".sandcastle/prompt.md",
  completionSignal: "<promise>COMPLETE</promise>",
  idleTimeoutSeconds: 600,
});
```

**Continuous loop** (Sandcastle's `maxIterations`):
- Use `maxIterations: N`
- Each iteration: fresh context, reads PRD + progress file
- Stop on completion signal or N iterations

## The Key Pattern: Interactive → AFK Escalation

Sandcastle's `createWorktree()` materializes this directly:
```typescript
await using wt = await createWorktree({ branchStrategy: { type: "branch", branch: "agent/feature-x" } });

// Phase 1-4: human-driven interactive session (no sandbox)
await wt.interactive({ agent: claudeCode("claude-opus-4-7"), prompt: "Let's design this." });

// Phase 5: same worktree handed to AFK agent
await wt.run({ agent: claudeCode("claude-opus-4-7"), sandbox: docker(), prompt: "Implement.", maxIterations: 3 });
```

Don't skip the interactive stage. It's where the prompt converges.

## How To Practice On Your Own Projects

### Project candidate selection
Pick a problem where:
- You can articulate "done" (pass/fail or unambiguous quality bar)
- You have real data to test against
- Cost of bad output is recoverable (not destructive)

Good first AFK projects: content generation (you can read it), refactor passes, test backfill, doc generation.

### Setup checklist
- [ ] `npx skills@latest add mattpocock/skills` in target repo
- [ ] Run `/setup-matt-pocock-skills`
- [ ] `npm install --save-dev @ai-hero/sandcastle` + `npx sandcastle init`
- [ ] Configure Docker Desktop (or Podman)
- [ ] Set `.sandcastle/.env` with `ANTHROPIC_API_KEY`

### First-flow checklist
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
5. **Treating CONTEXT.md as a spec** — bloats fast; keep it as glossary only (Matt's strict rule).
6. **HITL/AFK undivided** — don't try to put creative-judgment work in a loop. It will produce confident garbage.

## Connections
- Phase 1: [[grill-with-docs]], [[context-md-pattern]]
- Phase 2-3: [[mattpocock-skills-library]] (`/prototype` skill)
- Phase 4: Matt's `/tdd` skill within [[mattpocock-skills-library]]
- Phase 5: [[sandcastle]], [[claude-code-sandboxing]]
- Cross-cutting: [[matt-pocock]], [[hitl-vs-afk-classification]], [[vertical-slicing]]
- Adjacent (different methodology): [[ralph-wiggum]] — community pattern Matt's stack builds on

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-05-17 | 6 Matt-official sources (see frontmatter) | Initial synthesis from Matt's tweet + skills library + Sandcastle + AI Hero blog |
| 2026-05-17 | (cleanup) | Removed Amplitude/Tessmann/Gekov/Aditya-derived patterns per source-purity policy |
