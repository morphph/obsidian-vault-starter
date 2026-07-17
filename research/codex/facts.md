# Codex 核验事实台账（facts.md）

> **这不是给人读的成品**,是两份 Codex 常青指南(`codex-overview.md` / `codex-advanced.md`)的**事实底座**。
> 所有研究元话术住这里——逐条核验状态(✅/⚠️/❌)、确切默认值、GA/弃用追踪、第三方辨伪、
> 「推断·未实测」标注。指南正文只取这里的**已核验结论**,并把最要命的 gotcha 以 callout 精华形式带进对应节。
> 官方源:`learn.chatgpt.com/docs/*`(Codex 文档已并入 ChatGPT Learn)· `developers.openai.com/{blog,cookbook}`。
> 事实漂移极快(默认模型/域名/改名两周内可全变),发稿前重核 [`/changelog`](https://learn.chatgpt.com/docs/changelog) 与 `/models`。

---

## A. 产品形态与入口

- **Codex = OpenAI 的智能编码 agent(agentic coding agent)**,开源、Rust 写。— ✅ [cli](https://learn.chatgpt.com/docs/cli)
- **四/多个 surface 共享一套配置**(approval policy / MCP / AGENTS.md / 模型偏好):CLI · IDE 扩展(VS Code/JetBrains,也能在 Cursor/Windsurf 跑)· 桌面 App(**2026-07-09 起并入 ChatGPT 桌面 App**)· Codex Cloud。另有 `codex exec` / Codex SDK / App Server / GitHub Action 等编排入口。— ✅ [ide](https://learn.chatgpt.com/docs/ide)
- **共享的是本机 config.toml / MCP / AGENTS.md 配置;本地、云端、远程主机仍是不同执行环境**,文件/凭证/工具不自动同步。— ✅

## B. 装 & 登录

- 官方 installer:`curl -fsSL https://chatgpt.com/codex/install.sh | sh`;无人值守/CI 加 `CODEX_NON_INTERACTIVE=1`。npm:`npm i -g @openai/codex`(需 Node ≥ 22)。— ✅ [cli](https://learn.chatgpt.com/docs/cli)
- 首次运行二选一:ChatGPT 账号登录 **或** 填 API key。— ✅

## C. 模型：GPT-5.6 家族

- **当前默认 = `gpt-5.6-sol` @ medium reasoning**。GPT-5.6 是 Sol / Terra / Luna 家族(2026-07 起为 Codex 默认线)。— ✅ [models](https://learn.chatgpt.com/docs/models)

| 模型 | 定位 | 状态 |
|---|---|---|
| `gpt-5.6-sol` | 当前默认 | ✅ |
| `gpt-5.6` | frontier(最难的活) | ✅ |
| `gpt-5.6-terra` | 更快更便宜(并行 worker) | ✅ |
| `gpt-5.4` / `gpt-5.4-mini` | 上一代 / 便宜快 | ✅ 回退可用 |
| `gpt-5.3-codex-spark` | 更快变体 | ⚠️ research preview(Pro) |
| `gpt-5.2` / `gpt-5.3-codex` | — | ❌ **已弃用**,对 ChatGPT 登录用户下架 |

- **命名两条线**:通用 frontier 线(gpt-5.4 / 5.6,现驱动 Codex)vs 旧「-Codex」后缀线(5.2/5.3-Codex,退场中)。方向 = 统一到 frontier,专用后缀退场。— ✅

## D. AGENTS.md（三级优先级）

- Codex 动手前先读的 markdown 指令文件,**三级从远到近拼接、近的覆盖远的**:Global `~/.codex/AGENTS.md` → repo 根 → 一路向下到 cwd 逐层合并,离 cwd 越近优先级越高。— ✅ [agents-md](https://learn.chatgpt.com/docs/agent-configuration/agents-md)
- 旋钮:`project_doc_max_bytes`、`project_doc_fallback_filenames`(fallback 顺序 `AGENTS.override.md → AGENTS.md → TEAM_GUIDE.md → .agents.md`)。`AGENTS.override.md` 覆盖同层一般文件。— ✅
- 项目级指令纳入 Git;个人偏好放 `~/.codex/`(全局)。— ✅

## E. config.toml（运行行为配置中心）

- 位置:用户级 `~/.codex/config.toml` · 项目级 `.codex/config.toml`(覆盖,**仅在项目被信任时加载**)· 状态目录 `CODEX_HOME`(默认 `~/.codex`)· CLI `-c key=value` 单次覆盖。— ✅ [config](https://learn.chatgpt.com/docs/config-file/config-reference)
- 不可信项目的项目级 Hooks/Rules/config 被忽略;用户级、系统级仍独立生效。— ✅
- 三个最该懂的键:`model` · `approval_policy`(untrusted/on-request/never)· `sandbox_mode`(read-only/workspace-write/danger-full-access)。— ✅

## F. Sandbox / Approval policy / Rules（三个别混）

- **Sandbox** = agent 实际能读/改/访问什么(read-only / workspace-write / danger-full-access)。— ✅
- **Approval policy** = 什么时候向用户请求授权(untrusted / on-request / never)。— ✅
- **Rules** = 某类命令请求离开 sandbox 时 allow / prompt / forbidden。— ✅ [rules](https://learn.chatgpt.com/docs/agent-configuration/rules)
- **Rules 语法(已核验)**:`prefix_rule()`,参数 `pattern`(必填,命令前缀列表)/ `decision`(allow|prompt|forbidden)/ `justification` / `match`·`not_match`(测试样例)。**用 Starlark(类 Python 沙箱语言)写,存 `rules/` 下的 `.rules` 文件**;Codex 逐条解析线性 shell 脚本、对复杂脚本保守处理。**实验特性。** — ✅
- 决策三档按严格度:`allow`(沙箱外直接跑)/ `prompt`(每次问)/ `forbidden`(禁止)。— ✅

## G. Subagents（子智能体）

- **开关:`[features] multi_agent = true`,默认已开,没有单独的 `subagents` flag**。暴露的多智能体工具:`spawn_agent` / `send_input` / `resume_agent` / `wait_agent` / `close_agent`。— ✅ [subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents)
- **`[agents]` 确切默认值**:`max_threads = 6`(同时最多几个子 agent)· `max_depth = 1`(root=depth 0,允许一层)· `job_max_runtime_seconds = 1800` · `interrupt_message = true`。— ✅
- 三个内置 agent:`default`(通用兜底)/ `worker`(执行/实现/修复)/ `explorer`(只读代码探索)。— ✅
- 自定义 agent:每个一个 TOML 文件,放 `~/.codex/agents/`(个人)或 `.codex/agents/`(项目);键含 `name`/`description`/`developer_instructions`/`nickname_candidates`,可选继承 `model`/`model_reasoning_effort`/`sandbox_mode`/`mcp_servers`/`skills.config`。— ✅
- **批处理 `spawn_agents_on_csv`(experimental)**:读 CSV → 每行 spawn 一个 worker → 全批等待 → 导出 CSV。每个 worker **必须调一次 `report_agent_job_result`**,否则该行 `status: error`。— ✅

## H. MCP

- **`[mcp_servers.<name>]` 表(不是 `[mcp]` 块)**。stdio:`command` + `args` + `env_vars` + `startup_timeout_sec`(默认 10)+ `tool_timeout_sec`(默认 60)+ 子表 `[mcp_servers.<name>.env]`。streamable HTTP:`url` + `bearer_token_env_var` + `auth="oauth"` + 子表 `[.http_headers]`。`command`↔stdio、`url`↔HTTP **互斥**。— ✅ [mcp](https://learn.chatgpt.com/docs/extend/mcp?surface=cli)
- CLI:`codex mcp add <name> -- <cmd>` · `codex mcp list` · `codex mcp login <server>`。本地客户端支持 STDIO + Streamable HTTP;桌面/CLI/IDE 共享同一 host 的 MCP 配置。— ✅
- App connectors(GitHub / Google Drive / Slack 等)= 已授权 SaaS 工作区的账号授权/私有数据/业务动作,不是通用网页搜索。结构化 connector/API/MCP 优先于 UI 操作(Browser/Chrome/Computer Use)。— ✅

## I. Hooks

- **10 个生命周期事件**:turn 级 8 个(`PreToolUse` / `PermissionRequest` / `PostToolUse` / `PreCompact` / `PostCompact` / `UserPromptSubmit` / `SubagentStop` / `Stop`)+ 启动级 2 个(`SessionStart` / `SubagentStart`)。— ✅ [hooks](https://learn.chatgpt.com/docs/hooks)
- **阻断 = handler `exit 2` + 原因写 stderr**。配置位置:`~/.codex/config.toml` / `~/.codex/hooks.json` / `repo/.codex/config.toml` / `repo/.codex/hooks.json`。个人:`[[hooks.PreToolUse]]` + `matcher`;企业托管:`requirements.toml`(`allow_managed_hooks_only`、`[hooks] managed_dir`)。项目 Hook 只在可信项目加载,改动后 hash 变会重触发审查。— ✅
- ⚠️ **GA 存疑**:官方 hooks 页**未标 GA 日期**。第三方称 GA=2026-05-14 / engine 稳定于 v0.124.0(2026-04-23)——**第三方,官方未逐字确认**。指南正文不写 GA 日期。

## J. Skills

- 遵循 **Agent Skills 开放标准**([agentskills.io](https://agentskills.io/specification),与 Anthropic Skills 同标准):含 `SKILL.md` 的目录(+ `scripts/`/`references/` + Codex 专属 `agents/openai.yaml`)。渐进披露:元数据启动加载 → 指令激活加载 → 资源按需。— ✅ [skills](https://learn.chatgpt.com/docs/build-skills)
- 预算:发现清单 = 上下文 2%(未知时 8,000 字符);单个 skill 正文建议 < 5000 tokens / SKILL.md < 500 行。关隐式调用(仍可 `$skill` 显式调):`agents/openai.yaml` 写 `policy: { allow_implicit_invocation: false }`。— ✅
- ⚠️ **Skills 官方未打 "GA" 标签**(已发布未标注)。指南正文不写 GA。

## K. Plugins

- **可安装的分发包**,组合 Skills / MCP servers / Hooks / connectors / commands / assets / marketplace metadata。— ✅ [plugins](https://learn.chatgpt.com/docs/build-plugins)
- **判断规则(已核验)**:还在单 repo/个人流程迭代 → 先做 local Skill;要跨团队/机器分发、打包 connector+MCP+hooks、发稳定包 → 才做 Plugin。— ✅

## L. Scheduled tasks（原 Automations）

- 官方已改名 "Scheduled tasks"。两型:standalone(每次起新 chat,可跨多 project)/ chat 内(复用上下文,支持**分钟级**主动跟进循环)。可跑在隔离 worktree;组织策略允许时自动用 `approval_policy="never"`,被 `requirements.toml` 禁止时回退到所选权限模式。需保持机器开机 + 桌面 App 运行。— ✅ [automations](https://learn.chatgpt.com/docs/automations)
- ⚠️ **调度是 RRULE 不是 cron**:App 内用 **RRULE(RFC 5545)**(如 `RRULE:FREQ=WEEKLY;BYDAY=MO;BYHOUR=9`);**cron 只在 CLI headless 路径**(`codex exec` 配你自己的 cron / GitHub Actions),UI 里填不了 cron。→ 进指南正文作 `> [!warning]`。
- ⚠️ **辨伪**:"heartbeat automations" / "Triage automations" 是坊间/GitHub issue 词,**不是官方分类**——官方只有一个 "Scheduled" 收件箱视图。指南正文不用这两个词。

## M. Codex Cloud

- 云面 `chatgpt.com/codex`;环境配置 `chatgpt.com/codex/settings/environments`;默认镜像 `universal`(`openai/codex-universal`)。— ✅ [cloud](https://learn.chatgpt.com/docs/cloud)
- **容器缓存最长 12 小时**(改 setup/maintenance script、env、secrets 会失效)。— ✅
- **网络分离(安全边界关键)**:setup 阶段有网、**agent 阶段默认无网**(可开);**secrets 只给 setup,agent 阶段前移除**,env vars 全程保留。— ✅
- `@codex` GitHub:`@codex review`(👀 + 行内发现 + PR 级总结)/ `@codex review for security regressions`(一次性聚焦)/ `@codex fix the P1 issue`(评审后修复,起云 chat)。评审规则用最近的 `AGENTS.md`;设置有 "Automatic reviews" 开关。— ✅ [github](https://learn.chatgpt.com/docs/third-party/github)

## N. Codex Remote（手机远程）

- **2026-06-25 GA**。手机是**控制面,不是第二个 Codex**:主机提供环境,手机发 prompt/审批/后续。— ✅ [remote](https://learn.chatgpt.com/docs/remote-connections)
- **二维码配对**(桌面 App 生 QR,扫码进 ChatGPT,认证一对一,绑当前登录会话);**secure relay 不把主机暴露公网**。随 GA 附 DigitalOcean 插件(`@DigitalOcean` 起 Droplet 当主机)。— ✅
- 限制:配对 desktop host 必须在线;主机睡眠/断网/关 App → Remote 中断;手机不直连 VPS;24/7 需 always-on host 或 `codex exec`/SDK 自建持久服务。— ✅

## O. Worktrees（桌面 App）

- **不是自动 per-thread**:新建 chat 时**手动选 "Worktree" / "Local"**;每个托管 worktree 通常专属一个 chat,resume 回同一 worktree。— ✅ [worktrees](https://learn.chatgpt.com/docs/environments/git-worktrees)
- **"Hand off"** 在 Local(前台)↔ Worktree(后台)间移动 chat = 官方并行范式。worktree root 默认 `$CODEX_HOME/worktrees`,自动清理保留**最近 15 个**(Settings > Worktrees;**config.toml 无专门 worktree 键**)。`projects.<path>.trust_level` 可标 trusted/untrusted。— ✅
- ⚠️ **辨伪**:CLI 无原生 `--worktree` flag(第三方说法),指南正文不写该 flag。

## P. codex exec（非交互式）

- flags(已核验):`--json`(JSONL 事件流)· `-o` / `--output-last-message`(存最终消息)· `--sandbox`(read-only 默认 / workspace-write / danger-full-access)· `--ephemeral`(不落 rollout 文件)· `--ignore-user-config` · `--ignore-rules`。恢复:`codex exec resume --last` / `codex exec resume <SESSION_ID>`。— ✅ [non-interactive](https://learn.chatgpt.com/docs/non-interactive-mode)
- **JSONL 事件类型**:`thread.started` · `turn.started` / `turn.completed` / `turn.failed` · `item.started` / `item.completed` / `item.*` · `error`。worker 应逐行解析,不要等进程结束一次读全。— ✅
- 生产不要依赖 `--last`,存准确 SESSION_ID。— ✅

## Q. Codex SDK / App Server / Agents SDK / GitHub Action

- **Codex SDK(已核验)**:TypeScript(Node 18+)· Python(3.10+,经 JSON-RPC 与本地 app-server 通信,含 `AsyncCodex` 异步变体)。能创建/恢复 thread、多轮跑、控 sandbox(per-turn 预设 read-only/workspace-write/full)。— ✅ [codex-sdk](https://learn.chatgpt.com/docs/codex-sdk)
- **App Server(已核验)**:驱动 rich client(如 VS Code 扩展)的底层接口;支持 authentication(bearer / SHA256 / signed token)、conversation history(persist/resume/fork/archive)、approvals、streamed events;JSON-RPC 2.0 over stdio / WebSocket / Unix socket。**明文 `ws://` 只用于 localhost 或 SSH 端口转发;远程需 TLS + 认证**。— ✅ [app-server](https://learn.chatgpt.com/docs/app-server)
- **Agents SDK 编排(已核验)**:`codex mcp-server` 把 Codex CLI 暴露成 MCP server,露出 `codex()` / `codex-reply()` 两个工具;OpenAI Agents SDK 可 handoff / guardrails / traces,把 Codex 当 coding specialist。— ✅ [mcp-server](https://learn.chatgpt.com/docs/mcp-server)
- **GitHub Action(已核验)**:`openai/codex-action@v1`,CI 里分析/修复失败检查、跑受控 review、写回结果。安全:`allow-users`/`allow-bots` 限触发者、**sanitize PR/commit/issue 文本防 prompt injection**、`safety-strategy`(`drop-sudo`/`unprivileged-user`)、Codex 作为最后一步。不能让不受信任的 issue/PR 文本驱动高权限 agent。— ✅ [github-action](https://learn.chatgpt.com/docs/github-action)

## R. Import from another agent

- 桌面 App `Settings > Import` 从其他 agent(如 Claude Code)导入。映射(已核验):Instruction files → `AGENTS.md`(及 `settings.json` → `config.toml`)· Skills/Plugins · MCP config · Hooks · Slash commands · Subagents → Codex agents · Project folders → Projects · 最近 30 天对话 → Tasks。**一次性,非持续双向同步**;不删原设置;导入的 plugin 可能需重新授权/登录。— ✅ [import](https://learn.chatgpt.com/docs/import)

## S. 长时任务方法论

- **四文件法**(官方博客,Derrick Choi,2026-02-23):`Prompt.md`(冻结目标:Goals/非目标/硬约束/交付物/"Done when")· `Plan.md`(里程碑 + 每里程碑验证命令 + Stop-and-fix rule)· `Implement.md`(执行手册,声明 "Plans markdown file is source of truth")· `Documentation.md`(状态 + 审计日志)。硬指标:**~25 小时不间断 / ~13M tokens / ~30k 行代码**。用 `/plan` 命令(**提示工程纪律,不是配置菜谱**,不含 approval/cron)。— ✅ [blog](https://developers.openai.com/blog/run-long-horizon-tasks-with-codex)
- **PLANS.md / ExecPlan**(官方 Cookbook,Aaron Friel,2025-10-07):自包含"活文档",与 AGENTS.md 配合(AGENTS.md 放触发短语);四个必需小节 **Progress · Surprises & Discoveries · Decision Log · Outcomes & Retrospective**;实证单 prompt 工作 **7+ 小时**。— ✅ [cookbook](https://developers.openai.com/cookbook/articles/codex_exec_plans)

## T. /goal loop 方法论

- `/goal` 与 `/plan` 都是**真官方 CLI slash 命令**(`/goal` = "Set, edit, pause, resume, view, or clear a task goal")。— ✅ [commands](https://learn.chatgpt.com/docs/developer-commands?surface=cli)
- 官方 Cookbook 三部曲:① Using Goals in Codex(Raj Pathak & Stefano Fabbri,2026-05-09)—— `/goal` = "completion contract",work→check→continue,需证据才算完成。② Build Iterative Repair Loops(Shreekant Agrawal,2026-05-11)—— Review→Repair→Validate,`repair_until_done()` 带停止条件(默认 max 3 轮),审计 `record.json`。③ Build an Agent Improvement Loop(Wesley Pasfield,2026-05-12)—— 5 段飞轮 Traces→Feedback→Evals→Validation→Harness Changes,交接制品 `codex_handoff.md`。— ✅
- ⚠️ **别抄**:第三方博客里的 `[goals] max_turns / check_model="o4-mini" / timeout_minutes` 块**官方无法证实**(`o4-mini` 对 2026 可疑),勿作事实源。指南正文不出现这些键。

## U. Prompting（GPT-5.6）

- 精简 prompt 提分 **10–15%** 且省 **41–66% token**;从 medium reasoning 起步,难任务再上 `reasoning.mode:"pro"`。— ✅ [prompting](https://developers.openai.com/api/docs/guides/prompt-guidance-gpt-5p6)
- 别在 prompt 里预告 "plan/status"(易早停);preamble 用 `phase` 参数;AGENTS.md 注入顺序影响效果。— ✅ [cookbook](https://developers.openai.com/cookbook/examples/gpt-5/codex_prompting_guide)

---

## 更新记录（本台账）
| 日期 | 变更 | 官方来源 |
|---|---|---|
| 2026-07-17 | 从 `codex-overview.md` / `codex-advanced.md` 迁出全部核验台账内容(确切 TOML/默认值、GA/弃用、RRULE-vs-cron、辨伪块),并 WebFetch 核验 Codex 范文独有的净新事实(Rules `prefix_rule`+Starlark、Plugins、codex exec flags/JSONL、Codex SDK、App Server、Agents SDK `mcp-server`、GitHub Action `openai/codex-action@v1`、Import 映射)——全部 ✅ | learn.chatgpt.com/docs/{models,agent-configuration/{rules,subagents,agents-md},config-file,extend/mcp,hooks,build-skills,build-plugins,automations,cloud,remote-connections,environments/git-worktrees,non-interactive-mode,codex-sdk,app-server,mcp-server,github-action,import} · developers.openai.com/{blog,cookbook} |
