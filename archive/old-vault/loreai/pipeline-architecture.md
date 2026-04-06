# LoreAI v2 — Pipeline Architecture (Code-Derived)

> Generated 2026-03-18 from source code analysis, not specs.

---

## Pipeline A — News Collection

| | |
|---|---|
| **Trigger** | Cron daily 4:00 AM SGT (Mon–Fri) |
| **Script** | `scripts/collect-news.ts` |

### Inputs

| Source | Type | Volume |
|--------|------|--------|
| RSS Feeds (TechCrunch, Verge, Ars, VentureBeat, MIT, Wired, Simon Willison, Lilian Weng, LangChain, Latent Space, Interconnects) | HTTP/RSS | ~35 items |
| Official Blogs (Anthropic eng+news, OpenAI releases, DeepMind, Google AI, HF) | HTTP/sitemap | ~25 items |
| Twitter/X (36 accounts + 18 search queries) | API via `lib/twitter.ts` | ~80 items |
| GitHub (5 trending queries + 18 release repos) | GitHub API | ~146 items |
| HuggingFace (trending + org-specific) | HF API | ~50 items |
| Hacker News (top 30 filtered by AI keywords) | HN API | ~7 items |
| Reddit (MachineLearning, artificial, LocalLLaMA, singularity) | Reddit API | ~23 items |

### Process Steps

1. Fetch items from each tier (0–5) with source-specific parsers
2. Assign scores per source (75–92 for RSS/blogs, 50–90 for GitHub, 50–85 for Reddit)
3. Capture engagement metrics (likes, retweets, downloads, comments)
4. Deduplicate by URL (in-batch, then DB UNIQUE constraint)
5. Bulk insert into SQLite

### Outputs

| Output | Location | Downstream |
|--------|----------|------------|
| `news_items` rows | SQLite DB | Newsletter (B), Entity Extract (A2), Blog seeds (B→C), Planner news signals (E) |

---

## Pipeline A2 — Entity Extraction

| | |
|---|---|
| **Trigger** | Cron daily 6:30 AM SGT |
| **Script** | `scripts/extract-entities.ts` |

### Inputs

| Source | Details |
|--------|---------|
| `news_items` table | Last 30 hours of items |
| `skills/entity-extraction/SKILL.md` | System prompt |
| Claude Sonnet 4.6 | AI extraction |

### Process Steps

1. Load recent news items (30h window)
2. Call Sonnet 4.6 with entity extraction skill
3. Parse JSON array of `{entity, normalized, type, mentions}` (types: company/model/technology/framework/concept/product)
4. For each entity: `upsertTopicCluster(slug, name)` → `topic_clusters` table
5. For each entity: `upsertKeyword(entity, 'ai-extraction', slug)` → `keywords` table
6. For new clusters: `braveExpandNewTopics()` — Brave Search for related keywords

### Outputs

| Output | Location | Downstream |
|--------|----------|------------|
| `topic_clusters` rows | SQLite DB | SEO daily gap analysis (D), Weekly strategy (J) |
| `keywords` rows | SQLite DB | SEO daily generation (D) |
| Brave related data | `topic_clusters.brave_related_json` | SEO generation context |

---

## Pipeline B — Newsletter Generation

| | |
|---|---|
| **Trigger** | Cron daily 5:00 AM SGT (Mon–Fri) |
| **Script** | `scripts/write-newsletter.ts` |

### Inputs

| Source | Details |
|--------|---------|
| `news_items` table | Last 72 hours |
| Previous newsletters | Last 7 days from `content/newsletters/en/` (for dedup) |
| Cluster changes | Via `getClusterChanges()` for blog seed enrichment |
| Skills | `newsletter-en/SKILL.md`, `newsletter-zh/SKILL.md`, `newsletter-outline/SKILL.md`, `email-en/SKILL.md`, `email-zh/SKILL.md` |
| Claude API | Opus (primary), Sonnet/Haiku (ZH fallback) |
| Brave Search | Blog seed search demand signal |

### Process Steps

