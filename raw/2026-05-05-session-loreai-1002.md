# Session Capture: loreai

**Date:** 2026-05-05
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Curating daily AI news selections for the newsletter (May 5, 2026 edition), reviewing coverage overlap with May 2-4 issues.

**Key Exchanges:**
- Reviewed recent newsletter coverage to avoid repeats: DeepSeek V4 covered May 3-4, GPT-5.5 party was Quick Link May 2, Harvard o1 ER trial was May 4 PICK
- Selected 20+ items across categories: LAUNCH, TOOL, RESEARCH, INSIGHT, BUILD, TECHNIQUE

**Decisions Made:**
- Claude for Creative Work (score 95) and Unity AI Open Beta (score 92) are top LAUNCH items — both signal major platform-level strategic shifts
- Grouped Anthropic SDK releases (Python v0.98.0 + TS v0.93.0) together — both add Managed Agents APIs, Workload Identity Federation, OAuth (enterprise auth stack landing at once)
- Claude Code v2.1.128 notable for zip plugin archives, /mcp tool-count diagnostics, --channels for console auth
- DeepSeek V4 Pro still newsworthy angle: claims beating Opus 4.7 and GPT 5.5 at 10x lower cost; Proximal analysis shows self-testing leads to overconfidence

**Lessons Learned:**
- Sierra's $950M raise at $15B+ ($150M ARR in 8 quarters) = fastest proof that enterprise agent deployment is real revenue category
- Mollick flags measurement crisis: benchmarking frontier agents on longer tasks is unreliable and expensive; harness-vs-API variance is real
- Context engineering emerging as key differentiator (Patrick Debois keynote) — prompts, rules, memory deserve same rigor as model itself
- Cisco acquiring Astrix confirms agent security is now an M&A category

**Action Items:**
- Ingest Claude for Creative Work announcement → wiki (Anthropic strategy expansion)
- Ingest Unity AI Open Beta → wiki (game engine + agentic AI convergence)
- Update Anthropic SDK wiki page with v0.98.0/v0.93.0 enterprise auth features
- Track Sierra as benchmark for agent business GTM
- Monitor White House executive order on AI model guardrails