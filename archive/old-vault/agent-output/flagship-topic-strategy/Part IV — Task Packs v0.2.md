# Part IV — Task Packs v0.2

Each task pack is designed to be independently executable by Claude Code with minimal ambiguity.

## Task pack rules

- One task pack should address one coherent problem.

- A task pack may touch multiple files, but should avoid spanning too many architectural layers at once.

- A task pack should include required outcomes and explicit non-goals.

- Claude Code should stop after completing one task pack and validating it, rather than guessing the next step.

- Each task pack should prefer dry-run or preview validation where available.


---

## Task Pack P0-1 — Canonical URL consolidation

### Goal

Establish one canonical URL policy for LoreAI and eliminate competing URL variants for flagship-topic pages.

### Why it matters

Flagship-topic authority compounds poorly if ranking signals are split across multiple URL variants.

### Relevant touchpoints

- canonical URL helpers

- route configuration

- page renderers/layouts where canonical tags are emitted

- sitemap generation logic

- redirect rules or equivalent canonical enforcement layer


### Inputs

- existing canonical behavior in live pages

- current sitemap output

- current route patterns for blog/topics/faq/compare/glossary


### Required changes

- define one canonical URL pattern

- update canonical tag generation to match that pattern

- ensure sitemap only outputs canonical URLs

- ensure duplicate variants are redirected, suppressed, or canonically resolved


### Do not change

- do not redesign page layouts

- do not rename content types

- do not delete historical pages

- do not introduce a second canonical policy path


### Acceptance criteria

- representative flagship-topic pages output the correct canonical URL

- sitemap lists only canonical variants

- duplicate variants no longer compete as independent discoverable URLs


### Validation

- inspect rendered canonical tags on representative pages

- inspect sitemap output

- verify representative variant behavior in preview/dev


### Stop conditions

- if route architecture is more fragmented than expected, stop and summarize the exact conflict instead of making speculative cross-site routing changes


---

## Task Pack P0-2 — Sitemap repair and validation

### Goal

Repair sitemap generation so it is valid, deterministic, and aligned with canonical policy.

### Why it matters

Search engines need a clean discovery surface, especially for new topic clusters.

### Relevant touchpoints

- sitemap generator

- content enumeration logic

- content-type route mapping

- validation helpers/tests if available


### Inputs

- current sitemap output

- content inventory and route patterns

- canonical policy from P0-1


### Required changes

- remove invalid entries

- eliminate undefined or malformed URLs

- ensure flagship pages are present and represented once

- make sitemap generation deterministic and inspectable


### Do not change

- do not change unrelated content selection rules unless needed for correctness

- do not add speculative sitemap segmentation beyond what is required now


### Acceptance criteria

- no undefined entries

- no obviously duplicate canonical rows

- representative flagship pages appear in sitemap

- sitemap generation is stable across repeated runs


### Validation

- inspect generated sitemap files

- compare against representative content inventory rows

- run any available tests or local validation checks


### Stop conditions

- if content-source inconsistencies make perfect coverage impossible in this pass, document the mismatch rather than masking it with hardcoded exceptions


---

## Task Pack P0-3 — FAQ schema support

### Goal

Add valid FAQPage structured data to FAQ pages.

### Why it matters

FAQ pages are one of the most AEO-friendly and rich-result-friendly asset types, but only if the page structure and schema are aligned.

### Relevant touchpoints

- FAQ page renderer/template

- schema/JSON-LD emitters

- content parsing for FAQ question-answer pairs


### Inputs

- current FAQ content structure

- representative FAQ pages

- site schema patterns if any exist already


### Required changes

- emit valid FAQPage structured data on FAQ pages

- map question-answer pairs from page content into schema

- ensure schema output is consistent with visible content


### Do not change

- do not redesign FAQ content model unless needed for schema correctness

- do not apply FAQ schema to non-FAQ page types indiscriminately


### Acceptance criteria

- representative FAQ pages output FAQPage structured data

- question-answer schema matches visible content

- schema is preview-testable


### Validation

- inspect rendered JSON-LD output

- verify alignment with visible Q&A blocks

- run structured data validation if available locally or via preview inspection workflow


### Stop conditions

- if FAQ content structures vary too much for a universal mapper, implement the safest common path and document exceptions rather than over-generalizing


---

## Task Pack P0-4 — Homepage flagship-topic discovery module

### Goal

Expose flagship-topic entry points from the homepage or equivalent top-level discovery surface.

### Why it matters

A flagship topic should not be discoverable only through deep navigation or chance internal links.

### Relevant touchpoints

- homepage modules/components

- topic card/list components

- content selection logic for homepage topic highlights


### Inputs

- current homepage structure

- current topic hub availability

- flagship priority list with Claude Code first


### Required changes

- add or improve a homepage module that surfaces flagship topics

- ensure Claude Code is included as the first flagship topic

- link discovery entry points to canonical topic destinations


### Do not change

- do not perform a full homepage redesign

- do not convert homepage into a topic-only experience


### Acceptance criteria

- homepage or equivalent surface clearly exposes flagship-topic entry points

