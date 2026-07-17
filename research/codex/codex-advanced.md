# Codex 进阶实战:当自主 agent 平台压榨

> Codex 常青报告 · 进阶篇 · 最后更新 2026-07-17
> 定位:你**已经了解 Codex 有哪些功能**(不了解先看《一文了解 Codex》`codex-overview.md`),现在要把它从"助手"升级成**能并行、能无人值守、能跑几十小时**的自主 agent 平台。
> 官方文档:`learn.chatgpt.com/docs/*`。

**一句话:** Codex 进阶的分水岭不是"更会写代码",而是**把它当自主 agent 平台压榨**——而这套能力的开关,全在几十行 TOML 和几个 markdown 文件里。

---

## 1. 心智模型:一条自主 agent 流水线

进阶用法不是孤立功能,是一条流水线:

```
subagents(并行拆活) → Scheduled tasks + approval_policy=never(无人值守)
        → Codex Cloud(后台跑) → Codex Remote(手机远程盯)
                → 长时任务四文件法(几十小时不跑偏)
```

配置层是杠杆:hooks 把"不要动"变"动不了",`[agents]` 旋钮控并行度,`approval_policy` 决定放手程度。**几十行 TOML > 换个更强的模型。**

---

## 2. Subagents:并行深配

**开关(默认已开):** `[features] multi_agent = true`,**没有单独的 `subagents` flag**。暴露的多智能体工具:`spawn_agent` / `send_input` / `resume_agent` / `wait_agent` / `close_agent`。

**旋钮 + 确切默认值:**

```toml
[features]
multi_agent = true          # stable, 默认开

[agents]
max_threads = 6             # 默认 6:同时最多几个子 agent
max_depth = 1               # 默认 1:root=depth 0,允许一层子 agent
job_max_runtime_seconds = 1800
interrupt_message = true
```

**三个内置 agent:** `default`(通用兜底)、`worker`(执行/实现/修复)、`explorer`(只读代码探索)。

**自定义 agent** —— 每个一个 TOML 文件,放 `~/.codex/agents/`(个人)或 `.codex/agents/`(项目):

```toml
name = "reviewer"
description = "PR reviewer focused on correctness, security, and missing tests."
developer_instructions = """
Review code like an owner.
Prioritize correctness, security, behavior regressions, and missing test coverage.
"""
nickname_candidates = ["Atlas", "Delta", "Echo"]
# 可选继承键: model, model_reasoning_effort, sandbox_mode, mcp_servers, skills.config
```

**批处理原语 `spawn_agents_on_csv`(experimental):** 读 CSV → 每行 spawn 一个 worker → 全批等待 → 结果导出 CSV。每个 worker **必须调一次** `report_agent_job_result`(否则该行 `status: error`)。提示里这样触发:

```text
Then call spawn_agents_on_csv with:
- csv_path: /tmp/components.csv
- id_column: path
- instruction: "Review {path} owned by {owner}. Return JSON with keys path, risk, summary, follow_up via report_agent_job_result."
- output_csv_path: /tmp/components-review.csv
```
[官方 · subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents)

**模型分工:** 难活用 `gpt-5.6`(默认 sol),并行 worker/杂活用 `gpt-5.6-terra` 或 `gpt-5.4-mini`。

---

## 3. 无人值守:Scheduled tasks + approval_policy=never + worktree

三件套让 Codex 无人值守跑:

**① Scheduled tasks(定时,原 Automations):** 两型——standalone(每次起新 chat,可跨多 project)/ chat 内(复用上下文,支持**分钟级**主动跟进循环)。

**② 全自动权限档:**

```toml
approval_policy = "never"          # untrusted | on-request | never
sandbox_mode = "workspace-write"   # read-only | workspace-write | danger-full-access
```
CLI 等价:`codex -a never -s workspace-write exec "…prompt…"`
> Scheduled tasks 在组织策略允许时自动用 `approval_policy = "never"`;被 `requirements.toml` 禁止时回退到所选权限模式。

