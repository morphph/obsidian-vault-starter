---
type: entity
created: 2026-05-22
last-updated: 2026-05-22
sources:
  - raw/2026-05-22-repo-anthropics-skills.md
tags: [wiki, entity, anthropic, claude-code, skills, repo]
---

# anthropics/skills (Repo)

## Summary
The **official Anthropic Skills repository** — 138.9K stars / 16.4K forks / actively maintained (last commit 2026-05-22). 17 example SKILL.md files + the [[anthropic-skill-creator]] meta-skill + a (minimal) template + a (one-line) spec pointing at agentskills.io. Distributed as Claude Code plugin marketplace: `/plugin marketplace add anthropics/skills`. Three plugin bundles: `document-skills` (docx/pdf/pptx/xlsx, source-available, power Claude's native document capabilities) + `example-skills` (12 Apache-2.0 example skills) + `claude-api` (Claude API + Managed Agents reference). **The canonical implementation of [[agent-skills-standard]].**

## Details

### The 17 example skills (full inventory)
| Category | Skills |
|---|---|
| **Creative & design** | algorithmic-art, brand-guidelines, canvas-design, theme-factory, slack-gif-creator |
| **Development & technical** | frontend-design, mcp-builder, web-artifacts-builder, webapp-testing |
| **Enterprise & communication** | internal-comms, doc-coauthoring |
| **Document skills** (source-available) | docx, pdf, pptx, xlsx |
| **Meta** | ⭐ skill-creator, claude-api |

### The template (the entire file)
```markdown
---
name: template-skill
description: Replace with description of the skill and when Claude should use it.
---

# Insert instructions below
```

Only `name` + `description` required. Everything else freeform.

### The spec
`spec/agent-skills-spec.md` contains exactly one line pointing to https://agentskills.io/specification. The actual spec lives off-repo.

### Plugin marketplace pattern
`.claude-plugin/marketplace.json` defines 3 plugins, each pointing to subsets of `skills/`. **Canonical way to ship a skill library** — a single repo can bundle multiple plugins with shared infrastructure.

### Three-tier progressive disclosure (concrete budgets from skill-creator)
| Level | When loaded | Size |
|---|---|---|
| Metadata (name + description) | Always in context | ~100 words |
| SKILL.md body | When skill triggers | <500 lines ideal |
| Bundled resources | As needed | Unlimited |

### Anatomy of a skill folder
```
skill-name/
├── SKILL.md (required)
└── (optional)
    ├── scripts/    - Executable code for deterministic tasks
    ├── references/ - Docs loaded into context as needed
    └── assets/     - Templates, icons, fonts used in output
```

**Domain organization pattern**: when supporting multiple variants (e.g., AWS/GCP/Azure), put each variant in `references/` so Claude loads only the relevant file.

### Partner skills
README highlights Notion as the first partner skill provider — first-party precedent for third-party SaaS shipping skills for their own products.

### Recent activity (last 10 commits, all in 2026-05)
Heavy focus on `claude-api` skill — Managed Agents self-hosted sandboxes, mid-session agent updates, MCP tool-output offload (>100K tokens auto-offload to file), Files API cleanup. Example skills are stable. **Maintainer: Keith Lazuka (klazuka@anthropic.com).**

### Why this repo matters more than the docs
The official [[agent-skills-standard|Claude Code Skills docs]] tell you the **syntax** (frontmatter fields, storage priority, char caps). This repo shows you the **writing** — 17 real SKILL.md examples + the [[anthropic-skill-creator]] meta-skill that operationalizes "how to actually iterate." Read docs for the spec, read this repo for the practice.

## Connections
- Related: [[anthropic]], [[anthropic-skill-creator]], [[claude-code]], [[agent-skills-standard]], [[skillify-meta-skill]], [[trigger-evals]], [[source-anthropics-skills-repo]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-05-22 | raw/2026-05-22-repo-anthropics-skills.md | Initial creation from GitHub Deep Scan |
