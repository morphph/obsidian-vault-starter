# Session Capture: loreai

**Date:** 2026-05-08
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Ingested/reviewed a comprehensive guide on Claude Memory vs CLAUDE.md — the decision framework for where to store different types of AI agent configuration.

**Key Exchanges:**
- Article covers the two-layer system: CLAUDE.md (shared, versioned project rules) vs Claude Memory (personal, adaptive, per-user)
- Decision rule distilled: "If a teammate needs it, commit it. If only you need it, let memory handle it."

**Decisions Made:**
- CLAUDE.md wins for: build commands, coding standards, architectural constraints, quality gates, project gotchas — anything team-wide and reviewable
- Memory wins for: personal preferences, behavioral feedback/corrections, project status (temporal), external system references (Linear, Grafana, etc.)
- CLAUDE.md takes precedence when memory conflicts with it — by design
- Memory is per-user, not synced across team; stored in `.claude/projects/<hash>/memory/`

**Lessons Learned:**
- **Common mistake #1:** Personal preferences in CLAUDE.md leak to all teammates
- **Common mistake #2:** Critical project rules in memory only — lost when person leaves
- **Common mistake #3:** Duplicating CLAUDE.md content in memory creates staleness risk
- **Common mistake #5:** Verbose CLAUDE.md wastes context tokens every session — keep concise, put details in separate files
- Four-layer config strategy: CLAUDE.md (foundation) → Skills (task-specific) → Memory (personal adaptation) → Global ~/.claude/CLAUDE.md (cross-project preferences)
- Convert relative dates to absolute in memory entries to prevent staleness ("Thursday" → "2026-05-08")

**Action Items:**
- Consider creating wiki page: `claude-code-configuration.md` covering this Memory vs CLAUDE.md framework
- Cross-reference with existing [[claude-code]] wiki pages if any
- This content traces to a blog post source — should be saved to `raw/` if not already there before wiki page creation