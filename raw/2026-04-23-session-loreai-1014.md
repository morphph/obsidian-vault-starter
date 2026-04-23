# Session Capture: loreai

**Date:** 2026-04-23
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Generated a Chinese-language AI daily newsletter (draft) covering major developments from April 23, 2026.

**Key Exchanges:**
- Newsletter covers: Google TPU v8 split (8T training / 8I inference), Claude Code `/ultrareview` multi-agent code review, Qwen3.6-27B surpassing Opus 4.5 on LiveBench, Shopify's unlimited Opus 4.6 budget for engineers, OpenAI "DeployCo" $10B enterprise JV, Anthropic prompt caching adoption stat (79% not using it), VS Code Copilot opening to custom models/API keys

**Decisions Made:**
- Format: Sections by category (发布动态 / 开发者工具 / 技术实战 / 研究前沿 / 行业洞察 / 值得一试 / 模型小课堂 / 快讯 / 今日精选)
- Lead story: Google TPU v8 chip split as hardware bet on Agent era
- 今日精选 anchor: Shopify unlimited token budget as strongest signal for agentic coding era

**Lessons Learned:**
- Qwen3.6-27B (dense, 27B params) benchmarks above Opus 4.5 on LiveBench — open-source coding ceiling keeps rising
- 79% of Claude API users not using prompt caching; top integrators hit 92–96% cache hit rate — actionable cost saving
- Google TPU 8T/8I split signals industry-level acknowledgment that training and inference are fundamentally different workloads
- Shopify: unlimited AI compute per engineer + 3 internal Agent tools (Tangle / Tangent / SimGym) = clearest enterprise agentic-coding case study to date

**Action Items:**
- Consider ingesting Shopify CTO Latent Space episode as raw source for deeper wiki coverage
- Consider wiki page update for Google TPU v8 / inference-optimized silicon trend
- Prompt caching stat worth adding to Anthropic or Claude API wiki page