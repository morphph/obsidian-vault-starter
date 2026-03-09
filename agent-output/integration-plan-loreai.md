---
type: implementation-plan
project: "[[LoreAI]]"
related: "[[blog2video]]"
source: agent
date: 2026-03-09
status: ready
---

# LoreAI v2: Integration Plan

Part of the [[LoreAI]] x [[blog2video]] content flywheel. This plan covers all changes in the `loreai-v2` repo. Execute steps in order — each builds on the previous.

## Why

Both projects serve the same content domain (AI developer education) but the loop between them is open:
- LoreAI blog posts already generate `video_ready`, `video_hook`, `video_status` in frontmatter — but `video_url` is never filled, so the "Watch video" button on ZH blog pages never activates
- blog2video produces rich artifacts (Chinese scripts, video_plan.json with structured concepts/hooks/analogies, cleaned source_blog.md) — all discarded after video render
- No `/zh/subscribe` page exists for Chinese audience capture from video viewers
- No source tracking on subscribe API — can't measure what converts
- Plausible analytics has no custom events — can't track signup conversions
- Videos have zero CTA pointing to LoreAI

**Goal**: Close the loop. Video viewers → subscribers. Video artifacts → blog posts + SEO pages. Measure everything.

> **Parallel work**: blog2video's CTA injection (see `~/Desktop/Project/blog2video/integration-plan-blog2video.md`) can run at the same time as Step 1 here.
> **Dependency**: Step 2 below needs blog2video to have produced at least one video output directory to import from.

---

## Step 1: Measurement Foundation (~3h)

*Do this first. Without source tracking, you can't measure whether anything else works.*

### 1a. Create `/zh/subscribe` page

- **New file**: `src/app/zh/subscribe/page.tsx`
- Model on existing `src/app/subscribe/page.tsx`
- Accept `?ref=` query parameter from URL
- Chinese copy — value props: AI精读深度解读 + 双语覆盖 + 每日中文简报
- Pass `ref` value to the subscribe API as `source`

### 1b. Add source tracking to subscribe API

- **Edit**: `server/db.ts` — add `source TEXT` column to `subscribers` table
- **Edit**: `server/index.ts` — accept `source` field in POST `/api/subscribe` body, store in DB
- **Edit**: `src/app/api/subscribe/route.ts` — forward `source` param to VPS API
- **Edit**: `src/components/NewsletterSignup.tsx` — read `ref` from `URLSearchParams`, include in API call

Source values to track: `video-cta`, `video-bio`, `blog-inline`, `newsletter-share`, `homepage`, `direct`

### 1c. Upgrade Plausible for conversion tracking

- **Edit**: `src/app/layout.tsx` (line ~131) — change `script.js` → `script.tagged-events.js`
- **Edit**: `src/components/NewsletterSignup.tsx` — on successful subscribe, fire:
  ```typescript
  window.plausible?.('Subscribe', { props: { source: refParam } });
  ```

### Verify

1. Visit `/zh/subscribe?ref=test`, submit email
2. Check SQLite: `SELECT email, source FROM subscribers ORDER BY id DESC LIMIT 1` — source should be `test`
3. Check Plausible dashboard for `Subscribe` custom event

---

## Step 2: Import Video Artifacts as Blog Posts (~4h)

*Biggest content ROI. Doubles output from same curation effort.*

### 2a. Build `import-video-blog.ts`

- **New file**: `scripts/import-video-blog.ts`

**Input**: path to a blog2video output directory
```bash
npx tsx scripts/import-video-blog.ts ~/Desktop/Project/blog2video/blog2video-output/agent-teams/
```

**Logic**:
1. Read `video_plan.json` → title, key_concepts, hooks, analogies
2. Read all `video_N_script.md` → Chinese narration content
3. Read `source_blog.md` → cleaned English source
4. Generate ZH blog post: use video script as primary content, Claude reformats spoken → written (NOT translation)
5. Generate EN blog post from `source_blog.md` if no matching post exists
6. Set frontmatter: `video_ready: true`, `video_hook` (from plan), `video_status: published`, `source: external`
7. Write to `content/blog/{en,zh}/{slug}.md`

**Reuse existing code**:
- `scripts/lib/ai.ts` — `callClaudeWithRetry()`
- `scripts/lib/validate.ts` — `validateBlogPost()`
- `scripts/lib/git.ts` — `gitAddCommitPush()`
- `scripts/lib/db.ts` — `upsertContent()`, `upsertKeyword()`

### 2b. Extract SEO entities from video artifacts

In the same script, also generate:
- **Glossary entries** from `video_plan.json → key_concepts[]` — each has `concept_en`, `concept_zh`, `analogy_direction` that maps directly to glossary format
- **FAQ entries** from `hook_question` and `actionable_takeaway` fields
- Write to `content/glossary/{en,zh}/` and `content/faq/{en,zh}/`

