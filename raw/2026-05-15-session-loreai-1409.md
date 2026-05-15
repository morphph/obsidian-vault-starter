# Session Capture: loreai

**Date:** 2026-05-15
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Generated a Chinese-language comparison article draft: "Claude Code vs Codex" for the LoreAI blog.

**Key Exchanges:**
- Produced a full `/zh/compare/` article comparing Claude Code (Anthropic) and OpenAI Codex across architecture, workflow, extensibility, pricing, and use-case fit

**Decisions Made:**
- Framed the core distinction as **local-first terminal Agent (Claude Code) vs cloud-first sandbox Agent (Codex)** — this is the organizing thesis
- Positioned them as complementary, not zero-sum ("两者并不互斥")
- Pricing nuance: Claude Code = per-token API billing or Pro/Max subscription; Codex = bundled in ChatGPT Pro ($200/mo) / Team / Enterprise
- Linked to existing blog posts: `codex-complete-guide`, `claude-code-extension-stack-skills-hooks-agents-mcp`, `claude-code-enterprise-engineering-ramp-shopify-spotify`

**Lessons Learned:**
- Codex's no-internet sandbox is a deliberate security trade-off that limits tasks needing network access (API calls, doc lookups, dependency downloads at runtime)
- Claude Code's 7-layer programmable architecture (CLAUDE.md → Skills → Hooks → MCP → Agent Teams → Slash Commands → Headless API) is a key differentiator for enterprise adoption
- Feedback loop length is a useful frame for comparing sync-interactive vs async-delegation workflows

**Action Items:**
- Article references `related_compare: [claude-code-vs-cursor]` — that comparison page should exist or be created
- Verify `related_glossary` entries (`agentic-coding`, `agent-sdk`) and `related_topics` (`claude-code`, `codex`) pages exist in the site
- Article needs editorial review for accuracy on Codex pricing (ChatGPT Pro is listed as $200/mo — confirm current pricing)