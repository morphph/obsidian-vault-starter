---
type: concept
created: 2026-05-09
last-updated: 2026-05-09
sources:
  - raw/2026-05-08-thariq-unreasonable-effectiveness-of-html.md
tags: [wiki, principle, agentic, ui, workflow]
---

# Throwaway Editors

## Summary
[[thariq|Thariq]]'s name for **single-purpose HTML files purpose-built for one piece of data**. Not products, not reusable tools — disposable UIs for the exact task in front of you, **always ending with a `Copy as JSON` / `Copy as prompt` button** that turns the user's edits back into something pasteable into Claude Code. Solves the "hard to describe what you want purely in a text box" problem. Anti-product ergonomics: the editor's job is to capture intent, not to be deployed.

## Details

### The pattern in one sentence
> When the task input is hard to express as text, ask Claude to build you a throwaway editor for it. End with an export button. Use the export, throw away the editor.

### The shape of a throwaway editor

```
[Single HTML file]
  ├─ UI tuned to this exact dataset (drag-drop / sliders / forms / annotations)
  ├─ Pre-populated with Claude's best guess
  ├─ Manipulation primitives appropriate to the data shape
  └─ Export button: copy-as-JSON / copy-as-prompt / copy-as-diff / copy-as-markdown
```

### Thariq's three example prompts (verbatim from the article)

**(1) Reordering 30 tickets**
> "I need to reprioritize these 30 Linear tickets. Make me an HTML file with each ticket as a draggable card across Now / Next / Later / Cut columns. Pre-sort them by your best guess. Add a 'copy as markdown' button that exports the final ordering with a one-line rationale per bucket."

**(2) Editing feature flag config**
> "Here's our feature flag config. Build a form-based editor for it, group flags by area, show dependencies between them, warn me if I enable a flag whose prerequisite is off. Add a 'copy diff' button that gives me just the changed keys."

**(3) Tuning a system prompt**
> "I'm tuning this system prompt. Make a side-by-side editor: editable prompt on the left with the variable slots highlighted, three sample inputs on the right that re-render the filled template live. Add a character/token counter and a copy button."

### The genres of "data shapes that resist text"

| Data shape | Throwaway editor pattern |
|------------|--------------------------|
| Ranked / bucketed items | Drag-drop cards across columns, copy-as-ordering |
| Constrained config (deps, prereqs) | Form with live validation + dependency warnings |
| Prompts with variable slots | Side-by-side editor with live template render |
| Datasets needing approve/reject | List of rows with toggle buttons + tagged export |
| Continuous-value tuning | Sliders / knobs with copy-as-parameters |
| Annotation tasks | Document with inline marker UI + structured export |
| Time/space pickers | Visual cron / region / curve editors |

### Why this isn't a "build a tool" task
**Throwaway = anti-product.** The cost of building a real tool: design, deploy, document, maintain. Cost of a throwaway: one prompt, one HTML file, no version control. **You only pay the cost when the task is in front of you, and only for this task.**

The breakeven shifts dramatically with Claude Code in the loop:
- Old breakeven: tool worth building if you'll use it 10+ times
- New breakeven: editor worth building if it makes *one* task significantly easier and the prompt costs < 5 minutes

### Why the export button is the load-bearing primitive
Without the export, you have a UI but no way to feed the user's intent back into the loop. **The export button is what makes the editor agent-compatible.** It turns rich UI manipulation into pasteable text — a structured prompt for the next Claude Code run.

This is the [[skill-as-method-call]] principle applied to UI: parameters in (the data), method body (the editor), parameters out (the export). Same shape, different surface.

### Anti-pattern: trying to make it reusable
> "Not a product, or a reusable tool, but a single HTML file, purpose-built for this one piece of data."

Once you start generalizing the throwaway, you've turned a 5-minute prompt into a 5-day project. The right move: when you find yourself rebuilding the same throwaway editor three times, **then** consider whether it deserves to be a [[skill-as-method-call|skill]] or a real product.

### How this fits this vault

- The closest existing pattern is `/visualize` (generates Excalidraw diagrams). Excalidraw is editable but not data-driven.
- A throwaway-editor pattern would suit:
  - **Wiki entry triage** — an HTML editor for "here are 30 raw/ files, drag them into the right wiki category, copy-as-ingest-plan"
  - **Draft tone tuning** — a side-by-side draft editor with voice-match slider that exports a tuned prompt
  - **Lint-result triage** — drag findings into Fix-Now / Schedule / Ignore columns, copy-as-action-plan
- These would extend `/visualize` without becoming a new slash command — just an option Claude offers in context.

### Connection to Khairallah's [[3-agent-starter-team]]
The Operations Agent's email triage workflow is *almost* a throwaway editor for one's inbox: categorize → flag → draft → review. The difference is persistence: an Operations Agent runs daily, a throwaway editor is one-shot. **They're the same UI shape with different lifetimes.**

## Connections
- Related: [[thariq]], [[html-as-output-format]], [[claude-code]], [[skill-as-method-call]], [[3-agent-starter-team]], [[diarization]], [[two-pipeline-architecture]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-05-09 | raw/2026-05-08-thariq-unreasonable-effectiveness-of-html.md | Initial creation |
