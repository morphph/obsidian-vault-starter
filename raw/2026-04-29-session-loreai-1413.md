# Session Capture: loreai

**Date:** 2026-04-29
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Reviewing/ingesting a detailed article comparing CLAUDE.md vs Claude Memory in Claude Code workflows.

**Key Exchanges:**
- Article provides a comprehensive framework for deciding what goes in CLAUDE.md vs Memory
- Covers team collaboration, maintenance patterns, content types, and conflict resolution

**Decisions Made:**
- **CLAUDE.md = team rules, Memory = personal context**: If context should be same for every developer → CLAUDE.md. If personal → Memory. If unsure → default to CLAUDE.md.
- **Priority hierarchy**: CLAUDE.md overrides Memory when they conflict. This ensures team standards beat individual preferences.
- **Start with CLAUDE.md, let Memory build naturally**: Don't pre-populate memories; let them accumulate through corrections and usage.

**Lessons Learned:**
- CLAUDE.md is version-controlled → `git blame` provides audit trail for AI behavior changes
- Memory creates asymmetry: experienced users get better AI assistance because richer memory store
- CLAUDE.md maintenance burden scales with project complexity; layered subdirectory approach helps for monorepos
- Stale memories (e.g., "migrating to CockroachDB" after migration completes) can mislead; review `~/.claude/projects/<project>/memory/` monthly
- Best maintenance pattern: update CLAUDE.md in the same PR that changes the underlying system
- CLAUDE.md for slow-changing rules, Memory for fast-changing context minimizes maintenance overhead

**Action Items:**
- Consider ingesting this as a wiki page (e.g., `wiki/claude-md-vs-memory.md`) — it's a strong reference for the builder-tools domain
- Cross-reference with existing wiki pages on [[Claude Code]] if they exist