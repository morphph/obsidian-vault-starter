---
paths: ["wiki/log.md"]
---

# Log Format

Append-only. Each operation gets a new entry:

```
## [YYYY-MM-DD] ingest | Source Title
source: raw/filename.md
pages-created: page1.md, page2.md
pages-updated: page3.md

## [YYYY-MM-DD] query | Question text
pages-consulted: page1.md, page2.md
answer-filed: synthesis-page.md (or "chat only")

## [YYYY-MM-DD] lint
pages-scanned: N
issues: orphans(N), stale(N), contradictions(N)
auto-fixed: description
```
