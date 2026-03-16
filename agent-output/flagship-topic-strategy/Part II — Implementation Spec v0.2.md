# Part II — Implementation Spec v0.2

This section is intentionally structured in a Claude-Code-friendly way, following a six-layer spec format so an agent with minimal project context can execute with fewer architecture guesses.

## Layer 1 — Goal and background

### Goal

Implement the first architectural shift required for LoreAI to become a **flagship-topic-driven SEO/AEO system** instead of a **newsletter-gated SEO byproduct system**.

### Background

LoreAI already has strong raw signal ingestion and a meaningful body of topic content, especially around Claude Code. However, the current pipeline still behaves like:

**Collect → Newsletter → Blog → SEO**

This means SEO assets are often starved by upstream selection even when the signal layer is rich. The current system therefore underuses collected information, underuses extracted keywords and topic clusters, and fails to complete flagship topic clusters.

At the same time, technical SEO issues are suppressing discoverability of already-existing assets. Therefore this implementation wave must address both:

- **architectural production logic**, and

- **technical visibility foundations**.


### Desired outcome

After this phase:

- newsletter still exists and still publishes,

- but newsletter is no longer the practical gatekeeper for SEO/AEO asset creation,

- technical SEO blockers no longer suppress flagship-topic pages,

- Claude Code becomes the first minimum-viable flagship cluster,

- and the codebase gains the foundation for planner-led topic graph generation.


### Constraints

- Preserve the existing newsletter pipeline.

- Prefer additive changes over destructive rewrite.

- Support dry-run-first execution where possible.

- Avoid broad UI redesign in this phase.

- Focus on English flagship authority first.

- Chinese is not a full parity goal in this phase.


---

## Layer 2 — Technical design

### Core architectural change

Insert a **planner-compatible topic graph layer** between extraction and generation.

### New canonical flow

**Signal Ingestion → Normalization → Entity / Intent / Compare Extraction → Topic Graph Planner → Asset Queue → Generate / Refresh → Validate / Link / Schema → Publish → Distribute**

### What this means in practice

#### A. Newsletter becomes downstream distribution

Newsletter should continue to consume valuable signals and finished content, but it should not be the only path by which SEO/AEO assets are generated.

#### B. Generation should support direct planner input

SEO generation must be able to consume candidate assets directly from a planner queue, even if those candidates never became newsletter items or blog seeds.

#### C. Page-type-aware generation

The system should support distinct asset types:

- topic_hub

- cornerstone_blog

- blog

- faq

- compare

- glossary

- refresh

- relink/enrichment tasks where useful


#### D. Topic state and completeness tracking

For flagship topics, the system should be able to inspect current coverage and answer:

- Does a topic hub exist?

- Does a cornerstone page exist?

- How many blogs / FAQ / compare / glossary nodes exist?

- Which high-priority compare pairs are missing?

- Which high-priority FAQ intents are missing?

- Which nodes are weakly linked?

- Which nodes should be refreshed instead of duplicated?


#### E. Technical SEO foundation

This implementation wave must also enforce:

- one canonical URL pattern,

- stable sitemap output,

- FAQ schema on FAQ pages,

- homepage discovery paths for flagship topics,

- cluster-internal discoverability.


### Phase-specific design intent

#### This phase must achieve

- one canonical URL policy,

- fixed sitemap behavior,

- FAQ schema support,

- homepage-to-flagship-topic discovery,

- a planner-compatible queue model,

- a direct entity/intent → queue path,

- Claude Code flagship cluster completion wave 1.


#### This phase does not need to achieve

- full multilingual parity,

- full replacement of every historical script,

- complete automation for all future topics,

- complete redesign of site navigation,

- speculative support for every low-signal topic.


---

## Layer 3 — File structure and implementation touchpoints

The exact file map should be confirmed against the repo during execution, but implementation should be guided by the following structure.

### Likely files/modules to modify

#### Collection / extraction / generation path

- collection scripts

- entity extraction scripts

- SEO generation scripts

- DB utilities and migration files

- internal-link helpers

- topic inspection utilities


#### Rendering / SEO path

- page renderers for FAQ pages

- schema/structured data emitters

- canonical URL logic

- sitemap generation

- homepage topic-discovery modules


#### New modules likely to be added

- planner module

- asset queue module

- topic state / completeness evaluator

- dry-run reporting module

- cluster backlog reporter


### File-planning rules

- Prefer placing new planner logic in a clearly separated module rather than burying it inside generation scripts.

- Prefer additive helpers rather than rewriting all historical code paths at once.

- Preserve existing newsletter-related modules unless directly necessary.

