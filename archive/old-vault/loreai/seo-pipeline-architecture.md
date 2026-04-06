# LoreAI v2 — SEO Pipeline Architecture

> Focused view of the SEO subsystem only. For full pipeline architecture, see `pipeline-architecture.md`.

---

## Overview

The SEO system has **4 phases** and **two generation paths**:

```
Signal Collection → Planning → Generation → Refresh
                                  ↓
                    ┌─────────────┴─────────────┐
                    │                           │
              Path 1: Reactive            Path 2: Proactive
              (SEO Daily — D)             (Cluster — E→F)
              Auto gap-fill from          Curated clusters with
              keyword inventory           multi-source discovery
```

---

## Phase 1 — Signal Collection

> Where do our SEO topics come from?

### A2: Entity Extraction (daily 6:30 AM)

**Input**: `news_items` from Pipeline A (news collection)
**Process**: Sonnet 4.6 extracts entities → upserts `topic_clusters` + `keywords` → Brave expands with related keywords
**Output**: Populates the keyword inventory that drives reactive generation (Path 1)

### H: GSC Export (manual/cron)

**Input**: Google Search Console API
**Process**: Pull 7-day search analytics (offset 3 days for data lag) → CSV
**Output**: `data/gsc-exports/latest.csv` — real search queries showing what users actually look for

---

## Phase 2 — Planning

> What content should we create?

### E: Cluster Discovery (6-stage pipeline)

This is the **proactive** planning system. It finds content candidates through 4 channels:

| Stage | Source | What it finds |
|-------|--------|---------------|
| 1 | Serper.dev (7 queries) | SERP demand: PAA → FAQ candidates, related searches |
| 2 | Exa Search (semantic) | Similar content gaps via `findSimilar()` |
| 3 | Competitor audit (Exa/Brave + LLM) | What competitors cover that we don't |
| 4 | News signals (14-day scan + LLM) | Entity pairs, questions, freshness events |
| 5 | GSC import | Queries with impressions but no landing page |
| 6 | Scoring (0-100) | Multi-signal formula, drop < 30 |

After scoring, a **human promotes or dismisses** candidates. Promoted candidates become generation targets in `flagship-clusters/{slug}.json`.

### J: Weekly Strategy

**Input**: `topic_clusters` + `keywords` + Brave demand validation
**Output**: Priority-scored content plan (`data/content-plan/{week}.json`)
**Role**: Periodic overview — which clusters need what content next

---

## Phase 3 — Generation (Two Paths)

### Path 1: SEO Daily (D) — Reactive Gap Fill

| | |
|---|---|
| **Trigger** | Daily 9:00 AM SGT |
| **Input** | `topic_clusters` (mention_count ≥ 2) + `keywords` |
| **Logic** | Find missing pages → generate up to 8/run (EN + ZH each) |

Gap detection rules:
- **Glossary**: Missing for cluster's `pillar_topic`
- **FAQ**: From `brave-discussion` or `blog-faq:*` keywords (max 2/cluster)
- **Compare**: From `vs` pattern or `blog-compare:*` keywords (max 2/cluster)
- **Topic Hub**: If `mention_count ≥ 5` and no hub exists

This path is **fully automatic** — no human curation needed.

### Path 2: Cluster Generation (F) — Proactive Targeted

| | |
|---|---|
| **Trigger** | Manual or `daily-pipeline.sh cluster --slug=<name>` |
| **Input** | `flagship-clusters/{slug}.json` (targets with status=missing) |
| **Logic** | Resolve sources → generate cornerstone + SEO pages (max 8/run) |

Source resolution chain (per page):
1. Curated URL (if provided) → fetch + cache
2. Exa Search with domain filtering
3. Brave Search → prioritize official domains
4. Empty fallback (graceful)

Key difference from Path 1: **source-grounded** — every page is backed by fetched reference material, with factual grounding instructions.

### What each path generates

| Content Type | Path 1 (Daily) | Path 2 (Cluster) |
|---|---|---|
| Cornerstone blog | — | Yes (2000-4000 tokens) |
| Glossary | Yes | Yes |
| FAQ | Yes | Yes |
| Compare | Yes | Yes |
| Topic Hub | Yes | — |

---

## Phase 4 — Refresh

> Keep existing content accurate when the world changes.

### G: Refresh Detection

**Input**: Freshness cache (from discovery Stage 4) or 7-day news fallback
**Process**:
1. Map event types to affected pages:
   - `pricing-change` → cornerstone + pricing FAQs + all compares
   - `new-feature` / `version-release` → cornerstone + all compares
   - `deprecation` → cornerstone + setup FAQs
2. LLM staleness check → severity (high/medium/low)
3. Append `RefreshFlag[]` to cluster JSON

### G: Refresh Execution

**Process**: Re-generate affected pages with fresh sources, preserving internal links. EN first, then ZH independently.
**Output**: Updated content files at their original paths.

---

## Data Flow (SEO only)

```
                    news_items (A)
                         │
                         ▼
               ┌─── A2: Entity ───┐
               │    Extraction    │
               ▼                  ▼
        topic_clusters        keywords ◄──── Blog SEO extract (C)
               │                  │
        ┌──────┼──────────────────┤
        │      │                  │
        ▼      ▼                  ▼
   D: SEO    J: Weekly     E: Cluster
   Daily     Strategy      Discovery
   (auto)    (plan)        (6-stage)
        │                       │
        │                  promote/dismiss
        │                       │
        ▼                       ▼
   glossary              flagship-clusters/
   faq                   {slug}.json
   compare                      │
   topic hub                    ▼
                          F: Cluster Gen
                          (source-grounded)
                                │
                           cornerstone
                           glossary
                           faq
                           compare

        ────── all content ──────
                    │
                    ▼
              G: Refresh
              (detect + execute)
```

---

## Key Differences: Path 1 vs Path 2

| | Path 1 (SEO Daily) | Path 2 (Cluster) |
|---|---|---|
| **Curation** | Fully automatic | Human-curated clusters |
| **Source material** | None (LLM knowledge only) | Fetched + grounded |
| **Scope** | Any cluster with ≥2 mentions | Specific flagship topics |
| **Quality** | Good for commodity SEO | Higher quality, source-backed |
| **Trigger** | Daily cron | Manual or on-demand |
| **Page types** | Glossary, FAQ, Compare, Hub | Cornerstone, Glossary, FAQ, Compare |
