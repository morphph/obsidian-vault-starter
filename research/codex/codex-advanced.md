# 压榨 Codex：把它变成能无人值守跑几十小时的 agent 平台

> 版本日期：2026-07-17 · Codex 常青报告 · 进阶篇
> 适用对象：你**已经了解 Codex 有哪些功能**（不了解先看《[上手 Codex](codex-overview.md)》概览篇），现在要把它从「助手」升级成能并行、能无人值守、能在 VPS/Telegram/CI 上跑几十小时的自主 agent 平台。你会读 TOML、会写点 shell/Python、有一台能常开的机器。
> 信息基础：以 OpenAI 官方 `learn.chatgpt.com/docs/*` 与 `developers.openai.com/{blog,cookbook}` 为准。核验细节、确切默认值出处见同目录 `facts.md`。

**一句话：** Codex 进阶的分水岭不是「更会写代码」，而是**把它当自主 agent 平台压榨**——而这套能力的开关，几乎全在几十行 TOML、几个 markdown 文件和一层任务持久化里。几十行 TOML 的杠杆，大于换一个更强的模型。

---

## 1. 心智模型：一条自主 agent 流水线

进阶用法不是一堆孤立功能，而是一条从「并行拆活」到「无人值守长跑」的流水线。每一环都由配置层撬动：hooks 把「不要动」变成「动不了」，`[agents]` 旋钮控并行度，`approval_policy` 决定放手到什么程度。

```
subagents（并行拆活）
   → Scheduled tasks + approval_policy=never（无人值守触发）
      → Codex Cloud / codex exec（后台执行）
         → Codex Remote（手机远程盯梢与审批）
            → 长时任务四文件法 / ExecPlan（几十小时不跑偏）
```

真正决定这条流水线可靠不可靠的，是它背后的**持久层**。「让 Codex 长时间运行」不是让一个 terminal session 永不退出，而是保证目标、任务状态、session ID、Git 状态、验证结果、待审批动作、预算这些东西在断线、重启、失败后仍然存在。所以可靠架构的持久层应该是「任务数据库 + Codex session + Git commit/worktree + 日志」，而不是「一条 SSH 连接 + 一个永不结束的 tmux 窗口」。tmux 仍然有用，但不该是唯一的任务状态来源。

## 2. Subagents：并行深配

并行能力默认已开（`[features] multi_agent = true`，没有单独的 `subagents` flag），对外暴露 `spawn_agent` / `send_input` / `resume_agent` / `wait_agent` / `close_agent` 几个工具。你真正要调的是并行度和分工。

**旋钮 + 确切默认值：**

```toml
[features]
multi_agent = true          # stable，默认开

[agents]
max_threads = 6             # 默认 6：同时最多几个子 agent
max_depth = 1               # 默认 1：root=depth 0，只允许一层子 agent
job_max_runtime_seconds = 1800
interrupt_message = true
```

三个内置 agent 各有分工：`default`（通用兜底）、`worker`（执行/实现/修复）、`explorer`（只读代码探索）。要自定义角色，每个写一个 TOML 文件放 `~/.codex/agents/`（个人）或 `.codex/agents/`（项目）：

```toml
name = "reviewer"
description = "PR reviewer focused on correctness, security, and missing tests."
developer_instructions = """
Review code like an owner.
Prioritize correctness, security, behavior regressions, and missing test coverage.
"""
nickname_candidates = ["Atlas", "Delta", "Echo"]
# 可选继承键：model, model_reasoning_effort, sandbox_mode, mcp_servers, skills.config
```

要批量处理一批文件，用实验原语 `spawn_agents_on_csv`：读 CSV → 每行 spawn 一个 worker → 全批等待 → 结果导出 CSV。

> [!warning] 每个 worker 必须回报结果，否则那一行算失败
> 用 `spawn_agents_on_csv` 时，每个 worker **必须调一次 `report_agent_job_result`**——漏掉的那一行会被标成 `status: error`。在触发指令里就写清楚要它返回什么（如「Return JSON with keys path, risk, summary via report_agent_job_result」）。

