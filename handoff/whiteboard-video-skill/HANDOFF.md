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

## This is WF3 with the format pinned — reuse before you build

vfan already runs two pipelines that together *are* most of this. Don't reinvent them; survey first, then propose how this skill leans on them.

**The shape already exists — content-ops WF1 / WF3.** WF3 is `topic → deep research → author-review gate → produce & publish`; WF1 is `URL → 精读 → whiteboard → gate → render → package`, writing a central ledger. This skill is **WF3 with the output format pinned to the Sean whiteboard template** (topic → research → gate → *whiteboard video* instead of an article). Read these as the orchestration blueprint — the topic-front, the review gate, the ledger discipline are already solved:
- `/Users/yufanp/Desktop/Project/content-ops/.claude/commands/WF3.md`
- `/Users/yufanp/Desktop/Project/content-ops/.claude/commands/WF1.md`

**The render layer already exists — blog2video is a template library, not a single renderer.** `/Users/yufanp/Desktop/Project/blog2video` is a **library of per-format video templates** (`.claude/skills/`) on a shared **HyperFrames** animation engine + **Remotion** render + a wired-up **TTS**. Existing templates: `faceless-explainer`, `website-to-video`, `product-launch-video`, `slideshow`, `talking-head-recut`, `motion-graphics`, … The **nearest neighbor is `faceless-explainer`** — *"topic → faceless explainer where every visual is invented (typography, diagrams, data-viz)"*. Sean's hand-drawn *"learn X in N min"* whiteboard is essentially **a new template in the same family** (longer-form, single Excalidraw canvas, whiteboard visual system). Reuse blog2video's engine + TTS — do **not** stand up a fresh vault-local Remotion+TTS stack.

**Template selection is already a solved pattern — you're adding one template, not building a menu.** blog2video already routes between formats via `/hyperframes` + each template's own routing rules (*"not a product launch? use faceless-explainer; a real site? use website-to-video"*). The new whiteboard template just **registers into that router and declares when it's the right pick.** That covers both entry modes vfan wants — design for both:
1. **Format baked into the ask** — *"explain X in 12 min"* routes straight to the whiteboard template.
2. **Research first, then choose** — WF3-style topic research runs; at render time the author picks a template from the menu (whiteboard-12min / faceless-explainer / slideshow / …).

**The one big open decision — propose, don't assume:** since the render + orchestration both live in *other repos*, is this even a vault skill? Or is the real build **"a whiteboard template added inside blog2video + a WF3-style topic-front in content-ops"**, with this vault holding only the Sean reference + the Excalidraw whiteboard authoring? Look at all three repos, then propose where each piece lives and how you'd reach across them. The Obsidian side still owns: the **reference** (`references/sean-whiteboard-explainer/`), the **research stash** (`/Users/yufanp/Desktop/Project/obsidian-vault-starter/research/`), and Excalidraw whiteboard authoring.

**Cross-repo map (real paths on vfan's Mac — you need read access to all three):**

| asset | path | what to reuse |
|---|---|---|
| this vault (where you run) | `…/Desktop/Project/obsidian-vault-starter` | reference, research stash, `excalidraw-diagram` skill |
| blog2video (engine + template library) | `…/Desktop/Project/blog2video` | HyperFrames + Remotion render, TTS, `faceless-explainer` as the template pattern |
| content-ops (orchestration) | `…/Desktop/Project/content-ops` | WF1/WF3 as the `topic→research→gate→render→ledger` blueprint |

## Decisions left to Fable 5 (propose, don't guess silently)

- **TTS provider** for step 4 — but blog2video already has a wired-up TTS (see reuse section above); prefer reusing it, and only propose an alternative with the API-key/cost reason.
- **Renderer** for step 5 — blog2video already runs **Remotion under HyperFrames**; reuse that engine for timed pan/zoom over the Excalidraw export rather than a vault-local Remotion stack. Confirm the seam, don't rebuild it.
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
