# Session Capture: loreai

**Date:** 2026-04-14
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Read/processed an article comparing Claude Memory vs CLAUDE.md in Claude Code — covering architecture, loading behavior, content boundaries, and when to use each.

**Key Exchanges:**
- Article covers two distinct context systems in Claude Code: CLAUDE.md (project rulebook) vs Claude Memory (personal notebook)
- CLAUDE.md loads entirely at conversation start, every line pays context-window rent on every conversation
- Memory uses lazy-loading: MEMORY.md index loads first, individual memory files only load when relevant
- MEMORY.md index capped at 200 lines; individual memory files have no practical limit

**Decisions Made:**
- Clear content boundary: CLAUDE.md = imperative rules + project facts (build commands, quality gates, architectural constraints); Memory = accumulated personal context (role, preferences, corrections, decision rationale)
- Neither system should store: derivable code patterns, git history, debugging solutions, ephemeral task details
- If it answers "what should Claude always do?" → CLAUDE.md. If "what does Claude need to know about me?" → Memory.

**Lessons Learned:**
- Stale CLAUDE.md is worse than no CLAUDE.md — outdated instructions cause confident wrong behavior
- Memory has built-in staleness risk; verification principle exists but isn't foolproof
- Trying to put personal preferences in CLAUDE.md bloats context on every conversation
- If a memory proves universally useful, promote it to CLAUDE.md (copy rule, delete memory + index entry)
- Teams sharing memory files is fragile — no merge strategy, not designed for manual editing

**Action Items:**
- This article is a strong candidate for `/ingest` into the wiki under builder tools / Claude Code workflow knowledge (source: appears to be from LoreAI blog or similar)