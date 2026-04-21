# Session Capture: loreai

**Date:** 2026-04-21
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Reviewing/processing a long-form comparison article on Claude Code vs OpenAI Codex, likely for wiki ingest or draft creation for LoreAI.

**Key Exchanges:**
- No interactive dialogue — the session context is entirely the article content itself (no user questions or Claude responses captured).

**Decisions Made:**
- N/A — no decisions visible in this session fragment.

**Lessons Learned:**
- Claude Code vs Codex distinction: **interactive pair programmer** (local, real-time, steerable) vs **async task queue** (sandboxed, PR-based, parallelizable)
- Claude Code reads `CLAUDE.md` + `SKILL.md`; Codex reads `AGENTS.md` — both can coexist in same repo
- Pricing snapshot: Claude Code on Pro ($20/mo, usage-based tokens); Codex full access requires ChatGPT Pro ($200/mo); Plus ($20/mo) gives limited Codex
- Multi-agent parallelism differs: Claude Code = coordination *within* a task; Codex = parallelism *across* independent tasks
- Safety tradeoff: Claude Code has real shell access (mitigated by hooks); Codex defaults to network-disabled sandbox

**Action Items:**
- Consider ingesting this article into `raw/` as a source for a `claude-code-vs-codex.md` wiki page — covers Claude Code capabilities, Codex capabilities, pricing data, and decision framework relevant to the builder tools domain.