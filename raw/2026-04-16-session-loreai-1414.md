# Session Capture: loreai

**Date:** 2026-04-16
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Reviewing a LoreAI blog article on CLAUDE.md vs Claude Memory — when to use each, decision rules, and common mistakes.

**Key Exchanges:**
- Article explains CLAUDE.md = shared team config (version-controlled, deterministic, authoritative); Memory = personal context layer (automatic, adaptive, private, advisory)
- CLAUDE.md always wins conflicts with Memory — by design
- Memory is stored locally in `~/.claude/projects/` — does NOT sync across machines or teammates

**Decisions Made:**
- Clear split rule: "If you'd put it in a PR description → CLAUDE.md. If you'd say it in a 1:1 → Memory."
- Each fact should live in exactly ONE place (no duplication between CLAUDE.md and Memory)
- CLAUDE.md sweet spot: 30–80 lines. Over 200 lines = bloat (belongs in docs, skills, or Memory)

**Lessons Learned:**
- Stale CLAUDE.md instructions are worse than missing ones — stale = confidently wrong behavior
- Common mistake: putting team rules in Memory (only applies to you, not teammates)
- Skills (SKILL.md files) act as middle ground — repo-shared like CLAUDE.md, but invoked on-demand rather than loaded every session
- Layered CLAUDE.md (root + subdirectory) mirrors monorepo structure cleanly
- New devs benefit most from Memory — it builds personalized onboarding context automatically

**Action Items:**
- This article is a strong candidate for `/ingest` into the wiki under builder tools & workflows (Claude Code tooling)
- Consider creating a `claude-code-memory.md` wiki page synthesizing this with other Claude Code content