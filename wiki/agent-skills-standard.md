---
type: concept
created: 2026-04-21
last-updated: 2026-05-14
sources:
  - raw/2026-04-21-anthropic-agent-skills-docs.md
  - raw/2026-04-21-gbrain-gstack-github-deep-scan.md
  - raw/2026-05-14-anthropic-claude-code-skills-refresh.md
tags: [wiki, standard, agentic, architecture, skills]
---

# Agent Skills Standard

## Summary
Open standard at **agentskills.io** defining the file format for portable agent skills: a directory containing `SKILL.md` with YAML frontmatter (`name`, `description`, trigger metadata) + markdown body. Anthropic's Claude Code is the reference implementation; [[garry-tan|Garry Tan]]'s [[gbrain]] and [[gstack]] implement it with an extra explicit layer (`RESOLVER.md` + `manifest.json`). The standard **crystallizes the [[resolvers|resolver]] pattern** — `description` is the resolver entry; progressive disclosure keeps full bodies out of context until invoked.

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
