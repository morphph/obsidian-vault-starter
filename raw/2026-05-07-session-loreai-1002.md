# Session Capture: loreai

**Date:** 2026-05-07
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Curating the May 7, 2026 daily AI news digest (`/ingest-anthropic-daily`), selecting top stories from a scored candidate pool.

**Key Exchanges:**
- Reviewed May 5–6 coverage to avoid duplication before selecting today's stories
- Scored and ranked ~22 candidate items across LAUNCH, INSIGHT, TOOL, RESEARCH, BUILD categories

**Decisions Made:**
- **Code with Claude event** is the dominant story of the day — multiple items (dreaming, managed agents multiagent/outcomes/webhooks, Claude Code desktop preview tool)
- **Anthropic-SpaceX partnership** (score 98) selected as top item: access to Colossus 1 supercomputer, immediate user benefit (limits doubled, peak throttling removed)
- **OpenAI MRC protocol** (score 94) selected: open networking standard for AI training clusters, backed by AMD/Broadcom/Intel/Microsoft/NVIDIA
- **DeepSeek $50B valuation** noted as validation of open-source frontier model business
- **Ethan Mollick's take**: SpaceX selling Colossus compute to Anthropic implies Grok deprioritized as frontier model
- **SubQ claims** (50x faster, 20x cheaper than Opus 4.7) flagged with "extraordinary claims require extraordinary evidence"

**Lessons Learned:**
- Anthropic's compute-to-user-value pipeline (SpaceX deal → same-day limit increases) is uniquely fast among AI labs
- AI labs pivoting from APIs to full services companies is a confirmed industry pattern (Latent Space analysis)
- Usage volume on OpenRouter (Hy3's 3.66T tokens) is a stronger adoption signal than benchmarks
- ServiceNow research: RL agents trained for first-pass correctness outperform iterative-fix approaches

**Action Items:**
- Ingest Code with Claude event announcements into wiki (dreaming, multiagent orchestration, outcomes, webhooks)
- Update `wiki/anthropic.md` with SpaceX partnership and compute expansion details
- Track managed agents multiagent API (`managed-agents-2026-04-01` beta header) in tools/builder wiki pages
- Monitor SubQ independent benchmark results
- Note Next.js v16.2.5 security patch (DoS + middleware bypass) — relevant to builder projects