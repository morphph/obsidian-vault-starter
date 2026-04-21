# GBrain + GStack — GitHub Deep Scan

**Sources:**
- https://github.com/garrytan/gbrain (9,718 stars, TypeScript, updated 2026-04-21)
- https://github.com/garrytan/gstack (78,692 stars, TypeScript, updated 2026-04-21)

**Author:** Garry Tan (@garrytan)
**Fetched:** 2026-04-21 via `gh` CLI (GitHub Deep Scan)
**Context:** These are the production open-source stack referenced in Garry's 2026-04-15 "Resolvers" article — the knowledge layer (GBrain) + skills layer (GStack) that together with OpenClaw/Hermes Agent form the thin-harness/fat-skills architecture.

---

## GBrain

**Tagline:** "Your AI agent is smart but forgetful. GBrain gives it a brain."

**Production scale (as of 2026-04-19, from README):** 17,888 pages · 4,383 people · 723 companies · 21 cron jobs · built in 12 days.

**Architecture claim:** Contract-first — `src/core/operations.ts` defines ~41 shared operations. CLI and MCP server are both generated from this single source. Engine factory dynamically imports PGLite (embedded Postgres via WASM, zero-config default) or Postgres + pgvector (Supabase).

### The Resolver in the Wild — GBrain's `skills/RESOLVER.md`

```markdown
# GBrain Skill Resolver

This is the dispatcher. Skills are the implementation. **Read the skill file before acting.** If two skills could match, read both. They are designed to chain (e.g., ingest then enrich for each entity).

## Always-on (every message)

| Trigger | Skill |
|---------|-------|
| Every inbound message (spawn parallel, don't block) | `skills/signal-detector/SKILL.md` |
| Any brain read/write/lookup/citation | `skills/brain-ops/SKILL.md` |

## Brain operations

| Trigger | Skill |
|---------|-------|
| "What do we know about", "tell me about", "search for" | `skills/query/SKILL.md` |
| "Who knows who", "relationship between", "connections" | `skills/query/SKILL.md` (use graph-query) |
| Creating/enriching a person or company page | `skills/enrich/SKILL.md` |
| Where does a new file go? Filing rules | `skills/repo-architecture/SKILL.md` |
| Fix broken citations in brain pages | `skills/citation-fixer/SKILL.md` |
| "Research", "track", "extract from email", "investor updates" | `skills/data-research/SKILL.md` |

## Content & media ingestion

| Trigger | Skill |
|---------|-------|
| User shares a link, article, tweet, or idea | `skills/idea-ingest/SKILL.md` |
| Video, audio, PDF, book, YouTube, screenshot | `skills/media-ingest/SKILL.md` |
| Meeting transcript received | `skills/meeting-ingestion/SKILL.md` |
| Generic "ingest this" (auto-routes to above) | `skills/ingest/SKILL.md` |

## Thinking skills (from GStack)

| Trigger | Skill |
|---------|-------|
| "Brainstorm", "I have an idea", "office hours" | GStack: office-hours |
| "Review this plan", "CEO review", "poke holes" | GStack: ceo-review |
| "Debug", "fix", "broken", "investigate" | GStack: investigate |

## Disambiguation rules

When multiple skills could match:
1. Prefer the most specific skill (meeting-ingestion over ingest)
2. If the user mentions a URL, route by content type (link → idea-ingest, video → media-ingest)
3. If the user mentions a person/company, check if enrich or query fits better
4. Chaining is explicit in each skill's Phases section
5. When in doubt, ask the user

## Conventions (cross-cutting)

These apply to ALL brain-writing skills:
- `skills/conventions/quality.md` — citations, back-links, notability gate
- `skills/conventions/brain-first.md` — check brain before external APIs
- `skills/conventions/subagent-routing.md` — when to use Minions vs inline work
- `skills/_brain-filing-rules.md` — where files go
- `skills/_output-rules.md` — output quality standards
```

**Observations:**
- Pure markdown table of trigger → skill
- Disambiguation rules are human-readable, not code
- Cross-cutting conventions are referenced at the bottom (DRY)
- Cross-repo (GStack) skills are explicitly called out
- The fractal pattern is visible: top-level table routes to skills; each skill internally has its own Phases routing

### `skills/_brain-filing-rules.md` — The Manidis Fix, Codified

