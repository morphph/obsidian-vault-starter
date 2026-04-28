# Session Capture: loreai

**Date:** 2026-04-28
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Processing a detailed comparison article: Codex CLI vs Claude Code for the wiki/drafts pipeline.

**Key Exchanges:**
- Comprehensive feature comparison between OpenAI's Codex CLI (cloud-sandboxed) and Anthropic's Claude Code (local-execution) as of mid-2026
- Codex CLI is now included with ChatGPT Pro/Team/Enterprise subscriptions; Claude Code uses token-based API billing or Max plan ($100-200/month)

**Decisions Made:**
- Architecture difference is the core differentiator: Codex CLI trades capability for safety isolation (cloud sandbox), Claude Code trades safety isolation for capability (local execution)
- Claude Code's programmability stack (CLAUDE.md, SKILL.md, hooks, MCP servers, agent teams) is positioned as a multi-layered platform vs Codex CLI's single-layer AGENTS.md
- Verdict: not mutually exclusive — Codex CLI for well-scoped async tasks, Claude Code for complex context-heavy work

**Lessons Learned:**
- Codex CLI open-sourced its CLI tool; sandbox disables network by default
- Claude Code's hook system provides deterministic guardrails vs Codex's architectural sandboxing — different security models for different risk profiles
- Code quality depends more on configuration (skills, hooks) than which tool you use
- Many teams will use both tools together: Codex for ticket queue (bug fixes, tests, docs), Claude Code for refactoring and local-context work

**Action Items:**
- Ingest this article into wiki — touches pages: [[claude-code]], [[codex-cli]] (may need new page), [[ai-coding-agents]], [[pricing-models]]
- Cross-reference with existing Claude Code wiki content for any updates (agent teams, voice mode, remote control, Ctrl+S stashing are newer features worth tracking)
- Note pricing data point: ChatGPT Pro $200/mo includes Codex; Claude Max $100-200/mo — useful for [[pricing-models]] or similar page