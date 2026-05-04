# Session Capture: loreai

**Date:** 2026-05-04
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Drafting a Chinese comparison article on Codex Subagents vs Custom Agents for the LoreAI blog.

**Key Exchanges:**
- Generated a complete `compare/` article: `use-subagents-and-custom-agents-in-codex`

**Decisions Made:**
- Framed the two features as complementary layers, not competing alternatives: Subagents = "怎么拆" (how to split), Custom Agents = "拆给谁" (who to assign to)
- Mapped Codex concepts to Claude Code equivalents: Agent Teams ↔ Subagents, Skills system ↔ Custom Agents — this cross-referencing pattern is useful for the bilingual audience

**Lessons Learned:**
- When comparing two features from the same platform that aren't direct competitors, the "complementary layers" frame (one handles orchestration, the other handles specialization) works better than a winner/loser structure

**Action Items:**
- Article needs to be saved to the appropriate path in the repo and committed/pushed
- Internal links reference several existing blog posts (`codex-complete-guide`, `claude-code-agent-teams`, `claude-code-extension-stack-skills-hooks-agents-mcp`, etc.) — verify these slugs are live before publishing