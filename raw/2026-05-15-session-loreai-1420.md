# Session Capture: loreai

**Date:** 2026-05-15
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Generated a comparison article draft (`claude-memory-vs-claude-md`) for the blog, comparing Claude's two persistence mechanisms.

**Key Exchanges:**
- Drafted a full zh-lang compare article covering mechanism differences, team collaboration implications, and practical usage patterns for Claude Memory vs CLAUDE.md

**Decisions Made:**
- Framed the two systems as complementary, not competing: "规则放 CLAUDE.md，经验放 Memory"
- Core distinction: CLAUDE.md = deterministic (always loaded), Memory = probabilistic (semantically recalled)
- CLAUDE.md has higher priority — Memory cannot override CLAUDE.md rules
- Recommended three-layer approach: CLAUDE.md defines "laws," Memory accumulates "case law," periodic cleanup keeps Memory fresh

**Lessons Learned:**
- Memory is local-only, never enters Git — team consistency risk if relied upon for shared standards
- Critical engineering constraints (build steps, security rules, quality gates) must go in CLAUDE.md for 100% execution guarantee
- Memory recall degrades as entries accumulate — monthly manual review recommended
- The CLAUDE.md + Skills layer handles deterministic instructions; Memory + Hooks handle dynamic context — maps cleanly to the extension stack framework

**Action Items:**
- Article needs human review/polish before publish (now in drafts/)
- Related glossary entries referenced (`claude-code`, `claude-md`) — verify they exist in wiki
- Related blog posts referenced — verify slugs are correct: `claude-code-memory`, `anthropic-claude-memory-upgrades-importing`, `how-to-effectively-prompt-a-claude-code`, `5-claude-code-skills-i-use-every-single-day`, `claude-code-extension-stack-skills-hooks-agents-mcp`, `claude-code-seven-programmable-layers`, `9-principles-writing-claude-code-skills`