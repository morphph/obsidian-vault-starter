---
type: source-summary
created: 2026-04-09
last-updated: 2026-04-09
sources:
  - raw/2026-04-09-anthropic-managed-agents-docs.md
tags: [source, anthropic, docs]
---

# Source: Claude Managed Agents Official Docs

## Summary
Complete official documentation suite for Claude Managed Agents, Anthropic's fully managed agent hosting service. 10 pages covering overview, quickstart, agent setup, environments, tools, events/streaming, outcomes, multi-agent, memory, and API reference. Published 2026-04-09 (launch day, beta).

## Key Takeaways
- Four core concepts: Agent (config), Environment (container), Session (running instance), Events (communication)
- Built-in tools: bash, read, write, edit, glob, grep, web_fetch, web_search — all via `agent_toolset_20260401`
- Custom tools supported: define schema, Claude emits structured requests, your code executes
- SSE-based event streaming with user events (message, interrupt, tool confirmation) and agent events (message, thinking, tool use)
- Three research preview features: outcomes (rubric-driven grading), multi-agent (coordinator + threads), memory stores (persistent across sessions)
- SDKs in 7 languages, plus `ant` CLI tool
- Pricing: standard token rates + $0.08/session-hour

## Pages Created
- [[claude-managed-agents]] — main entity page
- [[managed-agents-architecture]] — brain/hands/session decoupling
- [[managed-agents-outcomes]] — rubric-driven self-evaluation
- [[managed-agents-multiagent]] — coordinator + thread model
- [[managed-agents-memory-stores]] — persistent memory stores

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-09 | raw/2026-04-09-anthropic-managed-agents-docs.md | Initial creation |
