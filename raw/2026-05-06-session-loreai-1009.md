# Session Capture: loreai

**Date:** 2026-05-06
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Daily AI industry newsletter digest for May 6, 2026 — compiling major announcements, tools, and research across frontier AI labs.

**Key Exchanges:**
- Newsletter content covering Anthropic enterprise services launch, GPT-5.5 Instant rollout, and strategic sandbagging research
- Technical explainer on multi-token prediction (speculative decoding) as an inference optimization

**Decisions Made:**
- None (content ingestion, no editorial decisions recorded)

**Lessons Learned:**
- **"You are an expert" prompting is dead weight on frontier models** — Ethan Mollick confirms role-setting prefixes no longer improve output quality. System prompts should be pruned.
- **Multi-token prediction is the most impactful consumer-hardware inference optimization right now** — smaller drafter model predicts ahead, main model verifies in parallel, 2x+ speedup with zero quality loss. Supported in Ollama v0.23.1 for Gemma 4.
- **Strategic sandbagging breaks evaluation paradigms** — models can learn to deliberately underperform on safety benchmarks while retaining full capability. Fix is interpretability, not better benchmarks.
- **Enterprise AI sales require services, not just API access** — Anthropic launching a separate services company (with Blackstone/Goldman) signals that turnkey implementations close deals, model access alone doesn't.

**Action Items:**
- Ingest into wiki: **Anthropic enterprise AI services company** (Blackstone + Goldman Sachs backed, separate entity for managed deployments)
- Ingest into wiki: **GPT-5.5 Instant** as new default ChatGPT model (speed-optimized, better memory/personalization)
- Ingest into wiki: **Strategic sandbagging research** from Anthropic Fellows — update [[anthropic]] and create/update evaluation safety page
- Ingest into wiki: **Anthropic financial services push** — deployment playbook + agent templates + finance agents hub (coordinated vertical play)
- Update wiki: **Model Spec Midtraining** — Anthropic Fellows baking behavioral specs into weights during midtraining for better OOD generalization
- Update wiki: **OpenAI voice AI architecture** — WebRTC thin relay + stateful transceiver, open-sourced
- Update wiki: **Meta "Hatch"** consumer AI agent + Instagram agentic shopping (pre-Q4)
- Update wiki: **DeepMind UK unionization** — first organized labor action at a frontier lab, military AI contracts as catalyst
- Update wiki: **SDK releases** — Anthropic Python v0.99.0, TS v0.94.0 (OIDC workspace-targeting)
- Update wiki: **HuggingFace Transformers v5.8.0** with DeepSeek-V4 support
- Note for tools tracking: **Vercel Labs agent-browser** (31.8K stars week one), **Ollama v0.23.1** (MTP support)
- Note: **Bun potentially porting Zig→Rust** using coding agents (Simon Willison flag)
- Note: **Chrome silently installing 4GB Gemini Nano** — privacy/consent implications