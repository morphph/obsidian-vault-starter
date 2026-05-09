---
type: concept
created: 2026-05-09
last-updated: 2026-05-09
sources:
  - raw/2026-05-08-thariq-unreasonable-effectiveness-of-html.md
tags: [wiki, principle, agentic, output-format, claude-code]
---

# HTML as Output Format

## Summary
[[thariq|Thariq]] (Claude Code team) argues that **HTML, not Markdown, is the right primary output format for modern agents** — for specs, plans, code reviews, reports, and any other artifact a human reads but doesn't edit. Headline insights: (a) **the 100-line markdown threshold** beyond which people stop reading; (b) the 1M-token Opus 4.7 context window makes HTML's 2-4× token cost negligible; (c) HTML's information density (CSS / SVG / tables / interactive JS) beats markdown for everything richer than a paragraph; (d) **"I feel more in the loop"** — output format as agent governance.

## Details

### The core argument
Markdown was correct when:
- Humans edited the agent's output
- Outputs were short
- Browsers didn't render markdown natively

In 2026 these have all flipped:
- "I'm increasingly **not editing these files myself, but using them as specs, reference files, brainstorming outputs**. When I do edit, I'm prompting Claude to edit them."
- Agent outputs routinely exceed 100 lines
- Sharing markdown still requires attachments; HTML is link-shareable

So the right format is now what the human consumes best, not what the human edits easiest. **That's HTML.**

### What HTML gives you that markdown can't

| Need | Markdown | HTML |
|------|----------|------|
| Tables | Crude pipe-tables | Rich tables with sorting, alignment, merged cells |
| Color | Estimated with unicode characters (yes, really — Thariq's article shows this) | CSS, instantly |
| Diagrams | ASCII art | SVG with text, geometry, gradients |
| Code | Code blocks | Code blocks + annotations + diff rendering + syntax highlighting |
| Layout | Linear top-to-bottom | Tabs, columns, mobile-responsive, sidebars |
| Interaction | None | Sliders, knobs, drag-drop, copy-buttons |
| Sharing | Attachment | Open the link |

**Thariq's claim:** "There is almost no set of information that Claude can read that you cannot fairly efficiently represent with HTML."

### The "100-line threshold" — why long markdown plans go unread
> "In practice, I've found I tend to not actually read more than a 100-line markdown file, and I certainly am not able to get anyone else in my organization to read it."

This is the silent failure of modern agent outputs: the plan gets written, the model thinks it's done its job, but nobody reads it past line 100. **HTML changes the per-line cost of reading**, making longer documents tolerable.

### Why this is "agent governance," not just formatting
> "The real reason I use HTML is that I feel much more in the loop with Claude. I had begun to fear that because I had stopped reading plans in depth I would simply have to leave Claude to make its choices."

The output format is what determines whether you stay in the loop. Markdown longform → skim → trust. HTML longform → actually read → catch issues → guide. Same agent, same model, same task — different oversight cost. **Output format is a [[resolvers|resolver]]-class governance choice**, not a stylistic one.

### Token economics
- HTML output: 2-4× more tokens than markdown
- HTML generation: 2-4× longer wall-clock time
- **But:** with 1M-token context windows ([[claude-opus-4-7]]), the extra tokens don't crowd the working set
- Net trade: pay 2-4× more compute to recover oversight bandwidth that was lost to skim-the-markdown

### When NOT to use HTML
- **Files Claude edits frequently** — diffs are noisy, hard to review
- **Files under version control as the primary artifact** — same diff problem
- **Data interchange between agents** — JSON/YAML still right
- **Quick chat replies** — overhead not worth it

### Don't make it a /html skill (yet)
Thariq explicitly: "I want to emphasize that you don't need to do much to get Claude to do this. **You can just ask it to 'make a HTML file' or 'make a HTML artifact'.** The trick is knowing what you want the artifact to do."

The reason: each HTML artifact is shaped by the *use case* (spec / review / playground / editor). A premature `/html` skill would standardize the wrong dimension. Better to prompt freeform until enough patterns emerge to deserve a skill.

### Five canonical use cases

1. **Specs / Planning / Exploration** — "Generate 6 distinctly different approaches and lay them out as a single HTML file in a grid so I can compare them side by side."
2. **Code Review & Understanding** — "Render the actual diff with inline margin annotations, color-code findings by severity." (Thariq attaches a HTML code explainer to every PR.)
3. **Design & Prototypes** — Sliders / knobs / copy-as-parameters. "Claude Design is based on HTML."
4. **Reports / Research / Learning** — "Single HTML explainer page: token-bucket flow diagram, 3-4 key code snippets annotated, gotchas section. Optimized for someone reading it once."
5. **[[throwaway-editors|Custom Editing Interfaces]]** — single-purpose HTML files for one piece of data with a copy-as-JSON/prompt export.

### Concrete prompt patterns
- "Create a [thing] as an HTML file. Use SVG for [diagram]. Include [interactive element]. Optimize for someone reading it once."
- "Compare N options side-by-side in a grid."
- "Add sliders to tune [parameter]. Include a copy button that gives me the parameters that worked well."
- "Render the diff with inline annotations color-coded by severity."

### How this fits this vault's existing concepts

- **[[diarization]]** — Garry's "model reads everything → one structured page profile" benefits massively from HTML. The structured page should *be* an HTML page.
- **[[blog2video]] / [[loreai]]** — These are content-pipeline projects. Output rendering is currently text-first. Thariq's pattern argues for HTML as the intermediate (and possibly final) artifact.
- **[[3-agent-starter-team]]** — Khairallah's research-agent brief is described as one-page; HTML is the natural form factor for the "weekly briefing in your inbox" pattern.
- **`/draft` in this vault** — currently produces markdown drafts in `drafts/`. Worth considering an HTML-output mode for shareable preview drafts.
- **`/visualize`** — already produces Excalidraw JSON. HTML+SVG is a less specialized but more shareable alternative for some diagrams.

### Counterargument the article doesn't address
HTML has a **diff-readability tax** that does matter when the artifact is also under git review (as in this wiki). Markdown wikilinks are reviewable; HTML diffs are noisy. The pattern most defensible here is: **HTML for one-shot artifacts (specs, briefs, reports), Markdown for evolving collaborative documents** (this wiki, the drafts folder before publication).

## Connections
- Related: [[thariq]], [[throwaway-editors]], [[claude-code]], [[claude-opus-4-7]], [[diarization]], [[blog2video]], [[loreai]], [[resolvers]], [[3-agent-starter-team]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-05-09 | raw/2026-05-08-thariq-unreasonable-effectiveness-of-html.md | Initial creation |
