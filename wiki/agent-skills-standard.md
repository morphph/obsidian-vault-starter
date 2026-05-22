---
type: concept
created: 2026-04-21
last-updated: 2026-05-22
sources:
  - raw/2026-04-21-anthropic-agent-skills-docs.md
  - raw/2026-04-21-gbrain-gstack-github-deep-scan.md
  - raw/2026-05-14-anthropic-claude-code-skills-refresh.md
  - raw/2026-05-22-repo-anthropics-skills.md
  - raw/2026-05-22-anthropic-equipping-agents-skills-blog.md
tags: [wiki, standard, agentic, architecture, skills]
---

> **Update 2026-05-16:** [[tw93|Tw93]]'s "你不知道的 Agent" piece (2026-03-19) added two production-grade design rules for the `description` field:
>
> 1. **Treat the description as a routing condition, not a feature ad.** "When should I be used?" matters more than "What can I do?". Best format: explicit **Use when / Don't use when** clauses + anti-examples.
> 2. **Anti-examples are not optional.** Hard data from Tw93's measurements: baseline 73% routing accuracy → drops to **53%** without anti-examples → climbs to **85%** when added back (response time also dropped 18.1%). The "Don't use when" half of the description is doing more work than the "Use when" half.
>
> Three Skills anti-patterns Tw93 surfaces:
> - Hundreds of lines of operating manual stuffed in SKILL.md body (should be supporting files)
> - One Skill trying to cover review + deploy + debug + incident
> - Side-effecting Skills without explicit "when not to call me" guards
>
> See [[source-tw93-agent-architecture-engineering]].


# Agent Skills Standard

## Summary
Open standard at **agentskills.io** defining the file format for portable agent skills: a directory containing `SKILL.md` with YAML frontmatter (`name`, `description`, trigger metadata) + markdown body. Anthropic's Claude Code is the reference implementation; [[garry-tan|Garry Tan]]'s [[gbrain]] and [[gstack]] implement it with an extra explicit layer (`RESOLVER.md` + `manifest.json`). The standard **crystallizes the [[resolvers|resolver]] pattern** — `description` is the resolver entry; progressive disclosure keeps full bodies out of context until invoked.

## Origin (2025-10-16)

The foundational framing — and the term "Agent Skills" itself — comes from Anthropic's engineering blog post **"Equipping Agents for the Real World with Agent Skills"** (Barry Zhang + Keith Lazuka + Mahesh Murag, 2025-10-16). See [[source-anthropic-equipping-agents-skills-blog]].

**The official analogy that drives the entire design:**

> "[Skills are] like putting together an onboarding guide for a new hire... enabling organizations to capture and share their procedural knowledge through reusable skill bundles."

Not a prompt (job description). Not tool docs (API reference). An **onboarding guide** — values + process + tools + culture.

**The philosophical claim that justifies the architecture:**

> "The amount of context that can be bundled into a skill is **effectively unbounded**."

Because progressive disclosure means only the relevant parts load at runtime, you can keep growing a skill's bundled files without ever paying the context cost upfront.

**The PDF skill as canonical example** (the only specific example in the announcement):
- `pdf/SKILL.md` — core workflow
- `pdf/reference.md` — referenced when needed
- `pdf/forms.md` — referenced only for form-filling subtasks
- Python script bundled — runs without loading the script or PDF into context

This worked example shows progressive disclosure not as a doc-organization choice but as **architecture**.

## Details

### The standard in one line
> **Write procedural knowledge in `SKILL.md` files. Claude loads the description into context; loads the body only when invoked.**

### YAML frontmatter reference (Claude Code's implementation, 2026-05-14 refresh)

```yaml
---
name: my-skill                       # slash-command + display name (max 64, kebab-case)
description: What it does + triggers  # Claude matches user intent against this string
when_to_use: Additional triggers      # Appended to description in the listing (shares 1,536-char cap)
disable-model-invocation: false       # true = user-only (for /commit, /deploy); ALSO blocks subagent preloading
user-invocable: true                  # false = Claude-only (for background knowledge)
allowed-tools: Read Grep              # Pre-approved without permission prompts (does NOT restrict)
argument-hint: [issue-number]         # Autocomplete hint
arguments: [issue, branch]            # Named positional args → $issue, $branch substitution
model: claude-opus-4-7                # Override session model (rest of current turn only)
effort: high                          # low | medium | high | xhigh | max
context: fork                         # fork = run in subagent
agent: Explore                        # Which subagent type for fork (built-in or custom)
hooks: { ... }                        # Lifecycle hooks scoped to this skill (PreToolUse / PostToolUse / Stop)
paths: ["wiki/**"]                    # Glob: only auto-load for matching files
shell: bash                           # bash | powershell for !`cmd` blocks
---
```