**处方：** 优先把只读、独立的探索/审查交给 subagents，写入型并行任务各自用独立 worktree。模型按难度分工——难活用 `gpt-5.6`，并行 worker 和杂活用 `gpt-5.6-terra` 或 `gpt-5.4-mini`，别用高成本模型跑无聊批量活。单个 job 的 subagent 数建议压在 2–3 个，因为每个都额外吃 token、进程和工具调用。

## 3. 无人值守：Scheduled tasks + approval=never + worktree

让 Codex 无人值守跑，是三件套配合：**定时触发 + 全自动权限档 + worktree 隔离**。

**① Scheduled tasks（定时）：** 两型——standalone（每次起新 chat，可跨多 project）和 chat 内（复用上下文，支持分钟级主动跟进循环）。

**② 全自动权限档：**

```toml
approval_policy = "never"          # untrusted | on-request | never
sandbox_mode = "workspace-write"   # read-only | workspace-write | danger-full-access
```

CLI 等价写法是 `codex -a never -s workspace-write exec "…prompt…"`。Scheduled task 在组织策略允许时会自动用 `approval_policy = "never"`；被 `requirements.toml` 禁止时回退到你所选的权限模式。

**③ worktree 隔离：** Git 仓库里可选让 scheduled task 跑在 local project 还是新 worktree，把定时任务的改动和你手头未完成的工作隔开。前提是机器保持开机、桌面 App 运行。

> [!warning] App 内调度是 RRULE，不是 cron
> 桌面 App 用 **RRULE（RFC 5545）**，例如 `RRULE:FREQ=WEEKLY;BYDAY=MO;BYHOUR=9`；UI 里填不了 cron 表达式。**cron 只在 CLI headless 路径**——要用 cron，走 `codex exec` 接你自己的 crontab 或 GitHub Actions。

> [!warning] `approval=never` 不等于安全
> 完全无交互只意味着遇到审批时不问你，不意味着动作本身安全。安全来自别处：sandbox、只允许固定仓库、独立 Linux 用户权限、secrets 隔离、command Rules、Hook 检查、worktree、网络策略、任务预算和停止条件。把 `never` 当成「我已经用其他层兜住了风险」的结果，而不是起点。

## 4. 后台与远程：Cloud + Remote + Worktree

**Codex Cloud** 在 `chatgpt.com/codex` 对 GitHub repo 跑后台长任务，环境在 `chatgpt.com/codex/settings/environments` 配。它有两个你必须知道的边界：容器缓存最长 12 小时（改 setup/maintenance script、env 或 secrets 都会让它失效）；**网络是分离的**——setup 阶段有网、agent 阶段默认无网（可开），而且 secrets 只发给 setup 阶段、进入 agent 阶段前会被移除，只有 env vars 全程保留。这层网络+secrets 分离是云端最关键的安全边界。GitHub 上直接用 `@codex review`（拿 👀 + 行内发现 + PR 级总结）、`@codex fix the P1 issue`（评审后起云 chat 去修），评审规则读最近的 `AGENTS.md`。

**Codex Remote**（2026-06-25 GA）让手机成为控制面：主机提供环境，手机只发 prompt、审批、后续。配对走二维码——桌面 App 生成 QR，手机 ChatGPT 扫码，认证一对一绑当前登录会话，secure relay 不把主机暴露公网。它的硬限制是配对主机必须在线，睡眠/断网/关 App 就中断，所以它适合「偶尔盯一眼、随手批一下」，不适合当 24/7 服务的骨架。

**Worktree 并行（桌面 App）** 是官方的前后台并行范式，但**不是自动 per-thread**：

| 想做的事 | 怎么做 |
|---|---|
| 新任务与手头工作隔离 | 新建 chat 时手动选 "Worktree"（不选就是 Local） |
| 前台专注 + 后台排队 | 用 "Hand off" 在 Local ↔ Worktree 间移动 chat |
| resume 一个后台任务 | 回到它专属的 worktree（每个托管 worktree 通常专属一个 chat） |

worktree root 默认在 `$CODEX_HOME/worktrees`，自动清理保留最近 15 个（在 Settings > Worktrees 调，`config.toml` 没有专门的 worktree 键）。

