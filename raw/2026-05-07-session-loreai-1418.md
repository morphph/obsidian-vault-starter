# Session Capture: loreai

**Date:** 2026-05-07
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Drafted a Chinese comparison article (`claude-memory-vs-claude-md`) for the LoreAI blog.

**Key Exchanges:**
- Generated a full-length comparison piece covering Claude Memory (Auto Memory in `~/.claude/projects/`) vs CLAUDE.md (project-root instruction files)

**Decisions Made:**
- Framed the core distinction as **control & determinism**: CLAUDE.md = "law" (explicit, versioned, team-shared rules); Memory = "experience" (soft, auto-accumulated, personal context)
- Recommendation hierarchy: CLAUDE.md first as infrastructure, Memory layered on top for personalization
- Cross-linked to existing blog posts: `claude-code-memory`, `claude-code-seven-programmable-layers`, `anthropic-claude-memory-upgrades-importing`, `claude-code-extension-stack-skills-hooks-agents-mcp`

**Lessons Learned:**
- Claude Code Auto Memory and Claude.ai Memory are two independent implementations — Code version is file-system based, engineering-oriented
- CLAUDE.md supports subdirectory-level rules via recursive reading from root to CWD
- Memory files are plain markdown, manually editable, stored locally, never auto-uploaded

**Action Items:**
- Article needs to be saved to `drafts/` and committed/pushed per git workflow rules
- Verify all cross-referenced blog slugs (`related_blog` frontmatter) actually exist before publishing