---
status: draft
sources:
  - raw/2026-04-09-bcherny-claude-code-best-practices.md
  - raw/2026-04-09-claude-code-official-docs-best-practices.md
platform: blog
created: 2026-04-09
last-updated: 2026-04-09
tags: [draft]
---

<!-- HOOK: Claude Code创始人Boris Cherny发了3条viral thread（合计数百万views）分享他的使用技巧。我把他的每条建议和Anthropic官方文档交叉对照，整理成这份完全指南——Boris怎么说、官方文档怎么写、具体怎么配置。 -->

# Claude Code Best Practices完全指南

Boris Cherny（Claude Code创始人）发了三条viral thread分享他的Claude Code使用技巧。我把他的每条建议和Anthropic官方文档交叉对照，整理成这份指南。每个实践都标注了：Boris怎么说、官方文档怎么写、具体怎么配置。

官方文档地址：[code.claude.com/docs](https://code.claude.com/docs/en/)

![[visual-best-practices-guide.png]]

---

## 一、基础工作流

### 1. 选对模型

**Boris:** "Uses Opus 4.5 with thinking for everything. It's the best coding model I've used. Even though bigger and slower than Sonnet, usually faster overall due to better steering and tool use."

**官方文档:** [Model Config](https://code.claude.com/docs/en/model-config)

模型别名一览：

| 别名 | 实际模型 | 适合场景 |
|------|---------|---------|
| `opus` | Opus 4.6 | 最强能力，复杂任务 |
| `sonnet` | Sonnet 4.6 | 平衡速度和能力 |
| `haiku` | Haiku 4.5 | 快速简单任务 |
| `opus[1m]` | Opus 4.6 + 1M context | 大项目 |
| `opusplan` | Opus规划 + Sonnet执行 | 省钱但不降质 |

设置方法：
- 会话中切换：`/model opus` 或快捷键 `Option+P`
- 启动时指定：`claude --model opus`
- 永久设置：settings.json里 `"model": "opus"`

Extended thinking（深度思考）：
- 快捷键：`Option+T` 开关
- 在prompt里写"ultrathink"可以临时触发高强度思考
- Effort levels: `low` / `medium` / `high` / `max`（Opus only）

### 2. 投资CLAUDE.md

**Boris:** "Team maintains shared CLAUDE.md checked into git. Whole team contributes multiple times a week. After every correction, end with: 'Update your CLAUDE.md so you don't make that mistake again.'"

**官方文档:** [Memory](https://code.claude.com/docs/en/memory)

CLAUDE.md在每一轮API调用都会被加载。位置和优先级：

| 范围 | 文件位置 | 优先级 |
|------|---------|--------|
| 组织策略 | `/Library/Application Support/ClaudeCode/CLAUDE.md` | 最高 |
| 项目共享 | `./CLAUDE.md` 或 `./.claude/CLAUDE.md` | 中 |
| 个人全局 | `~/.claude/CLAUDE.md` | 低 |
| 个人项目 | `./CLAUDE.local.md`（gitignore） | 最低 |

最佳实践：
- 目标 **200行以内**——太长反而降低遵从度
- 只放每个session都必须true的东西：构建命令、目录结构、编码规范、NEVER list
- 不要放：长篇背景、API文档、模糊原则
- 语言/目录specific规则放 `.claude/rules/`（支持 `paths:` glob前缀，按需加载）
- `@path/to/file` 语法可以import其他文件（最多5层嵌套）
- `claudeMdExcludes` 设置可以排除monorepo中不相关的CLAUDE.md
- `/init` 自动生成starter；`/memory` 查看所有已加载的指令文件

**加Compact Instructions：** 在CLAUDE.md里写明压缩时保留什么：
```markdown
## Compact Instructions
When compressing, preserve in priority order:
1. Architecture decisions (NEVER summarize)
2. Modified files and key changes
3. Current verification status
4. Open TODOs
5. Tool outputs (can delete, keep pass/fail only)
```

### 3. Plan Mode工作流

**Boris:** "Sessions typically start in Plan mode. Goes back and forth with Claude until plan looks good. Then switches to auto-accept. Claude usually completes in one shot after good planning. Pro move: one Claude writes plan, second Claude reviews like a staff engineer."

**官方文档:** [Permission Modes](https://code.claude.com/docs/en/permission-modes)

Plan mode = 只读探索，不改文件。在context最干净的时候做最重要的决策。

操作方式：
- 会话中：`Shift+Tab` 循环切换（default → acceptEdits → plan）
- 启动时：`claude --permission-mode plan`
- 单条prompt：用 `/plan` 前缀
- 设为默认：settings.json里 `"permissions": { "defaultMode": "plan" }`

Plan确认后的选项：
- 切到auto mode自动执行
- 切到acceptEdits逐步确认
- 继续规划（给反馈）
- 用Ultraplan在浏览器中review

6种权限模式一览：`default`、`acceptEdits`、`plan`、`auto`、`dontAsk`、`bypassPermissions`

### 4. Context管理

**Boris没有直接提到，但这是高效使用的基础。**

**官方文档:** [Commands](https://code.claude.com/docs/en/commands)

三个关键命令：
- **`/context`** — 可视化context占用（彩色网格），给出优化建议
- **`/compact [instructions]`** — 压缩对话，可指定保留重点。例：`/compact focus on the auth module changes`
- **`/clear`**（别名 `/reset`, `/new`）— 清空对话历史，释放context

什么时候用哪个：
- 换任务 → `/clear`
- 同一任务进入新阶段 → `/compact`
- 想知道还剩多少空间 → `/context`

---

## 二、并行化

### 5. Git Worktrees并行工作

**Boris (团队头号生产力提升):** "Spin up 3-5 git worktrees at once, each running its own Claude session in parallel. Shell aliases (za, zb, zc) for quick switching. Some maintain dedicated analysis worktrees for logs/BigQuery."

**官方文档:** [Common Workflows](https://code.claude.com/docs/en/common-workflows)

```bash
# 创建worktree并启动session
claude --worktree feature-auth    # 创建 .claude/worktrees/feature-auth/
claude -w                          # 自动生成随机名称

# 在已有session中
# 告诉Claude "work in a worktree" 也可以
```

关键细节：
- Worktree从 `origin/HEAD` 分支创建
- `.worktreeinclude` 文件列出需要复制的gitignored文件（如 `.env`）
- 无更改时自动清理；有更改时提示保留/删除
- `/resume` 可以跨worktree查看和恢复session
- 建议把 `.claude/worktrees/` 加入 `.gitignore`

### 6. 并行Sessions

**Boris:** "Runs 5 Claudes in parallel in terminal with numbered tabs + system notifications. Also runs 5-10 concurrent sessions on claude.ai/code."

每个session有独立的context窗口。一个session做一件事 = 每个context保持聚焦。

设置通知hook让你知道哪个session完成了：
```json
// .claude/settings.json
{
  "hooks": {
    "Stop": [{
      "matcher": "",
      "hooks": [{
        "type": "command",
        "command": "osascript -e 'display notification \"Claude finished\" with title \"Session Done\"'"
      }]
    }]
  }
}
```

### 7. /batch分布式变更

**Boris:** "Distributed changesets across dozens/hundreds/thousands of worktree agents."

**官方文档:** [Skills — Bundled](https://code.claude.com/docs/en/skills#bundled-skills)

```
/batch migrate src/ from Solid to React
```

工作流：
1. 研究codebase
2. 分解为5-30个独立单元
3. 呈现计划等你确认
4. 确认后，每个单元启动独立agent在隔离worktree中执行
5. 每个agent实现变更、跑测试、开PR

---

## 三、自动化 & 自定义

### 8. Slash Commands / Skills

**Boris:** "Uses slash commands for every inner loop workflow done many times a day. /commit-push-pr used dozens of times daily. Stored in .claude/commands/, committed to git for team reuse."

**官方文档:** [Skills](https://code.claude.com/docs/en/skills)

Skills是Commands的升级版——旧的 `.claude/commands/` 仍然有效，但Skills功能更强。

创建方法：
```
.claude/skills/commit-push-pr/
  SKILL.md           # 主指令（必需）
  template.md        # 可选模板
  scripts/           # 可选脚本
```

SKILL.md示例：
```markdown
---
name: commit-push-pr
description: Commit, push, and create PR
argument-hint: [branch-name]
allowed-tools:
  - Bash(git *)
  - Bash(gh pr create *)
---

1. Stage all changes
2. Write commit message based on diff
3. Push to origin
4. Create PR with gh cli
```

关键frontmatter字段：
- `disable-model-invocation: true` — 只允许用户手动触发
- `paths: ["src/**/*.ts"]` — 只在匹配路径时自动激活
- `context: fork` — 在subagent中运行（不占主context）
- `model: sonnet` — 用特定模型执行

动态内容注入：`` !`command` `` 语法在发送前执行shell命令

### 9. Hooks

**Boris:** "PostToolUse hooks for auto-formatting. Pre-configured permissions in .claude/settings.json. Notification hooks for desktop alerts."

**官方文档:** [Hooks](https://code.claude.com/docs/en/hooks)

Hooks在context外部执行——不占Claude注意力。4种handler类型：`command`、`http`、`prompt`、`agent`。

**22个hook事件类型**（Boris只提了几个，完整列表）：

| 常用事件 | 触发时机 | 能阻止？ |
|---------|---------|---------|
| `SessionStart` | session开始/恢复 | 否 |
| `PreToolUse` | 工具执行前 | 是 |
| `PostToolUse` | 工具成功后 | 否 |
| `Stop` | Claude完成回复 | 是 |
| `PreCompact` | context压缩前 | 否 |
| `SessionEnd` | session结束 | 否 |
| `FileChanged` | 监控文件变化 | 否 |
| `WorktreeCreate` | worktree创建 | 是 |

Boris的auto-formatting hook配置：
```json
{
  "hooks": {
    "PostToolUse": [{
      "matcher": "Edit|Write",
      "hooks": [{
        "type": "command",
        "command": "npx prettier --write $CLAUDE_FILE_PATH",
        "timeout": 10000
      }]
    }]
  }
}
```

Exit codes很重要：
- `0` = 成功
- `2` = 阻止操作（stderr内容会反馈给Claude）
- `1` = 非阻止性错误

### 10. Subagents

**Boris:** "Uses subagents: code-simplifier, verify-app. Append 'use subagents' to any request where you want Claude to throw more compute at the problem. Routes permission requests to Opus 4.5 for attack scanning."

**官方文档:** [Sub-agents](https://code.claude.com/docs/en/sub-agents)

三个内置subagent：
- **Explore** — Haiku模型，只读，快速搜索codebase
- **Plan** — 继承主模型，只读，规划模式研究
- **General-purpose** — 继承主模型，所有工具

自定义subagent：创建 `.claude/agents/code-simplifier.md`：
```markdown
---
name: code-simplifier
description: Simplify and refactor code for readability
tools:
  - Read
  - Grep
  - Glob
  - Edit
  - Write
model: sonnet
maxTurns: 15
---

You are a code simplification expert. When given code:
1. Identify unnecessary complexity
2. Propose simplified alternatives
3. Implement changes preserving behavior
```

关键配置：
- `isolation: worktree` — 在隔离worktree中运行
- `background: true` — 后台运行
- `permissionMode: acceptEdits` — 自动接受编辑
- `mcpServers` — 给subagent专属的MCP server
- 不能嵌套（subagent不能再启动subagent）

调用方式：自动（描述匹配）、`@"code-simplifier (agent)"`、`--agent code-simplifier`、自然语言

### 11. MCP集成

**Boris:** "Slack MCP integration — paste bug threads, say 'fix'. Claude can troubleshoot failing CI tests and docker logs without micromanagement."

**官方文档:** [MCP](https://code.claude.com/docs/en/mcp)

三种传输方式：HTTP（推荐）、SSE（已废弃）、stdio（本地进程）

添加MCP server：
```bash
# HTTP server
claude mcp add --transport http slack-mcp https://slack-mcp.example.com

# 本地进程
claude mcp add github-mcp -- npx @anthropic/mcp-github

# 查看状态
claude mcp list
```

三种作用域：
- **Local**（默认）— `~/.claude.json`，个人+当前项目
- **Project** — `.mcp.json`，提交到git，团队共享
- **User** — `~/.claude.json`全局，所有项目

热门MCP servers：Sentry, GitHub, Notion, Stripe, Asana, Airtable, Slack, Linear

---

## 四、验证 & 质量

### 12. Chrome Extension

**Boris (最重要的建议):** "Give Claude a way to verify its work. Chrome extension for frontend work. Once you do that, Claude will iterate until the result is great."

**官方文档:** [Chrome](https://code.claude.com/docs/en/chrome)（Beta）

前提条件：
- Chrome/Edge + Claude in Chrome扩展 v1.0.36+
- Claude Code v2.0.73+
- Anthropic直接订阅（Pro/Max/Team/Enterprise）

启动：`claude --chrome` 或会话中 `/chrome`

能做什么：
- **Live debugging** — 读console error和DOM状态，然后修代码
- **Design verification** — 构建UI后在浏览器中对照mockup验证
- **Web app testing** — 表单验证、视觉回归、用户流程测试
- **Authenticated apps** — 用你的登录态操作Google Docs、Gmail、Notion等
- **Session recording** — 录制操作为GIF

工作原理：Claude打开新tab、导航、点击、输入、读console、截屏。遇到登录/CAPTCHA时暂停等你手动操作。

### 13. Output Styles

**Boris:** "Enable Explanatory or Learning output styles. Request HTML presentations of unfamiliar code."

**官方文档:** [Output Styles](https://code.claude.com/docs/en/output-styles)

三种内置style：
- **Default** — 标准软件工程模式
- **Explanatory** — 在帮你干活的同时解释WHY（教育性"Insights"）
- **Learning** — 协作学习模式，给你标记 `TODO(human)` 让你自己写一部分

切换：`/config` → 选择 Output style，或settings.json里 `"outputStyle": "Explanatory"`

自定义style：在 `~/.claude/output-styles/` 或 `.claude/output-styles/` 放markdown文件，frontmatter里 `keep-coding-instructions: false` 可以完全替换代码相关的系统提示。

---

## 五、移动性 & 远程

### 14. Session Teleport

**Boris:** "claude --teleport or /teleport — continue cloud session locally."

**官方文档:** [Claude Code on the Web](https://code.claude.com/docs/en/claude-code-on-the-web)

```bash
claude --teleport              # 交互式选择cloud session
claude --teleport <session-id> # 直接恢复指定session
/teleport                      # 会话中使用（别名 /tp）
```

单向：cloud → local。Claude会验证你在正确的repo，checkout对应branch，加载完整对话历史。

前提：干净的git状态、正确的repo、branch已push、同一账号。

### 15. Remote Control

**Boris:** "Control local session from phone/web. Enable 'Remote Control for all sessions' in config."

**官方文档:** [Remote Control](https://code.claude.com/docs/en/remote-control)

三种启动方式：
```bash
claude remote-control          # 服务器模式，显示URL和QR码
claude --remote-control        # 带RC的交互session
/remote-control                # 已有session中开启
```

本质：一切在本地运行，web/mobile只是一个窗口。支持多concurrent sessions（`--spawn`）。断网后自动重连。

可以在 `/config` 里设为所有session默认开启。

### 16. Mobile App

**Boris:** "iOS app via Code tab — code without opening laptop."

**官方文档:** [Overview](https://code.claude.com/docs/en/overview), [Remote Control](https://code.claude.com/docs/en/remote-control)

- iOS: claude.ai/code的web界面在Claude iOS app中可用
- 用Remote Control从手机连接到本地CLI session
- 用Dispatch从手机发任务给Desktop app启动Code session
- `/mobile` 命令显示下载QR码

### 17. Cowork Dispatch

**Boris:** "Secure remote control for Claude Desktop app (Slack, email, file management)."

**官方文档:** [Desktop — Dispatch](https://code.claude.com/docs/en/desktop#sessions-from-dispatch)

Dispatch是Desktop app Cowork tab里的持久对话。从手机发消息 → Dispatch决定如何处理 → 如果是开发任务就启动Code session。完成后推送通知到手机。

和Remote Control的区别：
- **Dispatch**: 从手机发新任务 → Desktop启动新session
- **Remote Control**: 从手机/web连入已有session

---

## 六、高级功能

### 18. /loop & /schedule

**Boris:** "/loop — run tasks at intervals (e.g., /loop 5m /babysit). /schedule — schedule Claude to run automatically, up to a week."

**官方文档:** [Scheduled Tasks (local)](https://code.claude.com/docs/en/scheduled-tasks) / [Scheduled Tasks (cloud)](https://code.claude.com/docs/en/web-scheduled-tasks)

**`/loop`** — 本地session内循环执行：
```
/loop 5m check if the deploy finished
/loop 30m /slack-feedback
/loop 20m /review-pr 1234
```
- 默认10分钟间隔，支持 s/m/h/d
- session结束即停止
- 最多50个定时任务

**`/schedule`** — 云端定时任务：
- 在Anthropic基础设施上运行，电脑关机也能跑
- 创建：web UI (claude.ai/code/scheduled)、Desktop、或 `/schedule`
- 频率：每小时/每天/工作日/每周（最短1小时）
- 每次运行：新cloud session + clone repo from GitHub

三个层级对比：
| 类型 | 持久性 | 需要本地机器？ | 适合 |
|------|--------|--------------|------|
| `/loop` | session结束即停 | 是 | 当前任务监控 |
| Desktop scheduled | 跨session持久 | 是 | 需要本地环境的自动化 |
| `/schedule` | 完全独立 | 否 | 定期自动化 |

### 19. /voice

**Boris:** "I do most of my coding by speaking to Claude. You speak 3x faster than you type, and your prompts get way more detailed."

**官方文档:** [Voice Dictation](https://code.claude.com/docs/en/voice-dictation)

- `/voice` 开关push-to-talk
- 默认按键：Space（按住录音）。可在 `~/.claude/keybindings.json` 重新绑定
- 支持20种语言（包括中文、日语、韩语）
- 转录针对编程词汇优化（regex, OAuth, JSON等）
- 可以语音+打字混合输入
- 需要claude.ai账号（不支持API key/Bedrock/Vertex）

### 20. /branch & /btw

**官方文档:** [Commands](https://code.claude.com/docs/en/commands)

**`/branch [name]`** — 分叉当前对话：
- 在当前时间点创建对话分支
- 探索不同方案时不会丢失原始对话

**`/btw <question>`** — 侧问题：
- 在Claude正在工作时问一个快速问题
- 不进入主对话context——独立context执行
- 不会打断当前工作流

### 21. CLI高级标志

**官方文档:** [CLI Reference](https://code.claude.com/docs/en/cli-reference), [Headless](https://code.claude.com/docs/en/headless)

**`--bare`** — 极速启动模式：
- 跳过hooks、LSP、plugins、MCP、skills、auto memory、CLAUDE.md
- 只保留Bash、文件读写工具
- 适合脚本和SDK调用
- 需要 `ANTHROPIC_API_KEY`（跳过OAuth）

**`--add-dir`** — 多目录访问：
```bash
claude --add-dir ../apps ../lib   # 给Claude访问多个目录
/add-dir ../shared                # 会话中添加
```
注意：只授予文件访问，不加载那些目录的配置。

**`--agent`** — 自定义agent运行：
```bash
claude --agent code-reviewer       # 用code-reviewer agent启动session
```

### 22. /statusline

**Boris (团队建议):** "Customize status bars using /statusline."

**官方文档:** [Statusline](https://code.claude.com/docs/en/statusline)

```
/statusline show model name and context percentage with a progress bar
```

Claude自动生成脚本，显示你要的信息。可用数据：model名称、context占用百分比、session花费、工作目录、rate limit状态等。

---

## 总结：Boris的核心原则

| 原则 | 实践 |
|------|------|
| **让Claude能验证自己的工作** | Chrome extension、测试、lint |
| **并行化一切** | Worktrees、多session、/batch |
| **投资可复用的自动化** | Skills、Hooks、CLAUDE.md |
| **保持context聚焦** | Subagents隔离、/clear、单session单任务 |
| **用语音提升prompt质量** | /voice — 说比打字快3x，prompt更详细 |
| **没有唯一正确的用法** | "Experiment to see what works for you" |

<!-- CTA: [placeholder for closing call-to-action] -->
