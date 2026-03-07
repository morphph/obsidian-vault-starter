# Setup Guide

## 10 分钟快速上手

### 1. 把这个 vault starter 放到你想要的位置
```bash
# 解压后移动到你想要的目录
mv obsidian-vault-starter ~/obsidian-vault
```

### 2. 在 Obsidian 中打开
- 打开 Obsidian → "Open folder as vault" → 选择 `~/obsidian-vault`

### 3. 安装 Obsidian CLI（v1.12.4+，免费）
- 确保 Obsidian 更新到 v1.12.4+（Settings → About → Check for updates）
- Settings → General → 找到 "Command line interface" → 点 "Register CLI" → 开启
- 打开一个**新的**终端窗口测试：
  ```bash
  obsidian version
  ```
- 如果报 "command not found"，添加到 PATH：
  ```bash
  # macOS
  echo 'export PATH="$PATH:/Applications/Obsidian.app/Contents/MacOS"' >> ~/.zprofile
  source ~/.zprofile
  ```

### 4. 安装官方 Obsidian Skills
```bash
cd ~/obsidian-vault/.claude/skills
git clone https://github.com/kepano/obsidian-skills.git
```

### 5. 编辑 CLAUDE.md
打开 `CLAUDE.md`，修改 "Repo Locations" 部分的路径，确保指向你实际的项目目录。

### 6. 启动 Claude Code
```bash
cd ~/obsidian-vault
claude
```

试试：
- `/context` — 加载所有项目上下文
- `/log` — 记录今天的 build log
- `/sync-project all` — 从 repo 拉取最新信息

### 7. 填充项目上下文文件
打开 `projects/` 下的每个文件，填写 `[Write: ...]` 部分。
这是最重要的一步——花 30 分钟认真写。

---

## 日常使用节奏

| 频率 | 做什么 | 命令 | 耗时 |
|------|--------|------|------|
| 每天 | 记录 build log | `/log` | 5 min |
| 每个 session 开始 | 加载上下文 | `/context` | 30 sec |
| 每周 | 想法生成 + 毕业 | `/ideas` → `/graduate` | 20 min |
| 每周或按需 | 同步 repo 信息 | `/sync-project all` | 2 min |
| 每月 | 浮现隐藏模式 | `/emerge` | 15 min |
| 需要灵感时 | 跨域连接 | `/connect X Y` | 5 min |

详细命令说明见 `COMMANDS.md`。

---

## 文件结构

```
CLAUDE.md              ← Claude Code 的说明书（先编辑这个）
COMMANDS.md            ← 命令速查表
SETUP.md               ← 本文件
daily/                 ← 每日 build log（一天一个文件）
projects/              ← 项目上下文（auto-synced + human 双分区）
  loreai-context.md
  blog2video-context.md
ideas/                 ← "毕业"后的独立想法
references/            ← 工具、策略、人物笔记
agent-output/          ← agent 生成的报告（暂存区）
.claude/
  commands/            ← 自定义 slash commands
    log.md             ← /log — 带 auto-link 的 build log 记录
    context.md         ← /context — 分级上下文加载
    sync-project.md    ← /sync-project — 从 repo 同步
    ideas.md           ← /ideas — 跨项目想法生成 ⚠️重量级
    connect.md         ← /connect X Y — 跨域连接 ⚠️中量级
    emerge.md          ← /emerge — 浮现隐藏模式 ⚠️重量级
    graduate.md        ← /graduate — 想法毕业
  skills/              ← Agent skills（安装 kepano/obsidian-skills 到这里）
```

---

## 两个工作台

你有两个工作环境，用途完全不同：

**项目工作台** — 写代码时用
```bash
cd ~/Desktop/Project/loreai-v2 && claude
# Claude Code 看到：完整 codebase
# 适合：写代码、debug、实现功能
```

**大脑工作台** — 思考规划时用
```bash
cd ~/obsidian-vault && claude
# Claude Code 看到：所有项目上下文 + 你的思维历史
# 适合：规划、复盘、跨项目分析、发现模式
```

**循环：** vault 告诉你做什么 → repo 里去做 → /log 把发现带回 vault → vault 基于新信息再指引下一步。

---

## 常见问题

**好几天没写 build log 了** → 正常。回来继续就行。一周写 3 天已经够用。

**不知道该链接什么** → 问自己：这个东西会在其他笔记里再出现吗？会就链接，不确定也链接（零成本），确定不会就别管。

**项目上下文文件过时了** → 跑 `/sync-project` 更新技术部分，手动更新战略部分。每月一次足够。

**/ideas 给的建议太泛** → vault 还不够丰富。继续写 build log，3-4 周后会有明显改善。

**重量级命令耗时长** → 正常。Vin 的命令也需要 5-10 分钟。输出质量和上下文量成正比。

**想在 Obsidian 里嵌入终端** → 安装 Terminal 插件（社区插件搜 "terminal"），在里面运行 claude。效果和外部终端完全一样，只是更方便看笔记。
