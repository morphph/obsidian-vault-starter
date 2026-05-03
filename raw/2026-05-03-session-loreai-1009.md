# Session Capture: loreai

**Date:** 2026-05-03
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Generated the 2026-05-03 daily AI newsletter digest (Chinese), covering DeepSeek V4, SWE-bench small model breakthrough, and developer tooling news.

**Key Exchanges:**
- Produced a full-length daily newsletter in the established format with sections: 发布动态, 研究前沿, 开发者工具, 技术实战, 行业洞察, 值得一试, 模型小课堂, 快讯, 今日精选

**Decisions Made:**
- **Today's Pick (今日精选):** Chose the 250-sample SWE-bench result over DeepSeek V4 — rationale: more counterintuitive and actionable insight (data quality > model scale) vs. yet another benchmark leapfrog
- **模型小课堂 topic:** Scaling Laws vs. Data Efficiency — tied together the 250-sample result and DeepSeek V4 Flash into a single conceptual frame

**Lessons Learned:**
- DeepSeek V4 Pro now benchmarks above Opus 4.7 Medium — open-source frontier gap closing in months, not years
- 250 training samples on an archaic architecture solved a SWE-bench task — data curation may matter more than model scale for specific tasks
- Coding agents expanding into creative workflows (Codex /hatch pixel art) — not just code generation anymore
- Agent harness should live outside the sandbox (architecture insight from Mendral paper) — trust boundary design decision worth making early
- Code with Claude conference next week (week of May 5-9, 2026) — likely new capability announcements

**Action Items:**
- Ingest DeepSeek V4 details into wiki when benchmarks stabilize
- Track Code with Claude conference announcements next week for a follow-up digest
- Consider wiki page on "data efficiency vs scaling laws" — recurring theme worth a standalone entry