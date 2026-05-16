---
type: concept
created: 2026-05-16
last-updated: 2026-05-16
sources:
  - raw/2026-05-13-anthropic-computer-and-browser-use-best-practices.md
tags: [wiki, principle, agentic, teaching, ui-automation, computer-use]
---

# Demonstration-Based Teaching

## Summary
Anthropic's name for a workflow-teaching pattern that complements natural-language prompts: **record one demonstration with screenshots + annotated click positions, then let the model adapt at playback.** Unlike record-and-replay automation (RPA / Selenium scripts), Claude doesn't blindly replay coordinates — it **adapts the recorded sequence to the current UI state**. Robust to layout changes, resolution differences, minor element repositioning. The natural sibling to [[skill-as-method-call|skills]] for tasks that are visual and hard to describe in pure text.

## Details

### The data model (per step)
A demonstration captures:
- **Action type** — click / type / navigate / scroll / select
- **Human-readable description** — what the user was doing ("click Save")
- **CSS selector + coordinates** — both, because selectors can break and coordinates can drift
- **Screenshot with visual annotation** — the visual proof of context
- **Viewport dimensions** — so the model can re-locate elements at different sizes
- **Optional voice narration** — for intent that's hard to encode visually

### The adaptation principle (why this beats RPA)
Traditional record-and-replay automation:
- ❌ Coordinates drift → click on wrong element
- ❌ Layout shift → click on empty space
- ❌ Resolution mismatch → off-by-many pixels
- ❌ Element moves → script breaks

Demonstration-based teaching:
- ✅ Coordinates are *hints*, not commands
- ✅ Model re-identifies the target element on each playback via description + selector + visual context
- ✅ Adapts to UI variance by understanding *what* the user was doing, not *where* on the screen

This is the same evolution as: **natural-language instructions > regex scripts**. The script tells the computer how; the demonstration tells the model what — and the model figures out how on the day.

### When this beats writing a prompt
- **Visual tasks**: "click the third filter chip in the second row" — much easier to record than to describe
- **Long sequences**: "do these 20 steps in this app" — recording is faster than writing
- **Apps with quirks**: any workflow where the user knows non-obvious shortcuts
- **Cross-team handoff**: a non-engineer can record; a developer can wrap it in a [[skill-as-method-call|skill]]

### When this is the wrong tool
- One-shot tasks (recording overhead > benefit)
- Workflows that depend on dynamic external data (record once, the data is wrong tomorrow)
- High-stakes actions (demonstrations don't inherently force human-in-the-loop)
- Cross-app workflows that don't share viewport conventions

### Position in the agent-skill stack

| Layer | Form | Example |
|-------|------|---------|
| Strategic intent | Natural-language prompt | "Find me the cheapest flight to Tokyo" |
| **Procedural shape** | **Demonstration recording** | **Record: click "flights", type origin, type destination, sort by price** |
| Tactical execution | [[computer-and-browser-use|Computer-use API]] | Click coordinates, parse screenshot, return result |

A demonstration sits exactly between intent and execution. **It's a skill in visual form.** This is why it composes naturally with [[skillify-meta-skill|/skillify]]: a demonstration recorded once is the seed for a skill that codifies the workflow.

### How this relates to existing wiki concepts
- **[[skill-as-method-call]]** — A demonstration is a skill whose body is a visual sequence instead of a markdown procedure. Same calling convention (parameters in, result out).
- **[[computer-and-browser-use]]** — The execution layer beneath a demonstration. Demonstrations *call* the computer-use API.
- **[[diarization]]** — Both patterns share: distill messy human experience into a structured artifact the model can reliably consume.
- **[[ralph-wiggum]]** — A demonstration can be the loop's `PRD.md` input — what to do, with visual fidelity.
- **[[skillify-meta-skill]]** — A recorded demonstration is a strong candidate to skillify ("you did this manually once, here's the skill").

### Practical workflow
1. Use a recorder (browser extension or app) to capture screen + clicks + narration
2. The recorder produces a structured JSON/Markdown file with the per-step data model
3. Hand to Claude with computer-use enabled and the task description
4. On playback, Claude reads the recording, looks at the *current* screenshot, decides what to click based on the recorded intent + current visual context

### Open questions / what the post doesn't answer
- How does the model handle steps where the UI is genuinely different (e.g., a new modal appeared)? Likely combines recording + general-purpose visual reasoning, but the post doesn't say.
- Pricing relative to plain prompt-driven computer-use — not stated.
- Whether demonstrations carry across model upgrades (Sonnet 4.6 → Opus 4.7) — assume yes, but unstated.

## Connections
- Related: [[computer-and-browser-use]], [[claude-opus-4-7]], [[skill-as-method-call]], [[skillify-meta-skill]], [[diarization]], [[ralph-wiggum]], [[verification-loops]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-05-16 | raw/2026-05-13-anthropic-computer-and-browser-use-best-practices.md | Initial creation — extracted from "Teaching Claude via Demonstrations" section |
