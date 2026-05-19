# Session Capture: loreai

**Date:** 2026-05-19
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Drafting a Chinese comparison article: Codex CLI vs Claude Code (terminal coding agents).

**Key Exchanges:**
- Generated a full `/zh/compare/codex-cli-vs-claude-code` article with TL;DR, overviews, feature table, security model analysis, extensibility comparison, use-case recommendations, and FAQ

**Decisions Made:**
- **Core framing:** Not "different versions of the same tool" but "two different engineering philosophies" — Codex CLI prioritizes safety/transparency, Claude Code prioritizes engineering efficiency/programmability
- **Security as the key differentiator:** Codex CLI = architectural sandbox isolation (defense-by-design); Claude Code = approval-based security (flexibility-by-design)
- **Extensibility winner:** Claude Code's 4-layer system (CLAUDE.md → SKILL.md → Hooks → MCP) vs Codex CLI's AGENTS.md only
- **Not mutually exclusive:** Positioned both tools as complementary — Codex CLI for exploration/security-sensitive work, Claude Code for complex production workflows

**Lessons Learned:**
- Codex CLI's sandbox persists even in full-auto mode — it's architecture-level, not a config toggle
- Codex CLI network isolation means git push and external API calls require explicit sandbox policy changes
- Claude Code's Agent Teams (parallel sub-agents) is a meaningful differentiator for large refactoring tasks
- codex-1 is RL-optimized specifically for code; Claude models are stronger at complex context and multi-step reasoning

**Action Items:**
- Article references several internal links that must exist: `/zh/blog/codex-complete-guide`, `/zh/blog/claude-code-extension-stack-skills-hooks-agents-mcp`, `/zh/blog/first-few-days-with-codex-cli`, `/zh/faq/is-codex-cli-safe-to-use`, `/zh/blog/codex-for-students`, `/zh/blog/codex-for-open-source`, `/zh/blog/claude-code-seven-programmable-layers`, `/zh/blog/claude-code-memory`, `/zh/blog/codex-vscode` — verify all exist or create them
- Commit and push the comparison article to the repo