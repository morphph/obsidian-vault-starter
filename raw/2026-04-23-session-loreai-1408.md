# Session Capture: loreai

**Date:** 2026-04-23
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Reviewing a blog post comparing Claude Memory vs CLAUDE.md — when to use each, scope differences, content guidelines, and failure modes.

**Key Exchanges:**
- Article explains two distinct context systems: CLAUDE.md (shared, version-controlled, deterministic) vs Memory (personal, automatic, adaptive)
- Memory is AI-authored from conversation signals; CLAUDE.md requires active human maintenance
- CLAUDE.md supports hierarchical scoping: root + subdirectory files that merge with precedence

**Decisions Made:**
- Clear division of content types: CLAUDE.md for build commands, architecture constraints, gotchas, quality gates; Memory for personal preferences, role, communication style, ongoing project context
- Gray zone rule: **does this apply to the whole team, or just to me?** → Team = CLAUDE.md, Personal = Memory

**Lessons Learned:**
- CLAUDE.md fails loudly (wrong command → visible error → tight feedback loop); Memory fails quietly (stale assumptions, subtle drift, hard to catch)
- Memory entries need periodic manual auditing — completed projects, outdated team context, reversed decisions
- Don't duplicate info in both systems — CLAUDE.md is authoritative for project facts
- CLAUDE.md that's too long (500+ lines) dilutes important instructions — keep focused
- Memory cannot override CLAUDE.md directives; CLAUDE.md is treated as authoritative constraints
- Global `~/.claude/CLAUDE.md` fills a similar role to Memory but requires manual authoring — use for hard rules across all projects

**Action Items:**
- Consider ingesting this article as a raw source if it's from LoreAI blog or a tracked Anthropic/Claude tooling source
- Potential wiki page: `claude-code-memory-vs-claudemd.md` under Builder Tools category