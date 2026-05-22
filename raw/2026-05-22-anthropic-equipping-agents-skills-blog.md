# Equipping Agents for the Real World with Agent Skills

**Source URL:** https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills
**Published:** October 16, 2025 (note: predates all other Skills content in our wiki by ~5 months)
**Authors:** Barry Zhang, Keith Lazuka, and Mahesh Murag
**Fetched:** 2026-05-22 via WebFetch
**Context:** The **original Anthropic Engineering announcement** for Agent Skills — the piece that introduced the SKILL.md concept publicly, before the official docs or [[anthropics-skills-repo|github.com/anthropics/skills]] became canonical references.

---

## Overview

Agent Skills represent a new approach for building specialized agents by packaging procedural knowledge into organized, composable resources. Rather than creating custom agents for each use case, teams can now extend Claude's capabilities dynamically using skills—directories containing instructions, scripts, and resources that agents discover and load as needed.

The concept mirrors **"putting together an onboarding guide for a new hire,"** enabling organizations to "capture and share their procedural knowledge" through reusable skill bundles.

## Anatomy of a Skill

A skill is fundamentally a directory containing a `SKILL.md` file. This file must begin with YAML frontmatter specifying required metadata:

- `name`: The skill's identifier
- `description`: What the skill enables

At startup, Claude pre-loads the name and description of installed skills into its system prompt. This represents the **first level of progressive disclosure**, providing just enough information for the model to determine when a skill is relevant without loading its complete contents into context.

### The SKILL.md File Structure

The body of `SKILL.md` constitutes the **second level of detail**. If Claude determines the skill addresses the current task, it reads the full `SKILL.md` into context.

For complex skills, a **third level and beyond** involves bundling additional files within the skill directory. These supplementary files—referenced by name from `SKILL.md`—remain outside the context window until Claude selectively navigates to them as needed.

The PDF skill example demonstrates this approach: the core `SKILL.md` references two additional files (`reference.md` and `forms.md`). By separating form-filling instructions into a dedicated file, the skill author keeps the primary documentation lean, trusting Claude will access `forms.md` only during form-related tasks.

## Progressive Disclosure Design Principle

Progressive disclosure is described as **"the core design principle that makes Agent Skills flexible and scalable."** The comparison offered is instructive:

> "Like a well-organized manual that starts with a table of contents, then specific chapters, and finally a detailed appendix, skills let Claude load information only as needed."

This architecture allows agents with filesystem and code execution tools to avoid reading entire skills into their context window for particular tasks, making **"the amount of context that can be bundled into a skill...effectively unbounded."**

### Context Window Mechanics (concrete walkthrough)

The context window evolves through these stages:

1. Initially contains the core system prompt, metadata for installed skills, and the user's message
2. Claude invokes a Bash tool to read `pdf/SKILL.md` when triggering the PDF skill
3. Claude selectively reads the `forms.md` file bundled with the skill
4. Claude proceeds with the user's task using the loaded skill instructions

## Skills and Code Execution

Skills can bundle pre-written code for Claude to execute as tools at its discretion. The rationale emphasizes practical efficiency:

> "Sorting a list via token generation is far more expensive than simply running a sorting algorithm."

The PDF skill exemplifies this pattern with a Python script that reads PDFs and extracts form fields. Claude runs this script without loading either the script or PDF file into context, leveraging **"the deterministic reliability that only code can provide"** for consistency and repeatability.

This is the official Anthropic statement of the same principle Garry Tan calls [[latent-vs-deterministic]] and Ryan Sarver calls [[llm-judgment-vs-scripts]].

## Development and Evaluation Guidelines

The documentation offers several best practices:

### Start with evaluation
Identify capability gaps by running agents on representative tasks, observing where they struggle or need additional context, then build skills incrementally to address shortcomings.

### Structure for scale
- When `SKILL.md` becomes unwieldy, split content into separate files and reference them
- For mutually exclusive or rarely-used-together contexts, keeping paths separate reduces token usage
- Code serves dual purposes: executable tools and documentation, with clarity about whether Claude should run scripts directly or read them as reference

### Think from Claude's perspective
- Monitor real-world skill usage and iterate based on observations
- Watch for unexpected trajectories or overreliance on specific contexts
- **Pay particular attention to the skill's `name` and `description`**—Claude uses these to decide whether triggering the skill suits the current task

### Iterate with Claude
During task work, request that Claude capture successful approaches and common mistakes into reusable context and code within a skill. If using a skill leads to errors, ask Claude to self-reflect on what went wrong. This approach:

> "Will help you discover what context Claude actually needs, instead of trying to anticipate it upfront."

This is the **official Anthropic version of "post-execution skillification"** — the same pattern Garry Tan packages as `/skillify`.

## Security Considerations

Skills grant Claude new capabilities through instructions and code, introducing potential vulnerabilities. The guidance is explicit:

> "**Install skills only from trusted sources.**"

When installing from less-trusted sources, thoroughly audit before use:
- Read bundled file contents to understand functionality
- Pay particular attention to code dependencies and bundled resources like images or scripts
- Monitor for instructions or code directing Claude to connect to potentially untrusted external network sources

## Current Support and Future Direction

Agent Skills are currently supported across Claude.ai, Claude Code, the Claude Agent SDK, and the Claude Developer Platform. Forthcoming features will support the full lifecycle of creating, editing, discovering, sharing, and using skills.

The article expresses particular enthusiasm about organizations and individuals sharing "their context and workflows with Claude." Future exploration includes complementing Model Context Protocol (MCP) servers by teaching agents "complex workflows that involve external tools and software."

Looking further ahead, the vision encompasses enabling:

> "Agents to create, edit, and evaluate Skills on their own, letting them codify their own patterns of behavior into reusable capabilities."

This is the **recursive meta-skill vision** that [[skillify-meta-skill|Garry Tan]] and the [[anthropic-skill-creator|skill-creator]] meta-skill subsequently implemented.

## Design Philosophy

The overarching principle emphasizes simplicity:

> "Skills are a simple concept with a correspondingly simple format. This simplicity makes it easier for organizations, developers, and end users to build customized agents and give them new capabilities."

---

**Author note:** Barry Zhang (PM, Claude API), Keith Lazuka (engineer, also maintainer of [[anthropics-skills-repo]] per marketplace.json), Mahesh Murag (researcher).
