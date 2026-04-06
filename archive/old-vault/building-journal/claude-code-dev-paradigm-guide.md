---
source: agent
date: 2026-03-11
type: 指南
status: ready
topic: Claude Code 开发范式
---

# Claude Code 开发范式指南

> 基于 Claude Code 最新能力（Agent Teams、Worktree、Custom Subagents、Headless Mode）的功能开发决策框架。
> 核心理念：功能规模决定流程重量，依赖深度决定并行模式。

---

## 一、功能规模 → 开发流程

不是所有功能都需要同样的流程。判断标准是 **agent 跑偏后的返工成本**。

### 小功能：直接开发

**特征**：半小时内能完成，边界清晰，改动集中在少数文件。

**典型场景**：修 bug、加一个 API endpoint、调 UI 样式、写工具函数。

**做法**：直接用自然语言 prompt 让 Claude Code 执行，看 diff 确认即可。就算 agent 第一次没做对，纠正成本也很低。

```bash
# 直接开发，不需要 spec
claude "修复 /api/blog 返回 500 的问题，错误日志显示是 date parsing 失败"
```

### 大功能：Spec-Driven Development（先写方案，再让 Agent 执行）

**特征**：满足以下任意一条，就应该先写 spec。

| 判断条件 | 原因 |
|---------|------|
| 跨多个文件或模块 | agent 对某个模块设计理解错误会导致连锁返工 |
| 涉及现有代码重构 | agent 不知道你想保留什么、替换什么 |
| 需要 headless 或长时间自主执行 | 你不在旁边时 spec 是 agent 唯一的指南针 |
| 有外部 API 集成 | endpoint、参数、错误处理如果不写死 agent 会自己猜 |
| 预计开发时间 > 1 小时 | 投入 30 分钟写 spec 的 ROI 为正 |

**做法**：先与 Claude 脑暴技术方案 → 写成 spec 文件 → 让 agent 按 spec 执行。

```bash
# 按 spec 执行
claude --dangerously-skip-permissions \
  -p "按照 specs/blog-pipeline.md 实现，每完成一个 step 跑 vitest 验证"
```

---

## 二、Spec 的六层结构

一份好的 spec 应该让一个对项目完全没有上下文的 agent 读完后能独立完成开发，不需要回来问问题。

### 第 1 层：目标与背景（Why & What）

解决"为什么做"和"做成什么样"。把关键约束讲清楚。

```markdown
## 目标
基于一个 topic 关键词，通过 Gemini Deep Research 做深度调研，
生成一篇高质量的中英双语博文，自动发布到 LoreAI v2 博客系统。
目标：每篇文章在 SEO 上竞争该 topic 的 top ranking。

## 约束
- 输出语言：英文 + 中文
- 发布方式：自动写入数据库，通过现有 blog API 访问
- 质量标准：英文 > 1500 词，中文 > 1000 字
```

### 第 2 层：技术方案（Technical Design）

Spec 的核心。要写到 **agent 不需要做架构决策** 的粒度。

**反面例子**（太模糊，agent 会自由发挥）：
```markdown
实现一个博客生成系统，调用 Gemini 做调研后生成文章。
```

**正面例子**（足够具体，agent 只需要写代码）：
```markdown
## Pipeline 步骤

### Step 1: Topic Research
- 调用 Gemini 2.5 Pro 的 grounding with Google Search API
- 输入：topic string
- 输出：structured research report，schema 如下：
  { sources: Array<{url, title, summary}>, key_findings: string[], ... }
- 超时处理：30s timeout，重试 2 次
- 缓存：同一 topic 24h 内复用缓存结果

### Step 2: Content Generation
- 调用 Claude Sonnet，传入 Step 1 的 research report
- System prompt 在 prompts/blog-writer.md
- 输出 schema：{ title, content_en, content_zh, metadata }
```

### 第 3 层：文件规划（File Structure）

直接告诉 agent 代码放哪里。没有这个，agent 经常会创建跟现有代码风格不一致的目录结构。

```markdown
## 文件规划

新增文件：
- src/lib/blog-pipeline/research.ts     // Gemini Deep Research 调用
- src/lib/blog-pipeline/generator.ts    // 博文生成逻辑
- src/lib/blog-pipeline/types.ts        // 类型定义
- src/lib/blog-pipeline/cache.ts        // 调研结果缓存
- prompts/blog-writer.md                // 生成 prompt

修改文件：
- src/lib/db/schema.ts                  // 新增 blog_drafts table
- src/app/api/blog/route.ts             // 新增 API endpoint

不要动的文件：
- src/lib/seo/*                         // SEO 模块本次不改
- src/components/*                      // UI 组件本次不改
```

### 第 4 层：验收标准（Acceptance Criteria）

分两种：agent 能自动验证的，和需要人工 review 的。

