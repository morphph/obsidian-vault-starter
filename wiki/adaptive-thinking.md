---
type: concept
created: 2026-04-17
last-updated: 2026-04-17
sources:
  - raw/2026-04-16-claude-docs-opus-4-7-whats-new.md
tags: [wiki, concept, api, thinking]
---

# Adaptive Thinking

## Summary
The only supported thinking-on mode for [[claude-opus-4-7]]. Replaces the prior "extended thinking budget" mechanism where callers passed an explicit `budget_tokens`. Per Anthropic's internal evals, adaptive thinking reliably outperforms budget-based extended thinking. **Off by default on Opus 4.7** — must be explicitly enabled.

## Details
- Enable with: `thinking: {type: "adaptive"}`
- Breaking change on Opus 4.7: `thinking: {type: "enabled", budget_tokens: N}` returns a 400 error
- Pairs with [[xhigh-effort-level]] and other `effort` values to tune reasoning depth
- **Thinking content is omitted from the response by default** — thinking blocks appear in stream but `thinking` field is empty unless caller opts in:
  - `"display": "omitted"` (default) — no visible reasoning
  - `"display": "summarized"` — summarized reasoning returned
- UX implication: products that stream reasoning to users now see a long pause before output begins unless `display: "summarized"` is set
- Conceptual shift: the decision of "how much to think" moves from caller-controlled (budget) to model-controlled (adaptive) — another instance of [[assumptions-expire]] and harness → model offloading
- Not applicable to Claude Managed Agents (it handles thinking automatically)

## Connections
- Related: [[claude-opus-4-7]], [[xhigh-effort-level]], [[task-budgets]], [[assumptions-expire]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-17 | raw/2026-04-16-claude-docs-opus-4-7-whats-new.md | Initial creation |
