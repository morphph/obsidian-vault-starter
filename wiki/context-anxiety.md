---
type: concept
created: 2026-04-06
last-updated: 2026-04-06
sources:
  - raw/2026-04-06-anthropic-harness-design-long-running-apps.md
tags: [wiki, failure-mode, agentic]
---

# Context Anxiety

## Summary
A failure mode where LLM agents prematurely wrap up work as they perceive approaching context window limits. Part of the broader problem of context window degradation in long-running agentic tasks.

## Details
- Models lose coherence as context fills — this is the general "context window degradation" problem
- Context anxiety is the specific behavior of rushing to finish or cutting corners as the model senses it's running out of space
- Observed particularly in [[claude-model-family|Claude Sonnet 4.5]]
- **Mitigation**: Context resets (clearing context and restarting with structured handoffs) proved more effective than compaction for Sonnet
- Higher-capability models (Opus 4.6) handle this better — continuous sessions with automatic compaction work fine
- This is one of two core failure modes in long-running agentic coding (the other being [[self-evaluation-bias]])

## Connections
- Related: [[harness-design]], [[claude-model-family]], [[self-evaluation-bias]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-06 | raw/2026-04-06-anthropic-harness-design-long-running-apps.md | Initial creation |
