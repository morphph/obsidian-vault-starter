---
type: implementation-plan
project: "[[blog2video]]"
related: "[[LoreAI]]"
source: agent
date: 2026-03-10
status: in-progress
---

# blog2video: Integration Plan

Part of the [[LoreAI]] x [[blog2video]] content flywheel. This plan covers all changes in the `blog2video` repo.

## Architecture Overview

```
Local Mac: blog2video renders video
  → SCP to VPS: /home/ubuntu/blog2video/queue/<slug>/
  → Claudiny (same VPS): detects new delivery, reads flow_source from meta.json,
    notifies vfan, logs to publish-log.json when published
  → LoreAI cron (same VPS, 11:50pm SGT): scans queue/ for unimported dirs,
    runs import-video-blog.ts → blog posts + glossary + FAQ → git push → Vercel rebuild
```

**Key field**: `flow_source` in `meta.json`:
- `"manual-curate"` — default, vfan found the content manually
- `"loreai-picker"` — LoreAI's video candidate picker selected it

Claudiny reads `flow_source` on arrival, shows it in notifications, and logs it to `/home/ubuntu/blog2video/publish-log.json`.

**Artifacts LoreAI needs from each output dir**:
- `meta.json` — must have `blog_url` and `flow_source`
- `source_blog.md` — cleaned English source (for EN blog post generation)
- `video_X_script.md` — Chinese narration scripts (for ZH blog post generation)
- `video_plan.json` — `key_concepts[]` array with `concept_en`, `concept_zh`, `analogy_direction` (for glossary/FAQ)

---

## What's Been Implemented

### Step 1: CTA Injection — check current status

The plan called for:

| Task | What | Status |
|------|------|--------|
| 1a | Verbal CTA in script-writer prompt: "搜 loreai.dev，订阅每日 AI 精读日报" | Check `prompts/script-writer.md` |
| 1b | CTA slide Remotion component (`blog2video-remotion/src/slides/CtaSlide.tsx`) | Check if created |
| 1b | Register in `BlogVideo.tsx` + `types.ts` | Check if `cta` type exists |
| 1c | QR code at `blog2video-remotion/public/qr-subscribe-zh.png` | Check if file exists |
| 1d | XHS/WeChat bio updated | Manual — ask vfan |

**Expected behavior after CTA implementation**:
- Every `/blog2video` run produces a script ending with loreai.dev verbal CTA
- Rendered video has CTA slide as final slide with QR code
- QR code → `loreai.dev/zh/subscribe?ref=video-cta`

**If debugging CTA slide**:
- Slide not appearing? Check `BlogVideo.tsx` registers `CtaSlide` component for type `'cta'`
- QR not rendering? Check `blog2video-remotion/public/qr-subscribe-zh.png` exists
- Verbal CTA missing? Check `prompts/script-writer.md` outro section

### Step 2: `flow_source` in meta.json

- `meta.json` should include `"flow_source": "manual-curate"` by default
- Check wherever `meta.json` is generated — likely in the content-analyzer stage or the orchestrator command

**If debugging**:
- `flow_source` missing from meta.json? Check `prompts/content-analyzer.md` or the orchestration in `.claude/commands/blog2video.md`
- Existing 8 videos in queue don't have `flow_source` — Claudiny will ask vfan when they come up for publishing

### Artifact consistency check

After any `/blog2video` run, the output dir should have:

```
<slug>/
  meta.json              ← must have: blog_url, flow_source, topic, videos[]
  source_blog.md         ← cleaned English markdown (required for LoreAI EN blog)
  video_plan.json        ← must have: key_concepts[] with concept_en, concept_zh, analogy_direction
  video_1_script.md      ← Chinese narration (required for LoreAI ZH blog)
  video_1_audio.vtt      ← subtitles
  video_1.mp4            ← video file (gitignored, not needed by LoreAI)
  cover_photo.png        ← thumbnail
  slide_N.png            ← slide screenshots
```

**If LoreAI import fails**:
- Missing `video_plan.json` → import aborts. Check content-analyzer stage completed.
- Missing `source_blog.md` → import falls back to generating EN from ZH. Check Step 0 preprocessing.
- Missing `video_X_script.md` → import aborts. Check script-writer stage completed.
- `key_concepts[]` empty or missing fields → glossary/FAQ generation skipped but import continues.

---

## E2E Test Reference

See `agent-output/integration-e2e-test.md` in the obsidian vault for the full checklist. Key tests for blog2video:

1. Run `/blog2video` on a test URL
2. Check script ends with verbal CTA mentioning loreai.dev
3. Check rendered video has CTA slide with QR as final slide
4. Scan QR → opens `loreai.dev/zh/subscribe?ref=video-cta`
5. Check `meta.json` has `"flow_source": "manual-curate"`
6. Check output dir has all required artifacts (meta.json, source_blog.md, video_plan.json, scripts)
7. SCP to VPS → Claudiny detects and shows `flow_source` in notification

---

## Troubleshooting

| Symptom | Likely cause | Where to look |
|---------|-------------|---------------|
| No CTA slide in video | Component not registered | `blog2video-remotion/src/BlogVideo.tsx` — check `cta` in slide map |
| QR code blank/missing | Image file missing | `blog2video-remotion/public/qr-subscribe-zh.png` exists? |
| Verbal CTA missing from script | Prompt not updated | `prompts/script-writer.md` — check outro section |
| `flow_source` missing from meta.json | Not added to generation | Check where meta.json is written — content-analyzer or orchestrator |
| `source_blog.md` missing from SCP | Cleaned up before upload | Check SCP cleanup rules in `CLAUDE.md` post-render delivery section |
| `key_concepts` empty | Content-analyzer didn't extract | Check `prompts/content-analyzer.md` — must require key_concepts output |
| LoreAI import fails | Missing artifacts | Run: `ls <output-dir>/` and check for video_plan.json, source_blog.md, video_X_script.md |
| CTA slide too long/short | Duration config | Check `CtaSlide.tsx` duration prop, should be ~8-10 seconds |

---

## What NOT to Change

- Don't add any LoreAI-specific code to blog2video — keep it a standalone pipeline
- Don't modify the SCP delivery flow — it works fine
- Don't auto-trigger LoreAI imports from blog2video — LoreAI's cron handles that
- The only cross-repo dependencies are: QR code URL and `meta.json` field names
