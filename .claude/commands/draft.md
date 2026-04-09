---
name: draft
description: "Graduate a wiki page to a draft article. Usage: /draft <wiki-page-path>"
---

# Draft — Graduate Wiki Page to Article

Read CLAUDE.md first for wiki conventions.

## Arguments
Parse `$ARGUMENTS` for a wiki page path (e.g., `/draft wiki/connection-context-layers-and-best-practices.md`).

If no argument given, ask the user which wiki page to draft.

## Workflow

### 1. Read the wiki page

Read the specified wiki page. Also read all files listed in its `sources:` frontmatter to understand the full source material.

### 2. Detect page type and choose article structure

Analyze the wiki page content and classify it:

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
- What will be cut vs kept from the wiki version

Ask for confirmation or adjustments.

### 4. Create the draft article

Create `drafts/{same-filename-as-wiki-page}.md` with:

**Frontmatter:**
```yaml
---
status: draft
source-wiki: wiki/{filename}
platform: blog
created: {today YYYY-MM-DD}
last-updated: {today YYYY-MM-DD}
tags: [draft]
---
```

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

### 5. Update the wiki page

Add `status: draft` to the wiki page's frontmatter. Do NOT change any other content in the wiki page.

### 6. Report

Show in terminal:
- Wiki page → Draft article (paths)
- Detected type
- Article structure chosen
- What to do next: "Open `drafts/{filename}` and polish. The wiki page is unchanged and tagged `status: draft`."
