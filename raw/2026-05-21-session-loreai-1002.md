# Session Capture: loreai

**Date:** 2026-05-21
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Curating the May 21, 2026 AI newsletter — selecting 22 items from the news feed after reviewing May 19–20 coverage to avoid overlap.

**Key Exchanges:**
- Reviewed previous newsletters: May 20 pick = DeepMind cell rejuvenation; May 19 pick = Anthropic acquires Stainless
- Avoided re-covering Gemini 3.5/Omni, Karpathy joins Anthropic, Stainless acquisition (already headlined)

**Decisions Made:**
- Top pick (score 97): **OpenAI's math breakthrough** — AI model disproved Erdős's 1946 unit distance conjecture. First AI-originated major mathematical discovery.
- Google I/O 2026 included as reference list (100 announcements), not as individual items — avoids overlap with May 20 Gemini coverage
- Included Microsoft-uses-Claude and Spotify-uses-Claude stories from Code with Claude London event — signals multi-provider adoption at big tech
- Cohere Command A+ (MoE, hardware-efficient) and Qwen3.7-Max (agent-optimized) tracked as frontier model launches
- NVIDIA Nemotron diffusion LM flagged as architecturally novel (parallel token generation vs autoregressive)

**Lessons Learned:**
- OpenAI $2M tokens per YC startup = distribution lock-in play ("tokenmaxxing era")
- Simon Willison's Gemini fragmentation thread (12K likes) captures real developer pain with Google's product sprawl
- "Structural backpressure beats smarter agents" — formal verification gates > model upgrades for reliable coding agents
- BBC reporting on adversarial prompt injection in Google AI search = SEO manipulation is now a production problem, not academic
- Railway stats: 3M users, 100K signups/week, thesis that PRs are dying in the agent era

**Action Items:**
- Ingest OpenAI math proof story when full write-up is published (landmark AI-for-science moment)
- Track Cohere Command A+ and Qwen3.7-Max benchmarks as they stabilize
- Update Claude Code wiki page with v2.1.144 features (/resume, /model switching)
- Consider wiki page on "AI adoption at big tech" — Microsoft and Spotify using Claude stories are notable signals