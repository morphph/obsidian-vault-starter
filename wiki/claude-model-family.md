---
type: entity
created: 2026-04-06
last-updated: 2026-04-17
sources:
  - raw/2026-04-06-anthropic-harness-design-long-running-apps.md
  - raw/2026-04-16-anthropic-opus-4-7-announcement.md
tags: [wiki, product, llm]
---

# Claude Model Family

## Summary
[[Anthropic]]'s family of LLM models spanning different capability/cost tiers. Different models exhibit different behaviors under long-running agentic workloads, requiring different harness strategies.

## Details
- **Claude Sonnet 4.5**: Exhibits [[context-anxiety]] — prematurely wraps up work as context fills. Context resets (clear + restart with structured handoffs) work better than compaction for this model.
- **Claude Opus 4.6**: Higher capability allows removing scaffolding that lower models need. Continuous sessions with automatic compaction work well. Sprint constructs become optional.
- **[[claude-opus-4-7|Claude Opus 4.7]]** (2026-04-16): Current flagship. Same price as 4.6 ($5/$25 per M). Key deltas:
  - More literal instruction following — 4.6-era prompts may need re-tuning
  - Self-verification before reporting — internalizes what [[verification-loops]] did externally
  - First Claude model with high-res vision (3.75MP, up 3.3× from 1.15MP)
  - New [[xhigh-effort-level]] and [[task-budgets]] control primitives
  - Cyber capabilities deliberately reduced vs. the unreleased Mythos Preview (Project Glasswing)
- **Claude Haiku**: Cost-efficient tier (not discussed in harness design article)
- Key insight: harness complexity should decrease as model capability increases — [[assumptions-expire]]. 4.7 is a concrete step: control primitives that used to live in the harness (budgets, effort) are now model-native.

## Connections
- Related: [[Anthropic]], [[claude-opus-4-7]], [[harness-design]], [[context-anxiety]], [[xhigh-effort-level]], [[task-budgets]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-06 | raw/2026-04-06-anthropic-harness-design-long-running-apps.md | Initial creation — Sonnet vs Opus behavior differences |
| 2026-04-17 | raw/2026-04-16-anthropic-opus-4-7-announcement.md | Added Opus 4.7 as current flagship with deltas vs 4.6 |
