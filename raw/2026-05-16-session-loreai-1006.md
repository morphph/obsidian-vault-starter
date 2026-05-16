# Session Capture: loreai

**Date:** 2026-05-16
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Generated the daily AI newsletter digest JSON for 2026-05-16 (22 items across 6 sections + quick links).

**Key Exchanges:**
- Produced structured newsletter JSON with hero/regular prominence scoring across LAUNCH, TOOL, TECHNIQUE, RESEARCH, INSIGHT, BUILD sections
- Pick of the day: MCP vs SDK token efficiency gap (item 38260)

**Decisions Made:**
- **MoE model literacy angle chosen:** Explained active vs. total parameters using the 30B-A3B Olympiad gold result — framed as essential knowledge for evaluating deployment footprint
- **MCP efficiency gap as pick of the day:** Positioned the 10x token cost (SDK 15k vs MCP 158k) as an industry-level insight about interoperability vs. control flow tradeoffs, not just a cost story

**Lessons Learned:**
- MCP standardization may be optimizing for interoperability at the expense of tight, predictable agent control flow — concrete data now exists (Cloudflare code-mode thesis stress test on monday.com GraphQL API)
- MoE architectures (like 30B-A3B) are making frontier-class reasoning viable on consumer hardware — active parameter count is the metric that matters, not total parameters

**Action Items:**
- Wiki pages that should be updated based on this digest: [[MCP]] (10x token gap data), [[anthropic]] ($200M Gates commitment, legal case study, Claude Code v2.1.143), [[openai]] (Zed integration, Brockman unified-app reorg, Codex mobile), [[xai]] (Grok V9 1.5T), [[coding-agents]] (Claude Code vs Codex CLI comparison, Supabase plugin)
- Model literacy concept (MoE / active parameters) may warrant its own wiki page if not already covered