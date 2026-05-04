# Session Capture: loreai

**Date:** 2026-05-03
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Rewriting the 2026-05-03 ZH newsletter (DeepSeek V4 Flash edition) into email-optimized format using the 邮件简报改写规范.

**Key Exchanges:**
- User provided a detailed email newsletter rewriting spec (邮件简报改写规范 ZH) with 9 structural rules: title ≤30 chars with verb, date format, one-line opener, 今日看点 with 3 phrases, top 3 stories in full, remaining items as 快讯 one-liners, preserve 模型小课堂 and 今日精选 as-is, close with "下期见 ✌️"
- Rewrite was generated directly without tool use, as instructed

**Decisions Made:**
- Chose "DeepSeek V4 Flash 登场，250 条数据攻克 SWE-bench" as email subject — combines the two most impactful stories (speed king + data efficiency paradigm shift)
- Top 3 stories: DeepSeek V4 Flash, V4 Pro vs Opus 4.7, 250-data SWE-bench — all three hit the "open source challenging closed source" theme
- All remaining items (17 stories) compressed to single-line 快讯 format with source links preserved

**Lessons Learned:**
- The 邮件简报改写规范 is a reusable spec that should be stored somewhere persistent (currently passed inline each time) — candidate for `raw/` or a dedicated template file
- When newsletter has no explicit ### headings on items in 开发者工具/行业洞察 sections, need to judge which are "top 3" vs "快讯" based on the actual ### markers, not section importance

**Action Items:**
- Consider persisting the 邮件简报改写规范 as a reusable template so it doesn't need to be pasted each run