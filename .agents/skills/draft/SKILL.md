---
name: draft
description: Write a publication-ready article from a selected topic brief, outline, research report, or explicit author direction. Use when the user asks to draft, write, or turn researched material into an article, blog post, essay, guide, or publishable piece. Prefer an approved topic workspace containing topic-brief.md and outline.md; use research evidence without repeating the report's structure. Produces one article under drafts/. Do not use to investigate the subject; use /research. Do not use to study competitors or choose the editorial angle; use /topic.
---

# Draft — Write the Article

Read `AGENTS.md` before working in this repository.

Turn a chosen editorial position and its evidence into a strong article. Preserve the author's
take, serve the stated reader, and write a narrative that stands on its own outside the vault.

This version writes articles only. Do not create podcast, video, social-thread, or publication
automation artifacts.

## Inputs

Prefer, in order:

1. a `/topic` workspace with `topic-brief.md` and `outline.md`;
2. an explicit topic brief or outline plus its research workspace;
3. a research workspace plus a user-selected thesis;
4. direct author instructions and source material.

Also read:

- the linked `/research` `report.md` and `source-ledger.md`;
- original sources required by load-bearing claims;
- `audience-profile.md` when it matches the intended reader;
- relevant voice examples only when the user identifies them.

If the thesis, reader, or promise is genuinely ambiguous, ask before writing. Do not silently
perform a market scan or invent the author's position.

## Output

Write one non-destructive article at `drafts/<descriptive-slug>.md`. If that path already exists,
use the smallest free `-vN` suffix unless the user explicitly asks to revise the existing file.

Use concise frontmatter:

```yaml
---
status: draft
research: research/<slug>/
topic-brief: topics/<slug>/topic-brief.md
sources:
  - raw/<ingested-source>.md
external-refs:
  - https://example.com/direct-source
created: YYYY-MM-DD
last-updated: YYYY-MM-DD
tags: [draft]
---
```

Omit fields that do not apply. `sources:` contains only files that exist under `raw/`;
`external-refs:` contains cited sources not yet ingested. Start the body with an H1.

## Workflow

### 1. Reconstruct the editorial contract

Before drafting, state internally:

- target reader;
- current reader belief or tension;
- selected thesis;
- reader promise;
- why the article should exist now;
- author position and strongest objection;
- facts that need a final freshness check.

Treat `topic-brief.md` as editorial direction. Do not blend rejected topic options into the piece.

### 2. Build an evidence spine

Trace every load-bearing claim to an original source. Use the research report for orientation and
the source ledger for verification; do not cite either artifact as factual authority.

Open time-sensitive or contested original sources before writing. If a core claim remains
unsupported, narrow the thesis, state the uncertainty, or ask for more research.

Read `references/evidence-and-citations.md`.

### 3. Turn the outline into a narrative

An outline is scaffolding, not prose. Re-evaluate its sequence for reader momentum:

- open on a concrete tension, consequence, scene, or surprising distinction;
- state the thesis early enough to orient the reader;
- give each section one job in the argument;
- move from explanation to evidence to implication;
- surface the strongest objection at the point it matters;
- end with a changed understanding or proportionate action.

Read `references/article-writing.md`. Do not preserve the research report's order unless it is also
the strongest article order.

### 4. Write the full article

Write complete prose, not notes with polished headings.

- Prefer concrete nouns, verbs, examples, and decisions.
- Explain technical terms at first use without talking down to the reader.
- Use analogies only when they preserve important boundaries.
- Vary paragraph and sentence length for rhythm.
- Make transitions carry the argument instead of announcing sections.
- Put evidence beside the claim it supports.
- Keep source links useful and unobtrusive.
- Preserve nuance without burying the conclusion.

Do not include research-process language such as `verified`, `source ledger`, `our scan found`, or
`推断·未实测` in the reader-facing article unless the methodology itself is relevant.

### 5. Protect originality

Use market examples to understand conventions and gaps, never as prose templates.

- Do not copy a competitor's title, hook, phrasing, analogy, or signature sequence.
- Do not imitate a source's sentence rhythm across a passage.
- Attribute distinctive ideas.
- Add original synthesis by making the relationship between evidence and thesis explicit.
- Remove claims included only because they appeared in the research report.

### 6. Run an editorial review

Read `references/editorial-review.md`, revise the draft, and only then present it.

## Quality bar

The finished article must:

- make its thesis clear within the first 20% without necessarily stating it in the first sentence;
- deliver the promised reader change;
- contain no section that merely dumps background;
- distinguish evidence, interpretation, and author judgment;
- engage the strongest reasonable objection;
- support every load-bearing factual claim;
- sound like an article, not a compressed research report;
- remain useful to a reader who cannot access the vault;
- contain no placeholders, workflow instructions, or unpublished internal notes.

## Boundary with other skills

- `/research` builds the understanding and evidence.
- `/topic` chooses the editorial opportunity and produces the brief and outline.
- `/draft` writes and revises the article.

If writing exposes a factual gap, return the precise gap to `/research`. If it exposes an unclear
or weak thesis, return it to `/topic`. Do not absorb those jobs into drafting.
