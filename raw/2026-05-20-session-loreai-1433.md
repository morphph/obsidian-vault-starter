# Session Capture: loreai

**Date:** 2026-05-20
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Generated a Chinese-language comparison article (`codex-cli-vs-claude-code`) for the LoreAI blog, comparing terminal AI coding tools.

**Key Exchanges:**
- Produced a full draft comparing Codex CLI (OpenAI) vs Claude Code (Anthropic) across security, context management, multi-agent, ecosystem, and selection criteria

**Decisions Made:**
- Framed the comparison around **design philosophy** (safety isolation vs deep integration) rather than feature checklist — this avoids a "which is better" framing and positions them as complementary
- Called out **security model** as the most fundamental differentiator (physical sandbox vs approval + hooks)
- Recommended Claude Code as default for most fullstack devs, Codex CLI for security/compliance-sensitive environments
- Cross-linked to existing blog posts: `codex-complete-guide`, `whats-so-special-about-the-claude-code`, `first-few-days-with-codex-cli`, `claude-code-extension-stack-skills-hooks-agents-mcp`

**Lessons Learned:**
- Comparison articles need related content in frontmatter across multiple content types (`related_blog`, `related_compare`, `related_faq`, `related_glossary`) to maximize internal linking
- The "什么时候选X" (when to choose X) section format works well for actionable comparison conclusions

**Action Items:**
- Article needs to be saved to `drafts/` and committed/pushed per git workflow rules
- Verify all cross-linked posts (`codex-complete-guide`, etc.) actually exist; broken internal links hurt SEO
- Consider creating an English version for bilingual arbitrage coverage