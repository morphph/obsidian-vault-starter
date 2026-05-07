# Session Capture: loreai

**Date:** 2026-05-07
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Drafting a Chinese comparison article — Claude Code vs OpenAI Codex — for the LoreAI blog.

**Key Exchanges:**
- Generated a full comparison draft (`claude-code-vs-codex`) covering architecture (local terminal vs cloud sandbox), controllability (SKILL.md system vs task instructions), async workflow advantages of Codex, and use-case recommendations for each tool.

**Decisions Made:**
- Framing: positioned as "本地实时 vs 云端异步" — two architectural philosophies, not a winner-take-all comparison. Conclusion recommends trying both.
- Cross-linked to existing blog posts: `codex-complete-guide`, `claude-code-extension-stack-skills-hooks-agents-mcp`, `claude-code-enterprise-engineering-ramp-shopify-spotify`, `claude-code-vs-cursor`.
- Related glossary terms tagged: `agentic-coding`, `agent-sdk`.

**Action Items:**
- Draft needs to be saved to `drafts/` and reviewed before publishing.
- May need to update `wiki/index.md` if a corresponding wiki page is created.
- Verify all internal links (`/zh/blog/...`, `/zh/compare/...`) resolve correctly on the live site.