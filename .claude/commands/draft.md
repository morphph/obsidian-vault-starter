---
name: draft
description: "Create a draft article from wiki page or raw sources. Usage: /draft <wiki-page|raw-file|topic>"
---

# Draft — Create Article Draft

Read CLAUDE.md first for wiki conventions.

## Arguments
Parse `$ARGUMENTS` for one of:
- **Wiki page path** (e.g., `/draft wiki/context-noise-governance.md`) — graduate a wiki page
- **Raw file path** (e.g., `/draft raw/2026-04-09-bcherny-claude-code-best-practices.md`) — build article from source
- **Topic** (e.g., `/draft Claude Code best practices`) — find relevant raw/ sources and build article

If no argument given, ask the user what to draft.

## Workflow

### 1. Gather source material

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
platform: blog
created: {today YYYY-MM-DD}
last-updated: {today YYYY-MM-DD}
tags: [draft]
---
```

The `sources:` field always points to raw/ files — the immutable source material.

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

### 5. Update wiki page (only if source was a wiki page)

Add `status: draft` to the wiki page's frontmatter. Do NOT change any other content.

Skip this step if the draft was built directly from raw/ or a topic.

### 6. Report

Show in terminal:
- Source(s) → Draft article (paths)
- Detected type
- Article structure chosen
- What to do next: "Open `drafts/{filename}` and polish."
