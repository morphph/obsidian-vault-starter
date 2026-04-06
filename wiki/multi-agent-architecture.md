---
type: concept
created: 2026-04-06
last-updated: 2026-04-06
sources:
  - raw/2026-04-06-anthropic-harness-design-long-running-apps.md
  - raw/2026-04-06-claude-reviews-claude-overview.md
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

## Connections
- Related: [[harness-design]], [[self-evaluation-bias]], [[Anthropic]], [[claude-code]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-06 | raw/2026-04-06-anthropic-harness-design-long-running-apps.md | Initial creation |
| 2026-04-06 | raw/2026-04-06-claude-reviews-claude-overview.md | Added Claude Code multi-agent coordination pillar |
