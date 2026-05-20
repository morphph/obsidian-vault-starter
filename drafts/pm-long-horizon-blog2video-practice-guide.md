---
type: draft
status: practice-guide
created: 2026-05-19
last-updated: 2026-05-20
target-audience: vfan（个人 practice first；跑通后再回填 case study 到主文）
companion-article: drafts/pm-long-horizon-methodology.md
case-project: blog2video — chapter splitter (narration.md → video_1_script.md)
source-policy: 与主文一致 —— 只引用 OpenAI / Anthropic 官方 docs + Ralph Wiggum 社区经典 + Matt Pocock 公开材料
based-on:
  - wiki/claude-code-goal.md
  - wiki/source-openai-codex-cookbook-trilogy.md
  - wiki/source-openai-codex-use-case-follow-goals.md
  - wiki/source-openai-long-horizon-tasks-codex.md
  - wiki/source-claude-code-routines-docs.md
  - wiki/source-claude-code-scheduled-tasks-docs.md
  - wiki/source-claude-code-channels-docs.md
  - wiki/source-claude-code-hooks-docs.md
  - wiki/claude-code-agent-view.md
  - wiki/source-claude-code-programmatic-usage-docs.md
  - wiki/idea-to-afk-agent-flow.md
  - wiki/grill-with-docs.md
  - wiki/blog2video.md
tags: [drafts, practice-guide, blog2video, claude-code, automation, pm-workflow]
---

# 实操指南：用 blog2video chapter splitter 跑通 PM 长跑工作流 + 真正 AFK 工具链

> 📌 **使用说明**：这不是发表文章，是给你（vfan）个人按步骤跑通主方法论 + 工具链的 practice guide。
>
> 跑完后填底部的"复盘记录"，那些数据就是 case study 素材，可以回填到主文。

---

## 总览：你将跑通的 5 个 phase

| Phase | 主文映射 | 这一阶段你 build 什么 |
|---|---|---|
| **A. Spec** | 动作 1-2 | `docs/chapter-spec.md` + validator 脚本 |
| **B. Durable files** | 动作 3 | `docs/Prompt.md` / `Plan.md` / `Implement.md` |
| **C. Hooks** | 主文 Part 3 Layer 4 | `.claude/settings.json` 的 PreToolUse + PostToolUse + Stop 配置 |
| **D. Calibrate** | 动作 4 | 跑 in-session `/goal`，迭代 spec 直到收敛 |
| **E. AFK Deploy** | 动作 5 + Part 3 Layer 2,3,5 | `claude --bg` → cloud routine → Telegram channel |

A-B 主要是写 markdown。C 是写 shell + JSON。D 是看 turn 然后改 spec。E 是把 AFK 从 toy 升级到 production。

---

## Phase A — Spec

### A1. Grill 模糊愿望

打开 blog2video repo：

```
/grill-with-docs

我想要 build 一个 chapter splitter。输入是 docs/input/narration.md，
输出是带 [SLIDE N] markers + timecodes 的 docs/output/video_1_script.md。
帮我把"什么是好 chapter"问清楚。
```

预期 agent 会问类似（每个带它的推荐答案）：

- 每个 chapter 时长目标？（推荐 30-60 秒）
- chapter 内部结构？（推荐 hook + 论点 + 例证三段）
- 第一个 chapter 硬性约束？（推荐：8 秒内带 thesis）
- 最后一个 chapter 硬性约束？（推荐：以 CTA 结尾）
- 总 narration 长 / 原文长比例？（推荐 ≤ 1/3）
- 哪些"反 pattern"禁止？（推荐：summary / overview / 元描述）
- chapter 间允许内容重复吗？（推荐：禁止）
- narration 输入字数下限 / 上限？

落到 `docs/chapter-spec.md`。

**校准信号**：如果你 30% 以上问题答 "agent 你建议"，说明这 feature 你脑子里没想清 —— 这就是 grill 的价值。

### A2. 写 validator 脚本

Validator 不只是 "spec 的辅助"。Phase C 里它会变成 PostToolUse hook，**agent 改完文件 validator 不过 = 操作被 block**。换句话说，validator 决定了你的"自动化纪律"水平。