## 5. codex exec + 任务持久层：无人值守的骨架

`codex exec` 是非交互式 Codex，是脚本、CI、VPS 后台任务的入口。核心 flags：

```bash
codex exec "分析当前仓库，列出五个最高风险问题，不修改文件"   # 默认只读
codex exec --sandbox workspace-write "修复当前测试失败，运行相关测试并审查最终 diff"
codex exec --json --sandbox workspace-write "实施 issue #248 并运行测试"   # JSONL 事件流
codex exec -o /var/lib/codex-runner/jobs/1001/final.md "生成发布说明"       # 存最终消息
codex exec resume <SESSION_ID> "继续处理，但不要修改数据库 schema"          # 按 ID 恢复
```

`--json` 输出的 JSONL 事件包括 `thread.started`、`turn.started` / `turn.completed` / `turn.failed`、`item.started` / `item.completed`（agent 消息、命令执行、文件改动、MCP 调用等）、`error`。worker 应该逐行解析这些事件、实时更新状态，而不是等进程结束一次读完。同时保存完整 JSONL（审计用）和 `-o` 的 final message（给用户看摘要用）。

> [!tip] 生产别依赖 `--last`，存准确的 SESSION_ID
> `codex exec resume --last` 方便交互，但生产系统里多个任务会互相顶掉「最后一个 session」。把每个 job 的 SESSION_ID 落库，恢复时点名 resume。

要把这些拼成一个可恢复的系统，你需要一张任务表和一个状态机。最小 schema：

```text
jobs
├── id                ├── goal              ├── worktree_path
├── channel           ├── constraints       ├── codex_thread_id
├── requester_id      ├── verification      ├── status
├── repository_id     ├── base_branch       ├── retry_count
├── task_branch       ├── created_at        ├── credit_budget
├── timeout_at        ├── last_event        └── final_commit_sha
```

状态机不要只有 `running` 和 `done`——用户必须能区分正在执行、等待批准、测试中、失败、超时、已取消：

```text
queued → preparing → running → waiting_for_approval → validating → review_ready → completed
任意阶段 → failed / cancelled / timed_out
```

## 6. 何时从 shell wrapper 升级到 SDK / App Server

`codex exec` 够用很久。但当下面的需求同时出现两个以上，就该升级：保存并恢复准确 thread、多轮 follow-up、取消运行中的 task、处理 structured events、自定义审批、并发多任务、每任务选不同模型/sandbox、把结果展示在 dashboard、把 thread 关联到 Git commit 和业务工单。

| 需求 | 用什么 |
|---|---|
| 手机偶尔启动、查看、批准 | 官方 Remote |
| 已有 Telegram/CI，先快速试验 | `codex exec --json` |
| 稳定的多任务、恢复、审批、并发 | **Codex SDK**（TS Node 18+ / Python 3.10+，含 `AsyncCodex`） |
| 接近官方客户端的完整体验 | **App Server**（auth / history / approvals / streamed events） |
| Codex 只是更大业务编排里的 coding specialist | **`codex mcp-server` + OpenAI Agents SDK**（handoff / traces） |
| CI 里分析/修复失败检查、受控 review | **GitHub Action**（`openai/codex-action@v1`） |

> [!warning] 远程暴露 App Server 要上 TLS + 认证
> 明文 `ws://` 只能用于 localhost 或 SSH 端口转发。远程部署必须用安全 transport、认证和网络边界，别直接公开一个无认证的 WebSocket。GitHub Action 同理：`allow-users`/`allow-bots` 限制触发者、sanitize PR/commit/issue 文本防 prompt injection、用 `safety-strategy`（`drop-sudo`/`unprivileged-user`）——绝不让不受信任的 issue/PR 文本驱动一个高权限 agent。

## 7. 长时任务：让它跑几十小时不跑偏

两套官方方法，核心都是**用稳定的 markdown 文件当 agent 的持久记忆、冻结「做完的定义」**，防 scope drift。

**四文件法**（官方博客，Derrick Choi，2026-02-23）把长任务拆成四份文档：

