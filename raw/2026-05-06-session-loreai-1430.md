# Session Capture: loreai

**Date:** 2026-05-06
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Drafting/reviewing a comparison article: Codex CLI vs Claude Code for the LoreAI blog.

**Key Exchanges:**
- Comprehensive feature-by-feature comparison of OpenAI's Codex CLI vs Anthropic's Claude Code as terminal coding agents
- Analysis covers: security/sandboxing, extensibility, model flexibility, context/memory, workflow integration, pricing, and use-case recommendations

**Decisions Made:**
- Framing: Codex CLI wins on security/transparency (sandbox-first, open source); Claude Code wins on extensibility/depth (CLAUDE.md + hooks + MCP + memory)
- Hybrid approach presented as valid — use both for different scenarios
- Cost tip included: use cheap models (o4-mini, Haiku) for routine tasks, reserve expensive models (o3, Opus) for complex reasoning
- Article targets builders choosing between tools, not a "winner" verdict

**Lessons Learned:**
- Codex CLI's sandbox blocks network by default — breaks workflows that need to hit local services (docker compose, dev servers)
- Claude Code's extensibility is configure-not-code (CLAUDE.md, SKILL.md, hooks, MCP); Codex CLI's extensibility is fork-and-build
- Persistent memory is a compounding advantage for long-running projects — conventions explained once carry across sessions
- Container sandboxing on macOS uses Apple Seatbelt (not Docker)

**Action Items:**
- Article references internal links (`/blog/claude-code-extension-stack-skills-hooks-agents-mcp`, `/blog/claude-code-memory`, `/blog/claude-code-complete-guide`, `/blog/codex-vscode`, `/faq/using-codex`) — ensure these pages exist or are created
- Article ends with `/subscribe` CTA — confirm that route works on loreai.dev
- Wiki pages to consider creating/updating: `codex-cli.md`, `claude-code.md`, `ai-coding-agents-comparison.md`