---
type: source-summary
created: 2026-05-12
last-updated: 2026-05-12
sources:
  - raw/2026-04-21-garry-tan-skillify-manifesto.md
tags: [wiki, source, garry-tan, skillify, agentic, testing]
---

# Source: Garry Tan — The Skillify Manifesto (How to really stop your agents from making the same mistakes)

## Summary
Fifth piece in [[garry-tan|Garry Tan]]'s agent-building series (2026-04-21, **916.7K views, 4,824 bookmarks**). **The operational manifesto for [[skillify-meta-skill|/skillify]]**. Opens with a $160M shot at LangChain ("gym membership without a workout plan"), then uses two concrete production failures (calendar trip, "28 minutes" timezone math) to walk through **the 10-step Skillify Checklist** — the actual quality gates `gbrain doctor` enforces on every new skill. Headline: "**A feature that doesn't pass all ten is not a skill. It's just code that happens to work today.**" Most operationally dense piece in the entire series.

## Source
- **URL:** https://x.com/garrytan/status/2046876981711769720
- **Posted:** 2026-04-21 (approx)
- **Engagement (at fetch):** 916.7K views · 4,824 bookmarks · 1,651 likes · 90 replies
- **Fetch method:** Playwright MCP

## 要点解读

### 1. **LangChain 比喻 —— "$160M 给了你 gym 会员但没给 workout plan"**
开篇直接点名 LangChain（$160M 估值、LangSmith 测试平台、trajectory evals、LLM-as-judge）：
> "**They have the pieces. Credit where it's due. But pieces aren't a practice.** LangChain gives you testing. It never tells you what to test, in what order, or when you're done."

缺失的是**有 opinion 的工作流**：
> "There's no opinionated workflow that says, in order: **this failure happened → now write the deterministic code → now add a resolver trigger → now eval the resolver → now audit for duplicates.** That loop doesn't exist."

**"Most AI agent 'reliability' is vibes-based."** Prompt tweaks、"please don't hallucinate" 咒语、对话一复杂就退化。

### 2. **两个生产 failure，同样的形状**

**Failure 1: Trip Already in Database**
问 OpenClaw 10 年前一次新加坡旅行。Agent 调 live calendar API（被 block） → 邮件搜索（noisy） → 又调 API → 5 分钟后才搜本地知识库 → **答案一直在本地的 3,146 个 calendar 文件里**，一个 grep 就能找到。

**Failure 2: "28 minutes"**
Agent 说"下个会议 28 分钟后" → 实际 88 分钟。Agent 在脑子里做 UTC→PT 时区运算，错了正好一小时。`context-now.mjs` 脚本早就存在（50ms 跑完，零歧义），**agent 就是没运行它**。

**两个 failure 同一个 bug 模式：**
> "**The agent had the right tool and chose cleverness instead of discipline. The wrong thing happened in the wrong machine space.**"

即 [[latent-vs-deterministic|latent vs deterministic]] 错位 —— deterministic 工作（grep、减时间戳）被丢进 latent 空间。

### 3. **"模型自己写约束它的代码" —— 整篇最深的洞察**
> "**Here's the thing that makes this work: the agent itself wrote the deterministic script.** The skill file (markdown, living in latent space) told the agent how to fix the problem. The agent read the skill, understood that calendar search is deterministic work, and generated a script to handle it."

通用机制：
> "**This is the loop that makes the whole architecture work: the latent space builds the deterministic tool, then the deterministic tool constrains the latent space.**"
>
> "**The model's intelligence created the constraint that prevents the model from being stupid.**"

这是个非常深的递归 —— LLM 用判断力造出"约束未来 LLM 判断力"的工具。

### 4. **10 步 Skillify Checklist ⭐⭐⭐ —— 这是这篇文章的核心 deliverable**

```
□ 1. SKILL.md            — 契约（name, triggers, rules）
□ 2. Deterministic code  — scripts/*.mjs（代码能做的事不用 LLM）
□ 3. Unit tests          — vitest
□ 4. Integration tests   — live endpoints
□ 5. LLM evals           — quality + correctness
□ 6. Resolver trigger    — entry in AGENTS.md
□ 7. Resolver eval       — verify trigger 真的 route 对了
□ 8. Check-resolvable + DRY audit
□ 9. E2E smoke test
□ 10. Brain filing rules
```

