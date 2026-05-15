# Session Capture: loreai

**Date:** 2026-05-15
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Generated a Chinese-language comparison article (Codex CLI vs Claude Code) for the LoreAI blog.

**Key Exchanges:**
- Produced a full-length `/zh/compare/` article with frontmatter, feature table, architectural analysis, pricing breakdown, use-case recommendations, and FAQ section

**Decisions Made:**
- Framed the comparison around two design philosophies: Codex CLI as "safety-first sandbox executor" vs Claude Code as "deeply programmable engineering platform"
- Highlighted Claude Code's 4-layer extension stack (CLAUDE.md / Skills / Hooks / MCP) as its primary moat
- Highlighted Codex CLI's sandbox isolation + open-source transparency as its primary moat
- Positioned the two tools as complementary rather than mutually exclusive ("很多团队最终会两者并用")

**Lessons Learned:**
- Comparison articles benefit from identifying a single axis of philosophical divergence (safety vs flexibility) rather than listing features side by side
- Cross-linking to existing blog posts (`codex-complete-guide`, `claude-code-extension-stack`, `claude-code-hooks-mastery`, etc.) strengthens the content hub structure

**Action Items:**
- Article needs to be saved to the appropriate path (likely `drafts/` or the blog content directory) — not yet committed
- Verify all internal cross-references (`related_blog`, `related_compare`, `related_faq`) resolve to actual published pages
- Model versions and pricing may need updating before publish (article references Opus 4.6, codex-1, $100/$200 Max tiers — confirm current accuracy)