1. **Pre-filter**: Hard caps by source type (Twitter RT dedup, GitHub blocklist, HF min 100 likes, priority bypass for Anthropic/OpenAI/Google)
2. **Agent filter** (3-tier fallback): Agent with tools → Opus single-shot → Rule-based quotas → select 18–25 items with category balance (LAUNCH, TOOL, TECHNIQUE, RESEARCH, INSIGHT, BUILD)
3. **Outline generation**: Claude generates JSON outline (headline hook, Pick of the Day, Model Literacy section, section ordering, prominence levels) → `data/outlines/{DATE}.json`
4. **EN newsletter**: Claude Opus writes full markdown newsletter following outline
5. **ZH newsletter**: Independent creation (not translation), 3-tier model fallback (Opus → Sonnet → Haiku)
6. **Blog seed extraction**: Score top 15 items (engagement 30% + search demand 30% + mention frequency 40%), append cluster-derived seeds, save top 5
7. **Email HTML generation**: Rewrite markdown for email layout, convert to HTML
8. **Persist**: Write files, upsert DB records, link content sources, mark items as selected

### Outputs

| Output | Location | Downstream |
|--------|----------|------------|
| EN newsletter | `content/newsletters/en/{DATE}.md` | Weekly digest (I), Review (K), Vercel deploy (L) |
| ZH newsletter | `content/newsletters/zh/{DATE}.md` | Weekly digest (I), Review (K), Vercel deploy (L) |
| Blog seeds | `data/blog-seeds/{DATE}.json` | Blog generation (C) |
| Filtered items | `data/filtered-items/{DATE}.json` | Weekly digest (I), Review (K) |
| Outline | `data/outlines/{DATE}.json` | (internal reference) |
| Email HTML | `content/newsletters/email/{en,zh}/{DATE}.html` | Email distribution (L) |
| `content` rows | SQLite DB | (traceability) |
| `content_sources` links | SQLite DB | (traceability) |
| `news_items.selected_for_newsletter_at` | SQLite DB | Prevents re-selection |

---

## Pipeline C — Blog Generation

| | |
|---|---|
| **Trigger** | Cron daily 7:00 AM SGT (Mon–Fri) |
| **Script** | `scripts/write-blog.ts` |

### Inputs

| Source | Details |
|--------|---------|
| `data/blog-seeds/{DATE}.json` | Top-scored topics (falls back to yesterday) |
| `news_items` table | 7-day window for related context |
| Source URLs | HTTP fetch (3000 char excerpt) |
| Skills | `blog-en/SKILL.md`, `blog-zh/SKILL.md` |
| Claude Opus | EN + ZH generation |
| `lib/seo-extract.ts` | Entity extraction from generated content |

### Process Steps

1. Load seeds from today's JSON (fallback to yesterday if missing)
2. Select top 2–3 candidates by composite score, dedup vs last 7 days of blog slugs
3. Fetch source URL content (strip HTML, truncate to 3000 chars)
4. Find related news (keyword match against 7-day DB items, max 10)
5. EN generation: Claude Opus + blog skill → markdown with YAML frontmatter (800–1500 words), 3 retries
6. ZH generation: Claude Opus only (no fallback, skip candidate on failure)
7. SEO entity extraction: Claude extracts glossary terms, FAQ entries, comparison pairs → `upsertKeyword()` with 3 args
8. Also save brave_discussions and brave_related_searches from seed as keywords

### Outputs

| Output | Location | Downstream |
|--------|----------|------------|
| EN blog post | `content/blog/en/{slug}.md` | Review (K), Vercel deploy (L), Weekly cluster changes (I) |
| ZH blog post | `content/blog/zh/{slug}.md` | Review (K), Vercel deploy (L) |
| `content` rows | SQLite DB | (traceability) |
| `keywords` rows | SQLite DB | SEO daily gap analysis (D) |
| Blog errors | `data/blog-errors/{DATE}.json` | Review (K) |

---

## Pipeline D — SEO Daily Generation

| | |
|---|---|
| **Trigger** | Cron daily 9:00 AM SGT |
| **Script** | `scripts/generate-seo.ts` (default mode) |

### Inputs

| Source | Details |
|--------|---------|
| `topic_clusters` table | WHERE `mention_count >= 2` |
| `keywords` table | Per cluster, all keyword rows |
| Content filesystem | Check existence of `content/{type}/{lang}/{slug}.md` |
| `content` table | Check for existing DB records |
| Skills | `skills/seo/SKILL.md` |
| Claude API | EN + ZH generation |

### Process Steps

1. Load topic clusters with mention_count ≥ 2 (top 10 by count)
2. Load keywords per cluster from DB
3. Identify content gaps:
   - **Glossary**: Missing entry for cluster's `pillar_topic`
   - **FAQ**: From keywords with source `brave-discussion` or `blog-faq:*` (max 2/cluster)
   - **Compare**: From keywords matching `vs` pattern or `blog-compare:*` source (max 2/cluster)
   - **Topic Hub**: If mention_count ≥ 5 and `has_topic_hub = 0`
