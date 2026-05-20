# Session Capture: loreai

**Date:** 2026-05-20
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Reviewing a detailed article comparing Claude Memory vs CLAUDE.md as context mechanisms in Claude Code.

**Key Exchanges:**
- CLAUDE.md is a **team artifact** — version-controlled, code-reviewed, read by CI/CD. Memory is a **personal artifact** — local, auto-accumulated, per-developer.
- When they conflict, **CLAUDE.md wins** (authoritative project rules override personal preferences).
- Memory has four types: User (role/expertise), Feedback (behavioral corrections), Project (dynamic state), Reference (external system pointers).
- Memory files live in `~/.claude/projects/<hash>/memory/` with a `MEMORY.md` index. Keep index under 200 lines to avoid context window bloat.
- Memory does **not** sync across devices or get read by CI runners/sub-agents.

**Decisions Made:**
- **Decision framework established:** CLAUDE.md for stable team rules, architectural constraints, build/deploy commands, CI-affecting instructions. Memory for personal preferences, dynamic project state, external references, time-sensitive info.
- **Promotion pattern:** When 3+ developers independently tell Claude the same thing (e.g., "use pnpm not npm"), promote from Memory to CLAUDE.md.

**Lessons Learned:**
- Memory entries are fragile — "merge freeze starts May 25" becomes stale. Treat Memory as "true when written," not permanent truth. Periodic pruning needed.
- CLAUDE.md doesn't have staleness problem because it follows the code (updated in same commit as code changes).
- Common mistake: putting personal preferences in CLAUDE.md (clutters shared config) or putting critical rules in Memory (invisible to teammates and CI).
- Recommended team rollout: minimal CLAUDE.md week 1 → let Memory accumulate weeks 2-4 → review and promote patterns month 2.

**Action Items:**
- Potential wiki page: `claude-code-memory-vs-claude-md.md` covering the decision framework and team rollout sequence.
- Cross-reference with existing [[claude-code]] wiki pages if they exist.