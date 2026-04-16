---
status: draft
sources:
  - raw/2026-04-16-thariq-claude-code-session-management-1m.md
  - raw/2026-04-09-tw93-claude-code-architecture-governance.md
  - raw/2026-04-08-troyhua-claude-code-7-layers-memory.md
platform: blog
created: 2026-04-16
last-updated: 2026-04-16
tags: [draft]
---

# Claude Code 用得好不好，不在于提示词，而在于每次对话后你做的那个决定

大多数人觉得模型输出不好是因为 context window 不够大，但在 Claude 模型升级到 100 万 token 上下文之后，Anthropic 官方团队在跟大量用户聊完之后发现一个反直觉的事实：窗口越大，用得差的人和用得好的人，差距反而越来越大。

那差距出在哪呢？其实并不是说你的提示词写得好不好，而是你每一次跟 Claude 对话完之后你做的那个决定。

继续发消息？回退重来？压缩上下文？开新 session？交给子 agent？这五个选项里，大多数人只会第一个。这篇文章讲的是另外四个。

---

## 先理解一个底层事实：Context 不是越大越好

在讲实操之前，你需要理解一个底层机制，否则后面的所有建议都像是"别人说了所以我照做"。

### Context rot：越满越笨

Context window 是模型一次能"看到"的全部内容 —— 你的系统提示、对话历史、所有的 tool call 和输出、读过的每个文件。Claude Code 现在有 100 万 token 的窗口。

但 context window 有一个很少人提到的特性：**它会腐烂。** Anthropic 内部把这个现象叫 context rot —— 随着 context 增长，模型的注意力被分散到越来越多的 token 上，旧的、不相关的内容开始干扰当前任务。

简单说：**context 越满，模型越笨。**

这不是 bug，这是 transformer 架构的固有特性。所以 100 万 token 的窗口不意味着你可以无脑塞满。它给你的是更多时间在模型变笨之前主动干预 —— 不是无限的空间。

### 问题不是容量，是噪音

Tw93 写过一篇 280 万播放的 Claude Code 工程指南，里面有一个很精准的判断：**context 的问题通常不是容量问题，是噪音问题。** 有用的信息被无关内容淹没了。

他做了一个拆解，看看你的 context window 还没开始对话就被什么占了：

| 类别 | Token 消耗 | 备注 |
|------|-----------|------|
| 系统指令 | ~2K | 固定 |
| Skill 描述 | ~1-5K | 每个启用的 Skill 始终驻留 |
| MCP 工具定义 | ~10-20K | **最大的隐形杀手** —— 每个 server ~4-6K |
| CLAUDE.md | ~2-5K | 半固定 |
| 内存 | ~1-2K | 半固定 |

5 个 MCP server = 25K token，**还没开始工作就占了 12.5%**。再加上一个 grep 结果灌入几千行，一次大文件读取吃掉 50K —— 你以为有 100 万 token 可用，实际上有效空间一直在被噪音蚕食。

Tw93 的原则很直白：**"偶尔用的东西就不要每次都加载进来。"**

### Anthropic 自己有多认真？7 层系统

如果你觉得"context 管理"听起来像可有可无的优化，看看 Anthropic 自己在做什么。

Troy Hua 逆向工程了 Claude Code 的源代码，发现 Anthropic 在 context 管理上建了整整 **7 层架构** —— 从毫秒级的 token 裁剪到跨 session 的"做梦"式记忆整合：

| 层级 | 机制 | 成本 |
|------|------|------|
| 第 1 层 | Tool 结果写入磁盘，只放 2K 预览进 context | 磁盘 I/O |
| 第 2 层 | 微压缩：自动清理过期的 tool 输出 | 几乎为零 |
| 第 3 层 | Session 记忆：后台 agent 持续整理对话笔记 | 一次 fork |
| 第 4 层 | 完整压缩：总结全部对话历史 | 一次完整 API 调用 |
| 第 5 层 | 自动记忆提取：跨 session 持久化知识 | 一次 fork |
| 第 6 层 | "做梦"：后台跨 session 记忆整合 | 多轮 fork |
| 第 7 层 | 跨 Agent 通信 | 视情况 |

内部把 context window 定义为**"最稀缺的资源"**。每一个架构决策都围绕一个问题：怎么让这个窗口里的每个 token 都有价值。

更直观的数字：在 20 万 token 的 context 下，一次 prompt cache hit 成本 $0.003，一次 cache miss 成本 $0.60 —— **200 倍的差距。** Context 管理不只影响质量，直接影响成本。

如果 Anthropic 自己都要用 7 层系统来管理 context，那你作为用户，至少应该知道你的 5 个选项是什么。

