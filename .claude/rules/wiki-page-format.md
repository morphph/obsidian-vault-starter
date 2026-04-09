---
paths: ["wiki/**"]
---

# Wiki Page Format

Every wiki page uses this structure:

```
---
type: entity | concept | synthesis | source-summary
created: YYYY-MM-DD
last-updated: YYYY-MM-DD
sources:
  - raw/filename.md
tags: []
---

# Title

## Summary
[2-3 sentences]

## Details
[Bullet points preferred over prose]

## Connections
- Related: [[other wiki pages]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
```