- links point to canonical destinations

- implementation fits existing design patterns reasonably well


### Validation

- preview homepage rendering

- click through to canonical topic destinations

- verify no duplicate or broken homepage topic links


---

## Task Pack P1-1 — Claude Code cornerstone page

### Goal

Create the canonical head-term page for Claude Code.

### Why it matters

A flagship topic needs a primary head-term target page that acts as the cluster center of gravity.

### Relevant touchpoints

- content generation/template for cornerstone pages or blog pages

- topic hub links

- homepage flagship links

- metadata/title/description generation for the page


### Inputs

- existing Claude Code topic hub

- existing Claude Code deep dives

- cluster audit and missing-intent analysis


### Required changes

- create one primary Claude Code cornerstone page targeting the core entry intent

- ensure page links outward to setup, compare, FAQ, glossary, and key deep dives

- ensure hub and homepage can point to it appropriately


### Do not change

- do not create multiple competing head-term pages for the same intent

- do not leave cornerstone isolated from the rest of the cluster


### Acceptance criteria

- one clear primary head-term page exists

- metadata/title clearly target the core entry query

- page is internally linked as the cluster center


### Validation

- inspect rendered page structure and metadata

- inspect links to and from hub, compare, FAQ, glossary, and supporting pages

- verify no competing duplicate head-term target is introduced unintentionally


---

## Task Pack P1-2 — Claude Code compare wave 1

### Goal

Publish the first wave of high-priority Claude Code comparison pages.

### Why it matters

Compare pages capture mid-funnel decision intent and are one of the clearest missing node types in the current cluster.

### Suggested first set

- Claude Code vs Cursor

- Claude Code vs GitHub Copilot

- Claude Code vs Codex


### Relevant touchpoints

- compare page generator/template

- compare metadata/title logic

- topic hub and cornerstone linking

- related-links logic


### Inputs

- compare gap analysis

- existing compare pages if any

- cluster audit findings


### Required changes

- create the first compare set using a consistent comparison structure

- link them from the Claude Code hub and cornerstone page

- link compare pages back into the cluster and across adjacent compare pages where appropriate


### Do not change

- do not generate a wide compare library in this task

- do not use inconsistent templates across the first wave


### Acceptance criteria

- pages exist for the first compare set

- page titles and metadata align with comparison intent

- compare pages are internally discoverable from the cluster center


### Validation

- inspect page titles, headings, metadata, and cross-links

- verify compare pages appear in relevant hub/cornerstone sections

- confirm no broken compare links


---

## Task Pack P1-3 — Claude Code FAQ wave 1

### Goal

Publish the first wave of high-priority Claude Code FAQ pages.

### Why it matters

FAQ pages are the clearest path to long-tail answer coverage and AEO extraction.

### Suggested first set

- Is Claude Code free?

- How much does Claude Code cost?

- How do you install Claude Code?

- Can Claude Code work offline?

- Does Claude Code support Windows?

- How do you use Claude Code with monorepos?


### Relevant touchpoints

- FAQ content generation/template

- FAQ schema support

- topic hub/cornerstone links

- related-links logic


### Inputs

- FAQ gap analysis

- existing Claude Code FAQ pages if any

- cluster audit findings


### Required changes

- create the first FAQ set

- ensure FAQ schema is emitted

- ensure FAQ pages link back to the cornerstone and hub

- keep answers concise enough to be extractable while still useful


### Do not change

- do not generate an unbounded FAQ set in this task

- do not make FAQ pages thin stubs with low editorial value


### Acceptance criteria

- pages exist for the first FAQ set

- FAQ schema is present and correct

- FAQ pages are connected into the Claude Code cluster


### Validation

- inspect rendered FAQ pages

- inspect schema output

- inspect links to hub, cornerstone, and adjacent FAQ pages where relevant


---

## Task Pack P1-4 — Claude Code cluster linking reinforcement

### Goal

Reinforce internal linking across the Claude Code flagship cluster.

### Why it matters

A cluster is only a cluster if discovery and authority can flow between nodes.

### Relevant touchpoints

- topic hub sections

- related links helpers

- glossary cross-links

- compare/FAQ navigation sections


### Inputs

- current Claude Code asset map

- current internal-link patterns

- missing-link analysis if available


### Required changes

- ensure hub links to cornerstone, compare, FAQ, glossary, and major deep dives

- ensure cornerstone links to major child nodes

- ensure child nodes link back to cluster center and to adjacent nodes where useful


### Do not change

- do not add spammy or repetitive templated link blocks everywhere

- do not create unrelated cross-topic link clutter


### Acceptance criteria

- major Claude Code nodes are mutually discoverable

- link placement feels intentional and editorially coherent

- cluster center is obvious from internal-link structure


### Validation

- manually inspect representative pages

- run any link integrity checks available

- verify no obvious broken or circularly broken paths


---

## Task Pack P2-1 — Planner dry-run mode

### Goal

Introduce a planner that can inspect topic graph state and produce candidate assets without publishing.

### Why it matters

This is the first step that breaks the current newsletter-gated production logic.

