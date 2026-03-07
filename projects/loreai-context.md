---
status: active
role: core-platform
last-updated: 2026-03-04
repo: ~/Desktop/Project/loreai-v2
---

# [[LoreAI]]

Bilingual (EN/ZH) content platform for AI developers and product managers. Website: loreai.dev

---

## Auto-synced from repo
<!-- Updated by /sync-project. Do not edit manually. -->

**Architecture:** Next.js 16 SSG app (TypeScript) with a cron-driven content pipeline. VPS collects news from 15+ sources (RSS, Twitter, GitHub, HN, Reddit) at 4am SGT → Claude Opus filters/writes EN+ZH content → git push triggers Vercel rebuild. SQLite database for news items, content, and topic clusters.

**Tech stack:** Next.js 16, React 19, TypeScript, Tailwind CSS 4, better-sqlite3, Remotion (via blog2video), Claude Opus (Anthropic API) + Claude CLI (Max Plan), Vercel (free tier SSG), Edge TTS

**Recent activity:**
- Fix DeepSeek-R1 filtering + align EN/ZH newsletter selection
- Add blog date filter (30d) and switch HuggingFace to trendingScore
- Fix rule-based fallback to include blog items in newsletter
- Fix official blog scraper: replace broken HTML regex
- Fix newsletter pipeline: nested session, Twitter parsing, spam filtering
- Replace Anthropic SDK with Claude CLI for Max Plan usage
- Full test suite added: 113 tests across 9 suites
- Batch 8 (Growth & Polish) marked production-ready

**Current status:** Production-ready (Batch 8 complete). Daily newsletter pipeline running. 28 items/day across 5 categories. Bilingual EN/ZH content.

---

## Human context

### Why this project exists
[Write: the vision for LoreAI — what gap does it fill?]

### Content architecture
1. **Content production** — [[blog2video]] feeds into this
2. **Audience acquisition** — shifting from SEO traffic to [[owning subscribers vs renting SEO traffic]]
3. **AEO / Agent Engine Optimization** — making content discoverable by AI agents ([[AEO as distribution strategy]])

### Current state and bottleneck
[Write: where is the rebuild at? What's the biggest obstacle?]

### Key strategic shift
Moving from "generate SEO traffic" to "own email subscribers."
Reason: [Write: why this matters to you]

### Connections to other projects
- [[blog2video]] — Chinese video content arm

### Open questions
- What does AEO technically look like? llms.txt? Structured data? API endpoints?
- Email subscriber acquisition strategy — what's the hook?

### Learnings
- [Add as you go]
