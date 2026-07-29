---
name: research
description: Research a topic to build a clear, current, evidence-backed understanding before any editorial angle or article is chosen. Use when the user asks to investigate, understand, explain, map, or deeply research a topic; asks what a community is discussing; or needs origins, official positions, competing definitions, mechanisms, controversies, representative sources, and practical implications. Produces research-plan.md, report.md, source-ledger.md, and ingest-candidates.md in a dedicated research workspace. Do not use to choose a publishable angle or analyze content-market opportunities; use /topic. Do not use to write an article; use /draft.
---

# Research — Understand the Topic

Read `AGENTS.md` before working in this repository.

Build a trustworthy mental model of the topic. Treat official sources, original authors,
community-native discussion, independent analysis, and criticism as different evidence roles.
Do not turn the report into a content strategy or article draft.

## Output principle

Write for a reader, not for a research auditor. Lead the reader through:

1. what the topic is;
2. where it came from and why it matters now;
3. how to understand its mechanism;
4. how it differs from adjacent concepts;
5. how the community is defining, advancing, and disputing it;
6. what it means for the target reader;
7. what to learn or try next.

Keep verification metadata in `source-ledger.md`. Keep `report.md` readable, with direct citations
near load-bearing claims.

## Arguments

Parse the request for:

- **Topic** — required. Ask if it is genuinely missing.
- **`depth:`** — `quick | standard | deep`; default `standard`.
- **Reader context** — infer from the request. If relevant, read `audience-profile.md`; do not
  require internal wiki coverage.
- **`as_of:`** — default to today. State it explicitly for fast-moving topics.
- **Reference / golden example** — if the user provides one, treat it as an editorial and
  coverage benchmark, not as evidence. Read `references/reference-benchmarking.md` before
  research and record what to preserve, what to verify, and the comparison criteria.

Depth controls breadth and verification effort, not a dependency on any named research tool:

- `quick`: establish the definition, current state, and best starting sources.
- `standard`: map origins, mechanisms, adjacent concepts, community discourse, and criticism.
- `deep`: expand source diversity, trace contested claims, inspect primary material, and run a
  stronger counter-evidence pass.

## Artifacts

Create a non-destructive workspace at `research/<slug>/`. If it exists, use the smallest free
`<slug>-rerun-N/`.

Write:

- `research-plan.md` — questions, ambiguities, channel choices, freshness boundary, and search
  lanes. This is a compact working document, not a user checkpoint.
- `report.md` — reader-facing research report. Read `references/report-template.md` before
  writing it.
- `source-ledger.md` — claim-level evidence, source roles, contradictions, and metric status.
  Read `references/source-ledger.md` and `references/source-quality.md`.
- `ingest-candidates.md` — a short checkbox list of sources worth later human review:
  `- [ ] <canonical URL> — <why it is worth preserving>`.

Never write research results directly into `raw/` or `wiki/`; never auto-ingest candidates.

## Workflow

### 1. Frame the research

Turn the topic into a question map:

- definition and necessary disambiguation;
- origin and timeline;
- mechanism or causal logic;
- adjacent concepts and boundaries;
- official or first-party positions;
- community-native definitions and disputes;
- evidence against the dominant narrative;
- implications for the target reader.

Record unknown entities and ambiguous meanings in `research-plan.md`. Resolve them through
evidence rather than silently choosing the most popular interpretation.

### 2. Discover broadly

Choose channels because they fit the topic, not because a fixed template demands them. Possible
channels include official sites, original essays, papers, GitHub, X, Reddit, Hacker News,
newsletters, blogs, talks, and videos.

Before using a browser for a channel, discover whether a dedicated connector, API, or MCP can
perform the required operation. Prefer the dedicated surface when it is available and
appropriately scoped; otherwise use a browser for direct, read-only observation, then public web
discovery or third-party snapshots as explicit fallbacks.

Search for distinct evidence roles:

- **Originators** — earliest traceable use, original proposal, or primary release.
- **Authorities** — official docs, maintainers, authors, datasets, or code.
- **Amplifiers** — people or pieces that made the topic spread.
- **Explainers** — sources that clarify mechanisms or boundaries.
- **Practitioners** — concrete implementations, results, and failure reports.
- **Critics** — counterarguments, falsifications, and hype checks.

For current products, APIs, commands, prices, deployment advice, or other operational
best-practice topics, create a **technical-contract lane**. Verify each actionable claim against
the canonical current source and record the surface, minimum version, access prerequisites,
provider or plan limits, beta status, and `as_of` date. Do not let a launch post or community
summary carry a runtime contract.

