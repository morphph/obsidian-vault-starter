# Session Capture: loreai

**Date:** 2026-04-21
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Generated a Chinese comparison article draft: "Codex CLI vs Claude Code" for the LoreAI blog.

**Key Exchanges:**
- Article produced as a full MDX draft in Chinese covering architecture, security model, pricing, and use-case recommendations for both tools.

**Decisions Made:**
- Article structured as a `/compare` content type with frontmatter linking to related glossary (agentic-coding, agent-sdk), blog posts, and topics.
- Verdict framing: Claude Code = local execution + deep customization; Codex CLI = cloud sandbox + async safety.
- Slug: `codex-cli-vs-claude-code`, category: `tools`, lang: `zh`.

**Lessons Learned:**
- Key differentiator to emphasize: Codex CLI runs in cloud sandbox (safe but limited local access); Claude Code runs locally (powerful but requires permission config discipline).
- Pricing asymmetry worth noting: Claude Pro entry at $20/mo vs ChatGPT Pro at $200/mo — meaningful for individual devs.
- Both tools use parallel sub-agent support but with different execution contexts (cloud vs local).

**Action Items:**
- Save draft to `drafts/` directory if not already done.
- Verify all `related_blog` slugs exist as published or draft pages before publishing.
- Consider creating a wiki page `wiki/codex-cli.md` if one doesn't exist yet — the article references it as a topic.