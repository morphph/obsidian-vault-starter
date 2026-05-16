# Session Capture: loreai

**Date:** 2026-05-16
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Generated the daily AI newsletter digest for 2026-05-16.

**Key Exchanges:**
- Newsletter produced covering: MoE efficiency breakthrough, MCP token cost benchmarking, OpenAI org restructure, Anthropic philanthropy, and tool updates

**Decisions Made:**
- Pick of the Day: MCP vs code-first 10x token gap — chosen because it provides hard data on a tradeoff the industry has been debating abstractly
- MoE active parameters explanation chosen as Model Literacy topic — timely tie-in to the 30B-A3B headline

**Lessons Learned:**
- **MCP vs SDK cost is now quantified**: MCP used 158k tokens / 4 steps vs SDK's 15k tokens / 1 step on Monday.com GraphQL API. Practical guidance: MCP for long-tail integrations, tight SDK bindings for high-frequency APIs.
- **"Total params vs active params" is the new evaluation framework** for MoE models — 30B knowledge capacity at 3B inference cost enables consumer-hardware reasoning.
- **Simon Willison's "port and port back" pattern**: coding agents make throwaway rewrites economically rational as a testing strategy.
- **LeCun's heuristic**: LLMs strongest where language IS the reasoning substrate (math, code, logic), weakest where language merely describes processes in other media (physical, spatial).

**Action Items:**
- Wiki pages to consider updating: [[anthropic]] ($200M Gates Foundation commitment, legal industry case study), [[claude-code]] (v2.1.143 — plugin deps, worktree isolation), [[openai]] (Zed integration, Codex mobile, org restructure under Brockman), [[mcp]] (10x token cost benchmark data)
- Track new entities: Grok V9 (1.5T params), Microsoft Lens (3.8B T2I), Mythos Preview (first to solve both UK AISI cyber ranges), Supabase agent plugin
- Next week preview: GPT 5.6 vs Gemini 3.2 announcements expected