---
type: implementation-plan
project: "[[blog2video]]"
related: "[[LoreAI]]"
source: agent
date: 2026-03-09
status: ready
---

# blog2video: Integration Plan

Part of the [[LoreAI]] x [[blog2video]] content flywheel. This plan covers all changes in the `blog2video` repo. Only 2 steps — blog2video's role is to inject CTAs and make its artifacts importable.

## Why

blog2video produces Chinese narrated videos from English tech content, published to XHS and WeChat under the "AI精读" brand. LoreAI (loreai.dev) is a bilingual AI newsletter/blog platform. Currently:
- Videos have zero CTA pointing to LoreAI — viewers watch and leave
- Rich artifacts (Chinese scripts, video_plan.json with structured concepts, source_blog.md) are discarded after render — they could become blog posts and SEO pages on loreai.dev
- No cross-promotion between the brands

**Goal**: Every video becomes a newsletter signup funnel. Every video's artifacts become reusable by LoreAI's import pipeline.

> **Parallel work**: LoreAI's measurement foundation (see `~/Desktop/Project/obsidian-vault-starter/agent-output/integration-plan-loreai.md`) runs at the same time as Step 1 here. No dependency on LoreAI changes.
> **Coordinate**: CTA QR code should point to `loreai.dev/zh/subscribe?ref=video-cta` — confirm this URL works after LoreAI creates the `/zh/subscribe` page.

---

## Step 1: CTA Injection into Every Video (~2h)

*Highest-leverage single change. Every future video drives newsletter signups.*

### 1a. Add verbal CTA to script writer prompt

- **Edit**: `prompts/script-writer.md` (or `.claude/skills/blog2video/prompts/script-writer.md`)
- In the outro/sign-off section, change the standard ending to include LoreAI mention:

  Current: "AI 世界很吵，精读一篇，胜过刷一百条。我们下期再见。"

  New: "AI 世界很吵，精读一篇，胜过刷一百条。搜 loreai.dev，订阅每日 AI 精读日报，我们下期再见。"

- This requires zero code changes — just a prompt edit. Immediate effect on the next video.

### 1b. Build CTA slide Remotion component

- **New file**: `blog2video-remotion/src/slides/CtaSlide.tsx`
  - Dark background matching existing slide design (`#0D0D1A`)
  - QR code image (centered)
  - Text: "订阅免费 AI 日报" + "loreai.dev"
  - Brand: "AI精读 by LoreAI"
  - Duration: ~8-10 seconds

- **Edit**: `blog2video-remotion/src/types.ts` — add `'cta'` to slide type union
- **Edit**: `blog2video-remotion/src/BlogVideo.tsx` — register `CtaSlide` in slide component map
- **Edit**: `prompts/slide-html-generator.md` — add instruction: "After the final summary slide, always add a CTA slide of type `cta`. Do not generate HTML for it — the Remotion renderer handles it automatically."

### 1c. Generate QR code

- **New file**: `blog2video-remotion/public/qr-subscribe-zh.png`
- URL: `https://loreai.dev/zh/subscribe?ref=video-cta`
- Generate with any QR tool (e.g., `qrencode` CLI or online generator)
- White QR on transparent background, 400×400px minimum

### 1d. Manual: Update platform bios

- **XHS (小红书) profile bio**: Add "每日AI深度解读 | 订阅日报: loreai.dev"
- **WeChat Video Account bio**: Same text
- This takes 5 minutes. Do it the same day as 1a.

### Verify

1. Run `/blog2video` on any test URL
2. Check generated script ends with loreai.dev verbal CTA
3. Check rendered video has CTA slide with QR code as final slide
4. Scan QR → should open `loreai.dev/zh/subscribe?ref=video-cta`

---

## Step 2: Ensure Artifacts Are Import-Ready (~30min)

*Makes blog2video output consumable by LoreAI's import script (LoreAI Step 2).*

This is mostly a verification step — blog2video already produces the right artifacts. Just ensure consistency.

### 2a. Verify `meta.json` includes source URL

- **Check**: each output dir's `meta.json` should have `blog_url` field
- If missing in some runs, **edit**: `prompts/content-analyzer.md` to always emit `blog_url` in the plan
- The LoreAI import script needs this to link back to the original source

### 2b. Verify `video_plan.json` has structured concepts

- **Check**: `key_concepts[]` array should have `concept_en`, `concept_zh`, `analogy_direction` for each concept
- These feed directly into LoreAI's glossary and FAQ generation
- If older runs are missing these fields, no action needed — only future runs matter

### 2c. Keep `source_blog.md` in SCP delivery

- **Check**: current SCP cleanup rules in `CLAUDE.md` — `source_blog.md` IS included in delivery
- Confirm it's not being deleted pre-upload, as the LoreAI import script reads it

### Verify

1. After a `/blog2video` run, check output dir has: `video_plan.json` (with key_concepts), `meta.json` (with blog_url), `source_blog.md`, all `video_N_script.md` files
2. These are all the LoreAI import script needs

---

## Execution Summary

| Step | What | Depends on | ~Time |
|------|------|-----------|-------|
| 1 | CTA injection (prompt + slide + QR + bios) | Nothing | 2h |
| 2 | Verify artifacts are import-ready | Nothing | 30min |

**Total: ~2.5h, can be done in one session**

---

## What NOT to Change

- Don't add any LoreAI-specific code to blog2video — keep it a standalone pipeline
- Don't modify the SCP delivery flow — it works fine
- Don't auto-trigger LoreAI imports from blog2video — that's LoreAI's responsibility
- The only new dependency is a static QR code image file
