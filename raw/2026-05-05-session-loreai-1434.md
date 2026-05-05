# Session Capture: loreai

**Date:** 2026-05-05
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Creating a Chinese-language comparison article (Codex CLI vs Claude Code) for the LoreAI blog.

**Key Exchanges:**
- Generated a full `/zh/compare/codex-cli-vs-claude-code` article with frontmatter, feature table, and detailed analysis sections

**Decisions Made:**
- Framed the core distinction as **security isolation (Codex CLI)** vs **deep workflow integration (Claude Code)**
- Pricing data: o4-mini ~$1.10/$4.40 per M tokens; Sonnet 4.6 ~$3/$15; Opus 4.6 ~$15/$75
- Positioned them as complementary tools rather than either/or choice
- Cross-linked to existing blog posts: `codex-complete-guide`, `claude-code-seven-programmable-layers`, `first-few-days-with-codex-cli`

**Lessons Learned:**
- Codex CLI's key differentiator is its **mandatory network isolation sandbox** — even in full-auto mode, no outbound network access is possible
- Claude Code's differentiator is the **CLAUDE.md/SKILL.md configuration hierarchy** + MCP ecosystem (150+ integrations)
- Context window gap matters: Claude's 1M tokens vs GPT's 128K-200K gives Claude Code an edge on large codebase comprehension
- Both tools are terminal-native, macOS/Linux only (Windows via WSL)

**Action Items:**
- Ensure this article is saved to `drafts/` or the appropriate content directory in the LoreAI site
- Update `wiki/index.md` if a wiki page on this comparison is created
- Verify cross-referenced articles (`codex-complete-guide`, etc.) exist and links resolve correctly