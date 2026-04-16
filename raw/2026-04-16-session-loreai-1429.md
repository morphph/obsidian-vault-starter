# Session Capture: loreai

**Date:** 2026-04-16
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Article content comparing Codex CLI vs Claude Code across security, pricing, multi-agent capability, and use cases — likely a draft or raw source for LoreAI blog.

**Key Exchanges:**
- No back-and-forth — this is a document review/flush request, not a dialogue.

**Decisions Made:**
- None recorded in this session.

**Lessons Learned:**
- **Codex CLI differentiator:** Network-disabled sandbox is architectural default, not a toggle — strongest structural security of any major coding agent. Best for regulated industries or sensitive codebases.
- **Claude Code differentiator:** Multi-agent orchestration (parallel sub-agents) is unique among terminal-based coding agents. Agent teams + skills + hooks + MCP = composable extension platform.
- **Pricing rule of thumb:** Codex CLI is effectively free if you already pay for ChatGPT. Claude Code costs scale with heavy API usage.
- **Context file coexistence:** `AGENTS.md` (Codex) and `CLAUDE.md` (Claude Code) can coexist in the same repo without conflict — teams can run both tools on the same project.
- **Memory model contrast:** Codex CLI = clean session each time (reproducible, no drift). Claude Code = persistent cross-session memory (lower friction for ongoing projects).
- **VS Code integration:** Codex CLI has a VS Code extension for developers who prefer staying in-editor.

**Action Items:**
- Consider ingesting this article into the wiki as a comparison page (e.g., `codex-cli-vs-claude-code.md`) once the draft is finalized.