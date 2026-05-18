# Run long-horizon tasks with Codex

**Source URL:** https://developers.openai.com/blog/run-long-horizon-tasks-with-codex
**Author:** OpenAI Developers (official blog)
**Estimated publish date:** ~2026-05-05 (based on secondary references)
**Fetch date:** 2026-05-18
**Fetch method:** WebFetch
**Format:** Official OpenAI blog post

---

## Core Thesis

The practical change in 2026 Codex is **time horizon**: agents can stay coherent for longer, complete larger chunks of work end-to-end, and recover from errors without losing the thread.

> "The practical change is that agents can stay coherent for longer, complete larger chunks of work end-to-end, and recover from errors without losing the thread."

This is **not about /goal command specifically** — it's about the underlying capability that makes /goal-like workflows useful.

## The Codex Operational Cycle (Agent Loop)

The agent does:
1. **Plan** — figure out what to do next
2. **Edit** — make changes
3. **Run tools** — tests / build / lint / etc
4. **Observe results** — read what happened
5. **Repair failures** — fix what didn't work
6. **Update documentation** — record state

This is the standard agent loop (TAO-ish), but the article emphasizes that **the loop's coherence over many iterations is the new capability**, not the loop structure itself.

## Durable Project Memory Pattern — Three Markdown Files

The core architectural recommendation: three markdown files that maintain coherence across the long task:

### 1. **Prompt.md** — Specification & Deliverables
> "Freeze the target so the agent doesn't build something impressive but wrong"

Contains:
- What success looks like
- Concrete deliverables
- Acceptance criteria

**Key insight in this name**: by calling it "Prompt.md" (not "Spec.md"), OpenAI is signaling that the agent **reads this every iteration** like it's the prompt — not a one-time spec doc.

### 2. **Plan.md** — Milestone Checkpoints
Contains:
- Milestone-based decomposition of the work
- Validation criteria per milestone
- Order of execution

The plan is checkpoint-driven. Each milestone has a validation step before moving on.

### 3. **Implement.md** — Execution Runbook
Contains:
- How the agent should behave operationally
- What tools to use
- How to record progress

This is the "operating manual" for the agent's behavior, separate from what it's building (Prompt.md) and the order (Plan.md).

## Verification Discipline

After each milestone, the agent ran:
- Lint
- Typecheck
- Tests
- Build

Only after these passed did it proceed to the next milestone. The validation gate is **per-milestone**, not per-session.

## Comparison Notes (Implicit)

Article doesn't mention:
- `/goal` command (this is conceptually distinct content)
- Pause/resume lifecycle
- Evaluator mechanism

This blog post is about **the underlying capability** (long-horizon coherence + durable memory pattern); `/goal` is a separate productization that builds on top.

## Key Quotes

> "The practical change is that agents can stay coherent for longer, complete larger chunks of work end-to-end, and recover from errors without losing the thread."

> "Freeze the target so the agent doesn't build something impressive but wrong."

## Notable Distinctions from Chris Hayduk's PLAN/EXPERIMENTS/SCRATCHPAD Pattern

| Slot | OpenAI blog (this article) | Chris Hayduk |
|------|---------------------------|--------------|
| Spec / target | Prompt.md | PLAN.md (high-level direction) |
| Progress / state | Implement.md | EXPERIMENTS.md (curated attempt log — Chris says "most important") |
| Real-time thoughts | (not named) | SCRATCHPAD.md (chronological raw) |
| Operational behavior | Implement.md | (less explicit) |
| Plan / milestones | Plan.md | (collapsed into PLAN.md) |

**Convergence**: Both vendors recommend ~3 durable markdown files. The exact decomposition differs but the pattern is universal: **spec + plan + state, on disk, agent reads every turn**.

## Implications for Practitioners

1. **The horizon is the capability** — `/goal` and similar commands productize this capability into a UX
2. **Durable files are non-negotiable** — both Hayduk's pattern and OpenAI's converge on ~3 markdown files
3. **"Freeze the target" is the key constraint** — if Prompt.md can be modified by the agent, it can drift; if it's frozen, the agent always builds against the same target
4. **Milestone-level validation > per-turn validation** — too granular validation slows the loop; too coarse misses bugs

## Source Authority
Official OpenAI Developers blog. Authoritative. Symptom of OpenAI's strategy to **separate the long-horizon capability narrative from the /goal product** — implying /goal is one of multiple possible UXes on top of the underlying capability.
