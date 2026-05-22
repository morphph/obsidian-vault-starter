---
name: lint
description: "Use this skill whenever the user wants to audit wiki health or asks 'is anything broken in the wiki', 'find orphan pages', 'check for stale notes', 'lint the wiki', 'wiki health check', 'are there contradictions', 'what's missing'. Also triggers proactively if user mentions wiki feeling messy or after a large batch of ingests. **Don't use when** the user wants to add new content — that's `/ingest`."
---

# Lint — Wiki Health Check

Read CLAUDE.md first for wiki conventions.

## Workflow

### 1. Scan everything

- Read wiki/index.md
- Read every wiki page (excluding index.md and log.md)
- Read wiki/log.md for recent activity

### 2. Check for issues

**Orphan pages:** Wiki pages not linked from any other wiki page and not in the index.

**Stale pages:** Pages whose `last-updated` is old relative to their domain. Flag pages not updated in 30+ days if their topic is fast-moving.

**Missing cross-references:** Pages that mention the same entity or concept but don't link to each other.

**Contradictions:** Claims that conflict across different wiki pages.

**Index drift:** Pages that exist in wiki/ but aren't listed in index.md, or index entries pointing to non-existent pages.

**Unresolved links:** [[wikilinks]] in wiki pages that point to pages that don't exist yet. These are candidates for new pages.

**Thin coverage:** Entities or concepts with only one source (fragile knowledge).

**Source gaps:** Topics mentioned across multiple pages but lacking a dedicated page.

### 3. Report

Show in terminal:
- Total pages scanned
- Issues found by category with specifics
- Suggested actions (create page X, add link from Y to Z, etc.)

### 4. Auto-fix (with permission)

Ask: **"Auto-fix index drift and add missing cross-references?"**

If yes:
- Update index.md to match actual wiki pages
- Add missing [[wikilinks]] where pages reference the same concepts
- Do NOT auto-resolve contradictions — flag them for human review

### 5. Log

Append to wiki/log.md:
```
## [YYYY-MM-DD] lint
pages-scanned: {N}
issues: orphans({N}), stale({N}), contradictions({N}), index-drift({N}), unresolved-links({N}), thin({N})
auto-fixed: {description or "none"}
```
