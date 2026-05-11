# Session Capture: loreai

**Date:** 2026-05-11
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** User ran a newsletter-to-email rewrite workflow for the 2026-05-11 ZH edition.

**Key Exchanges:**
- User provided a detailed 邮件简报改写规范 (email newsletter rewriting spec) with 9 formatting rules: 30-char title with verb, date format, 开场白, 今日看点, top 3 full stories, 快讯 one-liners, 模型小课堂 and 今日精选 preserved as-is, sign-off
- The spec is a reusable template — not currently stored in the repo as a command or skill

**Decisions Made:**
- Newsletter rewrite format is now stabilized: headline stories get full treatment (2-4 sentences), everything else compressed to `**标题**：一句话摘要。[→](url)` format
- Tone directive: "微信群里消息灵通的科技朋友" — professional, concise, opinionated, compressed for scanning

**Action Items:**
- Consider persisting the 邮件简报改写规范 as a `.claude/commands/rewrite-email.md` or similar, so it doesn't need to be pasted each time
- Newsletter content (2026-05-11) contains wiki-worthy intelligence not yet ingested: model capability regression trend (Opus 4.7 < 4.6, Gemini 3.1 < 2.5), DeepSeek $7.35B fundraise, GGUF local-AI growth data, MCP token overhead (55K tokens for 5 servers idle), Nvidia $40B equity investments in 2026