### Relevant touchpoints

- entity extraction outputs

- keyword/topic cluster data access

- candidate scoring logic

- new planner module

- dry-run reporting utilities


### Inputs

- keyword and topic tables or equivalent

- compare candidates / FAQ candidates if derivable

- existing content inventory for gap detection

- flagship topic priority list


### Required changes

- implement a planner path that reads current state and detects missing nodes

- score candidate assets by type and topic

- output inspectable candidate results without publishing side effects


### Do not change

- do not force publishing inside planner logic

- do not hardwire the planner to Claude Code only, even if Claude Code is the first priority topic


### Acceptance criteria

- planner dry-run can report missing Claude Code nodes by type

- candidate outputs are inspectable and understandable

- no publish side effects are required to validate planner behavior


### Validation

- run planner in dry-run mode

- inspect output for candidate types and priorities

- verify candidate set includes known missing Claude Code compare and FAQ nodes


### Stop conditions

- if current DB/content mismatch prevents trustworthy gap detection, stop and report the mismatch precisely rather than embedding fragile assumptions silently


---

## Task Pack P2-2 — Queue-backed generation path

### Goal

Allow generation scripts to consume planner queue entries directly.

### Why it matters

Without this step, the planner remains observational rather than operational.

### Relevant touchpoints

- generation entrypoints/scripts

- queue model or equivalent intermediate representation

- content write path

- preview/dry-run safeguards


### Inputs

- planner candidate outputs

- existing generation templates by page type

- content persistence path


### Required changes

- make generation consume queue entries for at least: faq, compare, glossary, topic_hub, cornerstone_blog

- allow preview or controlled execution without requiring newsletter selection first

- preserve existing newsletter/blog generation paths while adding the new queue path


### Do not change

- do not remove legacy generation paths in this task

- do not bypass preview safeguards


### Acceptance criteria

- at least one non-newsletter-originated candidate can go from queue to generated preview asset

- queue distinguishes page types correctly

- existing generation paths remain functional


### Validation

- run a controlled queue-backed preview generation

- inspect generated output

- confirm page type routing/template selection is correct


---

## Task Pack P2-3 — Topic state and completeness report

### Goal

Create a report that measures flagship-topic completeness and major graph gaps.

### Why it matters

The system should optimize for cluster completeness, not just publication count.

### Relevant touchpoints

- content inventory logic

- topic/cluster metadata

- planner or reporting utilities

- internal-link inspection helpers if available


### Inputs

- current content inventory

- topic/cluster associations

- queue/planner outputs if present


### Required changes

- implement a reusable completeness report for a topic

- include counts by page type

- include major missing-node categories

- include a basic notion of link or discovery weakness if derivable


### Do not change

- do not make the report Claude-Code-only in structure

- do not tie reporting to one-off hand-curated values


### Acceptance criteria

- Claude Code completeness can be inspected in one report

- Codex can be evaluated with the same structure later

- report is useful for prioritizing next-wave generation


### Validation

- generate report for Claude Code

- inspect counts and missing-node signals

- verify report structure is reusable for Codex


---

## Task Pack P2-4 — Refresh vs create distinction

### Goal

Teach the system to distinguish between new-node creation and existing-node refresh.

### Why it matters

Flagship-topic systems should compound by improving important pages, not only by endlessly spawning new ones.

### Relevant touchpoints

- planner candidate logic

- queue model

- generation/update path

- topic-state reporting


### Inputs

- existing high-value content pages

- freshness or update signals

- planner candidate outputs


### Required changes

- introduce a distinction between create and refresh candidates

- ensure candidate output can indicate update intent

- make refresh previewable without duplicating target pages


### Do not change

- do not attempt full refresh automation for every page type in this task

- do not create silent duplicate pages when refresh should have been chosen


### Acceptance criteria

- queue or candidate output can distinguish create vs refresh

- at least one clear refresh scenario can be represented

- system avoids obvious duplication behavior in preview mode


### Validation

- inspect planner/queue output for create vs refresh modes

- simulate or preview one refresh path safely


---

## Task Pack P3-1 — Codex flagship skeleton

### Goal

Replicate the flagship-topic pattern to Codex as the second target cluster.

### Why it matters

Replication is proof that the system is reusable.

### Relevant touchpoints

- topic hub generation/path

- cornerstone generation/path

- compare/FAQ generation templates

- topic-state reporting


### Inputs

- Codex topic signals and GSC evidence

- queue/planner outputs

- Claude Code flagship structure as template


### Required changes

- create Codex hub and cornerstone skeleton

- create first Codex compare and FAQ set

- ensure topic-state reporting works for Codex


### Do not change

- do not broaden into many adjacent topics in this task

- do not special-case Codex so heavily that the pattern becomes non-reusable


### Acceptance criteria

- Codex has a visible flagship skeleton

- same operating model used for Claude Code can be applied here

- cross-links between Codex and Claude Code are sensible where relevant


### Validation

- inspect Codex topic-state report

- inspect representative pages and links

- verify no new architectural exceptions were required unnecessarily


---
