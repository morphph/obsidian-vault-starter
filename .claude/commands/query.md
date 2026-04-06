---
name: query
description: "Ask a question against the wiki. Usage: /query <question>"
---

# Query — Ask the Wiki

Read CLAUDE.md first for wiki conventions.

## Arguments
`$ARGUMENTS` is a natural language question.

## Workflow

### 1. Find relevant pages

Read wiki/index.md to identify relevant pages. Then read those pages.

### 2. Synthesize answer

Answer the question grounded in wiki content. Cite sources with [[wikilinks]] to wiki pages. If referencing original sources, cite the raw/ file too.

Present different forms as appropriate:
- Prose answer
- Comparison table
- Bullet-point analysis

### 3. Identify gaps

If the wiki doesn't have enough information to fully answer:
- Say so explicitly
- Suggest what sources could fill the gap
- Log it as a data gap

### 4. File or discard

Ask: **"File this as a wiki page?"**

**If yes:**
- Create a new wiki page (type: synthesis) with the answer
- Update wiki/index.md
- Append to wiki/log.md with `answer-filed: {page}.md`

**If no:**
- Append to wiki/log.md with `answer-filed: chat only`

### 5. Log

Append to wiki/log.md:
```
## [YYYY-MM-DD] query | {Question}
pages-consulted: {list}
answer-filed: {page.md or "chat only"}
```
