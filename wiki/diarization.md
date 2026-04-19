---
type: concept
created: 2026-04-19
last-updated: 2026-04-19
sources:
  - raw/2026-04-11-garry-tan-thin-harness-fat-skills.md
tags: [wiki, principle, agentic, knowledge-work]
---

# Diarization

## Summary
[[garry-tan|Garry Tan]]'s name for the pattern that makes AI useful for real knowledge work: the model reads **everything** about a subject and writes a **structured one-page profile** distilled from dozens or hundreds of documents. Not a database lookup. Not a RAG retrieval. An analyst's brief produced by sustained reading.

## Details

### Why neither SQL nor RAG produces this
- SQL: returns rows that match. Doesn't notice contradictions, can't synthesize.
- RAG / embedding similarity: returns *similar-looking* chunks. Misses cross-document patterns, can't hold the whole picture in mind.
- Diarization requires the model to actually read, hold contradictions, notice what changed and when, and synthesize structured intelligence.

### The canonical output: SAYS vs ACTUALLY BUILDING
```
FOUNDER: Maria Santos
COMPANY: Contrail (contrail.dev)
SAYS: "Datadog for AI agents"
ACTUALLY BUILDING: 80% of commits are in billing module.
  She's building a FinOps tool disguised as observability.
```

The gap between "says" and "actually building" requires reading the GitHub commit history, the application, and the advisor transcript, and holding all three in mind at once. **No embedding similarity finds this. No keyword filter finds it.** This is the perfect decision to put in [[latent-vs-deterministic|latent space]].

### Compositional position in the architecture
Diarization sits inside the [[skill-as-method-call|skill]]. Example:
- `/enrich-founder` skill calls deterministic tooling (SQL, GitHub stats, browser tests, CrustData) to gather raw material → then invokes diarization in latent space to produce the one-page profile.
- A nightly cron keeps 6,000 profiles fresh.

### The two transferable loops
Garry frames diarization as one half of the most valuable knowledge-work loops in 2026:
1. **Forward loop**: retrieve → read → diarize → count → synthesize
2. **Learning loop**: survey → investigate → diarize → rewrite the skill

The second loop is how systems get better without anyone editing code — the [[thin-harness-fat-skills]] worked example shows YC's NPS "OK" responses being diarized into new matching rules that get written back into the skill file.

### Connection to existing wiki concepts
- [[index-over-rag]] generalizes the same anti-RAG intuition at the retrieval layer; diarization is the synthesis layer.
- [[knowledge-compiler-design]] / [[time-gated-compilation]] — wiki pages in this vault are themselves diarizations of raw/ sources.
- [[session-memory]] — Claude Code's continuous note-taking by forked subagent is real-time diarization of the session.

## Connections
- Related: [[thin-harness-fat-skills]], [[garry-tan]], [[skill-as-method-call]], [[latent-vs-deterministic]], [[index-over-rag]], [[knowledge-compiler-design]], [[session-memory]], [[time-gated-compilation]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-19 | raw/2026-04-11-garry-tan-thin-harness-fat-skills.md | Initial creation |
