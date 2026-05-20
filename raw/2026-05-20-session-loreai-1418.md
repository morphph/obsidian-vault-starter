# Session Capture: loreai

**Date:** 2026-05-20
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Ingested/reviewed a detailed article comparing Claude Code's two persistence layers — CLAUDE.md (deterministic, shared) vs Claude Memory (personal, contextual).

**Key Exchanges:**
- CLAUDE.md loads every token into context at session start — no filtering, no relevance scoring. Reliable but costs context window space.
- Memory loads via index; Claude reads full records only when deemed relevant. More context-efficient but non-deterministic (may skip relevant records).
- CLAUDE.md is version-controlled team infrastructure; Memory is private per-developer.

**Decisions Made:**
- **Primary rule:** Must-follow instructions → CLAUDE.md; nice-to-know context → Memory.
- **Team rule:** Anything you want to share with teammates belongs in CLAUDE.md, not Memory. If you want to share a Memory record, that's a signal it should be in CLAUDE.md.
- **Size guidance:** Keep CLAUDE.md under 500 lines. Overflow detailed instructions into `skills/*/SKILL.md` files that load on demand.

**Lessons Learned:**
- CLAUDE.md staleness is **visible** (breaks builds, gets fixed fast). Memory staleness is **invisible** (outdated records persist and mislead silently).
- Memory does NOT sync across devices — it's local to `~/.claude/projects/`. CLAUDE.md syncs via git.
- Memory cannot override CLAUDE.md — explicit CLAUDE.md directives always win in conflicts.
- Claude.ai memory and Claude Code file-based memory are **separate systems** that don't share data.
- Best pattern: CLAUDE.md handles the "what" and "how"; Memory handles the "who" and "why."

**Action Items:**
- This article is a good candidate for a wiki page (e.g., `wiki/claude-code-persistence-layers.md`) covering CLAUDE.md vs Memory architecture, since the project's own CLAUDE.md already leverages these patterns.
- Quarterly CLAUDE.md review + periodic Memory hygiene are recommended maintenance practices worth adopting.