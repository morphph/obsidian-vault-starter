# CODEX_MIGRATION.md — obsidian-vault-starter (llm-wiki)

## Locations
- **Old directory:** `/Users/yufanp/Desktop/Project/obsidian-vault-starter` (untouched)
- **New directory:** `/Users/yufanp/Developer/obsidian-vault-starter`
- **GitHub:** https://github.com/morphph/obsidian-vault-starter.git
- **Branch:** `main`
- **Tip commit:** `859265d` (new clone == old `main` == `origin/main`, exact match — old repo was already in sync).

## Clone method
Repo is 138 MB, dominated by `logs/` (~91 MB). Used a blobless partial clone + sparse checkout that **excludes `/logs/` from disk** (it stays fully tracked in git). Result: 83 MB working tree with the vault + tooling materialized. Restore logs with `git sparse-checkout disable`. No history was altered.

## Codex files created / modified
- **AGENTS.md** — created (did not exist). Distinguishes vault-content rules from code, documents structure, offline test/lint commands, and vault-specific safety constraints (no batch Markdown formatting, no `.obsidian/` edits).
- **CODEX_MIGRATION.md** — this report.

**No content, notes, or `.obsidian/` files were modified.** No `.codex/config.toml` created (nothing requires it).

## Old-path cleanup
None applied. A scan of execution areas (`scripts/`, `bin/`, `tests/`, `.claude/`, `pyproject.toml`) found **no** hardcoded `~/Desktop` / `~/Documents` paths. Any such strings elsewhere live in content directories (`wiki/`, `drafts/`, `raw/`, `research/`, `logs/`, `docs/`) and were intentionally left untouched (notes/content, not execution paths).

## Claude Code capability analysis
- `.claude/commands/` — `/draft`, `/learn`, `/learn-note`, `/ingest-anthropic-daily`, `/query`, `/visualize`, `/lint`. Kept for Claude Code.
- `.claude/skills/` (~27 MB) and `.claude/rules/` — kept intact.
- These slash commands map to the Python verbs in `scripts/` (`ingest_url.py`, `learn_note.py`, …), which are agent-agnostic and run standalone — so the core logic is usable from Codex via those scripts. The `.claude/` command wrappers are **Codex skill candidates** but were not mechanically converted (no functional need today).
- No secrets or personal account tokens found in `.claude/`.

### Cross-repo note
blog2video's `.codex/hooks.json` referenced `<vault>/hooks/pre-compact.py` and `hooks/session-start.py`. **Those files do not exist in this repo** (no `hooks/` dir) — the reference is stale. Flagged in blog2video's migration report; nothing to migrate here.

## Migrated
- Vault layer model, NEVER rules, and content/code separation → distilled into AGENTS.md.

## Not migrated (and why)
- `.claude/` commands/skills/rules — Claude-Code-specific; kept for Claude Code.
- Vault content and `.obsidian/` — deliberately untouched (this is a curated knowledge base, not code).

## Validation (safe, local; structure/config/test — no content mutation)
| Check | Result |
|-------|--------|
| Clone integrity: `git status` | clean (`## main...origin/main`) |
| Tip SHA vs `origin/main` | `859265d` == `859265d` ✅ |
| Write/delete in new dir (EPERM probe) | succeeds ✅ |
| `python3 tests/test_ingest_url.py` | **OK** ✅ (offline, fake binary) |
| `python3 tests/test_learn_note.py` | **OK** ✅ (offline, fake binary) |
| `ruff check scripts tests` | runs; 7 pre-existing style findings (e.g. E702) — **not introduced by migration** |
| `.obsidian/` files | untouched (no workspace churn) ✅ |
| Structure | vault layers + tooling intact; `logs/` sparse (tracked, not on disk) |

Note: sandbox Python is 3.10; `pyproject.toml` requires ≥ 3.12 (present on the Mac). The offline tests still passed here. No Obsidian plugin or vault-wide operation was run.

## TCC / EPERM status
New location `~/Developer/obsidian-vault-starter` is fully read/write/delete capable — **no TCC/EPERM risk**.

## Ready for Codex?
**Yes.** Clean, synced, offline tests pass, lint runs. Vault content is intact and untouched; AGENTS.md tells Codex how to treat content vs code. Use Python ≥ 3.12 and `pip install -e .` on the Mac for the tooling.
