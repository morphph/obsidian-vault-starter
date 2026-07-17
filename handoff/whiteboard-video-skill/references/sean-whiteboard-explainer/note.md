---
title: Sean's AI Stories — whiteboard explainer (style reference)
source: https://www.youtube.com/watch?v=GrNbuWWJYiI
channel: Sean's AI Stories (@SeanAIStories)
role: STYLE TARGET for the whiteboard-video skill
---

# Style reference — Sean's AI Stories whiteboard explainer

This folder is the **single style target** the skill must reproduce. It is one real
video, reverse-engineered into its two reusable halves:

| File | What it captures | How the skill uses it |
|------|------------------|------------------------|
| `visual-style-prompt.md` | The video's **visual DNA** — layout, color system (with hex), diagram style, camera motion, pacing, thumbnail — packaged as a generation prompt | The blueprint for the whiteboard + final render. The output video should look like it was produced from this prompt. |
| `transcript.md` | The **narration style** — how Sean explains: one running example, plain-language analogies (horse/reins), "let me walk you through this" tone, ~150 wpm | The model for the generated script's *voice and structure* (not its content — content comes from the topic's research) |
| `captions.srt` | The **caption format** — timed, two-line, auto-caption cadence | Format reference for the skill's caption output |

## The essence to reproduce (don't lose these)

- **Single continuous Excalidraw canvas**, hand-drawn/sketchy style — not slides, not polished corporate graphics.
- **Color system**: red/orange handwritten section titles, orange dashed grouping borders, pink/coral central nodes (`#FFB3B3`), green input/output nodes (`#B2F2BB`), gray database cylinders, black arrows. Full palette in `visual-style-prompt.md`.
- **Zoom-and-pan** across one big diagram as each concept is explained; progressive reveal. No hard cuts.
- **Narration**: solo presenter, conversational-but-knowledgeable, one running concrete example throughout, analogies over jargon.
- **Format**: the "*You Can Learn X in N Min*" framing — a whole system built from simple blocks, non-technical-friendly.

## What is NOT part of the style target

The webcam picture-in-picture and the presenter's face are in the reference but are
**out of scope** for an automated pipeline — reproduce the whiteboard + narration + captions,
not a talking head. (If the skill later adds an avatar, that's a separate decision.)
