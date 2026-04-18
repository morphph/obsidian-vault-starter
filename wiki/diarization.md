---
type: concept
created: 2026-04-18
last-updated: 2026-04-18
sources:
  - raw/2026-04-18-garrytan-thin-harness-fat-skills.md
tags: [wiki, agentic, knowledge-work, synthesis]
---

# Diarization

## Summary
The synthesis step where the model reads everything about a subject and produces a single-page structured profile — judgment distilled from dozens or hundreds of documents. Coined by [[garry-tan|Garry Tan]] as one of the five definitions in [[thin-harness-fat-skills]]. **No SQL query, RAG pipeline, or embedding search produces this.** It's the difference between a database lookup and an analyst's brief — and it's what makes AI useful for real knowledge work.

## Details

### What diarization is NOT
- ❌ Embedding similarity search ("find docs like this one")
- ❌ Keyword filter / SQL query ("find rows where X")
- ❌ RAG retrieval ("paste top-K chunks into context")
- ❌ Summarization of a single document

### What diarization IS
- The model **actually reads** every relevant document about a subject
- Holds **contradictions** in mind across sources
- Notices **what changed and when** (temporal awareness)
- Synthesizes a **structured intelligence profile** — typically one page

### The hallmark output: "says vs. actually building" gap
Garry's example from YC Startup School:

> FOUNDER: Maria Santos
> COMPANY: Contrail (contrail.dev)
> SAYS: "Datadog for AI agents"
> ACTUALLY BUILDING: 80% of commits are in billing module. She's building a FinOps tool disguised as observability.

Detecting this requires:
- Reading the application (what she **says**)
- Reading the GitHub commit history (what she **does**)
- Reading the advisor 1:1 transcripts (how she explains it)
- Holding all three in mind at once
- Making a judgment about the gap

Embeddings can't find this. Keywords can't find this. **The model must read the full profile.**

### Why this is canonically a [[latent-vs-deterministic|latent]] task
- Inputs are heterogeneous (free-form text, code, transcripts, structured data)
- The output requires **argument**, not retrieval
- Same inputs could produce different valid summaries depending on what matters for the question
- "This is the perfect decision to put in latent space" (Garry)

### The output is itself reusable infrastructure
- Diarized profiles become structured documents that downstream skills can consume
- Cron-refreshed nightly → always-fresh profiles
- Other skills (matching, recommendation, learning loops) read the profile rather than re-reading raw sources
- Compounds with [[skill-as-method-call]]: same `/enrich-X` skill diarizes any subject

### Universal pattern Garry calls out
> "Retrieve, read, diarize, count, synthesize."
> "Then: survey, investigate, diarize, rewrite the skill."
> "If you want to know what the most valuable loops are in 2026, it's those."

### Where diarization fits in our stack
- **blog2video AI精读**: This *is* diarization — read article → produce structured Chinese profile. Garry's framing gives us a sharper name and pattern for it.
- **Wiki ingest takeaways**: also diarization — read source, write structured wiki page with claims, sources, connections.
- **Future**: a `/profile-builder` skill that turns 3-10 X posts + GitHub commits + interviews of any builder into a one-page wiki page is a direct application.

## Connections
- Related: [[thin-harness-fat-skills]], [[latent-vs-deterministic]], [[skill-as-method-call]], [[garry-tan]], [[index-over-rag]], [[blog2video]], [[zero-friction-capture]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-18 | raw/2026-04-18-garrytan-thin-harness-fat-skills.md | Initial creation — definition + Maria Santos example + applications |