```markdown
## 自动化验收（vitest）

1. generateBlogPost("AI agents 2026") 返回包含
   title, content_en, content_zh, metadata 的对象
2. content_en 字数 > 1500，content_zh 字数 > 1000
3. metadata 包含 seo_title, description, keywords
4. 写入数据库后 GET /api/blog/[slug] 正确返回
5. 所有现有 vitest 测试仍然通过（不能 break 现有功能）

## 人工验收（开发完成后人工检查）

- [ ] 生成的文章语言自然，不像 AI 直接输出
- [ ] Gemini 调研结果的 sources 可访问、相关性高
- [ ] 中英文内容在语义上一致，不是机械翻译
```

### 第 5 层：自主执行配置（Autonomous Execution）

专门针对 headless mode 的 agent 行为规则。本质上是定义 **modify → evaluate → keep/discard 的循环规则**。

```markdown
## 执行配置

- 每完成一个 Step，运行 `npm run test` 验证
- 如果测试失败，分析错误原因并修复，最多重试 3 次
- 如果 3 次后仍失败：
  - git stash 当前变更
  - 在 specs/blog-pipeline-blockers.md 记录：
    失败的 step、错误信息、已尝试的修复方案
  - 停止执行，等待人工介入
- 每个 Step 完成且测试通过后，git commit
- commit message 格式：feat(blog-pipeline): Step N - 简要描述
```

### 第 6 层：边界声明（Out of Scope）

防止 agent "好心办坏事"，顺手改了你不想动的东西。

```markdown
## 不在本次范围内

- 不修改现有 UI 组件
- 不更改部署配置（vercel.json 等）
- 不升级任何依赖包版本
- 不重构现有的 newsletter pipeline
- 不添加用户认证逻辑
```

---

## 三、并行开发模式选择

当有多个大功能需要同时开发时，根据 **功能之间的依赖深度** 选择并行模式。

> **关键前提**：必须先把两个功能的 spec 都写完，才能判断依赖深度，才能选择并行模式。不要在 spec 完成前就决定用哪种模式。

### 模式 A：Git Worktree 并行（依赖浅）

**适用条件**：两个功能之间只共享数据模型或 types，不改同一批业务逻辑文件。

**原理**：每个 worktree 是独立的工作目录和分支，共享 git history，文件系统完全隔离。

**工作方式**：

```
main (先 commit 共享契约层：shared types, DB migration)
  ├── worktree 1: feature-blog-pipeline（独立开发）
  └── worktree 2: feature-seo-optimization（独立开发）
```

```bash
# 先在 main 上提交共享层
# 然后两个终端同时跑：
claude --worktree feature-blog-pipeline --dangerously-skip-permissions \
  -p "按照 specs/blog-pipeline.md 实现"

claude --worktree feature-seo-optimization --dangerously-skip-permissions \
  -p "按照 specs/seo-optimization.md 实现"
```

**优势**：完全隔离，互不干扰，各自可以长时间 headless 运行。

**劣势**：如果两边都在改同一块代码，合并时会有逻辑冲突（不只是 git conflict，而是逻辑不兼容）。

**合并策略**：侵入性小的功能（新增为主）先合，重构类功能后合。合并后跑完整测试。

### 模式 B：Agent Teams 协作（依赖中等）

**适用条件**：两个功能有上下游关系（如 A 的输出是 B 的输入），或需要改同一些模块但改的部分不同。

**原理**：一个 lead agent 统筹多个 teammate，teammate 之间能互相通信、共享发现、协调接口。每个 teammate 有独立的 context window。

**工作方式**：

```bash
# 开启 Agent Teams
export CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1

# 自然语言描述团队结构
claude "创建一个 agent team 来并行开发两个功能：
- Teammate 'blog': 按 specs/blog-pipeline.md 实现博客生成 pipeline
- Teammate 'seo': 按 specs/seo-optimization.md 实现 SEO 优化
- 两个 teammate 在修改共享模块时互相通信协调
- 用 worktree 隔离各自的文件修改
要求 plan approval，每个 step 完成后跑测试"
```

**优势**：teammate 之间能实时协调，比如 blog teammate 定义了输出格式，seo teammate 可以立即知道并适配。

**劣势**：token 消耗高（每个 teammate 是独立 context window，3 个 teammate ≈ 3-4x 单 session），有协调开销。

**适用场景举例**：Blog Pipeline 生成的文章结构需要被 SEO 模块索引和优化，两边需要协商内容 schema。

### 模式 C：顺序开发（依赖深）

**适用条件**：两个功能大量修改同一批文件，或者后一个功能的设计严重依赖前一个功能的实现结果。

**工作方式**：

```
1. 先完成 Feature A → 合入 main → 跑完整测试
2. 基于最新 main 开发 Feature B
```

**优势**：错误率最低，不会出现合并冲突或逻辑不兼容。

**劣势**：最慢，两个功能无法并行。

**适用场景举例**：SEO 优化要彻底重写的 pipeline 恰好也是 Blog Pipeline 要接入的，不确定改完之后接口长什么样。

### 选择决策树

```
两个功能的 spec 都写完了？
├── 否 → 先写完 spec，再做决策
└── 是 → 分析两个 spec 修改的文件列表
         ├── 基本没有重叠文件 → 模式 A（Worktree 并行）
         ├── 有部分重叠，但改的是不同部分 → 模式 B（Agent Teams）
         └── 大量重叠，改同一块逻辑 → 模式 C（顺序开发）
```