Only `description` is recommended. All others are optional. See [[source-claude-code-skills-docs-2026-05]] for canonical reference (refresh of original 2026-04-21 docs).

### Substitution variables (refresh)

- `$ARGUMENTS` — all arguments
- `$ARGUMENTS[N]` / `$N` — argument by 0-based index
- `$name` — named argument from `arguments` frontmatter list
- `${CLAUDE_SESSION_ID}` — current session ID
- `${CLAUDE_EFFORT}` — current effort level
- `${CLAUDE_SKILL_DIR}` — directory containing SKILL.md (for plugin skills: the skill subdirectory, NOT plugin root)

### `skillOverrides` setting (2026-05-14 refresh)

Control skill visibility from `settings.json` WITHOUT editing SKILL.md — useful for shared-repo skills you don't want to edit:

```json
{
  "skillOverrides": {
    "legacy-context": "name-only",   // name visible, description hidden
    "deploy": "off"                    // hidden entirely
  }
}
```

Values: `"on"` / `"name-only"` / `"user-invocable-only"` / `"off"`. Plugin skills NOT affected — manage via `/plugin`.

### Bundled skills (added 2026-05-14)

`/simplify`, `/batch`, `/debug`, `/loop`, `/claude-api` are now official **bundled skills** — prompt-based, not fixed logic. Same invocation as any other skill.

### The critical constraint: **1,536-char cap per entry**
> Description auto-truncation: **combined `description` + `when_to_use` is capped at 1,536 characters** in the skill listing. Budget scales dynamically at **1% of context window, fallback 8,000 chars** total. Raise with `SLASH_COMMAND_TOOL_CHAR_BUDGET`.

This is the **mechanical reason** [[context-rot]] degrades routing: if you have too many skills or verbose descriptions, Claude literally can't see the trigger keywords. **Front-load the key use case.**

### Two Dialects of the Same Standard

| Dimension | Anthropic Claude Code | GBrain (Garry Tan) |
|-----------|----------------------|---------------------|
| Trigger field | `description` + `when_to_use` (free-text) | `triggers: [...]` (array of canonical phrases) |
| Routing engine | LLM matches intent → string | LLM matches → string OR RESOLVER.md table has exact phrase |
| Registry | Filesystem scan of `~/.claude/skills/**/SKILL.md` | Explicit `manifest.json` + `RESOLVER.md` |
| Skill body structure | Free markdown | Mandatory: Contract · Phases · Output Format · Anti-Patterns |
| Reachability check | None built in | `src/core/check-resolvable.ts` + `skills/testing/SKILL.md` |
| DRY enforcement | None | `gbrain doctor --fix` rewrites inlined rules to callouts |

**GBrain layers explicit routing ON TOP of the implicit description-matching.** The belt-and-suspenders approach: strings for LLM matching + tables for deterministic audit.

### Progressive Disclosure — The Context-Management Primitive

> **In a regular session, skill descriptions are loaded into context so Claude knows what's available, but full skill content only loads when invoked.**