| 文件 | 作用 |
|---|---|
| `Prompt.md` | 冻结目标：Goals / 非目标 / 硬约束 / 交付物 / "Done when…" |
| `Plan.md` | 里程碑（每个可单循环完成）+ 每里程碑的验证命令 + Stop-and-fix rule |
| `Implement.md` | 执行手册，声明 "Plans markdown file is source of truth" |
| `Documentation.md` | 状态 + 审计日志 |

它的关键词是 "Freeze the target"——别让 agent 造出「impressive but wrong」的东西。这套方法实证跑到过约 25 小时不间断 / 约 13M tokens / 约 30k 行代码。

**PLANS.md / ExecPlan**（官方 Cookbook，Aaron Friel，2025-10-07）把任务写成自包含的「活文档」，与 `AGENTS.md` 配合（AGENTS.md 放触发短语），要求四个必需小节：Progress、Surprises & Discoveries、Decision Log、Outcomes & Retrospective。实证单条 prompt 工作 7+ 小时。

> [!tip] 四文件法用 `/plan`，别跟 `/goal` 混
> 四文件法那篇博客用的是 `/plan` 命令，是提示工程纪律、不是配置菜谱（不含 approval/cron 设置）。它和下一节的 `/goal` loop 是两套东西，别把两者的命令和参数搅在一起。

## 8. `/goal` loop：自我验证的闭环

`/goal` 和 `/plan` 都是真官方 CLI slash 命令（`/goal` = "Set, edit, pause, resume, view, or clear a task goal"）。`/goal` 的精髓是把目标当成一份 **completion contract**：work → check → continue，没有证据就不算完成，遇到超出当前 sandbox 或 approval policy 的动作仍会暂停。

官方 Cookbook 有一组三部曲讲这套方法论：**Using Goals in Codex**（把 `/goal` 当完成契约）、**Build Iterative Repair Loops**（Review→Repair→Validate，`repair_until_done()` 带停止条件、默认 max 3 轮）、**Build an Agent Improvement Loop**（Traces→Feedback→Evals→Validation→Harness Changes 五段飞轮）。vault 已经把这套方法论啃穿（`/goal` + 三层嵌套 loop、Chris Hayduk 三招），本篇只做落地指路。

> [!warning] 别抄第三方博客里的 `[goals]` 配置块
> 网上流传的 `[goals] max_turns / check_model="o4-mini" / timeout_minutes` 块官方无法证实（`o4-mini` 对 2026 也可疑），别当事实源写进你的 config。停止条件应该写在 prompt 的 Stop conditions 段里，而不是这些来路不明的键里。

## 9. Prompting：GPT-5.6 上的提示纪律

反直觉但已被官方量化：**精简 prompt 反而提分**——官方 GPT-5.6 指南显示精简提示提分 10–15% 且省 41–66% token。从 medium reasoning 起步，难任务再上 `reasoning.mode:"pro"`。另外别在 prompt 里预告「我会先给 plan/status」，这容易触发早停；preamble 用 `phase` 参数表达，而 `AGENTS.md` 的注入顺序也会影响效果。

**处方：** 无人值守 prompt 必须比交互 prompt 更明确——它没人临场补话。判断规则：一条无人值守 prompt 至少要写清 Outcome、Repository state、Constraints、Verification、Stop conditions、Final response 六段（完整模板见 §14）。

## 10. Rules + Hooks：机械边界与生命周期拦截

`AGENTS.md` 告诉 agent「应该怎么做」，Rules 和 Hooks 让某些边界**动不了**。

**Rules** 管命令级权限，用 `prefix_rule()` 声明 allow/prompt/forbidden。它用 Starlark（类 Python 的沙箱语言）写，存在 `rules/` 下的 `.rules` 文件里：

```python
prefix_rule(
    pattern = ["git", "push"],
    decision = "prompt",           # allow / prompt / forbidden
    justification = "Confirm target branch before pushing",
)
```