`scripts/validate-chapter-format.ts`：

```ts
#!/usr/bin/env tsx
// 输入: docs/output/video_1_script.md (argv[2] or default)
// 退出码: 0 = pass, 1 = fail
// 输出: 失败原因到 stdout

import fs from "node:fs";
import path from "node:path";

const file = process.argv[2] ?? "docs/output/video_1_script.md";
if (!fs.existsSync(file)) {
  console.error(`File not found: ${file}`);
  process.exit(1);
}

const content = fs.readFileSync(file, "utf8");

const failures: string[] = [];

// 1. 切 chapter
const chapters = content.split(/\[SLIDE \d+\]/).slice(1);
if (chapters.length === 0) failures.push("no [SLIDE N] markers found");

// 2. 每个 chapter word count 100-300 (30-60s @ 200 WPM, 中英混合放宽)
chapters.forEach((ch, i) => {
  const wc = ch.trim().split(/\s+/).length;
  if (wc < 100 || wc > 300)
    failures.push(`chapter ${i + 1}: word count ${wc} not in [100, 300]`);
});

// 3. 第一个 chapter 前 25 词包含 thesis 关键词
const first25 = chapters[0]?.trim().split(/\s+/).slice(0, 25).join(" ") ?? "";
// 启发式：含数字 / 问号 / 反常识词
if (!/[?？]|\d|\b(but|however|不是|反而|意外)\b/.test(first25))
  failures.push("first chapter first-25-words missing hook signal (?/digit/反常识)");

// 4. 最后 chapter 含 CTA 关键词
const last = chapters[chapters.length - 1] ?? "";
if (!/(关注|订阅|如果你|下一篇|follow|subscribe)/i.test(last))
  failures.push("last chapter missing CTA keyword");

// 5. 总长 ≤ 原文 1/3
const sourceFile = "docs/input/narration.md";
if (fs.existsSync(sourceFile)) {
  const srcWc = fs.readFileSync(sourceFile, "utf8").split(/\s+/).length;
  const outWc = content.split(/\s+/).length;
  if (outWc > srcWc / 3)
    failures.push(`total word count ${outWc} > source/3 (${Math.floor(srcWc / 3)})`);
}

// 6. 禁止元描述
const bad = /\b(summary|overview|in this section|in this chapter|in this episode)\b/i;
if (bad.test(content))
  failures.push(`forbidden meta-description term: ${content.match(bad)?.[0]}`);

if (failures.length) {
  console.log("VALIDATION FAILED:");
  failures.forEach((f) => console.log("  - " + f));
  process.exit(1);
}
console.log("VALIDATION PASSED");
process.exit(0);
```

`package.json` 加 script：

```json
{
  "scripts": {
    "validate-chapter-format": "tsx scripts/validate-chapter-format.ts"
  }
}
```

---

## Phase B — Durable files

### B1. 三个文件

按主文转换 2 的 OpenAI 官方命名：

```bash
cp docs/chapter-spec.md docs/Prompt.md  # 把 spec 作为 Prompt.md 的内容（或保留为引用关系）
touch docs/Plan.md docs/Implement.md
```

**`docs/Plan.md` seed**：

```markdown
# Plan: Chapter Splitter v0

## Direction
Take narration.md → produce video_1_script.md with [SLIDE N] markers,
满足 docs/Prompt.md (=chapter-spec.md) 全部 acceptance criteria。

## Milestones

### M1 — Identify chapter boundaries
Pass when: 找出 N 个 candidate boundaries (基于 heading / paragraph topic shift)
Validation: candidate count 在 [⌈article_words / 300⌉, ⌈article_words / 100⌉] 区间

### M2 — Enforce length constraints
Pass when: 每个 chapter word count 在 [100, 300]
Validation: `npm run validate-chapter-format -- --length-only`

### M3 — Shape into hook + 论点 + 例证
Pass when: 每个 chapter 第 1 句符合 hook 启发式
Validation: validator 检查 hook signal

### M4 — Insert [SLIDE N] markers
Pass when: 每个 chapter ≥ 1 个 [SLIDE N]
Validation: marker count check

### M5 — Final validation pass
Pass when: `npm run validate-chapter-format` exit 0 + 抽 3 个 chapter 人眼 review
Validation: full validator

## Known risks
- Article 太短 (< 6 chapters worth): spec 未覆盖，calibration 时遇到要补
- 含代码块: narration 里 inline code，chapter 切分要尊重边界
- 多语言混排: word count 计算需校准

## Open questions
- (留给 calibration 时发现的)
```

