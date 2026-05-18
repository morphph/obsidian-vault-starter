# Session Capture: loreai

**Date:** 2026-05-17
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** User ran a newsletter email rewrite task — transforming a full website-format AI newsletter (2026-05-17) into a concise email-optimized version using a defined spec.

**Key Exchanges:**
- User provided a complete "邮件简报改写规范" (email newsletter rewriting spec) with 9 structural rules + tone/punctuation guidelines
- Applied spec to a ~2000-word newsletter, producing a compressed email version

**Decisions Made:**
- Email rewriting spec is now a stable, repeatable workflow (title ≤30 chars with verb, top 3 stories keep full detail, rest compressed to one-line 快讯 format)
- Format: 标题 → 日期 → 开场白 → 今日看点 → 头条3则 → 快讯 → 模型小课堂 → 今日精选 → 结尾

**Lessons Learned:**
- The spec works well as a direct prompt instruction — no tools needed, pure text transformation
- "今日看点" uses 顿号 separator (X、Y、Z) not commas
- 快讯 format: `- **标题**：一句话摘要。[→](url)` — arrow link at end
- Title rule: must reference the most important news WITH a verb, never just a product name

**Action Items:**
- Consider saving the 邮件简报改写规范 as a reusable command/skill if this becomes a regular workflow (e.g., `.claude/commands/email-rewrite.md`)
- The 2026-05-17 newsletter source content could be ingested into `raw/` for wiki knowledge (covers: MoE 30B-A3B model, GPT-5.5 Codex regression, CTF death by AI, Gemini Pro pricing rumors, PrimeIntellect autonomous research, Anthropic Mythos, test-time compute scaling)