```markdown
# Brain Filing Rules — MANDATORY for all skills that write to the brain

## The Rule

The PRIMARY SUBJECT of the content determines where it goes. Not the format,
not the source, not the skill that's running.

## Decision Protocol

1. Identify the primary subject (a person? company? concept? policy issue?)
2. File in the directory that matches the subject
3. Cross-link from related directories
4. When in doubt: what would you search for to find this page again?

## Common Misfiling Patterns — DO NOT DO THESE

| Wrong | Right | Why |
|-------|-------|-----|
| Analysis of a topic → `sources/` | → appropriate subject directory | sources/ is for raw data only |
| Article about a person → `sources/` | → `people/` | Primary subject is a person |
| Meeting-derived company info → `meetings/` only | → ALSO update `companies/` | Entity propagation is mandatory |
| Research about a company → `sources/` | → `companies/` | Primary subject is a company |
| Reusable framework/thesis → `sources/` | → `concepts/` | It's a mental model |
| Tweet thread about policy → `media/` | → `civic/` or `concepts/` | media/ is for content ops |

## What `sources/` Is Actually For

`sources/` is ONLY for:
- Bulk data imports (API dumps, CSV exports, snapshots)
- Raw data that feeds multiple brain pages
- Periodic captures (quarterly snapshots, sync exports)

## Notability Gate
[people/companies/concepts gate logic]

## Iron Law: Back-Linking (MANDATORY)
Every mention of a person/company with a brain page MUST create a back-link
FROM that entity's page TO the page mentioning them. Bidirectional.

## Citation Requirements (MANDATORY)
Every fact written to a brain page must carry an inline `[Source: ...]` citation.

## Raw Source Preservation
< 100 MB → git-tracked `.raw/` sidecar; ≥ 100 MB or media → cloud storage with `.redirect.yaml` pointer.
```

### `src/core/check-resolvable.ts` — The Meta-Skill as Real Code

From the `CLAUDE.md` description:
> **Resolver validation: reachability, MECE overlap, DRY checks, structured fix objects.** v0.14.1: `CROSS_CUTTING_PATTERNS.conventions` is an array (notability gate accepts both `conventions/quality.md` and `_brain-filing-rules.md`). New `extractDelegationTargets()` parses `> **Convention:**`, `> **Filing rule:**`, and inline backtick references. DRY suppression is proximity-based via `DRY_PROXIMITY_LINES = 40`.

### `src/core/dry-fix.ts` — DRY Auto-Fix Engine

> `gbrain doctor --fix` engine. `autoFixDryViolations(fixes, {dryRun})` rewrites inlined rules to `> **Convention:** see [path](path).` callouts via three shape-aware expanders (bullet / blockquote / paragraph). Five guards: working-tree-dirty, no-git-backup, inside-code-fence, already-delegated (40-line proximity), ambiguous-multi-match, block-is-callout. `execFileSync` array args (no shell — no injection surface). EOF newline preserved.

### `gbrain doctor` — The Health Dashboard

> v0.12.3 adds two reliability detection checks: `jsonb_integrity` and `markdown_body_completeness`. v0.14.1: `--fix` delegates inlined cross-cutting rules to callouts.

### `skills/testing/SKILL.md` — The Skill Validation Framework

```markdown
---
name: testing
version: 1.0.0
description: |
  Skill validation framework. Validates every skill has SKILL.md with frontmatter,
  every reference exists, every env var is declared.
triggers:
  - "validate skills"
  - "test skills"
  - "skill health check"
  - "run conformance tests"
mutating: false
---

## Contract

This skill guarantees:
- Every skill directory has a SKILL.md file
- Every SKILL.md has valid YAML frontmatter (name, description)
- Every SKILL.md has required sections (Contract, Anti-Patterns, Output Format)
- manifest.json lists every skill directory
- RESOLVER.md references every skill in the manifest
- No MECE violations (duplicate triggers across skills)

## Phases
1. Walk skills directory. List all subdirectories containing SKILL.md.
2. Validate frontmatter. Parse YAML, check required fields.
3. Validate sections. Check for Contract, Anti-Patterns, Output Format.
4. Check manifest. Every skill directory must be listed in manifest.json.
5. Check resolver. Every manifest skill must have a RESOLVER.md entry.
6. Report results.

Automated: `bun test test/skills-conformance.test.ts test/resolver.test.ts`
```

