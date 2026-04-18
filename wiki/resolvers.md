---
type: concept
created: 2026-04-18
last-updated: 2026-04-18
sources:
  - raw/2026-04-18-garrytan-thin-harness-fat-skills.md
tags: [wiki, agentic, context-management]
---

# Resolvers

## Summary
A resolver is a **routing table for context**: when task type X appears, load document Y first. Coined by [[garry-tan|Garry Tan]] as one of the five definitions in [[thin-harness-fat-skills]]. Skills tell the model *how*; resolvers tell it *what to load and when*. The fix for bloated CLAUDE.md files (and the reason a 200-line skeleton with on-demand loading beats a 20,000-line dump).

## Details

### Why resolvers exist
- Context window is the [[context-management|scarcest resource]]
- Loading everything upfront → degraded attention, lower quality
- Loading nothing → model misses critical conventions
- Resolver bridges: minimal default context + automatic on-demand loading

### How a resolver works
- **Trigger**: task type, intent match, or file pattern
- **Action**: load specific document(s) into context
- **Result**: model reads the right thing at the right moment, without bloat

### Garry's confession (the canonical resolver story)
> "My CLAUDE.md was 20,000 lines. Every quirk, every pattern, every lesson I'd ever encountered. Completely ridiculous. The model's attention degraded. Claude Code literally told me to cut it back. The fix was about 200 lines — just pointers to documents. The resolver loads the right one when it matters. Twenty thousand lines of knowledge, accessible on demand, without polluting the context window."

### Built-in resolvers in [[claude-code]]
- **Skill description as resolver**: every skill has a `description` field; the model matches user intent to descriptions automatically. **The description IS the resolver.**
- You never have to remember `/ship` exists — describe your intent, the resolver finds the matching skill
- Slash commands' description metadata is doing the routing

### The eval-suite example (why this matters)
- Developer changes a prompt
- Without resolver: ships it, accuracy regresses, no one notices
- With resolver: model reads `docs/EVALS.md` first → "run the eval suite, compare scores, if accuracy drops more than 2%, revert and investigate"
- The developer didn't know the eval suite existed; the resolver loaded it

### Resolvers in our setup (already implemented)
- **`.claude/rules/*.md` with `paths:` glob** — this is a resolver pattern. When editing files matching the glob, the rule loads automatically.
  - `wiki-page-format.md` (paths: `wiki/**`) → loads when editing wiki pages
  - `log-format.md` (paths: `wiki/log.md`) → loads when editing the log
- **CLAUDE.md as 200-line index, not 20K-line dump** — already correct shape; should stay this way
- **Slash command descriptions** in `.claude/commands/` headers do auto-routing

### Design rules for resolvers
- Trigger conditions should be **specific, not generic** (file glob > intent match > catchall)
- Loaded documents should be **small and pointed** — they replace bloat, not add to it
- A resolver that loads 5K lines is not better than the 5K lines in CLAUDE.md
- Composability: resolvers can chain (rule loads doc, doc references skill, skill invokes tool)

## Connections
- Related: [[thin-harness-fat-skills]], [[context-management]], [[claude-code]], [[garry-tan]], [[skill-as-method-call]], [[harness-design]], [[documentation-layers]], [[context-noise-governance]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-18 | raw/2026-04-18-garrytan-thin-harness-fat-skills.md | Initial creation — Garry's resolver definition + 20K→200 line story |
