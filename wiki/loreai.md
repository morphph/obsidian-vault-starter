---
type: entity
created: 2026-04-09
last-updated: 2026-04-09
sources:
  - raw/2026-04-08-session-unknown-1216.md
  - raw/2026-04-08-session-unknown-1644.md
  - raw/2026-04-09-session-unknown-1620.md
tags: [wiki, project, seo, content-platform]
---

# LoreAI

## Summary
User's SEO/content platform at loreai.dev. Features a glossary, FAQ system, and automated content pipeline with dashboard monitoring. Focused on AI-related content with bilingual (EN/ZH) support and programmatic SEO.

## Details
- **Glossary routing:** Loads by filename (`${term}.md`); `generateStaticParams` uses `term || slug` from frontmatter. URLs are term-centric slugs (`codex-cli.md`), not question-style (`what-is-codex-cli.md`) — content can answer questions while keeping canonical term paths.
- **FAQ routing:** Loads by filename matching `meta.slug` — same constraint as glossary.
- **Dashboard:** Web-based with `DASHBOARD_SECRET` in `.env` (not PM2 env vars — those don't persist across restarts). Includes "Health Report" tab with score, stages, infrastructure checks, and auto-generated action items.
- **Pipeline visualization:** `/pipeline-flow` skill generates HTML+SVG diagram. Organized by **business purpose** (Content Consumption → Knowledge Extraction → SEO/AEO Authority Pipeline → Feedback Loop), not by cron schedule. Light mode background. Labels human-blocking steps with yellow badge, reactive vs proactive stages.
- **[[keyword-grouping-engine]]:** Reusable prompt engine for SEO keyword clustering — intent classification, content type assignment, primary keyword selection
- **Content quality patterns:**
  - HTML comments (`<!-- PRE-DRAFT PLANNING -->`) are visible to search engines and AI answer engines — must strip before publish
  - No slug/URL migrations during content-quality rounds — test content quality first, change URLs separately
  - No redirects to non-existent targets — defer until files exist
- **Scale:** 273 queued pages in pipeline

## Connections
- Related: [[blog2video]], [[keyword-grouping-engine]], [[content-distribution-china]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-09 | raw/2026-04-08-session-unknown-1216.md | Initial creation — keyword grouping engine |
| 2026-04-09 | raw/2026-04-08-session-unknown-1644.md | Added dashboard, pipeline visualization |
| 2026-04-09 | raw/2026-04-09-session-unknown-1620.md | Added content quality patterns, routing details |