> "**A feature that doesn't pass all ten is not a skill. It's just code that happens to work today.**"

**关键的 step-by-step 细节（生产实测）：**
- Step 3：他有 **179 unit tests 跨 5 个 suite，2 秒跑完**
- Step 5 最高产的 eval 启发：**"search your conversation history for when you said 'fucking shit' or 'wtf'. Those are the test cases you're missing."**（最诚实的 eval heuristic）
- Step 7：50+ resolver eval 测试用例，结构化测 + LLM-routing 双测
- Step 8：check-resolvable 第一次跑找出 **40+ skill 里 6 个不可达（15% dark capability）**；现在 `gbrain doctor --fix` 每周跑

### 5. **"Skillify" 已经变成动词 —— 真实日常工作流**
检查清单从 failure-response protocol 变成了 build-everything 的方式。Garry 的实际工作流：跟 agent 自然语言聊 → 解决问题 → 试一下 → 工作了 → 说一个词 "skillify"。

例子（直接抄他的原话）：
- "hot damn it worked. can you remember this as a webhook skill and skillify it... DRY it up too"
- "we should actually remember this as a skill whenever anything in openclaw needs a headless browser! ... skillify it!"
- "can we make a skill that says whenever you send me a link you have to curl it yourself to make sure the endpoint is open and the tunnel works? skillify it!"
- "Here is one regular skill I need you to write. It's the calendar check skill. Tomorrow I have a double booked 11am. Make a skill, make it deterministic..."

> "**One sentence. Code, skill, tests, resolver entry, reachability audit. The whole 10-step checklist in one breath.** ... I couldn't live without it."
>
> "I don't write specs. I don't file tickets. **I talk to my agent, we solve the problem together, and then the solution becomes a skill that the agent can use forever without me.**"

### 6. **Hermes Agent 缺什么 —— `skill_manage` 没有 verification 层**
Hermes 有一个 `skill_manage` tool 让 agent 自己创建/修改/删除 skill（procedural memory），还有 progressive disclosure 和 bounded MEMORY.md。**Smart design，但没有测试层：**
- ❌ 没 unit tests 测 deterministic code
- ❌ 没 resolver evals 测 routing
- ❌ 没 check-resolvable 找 dark skill
- ❌ 没 DRY audit 抓重复
- ❌ 没每日健康检查

**3 个会累积的 failure mode：**
- 周一造 `deploy-k8s`，周四造 `kubernetes-deploy`（不同对话）→ **ambiguous routing**
- Skill 写时完美，6 周后上游 API 改了 → **silently 返回垃圾** 直到人发现
- Auto-created skill 触发词太弱从不匹配 → **orphan**，吃 token 不工作

> "**Hermes handles creation beautifully. GBrain handles verification. You need both.**"

### 7. **整个 thesis（最后一句太狠了，值得记）**
> "In a healthy software engineering team, every bug gets a test. That test lives forever. The bug becomes structurally impossible to recur. **AI agents should work the same way.**"
>
> "**The agent I work with a year from now will be shaped by every mistake it made in the year before. That's not a nice-to-have. That's the whole thesis.**"

## Pages updated from this source
- [[skillify-meta-skill]] — **major expansion**: full 10-step checklist + the two production failures (calendar-recall, context-now) as canonical case studies + "skillify as a verb" daily workflow + Hermes vs GBrain comparison
- [[trigger-evals]] — 50+ test-case eval suite example; "fucking shit / wtf" search heuristic
- [[check-resolvable]] — `gbrain doctor --fix` weekly run; DRY audit 4-skill lane matrix; 3 specific checks (manifest ↔ resolver, callable scripts, no overlapping triggers)
- [[latent-vs-deterministic]] — calendar-recall + 28-min case studies; "latent space builds the deterministic tool that constrains the latent space" recursive insight
- [[garry-tan]] — 5th article in series with bookmark count + LangChain critique
- [[index]], [[log]]

## Connections
- Related: [[garry-tan]], [[skillify-meta-skill]], [[trigger-evals]], [[check-resolvable]], [[latent-vs-deterministic]], [[resolvers]], [[verification-loops]], [[gbrain]], [[openclaw]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-05-12 | raw/2026-04-21-garry-tan-skillify-manifesto.md | Initial creation |
