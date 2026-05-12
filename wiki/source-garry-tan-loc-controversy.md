---
type: source-summary
created: 2026-05-12
last-updated: 2026-05-12
sources:
  - raw/2026-04-18-garry-tan-loc-controversy.md
tags: [wiki, source, garry-tan, productivity, gstack]
---

# Source: Garry Tan — On the LOC Controversy

## Summary
Third piece in [[garry-tan|Garry Tan]]'s agent-building series (2026-04-18, **134.9K views**). Defends the "600,000 lines in 60 days" claim against critics by **doing the math honestly**: computes logical SLOC, applies a 2x AI-verbosity deflation, and shows the multiple is still 408× over his 2013 part-time baseline. Pairs the number with **quality data**: 2.0% revert rate, 6.3% post-merge fix rate, 2,000+ tests, slop-scan score cut by 62% in one session. Production stats for [[gstack]] at the time: **75K stars, 14,965 unique installs, 305,309 skill invocations, 95.2% success rate, ~7K weekly active users.** Headline thesis: **"engineers can fly now"** — one engineer in 2026 has the output of a ~100-person team in 2013.

## Source
- **URL:** https://x.com/garrytan/status/2045404377226285538
- **Posted:** 2026-04-18 07:29 UTC
- **Engagement (at fetch):** 134.9K views · 365 bookmarks · 274 likes · 41 replies
- **Fetch method:** Playwright MCP

## 要点解读

### 1. **三支 LOC 批评 —— 哪一支真正成立**
有人发推说他 60 天 ship 了 60 万行代码，被骂得很惨。Garry 拆解了三支批评：

- **支 1：LOC 不衡量质量** ✅ 对，永远对。Dijkstra 1988 就说"LOC 是 lines spent 不是 lines produced"。
- **支 2：AI 让 LOC 虚高** ✅ 对。LLM 默认写 verbose 代码、多防御性检查、多注释。
- **支 3：所以炫耀 LOC 很可耻** ❌ 这一支跑偏了。

**关键洞察：如果原始 LOC 被某个系数 inflated，那诚实的做法是 compute the deflation 然后报 deflated number。** 这就是这篇做的事。

### 2. **两层 deflation 之后还是 408×**
- 原始 NCLOC (non-blank, non-comment)：**11,417 行/天** (2026)
- 应用 2× AI 啰嗦系数（这是上界，实测 1.3-1.8×）：**5,708 logical lines/day**
- 对比 2013 兼职 baseline 14 lines/day：**仍然 408×**

如果你嫌 2013 baseline 太低（兼职 + 全职 YC），按 50/天算（3.5× 提升），multiple 仍然 **228×**。

如果你坚持 5× deflation（毫无依据但也行）：**162×**。10× 病态：**81×**。

> "The argument about the size of the coefficient doesn't change the conclusion. The number is large regardless."

### 3. **质量数据 —— 这是文章的真正杀手锏**
被 Sentry 创始人 David Cramer 质问"你 bug 率呢"之后给的硬数据：

| 指标 | 数据 | 解读 |
|------|------|------|
| Revert rate | 2.0% (7/351) | 成熟 OSS 区间 1-3%，正常 |
| Post-merge fix rate | 6.3% | 健康；0% 反而意味着没在抓自己的错 |
| Tests | 1月份 ~100 → 现在 **2,000+** | 100% critical-path coverage |
| Slop-scan score (Ben Vinegar 的工具) | 初始 5.24（最差）→ refactor 后**降 62%**（一次 session）|

**关键洞察（这条最有迁移价值）：**
> "Testing at multiple levels is what makes AI-assisted coding actually work. **Without those layers, you're just generating confident garbage at high speed.**"

层次：unit / E2E / LLM-as-judge / smoke / slop scan。这正是 [[verification-loops]] 的实践版。

### 4. **`/qa` 是 2000+ 行真代码，不是 prompt**
GStack 的 `/qa` 是 Playwright-based CLI browser —— "the thing that isn't just markdown prompts"。Server / CDP inspector / snapshot engine / content security / cookie management。

**他暗示 GStack 接下来要 ship GBrowser** —— 一个**编译 Chromium 60GB** 出来的、Claude Code 嵌在 sidebar 里的浏览器，类似 Perplexity Comet / Atlas。简化版 `/open-gstack-browser` 已经在 GStack 里。

### 5. **生产数据快照（4/18 时刻）**
GStack 当时已经是真产品：
- **75,000 stars in 5 weeks**
- 14,965 unique installs（opt-in telemetry，真实数 ≥ 2×）
- 305,309 skill 调用
- ~7,000 WAU 峰值
- 95.2% 成功率
- Top skills: `/qa` 57,650 次, `/plan-eng-review` 28,014, `/office-hours` 24,817, `/ship` 18,899
- 27,157 sessions 用了 browser

### 6. **诚实的让步（steelmanning）**
他自己承认：
- **Greenfield vs maintenance**：2026 数字主要是新项目代码，维护遗留代码 LOC 会少得多
- **2013 baseline 的存活偏差**：当时公开活动少（Bookface 是私有项目，但分析包含了它）
- **质量调整的生产力没完全证明**：缺乏 2013-me vs 2026-me 的清洁 bug-density 对比
- **"Shipped" 跨时代含义不同**：如果两年后 80% 项目死了，"build a bunch of unused stuff" 的批评成立

### 7. **真正的论点（最重要的一句）**
> "**The gap between 'I want this tool' and 'this tool exists and I'm using it' collapsed from 3 weeks to 3 hours.**"
>
> "Time to first user is the metric that matters, not LOC. The 60-day cycle from 'I wish this existed' to 'it exists and someone is using it' is the real shift. LOC is downstream evidence."

**The argument isn't about Garry — it's about whether the ground moved.** 答案：moved。**"You can fly too."**

## Pages updated from this source
- [[garry-tan]] — added 3rd article (LOC math defense + "engineers can fly" thesis)
- [[gstack]] — production stats at 4/18 (75K stars, 14,965 installs, 305,309 invocations)
- [[verification-loops]] — "testing at multiple levels is what makes AI-assisted coding actually work" framing
- [[gstack]] — `/qa` Playwright detail; GBrowser teaser
- [[index]], [[log]]

## Connections
- Related: [[garry-tan]], [[gstack]], [[verification-loops]], [[thin-harness-fat-skills]], [[skill-as-method-call]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-05-12 | raw/2026-04-18-garry-tan-loc-controversy.md | Initial creation |
