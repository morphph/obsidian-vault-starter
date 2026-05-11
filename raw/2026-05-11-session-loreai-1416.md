# Session Capture: loreai

**Date:** 2026-05-11
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Reviewing/processing a blog article about Claude Memory vs CLAUDE.md — the two persistence layers in Claude Code.

**Key Exchanges:**
- Article lays out the architectural difference: CLAUDE.md loads deterministically every session; Memory loads selectively based on relevance
- CLAUDE.md wins over Memory when instructions conflict — it's the authoritative source
- Decision framework: "If removing it would break the project for a new team member → CLAUDE.md. If it only degrades personalization for you → Memory."

**Decisions Made:**
- CLAUDE.md is for team-wide, non-negotiable project rules (build commands, quality gates, coding standards, gotchas)
- Memory is for personal context (role, preferences, feedback corrections, temporal info like deadlines)
- Global `~/.claude/CLAUDE.md` serves as a middle ground — personal but deterministic, applied across all projects
- Recommended CLAUDE.md size: 50–200 lines to avoid context bloat

**Lessons Learned:**
- Memory doesn't sync across devices (stored locally in `.claude/projects/`, typically gitignored)
- Memory can go stale — deadlines that passed, references to archived projects, corrections that no longer apply
- Pattern: start with Memory, promote to CLAUDE.md when you find yourself re-correcting Claude on something that should be a project rule
- CLAUDE.md has a "staleness advantage" because it's version-controlled and code-reviewed

**Action Items:**
- This article is a candidate for `/ingest` into the wiki — covers Claude Code workflow architecture relevant to the builder tools domain
- Could inform updates to this repo's own CLAUDE.md conventions (the article's best practices align with existing structure but offer the 50–200 line guideline as a useful benchmark)