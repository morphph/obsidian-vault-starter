---
status: draft
lang: en
sources:
  - raw/2026-05-14-openai-codex-hooks-docs.md
  - raw/2026-05-05-openai-blog-long-horizon-tasks-codex.md
  - raw/2025-10-07-openai-cookbook-plans-md-multi-hour.md
  - raw/2026-05-09-openai-cookbook-using-goals-in-codex.md
external-refs:
  - https://developers.openai.com/codex/cli
  - https://developers.openai.com/codex/ide
  - https://developers.openai.com/codex/guides/agents-md
  - https://developers.openai.com/codex/config-basic
  - https://developers.openai.com/codex/config-reference
  - https://developers.openai.com/codex/models
  - https://developers.openai.com/codex/mcp
  - https://developers.openai.com/codex/pricing
  - https://developers.openai.com/codex/changelog
  - https://openai.com/index/introducing-gpt-5-5/
research: research/openai-codex/
platform: blog
created: 2026-07-06
last-updated: 2026-07-06
tags: [draft]
---

<!-- HOOK: [placeholder for opening hook —— suggest the contrast "installing Codex is one line; my first run still went sideways"] -->

# Getting Started with OpenAI Codex: From Install to Your First Task, Verified Against the Docs

**The takeaway first (who this is for, what you'll get):** If you already use Claude Code or Cursor and want to add OpenAI Codex to your workflow, this guide walks you from install to a working first task — every claim checked against the official docs. But the one thing I actually want you to leave with is this:

> **The real barrier to getting started with Codex isn't installation — it's the mental model.** Installing is one line. The reason most people's first run underwhelms is that they treat Codex like "fancy autocomplete inside an IDE" — that framing is too shallow, and so is the usage. Codex is an **agent that reads, edits, and runs code on your machine.** So the first thing you do isn't type a prompt — it's **write an AGENTS.md, then let it work.** The entire weight of this guide sits on two words: the **config layer.**

**What Codex is (a clean definition):** Codex is OpenAI's **agentic coding agent** — the official framing is "read, edit, and run the code on your machine" — and it's **open source, written in Rust.** [Official · developers.openai.com/codex/cli](https://developers.openai.com/codex/cli)

> [!warning] Don't confuse the versions
> Plenty of third-party pages still describe Codex as "a cloud autonomous agent launched May 2025, driven by the GPT-5 family." That's the **old, cloud-only 2025 Codex.** The 2026 product is a **CLI-first platform with four surfaces.** Any "cloud-only / launched 2025-05" description is stale for the current product.

---

## 1. Four Surfaces: One Product, Four Entry Points, One Shared Config

Codex isn't a single CLI — it's **four surfaces that share the same approval policy, MCP setup, AGENTS.md, and model preferences.** Which one you pick depends on who you are:

| Surface | What it is | Who it's for |
|---|---|---|
| **CLI** (terminal) | The workhorse for real work | Solo builders, anyone who wants it scriptable |
| **IDE extension** | VS Code + JetBrains; also runs inside Cursor / Windsurf | People who already live in an editor |
| **Desktop App** | macOS / Windows; parallel threads + one worktree per thread + diff review + automations | People running multiple task lines at once |
| **Codex Cloud** | Runs background / long tasks against a GitHub repo, keeps going after you close your laptop | Teams, long-running jobs |

[Official · developers.openai.com/codex/ide](https://developers.openai.com/codex/ide) · [/codex/cli](https://developers.openai.com/codex/cli)

**Role-based note:** If you're a **solo builder**, CLI + App is plenty. If you're a **team lead**, Cloud is the one built for you (background runs, diff review, automations). But remember — **the config is identical across all four.** The work you put into AGENTS.md and config.toml pays off on every surface.

---

## 2. Install & Sign In: It Really Is One Line

macOS / Linux, pick one:

```bash
# Option A: official installer (recommended)
curl -fsSL https://chatgpt.com/codex/install.sh | sh
# Unattended / CI — add the env var:
CODEX_NON_INTERACTIVE=1 curl -fsSL https://chatgpt.com/codex/install.sh | sh

# Option B: npm (requires Node ≥ 22)
npm i -g @openai/codex
```

Then start it from the terminal:

```bash
codex
```

**Sign in:** The first run lets you choose — log in with a **ChatGPT account**, **or** provide an **API key.** [Official · developers.openai.com/codex/cli](https://developers.openai.com/codex/cli)

At this point you might think "that's it?" — yes, installing is that easy. **And that's exactly the point: freshly installed, you're still one AGENTS.md away from actually using it well.** The real work starts below.

---

## 3. Your First Task: Write AGENTS.md First, Then Let It Work

The classic beginner mistake is to install, point Codex at an empty repo, and type "add a login feature." Codex will do something — but it knows **nothing about your project's conventions**: naming, directory layout, which files are off-limits, which test framework you use.

The right order is:

1. **Write an AGENTS.md at the project root first** (minimal template in the next section) — the spec Codex reads before it touches anything.
2. **Then hand it the task.** Describe the task with a **quantified definition of done**, not "looks right to me."
3. For complex / long-horizon tasks, use `/goal` to break the objective into a verifiable loop. The "Goal → Repair → Improvement" three-layer loop methodology is covered in depth elsewhere in the vault, so I won't repeat it here — just know `/goal` is the switch that turns "a one-line ask" into "a loop the agent can verify itself against." (See further reading at the end.)

In one line: **Codex doesn't lack execution — it lacks the project context you haven't fed it yet.** The standard move for feeding that context is AGENTS.md.

---

## 4. AGENTS.md: The Real Leverage

This is the center of gravity. There's a meme in practitioner circles — **"the leverage isn't the model, it's those 30 lines of AGENTS.md"** — and it's right.

**What AGENTS.md is:** a markdown instruction file Codex reads before it acts. It has **three priority levels**, merged from far to near, with the nearest overriding the rest:

1. **Global** — `~/.codex/AGENTS.md` (your preferences across all projects)
2. **Project** — from the repo root down to your current working directory
3. **Merge rule** — layered from root downward; instructions closest to the cwd win

A few knobs worth knowing: `project_doc_max_bytes` (how much it reads), `project_doc_fallback_filenames`; the fallback filename order is `AGENTS.override.md → AGENTS.md → TEAM_GUIDE.md → .agents.md`. [Official · developers.openai.com/codex/guides/agents-md](https://developers.openai.com/codex/guides/agents-md)

> [!note] Don't call it an "industry standard"
> Some say AGENTS.md is a "cross-tool industry standard." The docs only present it as a **Codex feature** (they mention an agents.md site but don't claim industry-wide adoption). So don't write it up as a "standard" — that's unconfirmed.

**A copy-paste minimal AGENTS.md:**

```markdown
# AGENTS.md

## Project conventions
- Language / framework: <e.g. TypeScript + Next.js>
- Layout: business logic in src/, tests in tests/, no new top-level dirs
- Naming: components PascalCase, utilities camelCase

## Read before acting
- Run `npm test` after any change; only "all green" counts as done
- Never touch `migrations/` or `.env*`
- Commit messages in the imperative, describing what changed

## Definition of done
- Feature works + tests pass + no lint errors
```

**Why it's the leverage:** the docs and the practitioners agree — **AGENTS.md + config.toml + parallel worktrees** is where the gap opens up, not "switch to a stronger model." Ten minutes spent nailing 30 lines of convention beats hours agonizing over 5.5 vs 5.4.

---

## 5. config.toml: Three Knobs — approval / sandbox / model

If AGENTS.md tells Codex *what your project looks like*, config.toml tells Codex *how far you're letting it go.*

File locations:
- **User level** — `~/.codex/config.toml`
- **Project level** — `.codex/config.toml`
- State lives in `CODEX_HOME` (default `~/.codex`)
- `-c key=value` on the CLI for a one-off override

The three keys that matter most:

```toml
model = "gpt-5.5"                 # default model
approval_policy = "on-request"    # untrusted / on-request / never
sandbox_mode = "workspace-write"  # read-only / workspace-write / danger-full-access
```

[Official · developers.openai.com/codex/config-basic](https://developers.openai.com/codex/config-basic) · [full reference at /config-reference](https://developers.openai.com/codex/config-reference)

> [!tip] Don't start at full-access
> The single most useful starter practice: **begin with `sandbox_mode = workspace-write` + `approval_policy = on-request`** — not `danger-full-access` out of the gate. The former lets Codex edit the workspace but asks you before each action; once you've learned its habits, loosen up.

---

## 6. Which Model? GPT-5.5 vs Those "-Codex" Suffixes — Who's Who

This is the first place readers genuinely get stuck, and the section I think most deserves an honest walkthrough.

**Current default = GPT-5.5.** As of 2026-07 it's the recommendation for most Codex tasks; it landed in Codex around 2026-04-23; on the same task it uses **~40% fewer output tokens** than GPT-5.4 — not hand-waving, a verifiable money-saver. [Official · developers.openai.com/codex/models](https://developers.openai.com/codex/models) · [GPT-5.5 launch](https://openai.com/index/introducing-gpt-5-5/)

**Model cheat sheet:**

| Model | Role | When to use |
|---|---|---|
| **GPT-5.5** | Current default, frontier line | Most tasks, saves tokens |
| **GPT-5.4** | Previous frontier | Fall back when needed |
| **GPT-5.4 mini** | Cheap, fast | Boring bulk work, save money |
| **GPT-5.3-Codex-Spark** | Faster variant | Research preview (Pro only) |
| ~~GPT-5.3-Codex / GPT-5.2~~ | **Deprecated** | Removed for ChatGPT-login users |

**The naming trap (this is the real point):** you have to separate two lines —
- **The general frontier line**: GPT-5.4 / **5.5**, which now drives Codex;
- **The old "-Codex" suffix models**: GPT-5.2-Codex / 5.3-Codex, which are **being deprecated and replaced.**

The 2026 direction is clear: **consolidate onto the general frontier model (5.5); the dedicated "-Codex" suffix is on its way out.** So when you see a name like "5.3-Codex" elsewhere, it's likely stale — defaulting to GPT-5.5 is the safe call. [Official · developers.openai.com/codex/models](https://developers.openai.com/codex/models) · [changelog](https://developers.openai.com/codex/changelog)

**On pricing** (bundled with your ChatGPT plan): Free $0 · **Go $8** · **Plus $20** · **Pro from $100** (5× / 20× the rate limit of Plus) · Business $20/seat · Enterprise / Edu custom; API-key usage billing is also supported. [Official · developers.openai.com/codex/pricing](https://developers.openai.com/codex/pricing) (Pricing / rate limits move fast — check the current official page before you buy.)

---

## 7. A Peek Past the Basics: MCP / Hooks / What's New in 2026

Once the starter trio (AGENTS.md + config + model) clicks, here's where to explore:

- **MCP** — Codex supports MCP; configure it under `[mcp]` in `config.toml`, with dedicated docs at `/codex/mcp`. (Confirm exact TOML syntax against the official page.) [Official · developers.openai.com/codex/mcp](https://developers.openai.com/codex/mcp)
- **Hooks** — turn that "never touch `migrations/`" line in AGENTS.md from a **convention** into a **guarantee**: hooks intercept before an action (exit 2 blocks it outright), so "don't touch it" becomes "can't touch it." Codex Hooks went **GA on 2026-05-14.** [Tier-1 internal source · raw/2026-05-14-openai-codex-hooks-docs.md]

**Key 2026 H1 updates (timeline):**

| Date | Event |
|---|---|
| **2026-04-23** | GPT-5.5 lands in Codex (~40% fewer output tokens) |
| **2026-05-14** | Codex Hooks GA |
| ~2026-05-29 | Computer Use on Windows |
| ~2026-06-02 | Sites plugin |
| ~2026-06-18 | Record & Replay → a demo becomes a reusable skill (macOS, excl. EEA/UK/CH) |
| **~2026-06-25** | Codex Remote GA (control your host from your phone + QR pairing) |

[Official · developers.openai.com/codex/changelog](https://developers.openai.com/codex/changelog)

---

## 8. For Claude Code Users: Same Mental Model, Different CLI

If you're already a Claude Code veteran, good news — **you don't relearn, you port.** hooks / skills / subagents / cloud have converged across vendors and map almost one-to-one. The right framing isn't the "Codex vs Claude Code, who's stronger" benchmark shouting match — it's "same mental model, different CLI, up and running in ten minutes."

| Claude Code concept | Codex equivalent |
|---|---|
| CLAUDE.md (project spec) | **AGENTS.md** (three priority levels) |
| Permission / approval modes | **approval_policy** (untrusted / on-request / never) |
| Sandbox | **sandbox_mode** (read-only / workspace-write / danger-full-access) |
| hooks | **hooks** (GA 2026-05-14) |
| skills / subagents | Codex skills / subagents |
| Background / cloud tasks | **Codex Cloud** |

The port path: move your CLAUDE.md instincts into AGENTS.md, map your permission intuition onto approval_policy + sandbox_mode, and the rest is just a different command set. **Don't fight them — use them side by side.**

---

<!-- CTA: [placeholder for closing CTA —— nudge the reader to "write your first AGENTS.md before you run anything," with a link into the vault methodology pieces] -->

## Wrap-up: The Barrier Isn't Install — It's Whether You Configure First

Back to the opening line: **the real barrier to getting started with Codex isn't installation — it's the mental model.** Installing is a one-line affair. Treating it as an agent that reads, edits, and runs code — writing its AGENTS.md before you let it act — is the watershed between "used it once" and "using it as leverage."

**Further reading (the vault's methodology layer, not covered here):**
- `/goal` + the three-layer nested loop (Goal → done / Repair → quality / Improvement → evolution) — the methodology that turns a one-line ask into a self-verifying loop.
- Chris Hayduk (OpenAI FDE) on three `/goal` moves: quantified goals + tight feedback + three files.
- The AGENTS.md + PLANS.md combo for running multi-hour long-horizon tasks.
