---
type: test-plan
projects: ["[[LoreAI]]", "[[blog2video]]"]
source: agent
date: 2026-03-10
status: ready
---

# Integration End-to-End Test

Validates the full [[LoreAI]] x [[blog2video]] flywheel using one real video from the existing queue.

---

## Setup

- [ ] Pick a test video from queue (e.g., `web-search-tool/`)
- [ ] Confirm it has: `meta.json`, `source_blog.md`, `video_X_script.md`

---

## 1. blog2video: CTA Slide

- [ ] Re-render one test video with `/blog2video` (or check if already rendered with new CTA)
- [ ] Final slide has QR code pointing to `loreai.dev/zh/subscribe?ref=video-cta`
- [ ] Script ends with verbal CTA mentioning loreai.dev
- [ ] `meta.json` has `"flow_source": "manual-curate"`

## 2. Claudiny: Queue Detection + Source Tracking

- [ ] Claudiny detects video in `/home/ubuntu/blog2video/queue/<slug>/`
- [ ] Notification shows `flow_source` tag (manual-curate or loreai-picker)
- [ ] Publish video manually to XHS
- [ ] Tell Claudiny "published"
- [ ] Confirm logged to `publish-log.json` with: slug, flow_source, platform, date

## 3. LoreAI: Subscribe Page + Source Tracking

- [ ] Visit `loreai.dev/zh/subscribe?ref=video-cta` — page loads in Chinese
- [ ] Submit test email
- [ ] Check VPS SQLite:
  ```bash
  sqlite3 /path/to/loreai.db "SELECT email, source, lang FROM subscribers ORDER BY id DESC LIMIT 1"
  ```
  Expected: `source='video-cta'`, `lang='zh'`
- [ ] Check Plausible dashboard → custom event `Subscribe` with source prop

## 4. LoreAI: Import Script (Single Video)

- [ ] Dry run first:
  ```bash
  cd /path/to/loreai-v2
  npx tsx scripts/import-video-blog.ts --dir=/home/ubuntu/blog2video/queue/web-search-tool/ --dry-run
  ```
- [ ] Shows what would be created: ZH blog, EN blog, glossary entries, FAQ entries
- [ ] Run for real (remove `--dry-run`)
- [ ] Check `content/blog/zh/` — new post reads like written article, not spoken script
- [ ] Check `content/blog/en/` — EN version exists
- [ ] Check `content/glossary/` — new entries from key_concepts
- [ ] `git push` → Vercel rebuild succeeds
- [ ] New pages visible on loreai.dev

## 5. LoreAI: "Watch Video" Button

- [ ] Run status update:
  ```bash
  npx tsx scripts/update-video-status.ts --slug=web-search-tool --status=published --video-url=<xhs-url-from-step-2>
  ```
- [ ] After Vercel rebuild, visit ZH blog post
- [ ] "Watch video" button appears and links to correct XHS URL

## 6. LoreAI: Batch Import

- [ ] Run batch dry run:
  ```bash
  npx tsx scripts/import-video-blog.ts --batch --dry-run
  ```
- [ ] Lists remaining unimported dirs (should skip `web-search-tool`)
- [ ] Count matches expected (6-7 remaining)

## 7. LoreAI: Newsletter Integration

- [ ] Trigger weekly newsletter generation
- [ ] Output contains "本周精读" section with the imported video post
- [ ] Section includes title + hook + link to ZH blog post

## 8. LoreAI: Cron Job

- [ ] Verify cron is registered:
  ```bash
  crontab -l | grep import-video
  ```
  Expected: `50 23 * * 1-5 ... import-video-blog.ts --batch --auto`
- [ ] Wait for one cron run (or trigger manually) and check logs

---

## Execution Order

Steps 1-3 can run in parallel. Steps 4-8 are sequential.

```
Parallel:
  ├─ Step 1: blog2video CTA check
  ├─ Step 2: Claudiny queue detection
  └─ Step 3: Subscribe page + tracking

Sequential:
  Step 4: Import single video
  Step 5: Watch video button
  Step 6: Batch import dry run
  Step 7: Newsletter section
  Step 8: Cron job verification
```

## Troubleshooting

| Issue | Likely cause | Fix |
|-------|-------------|-----|
| Import aborts | Missing `video_plan.json` in queue dir | Check SCP delivery includes all artifacts |
| Slug collision | Post already exists | Check upsert behavior in `import-video-blog.ts` |
| Subscribe source is null | `ref` param not forwarded | Check `NewsletterSignup.tsx` reads URL params |
| No Plausible event | Wrong script version | Confirm `script.tagged-events.js` in layout.tsx |
| Cron doesn't run | Wrong timezone | VPS cron uses UTC; 23:50 SGT = 15:50 UTC |
| "Watch video" missing | video_url not in frontmatter | Run `update-video-status.ts` and verify frontmatter |
