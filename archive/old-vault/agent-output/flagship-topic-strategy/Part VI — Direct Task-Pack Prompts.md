# Part VI — Direct Task-Pack Prompts for Claude Code

These prompts are intentionally written so they can be copied into Claude Code with minimal adaptation. The recommended usage pattern is:

- provide the overall strategy/spec once,

- then give Claude Code only one task-pack prompt at a time,

- require it to stop after validation,

- and require it to summarize blockers instead of guessing past them.


---

## Prompt Template A — Use for infrastructure / SEO tasks

Use this template for tasks like canonical cleanup, sitemap repair, schema support, queue insertion, and reporting.

```text
You are implementing a scoped task inside the LoreAI repo.

Read the implementation spec and execute ONLY the task described below.
Do not proceed to any later task automatically.
Do not redesign unrelated systems.
Preserve existing newsletter functionality unless this task explicitly changes it.
Prefer additive, reversible changes.
Use dry-run or preview-safe behavior whenever possible.

Execution rules:
1. First inspect the relevant files and summarize your intended changes briefly.
2. Then implement only this task.
3. Run validation checks appropriate to the task.
4. If validation fails, diagnose and retry up to 3 times.
5. If still blocked, stop and summarize the blocker precisely.
6. At the end, report:
   - files changed
   - key behavior changed
   - validations run
   - residual risks
   - whether the next task is now unblocked

Task:
[PASTE TASK PACK HERE]
```

---

## Prompt Template B — Use for content-cluster tasks

Use this template for tasks like cornerstone page creation, compare waves, FAQ waves, and cluster linking reinforcement.

```text
You are implementing a scoped flagship-topic content task inside the LoreAI repo.

Read the implementation spec and execute ONLY the task described below.
Do not proceed to any later task automatically.
Do not generate unbounded extra pages beyond the task scope.
Do not create competing pages for the same core intent unless the task explicitly requires that.
Preserve existing newsletter/blog generation behavior unless this task explicitly changes it.
Keep content editorially useful and structurally suited for SEO/AEO.

Execution rules:
1. Inspect relevant generation templates, existing related pages, and linking logic first.
2. Summarize the intended implementation briefly before making changes.
3. Implement only this task.
4. Validate page structure, metadata, links, and any schema requirements.
5. If blocked by content-model or routing ambiguity, stop and summarize the blocker precisely.
6. At the end, report:
   - files changed
   - pages created or updated
   - links added or changed
   - validations run
   - residual risks
   - whether the next task is now unblocked

Task:
[PASTE TASK PACK HERE]
```

---

## Ready-to-use Prompt — P0-1 Canonical URL consolidation

```text
You are implementing a scoped task inside the LoreAI repo.

Read the implementation spec and execute ONLY this task: P0-1 — Canonical URL consolidation.
Do not proceed to any later task automatically.
Do not redesign unrelated systems.
Preserve existing newsletter functionality unless this task explicitly changes it.
Prefer additive, reversible changes.
Use dry-run or preview-safe behavior whenever possible.

Task goal:
Establish one canonical URL policy for LoreAI and eliminate competing URL variants for flagship-topic pages.

Why it matters:
Flagship-topic authority compounds poorly if ranking signals are split across multiple URL variants.

Relevant touchpoints:
- canonical URL helpers
- route configuration
- page renderers/layouts where canonical tags are emitted
- sitemap generation logic
- redirect rules or equivalent canonical enforcement layer

Inputs:
- current live canonical behavior
- current sitemap output
- route patterns for blog/topics/faq/compare/glossary

Required changes:
- define one canonical URL pattern
- update canonical tag generation to match that pattern
- ensure sitemap only outputs canonical URLs
- ensure duplicate variants are redirected, suppressed, or canonically resolved

Do not change:
- page layouts
- content-type naming
- historical page inventory
- unrelated UI systems

Acceptance criteria:
- representative flagship-topic pages output the correct canonical URL
- sitemap lists only canonical variants
- duplicate variants no longer compete as independent discoverable URLs

Validation:
- inspect rendered canonical tags on representative pages
- inspect sitemap output
- verify representative variant behavior in preview/dev

Stop condition:
If route architecture is more fragmented than expected, stop and summarize the exact conflict instead of making speculative cross-site routing changes.

Execution rules:
1. First inspect the relevant files and summarize your intended changes briefly.
2. Then implement only this task.
3. Run validation checks appropriate to the task.
4. If validation fails, diagnose and retry up to 3 times.
5. If still blocked, stop and summarize the blocker precisely.
6. At the end, report:
   - files changed
   - key behavior changed
   - validations run
   - residual risks
   - whether the next task is now unblocked
```

