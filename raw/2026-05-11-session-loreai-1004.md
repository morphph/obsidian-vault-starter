# Session Capture: loreai

**Date:** 2026-05-11
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Generating the daily AI newsletter editorial plan (JSON) for 2026-05-11.

**Key Exchanges:**
- Produced a 22-item newsletter plan with hero/regular/quick prominence tiers across INSIGHT, TECHNIQUE, TOOL, BUILD, LAUNCH, and QUICK_LINKS sections

**Decisions Made:**
- **Pick of the Day:** Item 36099 — "Better Every Generation assumption breaking down" (Opus 4.7, Gemini 3.1, Sonnet 4.6 all regressing vs predecessors). Thesis: model selection is now a continuous evaluation problem, not a version-number upgrade path.
- **Model Literacy concept:** Tool-Use Token Overhead — MCP's 55K token cost for 5 servers chosen as the day's educational concept.
- **Headline hook:** "Next-Gen Models Stumble, DeepSeek Eyes $7B, and Shopify Forces AI Into the Open"
- **Hero pairings:** Model regression + DeepSeek $7.35B round (INSIGHT); Shopify public-channel AI constraint + swyx's "K8s Hard Way for AI" (TECHNIQUE)

**Lessons Learned:**
- The "models always get better" assumption is empirically breaking — multiple frontier labs shipping regressions simultaneously is a pattern, not an anomaly
- MCP convenience has a concrete, quantifiable cost: ~11K tokens per server in tool schema overhead
- Shopify's "AI agents only in public channels" is a reusable adoption pattern (Midjourney Discord playbook for enterprise)
- Local AI (GGUF) is accelerating from niche to movement — HuggingFace CEO data backs this

**Action Items:**
- This JSON needs to be rendered into the final newsletter copy (no `/draft` was run yet)
- DeepSeek $7.35B story and Google I/O framing may need wiki page updates if confirmed