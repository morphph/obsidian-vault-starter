---
type: concept
created: 2026-04-07
last-updated: 2026-04-15
sources:
  - raw/2026-04-07-anatomy-of-agent-harness.md
  - raw/2026-04-15-tips-ai-coding-ralph-wiggum.md
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
- **[[ralph-wiggum|Ralph Loop]]** for long-running tasks: Initializer Agent sets up environment + progress files, subsequent Coding Agents read git logs and progress to orient, completing features iteratively across multiple context windows
- **Ralph practical mechanics** ([[matt-pocock]]): Same prompt runs in a bash loop with capped iterations. Each iteration reads PRD + `progress.txt`, agent picks highest-priority task, implements it, runs feedback loops, commits, appends progress. Uses `<promise>COMPLETE</promise>` as termination signal. Two modes: HITL (watch, intervene) and AFK (set and forget). Alternative loop types beyond feature backlogs: test coverage, linting, duplication, entropy reversal.

## Connections
- Related: [[query-loop]], [[harness-design]], [[context-management]], [[claude-code]], [[ralph-wiggum]], [[matt-pocock]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-07 | raw/2026-04-07-anatomy-of-agent-harness.md | Initial creation |
| 2026-04-15 | raw/2026-04-15-tips-ai-coding-ralph-wiggum.md | Added Ralph practical mechanics, HITL/AFK modes, alternative loop types |
