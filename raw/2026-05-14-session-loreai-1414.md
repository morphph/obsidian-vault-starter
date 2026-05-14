# Session Capture: loreai

**Date:** 2026-05-14
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Reviewing a blog post / article about CLAUDE.md vs Claude Memory — two complementary configuration systems in Claude Code.

**Key Exchanges:**
- Article explains the architecture: CLAUDE.md is team-wide project config (git-tracked, imperative, 50–200 lines), Claude Memory is personal context (local `~/.claude/projects/`, structured markdown with typed frontmatter, self-maintaining)
- Memory entries use `[[wikilinks]]` to build a knowledge graph; CLAUDE.md is flat with no linking
- Precedence rule: CLAUDE.md always overrides Memory if they conflict

**Decisions Made:**
- CLAUDE.md handles **project truth** (build commands, guardrails, standards); Memory handles **personal context** (role, preferences, corrections, temporal info)
- For long CLAUDE.md files (>200 lines), move detailed guidelines into `skills/` files loaded on-demand
- Update CLAUDE.md in the same PR that changes the behavior it documents

**Lessons Learned:**
- Common mistakes: putting personal prefs in CLAUDE.md, relying on Memory for team rules, duplicating across both, never reviewing Memory, writing 500-line CLAUDE.md files
- Memory doesn't sync across devices; CLAUDE.md does (via git)
- Stale CLAUDE.md is worse than no CLAUDE.md — actively misleads the AI
- Memory entries follow `rule → Why → How to apply` structure for feedback type
- The "correction you give once should stick" — if repeating corrections, that's the signal to let Memory capture it

**Action Items:**
- Potential wiki page: `claude-code-configuration.md` covering the CLAUDE.md + Memory architecture as builder tooling knowledge
- Cross-reference with existing Claude Code / builder workflow pages if any exist