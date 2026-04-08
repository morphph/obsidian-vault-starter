---
type: source-summary
created: 2026-04-08
last-updated: 2026-04-08
sources:
  - raw/2026-04-08-troyhua-claude-code-7-layers-memory.md
tags: [wiki, source, claude-code, architecture]
---

# Source: How Anthropic Built 7 Layers of Memory and a Dreaming System for Claude Code

## Summary
Comprehensive reverse-engineering by [[troy-hua]] of every memory and context management system inside Claude Code's leaked harness. Covers the full 7-layer architecture from tool result storage to cross-agent communication, with source file paths, configuration values, and design rationale. The most detailed public technical breakdown of Claude Code's internals.

## Details
- **Author:** Troy Hua (@troyhua) — Agentic Memory at EverMind, PhD Dialogue Systems at CMU
- **Published:** 2026-04-01 on X (long-form article format)
- **Engagement:** 135K views, 850 bookmarks, 395 likes, 100 reposts
- **Method:** Reverse-engineering Claude Code's leaked/open source code
- **Includes:** Embedded videos for key sections, architecture diagrams, configuration tables

## Key Contributions to Wiki
- Corrected [[context-management]] from "4 layers" to 7 layers with full breakdown
- Introduced [[session-memory]] — the "free compaction" mechanism
- Introduced [[dreaming]] — cross-session memory consolidation
- Introduced [[forked-agent-pattern]] — foundation of all background operations
- Introduced [[prompt-cache-optimization]] — 200x cost difference driving architecture
- Added circuit breaker stats to [[context-anxiety]] (250K wasted API calls/day)
- Updated [[claude-code]] with internal system details

## Pages Created
- [[troy-hua]], [[session-memory]], [[dreaming]], [[forked-agent-pattern]], [[prompt-cache-optimization]]

## Pages Updated
- [[context-management]], [[claude-code]], [[context-anxiety]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-08 | raw/2026-04-08-troyhua-claude-code-7-layers-memory.md | Initial creation |
