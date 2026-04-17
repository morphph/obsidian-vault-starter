---
type: concept
created: 2026-04-17
last-updated: 2026-04-17
sources:
  - raw/2026-04-16-anthropic-opus-4-7-announcement.md
tags: [wiki, concept, agentic, control]
---

# xhigh Effort Level

## Summary
New effort tier introduced with [[claude-opus-4-7]], sitting between `high` and `max`. Anthropic officially recommends `xhigh` for agentic coding and complex reasoning, reserving `max` for edge cases. Represents a finer-grained knob for trading latency and token spend against reasoning depth.

## Details
- **Tier ordering:** `low` → `medium` → `high` → `xhigh` (new) → `max`
- **Recommended usage:** agentic coding, long-horizon planning, complex reasoning
- **Cost implication:** pricing per token is unchanged, but `xhigh` produces more thinking tokens — real bills go up even though rates don't
- **Operational advice:** A/B test existing workflows at `high` vs `xhigh` before flipping all traffic; the ROI curve is task-dependent
- Paired with [[task-budgets]] — together they form 4.7's two new agentic control primitives
- Part of a broader trend: [[assumptions-expire]] — as models get stronger, the harness can offload more decisions to the model itself

## Connections
- Related: [[claude-opus-4-7]], [[task-budgets]], [[assumptions-expire]], [[claude-code]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-17 | raw/2026-04-16-anthropic-opus-4-7-announcement.md | Initial creation |
