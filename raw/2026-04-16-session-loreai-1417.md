# Session Capture: loreai

**Date:** 2026-04-16
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Reviewing an article about Claude Code memory architecture — CLAUDE.md vs. Claude Memory files — likely as candidate raw material for ingestion.

**Key Exchanges:**
- No back-and-forth; this was a document review session, not a dialogue.

**Decisions Made:**
- None recorded.

**Lessons Learned:**
- **CLAUDE.md vs Memory distinction**: CLAUDE.md = shared, deterministic, version-controlled project rules. Memory (`~/.claude/projects/[project]/memory/MEMORY.md`) = personal, adaptive, heuristic — not synced across machines, not for version control.
- **CLAUDE.md takes precedence** when it conflicts with memory. Avoid duplicating project facts in both layers.
- **Memory staleness**: Add "as of [date]" context to project memories so freshness can be assessed. Claude should verify memories against current code before acting.
- **Don't pre-populate memory** — let it build naturally from corrections and context shared across real sessions.
- **Memory location path**: `~/.claude/projects/[your-project]/memory/MEMORY.md`
- **CLAUDE.md token cost**: ~700 tokens per 500 words. Keep it concise; move explanatory content to on-demand docs.

**Action Items:**
- Consider ingesting this article as `raw/` source on Claude Code memory best practices — relevant to vfan's builder workflow and LoreAI project context.