4. Deduplicate by type+slug, rate-limit to `MAX_PAGES_PER_RUN = 8`
5. Generate EN + ZH for each job (Claude with skill prompt, retry logic, type-specific validators)
6. Update `keywords` table: set `content_exists = 1`, `content_type`, `content_slug`
7. For topic hubs: update `topic_clusters.has_topic_hub = 1`

### Outputs

| Output | Location | Downstream |
|--------|----------|------------|
| Glossary pages | `content/glossary/{en,zh}/{slug}.md` | Review (K), Vercel deploy (L), Health (K) |
| FAQ pages | `content/faq/{en,zh}/{slug}.md` | Review (K), Vercel deploy (L), Health (K) |
| Compare pages | `content/compare/{en,zh}/{slug}.md` | Review (K), Vercel deploy (L), Health (K) |
| Topic hub pages | `content/topics/{en,zh}/{slug}.md` | Review (K), Vercel deploy (L), Health (K) |
| `content` rows | SQLite DB | (traceability) |
| Updated `keywords` | SQLite DB | Future gap analysis cycles |
| Updated `topic_clusters` | SQLite DB | Future gap analysis cycles |

---

## Pipeline E — Cluster Discovery & Planning

| | |
|---|---|
| **Trigger** | Manual or cron via `daily-pipeline.sh discover` |
| **Script** | `scripts/planner.ts` + `scripts/lib/discover.ts` |

### Inputs

| Source | Details |
|--------|---------|
| `data/flagship-clusters/{slug}.json` | Cluster definition (pillar topic, domains, existing targets) |
| Serper.dev API | SERP demand signals (7 query patterns per topic) |
| Exa Search API | Semantic gap discovery (findSimilar on cornerstone + top compare) |
| Brave Search API | Fallback for competitor content audit |
| `news_items` table | 14-day scan for news signals |
| `data/gsc-exports/latest.csv` | Unmatched query import |
| Claude API | Competitor audit extraction, news signal extraction, refresh detection |
| Skills | `planner/competitor-audit.md`, `news-signal-extract.md`, `refresh-detect.md` |

### Process Steps (6-stage discovery)

1. **SERP Demand**: 7 Serper.dev queries → PAA (→ FAQ candidates), related searches, organic URLs
2. **Exa Semantic Gap**: `exaFindSimilar()` on cornerstone + top compare → compare/FAQ candidates
3. **Competitor Audit**: Exa/Brave search → fetch pages → LLM extracts compare_targets + faq_questions
4. **News Signals**: 14-day `news_items` scan → batch LLM extraction → entity pairs, questions, freshness events (cached to `.freshness-cache.json`)
5. **GSC Import**: Parse CSV, filter by pillar topic + ≥10 impressions + no landing page, classify as compare/FAQ
6. **Scoring**: Multi-signal formula (max 100): Brave count (20) + related search (25) + competitor coverage (20) + cluster relevance (15) + intent clarity (10) + freshness (10) + GSC impressions (35) + PAA (20) + Exa (15). Drop < 30, "low-signal" 30–39, "pending" ≥ 40
7. **Glossary Inference**: Scan compare targets → extract item_b as glossary terms

### Management Commands

| Command | Action |
|---------|--------|
| `--status` | Display candidates grouped by type with score-based hierarchy |
| `--promote=<slug>` | Move candidate to target array, infer glossary, set status=approved |
| `--promote-above=<score>` | Batch promote all pending candidates ≥ threshold |
| `--dismiss=<slug>` | Set candidate status=dismissed |
| `--refresh-check` | Detect stale pages via freshness signals → append RefreshFlag to cluster JSON |
| `--clear-refresh=<slug\|all>` | Set refresh flags to cleared |

### Outputs

| Output | Location | Downstream |
|--------|----------|------------|
| Candidates appended | `data/flagship-clusters/{slug}.json` | Promotion → cluster generation (F) |
| `keywords` rows | SQLite DB | SEO daily gap analysis (D) |
| Freshness cache | `data/flagship-clusters/.freshness-cache.json` | Refresh detection (G) |
| Refresh flags | `data/flagship-clusters/{slug}.json` → `refresh_needed[]` | Refresh execution (G) |

