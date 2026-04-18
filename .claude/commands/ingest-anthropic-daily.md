---
name: ingest-anthropic-daily
description: "Sweep all Anthropic + Claude sources, dedupe, summarize by category. Usage: /ingest-anthropic-daily [since:YYYY-MM-DD | YYYY-MM-DD..YYYY-MM-DD | (default: since last run)]"
---

# Ingest Anthropic Daily — Sweep, Dedupe, Summarize

Read CLAUDE.md and `wiki/anthropic-daily-sources.md` first.

## Arguments

Parse `$ARGUMENTS` for time-window:
- **(empty)** → daily mode: since last run timestamp in `.claude/state/anthropic-daily-last-run.json`. If no state file exists, default to "since yesterday."
- **`since:YYYY-MM-DD`** → backfill from that date to today
- **`YYYY-MM-DD..YYYY-MM-DD`** → explicit range
- **`today` | `yesterday` | `7d` | `30d`** → relative shortcuts

## Workflow

### 1. Load source list

Read `wiki/anthropic-daily-sources.md`. Extract the 18 sources from the Final Source List table, grouped by category (Anthropic, Claude, Claude API, Claude Code, Claude Cowork).

### 2. Determine fetch window

- Read `.claude/state/anthropic-daily-last-run.json` (create dir if missing).
- Compute `[start_ts, end_ts]` based on argument.
- For each source, the effective window = `max(start_ts, source's last_fetched)` → `end_ts`.

### 3. Fetch each source within window

**IMPORTANT (Option B scope):** For the first historical backfill, **skip all X handles** — too fragile to scroll back months. X handles only fetched in **daily mode** going forward (just read the latest visible posts via Playwright, filter by date).

Per source type:

| Source type | Method | Date filter |
|---|---|---|
| anthropic.com/news, /engineering | WebFetch | Parse post dates from listing, filter to window |
| claude.com/blog | WebFetch | Parse post dates, filter to window |
| support.claude.com release-notes | WebFetch | Has dated sections, filter to window |
| platform.claude.com/docs/en/release-notes | WebFetch | Has dated sections, filter to window |
| platform.claude.com/docs/en/about-claude/models/overview | WebFetch | Snapshot — diff against last fetch |
| platform.claude.com/docs/en/claude-code | WebFetch | Snapshot — diff against last fetch |
| github raw CHANGELOG.md | WebFetch | Has dated sections, filter to window |
| github releases.atom | RSS parser | Filter entries to window |
| claude.com/cowork | WebFetch | Snapshot — diff against last fetch |
| **X handles** | Playwright `browser_navigate` | **Skip in backfill mode**; in daily mode parse top ~20 posts, filter to window |

For "Snapshot" sources (no date metadata): compare current content against last cached version → only treat changed sections as new.

### 4. Deduplicate across sources

Same announcement often appears on: blog post + multiple tweets + maybe a docs update. Cluster by topic:

- Group items mentioning the same product/feature/model name
- Within a cluster, pick **canonical source** in this priority: official blog post > docs page > release notes > tweet
- Keep tweets/secondary sources as supporting links under the canonical entry

Use LLM judgment for clustering — when in doubt about whether two items are the "same news," prefer merging.

### 5. Summarize by category

Build a structured digest grouped by these categories (matches `anthropic-daily-sources.md`):

```
## Anthropic (company)
- {item} — {one-line summary} | sources: {canonical}, +{N supporting}

## Claude (product)
- ...

## Claude API
- ...

## Claude Code
- ...

## Claude Cowork
- ...
```

Each item: 1-2 sentences max. Link the canonical source URL. List supporting sources as "(also: @handle, @handle)".

### 6. Write digest page

**Backfill (range > 7 days):** Write to `wiki/digest-anthropic-{start}-to-{end}.md` (e.g., `digest-anthropic-2026-01-01-to-2026-04-18.md`).

**Daily mode:** Write to `wiki/digest-anthropic-{YYYY-MM-DD}.md`.

Page format:
```markdown
---
type: synthesis
created: {today}
last-updated: {today}
sources:
  - {list of raw/ files saved during this run}
tags: [wiki, digest, anthropic, claude]
---

# Anthropic + Claude Digest — {window}

## Summary
{N items} across {M categories}, fetched {date}, window {start..end}. Dedupe collapsed {X} duplicates.

## {category sections from step 5}

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| {today} | {raw files} | Initial digest |
```

### 7. Update individual wiki entities

For each canonical item that significantly updates an existing entity (e.g., new Opus model → update `claude-model-family.md`), follow the normal `/ingest` flow for that page:
- Add raw source to frontmatter
- Update `last-updated`
- Append to Source Log
- Add new content under Details

If a canonical item introduces a brand-new entity/concept, create a new wiki page following the standard format.

### 8. Update state

Write `.claude/state/anthropic-daily-last-run.json`:
```json
{
  "last_run": "{ISO timestamp}",
  "sources": {
    "anthropic.com/news": "{ISO timestamp}",
    "...": "..."
  }
}
```

### 9. Update index + log

- Add digest page to `wiki/index.md` under a new `## Digests` section (create if missing).
- Append to `wiki/log.md`:
  ```
  ## [YYYY-MM-DD] anthropic-daily | {window}
  window: {start..end}
  items: {N total, {M} after dedupe}
  pages-created: digest-anthropic-{...}.md, {new entity pages}
  pages-updated: {entity pages}
  raw-saved: {raw filenames}
  ```

### 10. Report

Show in terminal:
- Window covered
- Items found / after dedupe
- Categories summary (counts per category)
- Digest page link
- Pages created/updated

## Notes for Option B (current scope)

- **First-run backfill skips X.** Only websites + RSS + CHANGELOG.
- **Daily mode (going forward) includes X.** Playwright reads top ~20 posts per handle, filters by date.
- **No LLM-as-judge dedup library yet** — use direct prompt to cluster within this command's run.
- **Idempotency:** Re-running with same window should produce same digest (state file ensures sources aren't double-counted in daily mode; backfill is explicit so it's fine to re-run).
