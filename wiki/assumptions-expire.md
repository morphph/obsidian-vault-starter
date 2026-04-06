---
type: concept
created: 2026-04-06
last-updated: 2026-04-06
sources:
  - raw/2026-04-06-anthropic-harness-design-long-running-apps.md
tags: [wiki, principle, agentic]
---

# Assumptions Expire

## Summary
A design principle for agentic systems: as LLM models improve, regularly re-test and strip away scaffolding components that are no longer load-bearing. Harness complexity should decrease as model capability increases.

## Details
- When Claude Opus 4.6 shipped, the sprint construct that was essential for Sonnet became removable
- Continuous sessions with automatic compaction replaced structured sprint cycles
- The evaluator agent remained valuable at capability edges but became overhead for simpler tasks
- **Implication**: Don't assume harness complexity is permanent. Improved models shift the frontier, creating new opportunities for simpler configurations
- The space of interesting architectural combinations *expands* as capabilities grow — new problems become tractable

## Connections
- Related: [[harness-design]], [[claude-model-family]], [[multi-agent-architecture]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-06 | raw/2026-04-06-anthropic-harness-design-long-running-apps.md | Initial creation |
