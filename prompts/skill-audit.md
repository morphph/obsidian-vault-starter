# Skill Audit & Excavation — Drop-in Prompt

Paste this whole file into a Claude Code session in any repo (LoreAI v2, blog2video, future repos). It is self-contained — Claude does not need to read any external wiki or memory to run it.

---

## Your role

You are auditing the slash commands / skills in this repo and excavating evidence for new ones. Apply the principles in the **Knowledge Base** section below. Three things matter most:

1. **Pushy descriptions** — Claude undertriggers skills by default; descriptions must aggressively enumerate trigger phrases so routing fires.
2. **Anti-triggers** — every description ends with "Don't use when…" pointing at the sibling skill that should fire instead. Tw93 measured +32 percentage points routing accuracy from this alone (73% → 53% without anti-examples → 85% with).
3. **Past evidence only** — propose new skills only when you can cite ≥3 concrete past instances of the workflow. No future speculation. (Garry Tan's rule: "if I have to ask you for something twice, you failed" — wait until ask #3 to skillify.)

## Working mode: propose-confirm

Do **not** edit files or run git commands without the user's explicit OK on the specific change. Batch your proposals into one report at the end of each phase, then ask:

- "Approve all?" — apply every proposed change
- "Approve some?" — user lists which numbers to apply
- "Modify N?" — user gives feedback, you re-propose just that one

Edit only after the user OKs. After editing, commit + push per the repo's git conventions (check `CLAUDE.md` if it exists; default is one commit per phase with descriptive message).

---

## Phase 0 — Repo orientation (always, ≤5 min)

Before anything else, scan to understand what's here:

1. **List existing slash commands**: `ls .claude/commands/ 2>/dev/null` and `ls ~/.claude/commands/ 2>/dev/null`
2. **Read CLAUDE.md** (project root + `~/.claude/CLAUDE.md` if any) to understand repo conventions
3. **Detect language mix**: `grep -rl "[一-鿿]" --include="*.md" . 2>/dev/null | head -5` — if Chinese content exists, plan to add bilingual triggers in audit/excavation. If not, English-only is fine.
4. **Locate evidence sources** for the excavation phase. Candidates to check (any may be absent):
   - `git log --oneline -n 200` — recurring commit patterns
   - Session/journal/log files: `find . -maxdepth 3 -name "log.md" -o -name "CHANGELOG.md" -o -name "session-*.md" -o -name "daily-*.md" 2>/dev/null`
   - Scripted task lists: `cat package.json | grep -A 30 '"scripts"' 2>/dev/null`, `Makefile`, `justfile`, `tasks.json`
   - Recurring file patterns in the repo: `ls | awk -F'-' '{print $NF}' | sort | uniq -c | sort -rn | head -10` (cheap heuristic for repeating naming patterns)
   - README workflow sections, `docs/`, `notes/`

Report a one-paragraph orientation: "This repo has N existing commands at PATH, uses LANGUAGE(S), and has the following candidate evidence sources: …". Then proceed.

---

## Phase 1 — Audit existing slash commands

**Skip this phase** if Phase 0 found zero commands. Tell the user "no existing commands — skipping to Phase 2" and move on.

### For each existing command file:

1. Read the file (just the frontmatter + first ~30 lines)
2. Determine the **current description quality** against the four checks below
3. Draft a **rewritten description** following the template

### Quality checks (failing any one = needs rewrite)

| Check | Pass criterion |
|-------|---------------|
| Opener | Starts with **"Use this skill whenever…"** (or "Use whenever…") |
| Enumeration | Lists **5-9 trigger phrases** (or near-phrases) the user might actually say |
| Anti-trigger | Ends with **"Don't use when…"** pointing at a sibling command |
| Length | Under **1,024 chars** (Anthropic's per-skill budget; the global `SLASH_COMMAND_TOOL_CHAR_BUDGET` is 1,536 combined with `when_to_use`) |

### Rewrite template

```
"Use this skill whenever the user wants to <core intent>.
Triggers: '<phrase 1>', '<phrase 2>', '<phrase 3>', '<phrase 4>',
'<phrase 5>'<, '<bilingual phrase if natural>'>.
<Optional catch-all: 'Use even if the user hasn't explicitly said
"<command name>" — when they ask for X, Y, Z'>.
**Don't use when** <near-miss case> — use `/<sibling-command>` instead."
```

### Sharp rules to apply

- **Imperative voice** ("Use this skill…"), not descriptive ("This skill helps you…")
- **No ALL CAPS MUSTs** — Anthropic flags these as a yellow flag; reframe as theory-of-mind ("when the user…")
- **No emojis** in descriptions
- **Bilingual triggers only where natural** — if the user really would say "把这个加入 wiki", include it; don't translate every phrase mechanically
- **Near-miss anti-triggers beat generic ones** — "Don't use when ingesting a fresh source" (concrete) beats "Don't use for unrelated tasks" (vague)
- **Front-load the key use case** — first sentence should make the most common trigger crystal clear; description gets truncated at 1,536 chars combined
- **Argument hint as a separate field** — if the current description embeds usage syntax like `"Usage: /foo <arg>"`, extract it into an `argument-hint: "<arg>"` frontmatter field (cleaner, surfaces in the autocomplete UI)

### Report format at end of Phase 1

Show one block per command:

```
### N. `/<command-name>`
**Current** (NNN chars): "<paste current description>"
**Proposed** (NNN chars): "<paste new description>"
**Why changed**: <one line — e.g., "added 6 triggers and anti-trigger to /sibling">
```

Then ask: **"Approve all N proposals? Or pick specific numbers? Or modify any?"**

After approval, edit each file's frontmatter `description:` line (and add `argument-hint:` where extracted), then commit + push.

---

## Phase 2 — Excavate new skill candidates from past evidence

This phase produces a **candidate list** — you do NOT build any skills in Phase 2. The user picks 0, 1, or several after seeing the report.

### The hard rule (do not violate)

A pattern is a candidate only if you can cite **≥3 concrete past instances** in this repo. If you catch yourself writing "this could be a skill for future X" — **stop and delete that candidate**. The whole point of waiting is that speculative skills bloat the description budget and pollute routing.

### Where to look (adapt to what Phase 0 found)

Look for repetition in:

1. **Git log patterns** — search for repeated commit-message prefixes or verbs:
   ```bash
   git log --since="6 months ago" --pretty=format:"%s" | awk '{print $1}' | sort | uniq -c | sort -rn | head -20
   ```
   Any prefix appearing ≥3 times with the same shape is a candidate (e.g., 7 commits starting with "session:" → candidate `/session` skill).

2. **Recurring file shapes** — files matching the same template:
   ```bash
   find . -maxdepth 4 -name "*.md" | xargs -I{} head -5 {} 2>/dev/null | grep -c "^# Some Common Header"
   ```
   If 3+ files share an obvious template (e.g., session captures with `Context / Decisions / Lessons / Actions` headings), the template generation is a candidate.

3. **Logs / journals** — read the most recent 100-300 lines of any `log.md`, `CHANGELOG.md`, or journal file. Look for repeated **operation verbs** (compile, sync, deploy, backfill, audit, sweep, digest) and group by verb.

4. **Drafts / artifacts with consistent frontmatter** — if 3+ files in a `drafts/`, `posts/`, `articles/`, or output dir share unusual frontmatter fields (e.g., `target-audience`, `source-policy`, `framing`), that artifact type is a candidate.

5. **Scripts/Makefile/package.json** — recurring multi-step commands worth promoting:
   ```bash
   cat package.json | grep -A 50 '"scripts"' 2>/dev/null
   cat Makefile 2>/dev/null
   ```

6. **CLAUDE.md procedures** — Anthropic's own guidance: **"when a section of CLAUDE.md has grown into a procedure rather than a fact, it should become a skill."** Scan CLAUDE.md for multi-step instructions and propose extraction.

### For each candidate, report:

```
### Candidate N — `/proposed-name` (ROI: HIGH | MEDIUM | LOW)

**Evidence (≥3 instances):**
- <cite specific file/commit/log line 1>
- <cite specific file/commit/log line 2>
- <cite specific file/commit/log line 3>

**Differentiation from existing skills:**
<one paragraph — what makes this distinct from /<sibling>>

**Proposed triggers (4-6):**
- "<phrase 1>"
- "<phrase 2>"
- ...

**Anti-trigger:** "Don't use when <near-miss> — use `/<sibling>` instead."

**Frequency estimate:** <X times in last N days>

**Caveats:** <any flags — e.g., dormant pattern, only-applies-to-bilingual-content>
```

### Sub-threshold patterns

Be transparent. List patterns that **almost** crossed the bar (1-2 instances) but didn't, so the user can correct you if memory matches. Phrase them as:

> Sub-threshold (not candidates, listed for your review):
> - `<pattern>` — only N instance(s); below ≥3 bar.

### Report format at end of Phase 2

A markdown report listing all candidates (typically 0-5; if you have >5, your bar is too loose — re-check the ≥3 rule), plus the sub-threshold list, plus a recommended pick.

Then ask: **"Which do you want to build? (numbers, 'none', or 'all')"**

Do NOT build anything in this phase. The build itself is the user's call and may be a separate session.

---

## Knowledge Base — the principles inline

(You don't need to look these up; everything you need is here.)

### Why descriptions must be pushy

> "Currently Claude has a tendency to **'undertrigger'** skills — to not use them when they'd be useful. To combat this, please make the skill descriptions a little bit **'pushy'**."
> — Anthropic skill-creator (the official meta-skill at `github.com/anthropics/skills`)

Concrete contrast:

| Passive (bad) | Pushy (good) |
|---|---|
| "How to build a dashboard." | "**Use this skill whenever the user mentions dashboards, data visualization, internal metrics, or wants to display any kind of company data, even if they don't explicitly ask for a 'dashboard.'**" |

### Why anti-triggers are non-negotiable

Tw93 (Tencent, Claude Code engineer) measured the routing accuracy of his agents. Without "Don't use when" clauses: **53%** accuracy. With them: **85%**. The "Don't use when" half of the description is doing more work than the "Use when" half. Anti-triggers also reduced response time by ~18% because Claude stopped considering wrong skills.

### Why the ≥3-instance rule

Garry Tan (Y Combinator, builds gbrain/gstack — open-source skill systems with 9,700+ stars):

> "If I have to ask you for something twice, you failed."

`/skillify` waits for the **third** occurrence before turning a workflow into a skill. The reason: a skill written before you've done the task at least twice captures the wrong pattern. You don't know which abstraction is right until you've executed the workflow.

Anthropic's foundational Skills blog (2025-10-16) makes the same point:

> "Iterate with Claude — request that Claude capture successful approaches and common mistakes into reusable context within a skill. This will help you discover what context Claude actually needs, **instead of trying to anticipate it upfront**."

### Why descriptions stay short and lean

| Tier | When loaded into Claude's context | Budget |
|---|---|---|
| **Metadata** (name + description) | **Always** | **~100 words / 1,024 chars per skill, 1,536 chars combined with `when_to_use`** |
| SKILL.md body | Only when skill invokes | <500 lines ideal |
| Bundled resources (scripts, references) | On-demand | Unlimited |

If descriptions are too long or too many skills exist, Claude literally cannot see the trigger keywords — they get truncated. **Front-load the key use case in the first sentence.**

### Anthropic's 4 improvement principles (when polishing a description that didn't route well)

1. **Generalize from feedback.** Don't add "fiddly overfitty MUSTs"; try different metaphors or reframe.
2. **Keep the prompt lean.** If the skill makes Claude waste time on unproductive things, cut those parts.
3. **Explain the why.** ALL CAPS MUSTs are a yellow flag — reframe as theory-of-mind explanation.
4. **Look for repeated work.** If multiple test cases ended up writing the same script, **bundle that script as a resource file** rather than re-deriving it each time.

### The most honest test-case discovery heuristic

If you ever want to validate a description with real trigger evals:

> "Search your conversation history for when you said 'fucking shit' or 'wtf.' Those are the test cases you're missing."
> — Garry Tan

Frustration moments are the empirical proof of routing failures.

---

## Worked example (real audit, 2026-05)

Before/after of a real description rewrite in a wiki repo, for calibration:

**Before** (factual, 75 chars):
```
description: "Ask a question against the wiki. Usage: /query <question>"
```

**After** (pushy + anti-trigger, 502 chars):
```
description: "Use this skill whenever the user asks a question whose
answer should come from the wiki rather than general knowledge.
Triggers include: 'what does the wiki say about X', 'do we have
notes on Y', 'remind me what Z is', 'I think we ingested something
about W', '我们 wiki 里有 X 吗', or any question where the user is
testing recall of previously ingested material. **Don't use when**
the user is asking a new question that requires ingesting fresh
sources first — suggest `/ingest` instead."
```

What changed: pushy opener, 5 trigger phrases (4 EN + 1 ZH because repo is bilingual), one catch-all ("any question where the user is testing recall"), and an anti-trigger pointing at the sibling `/ingest` command. 502 chars — well under the 1,024 budget.

---

## End-of-session output format

When both phases are done, summarize as:

```
## Phase 1 — Audit results
- N existing commands audited
- N descriptions rewritten (commit: <sha>)
- N commands already passing all checks (no change)

## Phase 2 — Excavation results
- N candidates above ≥3-instance bar
- N sub-threshold patterns surfaced
- Recommended pick: <name>

## Next step
You decide: build any candidates from Phase 2, or ship and revisit later.
```

---

## What this prompt does NOT do

- Does **not** build new skills automatically — that's a follow-up session after the user picks.
- Does **not** run automated trigger evals — that's Anthropic's heavier 20-query / 60-40 / 3× / 5-iter optimization loop, only worth it for skills used >100×/month.
- Does **not** edit anything without user confirmation.
- Does **not** delete commands (proposing a `disable-model-invocation: true` setting is fine; deletion is the user's call).

---

## If something goes wrong

- **No commands found and no evidence sources found** → tell the user "this repo has nothing to audit or excavate yet; come back after you've built workflows" and stop.
- **More than ~10 commands** → audit in batches of 5, check in between batches.
- **Evidence is ambiguous** (e.g., 3 files share a header but feel like coincidence) → flag it as sub-threshold rather than a candidate; let the user decide.
- **User wants you to skip Phase 1 or Phase 2** → honor it; this prompt is a default flow, not a contract.
