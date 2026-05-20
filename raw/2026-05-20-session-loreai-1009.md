# Session Capture: loreai

**Date:** 2026-05-20
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** User ran the ZH email newsletter rewrite workflow for the 2026-05-20 edition.

**Key Exchanges:**
- User provided a full website newsletter (Gemini 3.5 / Google I/O heavy) and the 邮件简报改写规范 spec for converting it to email format
- Assistant produced the email-optimized version following all 9 rules (title, date, opener, highlights, top 3, quick hits, 模型小课堂, 今日精选, sign-off)

**Decisions Made:**
- Email title chosen: "Gemini 3.5 来了，Karpathy 官宣加入 Anthropic" — picked the two highest-signal stories rather than just one, both with verbs
- Top 3 selected: Gemini 3.5 Flash, Karpathy → Anthropic, Claude Agent self-hosted sandbox — balanced across Google/Anthropic/developer tooling
- All remaining items (including research, industry, 技术实战) collapsed into 快讯 format with one-line summaries + arrow links

**Lessons Learned:**
- The rewrite spec is now a stable, repeatable prompt — can be reused as-is for future editions
- When the newsletter has 20+ items, the 快讯 section gets very long; may want to consider a cap or grouping in future iterations
- The spec says "3 个短语" for 今日看点 but fitting a Google I/O mega-dump into 3 highlights requires aggressive prioritization

**Action Items:**
- This rewrite spec (邮件简报改写规范 ZH) should be stored as a reusable asset if not already in `raw/` or a command file — it was provided inline, not from a saved source