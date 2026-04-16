# Session Capture: loreai

**Date:** 2026-04-16
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Assistant returned a scored batch of 22 AI news signals (dated 2026-04-16), likely output from a digest pipeline or `/query` run.

**Key Exchanges:**
- No user query visible — this appears to be automated pipeline output (scored news JSON), not an interactive session.

**Decisions Made:**
- None recorded.

**Lessons Learned:**
- Top signals worth tracking from this batch (by score and novelty):
  - **Claude Opus 4.7 imminent** (score 92) — The Information reporting next Anthropic flagship is close
  - **Gemini 3.1 Flash TTS + Audio Tags** (score 90) — inline text directives for voice style/pace; new prompt engineering pattern for TTS
  - **OpenAI Agents SDK sandbox** (score 88) — Vercel + Modal as official isolated execution providers; key for production agents
  - **Nucleus-Image MoE diffusion** (score 85) — 17B params / 2B active at inference; MoE architecture arrives in image gen
  - **ERNIE-Image 8B open-source** (score 84) — Baidu DiT model, #1 on benchmarks, GGUF variants same day
  - **Claude Code cost split**: 56% of spend is model "thinking", only 21% actual coding — useful budgeting benchmark
  - **Humwork MCP**: agent-initiated human escalation in 30s — novel human-in-the-loop pattern
  - **EU AI Act + GDPR amendments**: final decision ~2 weeks from 2026-04-16 — time-sensitive for EU builders
  - **Mollick hype cycle**: overstated → minor wins → real breakthrough — reusable mental model for evaluating AI claims

**Action Items:**
- Watch for official Claude Opus 4.7 announcement
- Review EU AI Act proposed amendments before ~2026-04-30 deadline if shipping to EU
- Audit Claude Code session spend using the dashboard pattern (classify turns by category)
- Evaluate Nucleus-Image and ERNIE-Image against current image gen stack