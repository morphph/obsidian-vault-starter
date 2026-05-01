# Session Capture: loreai

**Date:** 2026-05-01
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Drafting/reviewing a blog article comparing CLAUDE.md vs Claude Memory for Claude Code context management.

**Key Exchanges:**
- Article covers the two-layer context system: CLAUDE.md (shared, version-controlled, deterministic) vs Memory (personal, adaptive, automatic)
- Decision framework for what belongs where, with concrete examples of common misplacements

**Decisions Made:**
- **CLAUDE.md wins conflicts**: When Memory and CLAUDE.md contradict, CLAUDE.md takes priority (deterministic load at session start)
- **Start with CLAUDE.md if forced to choose one**: It provides the foundation; Memory adds personalization on top
- **Promotion workflow**: Discover patterns in Memory → validate through use → promote to CLAUDE.md for team benefit

**Lessons Learned:**
- Memory is stored locally (`~/.claude/projects/`), does NOT sync across devices — CLAUDE.md travels with git
- CLAUDE.md should stay under ~500 lines; use subdirectory CLAUDE.md or SKILL.md files to avoid bloat
- Putting temporal context (e.g., "we're migrating from Postgres") in CLAUDE.md causes context rot — Memory handles shelf-life info better
- Putting build rules in Memory is risky — relevance filtering may skip them in some sessions
- Memory can't detect when codebase changes invalidate it; periodic review needed (monthly for project/reference memories)
- CLAUDE.md at multiple directory levels mirrors org structure: root = universal rules, subdirs = team-specific

**Action Items:**
- Article references several internal links (`/blog/claude-code-memory`, `/blog/claude-code-extension-stack-skills-hooks-agents-mcp`, etc.) — ensure those exist or are planned
- Article ends with `/subscribe` CTA — confirm LoreAI subscribe page is live
- Consider ingesting this article's framework into `wiki/` as a reference page on Claude Code context management best practices