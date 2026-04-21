# Anthropic: Extend Claude with Skills — Official Docs

**Source URL:** https://docs.claude.com/en/docs/claude-code/skills (redirects to https://code.claude.com/docs/en/skills)
**Alt:** https://agentskills.io (open standard)
**Fetched:** 2026-04-21 via WebFetch
**Fetch method:** WebFetch after two redirects (docs.anthropic.com → docs.claude.com → code.claude.com)
**Context:** Claude Code's canonical implementation of [[resolvers|resolvers]] — the `description` field on a skill is the official, production "when X appears, load Y" routing entry. Cross-reference: Garry Tan's article calls this out by name as "the canonical resolver."

---

## What a Skill Is

> Skills extend what Claude can do. Create a `SKILL.md` file with instructions, and Claude adds it to its toolkit. Claude uses skills when relevant, or you can invoke one directly with `/skill-name`.

> Create a skill when you keep pasting the same playbook, checklist, or multi-step procedure into chat, or **when a section of CLAUDE.md has grown into a procedure rather than a fact. Unlike CLAUDE.md content, a skill's body loads only when it's used, so long reference material costs almost nothing until you need it.**

*(This is exactly Garry Tan's "20,000 → 200 lines" argument, but as official doc.)*

## Open Standard

> Claude Code skills follow the **Agent Skills open standard** (agentskills.io), which works across multiple AI tools. Claude Code extends the standard with additional features like invocation control, subagent execution, and dynamic context injection.

## Storage Locations (priority)

| Location   | Path                                                | Applies to                     |
| :--------- | :-------------------------------------------------- | :----------------------------- |
| Enterprise | managed settings                                    | All users in your organization |
| Personal   | `~/.claude/skills/<skill-name>/SKILL.md`            | All your projects              |
| Project    | `.claude/skills/<skill-name>/SKILL.md`              | This project only              |
| Plugin     | `<plugin>/skills/<skill-name>/SKILL.md`             | Where plugin is enabled        |

Priority: enterprise > personal > project. Plugin skills use `plugin-name:skill-name` namespace.

**Custom commands have been merged into skills.** `.claude/commands/deploy.md` and `.claude/skills/deploy/SKILL.md` both create `/deploy`. Commands files still work. Skills add: directory for supporting files, frontmatter for invocation control, auto-load when relevant.

## YAML Frontmatter Reference (the authoritative list)

```yaml
---
name: my-skill
description: What this skill does
when_to_use: Additional trigger context
disable-model-invocation: false
user-invocable: true
allowed-tools: Read Grep
argument-hint: [issue-number]
model: claude-opus-4-7
effort: high
context: fork
agent: Explore
paths: ["wiki/**"]
shell: bash
---
```

| Field | Required | Notes |
|-------|----------|-------|
| `name` | No | Display name (defaults to dir name). Lowercase/numbers/hyphens, max 64. |
| `description` | **Recommended** | **"Claude uses this to decide when to apply the skill."** If omitted, uses first paragraph. **Front-load the key use case: combined `description` + `when_to_use` is truncated at 1,536 characters** in the skill listing to reduce context usage. |
| `when_to_use` | No | Trigger phrases / example requests. Counts toward the 1,536-char cap. |
| `disable-model-invocation` | No | `true` = only user invokes (for `/commit`, `/deploy`). |
| `user-invocable` | No | `false` = only Claude invokes (for background knowledge). |
| `allowed-tools` | No | Pre-approved tools while skill is active. |
| `paths` | No | Glob patterns limit when skill auto-loads. *(Same format as path-specific CLAUDE.md rules.)* |
| `context: fork` | No | Run in forked subagent. |
| `agent` | No | Which subagent type (`Explore`, `Plan`, custom). |

## Progressive Disclosure (the resolver mechanism)

> In a regular session, **skill descriptions are loaded into context so Claude knows what's available, but full skill content only loads when invoked.** Subagents with preloaded skills work differently: the full skill content is injected at startup.

**Description budget:**
> All skill names are always included, but if you have many skills, descriptions are shortened to fit the character budget, which can strip the keywords Claude needs to match your request. The budget scales dynamically at **1% of the context window, with a fallback of 8,000 characters.**
>
> To raise the limit, set the `SLASH_COMMAND_TOOL_CHAR_BUDGET` environment variable. Or trim the `description` and `when_to_use` text at the source: **front-load the key use case, since each entry's combined text is capped at 1,536 characters regardless of budget.**

## Skill Content Lifecycle

> When you or Claude invoke a skill, the rendered `SKILL.md` content enters the conversation as a single message and stays there for the rest of the session. Claude Code does not re-read the skill file on later turns, so write guidance that should apply throughout a task as standing instructions rather than one-time steps.

> Auto-compaction carries invoked skills forward within a token budget. When the conversation is summarized to free context, Claude Code re-attaches the most recent invocation of each skill after the summary, keeping the first 5,000 tokens of each. Re-attached skills share a combined budget of 25,000 tokens.

## Two Types of Skill Content

**Reference content** — conventions, patterns, style guides. Runs inline so Claude can use it alongside conversation context.

**Task content** — step-by-step actions like deployments. Often invoked directly via `/skill-name` with `disable-model-invocation: true`.

## Troubleshooting — Skill Not Triggering

> 1. Check the description includes keywords users would naturally say
> 2. Verify the skill appears in `What skills are available?`
> 3. Try rephrasing your request to match the description more closely
> 4. Invoke it directly with `/skill-name`

## Troubleshooting — Skill Triggers Too Often

> 1. Make the description more specific
> 2. Add `disable-model-invocation: true` if you only want manual invocation

## Automatic Discovery from Nested Directories

> When you work with files in subdirectories, Claude Code automatically discovers skills from nested `.claude/skills/` directories. For example, if you're editing a file in `packages/frontend/`, Claude Code also looks for skills in `packages/frontend/.claude/skills/`. This supports monorepo setups where packages have their own skills.

## Key Official Primitives (cross-refs to wiki concepts)

- **`description` field** = canonical resolver entry (see [[resolvers]])
- **`paths:` glob** = filing/context resolver (see `.claude/rules/*.md` in this vault)
- **1,536-char cap per entry + 1% context budget** = the concrete constraint behind "front-load the key use case" (see [[context-noise-governance]])
- **Description auto-truncation** = the actual mechanism behind [[context-rot]] — if you have too many skills, Claude literally can't see their trigger keywords
- **`disable-model-invocation`** = the "user-only" trigger type (see [[trigger-evals]] false-positive defense)
- **Skill invocation = single message, stays forever** = why skills are "fat" (load once, use all session) and harnesses are "thin" (see [[thin-harness-fat-skills]])

## Related docs referenced

- `/en/sub-agents` — delegate tasks to specialized agents
- `/en/plugins` — package and distribute skills
- `/en/hooks` — automate workflows around tool events
- `/en/memory` — CLAUDE.md management
- `/en/commands` — built-in commands + bundled skills reference
- `/en/permissions` — control tool and skill access
