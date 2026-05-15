# Session Capture: loreai

**Date:** 2026-05-15
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Reviewing/ingesting a comprehensive guide on CLAUDE.md vs Claude Memory — when to use each system and how they complement each other.

**Key Exchanges:**
- Article covers the full mental model for Claude Code's two knowledge persistence systems: CLAUDE.md (file-based, team-shared, version-controlled) vs Claude Memory (file-per-memory with index, individual, local-only)

**Decisions Made:**
- **Decision rule:** "Would my teammate need this?" → Yes = CLAUDE.md, No = Memory
- **CLAUDE.md = "what" and "how"** (project rules, build commands, conventions, constraints)
- **Memory = "who" and "why"** (personal context, role, corrections, ephemeral project state)
- **Never duplicate across both systems** — drift between copies creates contradictory instructions
- **Memory can reference CLAUDE.md context; CLAUDE.md should never reference memory** (memory is personal/invisible to team)

**Lessons Learned:**
- CLAUDE.md loads entirely every session — no selective retrieval. Keep it concise (<50 lines ideal). 500-line files waste context window.
- Memory uses selective retrieval via index (`MEMORY.md`) — scales better but risks missing relevant memories if descriptions don't match current task.
- Memory staleness is a real problem: project-type memories decay fastest. Claude Code has a verification step but it's not foolproof.
- Memory doesn't have subdirectory scoping (unlike CLAUDE.md's directory hierarchy). A React preference applies everywhere.
- Memory doesn't sync across machines (`~/.claude/projects/`, local only). CLAUDE.md syncs via git.
- `MEMORY.md` index truncates at 200 lines; aim for 20-40 focused memories.
- More specific instructions tend to win when memory and CLAUDE.md conflict.

**Action Items:**
- Consider ingesting this as a wiki page (e.g., `wiki/claude-code-memory-vs-claude-md.md`) — high relevance to builder tools domain
- Review own CLAUDE.md against the "concise and universally relevant" principle
- Maintenance cadence: review CLAUDE.md quarterly or on stack changes; periodically prune `MEMORY.md` for stale project memories