**Hooks** 在 10 个生命周期事件上跑脚本——turn 级 8 个（`PreToolUse` / `PermissionRequest` / `PostToolUse` / `PreCompact` / `PostCompact` / `UserPromptSubmit` / `SubagentStop` / `Stop`）加启动级 2 个（`SessionStart` / `SubagentStart`）。阻断的方式是 handler `exit 2` 并把原因写进 stderr。个人配置写在 `config.toml`：

```toml
[[hooks.PreToolUse]]
matcher = "^Bash$"

[[hooks.PreToolUse.hooks]]
type = "command"
command = '/usr/bin/python3 "$(git rev-parse --show-toplevel)/.codex/hooks/pre_tool_use_policy.py"'
timeout = 30
statusMessage = "Checking Bash command"
```

企业用 `requirements.toml` 托管（`allow_managed_hooks_only = true` + `[hooks] managed_dir = "/enterprise/hooks"`）。在无人值守系统里，Hooks 的典型分工是：`SessionStart` 加载 job 元数据、`UserPromptSubmit` 扫 secrets、`PreToolUse` 拦危险命令、`PostToolUse` 写审计、`Stop` 检查测试和 final summary。

> [!warning] 无人值守部署要显式验证 Hook trust
> 项目 Hook 只在可信项目加载，改动后 hash 变会重新触发审查。无人值守发布流程里必须显式检查 Hook 的 trust 状态——别等第一条生产任务跑起来才发现 Hook 被静默跳过了。高风险 Hook 应 fail closed，不是静默放行。

## 11. 审批模型：按风险分级放手

把动作按风险分级，然后给每级配一个默认处置——这比「全部自动」或「全部手动」都可靠：

| 风险 | 示例 | 建议处置 |
|---|---|---|
| 低 | 读代码、搜索、跑只读测试 | 自动允许 |
| 中 | 改 worktree、装已锁定依赖、本地 commit | 预授权或策略允许 |
| 高 | push、开/改 PR、调有副作用的 MCP | 人工审批（如 Telegram） |
| 极高 | deploy、生产数据库、删资源、发布 package | 二次确认或直接禁止 |

审批消息要带上足够上下文，approval ID 必须一次性、带过期时间、绑定具体动作和参数，不能是「本任务以后全部允许」这种通用放行（模板见 §14）。

## 12. 端到端工作流：一次无人值守任务的完整闭环

假设一个 Telegram 用户发来 `/run my-app 实现 issue #248`。可靠的系统会这样走完一圈：gateway 校验来人身份、把请求写进 job 数据库、返回 job ID；worker 领走任务，先验证 remote 可用、base branch 已更新、准备一个专属 worktree、记下 base commit；然后用 `codex exec --json` 起 Codex，逐行解析 JSONL、把状态写库、把「已接受 / 分析完 / 实施中 / 验证中」这类里程碑推给 Telegram；跑到 push 这种高风险动作时暂停，发一条带 job/branch/commit 的审批消息等人 `/approve`；批准后 resume、跑验证、生成 focused commit；最后回一份总结，带上改了什么、测试证据、commit SHA、残余风险。任何一步断线，系统都能从 job 记录、session ID 和 Git 状态重新接上——这才是「长时间运行」的真正含义。

## 13. 分阶段实施方案（Phase 1–5）

别一步到位建 SDK 平台。按风险递增分五阶段，每阶段有明确动作和验收。

### Phase 1：一小时 PoC
- 动作：选一个只读 Telegram/CLI command，后端调 `codex exec --json`，返回 final message，保存 JSONL 和 session ID，不允许写文件。
- 验收：一个只读任务能跑通并把摘要发回来。

### Phase 2：低风险写入
- 动作：加固定仓库 allowlist，用 `workspace-write`，每任务独立 worktree，跑测试，只生成 diff 不 push。
- 验收：一个写入任务能改 worktree、跑测试、产出 diff，且没碰 allowlist 外的仓库。

### Phase 3：恢复与审批
- 动作：用数据库保存 job/thread，`/continue` 能恢复 session，push 和 PR 需 Telegram 审批，加上 timeout、retry、预算。
- 验收：断线后 worker 重启能识别 orphan job；push 前一定停下来等审批。

