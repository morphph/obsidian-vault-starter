# Session Capture: loreai

**Date:** 2026-05-18
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Drafting/reviewing a Claude Code vs OpenAI Codex comparison article for LoreAI blog.

**Key Exchanges:**
- Comprehensive feature comparison covering: interaction model (interactive vs async), context systems (CLAUDE.md/SKILL.md vs per-task prompts), security models (local permission-based vs sandboxed zero-trust), pricing (per-token vs subscription), and IDE integration
- Article positions the tools as complementary, not competing — different workflows for different task types

**Decisions Made:**
- **Framing**: Claude Code = interactive pair-programmer; Codex = async task delegator. Not "which is better" but "which workflow fits the task"
- **Recommendation pattern**: Claude Code for ambiguous/complex tasks, local env access, strong conventions; Codex for well-specified batch tasks, security isolation, predictable costs
- **Verdict**: Many teams should use both — Claude Code for interactive sessions, Codex for parallelized well-defined tasks
- Internal links point to `/blog/claude-code-complete-guide`, `/blog/codex-complete-guide`, `/compare/claude-code-vs-cursor`, `/blog/claude-code-hooks-mastery`, `/blog/codex-vscode`, `/blog/codex-for-students`, `/blog/codex-for-open-source`

**Lessons Learned:**
- Codex clones full repo into sandbox; Claude Code explores incrementally — impacts how each handles monorepos
- Codex's network-disabled sandbox is easier to pass enterprise security review but limits capability (no package install, no API calls without config)
- Claude Code's CLAUDE.md + SKILL.md = persistent, version-controlled project context; Codex has no equivalent reusable instruction layer
- Cost math: high-volume teams favor Codex subscription; variable-usage teams favor Claude Code pay-per-token
- As of mid-2026: Codex has VS Code extension and API access beyond the ChatGPT web UI; Claude Code has terminal, VS Code, JetBrains, web, and desktop apps

**Action Items:**
- Article references several internal blog posts that need to exist: codex-complete-guide, codex-vscode, codex-for-students, codex-for-open-source, claude-code-hooks-mastery — verify these are published or queued
- Pricing section notes "details change frequently" — flag for periodic review
- Consider ingesting this as a raw source and creating/updating wiki pages for `claude-code.md`, `openai-codex.md`, and possibly `ai-coding-agents-comparison.md`