---

## Ready-to-use Prompt — P0-2 Sitemap repair and validation

```text
You are implementing a scoped task inside the LoreAI repo.

Read the implementation spec and execute ONLY this task: P0-2 — Sitemap repair and validation.
Do not proceed to any later task automatically.
Preserve existing newsletter functionality unless this task explicitly changes it.
Prefer additive, reversible changes.

Task goal:
Repair sitemap generation so it is valid, deterministic, and aligned with canonical policy.

Why it matters:
Search engines need a clean discovery surface, especially for new topic clusters.

Relevant touchpoints:
- sitemap generator
- content enumeration logic
- content-type route mapping
- validation helpers/tests if available

Inputs:
- current sitemap output
- content inventory and route patterns
- canonical policy from P0-1

Required changes:
- remove invalid entries
- eliminate undefined or malformed URLs
- ensure flagship pages are present and represented once
- make sitemap generation deterministic and inspectable

Do not change:
- unrelated content selection rules unless needed for correctness
- speculative sitemap segmentation beyond what is required now

Acceptance criteria:
- no undefined entries
- no obviously duplicate canonical rows
- representative flagship pages appear in sitemap
- sitemap generation is stable across repeated runs

Validation:
- inspect generated sitemap files
- compare against representative content inventory rows
- run any available tests or local validation checks

Stop condition:
If content-source inconsistencies make perfect coverage impossible in this pass, document the mismatch rather than masking it with hardcoded exceptions.

Execution rules:
1. Inspect the relevant files and summarize intended changes briefly.
2. Implement only this task.
3. Run validations.
4. Retry up to 3 times if blocked by fixable issues.
5. If still blocked, stop and summarize precisely.
6. Report files changed, behavior changed, validations run, residual risks, and whether the next task is unblocked.
```

---

## Ready-to-use Prompt — P0-3 FAQ schema support

```text
You are implementing a scoped task inside the LoreAI repo.

Read the implementation spec and execute ONLY this task: P0-3 — FAQ schema support.
Do not proceed to any later task automatically.
Preserve existing rendering behavior unless required for schema correctness.
Prefer additive, reversible changes.

Task goal:
Add valid FAQPage structured data to FAQ pages.

Why it matters:
FAQ pages are one of the most AEO-friendly and rich-result-friendly asset types, but only if the page structure and schema are aligned.

Relevant touchpoints:
- FAQ page renderer/template
- schema/JSON-LD emitters
- content parsing for FAQ question-answer pairs

Inputs:
- current FAQ content structure
- representative FAQ pages
- site schema patterns if any exist already

Required changes:
- emit valid FAQPage structured data on FAQ pages
- map question-answer pairs from page content into schema
- ensure schema output is consistent with visible content

Do not change:
- FAQ content model unless needed for schema correctness
- non-FAQ pages indiscriminately

Acceptance criteria:
- representative FAQ pages output FAQPage structured data
- question-answer schema matches visible content
- schema is preview-testable

Validation:
- inspect rendered JSON-LD output
- verify alignment with visible Q&A blocks
- run structured data validation if available locally or via preview inspection workflow

Stop condition:
If FAQ content structures vary too much for a universal mapper, implement the safest common path and document exceptions rather than over-generalizing.

Execution rules:
1. Inspect the relevant files and summarize intended changes briefly.
2. Implement only this task.
3. Run validations.
4. Retry up to 3 times if blocked by fixable issues.
5. If still blocked, stop and summarize precisely.
6. Report files changed, behavior changed, validations run, residual risks, and whether the next task is unblocked.
```

