# Session Capture: loreai

**Date:** 2026-04-23
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Reviewing an AI news digest (dated 2026-04-23) for knowledge worth capturing in the wiki.

**Key Exchanges:**
- Newsletter digest covers ~15 AI news items across tools, research, infrastructure, and industry moves

**Decisions Made:**
- N/A (no interactive decisions in this context)

**Lessons Learned:**
- **Prompt caching gap**: 79% of Claude API orgs leave caching off; top integrations hit 92–96% cache rates. Anthropic now ships an adoption dashboard. Fastest cost-reduction lever for any team using repeated system prompts.
- **TPU bifurcation**: Google TPU v8 splits into 8T (training) and 8I (inference) — training is throughput-bound, inference is latency-bound. Agentic workloads (many sequential calls per session) make inference chip economics the key cost variable.
- **Shopify all-in on agentic coding**: Every engineer gets unlimited Opus 4.6 budget. Three internal tools: Tangle (code gen), Tangent (exploration), SimGym (simulation). Strongest public signal that agentic coding has crossed from experiment to infrastructure at a major tech company.
- **Open-weight catching up**: Qwen3.6-27B reportedly beats Opus 4.5 on LiveBench at 16GB quantized — runs on consumer hardware. Price-performance ratio increasingly challenges frontier API costs.

**Action Items:**
- Consider ingesting Shopify CTO Latent Space podcast episode into wiki (strong builder signal)
- Consider creating/updating wiki pages for: `prompt-caching.md`, `ollama.md`, `claude-code.md` (v2.1.117 features: forked subagents, MCP in agent sessions, persistent model selection)
- Claude Code v2.1.117 notable: forked subagents via env flag, MCP servers in agent sessions, persistent model selection