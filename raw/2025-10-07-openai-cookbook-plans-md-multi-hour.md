# OpenAI Cookbook — Using PLANS.md for Multi-Hour Problem Solving

**Source:** https://developers.openai.com/cookbook/articles/codex_exec_plans (originally cookbook.openai.com)
**Publisher:** OpenAI Developers Cookbook
**Date:** 2025-10-07
**Fetch date:** 2026-05-20
**Fetch method:** WebFetch

---

## Premise / claim

> "The particular PLANS.md included below is very similar to one that has enabled Codex to work for more than seven hours from a single prompt."

This is OpenAI's earliest official long-horizon playbook — **predates** the May 2026 cookbook trilogy by 7 months. Significance: durable-files pattern in OpenAI's official content begins here, not with the May Prompt+Plan+Implement triad.

## Two-file model

- **AGENTS.md** — terminology and rules; tells agent *when* to use a planning document
- **PLANS.md** (also called ExecPlan) — comprehensive design document; agent uses it as living spec

## AGENTS.md trigger entry (example)

> "When writing complex features or significant refactors, use an ExecPlan (as described in .agent/PLANS.md) from design to implementation."

This is the shorthand-as-trigger pattern: a vocabulary word ("ExecPlan") in AGENTS.md activates the protocol described in PLANS.md.

## Five non-negotiable PLANS.md criteria

1. **Complete self-containment** — all knowledge needed is *inside* the plan
2. **Living document** — evolves as discoveries occur and decisions solidify
3. **Novice enablement** — a complete beginner should succeed without external context
4. **Demonstrable outcomes** — working behavior, not "code matches spec"
5. **Plain language** — every specialized term defined in accessible prose

## Required sections of an ExecPlan

- **Purpose / Big Picture** — user-visible outcomes + how to verify
- **Progress** — timestamped checkpoint list of granular steps
- **Surprises & Discoveries** — unexpected findings with evidence
- **Decision Log** — rationale for key choices made during implementation
- **Outcomes & Retrospective** — summary of achievements + lessons learned
- **Concrete Steps** — exact commands with expected outputs
- **Validation & Acceptance** — observable behavior verification

## Verification philosophy

Behavior-focused, not implementation-focused. Example success criterion:

> "after starting the server, navigating to localhost:8080/health returns HTTP 200"

Not: "function `health_check()` returns HTTP 200 response."

## Format rules

- Single fenced code block — no nested triple-backticks
- Prefer indentation for examples and transcripts
- Prose precedence over checklists, **except** in Progress section
- Milestones = narrative units, not bureaucratic checkpoints

Each milestone introduces:
- Scope
- What exists afterward
- Validation commands
- Expected outcomes (before proceeding)

## Workflow phases

1. Research & Design (embedded in plan narrative)
2. Proof-of-Concept Milestones (de-risking unknowns)
3. Iterative Implementation (with checkpoint updates)
4. Validation & Testing (behavior-focused acceptance)
5. Documentation (decisions logged as discoveries emerge)

---

## Critical comparison: PLANS.md vs Prompt+Plan+Implement triad

| Aspect | PLANS.md (Oct 2025) | Prompt+Plan+Implement triad (May 2026) |
|---|---|---|
| File count | 1 (ExecPlan) + AGENTS.md trigger | 3 separate files |
| Spec vs plan | Both in single doc | Prompt.md = spec (FROZEN); Plan.md = milestones |
| Runbook | Embedded sections | Implement.md (separate) |
| Trigger | AGENTS.md vocabulary word | Direct `/goal` reference |
| Author POV | "Living document" updated by agent | Prompt.md frozen; Plan/Implement evolve |

**Key insight:** PLANS.md is a **single-file variant** of the durable-files pattern; triad is the multi-file variant. Both work. Single-file is faster to write but harder to enforce role separation; multi-file is more disciplined but more setup. **This is the 4th independent reinvention of durable-files** — and the *earliest* one in OpenAI official content.

## Why this matters for long-horizon writing

If you're claiming "three independent reinventions of durable files" (Ralph 2025-07 / Matt CONTEXT.md 2026-04 / OpenAI Prompt+Plan+Implement 2026-05), this PLANS.md article from 2025-10 is **chronologically the 2nd, not the 4th**. The order should be:

1. **Ralph Wiggum** (Geoffrey Huntley, 2025-07) — `PRD.md` + `progress.txt` + `AGENTS.md`
2. **PLANS.md / ExecPlan** (OpenAI Cookbook, 2025-10) — `AGENTS.md` + single ExecPlan
3. **Matt Pocock CONTEXT.md** (2026-04) — `CONTEXT.md` + skill files
4. **OpenAI Prompt+Plan+Implement** (May 2026) — three-file split

**The 7-month gap between Ralph and PLANS.md, then 6 months to Matt, then 1 month to triad** = pattern was actively maturing. PLANS.md is the "long-tail tail" of independent reinventions.