This is the implementation of [[resolvers|Garry's "200 lines vs 20,000 lines"]]:
- Skill description (1 line to ~1.5 KB): always in context
- Skill body (can be 500+ lines): loaded on invocation
- Body stays for the rest of the session (single message, not re-read)
- Auto-compaction carries invoked skills forward with token budget (25K shared, 5K per skill)

### Three-tier budgets (from [[anthropic-skill-creator|skill-creator]] official guidance, 2026-05-22)

| Level | When loaded | Size |
|---|---|---|
| **Metadata** (name + description) | Always in context | **~100 words** |
| **SKILL.md body** | When skill triggers | **<500 lines ideal** |
| **Bundled resources** | As needed (scripts can execute without loading) | **Unlimited** |

> "These word counts are approximate and you can feel free to go longer if needed... if you're approaching this limit, add an additional layer of hierarchy along with clear pointers about where the model using the skill should go next to follow up."

### Anatomy of a skill folder (official, from [[anthropics-skills-repo]])

```
skill-name/
├── SKILL.md (required)
└── (optional)
    ├── scripts/    - Executable code for deterministic/repetitive tasks
    ├── references/ - Docs loaded into context as needed
    └── assets/     - Files used in output (templates, icons, fonts)
```

**Domain organization pattern**: when a skill supports multiple variants (AWS/GCP/Azure, English/Chinese, web/mobile), put each variant in `references/` so Claude reads only the relevant file at runtime. SKILL.md handles the selection logic.

### ⭐ "Pushy descriptions" — the official counter-intuitive rule (2026-05-22)

[[anthropic-skill-creator]] reveals a finding the docs don't state outright:

> "Currently Claude has a tendency to **'undertrigger'** skills — to not use them when they'd be useful. To combat this, please make the skill descriptions a little bit **'pushy'**."

**Example:** "How to build a dashboard..." → "...**Make sure to use this skill whenever the user mentions dashboards, data visualization, internal metrics, or wants to display any kind of company data, even if they don't explicitly ask for a 'dashboard.'**"

**Combine with Tw93's "Don't use when..." finding for the complete pattern:**
- Pushy positives ("use this whenever X, Y, Z, even if user doesn't explicitly ask")
- Explicit negatives ("Don't use when [near-miss case]")

### Subagent Skills (Preloaded vs On-Demand)

| Approach | When body loads |
|----------|-----------------|
| Regular session | On invocation |
| Skill with `context: fork` | Subagent runs this skill as its prompt |
| Subagent with `skills:` field | **Full body injected at subagent startup** |

Preloaded skills trade startup context for invocation latency — useful for specialized subagents like Explore or Plan.

### Storage Locations (priority order)

| Level | Path | Scope |
|-------|------|-------|
| Enterprise | Managed settings | All users in org |
| Personal | `~/.claude/skills/<name>/SKILL.md` | All projects |
| Project | `.claude/skills/<name>/SKILL.md` | This project |
| Plugin | `<plugin>/skills/<name>/SKILL.md` | Where plugin enabled (namespaced `plugin:skill`) |

**Conflicts:** higher level wins. Skills take precedence over identically-named `.claude/commands/`.

### Nested Discovery (monorepo-aware)
When editing a file in `packages/frontend/`, Claude Code also loads skills from `packages/frontend/.claude/skills/`. This is the context-resolver pattern at the filesystem level: the path you're editing *is* the routing signal.

### Connection to our vault's current pattern

This vault already uses the Agent Skills pattern in two places:
1. **`.claude/commands/*.md`** → these are effectively skills (the Claude Code docs explicitly say commands + skills are now one thing)
2. **`.claude/rules/*.md` with `paths:` glob** → auto-load-by-path is the standard's context-resolver mechanism

What we don't yet have:
- Explicit registry (no `manifest.json` equivalent)
- Trigger canonicalization (no `triggers: [...]` array — only free-text descriptions)
- Reachability check (nothing catches a `.claude/commands/` file that isn't mentioned in CLAUDE.md's Commands table)

## Connections
- Related: [[resolvers]], [[check-resolvable]], [[trigger-evals]], [[context-rot]], [[gbrain]], [[gstack]], [[claude-code]], [[thin-harness-fat-skills]], [[skill-as-method-call]], [[context-noise-governance]], [[documentation-layers]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-21 | raw/2026-04-21-anthropic-agent-skills-docs.md | Initial creation from Claude Code Skills official docs |
| 2026-04-21 | raw/2026-04-21-gbrain-gstack-github-deep-scan.md | Added GBrain's explicit-routing dialect as contrast to Anthropic's description-matching |
| 2026-05-14 | raw/2026-05-14-anthropic-claude-code-skills-refresh.md | Added new fields (paths, hooks, shell, arguments, when_to_use), substitution variables ($ARGUMENTS[N], $N, $name, ${CLAUDE_SESSION_ID}, ${CLAUDE_EFFORT}, ${CLAUDE_SKILL_DIR}), `skillOverrides` setting, bundled skills (/simplify, /batch, /debug, /loop, /claude-api), monorepo nested discovery, live change detection |
| 2026-05-16 | raw/2026-05-11-khairallah-how-to-use-claude-skills.md | Added Khairallah's mass-audience 4-phase Skill build playbook: (Phase 1) install from anthropic/skills GitHub; (Phase 2) Three-Question Test (what + when + perfect-output-example); (Phase 3) Three-Scenario Test (happy path / edge case / stress test) + weekly refinement; (Phase 4) library compounding math (10 skills × 30 min/wk = 260 hours/yr). Hard rules: under 500 lines, no vague language, every instruction testable. Plus industry-specific Skill templates. |
| 2026-05-22 | raw/2026-05-22-repo-anthropics-skills.md | Added Anthropic-official **three-tier word budgets** (~100 words metadata / <500 lines body / unlimited resources), **official folder anatomy** (scripts/ + references/ + assets/), **domain organization pattern** (variants in references/), and the **"pushy descriptions" counter-intuitive rule** (combat Claude's undertriggering bias by writing descriptions aggressively) — combine with Tw93's "Don't use when..." for the complete pattern |
| 2026-05-22 | raw/2026-05-22-anthropic-equipping-agents-skills-blog.md | Added **Origin section** — the foundational 2025-10-16 announcement by Barry Zhang + Keith Lazuka + Mahesh Murag that introduced the term "Agent Skills." Covers: **"onboarding guide for a new hire" analogy** (the core framing), **"effectively unbounded" context philosophy** (justifies architecture), **PDF skill as canonical example** (the only specific example in the announcement). This is the source the docs/repo/Garry/Matt/Khairallah all stand on |