Read `references/community-discourse.md` when the topic is community-formed, definitionally
unstable, or driven by social discussion.

When X materially carries the origin, spread, definition, or dispute, also read
`references/x-community-research.md` and follow its routing, sampling, capture, and fallback
protocol. Do not add an X lane merely to fill a channel quota.

### 3. Deep-read the load-bearing sources

Do not synthesize from search snippets alone. Open the sources that carry the definition,
origin, numbers, causal claims, or central disagreement.

When subagents are available, use independent lanes for origin/facts, community discourse,
mechanism/comparison, and criticism. Give the main session distilled findings and source URLs,
not raw browsing noise. The coordinating agent remains responsible for reconciling conflicts.

### 4. Build the evidence ledger

Before drafting the report:

- canonicalize URLs;
- separate observed facts, source claims, and researcher synthesis;
- attach dates to time-sensitive claims;
- record competing evidence instead of averaging it away;
- counter-search claims containing `first`, `only`, `best`, `top`, `most`, or exact metrics;
- label engagement signals `observed`, `proxy`, or `unavailable`.
- preserve the observation surface, query boundary, timestamp, and displayed metric precision
  for social evidence.
- record the author's current affiliation, vendor relationship, sponsorship, customer status, or
  other dependency when it changes the source's independence;
- collapse posts, videos, newsletters, and interviews that repeat one person's test into one
  evidence chain rather than counting them as independent confirmation;
- for technical recommendations, attach the exact surface, version, prerequisites, limits, and
  verification path needed to execute them safely.

If actual performance data is absent, call a source `representative` or `high-signal`; do not
rank it as Top-N.

### 5. Run an adversarial pass

Ask what would make the current explanation wrong:

- Is the term older than the apparent origin?
- Are two unrelated meanings being conflated?
- Is a popular claim sourced only to people repeating one another?
- Is a supposed official source actually a third-party interpretation?
- Are examples demonstrations rather than production evidence?
- Is the report mistaking virality for truth?

Apply a **recommendation risk gate** to advice involving deletion, autonomous permissions,
production changes, migrations, paid actions, or high-stakes domains. Such advice needs:

1. direct primary evidence and a serious counter-evidence check;
2. a reversible pilot or canary with explicit success metrics;
3. rollback and permission boundaries;
4. a human Gate for irreversible or high-stakes consequences.

If these conditions are absent, downgrade the advice to a hypothesis to test. Distinguish
removing redundant prompt scaffolding from removing executable tests, acceptance checks, or
safety controls.

Update the ledger and soften or remove unsupported claims.

### 6. Write the reader journey

Follow `references/report-template.md`, adapting sections to the topic. Preserve the cognitive
sequence, not literal headings or quotas.

Translate complexity without erasing it:

- give an answer-first definition;
- use one strong analogy when it materially helps;
- surface competing definitions;
- compare adjacent concepts using one stable dimension;
- explain why the topic matters to this reader;
- end with proportionate next steps and a curated resource index.

For an actionable best-practice report, express recommendations as decision contracts:
**surface → when to use → action → evidence → boundary → how to verify**. State what new evidence
would change the recommendation. Avoid a universal “best” or “default” when the correct answer
depends on the reader's workload eval.

### 7. Quality check

Before finishing, verify:

- every load-bearing factual claim has a direct source;
- the report distinguishes fact, source opinion, and synthesis;
- origin and superlative claims show their search limits;
- community coverage includes disagreement, not just amplifiers;
- X-based community claims come from directly observed original posts or are explicitly marked
  `proxy` or `unavailable`;
- the explanation is useful to the stated reader without assuming wiki context;
- recommendations do not outrun the evidence;
- every claim containing `first`, `only`, `best`, `top`, `most`, `highest`, `always`, `never`,
  an exact metric, a quote, an identity, a version, a price, or a command has a matching ledger
  record or has been softened;
- technical instructions state their surface and prerequisites and do not silently mix API,
  CLI, subscription, provider, beta, and production behavior;
- high-risk recommendations include a reversible pilot, rollback, and the required human Gate;
- source independence is not overstated and repeated items from one evidence chain are not
  counted as corroboration;
- all four artifacts exist and links resolve syntactically.

## Boundary with other skills

- `/research` explains the topic and its discourse.
- `/topic` studies how existing content is packaged and received, finds editorial gaps, and
  proposes publishable angles.
- `/draft` writes an article from a selected topic brief and its evidence.

Do not generate angle cards, an outline, a guide, or a publication draft here.
