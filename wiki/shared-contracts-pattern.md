---
type: concept
created: 2026-05-17
last-updated: 2026-05-17
sources:
  - raw/2026-05-17-tessmann-agent-teams-ralph-hybrid.md
tags: [wiki, multi-agent, coordination, pattern]
---

# Shared Contracts Pattern

## Summary
Meag Tessmann's coordination pattern for parallel agents: the planner agent generates a **Shared Contracts** section BEFORE work begins, specifying exact values (test IDs, type names, API shapes) that all downstream agents must use. Solves the "agents independently invented incompatible names" failure mode in multi-agent + Ralph hybrid systems.

## Details

### The failure it prevents
Parallel agents working on the same feature drift on naming:
- `inline-quick-add` vs `quick-add-inline` (test IDs)
- `Customer` vs `User` (type names)
- `/api/orders` vs `/orders` (route paths)

Downstream agents (test writers, integration code) fail because they can't find the names the implementation agent invented.

### Contract structure
```markdown
## Shared Contracts

### Test IDs: InlineQuickAdd
| Element | Test ID | Used by |
|---------|---------|---------|
| Toggle button | inline-quick-add-toggle | component-builder, test-writer |
| Submit button | inline-quick-add-submit | component-builder, test-writer |
```

### Three enforcement rules
1. **Only planners define contracts** — downstream agents read, never write
2. **Every test ID a test references must appear in contracts** — no improvisation
3. **Only define IDs for elements that actually exist** — no over-specification

### Why it works
Contracts shift the coordination problem from runtime (agents trying to agree mid-work) to design time (planner decides once, all agents inherit). Pure structural coordination — no inter-agent communication needed.

### Limitations Tessmann acknowledged
- Works for cleanly decomposable features
- Fails for components requiring real-time negotiation between agents
- Currently no clean pattern for an agent to request a contract update mid-flight

### Connections to existing wiki
- Sibling of [[sprint-contracts]] (evaluator/generator agree upfront)
- Distinct from CONTEXT.md ([[context-md-pattern]]) which is ubiquitous vocab; contracts are tactical per-feature
- Required by parallel [[ralph-wiggum]] loops in [[multi-agent-architecture]]

## Connections
- [[ralph-wiggum]], [[multi-agent-architecture]]
- [[sprint-contracts]] (close cousin)
- [[idea-to-afk-agent-flow]] (Phase 5 advanced pattern)
- [[hitl-vs-afk-classification]] (contracts enable safer AFK)

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-05-17 | Tessmann Medium article | Initial creation |
