# Session Capture: loreai

**Date:** 2026-04-14
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Article ingestion — Claude Code: Memory vs CLAUDE.md comparison and best practices

**Key Exchanges:**
- Detailed breakdown of CLAUDE.md (deterministic, always loaded, version-controlled, team-shared) vs Claude Memory (probabilistic recall, private, conversation-driven, locally stored)
- CLAUDE.md supports directory-level scoping (mirrors `.gitignore` pattern); Memory is project-wide only, no subdirectory granularity
- Memory stored locally at `~/.claude/projects/{project-hash}/memory/` — does NOT sync across devices

**Decisions Made:**
- Clear division of ownership: CLAUDE.md = team instruction manual; Memory = personal adaptation layer
- Decision rule: "If removing it would break Claude Code for the whole team → CLAUDE.md. If only affects your experience → Memory"

**Lessons Learned:**
- CLAUDE.md changes go through code review (auditable); Memory changes are invisible to teammates
- 5 anti-patterns: (1) build commands in Memory, (2) personal preferences in team CLAUDE.md, (3) ephemeral state (code freezes) in CLAUDE.md, (4) ignoring Memory entirely, (5) duplicating info across both systems
- Memory cannot override CLAUDE.md — project rules always take priority
- Staleness risk: Memory can silently become outdated; CLAUDE.md evolves with the codebase via PRs
- CLAUDE.md is the first thing to set up when a team adopts Claude Code

**Action Items:**
- Consider ingesting this article as a raw source for a `claude-code-memory-vs-claudemd.md` wiki page (source: appears to be from loreai.dev blog)