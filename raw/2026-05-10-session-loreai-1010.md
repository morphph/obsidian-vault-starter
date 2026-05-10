# Session Capture: loreai

**Date:** 2026-05-10
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Curated the daily AI newsletter digest (May 10, 2026) — 23 items across LAUNCH, RESEARCH, INSIGHT, BUILD, TOOL, TECHNIQUE sections.

**Key Exchanges:**
- Generated full newsletter JSON with hero picks, angles, and model literacy explainer on weight quantization

**Decisions Made:**
- **Pick of the Day:** Anthropic's alignment research (teaching Claude to reason about *why* rules exist, not memorize them) — rationale: alignment-as-capability is a paradigm shift worth highlighting
- **Model Literacy topic:** Weight quantization — tied to antirez's ds4 running DeepSeek v4 Flash at 2-bit on a Mac
- **Hero selections:** Baidu Ernie-5.1 (LAUNCH), Anthropic alignment research (RESEARCH), Altman crowdsourcing next model priorities (INSIGHT), antirez ds4 local inference (BUILD)

**Lessons Learned:**
- Claude Code consumes 14% of tokens on CLAUDE.md and 13% re-reading conversation history — practical optimization targets for heavy users
- Factory AI's 16-day multi-agent run succeeded because validation contracts were written *before* implementation
- WebRTC is a poor transport choice for OpenAI's Realtime API voice agents — worth noting for anyone building on Realtime-2

**Action Items:**
- Track Baidu Ernie-5.1 benchmark claims for independent verification
- GitHub deprecating Grok Code Fast 1 from Copilot — **deadline May 15, 2026** (5 days away), migrate to GPT-5 mini or Claude Haiku 4.5
- Claude Certified Architect credential launched — potential wiki page on AI engineering credentialing
- Gemini 3.1 Flash Lite now GA — update model comparison pages if they exist
- Mollick's guild theory (professions with guilds get AI displacement protection; tech workers don't) — worth a wiki note under labor/displacement themes