**Key contract: "Every manifest skill must have a RESOLVER.md entry." — MECE: no duplicate triggers across skills.**

### `skills/manifest.json` — Machine-Readable Skill Registry

Every skill gets an entry: `{name, path, description}`. This is the middle layer between `RESOLVER.md` (human-readable trigger table) and individual `SKILL.md` files.

### GBrain SKILL.md Frontmatter Convention

```yaml
---
name: ingest
version: 1.0.0
description: |
  Route content to specialized ingestion skills. Detects input type and delegates.
triggers:
  - "ingest this"
  - "save this to brain"
  - "process this meeting"
tools:
  - search
  - get_page
  - put_page
  - add_link
mutating: true
---
```

**Note:** GBrain uses `triggers:` as an explicit array (vs. Anthropic's single `description` + `when_to_use`). The contract also includes a required `Contract / Phases / Output Format / Anti-Patterns` section structure per skill.

### Every brain-writing skill's top-line mandate (example from ingest)

> **Filing rule:** Read `skills/_brain-filing-rules.md` before creating any new page.

This is the two-line header Garry's article described — enforced across every skill.

### BrainBench v1 benchmark (from README)

> **Recall@5 jumps from 83% to 95%, Precision@5 from 39% to 45%, +30 more correct answers in the agent's top-5 reads** on a 240-page Opus-generated rich-prose corpus. Graph-only F1: **86.6% vs grep's 57.8%** (+28.8 pts).

### Minions — Postgres-native job queue

> A durable, Postgres-native job queue built into the brain. Every long-running agent task is now a job that survives gateway restarts, streams progress, gets paused/resumed/steered mid-flight.

Production comparison (pulling social posts):
- Minions: 753ms wall, $0.00 tokens, 100% success, ~2MB memory
- `sessions_spawn` (sub-agents): >10,000ms (gateway timeout), ~$0.03, 0% success

**The routing rule:**
> - **Deterministic** (same input → same steps → same output) → **Minions**
> - **Judgment** (requires assessment or decision) → **Sub-agents**

*(This is Garry's "latent vs deterministic" distinction at the runtime layer.)*

---

## GStack

**Tagline:** "I've been building products for twenty years, and right now I'm shipping more products than I ever have. gstack is how I do it."

**Traction:** 78,692 GitHub stars (Garry's article said 72K; now ~79K).

**Claim from README:** "2026 run rate is **~810× my 2013 pace** (11,417 vs 14 logical lines/day). Year-to-date (through April 18), 2026 has already produced **240× the entire 2013 year**. Measured across 40 public + private `garrytan/*` repos."

**Karpathy quote in README:** "I don't think I've typed like a line of code probably since December" (No Priors podcast, March 2026).

### GStack's Skill Resolver (`AGENTS.md`)

Unlike GBrain, GStack doesn't have a single RESOLVER.md. Each skill is self-contained with YAML frontmatter; Claude Code's built-in skill discovery is the resolver. AGENTS.md lists available skills as a flat table.

### GStack's 20+ Skills (the virtual engineering team)

| Skill | Role |
|-------|------|
| `/office-hours` | YC Office Hours — 6 forcing questions |
| `/plan-ceo-review` | CEO / Founder — rethink the problem |
| `/plan-eng-review` | Eng Manager — lock architecture, data flow |
| `/plan-design-review` | Senior Designer — rate 0-10 with AI-slop detection |
| `/plan-devex-review` | DX Lead — TTHW benchmarking |
| `/design-consultation` | Design Partner — full design system |
| `/review` | Staff Engineer — bug hunt |
| `/investigate` | Debugger — root cause, no-fix-without-investigation |
| `/design-review` | Designer who codes — audit + fix |
| `/devex-review` | DX Tester — live onboarding test |
| `/design-shotgun` | 4-6 AI mockup variants |
| `/design-html` | Production HTML from mockup |
| `/qa` | QA Lead — real browser + regression tests |
| `/pair-agent` | Multi-agent browser sharing |
| `/cso` | Chief Security Officer — OWASP + STRIDE |
| `/ship` | Release Engineer — tests + PR |
| `/land-and-deploy` | Merge → CI → deploy → verify |
| `/canary` | SRE — post-deploy monitoring |
| `/benchmark` | Performance engineer |
| `/autoplan` | CEO → design → eng pipeline |
| `/retro` | Weekly engineering retrospective |
| `/careful` / `/freeze` / `/guard` / `/unfreeze` | Safety skills |

### GStack's Host System (the cross-runtime insight)

**SKILL.md files are GENERATED from `.tmpl` templates.** `bun run gen:skill-docs --host codex` regenerates Codex-specific output. Supported hosts:

| Agent | Flag | Install dir |
|-------|------|-------------|
| Claude Code | (default) | `~/.claude/skills/gstack-*/` |
| OpenAI Codex CLI | `--host codex` | `~/.codex/skills/gstack-*/` |
| Cursor | `--host cursor` | `~/.cursor/skills/gstack-*/` |
| Factory Droid | `--host factory` | `~/.factory/skills/gstack-*/` |
| OpenCode | `--host opencode` | `~/.config/opencode/skills/gstack-*/` |
| Slate | `--host slate` | `~/.slate/skills/gstack-*/` |
| Kiro | `--host kiro` | `~/.kiro/skills/gstack-*/` |
| Hermes | `--host hermes` | `~/.hermes/skills/gstack-*/` |
| GBrain | `--host gbrain` | `~/.gbrain/skills/gstack-*/` |
| OpenClaw | (via ACP) | ClawHub install |

**Implication:** GStack treats the agentic runtime as a pluggable target. Same skill source → 10 hosts. This is the "open Agent Skills standard" made real.

### GStack Team Mode — Version Governance

> `./setup --team` + `gstack-team-init required` → teammates get gstack automatically on first Claude Code session. Fast auto-update check, throttled to once/hour, network-failure-safe. **No vendored files, no version drift.**

### GStack Test Tiers

- Gate (CI default): safety + deterministic functional, free, <5s
- Periodic (weekly cron): quality benchmarks, Opus tests, Codex-E2E (~$4/run)
- Diff-based test selection via `test/helpers/touchfiles.ts` — only runs tests impacted by the diff

### Installation Flow (via Claude Code)

Paste one-liner to Claude:
> Install gstack: run `git clone --single-branch --depth 1 https://github.com/garrytan/gstack.git ~/.claude/skills/gstack && cd ~/.claude/skills/gstack && ./setup` then add a "gstack" section to CLAUDE.md that says to use the /browse skill from gstack for all web browsing, never use mcp__claude-in-chrome__* tools, and lists the available skills: [long list].

*(Claude does the rest — this itself is a skill-as-method-call pattern.)*

---

## Cross-cutting Observations

1. **Two implementations of the Agent Skills standard:**
   - **Anthropic Claude Code**: `description` (+ `when_to_use`) as free-text, model matches user intent to string. 1,536-char cap.
   - **GBrain**: `triggers: []` as explicit array of canonical phrases. Plus a top-level `RESOLVER.md` trigger table. Plus a `manifest.json` registry.
   - GBrain layers explicit routing ON TOP of the implicit description-matching resolver.

2. **The three tools that defend against [[context-rot]] are real:**
   - `skills/testing/SKILL.md` = [[trigger-evals]] + [[check-resolvable]] conformance checks (manifest ↔ resolver ↔ SKILL.md three-way integrity)
   - `src/core/check-resolvable.ts` = MECE overlap + DRY detection engine
   - `gbrain doctor --fix` = auto-remediation (inlined rules → callouts)

3. **DRY is enforced mechanically:**
   - Proximity-based suppression (40-line window)
   - Auto-rewrite to `> **Convention:** see [path](path).` callouts
   - Five guards prevent destructive edits
   - Working-tree-dirty check

4. **Skills are a three-layer artifact:**
   - Top: `RESOLVER.md` (trigger table, human-readable)
   - Middle: `manifest.json` (machine-readable registry)
   - Leaf: `SKILL.md` (the actual procedure, with `Contract / Phases / Output Format / Anti-Patterns`)

5. **Latent-vs-deterministic split is enforced at runtime:**
   - Minions = deterministic work (cheap, durable, fast)
   - Sub-agents = judgment work
   - `minion_mode: pain_triggered` auto-routes based on task shape

6. **Karpathy scale:** GStack's "810× productivity" claim is measured in logical lines (diff-based, AI-inflation-corrected), not raw LOC. Methodology in `docs/ON_THE_LOC_CONTROVERSY.md`.
