# Session Capture: loreai

**Date:** 2026-04-27
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Reviewing a long-form comparison article about Claude Code vs OpenAI Codex for potential ingestion into the wiki.

**Key Exchanges:**
- No interactive exchange — this was a single-turn context flush of article content.

**Decisions Made:**
- (None recorded — article was presented as context, not discussed)

**Lessons Learned:**
- Claude Code vs Codex key differentiator: **local/interactive vs cloud/async**
  - Claude Code: real-time conversational, full filesystem access, CLAUDE.md + SKILL.md + hooks, MCP extensibility, agent teams
  - Codex: async delegation, sandboxed microVM (no network by default), GitHub-integrated, PR-delivery model
- Codex's "current" product (2024+) uses o3/o4-mini and is unrelated to the 2021 Codex model that powered early Copilot — name reuse causes confusion
- Codex has free programs: open-source maintainers get free access; students get $100 credits — Claude Code has no equivalent
- Claude Code billing: usage-based API or Claude Max subscription; Codex: bundled into ChatGPT Pro/Plus/Team tiers
- For large monorepos: Claude Code wins (direct filesystem, no clone latency, agent teams for parallel work)
- Security posture: Codex = default isolation; Claude Code = configurable control (opt-in guardrails via hooks + permissions)

**Action Items:**
- Consider ingesting this article as a raw source → wiki page `claude-code-vs-codex.md` under the "Builder tools and workflows" category
- Cross-reference with existing pages: [[Claude Code]], [[Codex]], [[MCP]], [[hooks]], [[agent teams]] if they exist