**`docs/Implement.md` seed**（agent 的操作 runbook + 实时 log）：

```markdown
# Implement: Chapter Splitter

## How this agent operates

Tools allowed: Read, Write, Edit, Bash (only for npm test/validate commands).
NOT allowed: editing files outside the Boundaries list in /goal.

Per-turn protocol:
1. Read docs/Prompt.md (FROZEN source of truth)
2. Read docs/Plan.md for current milestone
3. Read this file's "Attempt log" below — DO NOT repeat previous failed approaches
4. Execute the smallest meaningful change toward current milestone
5. Run validation, log result here in "Attempt log"
6. Update docs/Plan.md milestone status

## Stop conditions
- Emit <promise>COMPLETE</promise> when all M1-M5 milestones pass
- Stop after 20 turns total, write blocker to "Blocker log" below

## Attempt log

<!-- Agent appends. Format:

### Attempt N — <one-line title>
**Approach:** <what you tried>
**Result:** <pass/fail + which criteria>
**Conclusion:** <next step>

-->

## Scratchpad (chronological)

<!-- Agent appends turn-level thoughts here. Auditor reads this to spot drift. -->

## Blocker log

<!-- Only filled if agent stops due to blocker. -->
```

---

## Phase C — Hooks（这一步把"应该"变"不能违反"）

> 这是主文 Part 3 Layer 4 的具体落地。Spec 里写 `FROZEN` 是一句话，hook 是真正拦截。

### C1. PreToolUse hook：拦 FROZEN 文件

`scripts/guard-frozen.sh`：

```bash
#!/usr/bin/env bash
# Reads hook JSON context from stdin, checks file_path target.
# Exit 2 = block + feed message back to agent as feedback.

input=$(cat)
path=$(echo "$input" | jq -r '.tool_input.file_path // empty')

# FROZEN paths — agent absolutely must not touch
case "$path" in
  docs/Prompt.md|docs/chapter-spec.md)
    echo "BLOCKED: $path is FROZEN — to modify the spec, ask the human" >&2
    exit 2 ;;
  raw/*|docs/input/narration.md)
    echo "BLOCKED: $path is source data — agent may not modify" >&2
    exit 2 ;;
esac

# Out-of-scope paths (boundaries 里 do not change 的)
case "$path" in
  src/*|app/*|lib/*)
    echo "BLOCKED: $path is outside chapter-splitter boundaries" >&2
    exit 2 ;;
esac

exit 0
```

```bash
chmod +x scripts/guard-frozen.sh
```

### C2. PostToolUse hook：每次写完跑 validator

`scripts/run-validator.sh`：

```bash
#!/usr/bin/env bash
input=$(cat)
path=$(echo "$input" | jq -r '.tool_input.file_path // empty')

# Only validate when video_1_script.md was just written
if [[ "$path" == "docs/output/video_1_script.md" ]]; then
  if ! npm run validate-chapter-format >&2; then
    echo "Validator failed. Fix the issues above before continuing." >&2
    exit 2
  fi
fi
exit 0
```

