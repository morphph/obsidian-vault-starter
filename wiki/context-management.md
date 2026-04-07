---
type: concept
created: 2026-04-06
last-updated: 2026-04-07
sources:
  - raw/2026-04-06-claude-reviews-claude-overview.md
  - raw/2026-04-06-anthropic-harness-design-long-running-apps.md
  - raw/2026-04-07-anatomy-of-agent-harness.md
tags: [wiki, architecture, agentic]
---

# Context Management

## Summary
The system for handling LLM context window limits in [[claude-code|Claude Code]]. Uses a four-layer compression system and treats the context window as the "scarcest resource." Directly addresses [[context-anxiety]] — the failure mode where agents rush as context fills.

## Details
- **Four-layer compression system** in Claude Code (specific layers not detailed in overview — covered in deeper chapters)
- Context window is treated as the "scarcest resource" — all architectural decisions optimize for context efficiency
- One of the six foundational pillars of Claude Code architecture
- **Mitigation strategies from harness design research:**
  - Context resets (clear + restart with structured handoffs) — better for Claude Sonnet 4.5
  - Automatic compaction — works for Claude Opus 4.6
  - The right strategy depends on model capability level
- Comprehensive error recovery for context-related failures: rate-limiting, token exhaustion
- **Performance impact** (Pachaar/Chawla): Performance degrades 30%+ when key content falls in mid-window positions — prioritize beginning and end positioning
- **Four production strategies**: compaction (summarizing history), observation masking (hiding old outputs), just-in-time retrieval (dynamic loading), subagent delegation (condensed summaries)
- **Prompt construction**: hierarchical assembly — system prompt → tool definitions → memory files → conversation history → user message. Priority stacking keeps critical info accessible.

## Connections
- Related: [[claude-code]], [[context-anxiety]], [[query-loop]], [[claude-model-family]], [[orchestration-loop]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-06 | raw/2026-04-06-claude-reviews-claude-overview.md | Initial creation — four-layer compression system |
| 2026-04-06 | raw/2026-04-06-anthropic-harness-design-long-running-apps.md | Added mitigation strategies from harness design research |
| 2026-04-07 | raw/2026-04-07-anatomy-of-agent-harness.md | Added 30% degradation stat, 4 strategies, prompt construction hierarchy |
