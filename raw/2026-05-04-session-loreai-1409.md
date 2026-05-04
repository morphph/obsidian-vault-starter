# Session Capture: loreai

**Date:** 2026-05-04
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Drafted a Chinese comparison article "Claude Code vs Codex" for the LoreAI blog.

**Key Exchanges:**
- Created a full-length comparison piece covering architecture philosophy (local terminal agent vs cloud sandbox), developer experience (interactive pairing vs async delegation), context/customization capabilities, and use-case recommendations for each tool.

**Decisions Made:**
- Framing: Not "same tool, different versions" but "two routes for AI programming" — interactive collaboration vs async delegation
- Balanced stance: Neither tool declared winner overall; positioned as complementary (Claude Code for deep interactive work, Codex for parallelizable independent tasks)
- Claude Code advantages highlighted: context system (CLAUDE.md/SKILL.md), full shell access, Hooks/MCP extensibility, multi-agent review
- Codex advantages highlighted: native multi-task parallelism, sandbox security isolation, GUI-friendly, free tiers for OSS/students

**Lessons Learned:**
- Codex (codex-1) is an RL-optimized o3 variant running in network-isolated cloud containers — dependencies must be pre-installed via setup script
- Codex customization is lighter than Claude Code: only README + AGENTS.md, no equivalent to Hooks or MCP
- Key architectural tradeoff: Codex sacrifices environment flexibility for safety + parallelism; Claude Code sacrifices isolation for depth of local integration

**Action Items:**
- Article references related posts that should exist: `codex-complete-guide`, `claude-code-agent-teams`, `claude-code-vs-cursor`, `codex-for-open-source`, `codex-for-students`, `codex-vscode` — verify these are published or queued
- Frontmatter links to glossary entries `agentic-coding` and `agent-sdk` — confirm they exist in wiki