---

## Pipeline F — Cluster Content Generation

| | |
|---|---|
| **Trigger** | Manual or cron via `daily-pipeline.sh cluster --slug=<name>` |
| **Script** | `scripts/generate-seo.ts --cluster=<SLUG>` |

### Inputs

| Source | Details |
|--------|---------|
| `data/flagship-clusters/{slug}.json` | Cluster definition with targets (status=missing) |
| Source resolution chain | Curated URL → Exa Search → Brave Search → empty |
| `lib/source-fetch.ts` | `resolveSource()`, `fetchWithCache()`, `buildGroundingInstruction()` |
| Skills | `skills/seo/SKILL.md` (SEO pages), `skills/blog-en/SKILL.md` (cornerstone) |
| Claude API | EN + ZH generation |

### Process Steps

1. Load cluster JSON, filter targets with `status = 'missing'`
2. Resolve source material for each page via fallback chain:
   - Curated URL → fetch + cache (15s timeout, HTML→text)
   - Exa Search with domain filtering → first result with >200 chars
   - Brave Search → prioritize official domains → fetch top 2–3 results
   - Empty string fallback (graceful)
3. Build factual grounding instruction (ONLY facts from source material, "not publicly documented" for missing details)
4. Generate cornerstone page if missing (2000–4000 tokens, ≥800 words validation)
5. Generate remaining SEO pages (compare, FAQ, glossary) up to MAX_PAGES_PER_RUN = 8
6. Update cluster JSON status (missing → exists)
7. Upsert keywords with source='cluster-target'

### Outputs

| Output | Location | Downstream |
|--------|----------|------------|
| Cornerstone page | `content/blog/{en,zh}/{slug}.md` | Review (K), Vercel deploy (L) |
| Compare pages | `content/compare/{en,zh}/{slug}.md` | Review (K), Vercel deploy (L) |
| FAQ pages | `content/faq/{en,zh}/{slug}.md` | Review (K), Vercel deploy (L) |
| Glossary entries | `content/glossary/{en,zh}/{slug}.md` | Review (K), Vercel deploy (L) |
| Updated cluster JSON | `data/flagship-clusters/{slug}.json` | Health (K), Discovery (E) |
| `content` rows | SQLite DB | (traceability) |
| `keywords` rows | SQLite DB | SEO daily (D) |

---

## Pipeline G — Refresh Detection & Execution

| | |
|---|---|
| **Trigger** | `planner.ts --refresh-check` (detection) + `generate-seo.ts --cluster=<SLUG> --refresh` (execution) |
| **Script** | `scripts/lib/discover.ts` (detection) + `scripts/generate-seo.ts` (execution) |

### Inputs

| Source | Details |
|--------|---------|
| `.freshness-cache.json` | Freshness events from discovery Stage 3 |
| `news_items` table | 7-day fallback if no cache |
| `data/flagship-clusters/{slug}.json` | Cluster definition + existing content paths |
| Content files | Existing markdown to reference during refresh |
| Claude API | Staleness assessment + refresh generation |
| Skills | `planner/refresh-detect.md` |

### Process Steps — Detection (`--refresh-check`)

1. Collect freshness signals (cache or 7-day news fallback)
2. Map event types to affected pages:
   - `pricing-change` → cornerstone + pricing/cost/free FAQs + all compares
   - `new-feature` / `version-release` → cornerstone + all compares
   - `deprecation` → cornerstone + install/setup/how-to FAQs
   - `platform-change` → cornerstone + windows/install/setup FAQs + all compares
3. LLM staleness check per affected page → severity (high/medium/low), affected_sections, reason
4. Append `RefreshFlag[]` to cluster JSON (status=pending)

### Process Steps — Execution (`--refresh`)

1. Load cluster JSON, filter `refresh_needed[]` where status=pending
2. Validate EN content files exist
3. Resolve fresh sources (compare: primary + competitor; FAQ/blog: primary; glossary: none)
4. Generate refreshed EN content (prompt includes: fresh sources, existing content, internal links, affected sections + reason)
5. Generate refreshed ZH independently (references new EN content)
6. Write both EN + ZH to original file paths
7. Update refresh flag status to 'refreshed'

### Outputs

