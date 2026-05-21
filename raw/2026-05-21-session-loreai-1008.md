# Session Capture: loreai

**Date:** 2026-05-21
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Processing/formatting the daily AI newsletter digest for May 21, 2026.

**Key Exchanges:**
- Newsletter compiled covering major AI developments: OpenAI math proof, Google I/O 2026, Spotify's Claude deployment scale, NVIDIA diffusion LMs

**Decisions Made:**
- Pick of the Day: OpenAI's general-purpose model disproving Erdős's 1946 planar unit distance conjecture — framed as evidence that scaled general reasoning beats domain-specific solvers for scientific breakthroughs

**Lessons Learned:**
- Diffusion language models (NVIDIA Nemotron) generate all tokens simultaneously vs autoregressive left-to-right — architectural ceiling is higher but quality still trails; watch this space
- Structural backpressure (formal verification gates) in coding agent loops outperforms upgrading to smarter models — constraints > intelligence
- Railway seeing agents skip PRs and deploy directly — infrastructure layer rebuilding for agent-native workflows
- Spotify at 4,500 Claude-powered deploys/day — Claude embedded in CI/CD, not just IDE

**Action Items:**
- Wiki pages to create/update: `openai.md` (math conjecture breakthrough), `diffusion-language-models.md` (new concept — Nemotron shipping), `claude-code.md` (v2.1.144 features), `google.md` (I/O 2026, Gemini Omni, 3.5 Flash), `cohere.md` (Command A+ MoE), `qwen.md` (Qwen3.7-Max agent model), `spotify.md` (production Claude adoption data point)
- Track concept: "structural backpressure" as agent engineering pattern
- Track concept: "agents skip PRs, deploy directly" as infrastructure thesis (Railway)
- Track: Kapso MCP = WhatsApp channel for agents (2B MAU distribution channel)