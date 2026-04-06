---
type: concept
created: 2026-04-06
last-updated: 2026-04-06
sources:
  - raw/2026-04-06-anthropic-harness-design-long-running-apps.md
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

## Connections
- Related: [[multi-agent-architecture]], [[context-anxiety]], [[self-evaluation-bias]], [[Anthropic]], [[Prithvi Rajasekaran]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-06 | raw/2026-04-06-anthropic-harness-design-long-running-apps.md | Initial creation — full concept from engineering blog |
