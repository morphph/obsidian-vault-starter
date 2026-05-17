---
type: concept
created: 2026-05-17
last-updated: 2026-05-17
sources:
  - raw/2026-05-17-adityapuri-matt-pocock-5-skills.md
  - raw/2026-05-17-aihero-5-agent-skills.md
tags: [wiki, workflow, decomposition]
---

# Vertical Slicing

## Summary
Unit-of-work pattern from Matt Pocock's `/to-issues` skill: break features into thin "vertical slices" that cut through all integration layers (schema + API + UI + tests), NOT into horizontal layers (all schemas first, then all APIs, then all UIs). Each slice is independently shippable, surfaces unknowns end-to-end, and enables parallel agents.

## Details

### Why vertical, not horizontal
**Horizontal** (`all schemas → all APIs → all UIs`):
- Nothing ships until everything is done
- Integration risk discovered last
- Hard to parallelize (each layer blocks the next)

**Vertical** (`each issue = full thin feature, schema-to-UI-to-test`):
- Each slice ships independently
- End-to-end validation per slice
- Multiple agents can take different slices in parallel
- Each slice surfaces unknowns at the integration boundary

### Slice characteristics
- **Independently shippable** — can deploy alone
- **Spans all layers** — no slice is "just backend" or "just UI"
- **Has its own tests** — verification gate inside the slice
- **Pulls its own dependencies** — `/to-issues` maps dependencies between slices for scheduling

### Why this enables AFK
Vertical slices are scope-bounded enough to label [[hitl-vs-afk-classification|AFK]] and let an autonomous loop pick them. Horizontal layers are too coupled — an agent working on "all schemas" has no end condition.

### Beyond code
The pattern generalizes to non-code work:
- **Articles:** complete chapter (hook + argument + conclusion) per slice, not "all hooks then all arguments"
- **Videos:** complete short scene, not "all script then all editing"
- **Research:** complete answer to one sub-question, not "all data then all analysis"

Each "slice" is something an autonomous agent could finish and verify.

## Connections
- Source skill: [[mattpocock-skills-library]] (`/to-issues`)
- Required by: [[hitl-vs-afk-classification]] (labels only work on right-sized units)
- Related: [[sprint-contracts]], [[3-agent-starter-team]]
- Phase context: [[idea-to-afk-agent-flow]] (Phase 5 unit of work)

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-05-17 | Aditya walkthrough + Matt's AI Hero article | Initial creation |