- Do not delete historical content files.

- Do not introduce a second competing canonical-policy implementation.


### Files or areas that should not be broadly refactored in this phase

- broad front-end design system

- unrelated UI components

- deployment platform configuration unless absolutely required

- large-scale historical prompt rewrites not directly required for planner insertion


---

## Layer 4 — Acceptance criteria

This phase should be accepted only when all of the following are true.

### A. Technical SEO acceptance

- There is a single canonical URL pattern for flagship-topic pages.

- Sitemap output no longer contains invalid URLs.

- Duplicate URL variants are redirected, suppressed, or canonically resolved.

- FAQ pages emit valid FAQPage structured data.

- Homepage exposes flagship topic entry points.


### B. Planner and queue acceptance

- The system can derive candidate assets from raw signals and extracted entities/intents without requiring newsletter selection first.

- The queue can distinguish at least: topic_hub, cornerstone_blog, faq, compare, glossary, refresh.

- The queue supports dry-run inspection.

- Claude Code gaps can be surfaced in a machine-readable or inspectable report.


### C. Claude Code cluster acceptance

- A canonical Claude Code cornerstone page exists.

- The first wave of Claude Code compare pages exists.

- The first wave of Claude Code FAQ pages exists.

- The topic hub links to the key flagship nodes.

- Key flagship nodes link back into the hub and adjacent nodes.


### D. Safety acceptance

- Newsletter generation still works.

- Existing blog generation still works.

- Historical content remains intact.

- New migrations are safely re-runnable or reversible.

- New queue/planner logic can be previewed without forced publish side effects.


### E. Manual review acceptance

- Flagship pages read like authoritative editorial assets rather than thin generated fill.

- Compare pages have clear positioning and useful differentiation.

- FAQ pages provide concise, extractable answers suitable for AEO.

- Internal linking feels intentional rather than purely templated.


---

## Layer 5 — Autonomous execution configuration

This section defines how Claude Code should execute in a headless or semi-autonomous mode.

### Execution mode

- Prefer phase-aware execution.

- Prefer one task pack at a time, even if the full strategy/spec is loaded.

- Use dry-run-first behavior wherever publishing side effects are possible.


### Execution loop

For each task pack:

1. inspect relevant files,

2. implement only the scoped change,

3. run the appropriate validation commands/checks,

4. if validation fails, attempt to diagnose and fix,

5. retry up to 3 times,

6. if still failing, stop, summarize blocker, and do not continue to the next task pack blindly.


### Validation expectations

Each task should validate through some combination of:

- build/test checks,

- sitemap inspection,

- schema inspection,

- canonical inspection,

- topic-state report inspection,

- queue dry-run output inspection,

- sample page rendering checks.


### Safety behavior

- Do not delete historical content to "clean up" state.

- Do not silently rename or repurpose content types.

- Do not bypass dry-run logic if a write path is available but preview is possible.

- Do not refactor unrelated modules opportunistically.

- Preserve newsletter functionality even while removing its gatekeeper role for SEO/AEO generation.


### Suggested commit discipline

- Make scoped commits by task pack or step.

- Prefer reversible increments over large monolithic changes.

- Document blockers when execution stops.


---

## Layer 6 — Out of scope

The following are explicitly out of scope for this implementation wave:

- full Chinese graph mirror,

- full UI redesign,

- GA4 integration,

- full rewrite of the newsletter pipeline,

- broad dependency upgrades,

- speculative expansion to many low-signal topics,

- total historical content normalization,

- complete redesign of all prompts in the repo.


---

## Supporting data model guidance

If needed, implementation may introduce a lightweight queue/state model. Exact schema can be finalized during coding, but the system should support the following logical entities.

### asset_queue

Suggested logical fields:

- id

- topic_slug

- cluster_slug

- asset_type

- target_slug

- language

- priority_score

- status

- source_evidence

- creation_mode (create / refresh / relink)

- created_at

- updated_at


### topic_state

Suggested logical fields:

- topic_slug

- has_hub

- has_cornerstone

- blog_count

- faq_count

- compare_count

- glossary_count

- missing_compare_count

- missing_faq_count

- missing_glossary_count

- link_coverage_score

- freshness_score

- updated_at


### Migration requirements

- migrations must be idempotent,

- historical content should not be destroyed,

- backfill should be possible from existing content and keyword/topic data.


---

## Validation summary

Every phase should support:

- dry-run queue generation,

- local or preview URL inspection,

- sitemap inspection,

- schema inspection,

- topic-state report inspection,

- link integrity inspection,

- build and publish safety checks.
