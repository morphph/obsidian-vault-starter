# Session Capture: loreai

**Date:** 2026-05-20
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Drafting/reviewing a comparison article on OpenAI Codex vs ChatGPT for coding workflows (likely for LoreAI blog).

**Key Exchanges:**
- Comprehensive breakdown of Codex (agentic, async, cloud-sandboxed) vs ChatGPT (conversational, real-time, general-purpose) for developer use cases
- Pricing tiers mapped to feature access: Free → Plus ($20) → Pro ($200, includes Codex) → Team

**Decisions Made:**
- Codex positioned as a **coding agent** (delegate work), ChatGPT as a **coding assistant** (collaborate on work) — this framing drives the entire article
- Recommendation ladder: start with ChatGPT Plus, upgrade to Pro+Codex when multi-file delegation becomes frequent
- For teams: Codex on Team plans is the real value play (parallel execution, PR output, sandboxed security)

**Lessons Learned:**
- Codex runs on `codex-1` (fine-tuned for agentic SWE), distinct from GPT-4o/o3/o4-mini used by ChatGPT
- Codex sandboxes are firewalled — no network access during execution, can't download packages outside lock file — important security differentiator for proprietary codebases
- Codex's parallel task execution (queue multiple independent tasks, review batch PRs) is an underappreciated advantage over serial ChatGPT conversations
- Codex weak spots: exploratory work, unclear debugging, tasks needing external API access
- ChatGPT has no official IDE extension (VS Code, JetBrains) — significant integration gap vs Codex's VS Code extension
- Closest competitor mapping: Codex ↔ Claude Code (agentic), ChatGPT ↔ Claude/Gemini (conversational)

**Action Items:**
- Wiki pages to create/update: Codex pricing, codex-1 model, Codex vs Claude Code comparison
- Cross-reference with existing wiki content on [[agentic-coding]], agent harnesses, coding agents reshaping EPD
- Article references internal links (`/blog/codex-vscode`, `/blog/agent-harnesses-2026`, `/blog/coding-agents-reshaping-epd`) — ensure those pages exist or are planned