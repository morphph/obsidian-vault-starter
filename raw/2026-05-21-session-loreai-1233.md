# Session Capture: loreai

**Date:** 2026-05-21
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Signal triage batch (2026-05-20/21) — 20 signals from Twitter, GitHub trending, and Anthropic blog routed to LoreAI content pages.

**Key Exchanges:**
- Routed 20 incoming signals; 9 actionable, 11 ignored (duplicates, vague, or promotional)
- Three signals flagged as `refresh_and_create` (highest priority): claude-code-setup official plugin (signal 7), HTML-as-deliverable blog post (signal 4), Claude Code at scale best practices (signal 2)
- Six signals flagged as `refresh` only: Learning mode adoption (1), narrator-ai skill (6), Venice MCP 31-tool server (8), Weft macOS workbench (14), akii SEO/AEO plugin (16), Readwise MCP server (18), creating-claude-md skill (20)

**Decisions Made:**
- **claude-code-setup official plugin** is the highest-impact signal this cycle — an Anthropic-published plugin that auto-configures MCP, hooks, subagents, and skills from project structure. Routed to plugin FAQ, MCP blog, and subagents blog; new dedicated FAQ page suggested.
- **"Unreasonable effectiveness of HTML"** (official Anthropic blog) reframes Claude Code as a non-dev deliverable tool. Routed to non-technical use case pages; new tutorial suggested for HTML-as-deliverable workflow.
- **Claude Code vs Codex framing shift**: migration isn't about CLAUDE.md → AGENTS.md; hooks, MCP, plugins, permissions are the real ecosystem lock-in. New migration guide blog suggested.
- **MCP ecosystem expanding**: Venice (31 multimodal tools) and Readwise both launched official MCP servers — signals MCP adoption beyond dev-only tooling.

**Lessons Learned:**
- Duplicate detection worked well this cycle (Venice × 2, training course × 3, claude-code-setup × 2) — dedup before routing saves effort
- Signals without enough context (signal 3: "available in latest CC Desktop update" with no detail) are unroutable — capture pipeline should require minimum summary length
- The "ecosystem lock-in" framing (signal 15) is a strong narrative angle: Claude Code's moat is hooks + MCP + plugins, not the model or CLAUDE.md

**Action Items:**
- **Create new pages:** (1) FAQ for claude-code-setup plugin, (2) tutorial on HTML-as-deliverable workflow, (3) blog on Claude Code best practices at scale, (4) blog on migrating Claude Code → Codex ecosystem
- **Refresh existing pages:** claude-code-output-styles FAQ (Learning mode), claude-code-skills FAQ (narrator-ai + creating-claude-md examples), claude-code-mcp-setup blog (Venice + Readwise), claude-code-pricing FAQ (Weft token monitoring), plugin-json-manifest FAQ (akii SEO plugin), claude-code-is-not-a-coding-tool blog (akii + HTML use cases), claude-code-vs-codex compare page (ecosystem lock-in framing)
- Investigate capture pipeline: enforce minimum summary length to avoid unroutable signals like signal 3