---

## Ready-to-use Prompt — P1-1 Claude Code cornerstone page

```text
You are implementing a scoped flagship-topic content task inside the LoreAI repo.

Read the implementation spec and execute ONLY this task: P1-1 — Claude Code cornerstone page.
Do not proceed to any later task automatically.
Do not generate unbounded extra pages beyond the task scope.
Do not create competing pages for the same core intent.
Preserve existing newsletter/blog generation behavior unless this task explicitly changes it.
Keep content editorially useful and structurally suited for SEO/AEO.

Task goal:
Create the canonical head-term page for Claude Code.

Why it matters:
A flagship topic needs a primary head-term target page that acts as the cluster center of gravity.

Relevant touchpoints:
- content generation/template for cornerstone pages or blog pages
- topic hub links
- homepage flagship links
- metadata/title/description generation for the page

Inputs:
- existing Claude Code topic hub
- existing Claude Code deep dives
- cluster audit and missing-intent analysis

Required changes:
- create one primary Claude Code cornerstone page targeting the core entry intent
- ensure page links outward to setup, compare, FAQ, glossary, and key deep dives
- ensure hub and homepage can point to it appropriately

Do not change:
- do not create multiple competing head-term pages for the same intent
- do not leave the cornerstone page isolated from the rest of the cluster

Acceptance criteria:
- one clear primary head-term page exists
- metadata/title clearly target the core entry query
- page is internally linked as the cluster center

Validation:
- inspect rendered page structure and metadata
- inspect links to and from hub, compare, FAQ, glossary, and supporting pages
- verify no competing duplicate head-term target is introduced unintentionally

Execution rules:
1. Inspect relevant generation templates, existing related pages, and linking logic first.
2. Summarize intended implementation briefly before making changes.
3. Implement only this task.
4. Validate page structure, metadata, links, and any schema requirements.
5. If blocked by content-model or routing ambiguity, stop and summarize the blocker precisely.
6. Report files changed, pages created or updated, links added or changed, validations run, residual risks, and whether the next task is unblocked.
```

---

## Ready-to-use Prompt — P1-2 Claude Code compare wave 1

```text
You are implementing a scoped flagship-topic content task inside the LoreAI repo.

Read the implementation spec and execute ONLY this task: P1-2 — Claude Code compare wave 1.
Do not proceed to any later task automatically.
Do not generate unbounded extra pages beyond the task scope.
Preserve existing newsletter/blog generation behavior unless this task explicitly changes it.
Keep content editorially useful and structurally suited for SEO/AEO.

Task goal:
Publish the first wave of high-priority Claude Code comparison pages.

Suggested first set:
- Claude Code vs Cursor
- Claude Code vs GitHub Copilot
- Claude Code vs Codex

Why it matters:
Compare pages capture mid-funnel decision intent and are one of the clearest missing node types in the current cluster.

Relevant touchpoints:
- compare page generator/template
- compare metadata/title logic
- topic hub and cornerstone linking
- related-links logic

Inputs:
- compare gap analysis
- existing compare pages if any
- cluster audit findings

Required changes:
- create the first compare set using a consistent comparison structure
- link them from the Claude Code hub and cornerstone page
- link compare pages back into the cluster and across adjacent compare pages where appropriate

Do not change:
- do not generate a wide compare library in this task
- do not use inconsistent templates across the first wave

Acceptance criteria:
- pages exist for the first compare set
- page titles and metadata align with comparison intent
- compare pages are internally discoverable from the cluster center

Validation:
- inspect page titles, headings, metadata, and cross-links
- verify compare pages appear in relevant hub/cornerstone sections
- confirm no broken compare links

Execution rules:
1. Inspect relevant generation templates, existing related pages, and linking logic first.
2. Summarize intended implementation briefly before making changes.
3. Implement only this task.
4. Validate page structure, metadata, links, and any schema requirements.
5. If blocked by content-model or routing ambiguity, stop and summarize the blocker precisely.
6. Report files changed, pages created or updated, links added or changed, validations run, residual risks, and whether the next task is unblocked.
```

---

