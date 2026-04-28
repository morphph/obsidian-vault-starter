# Session Capture: loreai

**Date:** 2026-04-28
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Reviewing/processing an article about CLAUDE.md vs Claude Memory in Claude Code — likely source material for wiki ingestion or draft creation.

**Key Exchanges:**
- Article provides a comprehensive framework for choosing between CLAUDE.md (shared project rules) and Claude Memory (personal adaptive context)
- Decision heuristic: "If removing it would break a teammate's workflow → CLAUDE.md. If removing it would only affect your own experience → Memory."

**Decisions Made:**
- CLAUDE.md = deterministic foundation (always loads, team-shared, code-reviewed); Memory = adaptive optimization (auto-learns, personal, temporal)
- CLAUDE.md should stay under 200 lines of actionable instructions; reference material goes to `docs/` or Memory
- CLAUDE.md hierarchy is directory/spatial-based; Memory hierarchy is type/temporal-based
- If forced to pick one: start with CLAUDE.md — it's the foundation, Memory is the optimization

**Lessons Learned:**
- Don't use CLAUDE.md as a knowledge base — it loads every session, bloating tokens
- Don't duplicate CLAUDE.md instructions in Memory — creates drift risk
- Don't store ephemeral task state in Memory — convert relative dates to absolute, only save what's useful cross-session
- Memory doesn't sync across devices; CLAUDE.md does (via git)
- Memory cannot override CLAUDE.md — project rules always win
- Three-layer context stack: CLAUDE.md (project rules) + Memory (personal context) + SKILL.md (task instructions)

**Action Items:**
- Article references enterprise case studies (Ramp, Shopify, Spotify) and links to other blog posts — these could be future `/ingest` targets
- Article ends with LoreAI subscribe CTA — confirms this is publication-ready content for the blog