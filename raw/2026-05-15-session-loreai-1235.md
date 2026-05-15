# Session Capture: loreai

**Date:** 2026-05-15
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** User tested a "Flagship Freshness — Event-to-Subtopic Routing" prompt template against the OpenAI Codex topic with one incoming signal.

**Key Exchanges:**
- User provided a complete, production-ready prompt for classifying fresh news signals against an approved subtopic pack and existing content inventory. The prompt enforces strict routing (no new subtopics allowed), supports fan-out (one event → many subtopics), and outputs structured JSON for downstream automation.
- The single signal tested (Codex community meetup in Milan) was correctly routed as `ignore` — no technical content, no SEO value until post-event recaps surface.

**Decisions Made:**
- The routing prompt uses a conservative-create / aggressive-refresh philosophy: flag existing pages for review liberally, but only create new pages when a genuine content gap exists.
- Content types for `create` are constrained to: `faq`, `blog`, `compare`, `glossary`, `topic-hub`, `tutorial`.

**Lessons Learned:**
- The OpenAI Codex subtopic pack now has **27 approved subtopics** with freshness ratings — high-freshness subtopics include: `codex-models`, `codex-plugins`, `codex-mcp-servers`, `codex-pricing-and-plans`, `codex-changelog`, `codex-vs-competitors`.
- Community event announcements (meetups, conferences) are noise for content freshness purposes unless they contain actual product announcements or technical reveals.

**Action Items:**
- This routing prompt is a reusable pipeline component — should be stored/versioned if not already (likely part of LoreAI's freshness pipeline).
- The Codex subtopic pack and content inventory represent a snapshot as of 2026-05-15; future signals should be routed against the latest version.