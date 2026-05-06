# Session Capture: loreai

**Date:** 2026-05-06
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Reviewing/drafting a comprehensive article comparing CLAUDE.md vs Claude Memory as context mechanisms in Claude Code.

**Key Exchanges:**
- Article establishes a clear mental model: CLAUDE.md = project constitution (shared, deterministic, explicit); Memory = personal relationship (learned, adaptive, individual)
- Hierarchy rule: when CLAUDE.md and Memory conflict, CLAUDE.md always wins — by design

**Decisions Made:**
- **Three-layer architecture for Claude Code context:** team rules (project CLAUDE.md) → personal rules (global `~/.claude/CLAUDE.md`) → learned context (Memory)
- **CLAUDE.md owns the objective layer:** build/test commands, quality gates, architecture constraints, coding style, workflow rules
- **Memory owns the subjective layer:** role/expertise, communication preferences, corrections, external system references, frequently-changing project context
- **Global CLAUDE.md bridges the gap:** personal deterministic rules that aren't project-specific but shouldn't rely on Memory's probabilistic recall

**Lessons Learned:**
- Memory staleness risk is higher than CLAUDE.md staleness — memories accumulate silently with no review process; old project context can mislead
- Memory hygiene is necessary: periodically review `.claude/projects/*/memory/` and remove stale entries
- Keep CLAUDE.md concise — every line consumes context window tokens every session; move reference material into skills files
- Don't duplicate between systems — they are complementary, not redundant
- Memory should avoid saving "code patterns, conventions, architecture" derivable from current project state
- CLAUDE.md staleness has a tight feedback loop (wrong build command → immediate failure → fix), Memory does not
- Solo devs can lean on Memory; teams must prioritize CLAUDE.md for cross-contributor consistency

**Action Items:**
- Article references several internal links (`/blog/5-claude-code-skills-i-use-every-single-day`, `/blog/how-to-effectively-prompt-a-claude-code`, `/blog/claude-code-extension-stack-skills-hooks-agents-mcp`, `/blog/9-principles-writing-claude-code-skills`) — ensure these exist or are planned
- Consider ingesting this into wiki as a page on Claude Code context management patterns (covers [[CLAUDE.md]], [[Claude Memory]], team workflows)