| Output | Location | Downstream |
|--------|----------|------------|
| Refresh flags | `data/flagship-clusters/{slug}.json` → `refresh_needed[]` | Refresh execution, Health (K) |
| Refreshed EN/ZH pages | `content/{type}/{en,zh}/{slug}.md` | Vercel deploy (L) |
| Updated cluster JSON | `data/flagship-clusters/{slug}.json` | Health (K) |

---

## Pipeline H — GSC Export

| | |
|---|---|
| **Trigger** | Manual or cron via `daily-pipeline.sh gsc-export` |
| **Script** | `scripts/gsc-export.ts` |

### Inputs

| Source | Details |
|--------|---------|
| Google Search Console API | Service account auth via `config/gsc-service-account.json` |
| Site | `loreai.dev` |

### Process Steps

1. Load service account key, create JWT token, authenticate via OAuth2
2. Query Search Analytics: 7-day window offset by 3 days (GSC data lag)
3. Aggregate by query + page dimensions
4. Format as CSV: Query, Page, Clicks, Impressions, CTR%, Position
5. Create symlink `latest.csv` pointing to new export

### Outputs

| Output | Location | Downstream |
|--------|----------|------------|
| CSV export | `data/gsc-exports/weekly-{DATE}.csv` | Discovery GSC channel (E), Health (K) |
| Symlink | `data/gsc-exports/latest.csv` | All consumers use symlink |

---

## Pipeline I — Weekly Digest

| | |
|---|---|
| **Trigger** | Cron Saturday 5:00 AM SGT |
| **Script** | `scripts/write-weekly.ts` |

### Inputs

| Source | Details |
|--------|---------|
| `content/newsletters/en/` | Mon–Fri newsletter markdown |
| `data/filtered-items/{DATE}.json` | 5 days of scored item JSONs |
| Cluster changes | `getClusterChanges(monday, saturday)` from cluster JSONs |
| Blog posts | `content/blog/{en,zh}/` (date-filtered, video_status='published') |
| Skills | `newsletter-weekly-en/SKILL.md`, `newsletter-weekly-zh/SKILL.md` |
| Claude Opus | EN + ZH generation |

### Process Steps

1. Load Mon–Fri newsletter files (verify all 5 exist)
2. Load filtered-items JSONs for all 5 days
3. Rank stories: group by topic → score = frequency × 0.3 + engagement × 0.3 + max_score × 0.4
4. Select top 5 with category diversity (max 2 from same category)
5. Load cluster changes (new/updated pages this week)
6. EN weekly: Claude Opus writes 5-story synthesis + video posts section + topic updates section
7. ZH weekly: Independent creation, 3-tier fallback (Opus → Sonnet → Haiku)
8. Extract title/description, write files with frontmatter, upsert DB records

### Outputs

| Output | Location | Downstream |
|--------|----------|------------|
| EN weekly | `content/newsletters/weekly/en/{YYYY-WXX}.md` | Vercel deploy (L) |
| ZH weekly | `content/newsletters/weekly/zh/{YYYY-WXX}.md` | Vercel deploy (L) |
| `content` rows | SQLite DB | (traceability) |

---

## Pipeline J — Weekly Strategy

| | |
|---|---|
| **Trigger** | Cron or manual via `daily-pipeline.sh cluster-strategy` |
| **Script** | `scripts/generate-seo.ts --weekly-strategy` |

### Inputs

| Source | Details |
|--------|---------|
| `topic_clusters` table | All active clusters |
| `keywords` table | Per-cluster keyword inventory |
| Brave Search API | Demand validation (top 10 pillar topics, 1000 result threshold) |

### Process Steps

1. Run gap analysis: clusters × existing content
2. Brave batch validation: check search demand for top 10 topics
3. Generate priority-scored content plan:
   - High demand topics → priority 1, others → priority 2
   - Glossary (if not exists), Topic Hub (if mention ≥ 5), FAQ (up to 3/cluster, priority+1), Compare (up to 2/cluster, priority+1)
4. Sort each category by priority, write plan JSON

### Outputs

| Output | Location | Downstream |
|--------|----------|------------|
| Content plan | `data/content-plan/{weekNumber}.json` | Reference for manual planning |

---

## Pipeline K — Monitoring & Reporting

### K1: Cluster Health (`scripts/cluster-health.ts`)

| | |
|---|---|
| **Trigger** | Manual or cron via `daily-pipeline.sh health` |

**Reads**: Cluster JSONs + content files + GSC CSV (optional) + internal link graph
**Reports**: Completeness (targets by type), link health (broken/orphan/density), refresh status, discovery pipeline (candidate counts), GSC performance (CTR, position), schema coverage (JSON-LD)
**Writes**: `data/reports/cluster-health-{slug}-{date}.{md,html,json}`

