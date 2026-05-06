# Session Capture: loreai

**Date:** 2026-05-06
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Reviewing/ingesting a blog article comparing CLAUDE.md vs Claude Memory as persistence systems in Claude Code.

**Key Exchanges:**
- Article provides detailed architectural comparison: CLAUDE.md is a single version-controlled document for team-shared project instructions; Claude Memory uses file-per-memory design in `.claude/projects/{project-hash}/memory/` for personal/evolving context
- Memory index lives in `MEMORY.md`, individual memories are separate `.md` files with frontmatter (`name`, `description`, `type`)

**Decisions Made:**
- **CLAUDE.md for team consistency**: build commands, code style, architectural guardrails, workflow gates — anything that must be the same for all developers
- **Memory for personal context**: role/expertise, approach corrections, frequently changing project context, external system pointers
- **Start with CLAUDE.md** if choosing one to invest in first — highest immediate impact; Memory accumulates naturally
- **CLAUDE.md takes precedence** if Memory and CLAUDE.md conflict

**Lessons Learned:**
- Solo devs can blur the line; for teams the distinction is critical — putting team conventions in Memory causes fragmentation across developers
- Memory does NOT sync across devices (local only in `.claude/projects/`); CLAUDE.md syncs via git
- Pattern: "CLAUDE.md sets rules; Memory refines application" — e.g., CLAUDE.md says "write tests," Memory remembers you prefer integration tests over unit tests
- If you correct Claude about the same thing twice, promote it from Memory to CLAUDE.md
- Three-layer personal setup: repo-root CLAUDE.md (team), `~/.claude/CLAUDE.md` (personal globals), auto Memory (organic accumulation)

**Action Items:**
- Potential wiki page: `claude-code-memory-vs-claude-md.md` — this is a rich reference for the Claude Code tooling knowledge area
- Cross-reference with existing wiki pages on [[Claude Code]] architecture and extension stack