---
type: concept
created: 2026-04-06
last-updated: 2026-04-07
sources:
  - raw/2026-04-06-anthropic-harness-design-long-running-apps.md
  - raw/2026-04-07-anatomy-of-agent-harness.md
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
- **"Scaffolding principle"** (Pachaar/Chawla): Construction scaffolding enables workers to build structures they couldn't reach otherwise — but gets removed when complete. Models increasingly internalize capabilities that once required harness management.
- **Thin vs thick harness**: Thin harnesses bet on model improvement; graph frameworks (LangGraph) bet on explicit control. The right choice depends on how fast you believe models will improve.

## Connections
- Related: [[harness-design]], [[claude-model-family]], [[multi-agent-architecture]], [[orchestration-loop]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-06 | raw/2026-04-06-anthropic-harness-design-long-running-apps.md | Initial creation |
| 2026-04-07 | raw/2026-04-07-anatomy-of-agent-harness.md | Added scaffolding principle metaphor, thin vs thick harness tradeoff |
