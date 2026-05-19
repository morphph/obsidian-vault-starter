# Session Capture: loreai

**Date:** 2026-05-19
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Drafting/reviewing a comparison article: Claude Code vs OpenAI Codex (2026 products)

**Key Exchanges:**
- Full comparison article produced covering architecture, interaction model, extensibility, pricing, and use-case recommendations for Claude Code vs OpenAI Codex

**Decisions Made:**
- Framed as "local agent vs cloud sandbox" — not "better vs worse." Both tools are genuinely agentic, not autocomplete copilots
- Explicitly clarified 2026 Codex ≠ retired 2021 Codex API (FAQ section addresses this)
- Positioned the tools as complementary, not mutually exclusive — "use Claude Code for complex interactive work, Codex for batching routine tasks"

**Lessons Learned:**
- Codex pricing: included with ChatGPT Pro ($200/mo) and Plus ($20/mo limited); also free for open-source maintainers and students ($100 credits)
- Claude Code pricing: usage-based API or Max plan ($100–200/mo); no free tier
- Key architectural distinction: Claude Code = local execution (code stays on machine); Codex = cloud sandbox (code transits to OpenAI infra)
- Codex has a VS Code extension now (not just ChatGPT web UI)
- Claude Code's extensibility stack (CLAUDE.md → SKILL.md → Hooks → MCP) is significantly deeper than Codex's setup-script model

**Action Items:**
- Article references several internal links that need to exist: `/compare/claude-code-vs-cursor`, `/blog/codex-vscode`, `/blog/codex-for-students`, `/blog/codex-for-open-source`, `/blog/codex-complete-guide` — verify these pages are published or queued
- Could spin off wiki pages: `wiki/openai-codex.md`, `wiki/claude-code-vs-codex.md`, `wiki/agentic-coding-tools.md`