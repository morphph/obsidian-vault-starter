# Session Capture: loreai

**Date:** 2026-05-13
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Drafted a Chinese comparison article "Claude Memory vs CLAUDE.md" for the LoreAI blog.

**Key Exchanges:**
- Generated a full `/compare` article distinguishing Claude Memory (auto user-level persistence in `~/.claude/`) from CLAUDE.md (manual project-level config in Git)

**Decisions Made:**
- Framing: Memory = "who you are" (personal prefs), CLAUDE.md = "how this project works" (team rules). Not either/or — complementary layers.
- Recommendation: solo projects start with Memory (zero cost); team projects start with CLAUDE.md (consistency). Eventually use both.

**Action Items:**
- Article needs to be saved to `drafts/` and committed/pushed per Git workflow rules
- Related blog cross-links reference several existing posts (`claude-code-memory`, `claude-code-seven-programmable-layers`, etc.) — verify those slugs still resolve