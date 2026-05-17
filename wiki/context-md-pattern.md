---
type: concept
created: 2026-05-17
last-updated: 2026-05-17
sources:
  - raw/2026-05-17-mattpocock-grill-with-docs-skill.md
  - raw/2026-05-17-aihero-grill-with-docs-changelog.md
tags: [wiki, ddd, documentation, pattern]
---

# CONTEXT.md Pattern (Ubiquitous Language File)

## Summary
File format from [[grill-with-docs]]: a per-bounded-context glossary that the agent loads to inherit team-specific vocabulary. Strict rule — glossary only, no implementation details. Created lazily as terms resolve during grilling sessions. The on-disk implementation of Eric Evans' ubiquitous language from DDD.

## Details

### Strict rule
CONTEXT.md is a **glossary**. NOT:
- A specification
- A scratchpad
- An implementation log
- A runbook

If you find yourself writing "to do X, run Y" — that doesn't belong. CONTEXT.md is "the noun 'Customer' means..." Period.

### Why strict
A glossary can stay current for years. A scratch document rots in weeks. Conflating them destroys both.

### File structure for one context
```
/
├── CONTEXT.md             ← single glossary
├── docs/adr/              ← architectural decisions
└── src/
```

### File structure for bounded contexts
```
/
├── CONTEXT-MAP.md         ← points to per-context files
├── docs/adr/              ← system-wide decisions
└── src/
    ├── ordering/
    │   ├── CONTEXT.md     ← ordering domain glossary
    │   └── docs/adr/
    └── billing/
        ├── CONTEXT.md     ← billing domain glossary
        └── docs/adr/
```

### Sample entry shape
```markdown
## Customer
A person who has placed at least one Order. Distinct from User (which may or may not have ordered). Use "Customer" when referring to ordering/billing behavior; use "User" only for auth/profile context.
```

### Token economics (why this earns its keep)
Before CONTEXT.md, agent describes "the issue where a lesson inside a section of a course gets a real filesystem location." After CONTEXT.md, agent says "materialization cascade issue." Savings per session: 50-200 tokens × N references × M sessions. Compounds.

### Lifecycle
- **Created** lazily — first time a term is resolved in grilling
- **Updated** inline during `/grill-with-docs` sessions
- **Maintained** by `/improve-codebase-architecture` (flags inconsistencies)
- **Referenced** by every subsequent skill (`/to-prd`, `/to-issues`, `/tdd`, etc.)

### Anti-patterns
- "Living document" with implementation history → rotted in 2 weeks
- One CONTEXT.md per file → defeats unification purpose
- 200+ entries → unmaintainable, find what you need to actually disambiguate

## Connections
- Produced by: [[grill-with-docs]]
- Consumed by: [[mattpocock-skills-library]] (all 5 skills)
- DDD lineage: Eric Evans (Domain-Driven Design)
- Phase 1 artifact of: [[idea-to-afk-agent-flow]]
- Sibling: [[four-files-context-architecture]] (Khairallah's lighter version)

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-05-17 | grill-with-docs SKILL.md + AI Hero changelog | Initial creation |
