---
type: concept
created: 2026-05-15
last-updated: 2026-05-15
sources:
  - raw/2026-05-11-chrishayduk-using-codex-goals-effectively.md
tags: [wiki, principle, agentic, loop, state-management, context]
---

# Agentic Loop Tracking Files

## Summary
[[chris-hayduk|Chris Hayduk]]'s pattern for letting an agent run for **hours or days** without losing coherence: instead of forcing the model to hold all state in its (compaction-prone) context window, give it **three dedicated markdown files** as external memory — **PLAN.md** (high-level direction), **EXPERIMENTS.md** (curated attempt log), **SCRATCHPAD.md** (chronological real-time thoughts). The deeper principle: **for long-running loops, working memory should live on disk, not in context.** Hayduk: *"EXPERIMENTS.md is the most important of the three."*

## Details

### The three files (and what they do)

| File | Content | When to read | When to write |
|------|---------|--------------|---------------|
| **PLAN.md** | High-level plan the agent intends to follow; seeded with initial ideas | At loop start; whenever direction is unclear | When plan changes; rarely otherwise |
| **EXPERIMENTS.md** | Clean, curated list of experiments with title + description + result | Before deciding next experiment (so it doesn't repeat) | After every completed attempt |
| **SCRATCHPAD.md** | Chronological real-time thoughts as actions execute | Rarely (auditor / human reads this) | Continuously, append-only |

### Why this works (the context-window argument)
With `/goal` mode (Codex or [[claude-code-goal|Claude Code]]), the agent can run for **multiple days at a time**. Even with great compaction, the model can't maintain a coherent thread across days. Compaction summarizes; summaries lose detail; details lost from compaction are gone unless they were persisted elsewhere.

**The three files are what survives compaction** — they live on disk and can be re-read at any point. They become the *durable* working memory. Context window holds the current burst; the files hold everything else.

### Why EXPERIMENTS.md matters most
> "EXPERIMENTS.md is the most important of the three, as it lets both you and the agent review its previous attempts at achieving the goal and why they did/didn't work."

In long-running loops the dominant failure is **repeating previous failed attempts** because context summarization dropped the failure record. EXPERIMENTS.md prevents this. It's the agent's lab notebook.

A good entry looks like:
```
## Attempt 7 — Reduce embedding dim from 768→384
**Hypothesis:** Smaller embeddings → faster forward pass without quality hit
**Result:** -2% recall@10 on validation, 1.8× speedup
**Conclusion:** Speedup not worth quality regression. Try sparse-attn next.
```

The agent reads previous entries before proposing the next experiment. **The lab notebook becomes the search heuristic.**

### Why SCRATCHPAD.md is auditable working memory
SCRATCHPAD is the **append-only stream of thoughts** as the agent runs. It's not meant for the agent's own re-reading (that's PLAN/EXPERIMENTS) — it's meant for **you** to spot when the agent is going off the rails.

> "This file is great to have so that you can audit the agent's thought process and see if you need to nudge it back in another direction."

Pattern: every few hours you skim SCRATCHPAD; if you see flailing, you intervene by editing PLAN.md. **The agent re-reads PLAN.md and self-corrects.** This is how a human stays in the loop without continuously sitting at the keyboard.

### Generalizing beyond ML

| Domain | PLAN.md | EXPERIMENTS.md | SCRATCHPAD.md |
|--------|---------|----------------|---------------|
| ML architecture search | Target metrics + constraints | Each architecture tried + score | Loss curves, debugging notes |
| Migration to new framework | Phased rollout plan | Each file migrated + tests passed | Errors encountered, fixes |
| Codebase refactor | Architectural target | Each subsystem touched + status | Per-commit thinking |
| Research synthesis | Question + hypotheses | Each source reviewed + finding | Half-formed connections |
| Multi-day production task | What's being built | What was tried (worked / didn't) | Today's real-time decisions |

### Connection to existing wiki concepts

- **[[claude-code-goal]]** — The Claude Code analogue of Codex `/goal`. Same three-file pattern applies directly. Adding it would close one of the article's "anti-patterns" (running long without persisting state).
- **[[skillify-meta-skill]]** — Skills are durable workflow files. The three tracking files are durable *run-state* files. Skills capture "how to do this kind of task"; tracking files capture "what happened in this specific run." Complementary.
- **[[session-memory]]** — Claude Code's forked-subagent that maintains structured notes is the in-system version of this. The three files are the *user-controlled* version that's portable across vendors.
- **[[dreaming]]** — Cross-session memory consolidation. After a long run completes, dreaming could summarize EXPERIMENTS.md into the brain; then start a fresh run.
- **[[filing-cabinet-vs-nervous-system]]** — The three files are nervous-system primitives: they propagate state across the gap between turns.

### How this differs from Claude Code's built-in compaction
- Compaction is **automatic + lossy** — model decides what to summarize
- The three files are **explicit + lossless within their scope** — agent decides what to log, you can audit

Used together: compaction handles short-range coherence within a session, the three files handle long-range coherence across sessions / compactions / days.

### Implementation checklist (from Hayduk + extrapolated)
- [ ] Pre-create the three files in the workspace (with empty headings) before starting the loop
- [ ] Seed PLAN.md with initial direction
- [ ] Tell the agent in the goal/prompt: *"Maintain PLAN.md, EXPERIMENTS.md, SCRATCHPAD.md. Read EXPERIMENTS.md before each new attempt. Append to SCRATCHPAD.md continuously."*
- [ ] Optionally: add a `gbrain doctor`-style check that fails the loop if EXPERIMENTS.md hasn't grown in N hours (probably stuck)

## Connections
- Related: [[chris-hayduk]], [[claude-code-goal]], [[skillify-meta-skill]], [[session-memory]], [[dreaming]], [[filing-cabinet-vs-nervous-system]], [[sprint-contracts]], [[verification-loops]], [[context-management]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-05-15 | raw/2026-05-11-chrishayduk-using-codex-goals-effectively.md | Initial creation from "Using Codex Goals Effectively" |
