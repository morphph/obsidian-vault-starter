# Session Capture: loreai

**Date:** 2026-05-01
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Curating items for the daily AI newsletter/digest (2026-05-01 edition).

**Key Exchanges:**
- Selected 23 items across launches, insights, research, and techniques from multiple sources (Claude Blog, Twitter, HN, RSS, HuggingFace, GitHub)

**Decisions Made:**
- **Claude Security** (public beta) selected as top story — code vulnerability scanning with validation + patch suggestions, massive engagement (13K likes)
- **GPT-5.5-Cyber** included — government-coordinated restricted release signals new access tier for frontier models
- **Karpathy's thesis** (LLMs enable new app categories, not just acceleration) highlighted as strategic insight
- **Ling-2** (China's trillion-param open-source model) and **LLM-jp-4** (Japanese models beating GPT-4o) both included — non-US open-weight frontier race accelerating
- **Gemini Embedding 2** — first natively multimodal embedding model (text+image+video in one space)
- **Anthropic TS SDK v0.92.0** — Managed Agents API improvements noted
- **Emollick's Mythos framing** — it's a capable general model restricted for safety, not a specialist cyber model
- **PyTorch Lightning supply chain attack** — ML infra now a target

**Lessons Learned:**
- Felix Rieseberg's 98/2 rule: AI collapses 80/20 → "basically works" is instant, last 2% polish still takes real time
- Mollick's natural experiment: Microsoft & OpenAI have same models but wildly different products → product design > model access
- Zig's AI ban rationale: PR review exists to grow contributors, not just verify code quality — AI submissions short-circuit mentorship

**Action Items:**
- Ingest Claude Security, enterprise agents guide, and prompt caching blog posts into wiki
- Track Managed Agents API evolution (SDK v0.92.0)
- Monitor GPT-5.5-Cyber access expansion
- Update wiki with Gemini Embedding 2 multimodal capabilities