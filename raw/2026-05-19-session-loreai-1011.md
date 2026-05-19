# Session Capture: loreai

**Date:** 2026-05-19
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** User ran email newsletter rewrite for the 2026-05-19 ZH edition using a detailed rewriting spec.

**Key Exchanges:**
- User provided a complete **邮件简报改写规范（ZH）** — a reusable spec for converting website newsletters into email-optimized format (title ≤30 chars with verb, 3 headlines kept full, rest compressed to one-line 快讯, preserve 模型小课堂 and 今日精选 verbatim)

**Decisions Made:**
- Email rewrite spec is now codified with 9 structural rules (标题, 日期, 开场白, 今日看点, 头条3则, 快讯, 模型小课堂, 今日精选, 结尾) — this should be saved as a reusable prompt/template if not already persisted
- The spec lives in the user's prompt, not yet in any file in the repo

**Lessons Learned:**
- The rewrite spec is a production workflow asset — it defines tone ("微信群里消息灵通的科技朋友"), punctuation rules (中文标点, 英文中文间加空格), and structural compression logic
- Title rule is specific: must reference the most important news WITH a verb, max 30 Chinese characters, no bare product names

**Action Items:**
- Consider persisting the 邮件简报改写规范 as a reusable template (e.g., in `raw/` or as a command/skill) so it doesn't need to be re-pasted each run
- Industry intel from this issue worth ingesting: Anthropic acquired Stainless (SDK+MCP full-stack), Cache diagnostics tool in public beta, Claude Design token limits doubled, Google I/O tomorrow with Gemini 3.2 expected