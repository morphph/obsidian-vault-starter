---
type: concept
created: 2026-04-09
last-updated: 2026-04-09
sources:
  - raw/2026-04-08-session-unknown-1216.md
tags: [wiki, seo, content-distribution, tool]
---

# Keyword Grouping Engine

## Summary
Reusable LLM prompt engine for clustering SEO keywords into content-ready groups. Given a subtopic + keyword list, outputs grouped keywords with intent classification, content type assignment, and primary keyword selection. Designed to be fed repeatedly across subtopics.

## Details
- **Input:** Subtopic name + numbered keyword list
- **Output:** JSON with number-based references (not strings) for compact, parseable output
- **Grouping rules:**
  - Group size: 2-8 typical, max 15, single-keyword groups valid
  - Different comparison pairs (vs cursor, vs copilot) → always separate groups
  - Off-topic keywords correctly ungrouped
- **Intent classification per group:**
  - Informational questions → `faq` content type
  - Commercial comparisons → `compare` content type
  - Broad head terms → `topic-hub` content type
- **Example output (Claude Code Pricing):**
  - Cluster 1: General pricing (4 keywords)
  - Cluster 2: Free tier (2 keywords)
  - Cluster 3: Enterprise/API pricing (2 keywords)
  - Cluster 4: vs Cursor comparison (1 keyword)
  - Ungrouped: "what is claude code" (definitional, not pricing intent)
- **Reusability:** Engine prompt designed as a template for repeated use across subtopics. Could be saved as a Claude Code skill.

## Connections
- Related: [[loreai]], [[content-distribution-china]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-09 | raw/2026-04-08-session-unknown-1216.md | Initial creation — prompt design + example output |
