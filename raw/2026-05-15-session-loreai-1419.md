# Session Capture: loreai

**Date:** 2026-05-15
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Reviewing/ingesting a comprehensive article comparing Claude Code's CLAUDE.md vs Claude Memory systems — when to use each and best practices.

**Key Exchanges:**
- Article provides a clear decision framework: CLAUDE.md for shared/deterministic/code-coupled rules; Memory for personal/emergent/ephemeral context
- Memory is relevance-filtered (loaded on-demand), CLAUDE.md loads every turn — this has token cost implications
- Memory is local-only (`~/.claude/projects/`), no sync across devices or team members

**Decisions Made:**
- CLAUDE.md size target: 500–2,000 words; beyond that, move detail into SKILL.md files
- "If forgetting it would cause a bug or violate a team standard → CLAUDE.md. If forgetting it would make Claude slightly less helpful → Memory."
- Memory cannot override CLAUDE.md — it provides context, not overrides

**Lessons Learned:**
- Common mistake: putting personal preferences in CLAUDE.md or team rules in Memory
- Memory risk: accumulation without pruning over months → contradictory/stale entries
- CLAUDE.md risk: instruction rot — rules added months ago may no longer apply
- Pattern: use Memory as "CLAUDE.md staging" — capture rules discovered mid-session, promote later
- Pattern: CLAUDE.md for the rule, Memory for the *why* behind it (helps Claude reason about related decisions)
- CLAUDE.md sits in a 7-layer stack alongside Skills, Hooks, MCP servers

**Action Items:**
- Worth creating/updating wiki pages: [[claude-code-memory]], [[claude-code-claude-md]], or a combined [[claude-code-configuration]] page covering the CLAUDE.md vs Memory decision framework
- Cross-reference with existing [[claude-code]] wiki content if present