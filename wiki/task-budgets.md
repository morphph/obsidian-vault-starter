---
type: concept
created: 2026-04-17
last-updated: 2026-04-17
sources:
  - raw/2026-04-16-anthropic-opus-4-7-announcement.md
tags: [wiki, concept, agentic, context]
---

# Task Budgets

## Summary
New agentic primitive introduced with [[claude-opus-4-7]]: a rough token target given to the model for an entire agentic loop — thinking, tool calls, tool results, and final output combined. Model-native solution to the "how hard should I work on this" problem, previously managed externally by the harness.

## Details
- Budget covers the **whole loop**, not a single turn: thinking + tool calls + tool results + final output
- Gives the model a self-awareness signal it previously lacked — it can calibrate depth vs. breadth
- Conceptually complements [[xhigh-effort-level]]: effort tunes per-turn reasoning depth; task budget tunes total loop spend
- Shifts a responsibility **down the stack**: previously the harness (e.g. [[claude-code]]) tracked and warned about context spend. Now the model can self-regulate.
- Related failure mode being addressed: [[context-anxiety]] — models prematurely wrapping up work. An explicit budget replaces the model's implicit guess about how much context remains.
- Worth monitoring: whether explicit budgets create a new failure mode (e.g., model "pads" output to hit budget, or truncates too aggressively when under-budget)

## Connections
- Related: [[claude-opus-4-7]], [[xhigh-effort-level]], [[context-anxiety]], [[context-management]], [[assumptions-expire]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-17 | raw/2026-04-16-anthropic-opus-4-7-announcement.md | Initial creation |
