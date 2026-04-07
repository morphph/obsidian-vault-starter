---
type: source-summary
created: 2026-04-07
last-updated: 2026-04-07
sources:
  - raw/2026-04-07-repo-claude-memory-compiler.md
tags: [wiki, source, github-repo]
---

# Source: claude-memory-compiler (GitHub Repo)

## Summary
Open-source Python project by coleam00 that gives [[claude-code]] persistent memory via hooks and the Claude Agent SDK. Adapted from Karpathy's LLM KB pattern for conversation capture. First GitHub repo ingested via deep scan.

## Key Takeaways
- [[zero-friction-capture]]: Hook-based auto-capture (SessionEnd + PreCompact) with detached background LLM extraction
- [[compiler-analogy]]: daily = source, LLM = compiler, knowledge = executable — powerful naming framework
- [[index-over-rag]]: At personal scale, structured index beats vector similarity
- [[time-gated-compilation]]: Capture all day, compile after 6 PM — no cron needed
- [[connection-articles]]: Cross-cutting insights as first-class standalone wiki pages
- Recursion prevention via env var (`CLAUDE_INVOKED_BY`) — critical for hook → Agent SDK → hook loops

## Patterns Extracted

### Harness Engineering
- Zero-friction capture, recursion prevention, SessionStart knowledge injection, flush deduplication, detached background process spawning (cross-platform)

### System Design
- Compiler analogy, incremental compilation with hash tracking, 7-check lint system, file-back compounding queries

### Developer Experience
- Self-setup via AI agent ("repo as prompt"), cost transparency, pure markdown + Obsidian-native

## Entities Extracted
- [[claude-memory-compiler]] (new)

## Concepts Extracted
- [[zero-friction-capture]] (new), [[compiler-analogy]] (new), [[index-over-rag]] (new), [[time-gated-compilation]] (new), [[connection-articles]] (new)
- [[harness-design]] (updated), [[claude-code]] (updated)

## Source File
`raw/2026-04-07-repo-claude-memory-compiler.md`
