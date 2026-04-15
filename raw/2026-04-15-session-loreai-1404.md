# Session Capture: loreai

**Date:** 2026-04-15
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Created a Chinese-language compare article: Claude Code vs OpenAI Codex (`drafts/claude-code-vs-codex.md`)

**Key Exchanges:**
- Draft compare article produced covering architecture, pricing, customizability, and use cases for both tools

**Decisions Made:**
- Framing: positioned the two tools as fundamentally different paradigms — Claude Code as synchronous/local/real-time, Codex as asynchronous/cloud/batch — rather than a direct feature-for-feature race
- Claude Code wins on: customizability (Skills/Hooks/MCP), cost entry point ($20 vs $200/mo), local env access
- Codex wins on: async task distribution, GitHub-native PR workflow, team-scale parallelism
- Conclusion: tools are complementary, not mutually exclusive; choice depends on work style

**Lessons Learned:**
- The key differentiator is **interaction paradigm** (real-time vs async), not raw capability — this framing is useful for future compare articles involving agentic tools
- Codex's $200/mo entry point is a significant adoption barrier vs Claude Code's $20 tier; worth noting in any pricing-sensitive content

**Action Items:**
- None explicitly stated; article is complete and ready for human polish before publication