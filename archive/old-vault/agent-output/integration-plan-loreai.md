---
type: implementation-plan
project: "[[LoreAI]]"
related: "[[blog2video]]"
source: agent
date: 2026-03-10
status: in-progress
---

# LoreAI v2: Integration Plan

Part of the [[LoreAI]] x [[blog2video]] content flywheel. This plan covers all changes in the `loreai-v2` repo.

## Architecture Overview

All services run on the same VPS (`/home/ubuntu/`):

```
/home/ubuntu/blog2video/queue/          ← SCP delivery from local Mac
  ├── effective-harnesses-for-long-running-agents/
  ├── ivanhzhao-notion-thoughts/
  ├── obsidian-claude-code-life/
  ├── red-green-refactor-claude-code/
  ├── superpowers/
  ├── trq212-2027463795355095314/
  └── web-search-tool/

Each dir contains:
  meta.json              ← has flow_source ("manual-curate" or "loreai-picker"), blog_url, topic
  source_blog.md         ← cleaned English source content
  video_X_script.md      ← Chinese narration scripts (1-3 per video series)
  video_X_audio.vtt      ← subtitles
  (no .mp4 — gitignored, uploaded to Google Drive separately)
```

**Data flow**: blog2video renders on local Mac → SCP to VPS queue/ → Claudiny publishes to XHS/WeChat → LoreAI cron (11:50pm SGT) imports as blog posts → git push → Vercel rebuild.

**Key field**: `flow_source` in `meta.json` tracks origin:
- `"manual-curate"` — vfan found the content manually (blog2video default)
- `"loreai-picker"` — LoreAI's video candidate picker selected it

---

## What's Been Implemented (Step 1 — complete)

### Subscribe page + source tracking + Plausible events

- `/zh/subscribe` page exists, accepts `?ref=` param
- `NewsletterSignup` component reads `ref` from URL, sends as `source` in API call, also sends `lang`
- VPS subscribe API (`server/index.ts`) stores `source` column in SQLite `subscribers` table
- `server/db.ts` has migration to add `source TEXT DEFAULT NULL` column
- Plausible upgraded to `script.tagged-events.js` — fires `Subscribe` custom event with `{ lang, source }` props

**Expected behavior**:
- `loreai.dev/zh/subscribe?ref=video-cta` → Chinese subscribe page
- Submit email → SQLite row has `source='video-cta'`, `lang='zh'`
- Plausible dashboard shows `Subscribe` event

**If debugging**: Check `server/index.ts` line ~72 for source handling. Check `src/components/NewsletterSignup.tsx` for `useSearchParams()` reading `ref`. Check `src/app/layout.tsx` line ~131 for Plausible script URL.

---

## What Needs Implementation

### Step 2: Import Video Artifacts as Blog Posts

**Script**: `scripts/import-video-blog.ts`

```bash
# Single dir
npx tsx scripts/import-video-blog.ts --dir=/home/ubuntu/blog2video/queue/web-search-tool/

# Batch (all unimported)
npx tsx scripts/import-video-blog.ts --batch [--dry-run] [--auto]

# --auto skips confirmation prompt (for cron)
```

**Pipeline stages**:

| Stage | What | Reuses |
|-------|------|--------|
| 1 | Parse: read `video_plan.json` + `video_N_script.md` + `source_blog.md` from dir | — |
| 2 | Generate ZH blog post from script (spoken → written, NOT translation) | `callClaudeWithRetry()`, `validateBlogPost()` |
| 3 | Generate EN blog post from `source_blog.md` | `callClaudeWithRetry()`, `skills/blog-en/SKILL.md` |
| 4 | Extract SEO entities from `video_plan.json → key_concepts[]` | `upsertKeyword()` |
| 5 | Write files + DB + git | `upsertContent()`, `gitAddCommitPush()` |

**Frontmatter for imported posts**:
```yaml
video_ready: true
video_hook: "..." # from video_plan.json
video_status: published
source_type: video
flow_source: manual-curate  # or loreai-picker, read from meta.json
```

