---
type: concept
created: 2026-04-06
last-updated: 2026-04-06
sources:
  - raw/2026-04-06-claude-reviews-claude-overview.md
tags: [wiki, architecture, agentic]
---

# Query Loop

## Summary
The core execution engine of [[claude-code|Claude Code]] — a 12-step state machine that drives agentic iteration. Not a naive "LLM in a while loop" but a structured state machine handling tool calls, responses, error recovery, and context management per cycle.

## Details
- 12 distinct steps in the state machine
- Drives the agentic iteration cycle: user prompt → LLM reasoning → tool call → result → next iteration
- One of the six foundational pillars of Claude Code architecture
- Works in concert with [[context-management]] to handle long-running sessions
- Part of the "Core Loop" learning track (4 chapters in the Claude Reviews Claude analysis)

## Connections
- Related: [[claude-code]], [[context-management]], [[harness-design]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-06 | raw/2026-04-06-claude-reviews-claude-overview.md | Initial creation |
