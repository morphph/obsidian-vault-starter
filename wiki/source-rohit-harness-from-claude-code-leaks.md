---
type: source-summary
created: 2026-04-09
last-updated: 2026-04-09
sources:
  - raw/2026-04-09-rohit-harness-from-claude-code-leaks.md
tags: [wiki, source, claude-code, architecture]
---

# Source: How I Built Harness for My Agent Using Claude Code Leaks

## Summary
Comprehensive architectural blueprint by Rohit (@rohit4verse) based on reverse-engineering Claude Code's 55 directories and 331 modules. 298K views, 2,403 bookmarks. Introduces the "4th layer" thesis (infrastructure beyond harness) and documents async generator patterns, streaming tool execution, and the 823-line retry system.

## Details
- **Author:** Rohit (@rohit4verse) — Engineer, FullStack + Applied AI
- **Published:** 2026-04-08 on X (long-form article)
- **Engagement:** 298K views, 2,403 bookmarks, 752 likes
- **Approach:** "Not a teardown. It is a blueprint." — practical patterns you can implement

## Key Contributions to Wiki
- Introduced [[infrastructure-layer]] — the "4th layer" beyond weights/context/harness
- Updated [[query-loop]] with async generator pattern, 5-phase iteration, streaming tool executor, dependency injection
- Updated [[harness-design]] with Layer 4 thesis
- Updated [[prompt-cache-optimization]] with system prompt boundary design

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-09 | raw/2026-04-09-rohit-harness-from-claude-code-leaks.md | Initial creation |