**Edge cases**:
- Multi-video series (e.g., 2 scripts) → concatenate all scripts into one article
- No `source_blog.md` → generate EN from ZH + video_plan metadata
- No `video_plan.json` → abort with clear error
- Slug collision → upsert (update existing)

**Cron job** (11:50pm SGT = 15:50 UTC):
```
50 15 * * 1-5  cd /path/to/loreai-v2 && npx tsx scripts/import-video-blog.ts --batch --auto >> /var/log/loreai-import.log 2>&1
```

**Reusable code locations**:
- `scripts/lib/ai.ts` — `callClaudeWithRetry()`
- `scripts/lib/validate.ts` — `validateBlogPost()`
- `scripts/lib/git.ts` — `gitAddCommitPush()`
- `scripts/lib/db.ts` — `upsertContent()`, `upsertKeyword()`
- `skills/blog-zh/SKILL.md` — ZH blog structure reference
- `skills/blog-en/SKILL.md` — EN blog structure reference

### Step 3: Newsletter Enhancement

- **Edit**: `scripts/write-weekly.ts` — scan `content/blog/zh/` for `video_status: published` posts in past 7 days, add "本周精读" section
- **Edit**: `scripts/lib/email-html.ts` — add `'精读': { bg: '#fae8ff', fg: '#9333ea' }` section color, add mailto share link with `?ref=newsletter-share`

### Step 4: Video Candidate Picker

- **New**: `scripts/pick-video-candidates.ts` — scan `content/blog/en/` for `video_ready: true` + `video_status: none`, rank by recency + diversity, output to `data/video-queue/YYYY-WXX.json`. **Must include `"flow_source": "loreai-picker"` in candidate data.**
- **New**: `scripts/update-video-status.ts` — takes `--slug` + `--status` + `--video-url`, updates frontmatter, git push

### Step 5: Subscriber Source Report

- **New**: `scripts/subscriber-report.ts` — `SELECT source, lang, COUNT(*) FROM subscribers GROUP BY source, lang`, write HTML to `data/review/`

---

## E2E Test Reference

See `agent-output/integration-e2e-test.md` in the obsidian vault for the full checklist. Key tests for LoreAI:

1. `/zh/subscribe?ref=video-cta` → submit → check SQLite `source` + Plausible event
2. `import-video-blog.ts --dir=<queue-dir> --dry-run` → shows what would be created
3. Import one real video → check ZH blog reads as written article, not spoken script
4. `update-video-status.ts --slug=X --video-url=Y` → "Watch video" button appears
5. `import-video-blog.ts --batch --dry-run` → lists remaining unimported dirs
6. Weekly newsletter generation → "本周精读" section appears

---

## Troubleshooting

| Symptom | Likely cause | Where to look |
|---------|-------------|---------------|
| `/zh/subscribe` 404 | Page not built | `src/app/zh/subscribe/page.tsx` exists? `npm run build` |
| Subscribe works but `source` is null | `ref` param not forwarded | `NewsletterSignup.tsx` — check `useSearchParams()` reads `ref` |
| No Plausible `Subscribe` event | Wrong script version | `layout.tsx` line ~131 — must be `script.tagged-events.js` |
| Import script can't read queue dir | Wrong path or permissions | Check `/home/ubuntu/blog2video/queue/` exists and is readable |
| Import aborts | Missing `video_plan.json` | Check SCP delivery includes all artifacts, not just .mp4 |
| ZH blog reads like spoken script | Skill prompt not converting properly | Check `skills/video-to-blog-zh/SKILL.md` instructions |
| "Watch video" button missing | `video_url` not set in frontmatter | Run `update-video-status.ts`, check `src/app/zh/blog/[slug]/page.tsx` line ~68 |
| Cron doesn't run | Timezone mismatch | VPS cron uses UTC: 23:50 SGT = 15:50 UTC |
| Slug collision on import | Post already exists | `upsertContent()` should handle — check DB behavior |
| `flow_source` missing in imported post | `meta.json` doesn't have field | Check blog2video writes `flow_source` to `meta.json` |
