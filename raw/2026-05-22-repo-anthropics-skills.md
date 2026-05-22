# anthropics/skills — Official Anthropic Skills Repo (GitHub Deep Scan)

**Source:** https://github.com/anthropics/skills
**Author/Org:** anthropics (Anthropic)
**Stars:** 138,882 | **Forks:** 16,386 | **Language:** Python | **Last updated:** 2026-05-22
**Fetch method:** GitHub Deep Scan (gh CLI)
**Fetched:** 2026-05-22

## What It Does

> "Skills are folders of instructions, scripts, and resources that Claude loads dynamically to improve performance on specialized tasks. Skills teach Claude how to complete specific tasks in a repeatable way."

The **official Anthropic repository** of example skills + the open-standard spec + a template. Distributed as a Claude Code plugin marketplace: `/plugin marketplace add anthropics/skills`. Three plugin bundles:

- `document-skills` — docx, pdf, pptx, xlsx (source-available, power Claude's native document capabilities)
- `example-skills` — 12 example skills (Apache 2.0 open source)
- `claude-api` — Claude API + Managed Agents reference skill

> "These skills are provided for demonstration and educational purposes only... meant to illustrate patterns and possibilities."

## Architecture

### File structure of a skill (the **official** anatomy)

```
skill-name/
├── SKILL.md (required)
│   ├── YAML frontmatter (name, description required)
│   └── Markdown instructions
└── Bundled Resources (optional)
    ├── scripts/    - Executable code for deterministic/repetitive tasks
    ├── references/ - Docs loaded into context as needed
    └── assets/     - Files used in output (templates, icons, fonts)
```

### Three-level progressive disclosure (concrete word counts)

| Level | When loaded | Size |
|---|---|---|
| **Metadata** (name + description) | Always in context | ~100 words |
| **SKILL.md body** | Whenever skill triggers | <500 lines ideal |
| **Bundled resources** | As needed (scripts can execute without loading) | Unlimited |

### Domain organization pattern

When a skill supports multiple variants, organize by variant in `references/` so Claude reads only the relevant file:

```
cloud-deploy/
├── SKILL.md (workflow + selection logic)
└── references/
    ├── aws.md
    ├── gcp.md
    └── azure.md
```

### The 17 example skills (full inventory)

**Creative & design (4):** algorithmic-art, brand-guidelines, canvas-design, theme-factory, slack-gif-creator
**Development & technical (4):** frontend-design, mcp-builder, web-artifacts-builder, webapp-testing
**Enterprise & communication (2):** internal-comms, doc-coauthoring
**Document skills (4):** docx, pdf, pptx, xlsx
**Meta (2):** ⭐ **skill-creator**, claude-api

### The template (trivially minimal)

```markdown
---
name: template-skill
description: Replace with description of the skill and when Claude should use it.
---

# Insert instructions below
```

That's literally the entire template — Anthropic says only `name` + `description` are required, the body is freeform markdown.

### The spec

`spec/agent-skills-spec.md` contains only one line pointing to the open standard at https://agentskills.io/specification. The spec lives off-repo.

---

## ⭐ skill-creator — Anthropic's Official Meta-Skill (the most important file)

`skills/skill-creator/SKILL.md` is the headline content of this repo. It's the official Anthropic playbook for **creating, improving, and optimizing skills**. Full text follows because every line is dense.

### Description (note the example of a "pushy" description)

> "Create new skills, modify and improve existing skills, and measure skill performance. Use when users want to create a skill from scratch, edit, or optimize an existing skill, run evals to test a skill, benchmark skill performance with variance analysis, or optimize a skill's description for better triggering accuracy."

### The core loop (stated 3 separate times in the file — Anthropic really wants you to internalize it)

```
1. Figure out what the skill is about
2. Draft or edit the skill
3. Run claude-with-access-to-the-skill on test prompts
4. With the user, evaluate the outputs:
   - Generate review viewer (eval-viewer/generate_review.py)
   - Run quantitative evals
5. Improve based on user feedback
6. Repeat until satisfied
7. Package and return the final skill
```

### Phase 1 — Capture intent (4 questions)

1. What should this skill enable Claude to do?
2. When should this skill trigger? (what user phrases/contexts)
3. What's the expected output format?
4. Should we set up test cases?
   - **Skills with objectively verifiable outputs** (file transforms, data extraction, code generation, fixed workflow steps) → yes
   - **Skills with subjective outputs** (writing style, art) → often don't need them

### Phase 2 — Write the SKILL.md (the "pushy description" rule)

> "Currently Claude has a tendency to **'undertrigger'** skills — to not use them when they'd be useful. To combat this, please make the skill descriptions a little bit **'pushy'**."

**Example of the same description, before and after:**

| Version | Description |
|---|---|
| Too passive | "How to build a simple fast dashboard to display internal Anthropic data." |
| **Pushy (correct)** | "How to build a simple fast dashboard to display internal Anthropic data. **Make sure to use this skill whenever the user mentions dashboards, data visualization, internal metrics, or wants to display any kind of company data, even if they don't explicitly ask for a 'dashboard.'**" |

### Phase 3 — Test cases

> "After writing the skill draft, come up with **2-3 realistic test prompts** — the kind of thing a real user would actually say."

Saved to `evals/evals.json`:

```json
{
  "skill_name": "example-skill",
  "evals": [
    {
      "id": 1,
      "prompt": "User's task prompt",
      "expected_output": "Description of expected result",
      "files": []
    }
  ]
}
```

Don't write assertions yet — just the prompts. Add assertions later while runs are in progress.

### Phase 4 — Run evals (with-skill vs baseline, **in the same turn**)

Workspace layout:

```
<skill-name>-workspace/
├── iteration-1/
│   ├── eval-0/
│   │   ├── with_skill/outputs/
│   │   ├── without_skill/outputs/   # baseline for new skill
│   │   ├── (or old_skill/outputs/   # baseline for improving existing)
│   │   ├── eval_metadata.json
│   │   ├── timing.json
│   │   └── grading.json
│   └── eval-1/ ...
│   ├── benchmark.json
│   └── benchmark.md
├── iteration-2/ ...
└── feedback.json
```

**Critical rule:** spawn with-skill AND baseline subagents **in the same turn, in parallel**. Don't do with-skill first and come back for baseline later.

**Baseline depends on context:**
- **Creating a new skill** → baseline is no skill at all (`without_skill/`)
- **Improving an existing skill** → snapshot the old version first (`cp -r <skill-path> <workspace>/skill-snapshot/`), point baseline at snapshot (`old_skill/`)

### Phase 5 — Grade & aggregate

Grading.json schema (the viewer depends on these exact field names):

```json
{
  "expectations": [
    {"text": "...", "passed": true/false, "evidence": "..."}
  ]
}
```

> "For assertions that can be checked programmatically, **write and run a script rather than eyeballing it** — scripts are faster, more reliable, and can be reused across iterations."

Aggregate:
```bash
python -m scripts.aggregate_benchmark <workspace>/iteration-N --skill-name <name>
```

Produces `benchmark.json` + `benchmark.md` with pass_rate, time, tokens — **mean ± stddev** with delta between configurations.

### Phase 6 — Analyst pass (what to look for, beyond aggregate stats)

- **Non-discriminating assertions** — pass regardless of whether skill is on
- **High-variance evals** — possibly flaky
- **Time/token tradeoffs** — skill might help quality but blow cost budget

### Phase 7 — Launch viewer for human review

```bash
nohup python <skill-creator-path>/eval-viewer/generate_review.py \
  <workspace>/iteration-N \
  --skill-name "my-skill" \
  --benchmark <workspace>/iteration-N/benchmark.json \
  > /dev/null 2>&1 &
```

User sees 2 tabs:
- **Outputs** — one test case at a time, prompt + output + (previous iteration output collapsed) + (formal grades collapsed) + feedback textbox (auto-saves) + previous feedback shown below
- **Benchmark** — stats summary with per-eval breakdowns + analyst observations

**Headless/Cowork environments:** use `--static <output_path>` to write standalone HTML; feedback downloads as a file.

### ⭐⭐⭐ Phase 8 — How to actually improve the skill (the 4 principles)

This section is **the most important paragraph in the entire repo** for anyone trying to make their skills better.

> "**1. Generalize from the feedback.** We're trying to create skills that can be used a million times across many different prompts. Here you and the user are iterating on only a few examples over and over again because it helps move faster... But if the skill you and the user are codeveloping works only for those examples, it's useless. Rather than put in fiddly overfitty changes, or oppressively constrictive MUSTs, if there's some stubborn issue, you might try branching out and using different metaphors, or recommending different patterns of working."
>
> "**2. Keep the prompt lean.** Remove things that aren't pulling their weight. Make sure to read the transcripts, not just the final outputs — if it looks like the skill is making the model waste a bunch of time doing things that are unproductive, you can try getting rid of the parts of the skill that are making it do that."
>
> "**3. Explain the why.** Try hard to explain the **why** behind everything you're asking the model to do. Today's LLMs are *smart*. They have good theory of mind and when given a good harness can go beyond rote instructions and really make things happen... **If you find yourself writing ALWAYS or NEVER in all caps, or using super rigid structures, that's a yellow flag** — if possible, reframe and explain the reasoning so that the model understands why the thing you're asking for is important. That's a more humane, powerful, and effective approach."
>
> "**4. Look for repeated work across test cases.** Read the transcripts from the test runs and notice if the subagents all independently wrote similar helper scripts or took the same multi-step approach to something. If all 3 test cases resulted in the subagent writing a `create_docx.py` or a `build_chart.py`, that's a **strong signal the skill should bundle that script.** Write it once, put it in `scripts/`, and tell the skill to use it. This saves every future invocation from reinventing the wheel."

### ⭐ Description Optimization (the trigger eval loop)

This is the most operationally novel part of the file — Anthropic's automated description-tuning protocol.

#### Generate 20 trigger eval queries (8-10 should-trigger + 8-10 should-not-trigger)

**The key rule for queries:** they must be **realistic and concrete** — what a real user would actually type.

> Bad: `"Format this data"`, `"Extract text from PDF"`, `"Create a chart"`
>
> Good: `"ok so my boss just sent me this xlsx file (its in my downloads, called something like 'Q4 sales final FINAL v2.xlsx') and she wants me to add a column that shows the profit margin as a percentage. The revenue is in column C and costs are in column D i think"`

Mix of:
- Different lengths
- Formal vs casual (typos, abbreviations, lowercase OK)
- File paths, personal context, column names, company names, URLs
- Backstory ("my boss sent me...", "the team's planning to...")
- **Edge cases > clear-cut cases**

**For should-trigger queries:** include different phrasings of same intent, cases where user doesn't explicitly name the skill or file type, uncommon use cases, cases where this skill competes with another but should win.

**For should-not-trigger queries:** the **most valuable** are **near-misses** — queries that share keywords with the skill but actually need something different. Don't make negatives obviously irrelevant ("write a fibonacci function" as a negative test for a PDF skill is too easy).

#### Run the optimization loop

```bash
python -m scripts.run_loop \
  --eval-set <path-to-trigger-eval.json> \
  --skill-path <path-to-skill> \
  --model <model-id-powering-this-session> \
  --max-iterations 5 \
  --verbose
```

What the loop does:
- **60/40 train/test split** (avoid overfitting)
- Each query run **3 times** to get a reliable trigger rate
- Calls Claude to propose description improvements based on what failed
- Re-evaluates each new description on both train and test
- Iterates up to 5 times
- **Selects best by test score** (not train score) to avoid overfitting

#### How skill triggering actually works (important nuance)

> "Skills appear in Claude's `available_skills` list with their name + description, and Claude decides whether to consult a skill based on that description. **The important thing to know is that Claude only consults skills for tasks it can't easily handle on its own** — simple, one-step queries like 'read this PDF' may not trigger a skill even if the description matches perfectly, because Claude can handle them directly with basic tools. **Complex, multi-step, or specialized queries reliably trigger skills when the description matches.**"

This means trigger eval queries must be **substantive** — simple queries are poor test cases regardless of description quality.

### Communication style (Anthropic's guidance to the meta-skill itself)

> "The skill creator is liable to be used by people across a wide range of familiarity with coding jargon... there's a trend now where the power of Claude is inspiring **plumbers to open up their terminals, parents and grandparents to google 'how to install npm'**."

Phrasing tiers:
- "evaluation" and "benchmark" — borderline, but OK
- "JSON" and "assertion" — wait for cues that user knows them
- Always OK to briefly explain a term if in doubt

### Writing style guidance

- **Imperative form preferred** in instructions
- **Don't use heavy-handed MUSTs** — use "theory of mind" and explain why things matter
- **Make skills general, not super-narrow to specific examples**
- Write a draft, then look at it with fresh eyes and improve

### Output format pattern

```markdown
## Report structure
ALWAYS use this exact template:
# [Title]
## Executive summary
## Key findings
## Recommendations
```

(Note: even Anthropic uses ALWAYS in their own template — context: defining a literal template is a legitimate use of must-style language, vs prescribing model behavior is where you should explain why instead.)

### Examples pattern

```markdown
## Commit message format
**Example 1:**
Input: Added user authentication with JWT tokens
Output: feat(auth): implement JWT-based authentication
```

---

## Tech Stack

- **Python** primary (eval scripts, aggregation, packaging)
- **Plugin marketplace** distribution via `.claude-plugin/marketplace.json`
- **JSON schemas** for evals, grading, benchmarks, feedback
- **HTML eval viewer** (browser-based human review tool)
- **Apache 2.0** for example skills; **source-available** for document skills (docx/pdf/pptx/xlsx)

## Key Patterns & Takeaways

### Pattern 1: "Pushy descriptions" combat undertriggering
Anthropic's own measurement: Claude **undertriggers** skills more often than it overtriggers. Counterintuitive fix is to write descriptions slightly more aggressively ("make sure to use this skill whenever..."), not more precisely. This contradicts the engineering instinct to be conservative.

### Pattern 2: Three-tier progressive disclosure with concrete budgets
- Metadata: ~100 words always in context
- SKILL.md body: <500 lines ideal, loaded on trigger
- Bundled resources: unlimited, loaded as needed

The 500-line ideal is more permissive than [[source-khairallah-claude-skills-automate-workflow|Khairallah's "under 500 lines"]] hard rule — Anthropic says "you can feel free to go longer if needed", but recommends adding hierarchy with pointers when approaching the limit.

### Pattern 3: Quantitative iteration loop with strict workspace structure
`workspace/iteration-N/eval-N/{with_skill,without_skill,old_skill}/` — the workspace structure is **load-bearing** because the viewer's HTML depends on it. Apply same pattern to non-coding work (content pipelines, marketing experiments).

### Pattern 4: Bundle repeated subagent work as scripts
If 3 test runs all independently wrote `create_docx.py`, that's a signal to write it once into `scripts/`. Generalizes: any pattern Claude reinvents 3+ times should become a deterministic script bundled with the skill.

### Pattern 5: Trigger eval realism over abstraction
"Format this data" is a useless eval query. "ok so my boss sent me this xlsx" is a useful one. The realism (typos, file paths, narrative context) is what makes the eval predictive of production behavior.

### Pattern 6: 60/40 train/test split + 3× runs for description optimization
Description optimization is treated as a small ML problem with proper train/test discipline. Each query runs 3× for variance. Select best by test score, not train, to prevent the description from overfitting to specific training queries.

### Pattern 7: "Look at the transcripts, not just outputs"
When a skill is too verbose or has the model doing unproductive work, the **transcript** reveals it, not the final output. This is the operational definition of "lean prompt" — read what Claude actually does step by step.

### Pattern 8: Domain variants in `references/`, not in SKILL.md
A `cloud-deploy` skill puts AWS/GCP/Azure docs in separate `references/` files. SKILL.md handles the selection logic. Claude loads only the relevant file. Saves context.

### Pattern 9: Plugin marketplace as distribution
The `.claude-plugin/marketplace.json` pattern lets a repo bundle multiple plugins (`document-skills`, `example-skills`, `claude-api`), each pointing to subsets of `skills/`. This is the canonical way to ship a skill library.

### Pattern 10: "Updating an existing skill" - preserve names & copy before editing
- Preserve the original skill directory name and `name` frontmatter (don't append `-v2`)
- Copy the installed skill to `/tmp/` before editing (the install path may be read-only)
- Package from the copy

## Ecosystem Connections

- This is the canonical implementation of [[agent-skills-standard]] (the open standard at agentskills.io)
- The skill-creator meta-skill is Anthropic's official answer to [[skillify-meta-skill|Garry Tan's /skillify]] — same idea, different implementation
- Description-optimization loop (60/40 train/test) parallels [[trigger-evals|trigger evals]] but at higher rigor
- The "pushy descriptions" finding **contradicts** the conservative-description instinct in [[agent-skills-standard]] and partially **complements** Tw93's "Don't use when..." finding (Tw93: be explicit about negatives; Anthropic: be aggressive about positives — combine both)
- The 4 improvement principles (generalize / lean / explain why / bundle repeated work) overlap heavily with [[source-mattpocock-skills-repo|Matt Pocock's 4-failure-modes framework]] but framed as positive guidance instead of failure taxonomy
- Aligns with [[thin-harness-fat-skills]] — Anthropic itself is publishing fat skills (skill-creator is ~500 lines of mostly markdown procedure)
- Eval workflow with `with_skill` vs `without_skill` baseline mirrors [[agent-improvement-flywheel|OpenAI's per-system-version improvement loop]] but at the skill level rather than the harness level

## Repo Vitals

- **Stars:** 138,882 | **Forks:** 16,386 (top-30 GitHub repo by stars)
- **Language:** Python (eval/aggregation scripts); SKILL.md content is markdown
- **Last commit:** 2026-05-22 — "Add CMA claude-api skill updates (#1164)" (active development, multiple updates per week)
- **Recent activity (last 10 commits):** Heavy focus on the `claude-api` skill — Managed Agents self-hosted sandboxes, mid-session agent updates, MCP tool-output offload, model migration. The example skills (algorithmic-art, brand-guidelines, etc.) are stable.
- **Maintainer:** Keith Lazuka (klazuka@anthropic.com) per marketplace.json
- **Assessment:** **Actively maintained**, canonical reference. License: Apache 2.0 for examples, source-available for document skills.

## Partner skills mention

The README explicitly highlights Notion as a partner skill provider: "Notion Skills for Claude" — pattern of third-party software vendors shipping skills for their own products. First-party precedent for what loreai.dev or blog2video could do (ship branded skills for their workflows).
