---
type: concept
created: 2026-04-07
last-updated: 2026-04-07
sources:
  - raw/2026-04-07-repo-claude-memory-compiler.md
tags: [wiki, harness-engineering, mental-model]
---

# Compiler Analogy

## Summary
Architecture framework that maps knowledge system layers to compiler concepts: raw logs = source code, LLM = compiler, structured knowledge = executable, lint = test suite, queries = runtime. Makes the architecture immediately understandable and reveals the correct responsibility boundaries.

## Details
- **Source code** (daily/ or raw/) — immutable input, append-only, never edited
- **Compiler** (LLM via /ingest or compile.py) — extracts, synthesizes, cross-references
- **Executable** (knowledge/ or wiki/) — structured output, maintained by the compiler
- **Test suite** (lint) — health checks for consistency, contradictions, orphans
- **Runtime** (queries) — using the compiled knowledge to answer questions
- This analogy applies to any LLM knowledge pipeline, not just conversation capture
- Reveals a key insight: **you don't manually organize knowledge — the compiler does**
- Originated in [[claude-memory-compiler]], applicable to this wiki's architecture too

## Connections
- Related: [[claude-memory-compiler]], [[harness-design]], [[index-over-rag]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-07 | raw/2026-04-07-repo-claude-memory-compiler.md | Initial creation |
