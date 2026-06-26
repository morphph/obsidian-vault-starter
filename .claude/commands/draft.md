---
name: draft
description: "Use this skill whenever the user wants to graduate wiki/raw content into a publication-ready article. Triggers: 'draft an article about X', 'turn this wiki page into a post', 'write a draft from this raw source', 'I want to publish about Y', 'graduate this to drafts', '把这个写成一篇文章'. Use even if the user hasn't explicitly said 'draft' — when they ask for a 'post', 'article', 'blog', or want something 'publish-ready'. **Don't use when** the user wants to add a raw source to the wiki — use `/ingest`."
---

# Draft — Create Article Draft

Read CLAUDE.md first for wiki conventions.

## Arguments
Parse `$ARGUMENTS` for one of:
- **Research workspace** (e.g., `/draft research/openai-codex/` or `.../outline.md`) — build article from a `/research` run (report + outline + candidates)
- **Wiki page path** (e.g., `/draft wiki/context-noise-governance.md`) — graduate a wiki page
- **Raw file path** (e.g., `/draft raw/2026-04-09-bcherny-claude-code-best-practices.md`) — build article from source
- **Topic** (e.g., `/draft Claude Code best practices`) — find relevant raw/ sources and build article

If no argument given, ask the user what to draft.

## Workflow

### 1. Gather source material

**If research workspace:** Read `report.md` + `outline.md` + `ingest-candidates.md` from the
`research/<slug>/` dir. The `outline.md` is the article skeleton — follow it. The `report.md`
supplies the facts (Track A) and the winning angle (Track B). Also read `audience-profile.md`
(repo root) for voice + GEO rules. **Sourcing follows the 务实 rule** — see step 4.
**If wiki page:** Read the wiki page + all files in its `sources:` frontmatter.
**If raw file:** Read the raw file. Check wiki/ for related pages that add context.
**If topic:** Search raw/ and wiki/ for relevant files. Show what you found, ask user to confirm.

### 2. Detect page type and choose article structure

Analyze the content and classify it:

**Narrative / Analytical** (has a thesis, argues a point, connects ideas):
→ Article structure: Hook → Thesis → Evidence/Argument → Implications → Takeaway

**Guide / Reference** (how-to, list of practices, configurations):
→ Article structure: Hook → Why this matters → The practices (reorganized for reading flow) → Quick-start summary

**Entity / Profile** (about a person, company, product):
→ Article structure: Hook → What they did → Why it matters → What to watch

### 3. Show the user a brief plan

Before creating the draft, show:
- Detected type and chosen structure
- Proposed article angle/hook (1 sentence)
- Source files being used
- What will be cut vs kept (if from wiki page)

Ask for confirmation or adjustments.

### 4. Create the draft article

Create `drafts/{descriptive-kebab-case-name}.md` with:

**Frontmatter:**
```yaml
---
status: draft
sources:
  - raw/{source-file-1}.md
  - raw/{source-file-2}.md
external-refs:        # only when drafting from a research workspace; else omit
  - https://example.com/un-ingested-source
research: research/{slug}/   # only when drafting from a research workspace; else omit
platform: blog
created: {today YYYY-MM-DD}
last-updated: {today YYYY-MM-DD}
tags: [draft]
---
```

The `sources:` field **always points to raw/ files** — the immutable source material.

**Sourcing rule when drafting from a research workspace (务实 / pragmatic):**
- `sources:` = only the candidates that have **already been ingested into `raw/`**. Check each
  `ingest-candidates.md` entry: does a `raw/` file exist for that URL/title? If yes → it's a
  source; if no → it goes in `external-refs:`.
- `external-refs:` = the URLs the draft references that are **not yet in `raw/`**.
- `research:` = pointer back to the `research/<slug>/` workspace.
- **Load-bearing claims must be backed by a `raw/` (ingested) source.** `external-refs` are only
  for supporting / color. If a key claim the article leans on has no `raw/` backing, **flag it**
  and tell the user: "claim X 依赖未 ingest 的源 <URL> — 建议先 `/ingest` 它再定稿。" Don't silently
  ship a load-bearing claim that can't trace to raw/.

**Content transformation:**
- Convert `[[wikilinks]]` to plain text (remove brackets) — reader doesn't have your wiki
- Remove `## Source Log` table — not for readers
- Remove `## Connections` section — internal wiki navigation
- Remove wiki-specific frontmatter references
- Add `<!-- HOOK: [placeholder for opening hook] -->` at the top of the body
- Add `<!-- CTA: [placeholder for closing call-to-action] -->` at the bottom
- Restructure sections according to the detected article type
- Keep the substance — don't water down the content, just reshape it for a reader who doesn't have your wiki context
- Preserve the original language (Chinese stays Chinese, English stays English, mixing is fine)

### 5. Offer companion visual (long-form + diagrammable content)

If the draft is long-form (>2000 words) **and** contains diagrammable structure (architecture, layered framework, workflow with stages, comparison matrix), offer to generate a companion visual:

- Run `/visualize <topic>` to produce `drafts/{name}.excalidraw` + `drafts/{name}.png`
- Embed the PNG in the article body with `![[{name}.png]]` near the relevant section — embed the PNG, NOT the `.excalidraw` (per `feedback_visualize_embed` memory)
- Keep both files in `drafts/` so the user can iterate the Excalidraw and re-export

Skip silently if the draft is short or purely narrative with no diagrammable structure. When unsure, ask the user — visuals take real time and don't fit every draft.

Evidence this step pays off: `managed-agents-architecture`, `connection-context-layers-and-best-practices`, and `claude-code-best-practices-guide` all carry companion visuals because the underlying material is structural.

### 6. Update wiki page (only if source was a wiki page)

Add `status: draft` to the wiki page's frontmatter. Do NOT change any other content.

Skip this step if the draft was built directly from raw/, a topic, or a research workspace.

### 7. Report

Show in terminal:
- Source(s) → Draft article (paths)
- Detected type
- Article structure chosen
- Companion visual: path if generated, else "none"
- What to do next: "Open `drafts/{filename}` and polish."
