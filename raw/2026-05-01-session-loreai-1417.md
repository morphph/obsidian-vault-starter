# Session Capture: loreai

**Date:** 2026-05-01
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Drafting/refining a blog post comparing CLAUDE.md vs Claude Memory in Claude Code workflows.

**Key Exchanges:**
- Detailed analysis of CLAUDE.md as team-shared project constitution vs Claude Memory as personal context layer
- Session startup flow: CLAUDE.md loads first (project rules), then Memory (personal context) — priority order matters
- Memory files stored locally in `.claude/projects/<hash>/memory/`, not synced via git, tied to path hashes

**Decisions Made:**
- **Priority hierarchy:** CLAUDE.md = hard constraints (law), Memory = soft context. CLAUDE.md wins on conflict.
- **Decision rule for teams:** "Would this help other contributors?" → Yes = CLAUDE.md, No = Memory
- **Migration path:** When a Memory-learned pattern proves universally useful, promote it to CLAUDE.md
- **Don't commit Memory files to git** — promote to CLAUDE.md or SKILL.md instead if worth sharing

**Lessons Learned:**
- CLAUDE.md staleness is visible (you see the file); Memory staleness is hidden (dotfile directories nobody browses)
- Memory can drift/accumulate stale entries — review `.claude/projects/<hash>/memory/` every few weeks
- Most common mistake: personal preferences in CLAUDE.md (annoys team) or team-critical knowledge only in Memory (invisible to others)
- Claude Code treats memories as "claims to verify" (e.g., checks if a remembered file path still exists) — but risk remains
- Memory doesn't sync across devices; CLAUDE.md syncs via git automatically

**Action Items:**
- Article references companion posts: "how to effectively prompt Claude Code," "claude-code-complete-guide," "whats-so-special-about-claude-code" — ensure those are published/linked
- Consider ingesting this into wiki as a page on Claude Code configuration best practices (`wiki/claude-code-config-layers.md` or similar)