# Session Capture: loreai

**Date:** 2026-05-01
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Working on a Claude Code vs Codex comparison article for the LoreAI blog.

**Key Exchanges:**
- Article positions Claude Code and Codex as complementary tools representing two philosophies: **interactive co-pilot** (Claude Code) vs **async task worker** (Codex)
- Claude Code strengths: real-time interaction, full environment access, CLAUDE.md extensibility, multi-file refactoring, debugging
- Codex strengths: async execution, cloud sandboxing, GitHub-native workflow, parallel task delegation, bundled ChatGPT pricing

**Decisions Made:**
- Verdict framing: "neither is universally better" — depends on workflow. Many teams use both.
- Clarified that current Codex ≠ original 2021 Codex model (GPT-3 based). Current one is built on o3 reasoning model family.
- Code quality depends on task scoping + project config, not the tool itself.

**Lessons Learned:**
- Claude Code demands attention during execution (tradeoff for power); Codex trades flexibility for delegation
- For large monorepos, Claude Code handles better (local filesystem + sub-agents); Codex clones full repo into sandbox
- No state conflict when using both on same codebase — Claude Code uses local checkout, Codex clones from remote

**Action Items:**
- Article references linked pages that may need to exist: `/blog/claude-code-complete-guide`, `/blog/codex-complete-guide`, `/blog/codex-for-open-source`, `/compare/claude-code-vs-cursor`, `/glossary/agentic-coding`
- Content should be ingested into wiki if not already tracked under AI tooling / builder workflows