### K2: Daily Review (`scripts/generate-review.ts`)

| | |
|---|---|
| **Trigger** | After daily pipeline run |

**Reads**: Newsletters + blogs + SEO pages + filtered-items + blog-seeds + blog-errors + keywords + clusters + live site
**Validates**: Newsletter structure (no stale news, no cross-day repeats, CJK punctuation), blog (800–1500 words, frontmatter, internal links), SEO (word counts by type)
**Writes**: `data/review/{DATE}.html` (dashboard + rendered content + benchmarks)

### K3: Pipeline Validation (`scripts/validate-pipeline.ts`)

| | |
|---|---|
| **Trigger** | Pre-commit gate (called by daily-pipeline.sh after each step) |

**Checks per step**: collect (≥20 items, ≥3 tiers), newsletter (≥10 links, ≥2 H2, required sections), blog (word count, glossary links, frontmatter), SEO (word counts by type)

---

## Pipeline L — Distribution

| | |
|---|---|
| **Trigger** | After content generation steps |

### L1: Email (`scripts/send-newsletter.ts`)
- Reads: `content/newsletters/email/{en,zh}/{DATE}.html` + `subscribers` table
- Sends: EN + ZH email newsletters to confirmed subscribers

### L2: Web Deploy
- Mechanism: `git push` triggers Vercel SSG rebuild
- All content files (newsletters, blogs, SEO pages, weekly) are deployed via static site generation

---

## Data Flow Summary

### SQLite Tables

| Table | Written By | Read By |
|-------|-----------|---------|
| `news_items` | Collect (A) | Newsletter (B), Blog (C), Entity Extract (A2), Planner news signals (E), Refresh fallback (G) |
| `topic_clusters` | Entity Extract (A2), SEO Daily (D) | SEO Daily (D), Weekly Strategy (J), Review (K) |
| `keywords` | Entity Extract (A2), Blog (C), SEO Daily (D), Cluster Gen (F), Planner (E) | SEO Daily (D), Weekly Strategy (J), Review (K) |
| `content` | Newsletter (B), Blog (C), SEO Daily (D), Cluster Gen (F), Weekly (I) | SEO Daily (D) (existence check) |
| `content_sources` | Newsletter (B) | (traceability only) |
| `subscribers` | Website signup form | Email Distribution (L) |

### File Stores

| File/Directory | Written By | Read By |
|---------------|-----------|---------|
| `data/blog-seeds/{DATE}.json` | Newsletter (B) | Blog (C), Review (K) |
| `data/filtered-items/{DATE}.json` | Newsletter (B) | Weekly (I), Review (K) |
| `data/outlines/{DATE}.json` | Newsletter (B) | (internal reference) |
| `data/flagship-clusters/{slug}.json` | Planner (E), Cluster Gen (F), Refresh (G) | Planner (E), Cluster Gen (F), Refresh (G), Health (K), Weekly cluster changes (I) |
| `data/flagship-clusters/.freshness-cache.json` | Planner discovery Stage 3 (E) | Refresh detection (G) |
| `data/gsc-exports/latest.csv` | GSC Export (H) | Planner GSC channel (E), Health (K) |
| `data/content-plan/{week}.json` | Weekly Strategy (J) | (manual reference) |
| `data/review/{DATE}.html` | Review (K) | (human review) |
| `data/reports/cluster-health-*.md` | Health (K) | (human review) |
| `content/newsletters/{en,zh}/{DATE}.md` | Newsletter (B) | Weekly (I), Review (K), Vercel (L) |
| `content/newsletters/weekly/{en,zh}/` | Weekly (I) | Vercel (L) |
| `content/newsletters/email/{en,zh}/{DATE}.html` | Newsletter (B) | Email (L) |
| `content/blog/{en,zh}/{slug}.md` | Blog (C), Cluster Gen (F), Refresh (G) | Review (K), Health (K), Weekly (I), Vercel (L) |
| `content/glossary/{en,zh}/{slug}.md` | SEO Daily (D), Cluster Gen (F), Refresh (G) | Review (K), Health (K), Vercel (L) |
| `content/faq/{en,zh}/{slug}.md` | SEO Daily (D), Cluster Gen (F), Refresh (G) | Review (K), Health (K), Vercel (L) |
| `content/compare/{en,zh}/{slug}.md` | SEO Daily (D), Cluster Gen (F), Refresh (G) | Review (K), Health (K), Vercel (L) |
| `content/topics/{en,zh}/{slug}.md` | SEO Daily (D) | Review (K), Health (K), Vercel (L) |

