# Session Capture: loreai

**Date:** 2026-04-27
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Article/source content about Claude Code's two-tier context system (CLAUDE.md vs Claude Memory) was reviewed — likely candidate for ingestion into the wiki.

**Key Exchanges:**
- Source is a blog post (appears to be from LoreAI or a similar builder-focused publication) explaining CLAUDE.md vs Claude Memory as complementary systems with different scopes, load behaviors, and team applicability.

**Decisions Made:**
- No decisions recorded — this was a read-only context review with no tool calls or user actions taken.

**Lessons Learned:**
- **CLAUDE.md loads deterministically** as part of the system prompt, every session, for every user — use it for non-negotiable rules (build commands, architecture constraints, quality gates, team standards).
- **Claude Memory loads selectively** based on agent judgment of relevance — use it for personal preferences, role context, and temporal/situational project state.
- Key split: CLAUDE.md answers "what are the rules?"; Memory answers "who am I working with and what's the current situation?"
- In team settings, CLAUDE.md is the only context system that travels with the repo and applies to everyone — Memory is inherently personal.
- Memory can become stale silently (no PR review process); CLAUDE.md staleness is catchable in code review if treated like documentation.
- **Practical threshold:** information with shelf life < 1 sprint → be cautious saving to Memory; shelf life > 1 quarter → put in CLAUDE.md.
- Memory cannot override CLAUDE.md — CLAUDE.md is authoritative.

**Action Items:**
- Consider running `/ingest` on this source if a raw file exists — it maps well to the "Builder tools and workflows (Claude Code)" domain focus and would populate or update a `claude-code-memory-system.md` wiki page.