### Phase 4：SDK 化
- 动作：从 shell wrapper 迁到 Codex SDK，加取消、流式状态、并发控制、结构化输出，建 metrics 和 dashboard。
- 验收：能同时跑多个任务、能中途取消、dashboard 显示实时状态。

### Phase 5：长期运维
- 动作：定期升级兼容性测试、secrets rotation、Hook trust audit、失败任务复盘、模型成本策略、定期清理 worktrees 和日志。
- 验收：有一套周期性运维清单在跑，而不是等出事才处理。

## 14. 可复制模板

### 模板 A：无人值守长任务 prompt（六段式）

```text
Outcome:
完成 issue #248 的实现，包括代码、测试和必要文档。

Repository state:
只在当前 task worktree 工作，以当前 base commit 为起点。

Constraints:
- 不修改数据库 schema；
- 不访问生产环境；
- 不 push main；
- 不覆盖不相关改动；
- 不引入新 runtime 依赖，除非先请求批准。

Verification:
- 相关单元测试通过；
- typecheck 通过；
- build 通过；
- 审查最终 diff；
- 创建一个 focused local commit。

Stop conditions:
- 产品行为存在关键歧义；
- 需要新增权限或 secrets；
- 连续三轮没有实质进展；
- 预计超过任务预算；
- 即将 push、deploy 或写数据库。

Final response:
总结修改、测试证据、commit SHA、未解决风险和需要人工决定的事项。
```

### 模板 B：审批消息格式（Telegram 风格）

```text
⚠️ Job 1001 requests: git push
Repository: my-app
Branch: codex/job-1001-fix-auth
Commit: a1b2c3d
Reason: publish review-ready change

/approve 1001 push-a1b2c3d
/reject 1001 push-a1b2c3d
```

### 模板 C：可直接搬的 TOML 金料

MCP —— `[mcp_servers.<name>]` 表（stdio 与 HTTP 互斥，`command`↔stdio、`url`↔HTTP）：

```toml
[mcp_servers.context7]
command = "npx"
args = ["-y", "@upstash/context7-mcp"]
startup_timeout_sec = 10          # 默认 10
tool_timeout_sec = 60             # 默认 60

[mcp_servers.figma]
url = "https://mcp.figma.com/mcp"
bearer_token_env_var = "FIGMA_OAUTH_TOKEN"
auth = "oauth"
```

Subagents —— `[agents]` 旋钮（默认值见注释）：

```toml
[features]
multi_agent = true          # 默认开

[agents]
max_threads = 6             # 默认 6
max_depth = 1               # 默认 1
job_max_runtime_seconds = 1800
```

## 15. 架构图

一个成熟的无人值守 Codex 系统长这样——官方 Remote 和自建 runner 共享同一份任务事实来源（Git branch/commit、job 数据库、Codex thread ID、worktree path），但绝不让两个入口同时对一个 worktree 发写任务：

```text
                    ┌────────────────────┐
ChatGPT Mobile ────▶│ Official Remote     │
                    └─────────┬──────────┘
                              │
Telegram ──▶ Gateway ──▶ Job Database / Approval Store
                              │
                              ▼
                       Queue Workers
                              │
             ┌────────────────┼────────────────┐
             ▼                ▼                ▼
       Worktree A       Worktree B       Worktree C
             │                │                │
       Codex SDK/exec   Codex SDK/exec   Codex SDK/exec
             │                │                │
             └────────────────┼────────────────┘
                              ▼
                  Tests → Review → Commit
                              │
                    Approval: Push / PR
                              │
                              ▼
                       GitHub / Deployment
```

核心不是让 Codex 拥有无限权限，而是让它在明确边界内持续推进、在越界前可靠暂停、任何时候都能从 job / session / Git 状态恢复。

## 16. 上线检查表

### 身份与网络
- [ ] 用户/触发者 allowlist（Telegram user/chat ID、GitHub allow-users）
- [ ] Bot token / API key 不进仓库或日志
- [ ] VPS 用非 root 独立用户，SSH key 和 Git token 最小权限
- [ ] App Server / MCP 没有无认证暴露公网