**③ worktree 隔离:** Git 仓库里可选 scheduled task 跑在 local project 还是新 **worktree**(把定时任务的改动与你手头未完成的工作隔离)。需保持机器开机 + 桌面 App 运行。

> [!warning] 调度是 RRULE 不是 cron
> App 内用 **RRULE(RFC 5545)**,例 `RRULE:FREQ=WEEKLY;BYDAY=MO;BYHOUR=9`。**cron 只在 CLI headless 路径**(`codex exec` 适合被你自己的 cron / GitHub Actions 调度)。UI 里填不了 cron 表达式。

> [!note] 别当官方术语写
> "heartbeat automations" / "Triage automations" 是坊间/GitHub issue 词,**不是官方分类**——官方只有一个 "Scheduled" 收件箱视图。[官方 · scheduled tasks](https://learn.chatgpt.com/docs/automations)

---

## 4. 后台与远程:Cloud + Remote

**Codex Cloud —— 后台跑长任务:**
- 云面 `chatgpt.com/codex`;环境配置 `chatgpt.com/codex/settings/environments`。
- **容器缓存最长 12 小时**(改 setup/maintenance script、env、secrets 会失效);默认镜像 `universal`(`openai/codex-universal`)。
- **网络分离:** setup 阶段有网、**agent 阶段默认无网**(可开);**secrets 只给 setup,agent 阶段前移除**,env vars 全程保留——这是安全边界的关键。
- **`@codex` GitHub:** `@codex review`(👀 + 行内发现 + PR 级总结)、`@codex review for security regressions`(一次性聚焦)、`@codex fix the P1 issue`(评审后修复,起云 chat)。评审规则用最近的 `AGENTS.md` 定制;设置里有 "Automatic reviews" 开关。[官方 · cloud](https://learn.chatgpt.com/docs/cloud) · [github](https://learn.chatgpt.com/docs/third-party/github)

**Codex Remote —— 手机盯长任务(2026-06-25 GA):**
- 手机是**控制面,不是第二个 Codex**:主机提供环境,手机发 prompt/审批/后续。
- **二维码配对**(桌面 App 生 QR,扫码进 ChatGPT,认证一对一,绑当前登录会话);**secure relay 不把主机暴露公网**。
- 随 GA 附 DigitalOcean 插件(`@DigitalOcean` 起 Droplet 当主机)。[官方 · remote](https://learn.chatgpt.com/docs/remote-connections)

**Worktree 并行(桌面 App):**
- **不是自动 per-thread**:新建 chat 时**手动选 "Worktree" / "Local"**;每个托管 worktree 通常专属一个 chat,resume 回同一 worktree。
- **"Hand off"** 在 Local(前台)↔ Worktree(后台)间移动 chat = 官方并行范式("排队后台工作,同时前台专注")。
- worktree root 默认 `$CODEX_HOME/worktrees`,自动清理保留**最近 15 个**(Settings > Worktrees 的设置,**config.toml 无专门 worktree 键**)。`projects.<path>.trust_level` 可标 trusted/untrusted。[官方 · worktrees](https://learn.chatgpt.com/docs/environments/git-worktrees)

---

## 5. 长时任务:让它跑几十小时不跑偏

两套官方方法,核心都是**用稳定的 markdown 文件当 agent 的持久记忆,冻结"做完的定义"**,防 scope drift。

### 四文件法(官方博客,Derrick Choi 2026-02-23)
| 文件 | 作用 |
|---|---|
| **`Prompt.md`** | 冻结目标:Goals / 非目标 / 硬约束 / 交付物 / "Done when…" |
| **`Plan.md`** | 里程碑(每个可单循环完成)+ 每里程碑的验证命令 + "Stop-and-fix rule" |
| **`Implement.md`** | 执行手册,声明 "Plans markdown file is source of truth" |
| **`Documentation.md`** | 状态 + 审计日志 |

**"Freeze the target"** = 别让 agent "造出 impressive but wrong 的东西"。硬指标:**~25 小时不间断 / ~13M tokens / ~30k 行代码**。
> 该博客用 **`/plan`** 命令,是**提示工程纪律,不是配置菜谱**(不含 approval/cron)。[官方博客](https://developers.openai.com/blog/run-long-horizon-tasks-with-codex)

### PLANS.md / ExecPlan(官方 Cookbook,Aaron Friel 2025-10-07)
把任务写成自包含的"活文档"ExecPlan,与 **AGENTS.md 配合**(AGENTS.md 放触发短语)。四个必需活文档小节:**Progress · Surprises & Discoveries · Decision Log · Outcomes & Retrospective**。实证单条 prompt 工作 **7+ 小时**。[官方 · cookbook](https://developers.openai.com/cookbook/articles/codex_exec_plans)

---

## 6. `/goal` loop 方法论:自我验证的闭环

`/goal` 是真官方 CLI slash 命令("Set, edit, pause, resume, view, or clear a task goal";`/plan` 亦真)。[官方 · commands](https://learn.chatgpt.com/docs/developer-commands?surface=cli)

配套的官方 Cookbook 三部曲(方法论一手):
1. **Using Goals in Codex**(Raj Pathak & Stefano Fabbri, 2026-05-09)—— `/goal` = "completion contract":work→check→continue,需证据才算完成。
2. **Build Iterative Repair Loops**(Shreekant Agrawal, 2026-05-11)—— Review→Repair→Validate,`repair_until_done()` 带停止条件(默认 max 3 轮),审计 `record.json`。
3. **Build an Agent Improvement Loop**(Wesley Pasfield, 2026-05-12)—— 5 段飞轮 Traces→Feedback→Evals→Validation→Harness Changes,产出交接制品 `codex_handoff.md`。

> vault 已把这套方法论啃穿(`/goal` + 三层嵌套 loop、Chris Hayduk 三招)——本篇只做落地指路,细节见 vault 方法论页。

---

## 7. Prompting:GPT-5.6 上的提示纪律

- **精简 prompt 反而提分:** 官方 GPT-5.6 指南——精简提示提分 **10–15%** 且省 **41–66% token**;从 medium reasoning 起步,难任务再上 `reasoning.mode:"pro"`。[官方 · prompting](https://developers.openai.com/api/docs/guides/prompt-guidance-gpt-5p6)
- **别在 prompt 里预告 "plan/status"**(易早停);preamble 用 `phase` 参数;AGENTS.md 的注入顺序会影响效果。[官方 cookbook · codex prompting](https://developers.openai.com/cookbook/examples/gpt-5/codex_prompting_guide)

---

## 8. 可复制语法金料(直接搬 · 每块标 ✅ 官方 / ⚠️ 存疑)

### ① MCP —— `[mcp_servers.<name>]` 表
stdio 服务器 ✅:
```toml
[mcp_servers.context7]
command = "npx"
args = ["-y", "@upstash/context7-mcp"]
env_vars = ["LOCAL_TOKEN"]
startup_timeout_sec = 10          # 默认 10
tool_timeout_sec = 60             # 默认 60

[mcp_servers.context7.env]
MY_ENV_VAR = "MY_ENV_VALUE"
```
streamable HTTP / 远程 ✅:
```toml
[mcp_servers.figma]
url = "https://mcp.figma.com/mcp"
bearer_token_env_var = "FIGMA_OAUTH_TOKEN"
auth = "oauth"

[mcp_servers.figma.http_headers]
"X-Figma-Region" = "us-east-1"
```
CLI ✅:`codex mcp add context7 -- npx -y @upstash/context7-mcp`
> `~/.codex/config.toml`(项目 `.codex/config.toml` 覆盖);`command`↔stdio、`url`↔HTTP 互斥。[官方](https://learn.chatgpt.com/docs/extend/mcp?surface=cli)

### ② Hooks —— config.toml(个人)
```toml
[[hooks.PreToolUse]]
matcher = "^Bash$"

[[hooks.PreToolUse.hooks]]
type = "command"
command = '/usr/bin/python3 "$(git rev-parse --show-toplevel)/.codex/hooks/pre_tool_use_policy.py"'
timeout = 30
statusMessage = "Checking Bash command"
```
Hooks —— requirements.toml(企业托管)✅:
```toml
allow_managed_hooks_only = true

[features]
hooks = true

[hooks]
managed_dir = "/enterprise/hooks"
windows_managed_dir = 'C:\enterprise\hooks'

[[hooks.PreToolUse]]
matcher = "^Bash$"

[[hooks.PreToolUse.hooks]]
type = "command"
command = "python3 /enterprise/hooks/pre_tool_use_policy.py"
timeout = 30
```
> **10 个生命周期事件**:turn 级 8 个(`PreToolUse`/`PermissionRequest`/`PostToolUse`/`PreCompact`/`PostCompact`/`UserPromptSubmit`/`SubagentStop`/`Stop`)+ 启动级 2 个(`SessionStart`/`SubagentStart`)。**阻断 = handler `exit 2` + 原因写 stderr。**[官方](https://learn.chatgpt.com/docs/hooks)
> ⚠️ 官方 hooks 页未标 GA 日期;第三方称 GA=2026-05-14 / engine 稳定于 v0.124.0(2026-04-23)——第三方,官方未逐字确认。

### ③ Skills —— SKILL.md frontmatter
```markdown
---
name: pdf-processing
description: Extract PDF text, fill forms, merge files. Use when handling PDFs.
license: Apache-2.0
metadata:
  author: example-org
  version: "1.0"
allowed-tools: Bash(git:*) Bash(jq:*) Read   # Experimental
---
```
> 发现清单预算 = 上下文 2%(未知时 8,000 字符);单个 skill 正文建议 < 5000 tokens / SKILL.md < 500 行。关掉隐式调用(仍可 `$skill` 显式调):skill 内 `agents/openai.yaml` 写 `policy: { allow_implicit_invocation: false }`。[官方](https://learn.chatgpt.com/docs/build-skills) · [标准](https://agentskills.io/specification)

> ⚠️ **别抄**:第三方博客里出现的 `[goals] max_turns / check_model="o4-mini" / timeout_minutes` 块**官方无法证实**(`o4-mini` 对 2026 可疑),勿作事实源。

---

## 9. 进阶避坑清单

1. MCP 用 `[mcp_servers.<name>]` 表(不是 `[mcp]`);能 `codex mcp add` 就别手写。
2. 并行先 `[features] multi_agent = true`(默认开)+ 控 `max_threads`/`max_depth`;批处理走 `spawn_agents_on_csv`(记得每 worker 回 `report_agent_job_result`)。
3. 无人值守 = Scheduled task + `approval_policy="never"` + 跑在 worktree;App 内 **RRULE** 不是 cron,headless 用 `codex exec`。
4. 长时任务用四文件法/ExecPlan **冻结目标**;它用 `/plan`,别跟 `/goal` 混。
5. 模型分工:难活 `gpt-5.6`、并行 worker `gpt-5.6-terra`/`gpt-5.4-mini`;prompt 精简省 41–66% token。
6. worktree 是**手动选 + Hand off**,不是自动 per-thread;CLI 无原生 `--worktree` flag(第三方说法)。
7. 数字/术语发稿/配置前重核 `learn.chatgpt.com/docs/{models,changelog}`——漂移极快。

---

## 更新记录

| 日期 | 变更 | 官方来源 |
|---|---|---|
| 2026-07-17 | **初版**:由角度「Codex 进阶实战:当自主 agent 平台压榨」成篇,合并旧+新调研并校准当前状态——subagents `[agents]` 默认值、MCP `[mcp_servers]` 逐字、hooks 10 事件、Scheduled tasks(RRULE/approval=never)、Cloud 12h 缓存+网络分离、Remote GA(06-25)、长时任务四文件法(博客,非 cookbook)、`/goal` 三部曲真实标题 | learn.chatgpt.com/docs/{agent-configuration/subagents,extend/mcp,hooks,automations,cloud,remote-connections,environments/git-worktrees} · developers.openai.com/{blog,cookbook} |