---

## 每次 Claude 回复完，你有 5 个选择

这是这篇文章的核心框架。记住：**每次 Claude 结束一个 turn，你准备发下一条消息的时候，你站在一个决策点上。**

### 选项 1：Continue（继续）

直接发下一条消息。最自然、最常见的动作。

**什么时候该 continue：**
- 当前任务还在继续
- Context 还没有膨胀到影响质量
- 下一步和刚才的工作直接相关

**什么时候不该 continue：**
- Claude 刚才走了一条错误的路（这时候应该 rewind）
- 你要切换到完全不同的任务（这时候应该 clear）
- Context 已经很长了（这时候应该 compact 或 clear）

大多数人每次都 continue —— 这恰恰是 context rot 的来源。

### 选项 2：Rewind（回退）

双击 `Esc`（或运行 `/rewind`）—— 跳回到之前某条消息，从那里重新开始。那条消息之后的所有内容从 context 中移除。

**这是 Anthropic 内部认为最重要的一个习惯。** Thariq 原话："如果我只能选一个习惯来衡量好的 context management，那就是 rewind。"

为什么 rewind 比纠正更好？看一个例子：

1. Claude 读了 5 个文件
2. 尝试了方案 A
3. 方案 A 不行

**大多数人的做法：** 继续发消息 —— "那个方法不行，试试 X 吧。"

问题是：方案 A 的所有尝试过程 —— tool call、输出、错误信息 —— **还留在 context 里**。它们占空间，产生干扰，让后续的输出质量更差。你在用越来越脏的 context 继续工作。

**更好的做法：** Rewind 到 Claude 读完 5 个文件之后那个点，然后重新提问：

> "不要用方案 A，foo 模块没有暴露那个接口 —— 直接用方案 B。"

这样，方案 A 的痕迹被清除了。Context 保持干净。Claude 拿着同样的文件读取结果 + 你的新指导，从一个干净的起点重新开始。

#### 进阶技巧："summarize from here"

如果 Claude 虽然走错了路但学到了有用的东西，你不想完全丢弃那些发现。这时候可以在 rewind 之前让 Claude 运行 "summarize from here" —— 它会把自己学到的东西总结成一段交接信息。

这就像未来的 Claude 给过去的 Claude 写了一张纸条：

> "我试过方案 A，不行。原因是 foo 模块的 API 在 v3 改了。你直接用方案 B，从 bar.ts 的第 42 行开始。"

然后你 rewind，把这段总结粘贴到新的 prompt 里。干净的 context + 完整的经验。

### 选项 3：Clear（开新 Session）

`/clear` —— 完全开一个新 session。你自己写一段简述，把你认为重要的信息带过去。

**什么时候用 clear：**
- 切换到完全不同的任务
- 当前 session 已经很长，你很清楚接下来要做什么
- 你尝试了 compact 但效果不好

Clear 比 compact 费事 —— 你需要自己写一段简述（"我们在重构 auth 中间件，约束是 X，相关文件是 A 和 B，我们已经排除了方案 Y"）。但它的好处是 **context 完全是你决定的内容**，没有模型替你做的有损判断。

**实操建议：** 把 clear 想象成给下一个 Claude 写一封 brief。你雇了一个新的高级工程师，他什么都不知道。你需要用最少的话让他能立刻开始工作。

### 选项 4：Compact（压缩）

`/compact` —— 让 Claude 总结当前 session 的对话历史，用总结替换掉原始内容。

这是一个**有损操作** —— 你在信任 Claude 来决定什么是重要的。好处是你不用自己写任何东西，Claude 可能比你更全面地保留细节。坏处是它可能丢掉你后面需要的东西。

**关键技巧：你可以给 compact 加方向。**

```
/compact focus on the auth refactor, drop the test debugging
/compact 保留数据库设计决策，删掉之前的调试过程
```

这让 Claude 的总结有了重点，大幅减少信息丢失的风险。

#### Compact vs Clear 的本质区别

| | Compact | Clear |
|---|---------|-------|
| 谁决定保留什么 | Claude（有损） | 你（精准） |
| 你的工作量 | 零 | 写一段简述 |
| 风险 | 可能丢掉你后面需要的东西 | 可能忘记写某些重要信息 |
| 适合场景 | 同一任务减负 | 切换任务方向 |

#### 什么导致 Bad Compact？

这是 Thariq 文章中最深刻的一个洞察。

Bad compact 发生在**模型无法预测你接下来要做什么**的时候。比如：

