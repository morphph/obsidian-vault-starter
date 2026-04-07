---
type: source-summary
created: 2026-04-07
last-updated: 2026-04-07
sources:
  - raw/2026-04-07-anatomy-of-agent-harness.md
tags: [wiki, source, architecture, agentic]
---

# Source: The Anatomy of an Agent Harness

## Summary
Comprehensive breakdown of agent harness architecture by Akshay Pachaar / Avi Chawla (Daily Dose of DS). Defines 11 production components, 7 architectural decisions, and compares implementations across [[Anthropic]], OpenAI, LangGraph, and CrewAI. Key finding: LangChain jumped from outside top-30 to #5 on TerminalBench 2.0 by modifying only the harness, same model.

## Details
- Published as X thread (Apr 6, 2026) and blog post on Daily Dose of DS
- Defines the harness as "the complete software infrastructure wrapping an LLM" — an OS where the model is just the CPU
- 11 components: orchestration loop (TAO cycle), tools, memory, [[context-management]], prompt construction, output parsing, [[state-management]], error handling, guardrails, [[verification-loops]], [[subagent-orchestration]]
- 7 architectural decisions: single vs multi-agent, ReAct vs plan-and-execute, context strategy, verification approach, permission architecture, tool scoping, harness thickness
- "Scaffolding principle" aligns with [[assumptions-expire]] — strip harness as models improve
- Introduces "Ralph Loop" pattern for long-running tasks: Initializer Agent + iterative Coding Agents across context windows
- Compares 4 frameworks: Anthropic Claude SDK ("dumb loop"), OpenAI Agents SDK (Runner class), LangGraph (state graphs), CrewAI (role-based)

## Connections
- Related: [[harness-design]], [[assumptions-expire]], [[context-management]], [[multi-agent-architecture]], [[claude-code]], [[orchestration-loop]], [[verification-loops]], [[permission-system]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-07 | raw/2026-04-07-anatomy-of-agent-harness.md | Initial creation |
