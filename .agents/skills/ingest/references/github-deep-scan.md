# GitHub Deep Scan — repo URL 的深扫流程

For GitHub repo URLs (e.g., `https://github.com/owner/repo`), run a deep architecture scan using `gh` CLI:

## Step 1 — Fetch repo data

```bash
# Metadata
gh repo view {owner}/{repo} --json name,description,stargazerCount,primaryLanguage,updatedAt

# File tree
gh api "repos/{owner}/{repo}/git/trees/main" --paginate --jq '.tree[] | select(.type=="blob") | .path'

# README
gh api repos/{owner}/{repo}/contents/README.md --jq '.content' | base64 -d

# Dependencies (try each, take what exists)
gh api repos/{owner}/{repo}/contents/package.json --jq '.content' | base64 -d
gh api repos/{owner}/{repo}/contents/pyproject.toml --jq '.content' | base64 -d

# Agentic config (if exists)
gh api repos/{owner}/{repo}/contents/CLAUDE.md --jq '.content' | base64 -d
gh api repos/{owner}/{repo}/contents/AGENTS.md --jq '.content' | base64 -d

# Recent activity
gh api "repos/{owner}/{repo}/commits?per_page=15" --jq '.[].commit.message'
```

## Step 2 — Read key source files

From the file tree, identify and fetch 2-3 key files:
- Entry point (e.g., `src/index.ts`, `main.py`, `scripts/` directory)
- Main config or schema file
- Any file that reveals the core architecture pattern

Use `gh api repos/{owner}/{repo}/contents/{path} --jq '.content' | base64 -d` to fetch each.

## Step 3 — Synthesize into structured source document

Save to `raw/{YYYY-MM-DD}-repo-{repo-name}.md` with this structure:

```markdown
# {Repo Name}

**Source:** {github URL}
**Author/Org:** {owner}
**Stars:** {count} | **Language:** {lang} | **Last updated:** {date}
**Fetch method:** GitHub Deep Scan (gh CLI)

## What It Does
[Problem it solves, who it's for, why it exists — from README]

## Architecture
[File structure analysis + key design decisions from reading source files]

## Tech Stack
[Language, dependencies, frameworks — from package.json/pyproject.toml]

## Key Patterns & Takeaways
[Reusable patterns, design decisions, best practices worth remembering]

## Ecosystem Connections
[How this relates to existing wiki concepts — link with [[wikilinks]]]

## Repo Vitals
- Stars: {N} | Forks: {N}
- Language: {lang}
- Last commit: {date} — {message}
- Active/stale assessment
```

**Important:** The Patterns section is the primary value — each pattern should state: what it is, why it works, where else it could apply.

Then proceed with normal ingest steps 2-7 (extract, discuss, create/update pages, update index + log).