1. 你花了很长时间 debug 一个问题
2. Autocompact 自动触发，它总结了 debugging 过程
3. 你的下一条消息是："现在去修 bar.ts 里那个之前看到的 warning"
4. 但因为 session 全是 debugging 内容，**那个 warning 在总结时被丢掉了**

更要命的是：**context rot 意味着模型在需要做 compact 的时候，恰恰处于它最不聪明的状态。** Context 满了 → 注意力分散 → 总结质量差 → 丢掉重要信息 → 后续工作出错。

**实操建议：**
1. 不要等 autocompact 触发 —— 100 万 token 给了你余裕，**在 context 还健康的时候主动 compact**
2. Compact 时附带方向说明，告诉 Claude 接下来你打算做什么
3. 如果你要切换任务方向（从 debug 转到新功能），**用 clear 而不是 compact**

### 选项 5：Subagent（子 Agent）

让 Claude 开一个独立的子 agent，在它自己的 context window 里完成一块工作，然后只把最终结论返回给你的主 session。

很多人以为 subagent 是为了并行工作。**但它的核心价值是 context management。**

Subagent 有自己独立的 context window。它可以做大量的工作 —— 读十几个文件、跑各种工具、反复尝试 —— 但这些中间过程**不会污染你的主 session**。你的主 session 只收到最终的结论报告。

**心理测试：** 问自己一个问题 —— "我还需要这些 tool output 吗，还是只需要结论？" 如果只需要结论 → 用 subagent。

#### 三个实用场景

**验证类：**
> "开一个 subagent 根据这个 spec 文件验证我刚才做的工作是否正确"

Claude 开一个子 agent → 它读 spec、读你的代码、逐条对比 → 只返回"通过/不通过 + 具体问题" → 你的主 session context 几乎没有增长。

**调研类：**
> "开一个 subagent 去读另一个代码库，总结它是怎么实现 auth flow 的，然后你按同样的方式实现"

子 agent 读了一整个代码库（可能消耗大量 token） → 总结成几段话返回 → 你的主 session 拿着简洁的总结继续工作。

**衍生类：**
> "开一个 subagent 根据我的 git changes 写这个功能的文档"

文档写作需要读大量 diff → 这些 diff 留在子 agent 的 context 里 → 只返回写好的文档。

---

## 决策流程图

每次 Claude 回复完，问自己：

```
Claude 刚回复完 →
  ├── 刚才做错了？
  │     → Rewind（esc esc）
  │
  ├── 要切换到完全不同的任务？
  │     → Clear（/clear + 写简述）
  │
  ├── 同一任务，但 context 太长了？
  │     → Compact（/compact + 方向说明）
  │
  ├── 接下来的工作会产生大量中间输出？
  │     → Subagent（"开一个 subagent 去..."）
  │
  └── 以上都不是？
        → Continue（直接发消息）
```

**默认应该是思考，不是 continue。** 每次停下来 2 秒想一下：我是应该继续，还是有更好的选择？这个习惯就是好用户和普通用户的区别。

---

## 实操清单

**立刻可以做的：**
- [ ] 记住快捷键：`esc esc` = rewind
- [ ] 下次 Claude 做错了，不要说"那个不行"，而是 rewind 到出错前重新 prompt
- [ ] 检查你启用了多少个 MCP server —— 不常用的关掉
- [ ] 在 CLAUDE.md 里加 Compact Instructions，告诉 Claude 压缩时保留什么

**养成习惯：**
- [ ] 每次 Claude 回复完，停 2 秒想：continue 还是其他 4 个选项？
- [ ] Session 变长后，主动 `/compact` + 方向说明，不要等 autocompact
- [ ] 要切方向时用 `/clear`，不要用 `/compact`
- [ ] 预见大量中间输出时，主动提议用 subagent

**进阶配置：**
```markdown
## Compact Instructions（加到你的 CLAUDE.md）
压缩时按优先级保留：
1. 架构决策（绝不能丢）
2. 已修改的文件和关键变更
3. 当前验证状态
4. 待办事项和回退备注
5. Tool 输出（可以删除，只保留通过/失败状态）
```

---

## 一句话总结

100 万 token 的 context window 不是让你不用管 context 了 —— 是让你有了更多时间在质量下降之前做出正确的选择。而那个选择，就发生在每次 Claude 回复完之后的那 2 秒钟。

<!-- CTA: 试试看：下次 Claude 做错了，不要纠正，rewind 到出错前重新 prompt。你会感受到区别。 -->

---

*本文基于 Anthropic 官方团队 Thariq 的 session management 指南，结合 Tw93 的 context 噪音治理框架和 Troy Hua 对 Claude Code 7 层记忆系统的逆向工程研究。*
