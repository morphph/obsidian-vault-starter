# Session Capture: loreai

**Date:** 2026-04-21
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Newsletter curation for Apr 21 — selecting top AI news items from a scored candidate pool.

**Key Exchanges:**
- Reviewed recent coverage to avoid duplication: Apr 20 picked Advisor strategy pattern, Apr 19 picked Claude Design; Managed Agents, Opus 4.7 best practices, Simon Willison's system prompt diff already covered
- Selected ~23 items across LAUNCH, INSIGHT, TOOL, TECHNIQUE, BUILD, RESEARCH categories

**Decisions Made:**
- All Anthropic tier-1 items included (standard policy)
- Kimi K2.6 elevated due to significance (1T-param open MoE claiming Opus 4.6-level coding at 76% lower cost)
- LeCun's generative AI critique included as high-engagement counter-narrative (score 92)

**Lessons Learned:**
- Opus 4.7 hidden cost: Simon Willison measured **1.46x token inflation for text, up to 3x for images** vs Opus 4.6 at same per-token price — budget impact before migrating workloads
- Atlassian flipped default data collection on for AI training — enterprises must opt out of Jira/Confluence data sharing
- Deezer reports 44% of daily music uploads are AI-generated — first hard platform number on AI content flood
- GitHub star manipulation is widespread enough to warrant cross-referencing with download metrics
- Recursive Superintelligence raised $500M at $4B valuation at 4 months old — extreme signal of frontier AI capital environment

**Action Items:**
- None — session was selection only; draft/publish step not shown