## Ready-to-use Prompt — P1-3 Claude Code FAQ wave 1

```text
You are implementing a scoped flagship-topic content task inside the LoreAI repo.

Read the implementation spec and execute ONLY this task: P1-3 — Claude Code FAQ wave 1.
Do not proceed to any later task automatically.
Do not generate unbounded extra pages beyond the task scope.
Preserve existing newsletter/blog generation behavior unless this task explicitly changes it.
Keep content editorially useful and structurally suited for SEO/AEO.

Task goal:
Publish the first wave of high-priority Claude Code FAQ pages.

Suggested first set:
- Is Claude Code free?
- How much does Claude Code cost?
- How do you install Claude Code?
- Can Claude Code work offline?
- Does Claude Code support Windows?
- How do you use Claude Code with monorepos?

Why it matters:
FAQ pages are the clearest path to long-tail answer coverage and AEO extraction.

Relevant touchpoints:
- FAQ content generation/template
- FAQ schema support
- topic hub/cornerstone links
- related-links logic

Inputs:
- FAQ gap analysis
- existing Claude Code FAQ pages if any
- cluster audit findings

Required changes:
- create the first FAQ set
- ensure FAQ schema is emitted
- ensure FAQ pages link back to the cornerstone and hub
- keep answers concise enough to be extractable while still useful

Do not change:
- do not generate an unbounded FAQ set in this task
- do not make FAQ pages thin stubs with low editorial value

Acceptance criteria:
- pages exist for the first FAQ set
- FAQ schema is present and correct
- FAQ pages are connected into the Claude Code cluster

Validation:
- inspect rendered FAQ pages
- inspect schema output
- inspect links to hub, cornerstone, and adjacent FAQ pages where relevant

Execution rules:
1. Inspect relevant generation templates, existing related pages, and linking logic first.
2. Summarize intended implementation briefly before making changes.
3. Implement only this task.
4. Validate page structure, metadata, links, and any schema requirements.
5. If blocked by content-model or routing ambiguity, stop and summarize the blocker precisely.
6. Report files changed, pages created or updated, links added or changed, validations run, residual risks, and whether the next task is unblocked.
```

---

## Ready-to-use Prompt — P2-1 Planner dry-run mode

```text
You are implementing a scoped task inside the LoreAI repo.

Read the implementation spec and execute ONLY this task: P2-1 — Planner dry-run mode.
Do not proceed to any later task automatically.
Do not force publishing inside planner logic.
Prefer additive, reversible changes.
Use dry-run or preview-safe behavior whenever possible.

Task goal:
Introduce a planner that can inspect topic graph state and produce candidate assets without publishing.

Why it matters:
This is the first step that breaks the current newsletter-gated production logic.

Relevant touchpoints:
- entity extraction outputs
- keyword/topic cluster data access
- candidate scoring logic
- new planner module
- dry-run reporting utilities

Inputs:
- keyword and topic tables or equivalent
- compare candidates / FAQ candidates if derivable
- existing content inventory for gap detection
- flagship topic priority list

Required changes:
- implement a planner path that reads current state and detects missing nodes
- score candidate assets by type and topic
- output inspectable candidate results without publishing side effects

Do not change:
- do not force publishing inside planner logic
- do not hardwire the planner to Claude Code only, even if Claude Code is the first priority topic

Acceptance criteria:
- planner dry-run can report missing Claude Code nodes by type
- candidate outputs are inspectable and understandable
- no publish side effects are required to validate planner behavior

Validation:
- run planner in dry-run mode
- inspect output for candidate types and priorities
- verify candidate set includes known missing Claude Code compare and FAQ nodes

Stop condition:
If current DB/content mismatch prevents trustworthy gap detection, stop and report the mismatch precisely rather than embedding fragile assumptions silently.

Execution rules:
1. Inspect the relevant files and summarize intended changes briefly.
2. Implement only this task.
3. Run validations.
4. Retry up to 3 times if blocked by fixable issues.
5. If still blocked, stop and summarize precisely.
6. Report files changed, behavior changed, validations run, residual risks, and whether the next task is unblocked.
```

---
