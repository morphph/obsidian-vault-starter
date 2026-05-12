# Session Capture: loreai

**Date:** 2026-05-12
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Reviewing/drafting a blog post comparing CLAUDE.md vs Claude Memory — when to use each persistence layer in Claude Code.

**Key Exchanges:**
- Article explains the two knowledge persistence systems in Claude Code: CLAUDE.md (team-scoped, version-controlled) vs Claude Memory (user-scoped, local to `~/.claude/projects/`)
- Detailed breakdown of what content belongs where, with concrete examples

**Decisions Made:**
- **Decision rule:** "If it's a team rule, it goes in CLAUDE.md; if it's personal context, it goes in Memory."
- **CLAUDE.md takes precedence** over Memory entries when they conflict — Memory supplements but never overrides
- **CLAUDE.md loads unconditionally** every session; Memory entries are loaded based on relevance matching — safety-critical rules must go in CLAUDE.md

**Lessons Learned:**
- **Anti-pattern:** personal preferences in CLAUDE.md (clutters team config) or team rules in Memory (won't apply to other devs)
- Memory risks: accumulation without cleanup, stale references to renamed files/functions, no audit trail
- Memory has a 200-line soft limit in MEMORY.md index; 20-40 well-maintained entries covers most needs
- Memory does NOT sync across devices — stored locally only (`~/.claude/projects/`)
- Best practice: treat CLAUDE.md updates as part of definition-of-done — update in the same commit as the change it documents
- Debugging patterns belong in code comments/docs, NOT in either AI instruction layer
- Claude Code's seven programmable layers: CLAUDE.md sits at project config layer (above model, below conversation)

**Action Items:**
- This article appears ready for publication — references `/subscribe` CTA at the end
- Cross-references other posts: `/blog/claude-code-seven-programmable-layers`, `/blog/claude-code-memory`, `/blog/claude-code-extension-stack-skills-hooks-agents-mcp` — ensure these exist or are planned