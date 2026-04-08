---
type: concept
created: 2026-04-06
last-updated: 2026-04-08
sources:
  - raw/2026-04-06-anthropic-harness-design-long-running-apps.md
  - raw/2026-04-06-claude-reviews-claude-overview.md
  - raw/2026-04-08-troyhua-claude-code-7-layers-memory.md
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
- **In Claude Code**: [[context-management]] (7-layer memory architecture) is the architectural response. Context window is treated as the "scarcest resource" — all architecture decisions optimize for context efficiency.
- **The concrete mechanism:** [[session-memory]] continuously maintains structured notes via forked subagent. When compaction triggers, the summary already exists — no expensive API call needed. This is the primary defense against context anxiety for Opus 4.6.
- **Circuit breaker lesson:** Before adding a 3-strike limit on autocompact retries, 1,279 sessions had 50+ consecutive compaction failures (up to 3,272 in a single session), wasting ~250K API calls/day globally. Context anxiety wasn't just degrading quality — the system's own recovery mechanism was spiraling.

## Connections
- Related: [[harness-design]], [[claude-model-family]], [[self-evaluation-bias]], [[context-management]], [[claude-code]], [[session-memory]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-06 | raw/2026-04-06-anthropic-harness-design-long-running-apps.md | Initial creation |
| 2026-04-06 | raw/2026-04-06-claude-reviews-claude-overview.md | Added Claude Code's 4-layer compression as architectural response |
| 2026-04-08 | raw/2026-04-08-troyhua-claude-code-7-layers-memory.md | Corrected 4→7 layers, added session memory mechanism + circuit breaker stats |
