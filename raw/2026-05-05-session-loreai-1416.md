# Session Capture: loreai

**Date:** 2026-05-05
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Drafting/reviewing an article comparing Claude Memory vs CLAUDE.md as persistence mechanisms in Claude Code.

**Key Exchanges:**
- Article covers the full decision framework for choosing between Memory (personal, cross-project, ephemeral) and CLAUDE.md (team, deterministic, reviewable)
- Memory sits above CLAUDE.md in prompt hierarchy — can add context but shouldn't contradict project rules
- CLAUDE.md loads fully into system prompt every session (no retrieval/filtering); Memory uses relevance-based retrieval

**Decisions Made:**
- CLAUDE.md wins on conflict with Memory (by design — reviewed rules > accumulated preferences)
- CLAUDE.md for team projects (consistency), Memory for personal projects (adaptation), both for mature setups
- Keep CLAUDE.md under 200 lines of actionable instructions to avoid context waste
- Skills (SKILL.md) are a third persistence layer — neither Memory nor CLAUDE.md

**Lessons Learned:**
- Stale CLAUDE.md causes subtle degradation (wrong conventions, skipped gates) — not visible failures
- Memory doesn't sync across devices or transfer between team members — knowledge silo risk
- Teams that put deployment/architecture info only in Memory create single-point-of-failure knowledge
- Treat CLAUDE.md updates as part of definition-of-done for any process change
- "If losing the information would block someone else's work, it belongs in CLAUDE.md or proper docs"

**Action Items:**
- Article references several internal links (`/blog/claude-code-memory`, `/blog/claude-code-complete-guide`, etc.) — ensure these exist or are planned
- Article is ready for `drafts/` — covers solo vs team, setup recommendations, FAQ section
- Could become a wiki page: `wiki/claude-code-memory-vs-claude-md.md` summarizing the decision framework