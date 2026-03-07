---
type: strategy
projects: ["[[LoreAI]]", "[[blog2video]]"]
source: agent
date: 2026-03-06
status: draft
---

# Strategy: Connecting [[LoreAI]] + [[blog2video]]

## Why This Matters

[[LoreAI]] drives newsletter signups through bilingual AI content. [[blog2video]] produces Chinese narrated videos gaining views on XHS/WeChat under the "AI精读" brand. Both serve the same content domain but reach different audiences through different channels. Connecting them creates a flywheel where content and audiences compound.

## Key Discoveries

**Discovery 1: LoreAI already has 80% of the video bridge wired.**
- Every blog post generates `video_ready: true`, `video_hook`, and `video_status: none` in frontmatter (`scripts/write-blog.ts:562-564`)
- The ZH blog template already renders a "Watch video" button when `video_url` exists (`src/app/zh/blog/[slug]/page.tsx:68,134`)
- But no blog post has `video_url` populated yet — the loop is open

**Discovery 2: blog2video is a better content ingestion engine than LoreAI's blog pipeline.**
- blog2video's Step 0 + 0.5 converts ANY source (X threads, YouTube, PDFs, GitHub repos) into clean, structured English markdown (`source_blog.md`)
- LoreAI's `fetchUrlContent` just strips HTML tags and takes first 3000 chars — much worse
- The external content vfan manually curates for videos (Anthropic eng blogs, viral X threads, etc.) is high-quality signal that LoreAI's automated pipeline doesn't capture

**The two-way flow:**
- LoreAI -> blog2video: automated curation feeds video topics (partially wired)
- blog2video -> LoreAI: external content picked for videos also becomes blog posts (**completely unwired, highest untapped value**)

---

## 4 Moves, Priority Order

### Move 1: CTA Slide in Every Video (~1-2h)

Add a newsletter signup CTA as the final slide in every blog2video output. QR code pointing to `loreai.dev/zh/subscribe?utm_source=xhs&utm_medium=video&utm_campaign=ai-jingdu`. Brand: "LoreAI x AI精读".

XHS/WeChat viewers who watch a 6-min AI explainer are pre-qualified newsletter subscribers. Zero dependency on LoreAI code changes.

**Files:**
- Edit: `blog2video/.claude/skills/blog2video/prompts/slide-html-generator.md`
- New: `blog2video/blog2video-remotion/public/loreai-qr.png`

---

### Move 2: External Videos Become LoreAI Blog Posts (~3-4h) — highest value

After blog2video processes any external URL, use the already-cleaned `source_blog.md` to generate EN + ZH blog posts on loreai.dev. Every video also becomes a blog post — doubling output from the same curation effort.

New script: `loreai-v2/scripts/import-external-blog.ts`
- Reads `source_blog.md` + `video_plan.json` from blog2video output
- Uses existing blog SKILL prompts + `callClaudeWithRetry` to generate EN + ZH posts
- Writes to `content/blog/{en,zh}/` with `video_ready: true`, `video_hook`, `source: external`
- Extracts SEO entities for glossary/FAQ/comparison linking
- Human stays in the loop — blog2video prints the import command, you decide whether to run it

**Reusable code from loreai-v2:**
- `scripts/lib/ai.ts` — `callClaudeWithRetry()`
- `scripts/lib/validate.ts` — `validateBlogPost()`
- `scripts/lib/git.ts` — `gitAddCommitPush()`
- `scripts/lib/db.ts` — `upsertContent()`, `upsertKeyword()`
- `skills/blog-en/SKILL.md`, `skills/blog-zh/SKILL.md`

---

### Move 3: Video Candidate Picker + Status Writeback (~2-3h)

Script that picks best video candidate from LoreAI's auto-generated blog posts.

New: `loreai-v2/scripts/pick-video-candidate.ts`
- Reads ZH blog posts, filters `video_ready: true` + `video_status: none`
- Outputs source URL + video_hook + `/blog2video <url>` command

New: `loreai-v2/scripts/update-video-status.ts`
- Takes slug + XHS video URL, updates frontmatter
- Auto-activates "Watch video" button on loreai.dev/zh/blog

---

### Move 4: Video Queue in Daily Pipeline (~2h)

LoreAI's blog pipeline auto-writes `data/video-queue/YYYY-MM-DD.json` with top video-ready topic. blog2video gets a `--from-queue` flag.

Edit: `loreai-v2/scripts/write-blog.ts` (~line 700)
Edit: `blog2video/.claude/commands/blog2video.md`

---

## Brand Strategy

**Complementary brands, not merged:**
- **LoreAI** = platform brand (newsletter, blog, SEO). English-first, bilingual.
- **AI精读** = video brand on Chinese social. Chinese-only.
- "AI精读 by LoreAI" in video descriptions. CTA slides link to LoreAI. LoreAI blogs link to AI精读 videos.

## What NOT to Do

- Don't deploy blog2video as a web service — runs fine locally
- Don't embed XHS/WeChat videos on loreai.dev — no embed URLs available. Link-out pattern is correct.
- Don't build a shared database — JSON files + CLI scripts are the right interface
- Don't auto-publish external content — keep human in the loop for editorial quality

---

## The Flywheel (end state)

```
Flow A — LoreAI-sourced (automated):
  LoreAI collects 350+ items/day
    -> Blog pipeline writes EN+ZH posts + video_hook
    -> Video queue picks top 1 for video
    -> blog2video renders video with CTA slide
    -> XHS/WeChat viewers subscribe to LoreAI
    -> Blog post shows "Watch video" button

Flow B — Externally-sourced (human-curated):
  vfan finds great content (X threads, eng blogs, YouTube)
    -> /blog2video renders Chinese video
    -> import-external-blog.ts creates LoreAI blog post from same source
    -> Blog post on loreai.dev with video link
    -> Newsletter readers get high-quality curated deep-dives
    -> Video viewers see CTA, subscribe

Both flows feed each other.
```
