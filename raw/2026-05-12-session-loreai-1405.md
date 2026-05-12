# Session Capture: loreai

**Date:** 2026-05-12
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Drafting/reviewing a Claude Code vs OpenAI Codex comparison article for the LoreAI blog.

**Key Exchanges:**
- Comprehensive feature comparison covering: execution model (local vs cloud sandbox), context/config systems (CLAUDE.md stack vs AGENTS.md), coding capabilities, security, pricing, IDE integration

**Decisions Made:**
- **Verdict positioning:** Claude Code is the better tool for most professional workflows; Codex wins specifically for batch processing of well-defined tasks and teams already in OpenAI ecosystem
- **Framing axis:** Interactivity-vs-parallelism spectrum — not a simple "which is better" but different points on a design tradeoff curve
- **Recommendation:** Start with Claude Code for core workflow, consider Codex as complementary for parallel well-scoped tasks
- **Pricing angle:** Claude Code offers better value at $20-$100/month tier for coding-only use; Codex bundled value if team already pays for ChatGPT Pro/Enterprise

**Lessons Learned:**
- Claude Code's extension stack (skills, hooks, MCP, agent teams) compounds over time — this is a key differentiator vs Codex's simpler AGENTS.md
- Codex's sandbox (no internet by default) is a genuine security advantage against supply chain attacks, even though Claude Code's local-first model is better for data privacy — these are different threat models
- Codex struggles with ambiguous/exploratory tasks because it can't ask clarifying questions mid-task
- Decision rules throughout the article follow a consistent pattern: map the choice to the user's workflow type, not abstract feature lists

**Action Items:**
- Article references `/compare/claude-code-vs-cursor` — ensure that comparison page exists or is planned
- Article references `/blog/codex-for-open-source` and `/blog/codex-for-students` — verify these are published
- Consider ingesting this article into wiki as a source on competitive landscape (Claude Code vs alternatives)