---
type: concept
created: 2026-04-06
last-updated: 2026-04-07
sources:
  - raw/2026-04-06-anthropic-harness-design-long-running-apps.md
  - raw/2026-04-06-claude-reviews-claude-overview.md
  - raw/2026-04-07-anatomy-of-agent-harness.md
tags: [wiki, architecture, agentic]
---

# Multi-Agent Architecture

## Summary
Architectural pattern where multiple specialized LLM agents collaborate on a task, each with a distinct role. Inspired by GANs (Generative Adversarial Networks) — the adversarial tension between generator and evaluator drives quality improvement.

## Details
- **Planner-Generator-Evaluator** is the canonical three-agent setup for full-stack coding
- GAN analogy: generator creates, evaluator critiques, iterative loop drives improvement (5-15 iterations for frontend design quality)
- Each agent can have different tools: generator has code tools, evaluator has Playwright MCP for user-like testing
- [[sprint-contracts]]: evaluator and generator negotiate success criteria before implementation begins
- Cost/time tradeoff: much more expensive than single-agent ($200 vs $9) but produces actually functional output
- **Key principle**: decomposition into specialized roles outperforms monolithic approaches
- As models improve, some agent roles become optional — the frontier shifts but doesn't eliminate the pattern
- **In Claude Code**: Multi-Agent Coordination is one of the 6 foundational pillars of [[claude-code]] architecture — distributed task execution built into the harness itself
- **When to split**: Maximize single agents first; split only when tools exceed ~10 overlapping functions
- **Subagent execution models** (Pachaar/Chawla): Fork (identical copy), Teammate (separate terminal with mailbox), Worktree (isolated git branch)
- **OpenAI patterns**: agents-as-tools (subtasks, return results) vs handoffs (full control transfer)
- **CrewAI**: role-based multi-agent with deterministic Flows backbone

## Connections
- Related: [[harness-design]], [[self-evaluation-bias]], [[Anthropic]], [[claude-code]], [[orchestration-loop]], [[verification-loops]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-06 | raw/2026-04-06-anthropic-harness-design-long-running-apps.md | Initial creation |
| 2026-04-06 | raw/2026-04-06-claude-reviews-claude-overview.md | Added Claude Code multi-agent coordination pillar |
| 2026-04-07 | raw/2026-04-07-anatomy-of-agent-harness.md | Added when-to-split heuristic, subagent models, OpenAI/CrewAI patterns |
