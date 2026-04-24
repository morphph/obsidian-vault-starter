# Session Capture: loreai

**Date:** 2026-04-24
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Curating daily AI newsletter for April 24, 2026 — selecting top stories from ranked candidates.

**Key Exchanges:**
- Reviewed recent newsletters (Apr 21–23) to avoid re-headlining: Claude Code /ultrareview, Shopify Opus budgets, ChatGPT Images 2.0, AI vs economist agents, Claude Cowork live artifacts, LeCun dead-end thesis
- Identified today's top new stories: GPT-5.5 launch (score 98), Claude Code quality post-mortem (96), Claude connectors for everyday life (95), Claude Managed Agents memory (94), Decoupled DiLoCo (92), Gemini Embedding 2 GA (91)

**Decisions Made:**
- GPT-5.5 selected as PICK — OpenAI's biggest model drop since GPT-5, purpose-built for agentic coding/computer use/scientific research, 35K likes signal
- Claude Code quality post-mortem selected — transparent Anthropic post-mortem on benchmark regression caused by infrastructure config; all users get rate limits reset; update to v2.1.116+
- Claude connectors for everyday life selected — Tripadvisor, Booking.com, Spotify, Instacart, TurboTax, etc.; Claude pivoting from work tool to personal assistant
- Claude Managed Agents memory selected — persistent memory in public beta; SDKs (Python v0.97.0, TS v0.91.0) already updated

**Lessons Learned:**
- Claude Code v2.1.117+ stopped calling Grep/Glob repeatedly — behavioral improvement from community feedback
- Claude Code v2.1.119 adds persistent /config, prUrlTemplate, agent worktrees — rapid iteration post-post-mortem
- Abacus AI first to move production workloads to open-source model (Kimi 2.6) — validates open-source cost thesis
- Gemini Embedding 2 GA: first natively multimodal embedding model (text + image + video in single space) — important for RAG pipelines
- llama.cpp CVE-2026-21869 (CVSS 8.8) patched in b8908 — heap-buffer-overflow from negative n_discard in server mode

**Action Items:**
- Update Claude Code to v2.1.119
- Update Anthropic SDK to Python v0.97.0 / TS v0.91.0 for agent memory support
- Update llama.cpp to b8908 if running as server