---

## 四、单功能内部的并行加速

不管用哪种跨功能并行模式，单个大功能内部也可以并行化。

### 用 Agent Teams 拆分角色

适合功能内部有明确的角色分工（如前端/后端/测试）：

```bash
claude "创建 agent team 实现 blog pipeline：
- Teammate 'researcher': 实现 Gemini Deep Research 集成层
- Teammate 'writer': 实现博文生成逻辑
- Teammate 'tester': 持续运行测试验证
三个 teammate 用 worktree 隔离"
```

### 用 Custom Subagent 拆分阶段

适合有清晰的先后阶段（如先分析再实现）：

```yaml
# .claude/agents/seo-analyzer.md
---
name: seo-analyzer
description: 分析现有 SEO pipeline 并生成优化方案
tools: Read, Grep, Glob, WebSearch, WebFetch
model: opus
isolation: worktree
---
分析当前 SEO 和 AEO pipeline 的完整实现，输出优化方案到 specs/seo-analysis.md

# .claude/agents/seo-implementer.md
---
name: seo-implementer
description: 基于分析结果实现 SEO 优化
tools: Read, Write, Edit, Bash, Glob, Grep
model: sonnet
isolation: worktree
---
基于 specs/seo-analysis.md 实现具体优化
```

### Subagent vs Agent Teams 选择

| | Subagent | Agent Teams |
|---|---------|-------------|
| 通信方式 | 只能报告回主 agent | teammate 之间可以互相通信 |
| 生命周期 | 短任务，完成即销毁 | 长运行，持续协作 |
| 适合场景 | 独立的子任务（搜索、分析、测试） | 需要协调的并行工作（前后端联调） |
| token 成本 | 较低 | 较高（每个 teammate 独立 context） |

---

## 五、关键实操配置

### 共享契约层（跨功能并行的前置步骤）

在任何并行开发开始前，先在 main 上提交两个功能共享的基础设施：

```markdown
## 契约层 checklist
- [ ] 共享 types/interfaces（src/shared/types.ts）
- [ ] 数据库 schema 变更（migration 文件）
- [ ] CONTRACTS.md（记录两个功能的接口约定）
- [ ] 两个功能各自的目录结构已在 spec 中定义
```

### 定期同步机制

并行开发时创建 custom command 防止两个分支漂移：

```markdown
# .claude/commands/sync-features.md

## Instructions
1. 将 main 的最新变更 rebase 到当前功能分支
2. 运行完整测试套件
3. 检查当前变更是否破坏 CONTRACTS.md 中的接口约定
4. 如发现接口需要变更，输出 contract-change-request.md
5. 总结同步状态
```

执行频率：每天在每个 worktree 至少跑一次。

### Headless 执行的安全网

```markdown
## Spec 中的执行配置模板

执行模式：headless（--dangerously-skip-permissions）
质量门：vitest 测试套件
循环规则：
  - 每个 step 完成后跑测试
  - 失败 → 分析 → 修复 → 重新测试（最多 3 轮）
  - 3 轮后仍失败 → stash 变更 → 记录 blockers → 停止
  - 通过 → git commit → 进入下一个 step
回滚能力：每个 step 一个 commit，可以 git revert 任意 step
```

### Token 消耗管理

| 模式 | 相对成本 | 备注 |
|------|---------|------|
| 单 session | 1x | 基准 |
| 2 个 worktree 并行 | 2x | 两个独立 session |
| Agent Teams (3 teammates) | 3-4x | 每个 teammate 独立 context |
| Worktree + 内部 Agent Teams | 6-8x | 最大并行度 |

建议：teammate 默认用 `model: sonnet`，只在需要深度架构决策时用 `model: opus`。

---

## 六、完整工作流总结

```
                     ┌─────────────────┐
                     │  功能需求出现    │
                     └────────┬────────┘
                              │
                     ┌────────▼────────┐
                     │  评估功能规模    │
                     └────────┬────────┘
                              │
                 ┌────────────┴────────────┐
                 │                         │
         < 30 分钟可完成            > 1 小时 / 跨模块 /
         边界清晰                  外部集成 / 要跑 headless
                 │                         │
         ┌───────▼───────┐        ┌────────▼────────┐
         │  直接 prompt   │        │  先写 Spec       │
         │  Claude Code  │        │  （6 层结构）     │
         └───────────────┘        └────────┬────────┘
                                           │
                                  ┌────────▼────────┐
                                  │  单功能 or 多功能？│
                                  └────────┬────────┘
                                           │
                              ┌────────────┴────────────┐
                              │                         │
                         单个大功能               多个大功能并行
                              │                         │
                     ┌────────▼────────┐       ┌────────▼────────┐
                     │  直接 headless   │       │  写完所有 spec   │
                     │  按 spec 执行    │       │  分析依赖深度    │
                     └─────────────────┘       └────────┬────────┘
                                                        │
                                           ┌────────────┼────────────┐
                                           │            │            │
                                      依赖浅        依赖中等       依赖深
                                           │            │            │
                                     Worktree      Agent Teams    顺序开发
                                      并行           协作
```
