# Session Capture: loreai

**Date:** 2026-04-20
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Reviewing an article comparing Claude Code vs Codex CLI across architecture, safety, extensibility, pricing, and use cases.

**Key Exchanges:**
- Article covers: local-first (Claude Code) vs cloud-sandboxed (Codex CLI) architecture tradeoffs
- Claude Code extensions: hooks (deterministic shell commands), MCP servers (external integrations), agent teams (parallel sub-agents), CLAUDE.md/skills system
- Codex CLI extensions: primarily VS Code extension GUI; no equivalent to hooks or MCP
- Safety contrast: Codex = architectural isolation (sandbox); Claude Code = permission-based (configurable guardrails)
- Workflow contrast: Codex = async submit-and-review; Claude Code = real-time interactive collaboration

**Decisions Made:**
- Article concludes: tools are **complementary**, not competing — use Claude Code for interactive/context-heavy dev, Codex CLI for batch/sandboxed jobs

**Lessons Learned:**
- Codex CLI free tiers: open-source maintainers + students with .edu emails
- Claude Code pricing: pay-per-token (cheaper for light use; expensive for heavy/long-context sessions vs $200/mo ChatGPT Pro flat rate)
- Claude Code agent teams = parallel sub-agents for large-scale refactoring — key differentiator for big codebases
- Codex CLI cloud mode cannot access local credentials, env vars, or local services — by design

**Action Items:**
- Worth ingesting this article as a raw source → wiki page `claude-code-vs-codex-cli.md` covering the comparison, pricing, and extension models