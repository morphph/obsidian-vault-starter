# Part III — Phase Backlog v0.2

This backlog is organized to maximize implementation success rate for Claude Code by reducing architectural ambiguity, limiting cross-layer changes per phase, and keeping each phase independently valuable.

## Phase design principles

- Each phase should deliver a user-visible or system-visible improvement.

- Earlier phases should reduce the risk of later phases.

- Technical visibility fixes should precede major content-scale expansion.

- Planner insertion should happen only after the existing graph is easier to observe and validate.

- Topic replication should happen only after the pilot topic has a stable operating pattern.


---

## Phase 0 — Technical visibility and site correctness

### Objective

Remove technical blockers that suppress discovery and measurement of existing flagship-topic assets.

### Why this phase exists

LoreAI already has meaningful content, but technical SEO defects can suppress ranking, indexing, rich results, and cluster discovery. If this phase is skipped, later content work will compound into a flawed discovery layer.

### Scope

- canonical URL consolidation

- redirect/canonical consistency

- sitemap repair

- FAQ schema support

- homepage exposure for flagship topics

- validation utilities for sitemap/canonical/schema checks


### Deliverables

- one canonical URL policy implemented

- sitemap output is valid and deterministic

- invalid or undefined URLs are eliminated from sitemap generation

- FAQ pages emit valid FAQPage structured data

- homepage or equivalent discovery surface exposes flagship topic entry points


### Dependencies

None. This is the first implementation phase.

### Exit criteria

- no conflicting canonical variants for flagship-topic pages

- no invalid sitemap entries

- FAQ schema visible on representative FAQ pages

- flagship topic entry points discoverable from the homepage or equivalent site entry surface


### Risks if incomplete

- duplicate URL equity split remains

- topic hubs remain hard to discover

- FAQ pages continue to miss rich-result opportunity

- future cluster expansion becomes harder to measure


---

## Phase 1 — Claude Code flagship cluster completion

### Objective

Turn Claude Code into the first minimum-viable flagship cluster and establish the model for later replication.

### Why this phase exists

Claude Code already has enough content density to serve as the pilot, but the cluster is incomplete and imbalanced. The goal is not just "more pages," but a coherent cluster that can serve as the flagship template.

### Scope

- create canonical Claude Code cornerstone page

- improve Claude Code topic hub

- publish first compare wave

- publish first FAQ wave

- normalize glossary/supporting links where needed

- reinforce cluster internal linking

- add cluster inspection/reporting for Claude Code


### Deliverables

- one clear head-term cornerstone Claude Code page

- first high-priority compare set published

- first high-priority FAQ set published

- topic hub visibly links to cornerstone, compare, FAQ, glossary, and major deep dives

- cluster state can be inspected in one report or equivalent output


### Dependencies

- Phase 0 complete or sufficiently stable


### Exit criteria

- Claude Code has a recognizable hub-spoke structure

- at least one main entry page exists for the head term

- compare and FAQ gaps are materially reduced

- internal linking between flagship nodes is intentional and testable


### Risks if incomplete

- Claude Code remains a content pile rather than a flagship cluster

- future Codex replication lacks a proven template

- planner logic later has a weak pilot cluster to optimize against


---

## Phase 2 — Planner and queue insertion

### Objective

Decouple SEO/AEO asset generation from newsletter/blog exclusivity and create a direct graph-planning layer.

### Why this phase exists

The biggest structural bottleneck in the current system is that SEO generation behaves like a downstream byproduct of newsletter and blog selection. This phase inserts the architectural mechanism that allows raw signals and extracted intents to directly feed graph expansion.

### Scope

- planner module or equivalent

- asset queue model or equivalent

- direct entity/intent/compare/FAQ candidate → queue path

- queue-aware generation path

- dry-run planning mode

- topic completeness/state evaluation

- refresh vs create distinction


### Deliverables

- planner can inspect the current graph state

- planner can produce candidate assets without publishing

- generation can consume queue candidates

- at least one candidate path does not require prior newsletter selection

- topic completeness can be reported for Claude Code and reused for Codex later


### Dependencies

- Phase 0 complete

- Phase 1 sufficiently complete to provide a working pilot topic model


### Exit criteria

- dry-run planner output exists and is inspectable

- queue supports distinct asset types

- non-newsletter-originated candidate assets can be preview-generated

- refresh logic foundation exists even if not fully mature


### Risks if incomplete

- SEO remains effectively newsletter-gated

- raw signal underutilization continues

- flagship-topic growth stays manual and brittle


---

## Phase 3 — Codex replication

### Objective

Apply the proven flagship-topic template to Codex as the second flagship topic.

### Why this phase exists

Codex already shows promising demand and sits naturally within the same ecosystem as Claude Code. Replication is the proof that the system is reusable rather than custom-crafted for one topic.

### Scope

- Codex topic hub

- Codex cornerstone page

- first Codex FAQ wave

- first Codex compare wave

- Claude Code ↔ Codex ecosystem linking

- Codex topic-state reporting


### Deliverables

- Codex has a minimum-viable flagship cluster skeleton

- compare pages connect Codex to Claude Code and adjacent tools

- the same queue/planner structure can score Codex gaps


### Dependencies

- Phase 2 must be working enough to support repeatable backlog generation


### Exit criteria

- second flagship topic can be expanded using the same operating model

- replication requires configuration and editorial choices, not architectural reinvention


### Risks if incomplete

- the system remains overly dependent on Claude Code as a one-off pilot


---

## Phase 4 — Selective multilingual and adjacent-topic expansion

### Objective

Extend the system carefully into Chinese-localized growth and adjacent topic clusters after the English flagship model is working.

### Why this phase exists

This phase prevents premature scaling while still leaving room for faster growth once the core system proves itself.

### Scope

- selective Chinese asset creation from proven English winners

- localized Chinese FAQ and compare logic

- adjacent-topic scouting and controlled expansion

- optional refresh automation improvements


### Deliverables

- Chinese growth layer follows evidence rather than parity pressure

- adjacent topics are scored before expansion

- multilingual growth does not compromise flagship authority in English


### Dependencies

- English flagship model proven in practice

- planner and queue stable enough to support selective localization decisions


### Exit criteria

- multilingual expansion is selective, measurable, and non-chaotic

- adjacent topics follow the flagship framework rather than ad hoc publishing


---

## Recommended execution order for Claude Code

1. Complete Phase 0 fully.

2. Complete Phase 1 enough to make Claude Code visibly flagship-like.

3. Insert planner/queue in Phase 2.

4. Replicate with Codex in Phase 3.

5. Expand selectively in Phase 4.


Claude Code should not jump directly to planner insertion before Phase 0 and Phase 1 are reasonably stable.

---
