# Session Capture: loreai

**Date:** 2026-04-27
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Session contained an article about Claude Code's CLAUDE.md vs Claude Memory systems — likely source material for wiki ingestion.

**Key Exchanges:**
- No actual Q&A exchanges occurred; session context is primarily a long-form article explaining the two context systems in Claude Code.

**Decisions Made:**
- (None recorded — no human-LLM decision dialogue visible)

**Lessons Learned:**
- CLAUDE.md loads **deterministically** at session start (every line injected into system prompt); Memory loads **selectively** based on relevance — this distinction drives the whole framework
- CLAUDE.md is a **team artifact** (version-controlled, PR-reviewed); Memory is **personal** (no git push for Memory)
- Critical rules → CLAUDE.md; nice-to-have personal context → Memory
- Memory does NOT sync across devices; CLAUDE.md syncs through Git
- CLAUDE.md instructions cannot be overridden by Memory
- Recommended size for CLAUDE.md: 50–200 lines; >300 lines → split into SKILL.md files
- Layering: Global `~/.claude/CLAUDE.md` → Project CLAUDE.md → Auto Memory → SKILL.md (on-demand)

**Action Items:**
- This article is a strong candidate for `/ingest` into the wiki under a page like `claude-code-memory-vs-claudemd.md` — domain-relevant (Builder tools + Claude Code workflows)