# Session Capture: loreai

**Date:** 2026-05-18
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Daily AI intelligence digest curation (2026-05-18) — 20 scored items from Twitter, HN, RSS, GitHub.

**Key Exchanges:**
- Curated feed output with scores 70–95 across categories: INSIGHT, BUILD, RESEARCH, TOOL, LAUNCH, TECHNIQUE

**Decisions Made:**
- None explicit — this appears to be a raw digest output, not yet ingested into wiki

**Lessons Learned:**
- Anthropic overtakes OpenAI in enterprise spend for the first time (Ramp card data) — score 95, strongest signal of the batch
- LeCun puts 12–18 month concrete timeline on hierarchical world models at Meta FAIR
- "AI is technology not a product" (Gruber) + "AI won't make processes faster" (HN viral) — two converging contrarian framings gaining traction
- Apple Silicon local inference is MORE expensive per token than cloud APIs when hardware amortization included — challenges "local is free" narrative
- ArXiv enforcing 1-year bans for fully AI-generated papers — first major academic enforcement mechanism
- `claude-code-setup` plugin dropped by Anthropic — auto-configures hooks, skills, MCP servers
- Multi-model agent routing (Opus for UI, GPT-5.5 for logic, Gemini for vision, DeepSeek for cost) becoming default multi-agent architecture pattern
- Coding agent UX is commoditizing: DeepSeek-TUI (30K+ stars) shows the pattern is model-agnostic now
- Clara Health $660M raise — one of largest AI healthcare rounds, AI-first clinical care with prescribing capability

**Action Items:**
- Ingest this digest into wiki (potential pages to update: [[anthropic]], [[open-models]], [[coding-agents]], [[ai-healthcare]])
- Track Ramp enterprise data as ongoing signal for Anthropic market position
- Monitor Meta FAIR world model papers through 2027 per LeCun timeline
- Evaluate `claude-code-setup` plugin for this repo's workflow