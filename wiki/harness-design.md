---
type: concept
created: 2026-04-06
last-updated: 2026-04-06
sources:
  - raw/2026-04-06-anthropic-harness-design-long-running-apps.md
  - raw/2026-04-06-claude-reviews-claude-overview.md
tags: [wiki, architecture, agentic]
---

# Harness Design

## Summary
The practice of designing multi-agent architectures (harnesses) around LLMs to achieve production-quality outputs on complex, long-running tasks. Inspired by GAN-style generator-evaluator loops. Core insight: decomposition into specialized roles (planner, generator, evaluator) outperforms monolithic single-agent approaches.

## Details
- **Core problem**: Naive single-agent approaches fail on long-running tasks due to [[context-anxiety]] and [[self-evaluation-bias]]
- **GAN-inspired solution**: Separate generation from evaluation — a generator produces, an evaluator critiques, quality improves iteratively over 5-15 rounds
- **Three-agent architecture** for full-stack coding:
  - **Planner**: Transforms brief prompts into ambitious specs, emphasizes deliverables over implementation
  - **Generator**: Works in feature-focused sprints (React, Vite, FastAPI, SQLite/PostgreSQL), self-evaluates before handoff
  - **Evaluator**: Uses Playwright MCP to test like a user — navigates UI, tests APIs, checks database state. Negotiates [[sprint-contracts]] defining success criteria before implementation
- **Performance**: Solo agent = 20 min / $9 (broken output). Full harness = 6 hours / $200 (functional, polished output)
- **Evolution**: As models improve (Sonnet → Opus), strip away components that are no longer load-bearing — [[assumptions-expire]]
- **Evaluation tuning**: Out-of-the-box Claude QA agents approve mediocre work. Requires multiple calibration cycles against human judgment.
- **Claude Code as concrete harness**: [[claude-code|Claude Code]] implements the harness pattern with 6 pillars. Its core design principle: "LLM as reasoning center; Harness provides perception, action, memory, and constraints." The [[query-loop]] (12-step state machine), [[context-management]] (4-layer compression), and [[permission-system]] (7-layer defense) are the harness infrastructure.

## Connections
- Related: [[multi-agent-architecture]], [[context-anxiety]], [[self-evaluation-bias]], [[Anthropic]], [[Prithvi Rajasekaran]], [[claude-code]], [[query-loop]], [[context-management]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-06 | raw/2026-04-06-anthropic-harness-design-long-running-apps.md | Initial creation — full concept from engineering blog |
| 2026-04-06 | raw/2026-04-06-claude-reviews-claude-overview.md | Added Claude Code as concrete harness implementation |