### C3. `.claude/settings.json`（项目级，commit 到 repo）

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          { "type": "command", "command": "scripts/guard-frozen.sh" }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          { "type": "command", "command": "scripts/run-validator.sh" }
        ]
      }
    ]
  }
}
```

### C4. 验证 hook 生效

跑一个故意违反的 prompt 测试：

```
claude "请直接 edit docs/Prompt.md，把'30-60秒'改成'10-30秒'"
```

应该看到 hook block + stderr 反馈被喂回 agent。如果 hook 没生效，检查：
- `scripts/*.sh` 有执行权限
- `jq` 已安装（`brew install jq`）
- `.claude/settings.json` 没语法错

---

## Phase D — Calibrate（in-session `/goal`）

校准阶段你坐在电脑前，跑 in-session `/goal`，看 3-5 turn，发现问题就 tighten。

### D1. 写 strong goal 命令

```
/goal 给 docs/input/narration.md 生成 docs/output/video_1_script.md，
符合 docs/Prompt.md 的全部 acceptance criteria

Source of truth:
- read docs/Prompt.md (FROZEN — do not modify)
- read docs/input/narration.md
- follow docs/Plan.md
- update docs/Implement.md status block after each milestone
- append turn-level thinking to docs/Implement.md scratchpad
- READ docs/Implement.md Attempt log BEFORE each new attempt to avoid repeating failures

Acceptance criteria:
- 每个 chapter narration 在 30-60 秒（按 200 WPM 计算）
- 每个 chapter 三段结构：hook + 论点 + 例证
- 第一个 chapter 必须 8 秒内带出 thesis（即前 25 words 内）
- 最后一个 chapter 必须以 CTA 结尾
- 总 narration 时长 ≤ 原文 1/3
- negative case: 不出现 summary / overview / 元描述
- 每个 chapter 至少 1 个 [SLIDE N] marker
- chapter 之间禁止内容重复

Validation:
- npm run validate-chapter-format docs/output/video_1_script.md exits 0

Boundaries:
- only edit docs/output/video_1_script.md
- only edit docs/Plan.md, docs/Implement.md
- do not modify raw/* (anything)
- do not modify docs/input/narration.md
- do not modify docs/Prompt.md (FROZEN — hooks will block anyway)

Loop behavior:
- after each chapter generated, validator hook will auto-run; if blocked, fix and retry
- update docs/Plan.md milestone status
- emit <promise>COMPLETE</promise> when validator passes全部
- stop after 20 turns if blocked, write blocker reason to docs/Implement.md
```

### D2. 看头 5 turn，按下面表 act

| 看到 | 立刻做 |
|---|---|
| agent 反复在 Attempt log 试同一错误 | tighten Prompt.md spec：加 "READ Attempt log before each turn" |
| 跑了 5 turn 还在第一个 chapter 上磨 | spec 太严，先放宽 acceptance criteria，AFK 后再 tighten |
| validator pass 但 chapter 看着 still bad | spec 有 gap，validator 没 catch → 加 validation 规则到 validator |
| hook 拦 agent 改 chapter-spec.md | 这是 hook 正确工作的证据，不需要 fix |
| Scratchpad 显示 agent confused 关于 narration 输入格式 | spec 缺 input contract，补一段描述 narration 预期格式 |
| chapter 数远超预期（10+ 个） | spec 没限上限，加 "max chapter count" |

**完成校准的标志**：连续 3 个 turn 你不需要干预 → 进入 Phase E。

---

## Phase E — AFK Deploy（3 个 tier 各跑一次）

主文 Part 3 Layer 2 讲了三个 deployment tier。这一节让你各跑一遍，理解差异。

### E1. Tier 1 — `claude --bg`（local background supervisor）

最简单的 AFK 升级 —— 把 `/goal` 从 attached session 移到 background：

```bash
# 把完整 goal 文本存进文件
cat > /tmp/chapter-splitter-goal.txt <<'EOF'
[粘贴 D1 的完整 /goal 文本]
EOF

# Dispatch as background session
claude --bg "$(cat /tmp/chapter-splitter-goal.txt)"
# 输出大概：
#   Background session: bg_01HJKL...
#   View: claude attach bg_01HJKL... | claude logs bg_01HJKL... | claude stop bg_01HJKL...
```

**关键属性**（来自 [[claude-code-agent-view]]）：
- 关终端，session 继续（supervisor process 独立）
- 关 laptop，session 停（supervisor 在本地）
- Session 自动跑在 `.claude/worktrees/` 隔离 worktree
- 1 小时 idle 自动退进程；状态保留，下次 attach 重启

**监控**：

```bash
claude agents        # 打开 agent view TUI
# Space 在某 session 上 = peek 最新输出
# Enter = attach 接管
# ← 在 attached session 里 = 重新背景化
```

或命令行：

```bash
claude logs bg_01HJKL...    # 最近输出
claude attach bg_01HJKL...  # 接管
claude stop bg_01HJKL...    # 终止
```

**适用**：第一次真 AFK；你的笔记本会一直开着；不想搞云端。

### E2. Tier 2 — Cloud routine（Anthropic 云上跑，关 laptop 也继续）

> 需要 Pro / Max / Team / Enterprise plan + Claude Code on the web enabled（见 [[source-claude-code-routines-docs]]）。

#### 2a. 准备 repo

Cloud routine 从 GitHub clone 一份新的代码跑，所以**所有需要的东西必须 commit**：

```bash
git add docs/Prompt.md docs/Plan.md docs/Implement.md
git add docs/chapter-spec.md
git add scripts/validate-chapter-format.ts
git add scripts/guard-frozen.sh scripts/run-validator.sh
git add .claude/settings.json
git add package.json
git commit -m "chapter splitter: ready for cloud routine"
git push
```

确认装了 **Claude GitHub App** 在这个 repo 上（routines 需要 webhook 接入）。

#### 2b. 创建 routine

在 claude.ai/code 创建一个 routine（也可以用 `/schedule` skill，但 web 是最完整的入口）：

- **Repo**: blog2video
- **Prompt**: 粘贴 D1 的完整 `/goal` 文本（4000 字符上限）
- **Trigger** （选一个，3 选 1）：
  - **Schedule**: 每天 6am 跑 —— 给 backlog clearing scenario
  - **API**: 你自己的脚本检测到 `raw/` 出现新 narration → `curl -X POST .../fire` —— 给 event-driven
  - **GitHub**: PR opened with label `needs-chapters` → 触发 —— 给 PR-driven workflow

GitHub trigger filter 示例：

```yaml
event: pull_request
action: labeled
filter:
  - field: labels
    operator: contains
    value: needs-chapters
```

#### 2c. 监控 routine

每次 fire 创建一个新 session，在 claude.ai/code 可见。**注意 gotcha**（来自官方 docs）：

> Green status in run list = session started + exited without infrastructure error. Does NOT mean task succeeded.

所以一个 routine fire 之后必须看 transcript 和 `docs/Plan.md` milestone 状态。

#### 2d. 验证 hooks 在 cloud 跑

Cloud routine 是 **没有 permission prompt 的 autonomous mode** —— hook 是你唯一的 safety net。在 D2 校准后，确认：

- `scripts/guard-frozen.sh` 有执行权限（git mode 0755）
- `.claude/settings.json` 在 repo 里
- `jq` 在 routine 环境里可用（默认 trusted network 允许装 npm/apt 包 —— 如果你的 hook 脚本依赖额外二进制，在 routine config 加 setup step）

**适用**：常态 AFK；你不需要笔记本开着；产生预期 PR / commit 流。

### E3. Tier 3 — Channels（手机收 agent 问题）

> 需要 v2.1.80+ + plugin install。

#### 3a. 装 Telegram channel

通过 BotFather 拿到 bot token，然后：

```bash
# 在你 attached 的 session 里
/telegram:access pair
# 它会给你 pair code，你在 Telegram bot 里输入，approve
```

#### 3b. 启动带 channel 的 session

```bash
claude --channels plugin:telegram@claude-plugins-official --bg "$(cat /tmp/chapter-splitter-goal.txt)"
```

#### 3c. AFK 中 agent 卡住 → 你手机收到

如果 agent 在 turn 7 撞到一个 spec 没覆盖的边界 case（比如 narration 只有 200 字，根本切不出 5 chapter），它会 emit 一个 notification。Channel hook 把 notification 推到 Telegram，你回复 `yes <id>` 或文字指令，agent 继续。

**permission relay**（v2.1.81+）：如果声明了 `claude/channel/permission` 能力，agent 想做的危险操作（比如调 Bash）的 approval prompt 直接推到 Telegram。你在咖啡馆回 `yes 4521` 批准。

**安全提醒**：channel 必须 gate on **sender ID**（你的 Telegram user ID），不是 chat ID。群组里 gate on chat = 任何群员能注入指令到你的 agent。

**适用**：真正的 "I'm away from keyboard but in the loop"。

---

## 跑完之后审什么

| 检查项 | 怎么看 |
|---|---|
| Plan.md M1-M5 milestone 状态 | 直接看 |
| validator exit code | `git log` 找 hook 拦截记录 |
| boundaries 遵守 | `git diff --stat` 看改了哪些文件 |
| FROZEN 没被改 | `git log docs/Prompt.md` 应该没有 agent 的 commit |
| 重复失败 | Implement.md Attempt log 看是否同一错误反复 |
| 时间花在哪 | Implement.md Scratchpad 时间戳 |
| Hook 拦截次数 | grep `BLOCKED` 在 session log |
| Channel 互动次数 | Telegram 历史 |

---

## 复盘记录（跑完填这里 → 回填到主文 case study 区段）

> 这些数据让主文从"行业方法论综述"升级成"带真实案例的 PM 视角文章"。

**Spec 阶段**：
- [ ] Grill 用时（分钟）：
- [ ] Grill 总问题数：
- [ ] 你答 "agent 你建议" 的占比：
- [ ] 最终 chapter-spec.md 行数：
- [ ] Validator 脚本写了多久：

**Hook 阶段**：
- [ ] Hook 配置 + 测试用时：
- [ ] 测试 prompt 让 hook 拦截，是否第一次就成功：
- [ ] PreToolUse hook 在校准 + AFK 阶段总共拦了几次：
- [ ] PostToolUse validator hook 在 AFK 阶段拦了几次：

**Calibration 阶段（in-session `/goal`）**：
- [ ] 干预了几次：
- [ ] 每次干预修了 spec 哪一条（按时间列）：
  1.
  2.
  3.
- [ ] Calibration 总耗时：
- [ ] 第几个 turn 之后开始连续 3 turn 不需干预：

**AFK Tier 1（`claude --bg`）**：
- [ ] 总 turn 数：
- [ ] 失败 attempt 数：
- [ ] 成功 attempt 数：
- [ ] Wall clock 时间：
- [ ] 最终 validation 是否 pass：

**AFK Tier 2（cloud routine）**（如果跑了）：
- [ ] Trigger 选了哪种：
- [ ] 第一次 fire 是否成功：
- [ ] "green status" 跟实际任务成功是否吻合：
- [ ] Routine 跑通后第二次自动 fire 表现：

**AFK Tier 3（Telegram channel）**（如果跑了）：
- [ ] AFK 中 channel 推了几次问题：
- [ ] 手机响应延迟（你看到 → 回复）：
- [ ] Permission relay 实际批准了什么操作：

**ROI 数据**：
- [ ] 这次（spec + hook + validator + AFK）总时间：
- [ ] 以前手做一次 chapter splitting 大概多久：
- [ ] 第二次跑（用同一 spec，不同 narration）需要多久：
- [ ] 第二次时 hook + validator + spec 还有效吗 / 需要改吗：

**Spec evolution 数据**：
- [ ] Grill 阶段没想到、calibration 才补的 acceptance criteria：
  -
  -
  -
- [ ] AFK 阶段被 Attempt log 暴露的 spec 漏洞：
  -

**意外发现**：
- [ ] 哪些预期之外的事情发生了：
  -

---

## 来源

- 主文：[[pm-long-horizon-methodology|drafts/pm-long-horizon-methodology.md]]
- 官方 docs：[[claude-code-goal]], [[source-openai-codex-cookbook-trilogy]], [[source-openai-codex-use-case-follow-goals]], [[source-openai-long-horizon-tasks-codex]], [[source-claude-code-routines-docs]], [[source-claude-code-hooks-docs]], [[source-claude-code-channels-docs]], [[claude-code-agent-view]], [[source-claude-code-programmatic-usage-docs]]
- 社区材料：[[idea-to-afk-agent-flow]], [[grill-with-docs]], [[sandcastle]]
- 项目背景：[[blog2video]]
