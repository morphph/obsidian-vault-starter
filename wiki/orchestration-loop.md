---
type: concept
created: 2026-04-07
last-updated: 2026-04-07
sources:
  - raw/2026-04-07-anatomy-of-agent-harness.md
tags: [wiki, architecture, agentic]
---

# Orchestration Loop

## Summary
The Thought-Action-Observation (TAO) cycle — also called the ReAct loop — that forms the heartbeat of any agent harness. Assembles prompts, calls the LLM, parses outputs, executes tool calls, feeds results back, and repeats until done.

## Details
- Anthropic describes this as a "dumb loop" where intelligence lives in the model, not the loop
- A single cycle flows through 7 steps: prompt assembly → LLM inference → output classification → tool execution → result packaging → context updates → loop/terminate
- Tool execution: concurrent for read-only operations, serial for mutations
- Errors returned as ToolMessages so the LLM can self-correct
- Context compaction triggers fire during the loop to prevent overflow
- **ReAct vs plan-and-execute**: ReAct interleaves reasoning and action (flexible, higher cost); plan-and-execute separates planning from execution (3.6x speedup reported)
- In [[claude-code]], this is implemented as the [[query-loop]] — a 12-step state machine
- **Ralph Loop** for long-running tasks: Initializer Agent sets up environment + progress files, subsequent Coding Agents read git logs and progress to orient, completing features iteratively across multiple context windows

## Connections
- Related: [[query-loop]], [[harness-design]], [[context-management]], [[claude-code]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-07 | raw/2026-04-07-anatomy-of-agent-harness.md | Initial creation |
