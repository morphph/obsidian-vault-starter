# AGENTS.md — obsidian-vault-starter (llm-wiki)

Guidance for any coding agent (Codex, Claude Code, Cursor, etc.). This repo is **both an Obsidian vault (content) and a small Python tooling layer**. Treat content and code differently. Full schema/conventions live in `CLAUDE.md`.

## Project overview
A personal LLM knowledge base: a curated Obsidian vault plus slash-command-driven Python scripts that ingest sources, maintain wiki pages, and draft articles. Package name `llm-wiki`.

## Repository structure
**Vault layers (content — edit only per the rules below):**
- `raw/` — immutable source docs (LLM reads, **never modifies**).
- `wiki/` — LLM-maintained knowledge base (flat; every page listed in `wiki/index.md`; ops appended to `wiki/log.md`).
- `drafts/` — publication drafts (human-owned).
- `learn/`, `references/`, `research/` — learning notes, create-from reference library, and Tier-4 research outputs respectively.
- `audience-profile.md` — voice/persona anchor. `archive/`, `events/`, `visuals/`, `docs/`.
- `.obsidian/` — Obsidian app config & plugins. **Do not modify** (workspace/layout/plugin state).
- `logs/` — tracked in git but **not materialized on disk in this clone** (sparse-checkout, ~91 MB). Run `git sparse-checkout disable` to fetch.

**Tooling (code — safe to develop):**
- `scripts/` — `ingest_url.py`, `learn_note.py`, `content_agent.py`, `obsidian_content.py`, plus `*-claude-remote.sh` helpers.
- `bin/obsidian-content` — CLI entry. `tests/` — offline unit tests. `pyproject.toml` — deps + ruff config.
- `.claude/` — slash commands (`/draft`, `/learn`, `/ingest`, `/query`, `/visualize`, …), `rules/`, `skills/`. Kept for Claude Code.

## Setup & development commands
- Runtime: **Python ≥ 3.12**. Install deps with `pip install -e .` or `uv sync` (deps: `claude-agent-sdk`, `python-dotenv`, `tzdata`).
- Copy env into a local `.env` (git-ignored); some scripts need an Anthropic key at runtime.

## Lint / typecheck / test / build
- **Lint:** `ruff check` (config in `pyproject.toml`, line-length 100). No typecheck config; no build step.
- **Tests (offline, safe):**
  ```bash
  python3 tests/test_ingest_url.py
  python3 tests/test_learn_note.py
  ```
  Both run against a throwaway repo skeleton with a fake claude binary — **no network, no model calls, production vault untouched.**

## Engineering & vault conventions
- Content vs code: the Python tooling is normal software; the vault is curated knowledge. Do not conflate them.
- `raw/` is immutable; `wiki/` is flat (no subdirs) and index-tracked; never make wiki claims without a `raw/` source.
- Never auto-ingest `research/` or `references/` material — only human-selected candidates via `/ingest`.

## Git & deployment rules
- Commit code and content changes with clear messages; there is no deploy step for this repo.
- Do not commit `.env`, secrets, or regenerate `logs/` into the working tree unnecessarily.

## Safety constraints (important for this repo)
- **Do not batch-format or bulk-rewrite Markdown**, notes, or vault content. Edit only the specific file a task requires.
- **Do not modify `.obsidian/`** — app settings, appearance, graph, plugin `data.json`, or workspace/layout state.
- **Do not launch Obsidian plugins that bulk-update the vault** (e.g. mass re-index, format-on-save sweeps).
- Do not touch content files unrelated to the task at hand.
- If a task has no build/test, validate with `git status`, structure checks, and config checks rather than editing content.

## Definition of Done
- Offline tests pass; `ruff check` has no **new** findings introduced by your change.
- No `.obsidian/` churn; no unrelated content files modified.
- Vault schema rules respected (index/log updated for wiki changes); descriptive commit message.
