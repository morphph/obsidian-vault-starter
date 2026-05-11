# Session Capture: loreai

**Date:** 2026-05-11
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Curating AI newsletter items for the May 11, 2026 edition, selecting from a scored feed of ~22 candidates across Twitter, HN, GitHub, and RSS sources.

**Key Exchanges:**
- Reviewed recent newsletter coverage to avoid duplication before making selections
- Evaluated candidates across categories: INSIGHT, TOOL, TECHNIQUE, BUILD, LAUNCH

**Decisions Made:**
- Selected items span a coherent narrative arc: model quality regression (Bindureddy: next-gen models no longer guaranteed better), local AI momentum (GGUF surge + HN essay), MCP token overhead costs (55K tokens for 5-server setup), and organizational AI patterns (Shopify's public-only agent)

**Lessons Learned:**
- **Model regression is a real theme now:** Opus 4.7 < 4.6, Gemini 3.1 < 2.5, Sonnet 4.6 buggier than 4.5 — model pinning strategy matters
- **MCP token costs are measurable:** Playwright MCP = 13.7K tokens, Chrome DevTools MCP = 18K — CLI may beat MCP for token-constrained agents
- **Shopify's "public Slack only" constraint for AI agents** is a brilliant adoption pattern — forces organizational learning like Midjourney's Discord era
- **AI PR slop is now a documented open-source problem** (RPCS3 emulator case)
- **DeepSeek pivoting to commercial entity** with potential $7.35B raise, hiring product talent from ByteDance
- **Nvidia investing $40B in AI equity in 2026 alone** — evolving from supplier to investor/ecosystem owner
- **Google I/O framed as existential:** either Gemini proves model quality or Google becomes "a data center and compute seller"

**Action Items:**
- Track whether model regression trend holds post-Google I/O
- Update [[MCP]] wiki page with token overhead data when ingested
- Watch for DeepSeek commercialization moves and Google I/O outcomes