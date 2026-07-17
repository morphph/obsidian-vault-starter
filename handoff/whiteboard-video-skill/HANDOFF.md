# Handoff — build a "topic → whiteboard explainer video" skill

**For:** Fable 5 (`claude-fable-5`), running as a coding agent in this repo.
**From:** a working session between vfan and Claude (Opus 4.8).
**Deliverable Fable 5 should produce:** a Claude Code skill that turns a topic into a
Sean-style whiteboard explainer video (script + captions + audio + rendered video).

This file is **context** — the why and the what. The actual build instruction is
`BUILD-PROMPT.md` (paste that into Fable 5). Read this first for background.

---

## Who this is for

vfan — solo AI-content builder in Singapore, growth marketer, bilingual (EN/ZH).
Runs a content pipeline (projects: **LoreAI**, **blog2video / AI精读**). Wants to
**mass-produce short explainer videos** in a proven format: *"You Can Learn X in N
Minutes"* — a whole system explained from simple building blocks on a hand-drawn
whiteboard, non-technical-friendly. Example topic: *"Learn Claude Code & Agentic
Coding in 12 Minutes."*

## Where this came from

vfan was collecting **references** to create content from. One reference — a Sean's
AI Stories video — he captured in two complementary halves:
1. the **transcript** (what's said), and
2. a **visual-style-prompt** (a reverse-engineered spec of how it *looks*).

That pairing — content + reproducible visual style — is the seed. The skill should
take those two halves as the *style target* and generate brand-new videos on any topic
in the same mold.

## The vision — what the skill does

One command, one topic, this pipeline:

```
topic
  │
  1. RESEARCH   ── deep, thorough investigation of the topic (facts, structure, the
  │                 "simple building blocks" that make it teachable)
  │
  2. SCRIPT     ── narration written in Sean's voice/structure (see reference),
  │                 in the "learn X in N min" format → also yields transcript + captions
  │
  3. WHITEBOARD ── a single Excalidraw canvas (hand-drawn, the reference's color system)
  │                 that the narration walks across
  │
  ├──────────────► REVIEW GATE ◄─── vfan reviews narration + whiteboard together.
  │                                  Nothing expensive runs until he approves.
  │
  4. AUDIO      ── TTS of the narration
  │
  5. RENDER     ── final video: whiteboard pan/zoom timed to the audio, captions burned in
  ▼
outputs: transcript · captions · audio · rendered video
```

**The review gate is the load-bearing design decision.** Audio + render are slow and
costly; vfan wants to see and approve the *narration + whiteboard* before the pipeline
spends anything on them. Build the skill so it stops there and waits.

## Decisions already made

- **Style target = one reference**, in `references/sean-whiteboard-explainer/` (see its `note.md`). Reproduce the whiteboard + narration + captions; the webcam/face is out of scope.
- **Format = "learn X in N min"** — the title/framing convention, system-from-simple-blocks, non-technical-friendly.
- **Review gate after step 3**, before audio/render.
- **House style for the build prompt** mirrors `prompts/fable5-pipeline-audit-prompt.md` (context/intent → where to read → invariants → task → working style → boundaries → deliverable shape → communication style).

## Decisions left to Fable 5 (propose, don't guess silently)

- **TTS provider** for step 4 (ElevenLabs / OpenAI / other) — flag the API-key/cost implication.
- **Renderer** for step 5 — this repo has a **Remotion** skill (`remotion-best-practices`); Remotion (React video) is the natural fit for timed pan/zoom over an Excalidraw export, but Fable 5 should confirm and propose the approach.
- **Whiteboard generation** — this repo has an **`excalidraw-diagram`** skill that emits `.excalidraw` JSON; reuse it for step 3.
- **How research runs** — this repo already has a `/research` skill; decide whether to reuse it or run a lighter topic-research pass inside the skill.
- **Skill granularity** — one skill, or a skill that orchestrates a few scripts. Fable 5's call.

## What's in this folder

```
handoff/whiteboard-video-skill/
├── HANDOFF.md          ← you are here (context)
├── BUILD-PROMPT.md     ← paste THIS into Fable 5
└── references/
    └── sean-whiteboard-explainer/
        ├── note.md              ← how to use this reference (read first)
        ├── visual-style-prompt.md ← the visual DNA to reproduce
        ├── transcript.md        ← the narration voice/structure to emulate
        └── captions.srt         ← caption format reference
```

## Repo resources Fable 5 should know about

- `excalidraw-diagram` skill (`.claude/skills/excalidraw-diagram/`) — Excalidraw JSON generation.
- `remotion-best-practices` skill — Remotion video rendering.
- `/research` skill (`.claude/skills/research/`) — existing topic-research workflow.
- `yt-dlp` is installed (used to capture the reference; not needed by the skill itself).
- `CLAUDE.md` (repo root) — vault conventions; the skill is a new tool, document it per the "Documentation Layers" table (CLAUDE.md declares WHAT, the skill defines HOW).
