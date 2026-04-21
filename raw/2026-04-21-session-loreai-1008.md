# Session Capture: loreai

**Date:** 2026-04-21
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Processing an AI news digest dated 2026-04-21, likely for the LoreAI or AI精读 newsletter pipeline.

**Key Exchanges:**
- The session appears to have ingested or drafted a newsletter issue covering major AI news from April 21, 2026
- Two versions of the newsletter exist in context: a shorter source digest and an expanded full-issue draft

**Decisions Made:**
- Newsletter expanded the original digest into a full issue with three lead stories: Claude live artifacts, Kimi K2.6, and Opus 4.7 token inflation

**Lessons Learned:**
- **Anthropic compute**: Secured up to 5 GW through Amazon (~1 GW by end of quarter) — infrastructure arms race now measured in power plant equivalents
- **Kimi K2.6**: 1T-parameter open-weight MoE model from Moonshot AI, claims Opus 4.6-level coding at 76% lower cost — most capable open model of 2026 so far
- **Opus 4.7 token inflation**: 1.46x more tokens than 4.6 for text, up to 3x for images — same per-token price but higher effective cost; audit before upgrading image-heavy pipelines
- **MoE architecture**: Only activates ~50-100B of 1T parameters per inference — "1T parameters ≠ 1T cost"
- **Atlassian data collection**: Flipped default to opt-in AI training for all Jira/Confluence content — enterprise admins need to check settings
- **Deezer stat**: 44% of daily uploads now AI-generated — first hard number from a major platform
- **LeCun thesis**: His efficiency argument (not capability) against autoregressive scaling is the sharpest counter-narrative, especially relevant when Anthropic needs 5 GW and trillion-param models need cloud to run

**Action Items:**
- None explicitly stated