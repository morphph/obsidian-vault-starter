---
type: concept
created: 2026-05-11
last-updated: 2026-05-11
sources:
  - raw/2026-05-09-garry-tan-meta-meta-prompting.md
tags: [wiki, principle, framing, knowledge-base, agentic]
---

# Filing Cabinet vs Nervous System

## Summary
[[garry-tan|Garry Tan]]'s sharpest framing for **why a knowledge base is not enough**: storage is filing cabinet, *connection* is nervous system. A filing cabinet stores things. A nervous system **connects them, flags what's changed, and surfaces what's relevant to right now.** This is the load-bearing distinction between Notion (filing cabinet — even with AI), Obsidian without an active agent (filing cabinet with backlinks), and [[gbrain]] (nervous system — every write triggers entity propagation, every meeting updates every mentioned person's page).

## Details

### The framing (verbatim)
> "This is the difference between having a filing cabinet and having a nervous system. The filing cabinet stores things. The nervous system connects them, flags what's changed, and surfaces what's relevant to right now."

### The four properties that distinguish a nervous system

| Property | Filing Cabinet | Nervous System |
|----------|----------------|------------------|
| **Storage** | ✅ Pages, files, folders | ✅ Pages, files, folders |
| **Linking** | Manual (you add backlinks) | **Automatic** (every entity mention creates typed links, zero LLM calls) |
| **Propagation** | None — meeting note stays in meeting folder | **Entity propagation** — meeting walks through every person/company mentioned and updates their page |
| **Recency awareness** | None — you search when you need something | **Flags what's changed** — surfaces stale info, contradictions, open threads |
| **Context-loading** | You pull what you remember | **Surfaces what's relevant to right now** — automatic dossier on the person you're about to meet |

### The "active" prerequisite
A knowledge base only becomes a nervous system when there's an **always-on agent loop** writing into it from multiple input streams (meetings, email, calendar, voice memos, browser). Without that:
- Notion: filing cabinet (even with Notion AI search)
- Obsidian alone: filing cabinet with manual links
- A wiki you read but don't write to from an agent: filing cabinet
- GBrain with `signal-detector` + 100 daily crons: nervous system

The pattern is: **state changes must propagate automatically**, or you don't have nerves, you have storage.

### What makes propagation cheap enough to be real-time

Garry's GBrain achieves entity propagation with **zero LLM calls** for the link-extraction layer:
- Pattern-matching for `[[Name](people/slug)]` and `[[people/slug|Name]]` wikilinks (see [[gbrain]] source detail)
- Typed edges (`attended`, `works_at`, `invested_in`, `founded`, `advises`) inferred from heuristics, not synthesis
- Vector + keyword hybrid search (no LLM in retrieval loop) — **97.6% recall on LongMemEval, beating MemPalace**

This is what lets the system **process 100+ crons/day without LLM cost spiraling**.

### Failure modes — when a "nervous system" decays to filing cabinet

- **No entity propagation** — meeting transcript creates one page; the 8 people and 3 companies mentioned never get the back-link → connections never form
- **Stale state** — pages get written once and never re-checked against fresh inputs → "current truth" becomes archaeology
- **No surfacing primitive** — you have to actively search; the system never pings you "this person you're meeting in 10 minutes has 4 open threads from last quarter"
- **Indexed but not understood** — pages live in folders, but no cross-cutting structure (timelines, relationships, scores) → you can find anything but understand nothing

[[context-rot]] is the same failure mode at the [[resolvers|resolver]] layer.

### The "active vs passive" knowledge-base test
Ask: **does my knowledge base do anything when I'm asleep?**

- No → filing cabinet
- Yes, runs crons that ingest / propagate / surface → nervous system

This is also the test for whether you're compounding. Filing cabinets don't compound. Nervous systems do.

### What this means for this vault

This vault sits **closer to filing cabinet than nervous system** today:
- ✅ Storage: structured, flat-namespace, [[index-over-rag]]
- ✅ Linking: [[wikilinks]] but **manual** (Claude adds them during ingest, but they're not extracted from prose post-hoc)
- ⚠️ Propagation: partial — when we ingest an article mentioning Garry Tan, his page gets updated, but only because we manually decide to. Not automatic from all sources.
- ❌ Recency awareness: none — we don't flag when a wiki page becomes stale because a newer source contradicts it (the `/lint` skill could check this but doesn't yet)
- ❌ Context-loading: none — there's no "you're about to do X, here's the relevant wiki pages" primitive

**Candidate to move this vault toward nervous-system**:
- Add automatic entity propagation: when a new raw/ file lands, scan for `[[entity]]` references and update entity pages with append-only timeline entries (the same Iron Law GBrain enforces, see [[gbrain]] `_brain-filing-rules.md`)
- Add staleness detection to `/lint`: flag wiki pages whose sources are >90 days old when newer sources on the same topic exist
- Pair with [[skillify-meta-skill]] so new ingest patterns codify themselves

These are downstream of the existing filing-rules candidate (1️⃣) — they require structured filing first.

### The enterprise version: System of Record → System of Intelligence

[[steph-zhang|Steph Zhang]]'s a16z piece (2026-05-14) makes the same argument at enterprise scale. The "filing cabinet" is the CRM (Salesforce, HubSpot, ServiceNow); the "nervous system" is the AI orchestration layer that reads/writes across CRM + calendar + Slack + email + product telemetry simultaneously. See [[system-of-intelligence]].

Same primitive, different scale:
- **Personal**: [[filing-cabinet-vs-nervous-system|filing cabinet vs nervous system]] ([[garry-tan|Garry Tan]])
- **Enterprise**: [[system-of-intelligence|system of record vs system of intelligence]] ([[steph-zhang|Steph Zhang]])

Both rest on the same mechanical claim: **once the cost of pulling from multiple sources approaches zero (because an agent does it), colocation stops being a moat. Synthesis becomes the moat.**

## Connections
- Related: [[garry-tan]], [[gbrain]], [[skillify-meta-skill]], [[book-mirror]], [[index-over-rag]], [[diarization]], [[context-rot]], [[two-pipeline-architecture]], [[zero-friction-capture]], [[steph-zhang]], [[system-of-intelligence]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-05-11 | raw/2026-05-09-garry-tan-meta-meta-prompting.md | Initial creation |
