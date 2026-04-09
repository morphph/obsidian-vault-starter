# CLAUDE.md Self-Audit: Applying Best Practices to Our Own Wiki

**Source:** Internal exercise — applied Boris Cherny + Tw93 frameworks to our own CLAUDE.md
**Date:** 2026-04-09

## Context

After ingesting Boris Cherny's best practices and Tw93's context layering framework, we turned the lens on our own project's CLAUDE.md. The question: does our CLAUDE.md follow the practices we just documented?

## Audit Findings

### What was already good
- Checked into git, team-shared (Boris's #1 recommendation)
- Concrete conventions (kebab-case, wikilinks rules, contradiction handling) — not vague "write good code"
- Clear three-layer architecture (raw → wiki → CLAUDE.md)
- Domain focus grounding every session
- 180 lines — under the 200-line ceiling

### Critical gaps found

**1. No Compact Instructions**
Our own wiki page literally says: "没有Compact Instructions → 压缩时架构决策会丢失". We didn't have them. When context compresses mid-session, Claude could forget the three-layer architecture, what commands exist, what raw/ means.

**2. ~55% of the file was only needed sometimes**
This was the big one. Applying Tw93's "偶尔用的东西就不要每次都加载进来" principle:

| Section | Lines | Only needed when... |
|---------|-------|-------------------|
| Wiki Page Format template | 29 lines | Creating/editing wiki pages |
| Log Format template | 17 lines | Writing to log.md |
| Pipeline B detailed breakdown | 30 lines | Never — derivable from reading scripts/ |
| Source Types | 7 lines | /ingest only (already duplicated in commands/ingest.md) |
| Source Fetching Tools | 10 lines | /ingest only (already duplicated in commands/ingest.md) |
| Repo Locations | 2 lines | Cross-repo reference, rarely needed |

~95 lines of sometimes-relevant content in an always-resident file. Every API turn, Claude was reading our Wiki Page Format template even when the user just asked `/query what is AEO?`.

**3. No NEVER list**
Boris and official docs both recommend explicit hard guardrails. We had implicit conventions scattered across the Conventions section but no consolidated NEVER list.

**4. No governance for documentation itself**
No mechanism to ensure future changes (new skills, commands) get documented in the correct layer. Easy to drift back to "dump everything in CLAUDE.md."

## Changes Made — With Exact Examples

### Restructure: 180 → 87 lines (52% reduction)

---

### Move 1: Wiki Page Format → `.claude/rules/wiki-page-format.md`

**BEFORE (in CLAUDE.md, loaded every turn — 29 lines):**
```markdown
## Wiki Page Format

Every wiki page uses this structure:

\```
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
\```
```

**AFTER (in `.claude/rules/wiki-page-format.md` — loaded only when editing wiki/):**
```markdown
---
paths: ["wiki/**"]
---

# Wiki Page Format
[same template content]
```

**In CLAUDE.md, replaced with one line:**
```markdown
- Wiki page format template: `.claude/rules/wiki-page-format.md` (auto-loaded when editing wiki/)
```

**Why this works:** The `paths: ["wiki/**"]` frontmatter means this rule auto-loads when Claude edits any file in wiki/. During `/query` (read-only) or general conversation, it's invisible. 29 lines → 1 line in always-resident context.

---

### Move 2: Log Format → `.claude/rules/log-format.md`

**BEFORE (in CLAUDE.md — 17 lines):**
```markdown
## Log Format

\```
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
\```
```

**AFTER (in `.claude/rules/log-format.md` — loaded only when editing wiki/log.md):**
```markdown
---
paths: ["wiki/log.md"]
---

# Log Format
[same template content]
```

**In CLAUDE.md, replaced with one line:**
```markdown
- Log entry format: `.claude/rules/log-format.md` (auto-loaded when editing wiki/log.md)
```

**Why this works:** Even narrower path targeting than the page format. Only loads when Claude is actually writing to the log. 17 lines → 1 line.

---

### Move 3: Remove duplication with commands

**BEFORE (in CLAUDE.md — 27 lines across two sections):**
```markdown
## Source Types

### Articles & Posts
Standard web content — blogs, documentation, X/Twitter articles. Saved as-is to `raw/`.

### GitHub Repos (Deep Scan)
For repo URLs, `/ingest` runs a deep architecture scan via `gh` CLI...

## Source Fetching Tools

For `/ingest` URL handling, use this priority chain:
1. **WebFetch** — Built-in. Fast, works for static sites...
2. **Claude for Chrome MCP** — Uses real browser with user's login sessions...
3. **Playwright MCP** — Headless browser automation...

JS-heavy sites (need browser): twitter.com, x.com, youtube.com...
```

**AFTER:** Deleted entirely. This content already existed word-for-word in `.claude/commands/ingest.md` under "Smart URL Fetch Chain" and "GitHub Deep Scan". It was pure duplication — loaded in CLAUDE.md on every turn, then loaded again from the command file when /ingest actually ran.

---

### Move 4: Compress Pipeline B (30 → 3 lines)

**BEFORE (30 lines with full subsections):**
```markdown
## Pipeline B: Internal Knowledge Capture

Automatic capture of knowledge from Claude Code sessions in LoreAI and blog2video.

### How it works
1. **SessionEnd / PreCompact hooks** fire automatically...
2. Hook extracts conversation context from JSONL transcript...
[7 numbered steps]

### Scripts (`scripts/`)
- `flush.py` — Background knowledge extraction...
- `compile.py` — Compiles raw → wiki pages...
- `config.py` — Path constants
- `utils.py` — Shared helpers...

### Hooks (`hooks/`)
- `session-start.py` — Injects wiki/index.md...
- `session-end.py` — Captures transcript...
- `pre-compact.py` — Safety net...

### Safety
- **Recursion guard:** `CLAUDE_INVOKED_BY`...
- **Deduplication:** Same session won't be flushed twice...
- **Wiki repo excluded:** No hooks configured here...

### Hooks configured in:
- `~/Desktop/Project/loreai-v2/.claude/settings.json`
- `~/Desktop/Project/blog2video/.claude/settings.json`
```

**AFTER (3 lines):**
```markdown
## Pipeline B: Internal Knowledge Capture

SessionEnd/PreCompact hooks in LoreAI and blog2video capture session knowledge → `scripts/flush.py` → `raw/`.
After 6 PM: `scripts/compile.py` auto-compiles new raw files into wiki pages.
Safety: `CLAUDE_INVOKED_BY` env var prevents recursion. No hooks configured in THIS repo.
```

**Why this works:** Script details (flush.py, compile.py, utils.py) are derivable by reading the files. Hook details are configured in OTHER repos, not here. The only non-derivable info: the recursion guard and "no hooks here" — safety-critical, kept.

---

### Addition 1: NEVER list (new, 5 lines)

```markdown
## NEVER
- Never modify files in `raw/` — they are immutable source documents
- Never create subdirectories in `wiki/` — flat structure only, use index.md categories
- Never create wiki pages without updating `wiki/index.md`
- Never make claims in wiki pages without tracing to a source file in `raw/`
- Never link generic terms (AI, marketing, Python) — only link concepts worth tracking
```

**Why added:** These rules were previously scattered implicitly across Conventions and Architecture sections. Consolidating them as a NEVER list gives them prominence and makes them harder to miss during context compression.

---

### Addition 2: Compact Instructions (new, 6 lines)

```markdown
## Compact Instructions

When compressing context, preserve in priority order:
1. Architecture decisions and the three-layer model (raw → wiki → CLAUDE.md)
2. NEVER list — always re-check before acting
3. Which files have been modified and key changes made
4. Current task state and open TODOs
5. Tool outputs can be discarded — keep only pass/fail status
```

**Why added:** Without this, context compression could discard the three-layer architecture model. For this wiki system, forgetting that raw/ is immutable or that index.md must be updated would cause immediate correctness failures.

---

### Addition 3: Documentation Layers table (new, 10 lines)

```markdown
## Documentation Layers

When adding or changing features, put information in the right layer:

| What changed | Update where |
|-------------|-------------|
| New convention (applies every session) | This file (CLAUDE.md) |
| Rule for specific file types/directories | `.claude/rules/{name}.md` with `paths:` glob |
| New slash command | `.claude/commands/{name}.md` + add row to Commands table above |
| New skill | `.claude/skills/{name}/SKILL.md` + add row to Skills table above |
| Skill/command behavior details | Inside the skill/command file, NOT here |

Principle: **CLAUDE.md declares WHAT exists. Skills and commands define HOW they work.**
```

**Why added:** Without this meta-convention, the natural tendency is to dump everything into CLAUDE.md because it's the most visible file. This table is Layer 1 content that prevents Layer 1 bloat — a self-regulating mechanism. It answers: "I just created a new skill, where do I document it?"

---

### Addition 4: Commands table (replaced 40+ lines of inline detail)

**BEFORE:**
```markdown
### `/ingest <url|file|scan>`
Drop a source into the wiki. The core operation — one source fans out...
- **URL**: Fetches content (see Source Fetching Tools below)...
- **GitHub repo URL**: Deep scan — fetches README...
- **File path**: Ingests an existing file in `raw/`
- **scan**: Finds all files not yet in `wiki/log.md`...
- Creates source summary + entity/concept pages...
- Discuss key takeaways with user before creating pages

### `/query <question>`
[8 lines of detail]

### `/lint`
[6 lines of detail]

### `/visualize <topic|source-path|blank>`
[8 lines of detail]
```

**AFTER:**
```markdown
## Commands

Four slash commands. Each has full instructions in `.claude/commands/`.

| Command | What it does |
|---------|-------------|
| `/ingest <url\|file\|scan>` | Drop a source into the wiki. One source fans out across multiple pages. |
| `/query <question>` | Ask a question against the wiki. Synthesize with [[wikilink]] citations. |
| `/lint` | Health check: orphans, stale pages, contradictions, index drift. |
| `/visualize <topic\|path\|blank>` | Generate Excalidraw diagram from wiki knowledge. |
```

**Why this works:** CLAUDE.md now tells Claude WHAT commands exist (always needed). HOW they work is in the command files (loaded on-demand when triggered). 40+ lines → 7 lines.

## Key Takeaways

1. **Audit your own CLAUDE.md against the framework you're teaching.** We had ingested and written up best practices for context layering, then discovered our own file violated them. The cobbler's children had no shoes.

2. **"Lines in CLAUDE.md" is a misleading metric.** 180 lines was under the 200-line ceiling, but line count isn't the point. The real question: how much of this is needed EVERY turn? Only ~85 of our 180 lines were always-relevant.

3. **Duplication between CLAUDE.md and commands is invisible waste.** Our Source Fetching Tools section was identical to what was already in `commands/ingest.md`. Every turn, Claude was loading it in CLAUDE.md AND then again when running /ingest. Pure overhead.

4. **The Documentation Layers table is a pattern worth replicating.** Any project with CLAUDE.md + skills + commands should have an explicit mapping of "what goes where." Without it, the natural tendency is to dump everything into CLAUDE.md because it's the most visible file.

5. **Compact Instructions are not optional.** They're the difference between Claude remembering your architecture after context compression and Claude starting fresh. For a wiki system where architecture decisions (three-layer model, immutability of raw/) are load-bearing, losing them mid-session is catastrophic.