### 文件与 Git
- [ ] 仓库 path allowlist，每任务独立 worktree
- [ ] 保存 base commit、branch、final commit
- [ ] push / merge / deploy 单独审批
- [ ] 不覆盖用户本地未提交修改

### Agent 边界
- [ ] 默认只读或 `workspace-write`，不默认 `danger-full-access`
- [ ] prompt 有明确 Stop conditions
- [ ] 设了 wall-clock timeout、max retry、max subagent、credit 预算
- [ ] 高风险命令有 Rule 或 Hook 兜底

### 可恢复性
- [ ] 保存 Codex thread/session ID 与 JSONL events
- [ ] 数据库持久化 job 状态；worker 重启能识别 orphan job
- [ ] 用户可 status / continue / stop

### 验证与交付
- [ ] test/typecheck/build 命令明确
- [ ] final diff 有 review，final report 含证据和残余风险
- [ ] commit message 聚焦，日志脱敏

## 17. 官方资料索引

- [Subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents) · [MCP](https://learn.chatgpt.com/docs/extend/mcp) · [Hooks](https://learn.chatgpt.com/docs/hooks) · [Rules](https://learn.chatgpt.com/docs/agent-configuration/rules)
- [Scheduled tasks](https://learn.chatgpt.com/docs/automations) · [Cloud](https://learn.chatgpt.com/docs/cloud) · [Remote connections](https://learn.chatgpt.com/docs/remote-connections) · [Worktrees](https://learn.chatgpt.com/docs/environments/git-worktrees)
- [Non-interactive mode](https://learn.chatgpt.com/docs/non-interactive-mode) · [Codex SDK](https://learn.chatgpt.com/docs/codex-sdk) · [App Server](https://learn.chatgpt.com/docs/app-server) · [Use Codex with Agents SDK](https://learn.chatgpt.com/docs/mcp-server) · [GitHub Action](https://learn.chatgpt.com/docs/github-action)
- [Sandbox and approvals](https://learn.chatgpt.com/docs/agent-approvals-security) · [Long-running work](https://learn.chatgpt.com/docs/long-running-work) · [Authentication](https://learn.chatgpt.com/docs/auth)
- 长任务方法论：[官方博客 · long-horizon tasks](https://developers.openai.com/blog/run-long-horizon-tasks-with-codex) · [Cookbook · ExecPlans](https://developers.openai.com/cookbook/articles/codex_exec_plans)
- 追新唯一权威：[changelog](https://learn.chatgpt.com/docs/changelog) · `/models`

---

## 更新记录

| 日期 | 变更 | 官方来源 |
|---|---|---|
| 2026-07-17 | 按 guide 模板 v1 重组为读者指南形状（心智模型流水线 + 每主题处方 + 何时升级 SDK 决策表 + 风险分级表 + 任务持久层/状态机 + 端到端无人值守闭环 + Phase 1-5 实施 + 无人值守 prompt/审批/TOML 模板 + ASCII 架构图 + 上线检查表）；核验台账迁至 `facts.md`；补入已核验的 codex exec flags/JSONL、Codex SDK、App Server、Agents SDK `mcp-server`、GitHub Action、任务数据库 schema。 | learn.chatgpt.com/docs/{agent-configuration/*,extend/mcp,hooks,automations,cloud,remote-connections,environments/git-worktrees,non-interactive-mode,codex-sdk,app-server,mcp-server,github-action} · developers.openai.com/{blog,cookbook} |
| 2026-07-17 | 初版：由角度「Codex 进阶实战：当自主 agent 平台压榨」成篇，合并旧+新调研并校准——subagents `[agents]` 默认值、MCP `[mcp_servers]` 逐字、hooks 10 事件、Scheduled tasks（RRULE/approval=never）、Cloud 12h 缓存+网络分离、Remote GA（06-25）、长时任务四文件法、`/goal` 三部曲真实标题。 | learn.chatgpt.com/docs/{agent-configuration/subagents,extend/mcp,hooks,automations,cloud,remote-connections,environments/git-worktrees} · developers.openai.com/{blog,cookbook} |
