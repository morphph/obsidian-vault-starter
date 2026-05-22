---
name: query
description: "Use this skill whenever the user asks a question whose answer should come from the wiki rather than general knowledge. Triggers include: 'what does the wiki say about X', 'do we have notes on Y', 'remind me what Z is', 'I think we ingested something about W', '我们 wiki 里有 X 吗', or any question where the user is testing recall of previously ingested material. **Don't use when** the user is asking a new question that requires ingesting fresh sources first — suggest `/ingest` instead."
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
