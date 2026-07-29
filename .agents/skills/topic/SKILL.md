---
name: topic
description: Turn an understood subject into a differentiated, evidence-backed editorial opportunity. Use when the user wants to decide what article to write, inspect how a topic is already covered, compare high-signal or high-performing content, identify saturated narratives and unmet reader needs, or choose and refine a content angle. Prefer a completed research workspace as input. Produces market-scan.md and topic-options.md, then topic-brief.md and outline.md after the user selects an angle. Do not use to establish the underlying facts or explain the whole subject; use /research. Do not write the article; use /draft.
---

# Topic — Decide What Is Worth Writing

Read `AGENTS.md` before working in this repository.

Study the editorial market around a subject and turn it into a small set of content bets. Keep
truth claims anchored to `/research`; focus this skill on reader demand, existing narratives,
content packaging, differentiation, and the author's chosen position.

## Two operations

### Explore

Use for `/topic <research-workspace-or-topic>`.

Produce:

- `topics/<slug>/market-scan.md`
- `topics/<slug>/topic-options.md`

Stop after presenting 2–4 angle options. Do not create an outline for every option.

### Finalize

Use when the user selects an option, for example:

`/topic finalize topics/<slug>/ angle:2`

Read the user's selection and corrections, then produce:

- `topics/<slug>/topic-brief.md`
- `topics/<slug>/outline.md`

Do not re-run the market scan unless the user asks or the source material is stale.

## Inputs

Prefer a `/research` workspace containing `report.md` and `source-ledger.md`. Also read:

- `audience-profile.md` when it describes the intended reader;
- relevant existing drafts to detect prior coverage;
- a target publication or channel only when the user specifies one.

If the user supplies only a raw topic, perform enough discovery to map existing content but do not
pretend to have completed factual research. Record factual uncertainties under `research gaps` and
recommend `/research` before drafting when they affect the proposed thesis.

## Explore workflow

### 1. Establish the editorial question

Write down:

- target reader and their job-to-be-done;
- what the research says is newly important;
- likely decision, tension, or misconception;
- relevant language and freshness window;
- prior coverage by this author, if available.

Do not search for titles before understanding what readers need.

### 2. Define a comparison set

Choose sources and channels because they compete for the same reader attention. Include a
reasonable mix of:

- discourse-shaping pieces from the research report;
- recent explainers, guides, arguments, and case studies;
- strong criticism or contrarian coverage;
- content surfaced by channel-native search;
- comments or audience questions when available.

Record the inclusion logic and data limits. A random list of search results is not a market scan.

### 3. Analyze content as editorial products

Read `references/content-analysis.md`. For each material example, extract:

- title and opening hook;
- promised reader outcome;
- thesis or framing;
- proof mechanism and examples;
- structure and level of depth;
- target reader and assumed knowledge;
- actual response data, if observable;
- unanswered questions and revealing comments.

Reuse factual sources from `/research`; do not reward a popular piece for unsupported claims.

### 4. Separate performance from prominence

Classify every content signal:

- `observed` — comparable views, reactions, comments, saves, or other direct metrics;
- `proxy` — citation frequency, search prominence, author reach, or repeated references;
- `unavailable` — no defensible signal.

Only use Top-N or performance ranking when observed metrics and the comparison set are documented.
Otherwise describe representative patterns and state the limitation.

### 5. Find editorial opportunities

Synthesize:

- **Saturated narratives** — repeated promises and frames with little remaining novelty.
- **Under-served questions** — reader needs visible in comments, criticism, or incomplete pieces.
- **Evidence gaps** — popular claims that the research contradicts or cannot verify.
- **Depth gaps** — content that names a concept without explaining its mechanism.
- **Audience gaps** — useful ideas explained for the wrong reader or assumed expertise.
- **Author advantage** — credible experience, viewpoint, examples, or synthesis available here.

Read `references/market-scan-template.md` and write `market-scan.md`.

### 6. Propose angle cards

Read `references/topic-options-template.md`. Produce 2–4 genuinely different content bets, not
title variations. Each must include:

- working title;
- one-sentence thesis;
- reader promise;
- why now;
- market-gap evidence;
- research evidence;
- differentiation from representative content;
- likely objections and risks;
- recommended structure at a high level.

Recommend one option, explain the tradeoff, and stop for the user's selection.

## Finalize workflow

### 1. Apply the author's choice

Treat the selected angle and the user's corrections as authoritative editorial direction. Do not
blend rejected options back into the result.

### 2. Write the topic brief

Read `references/topic-brief-template.md`. Make the selected thesis, audience promise, evidence,
boundaries, and author position explicit.

### 3. Write one outline

Build a narrative argument, not a report table of contents:

- place the thesis early;
- give each section a distinct job;
- map load-bearing claims to original sources;
- include the strongest objection;
- state what to omit;
- end with the reader's changed understanding or action.

The outline should be detailed enough for `/draft` to write without performing market research.

## Quality check

Before finishing:

- the comparison set matches the intended reader;
- popularity claims have observed data or are clearly marked as proxy;
- options differ in thesis, not just packaging;
- every angle has a real market or reader-gap rationale;
- no angle depends on a claim that `/research` disputes or leaves unsupported;
- the final brief reflects the author's selected take;
- neither artifact contains a finished article.

## Boundary with other skills

- `/research` establishes what the topic means, how it evolved, and what the community debates.
- `/topic` decides which editorial position is worth publishing.
- `/draft` turns the selected brief and outline into an article.