---

## Strategy Alignment

Mapping each pipeline to the strategy system roles (from the strategy doc's Section 4.3):

### Signal Engine
> Collects and processes raw information from the outside world

| Pipeline | Role |
|----------|------|
| **A — News Collection** | Primary signal ingestion — 7 tiers of sources, ~350 items/day |
| **A2 — Entity Extraction** | Signal enrichment — extracts structured entities from raw news, builds topic clusters |
| **H — GSC Export** | Performance signal — imports real search data showing what users actually search for |

### Graph Planner
> Decides what content to create, when, and in what order

| Pipeline | Role |
|----------|------|
| **E — Cluster Discovery** | 6-stage candidate discovery across 4 channels (SERP, competitor, news, GSC) with multi-signal scoring |
| **J — Weekly Strategy** | Periodic planning — gap analysis + demand validation → prioritized content plan |
| **E (management)** | Promote/dismiss workflow — human-in-the-loop curation of candidates into generation targets |

### Asset Generation
> Creates the actual content pages

| Pipeline | Role |
|----------|------|
| **B — Newsletter** | Daily newsletter (EN + ZH) — outline-driven, category-balanced, bilingual |
| **C — Blog** | Deep analysis posts from top seeds — bilingual with SEO entity extraction |
| **D — SEO Daily** | Gap-filling generation — glossary, FAQ, compare, topic hubs from keyword inventory |
| **F — Cluster Generation** | Targeted generation — source-grounded cornerstone + SEO pages from cluster definitions |

### Refresh Engine
> Keeps existing content accurate and up-to-date

| Pipeline | Role |
|----------|------|
| **G — Refresh Detection** | Freshness signal → page mapping → LLM staleness check → severity-tagged refresh flags |
| **G — Refresh Execution** | Re-generation with fresh sources, preserving internal links, updating both EN + ZH |

### Distribution Engine
> Delivers content to audiences

| Pipeline | Role |
|----------|------|
| **L1 — Email** | Newsletter email delivery to subscribers |
| **L2 — Web Deploy** | Git push → Vercel SSG rebuild → static site at loreai.dev |
| **I — Weekly Digest** | Saturday synthesis — 5 top stories + video + cluster updates |

### Monitoring Layer (cross-cutting)

| Pipeline | Role |
|----------|------|
| **K1 — Cluster Health** | Completeness + link health + GSC performance per cluster |
| **K2 — Daily Review** | Full pipeline validation report — rendered content + benchmarks vs live site |
| **K3 — Pipeline Validation** | Pre-commit quality gate — blocks bad content from shipping |

---

## Daily Timeline (SGT, Mon–Fri)

```
04:00  ┌─ A  — collect-news.ts ─────────────────────── ~350 items → news_items
       │
05:00  ├─ B  — write-newsletter.ts ──────────────────── EN + ZH newsletters
       │        ├─ → content/newsletters/{en,zh}/{DATE}.md
       │        ├─ → data/filtered-items/{DATE}.json
       │        ├─ → data/blog-seeds/{DATE}.json
       │        └─ → content/newsletters/email/{en,zh}/{DATE}.html
       │
06:30  ├─ A2 — extract-entities.ts ──────────────────── Entities → topic_clusters + keywords
       │
07:00  ├─ C  — write-blog.ts ───────────────────────── 2-3 blog posts (EN + ZH)
       │
09:00  ├─ D  — generate-seo.ts ─────────────────────── Up to 8 SEO pages (EN + ZH each)
       │
       └─ L  — git push → Vercel SSG rebuild ────────── All content live on loreai.dev

Sat 05:00  I — write-weekly.ts ─────────────────────── Weekly digest (EN + ZH)

Ad-hoc:    E — planner.ts ─────────────────────────── Discovery / promote / dismiss
           F — generate-seo.ts --cluster ──────────── Cluster generation
           G — generate-seo.ts --cluster --refresh ── Content refresh
           H — gsc-export.ts ──────────────────────── GSC data pull
           J — generate-seo.ts --weekly-strategy ──── Strategy planning
           K — cluster-health.ts / generate-review.ts  Monitoring
```
