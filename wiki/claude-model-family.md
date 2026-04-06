---
type: entity
created: 2026-04-06
last-updated: 2026-04-06
sources:
  - raw/2026-04-06-anthropic-harness-design-long-running-apps.md
tags: [wiki, product, llm]
---

# Claude Model Family

## Summary
[[Anthropic]]'s family of LLM models spanning different capability/cost tiers. Different models exhibit different behaviors under long-running agentic workloads, requiring different harness strategies.

## Details
- **Claude Sonnet 4.5**: Exhibits [[context-anxiety]] — prematurely wraps up work as context fills. Context resets (clear + restart with structured handoffs) work better than compaction for this model.
- **Claude Opus 4.6**: Higher capability allows removing scaffolding that lower models need. Continuous sessions with automatic compaction work well. Sprint constructs become optional.
- **Claude Haiku**: Cost-efficient tier (not discussed in harness design article)
- Key insight: harness complexity should decrease as model capability increases — [[assumptions-expire]]

## Connections
- Related: [[Anthropic]], [[harness-design]], [[context-anxiety]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-06 | raw/2026-04-06-anthropic-harness-design-long-running-apps.md | Initial creation — Sonnet vs Opus behavior differences |
