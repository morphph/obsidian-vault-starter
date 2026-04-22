# Session Capture: loreai

**Date:** 2026-04-22
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Article content comparing Codex CLI vs Claude Code across multiple dimensions — likely ingested or drafted for the LoreAI wiki.

**Key Exchanges:**
- Detailed breakdown of Claude Code vs Codex CLI across 6 dimensions: security/sandboxing, extensibility, model capabilities, IDE integration, pricing, and use cases.

**Decisions Made:**
- Claude Code wins on: extensibility (CLAUDE.md + skills + hooks + MCP + agent teams), IDE/workflow integration (VS Code, JetBrains, web, desktop, mobile remote), and git automation depth.
- Codex CLI wins on: hard network isolation/sandbox security, open-source transparency, cost-efficiency (o4-mini pricing, no platform fee).
- Ties on: model capability (different strengths), pricing (both usage-based with subscription options).

**Lessons Learned:**
- Codex CLI = "sandbox-first, transparent, auditable" philosophy — better for sensitive/compliance codebases.
- Claude Code = "programmable AI engineering platform" philosophy — better for teams needing encoded standards and complex workflows.
- CLAUDE.md + skills + hooks combo is a key differentiator: deterministic behavior without relying on model judgment.
- Both tools can coexist in same project (CLAUDE.md for Claude Code sessions, AGENTS.md for Codex sessions).
- Claude Code extended context window = practical advantage for large codebases; Codex CLI agent lacks multi-agent coordination for broad refactoring.
- Neither tool has native Windows support — both require WSL on Windows.

**Action Items:**
- Consider ingesting this comparison as a wiki page (e.g., `codex-cli-vs-claude-code.md`) under Builder Tools category.
- Cross-reference with existing Claude Code and MCP wiki pages if they exist.