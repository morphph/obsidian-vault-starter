---
type: concept
created: 2026-05-11
last-updated: 2026-05-11
sources:
  - raw/2026-05-09-garry-tan-meta-meta-prompting.md
tags: [wiki, pattern, agentic, knowledge-work, content]
---

# Book Mirror

## Summary
[[garry-tan|Garry Tan]]'s pattern for **two-column reading**: extract every chapter of a book, run a sub-agent per chapter that **(left) summarizes the author's idea + (right) maps it to your actual life** using your accumulated personal context. Garry has done 20+ books this way (Pema Chödrön, Watts, Hesse, Feynman, Hamming, Ken Wilber, etc.). Each book mirror is ~30,000 words. **"A $300/hour therapist couldn't do this in 40 hours"** because they don't have the full graph of your professional context, meeting notes, founder relationships, and reading history loaded and cross-referenceable. **Every mirror gets richer because the brain gets richer.**

## Details

### The pattern (verbatim from Garry)
> "The system extracted all 22 chapters of the book, and then, for each chapter, ran a sub-agent that did two things simultaneously: summarized the author's ideas, and then mapped every idea to my actual life. Not generic 'this applies to leaders' pablum. **Specific mapping.**"

### Output shape: chapter-by-chapter two-column page

```
| What [Author] says         | How it maps to me                |
|----------------------------|----------------------------------|
| Chapter idea 1, summarized | Cited reference to brain page X, |
|                            | specific founder convo from last |
|                            | week, the IM chat with college   |
|                            | roommate at 19, etc.             |
```

Per Garry's example (Pema Chödrön's *When Things Fall Apart*):
- 22 chapters → 30,000-word output
- Right column cites actual brain pages (per-section retrieval, not just synthesis)
- The chapter on groundlessness → linked a specific founder conversation
- The chapter on fear → mapped patterns his therapist had identified
- The chapter on letting go → referenced a late-night session about creative freedom

### The dependency chain: book-mirror calls multiple skills

| Sub-call | Purpose |
|----------|---------|
| `media-ingest` | Extract chapters from PDF / EPUB / audio |
| `brain-ops` | Search per-section for specific personal context |
| `enrich` | Pull person/company pages referenced |
| `cross-modal-eval` | Fact-check against known brain truths (catch errors before shipping) |
| `pdf-generation` | Final output format |

Book-mirror is the canonical example of **skill composition** (see [[skillify-meta-skill]]).

### Why this can't be done with naive RAG
The right-column entries cite *specific brain pages* — meeting notes from last Thursday, a 19-year-old IM transcript, a founder conversation about co-founder drama. A flat RAG over the book + journal would miss this. **Per-section, intent-aware retrieval against a structured knowledge graph is what makes it work.**

This is [[diarization]] applied to other people's ideas — sustained reading + structured cross-mapping, not similarity search.

### The compounding effect (the actual headline)
> "Each one gets richer because the brain gets richer. The second mirror knew about the first. The twentieth knew about all nineteen."

Once you have 20 book mirrors, the 21st can cite back to ideas from the previous 20. This is the core argument of [[filing-cabinet-vs-nervous-system|filing cabinet vs nervous system]]: connections compound.

### Engineering note: the first version was terrible
Garry's V1 book mirror had three factual errors:
- Said his parents were divorced (they weren't)
- Said he grew up in Hong Kong (he was born in Canada)
- Generic mapping instead of cited specifics

Fixes that compounded:
1. **Mandatory cross-modal-eval** — Opus 4.7 1M for precision, GPT-5.5 for recall, DeepSeek V4-Pro for generic-detection
2. **Per-section brain retrieval** instead of one-shot synthesis
3. All fixes baked into the skill file via [[skillify-meta-skill|/skillify]] — every subsequent mirror inherits them

This is the "compound curve" in action: each fix to a skill improves every future invocation.

### How this pattern generalizes

The book-mirror template applies to anything where (a) external content has structure (chapters, sections, episodes) and (b) you want to project that structure against your own context:

| Source | Mirror version | Right column |
|--------|----------------|---------------|
| Book | book-mirror | Personal life context |
| Podcast | episode-mirror | Project / founder context |
| Long thread / essay | thread-mirror | Strategic-decision context |
| Company report | report-mirror | Portfolio context |
| Conference talk | talk-mirror | Research / hiring context |

### Connection to this vault

This vault's `/ingest` does the **left column only** — extract + structure the source. Adding a **right-column pass** that maps each section against the existing wiki would turn `/ingest` into a vault-aware book-mirror:
- For an article about resolver patterns → map every key claim against what `wiki/resolvers.md`, `wiki/check-resolvable.md`, etc. already say
- Flag contradictions explicitly
- Surface where this article advances vs. duplicates existing wiki content

That's effectively what we already do informally in 要点解读 sections, but it would become systematic.

Connects to candidate 5️⃣ (`/draft` upgrade with quality-gate-loop) and 6️⃣ (HTML output) — the book-mirror two-column layout is a natural HTML artifact.

## Connections
- Related: [[garry-tan]], [[gbrain]], [[skillify-meta-skill]], [[diarization]], [[filing-cabinet-vs-nervous-system]], [[cross-modal-review]], [[index-over-rag]], [[html-as-output-format]], [[quality-gate-loop]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-05-11 | raw/2026-05-09-garry-tan-meta-meta-prompting.md | Initial creation |