One video run could yield 3-5 glossary entries + 1-2 FAQ entries + 2 blog posts.

### 2c. Batch mode + `/import-video` slash command

The script should support batch importing all existing blog2video outputs:

**`--batch` flag**:
```bash
npx tsx scripts/import-video-blog.ts --batch [--dry-run]
```
- Scans `~/Desktop/Project/blog2video/blog2video-output/*/`
- Compares against existing blog slugs in `content/blog/en/` and `content/blog/zh/` to skip already-imported dirs
- Processes all unimported dirs sequentially
- Single git commit at the end (not per-dir)
- Always show summary before proceeding: "Found 8 unimported dirs. Import? [y/n]"

**`/import-video` slash command** (for daily use):
- **New file**: `.claude/commands/import-video.md`
- Runs the same script but with interactive UX:
  1. Scan for unimported dirs
  2. List them with titles (from `video_plan.json`)
  3. Let user pick which to import (or "all")
  4. Run import + commit + push
- This becomes the single command you run after a blog2video session

**Backfill existing 11+ videos**:
After building the script, run the batch import:
```bash
# Preview first
npx tsx scripts/import-video-blog.ts --batch --dry-run

# Then import 1-2 as quality check
npx tsx scripts/import-video-blog.ts --dir=~/Desktop/Project/blog2video/blog2video-output/agent-teams/

# Once satisfied, batch the rest
npx tsx scripts/import-video-blog.ts --batch
```

### Verify

1. Run `--dry-run` on all existing output dirs — should list 11+ candidates
2. Import one dir, check content quality on loreai.dev
3. Run `--batch` for the rest, verify all new pages appear after push
4. Test `/import-video` slash command interactively

---

## Step 3: Newsletter Enhancement (~2h)

*Makes newsletter uniquely compelling with exclusive deep-dive content.*

### 3a. Add "本周精读" section to weekly digest

- **Edit**: `scripts/write-weekly.ts`
- Query `content/blog/zh/` for posts with `video_status: published` in the past 7 days
- Include in weekly newsletter prompt: title + 2-sentence hook + link to ZH blog post
- Mention "视频版本在AI精读" to drive cross-platform awareness

### 3b. Add share link to email template

- **Edit**: `scripts/lib/email-html.ts`
- Add new section color: `'精读': { bg: '#fae8ff', fg: '#9333ea' }`
- Add "Share with a friend" `mailto:` link in email footer with pre-filled subject + `?ref=newsletter-share` UTM

### Verify

1. Trigger weekly newsletter generation
2. Check output for "本周精读" section with video-sourced content
3. Check email footer for share link with correct UTM

---

## Step 4: Video Candidate Picker (~2h)

*Automates the "what should I make a video about?" decision.*

### 4a. Build `pick-video-candidates.ts`

- **New file**: `scripts/pick-video-candidates.ts`
- Scan `content/blog/en/` for posts where `video_ready: true` AND `video_status: none`
- Score by: recency, blog seed score, topic diversity vs recent videos
- Output ranked list of 3-5 candidates with URLs + hooks
- Write to `data/video-queue/YYYY-WXX.json`

### 4b. Build `update-video-status.ts`

- **New file**: `scripts/update-video-status.ts`
- Input: slug + XHS video URL
- Updates frontmatter: `video_status: none` → `published`, sets `video_url`
- Git commit + push → Vercel rebuild → "Watch video" button activates on loreai.dev/zh/blog

### Verify

1. Run picker — check `data/video-queue/` for JSON with ranked candidates
2. Run status update on a test post — check frontmatter changed
3. After push, verify "Watch video" button appears on the ZH blog page

---

## Step 5: Subscriber Source Report (~1h)

*Closes the measurement loop. Shows what's working.*

### 5a. Build `subscriber-report.ts`

- **New file**: `scripts/subscriber-report.ts`
- Query `subscribers` table: `SELECT source, COUNT(*) FROM subscribers GROUP BY source`
- Weekly summary with totals per channel
- Write to `data/review/subscriber-report-YYYY-WXX.html` (same pattern as existing pipeline review reports)

### Verify

1. Run report after a week of tracked signups
2. Check breakdown by source — `video-cta` vs `video-bio` vs `direct` etc.

---

## Execution Summary

| Step | What | Depends on | ~Time |
|------|------|-----------|-------|
| 1 | Measurement foundation | Nothing | 3h |
| 2 | Import video → blog posts | blog2video having outputs | 4h |
| 3 | Newsletter enhancement | Step 2 (needs published video posts) | 2h |
| 4 | Video candidate picker | Step 1 (needs tracking) | 2h |
| 5 | Subscriber source report | Step 1 (needs source data) | 1h |

**Total: ~12h across 2-3 weeks**
