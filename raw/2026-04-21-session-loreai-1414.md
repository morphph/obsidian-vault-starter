# Session Capture: loreai

**Date:** 2026-04-21
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Reading/reviewing an article about Claude Code's two persistence systems — CLAUDE.md vs Claude Memory — covering when to use each, their differences, and best practices.

**Key Exchanges:**
- Article distinguishes CLAUDE.md (team infrastructure, deterministic, version-controlled) from Claude Memory (personal adaptation layer, auto-learned, selective)
- Decision rule: "If removing this context would cause a bug or policy violation → CLAUDE.md. If it would just make Claude slightly less helpful to you personally → Memory is fine."
- CLAUDE.md loads fully every session (context cost); Memory loads selectively (only relevant files retrieved)
- Memory stored in `~/.claude/projects/` keyed by directory path, not git repo — clone to different path = fresh start

**Decisions Made:**
- What goes in CLAUDE.md: build commands, quality gates, architecture constraints, style guidelines, workflow rules, known gotchas, team-enforced rules
- What goes in Memory: role/expertise, communication preferences, external system pointers (Linear, Slack), temporal project state, confirmed judgment calls
- Keep CLAUDE.md under 200 lines; split task-specific instructions into skill files beyond 300 lines

**Lessons Learned:**
- Promoting memories to CLAUDE.md = how individual learning becomes team knowledge (explicit migration pattern)
- Memory can accumulate contradictory entries if preferences change — needs periodic audit
- CLAUDE.md has git history (auditability); Memory has no changelog
- CI/automated runs need CLAUDE.md — Memory is session-based and personal, doesn't exist in CI
- Memory files should be gitignored; if a memory contains team-relevant knowledge, migrate to CLAUDE.md

**Action Items:**
- This article is a strong candidate for `/ingest` into the wiki under a page like `claude-code-memory-vs-claudemd.md` or merged into an existing `claude-code.md` page