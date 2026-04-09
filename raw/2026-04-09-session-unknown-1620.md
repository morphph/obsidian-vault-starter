# Session Capture: unknown

**Date:** 2026-04-09
**Project:** unknown
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Content quality test on LoreAI glossary/FAQ pages — correcting a mistaken file-path migration back to in-place content updates.

**Key Exchanges:**
- User clarified that glossary pages should stay **term-centric slugs** (`codex-cli.md`), not question-style slugs (`what-is-codex-cli.md`) — content can answer questions while keeping canonical term paths
- Pre-draft planning HTML comments (`<!-- PRE-DRAFT PLANNING -->`) shipped to production — while invisible to readers, they're readable by search engines and AI answer engines, exposing SEO strategy to competitors

**Decisions Made:**
- **No slug/URL migrations during content-quality rounds** — test content quality first, change URLs separately if needed
- **No redirects to non-existent targets** — deferred ZH pages should not receive redirects until actual files exist
- **Strip planning comments before publish** — the v0.2 skill template includes them for review, but they must be removed before going live

**Lessons Learned:**
- LoreAI's glossary routing loads by **filename** (`${term}.md`), and `generateStaticParams` uses `term || slug` from frontmatter — filename must match the URL-facing identifier
- FAQ routing similarly loads by filename matching `meta.slug` — same constraint
- HTML comments are not truly hidden: search crawlers and AI extraction tools can read them. Don't include strategic planning content in comments on published pages
- When reverting commits that were already pushed, `git rebase` can conflict — force-resolving with correct file state was needed

**Action Items:**
- Ensure the v0.2 content skill **auto-strips planning blocks** before final output (or flags them for removal) — don't rely on manual cleanup for the 273 queued pages
- ZH versions of both pages still pending — create when ready at existing paths (`content/faq/zh/is-codex-free.md`, `content/glossary/zh/codex-cli.md`)