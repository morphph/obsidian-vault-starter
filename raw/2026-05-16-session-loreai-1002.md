# Session Capture: loreai

**Date:** 2026-05-16
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Curating and scoring the daily AI industry news digest (2026-05-16), selecting top items across Anthropic, OpenAI, open-source, and industry commentary.

**Key Exchanges:**
- Scored ~22 items across categories (INSIGHT, LAUNCH, TOOL, TECHNIQUE, RESEARCH, BUILD)
- Top-scored items: OpenAI Zed integration (93), Gates Foundation $200M (92), HuggingFace 30B-A3B reasoning model (91), OpenAI unified-app reorg (89)

**Decisions Made:**
- Selected a broad mix covering Anthropic (legal vertical, Claude Code v2.1.143, Mythos), OpenAI (Codex mobile, Zed, reorg), open-source (30B-A3B, Microsoft Lens), and critical commentary
- Included the MCP vs SDK efficiency data (10x token gap) as a high-value TECHNIQUE item — hard numbers that inform agent architecture

**Lessons Learned:**
- **MCP vs code-first agents:** SDK approach used 1 step/15k tokens vs MCP's 4 steps/158k tokens on same GraphQL API — architecture-level insight for agent builders
- **LeCun's framework:** LLMs excel where language IS the reasoning substrate (math, code), fail where language is just a description layer — useful heuristic for deployment decisions
- **AI healthcare paradox:** Abridge claims 100M visits/10-20hr savings while Ontario auditors find routine factual errors — both can be true, verification layers are non-negotiable
- **Throwaway-code economics:** Simon Willison notes porting apps between native and React Native with agents is now so cheap it reshapes build-vs-rewrite decisions
- **"AI psychosis"** (Mitchell Hashimoto) — companies making irrational decisions based on AI hype, resonated widely (612 likes)

**Action Items:**
- Watch next week: GPT 5.6 vs Gemini 3.2 announcements expected — frontier model release cadence accelerating
- Track Grok V9 benchmarks (1.5T params, 3x V8, pre-Cursor fine-tuning)
- OpenAI unified-app reorg under Brockman (Fidji Simo on leave) — watch for ChatGPT UI consolidation
- Update Claude Code to v2.1.143 — plugin dependency enforcement and worktree background isolation are relevant to this wiki's multi-agent workflows
- Supabase ships official agent plugin (MCP + skills for Codex, Claude Code, Cursor, Gemini CLI) — database-as-a-service going agent-native