---
type: entity
created: 2026-04-07
last-updated: 2026-04-07
sources:
  - raw/2026-04-07-repo-claude-memory-compiler.md
tags: [wiki, tool, knowledge-base, harness]
---

# Claude Memory Compiler

## Summary
Open-source system that gives [[claude-code|Claude Code]] persistent memory via hooks. Conversations are automatically captured into daily logs, then compiled by the Claude Agent SDK into structured knowledge articles. Adapted from Karpathy's LLM Knowledge Base pattern — same three-layer architecture, but the raw source is your own AI conversations instead of external articles.

## Details
- **Author:** coleam00 | **Stars:** 70 | **Language:** Python | **Status:** Just launched (2 commits)
- Uses Claude Code hooks (SessionEnd, PreCompact, SessionStart) for [[zero-friction-capture]]
- Uses Claude Agent SDK (not CLI) for LLM extraction — covered under existing Claude subscription
- Three layers: `daily/` (immutable logs) → `knowledge/` (compiled articles) → `AGENTS.md` (schema)
- Knowledge articles split into: concepts/, connections/, qa/
- [[index-over-rag]]: At 50-500 articles, structured index.md outperforms vector similarity
- [[compiler-analogy]]: daily = source code, LLM = compiler, knowledge = executable, lint = test suite, query = runtime
- Cost: flush ~$0.02-0.05/session, compile ~$0.45-0.65/daily log, query ~$0.15-0.25

## Connections
- Related: [[harness-design]], [[claude-code]], [[zero-friction-capture]], [[compiler-analogy]], [[index-over-rag]], [[time-gated-compilation]], [[connection-articles]]
- Same Karpathy lineage as this wiki — complementary systems (external vs internal knowledge)

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-07 | raw/2026-04-07-repo-claude-memory-compiler.md | Initial creation from GitHub deep scan |
