---
status: draft
sources:
  - raw/2026-07-08-fable-finding-your-unknowns.md
external-refs:
  - https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5
  - https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5
  - https://simonwillison.net/2026/Jun/9/claude-fable-5/
research: research/best-practices-for-claude-fable-5/
platform: blog
lang: zh
created: 2026-07-10
last-updated: 2026-07-10
tags: [draft]
description: "Claude Fable 5 的瓶颈不在 prompt 措辞,在你能不能澄清自己的未知。本文把 Thariq(Anthropic Claude Code 团队)的四象限 unknowns 框架拆成四个当场可抄的 Fable 动作:目标模板、反向访谈、原型+参照源码、盲区扫描,附实现前中后完整流程。"
keywords: [claude fable 5, unknowns, 四象限, finding your unknowns, thariq, give goals not steps, blindspot pass, agentic coding, prompting, implementation notes]
category: techniques
related_blog: loop-engineering-guide
related_glossary: [claude-code, claude]
---

# 给目标不给步骤：用 Thariq 的「四象限 unknowns」驾驭 Claude Fable 5

2026 年 7 月 4 日，Anthropic [Claude Code](/zh/glossary/claude-code) 团队的 Thariq(@trq212)在 X 上发了一篇长文，标题是《Finding Your Unknowns》。到本文成稿时，它累计 **335 万次浏览、20,168 次收藏**——这是同题材里唯一一篇带实测互动数据的文章（其余 Fable 科普帖的数字都是体感推断）。而且收藏数比点赞(8,885)还多。收藏多过点赞通常只说明一件事：读者不是看个乐，是打算收起来、照着做。

真正被反复引用的，是他那句判断：

> "Fable is the first model where I find the quality of the work is bottlenecked by my ability to clarify its unknowns."
> （Fable 是第一个让我觉得——工作质量被「我澄清未知的能力」卡住的模型。）

这句话把瓶颈挪了位置。过去两年，我们默认 agentic coding 的上限是模型能力：模型越强，你能做的越多。Thariq 说的是另一回事——**到了 Fable 这一档，卡住产出的不再是模型不够聪明，而是你没把自己不知道的东西说清楚。** 功夫，第一次明确地落在了 prompt 之外。

## 官方原则缺了半句

Anthropic 给 Fable 的官方 prompting guide 把最佳实践浓缩成一句反直觉的原则：**给目标，不给步骤**(give goals, not steps)。因为 Fable 被造来吸收模糊、自己想「该怎么做」，你把步骤规定得越死，反而越拖累它——前代模型为「弱一点的智能」搭的那些 prescriptive skill,在 Fable 手里成了枷锁。

这条原则是对的，但它缺了半句：**目标本身错了怎么办？**

只给目标、不挖未知，你交出去的那个目标可能从一开始就是歪的。X 上的 Fable 教程几乎都在教「怎么把 prompt 写得更漂亮」，可 Fable 是第一个瓶颈不在 prompt 措辞、而在「你能不能澄清自己未知」的模型。Thariq 的四象限，是目前唯一把这个瓶颈拆到可操作粒度的框架，而它正好能和官方那条「给目标不给步骤」对接上：**每一格未知，对应一个具体的 Fable 动作。** 换句话说，升级到 Fable 之前，先升级你的提问方式——最贵的 bug,往往藏在你从来没写下来的那句话里。

Thariq 用了一个更古老的说法来定位这件事：the map is not the territory,地图不是疆域。地图是你交给 Claude 的东西——prompt、skill、context;疆域是活儿真正发生的地方——代码库、真实世界、它实际的约束。**地图和疆域之间的差，就是未知。** 每撞上一个未知，Claude 就得靠「猜你想要什么」来做决定；活儿越大，它会撞上的未知越多。

那怎么系统地把未知找出来？**四象限 unknowns 是 Thariq 借自 Rumsfeld「已知/未知」矩阵的一套自查框架：把你对一个任务的认知，按「你知不知道」和「你知不知道自己知不知道」切成四格——已知的已知、已知的未知、未知的已知、未知的未知。** 下面这张地图，贯穿全文：每一格，配一个当场能抄的 Fable 动作。

- **如果你主要写代码**,重点看下一节里的「已知的未知 → 反向访谈」和「未知的已知 → 原型 + 参照源码」——这两格最容易在实现中途爆雷。
- **如果你用 agent 跑长时程任务**,重点看「串成流程」一节：把四象限动作沿实现前/中/后铺开，才不会让几小时的自主运行跑偏。
- **如果你带团队**,「经济学收束」和「行动清单」两节能直接落地成团队规范。

## 四象限，逐格配一个 Fable 动作

Thariq 观察过顶级的 agentic coder（他点名 Boris、Jarred）:他们的共同点不是 prompt 写得花，而是**未知很少**——对代码库和模型行为都深度同步，清楚自己要什么。但他们也**为未知留了余量**。减少并预判未知，才是 agentic coding 真正的手艺。好消息是，这门手艺可以靠和 Claude 一起练。

### 已知的已知 → 目标模板（给理由，不给清单）

**定义：** 这就是你 prompt 里明确写下来的东西——你告诉 agent 你要什么。

**怎么识别：** 你能一句话说清「做完长什么样」，而且这句话你有把握。这一格看着最安全，恰恰最容易被写得太干：只有目标，没有「为什么」。

**动作：** 把目标包进一层理由。Thariq 反复强调的一点是——给 Claude 你的起点上下文：告诉它你在思考的哪个环节、你对这个问题和这块代码的经验、把它当思考伙伴而不是执行器。官方 guide 把这层意思固化成了一个可抄的模板：

> I'm working on [大任务] for [谁]. They need [这个产出能让他们做成什么]. With that in mind: [具体请求].

带上「for 谁 / 他们需要什么」，Fable 在撞上你没写到的未知时，才有依据往对的方向 veer,而不是套一个「行业最佳实践」的默认值——那个默认值未必适合你的活儿。

### 已知的未知 → 让 Fable 反向访谈你

**定义：** 你还没想清楚、但你**知道**自己没想清楚的部分。

**怎么识别：** 你心里有「这块待定」的清单，只是懒得或没法一次说全。

**动作：** 别自己憋，让 Fable 一个一个问出来。Thariq 的原话模板：

> Interview me one question at a time about anything ambiguous, prioritize questions where my answer would change the architecture.

一次只问一个，而且**先问那些「你的回答会改变架构」的问题**——把访谈预算花在影响最大的岔路口上，而不是在无关紧要的细节上来回。

### 未知的已知 → 原型逼出隐性标准，参照物直接指向源代码

**定义：** 显而易见到你永远不会写下来、但一看到就能认出对不对的东西。典型是视觉品味：说不清，但看到就知道行不行。

**怎么识别：** 你发现自己在说「我也讲不清，做出来我看看」。

**动作 A——原型：** 在接后端、接状态之前，先让 Fable 用假数据搭个 HTML 原型，让你对着布局反应。Thariq 的用法：

> Before wiring anything up, make a single HTML file mocking the new editor toolbar with fake data. I want to react to the layout before you touch the real app.

隐性标准在原型阶段被逼出来很便宜；拖到实现阶段才发现，一个 spec 上的小改动可能引发代码里天翻地覆的重写，而 agent 要回退之前的改动会更难。

**动作 B——参照：** 有时你连描述都描述不出来，最好的参照物不是文档、不是截图，**是源代码**。把 Fable 直接指向那个实现了你想要行为的文件夹，哪怕它是另一种语言：

> This Rust crate in vendor/rate-limiter implements the exact backoff behavior I want. Read it and reimplement the same semantics in our TypeScript API client.

它读的是底层的 markup 和结构，拿到的细节远比一张截图丰富。

### 未知的未知 → 盲区扫描(blindspot pass)

**定义：** 你压根没考虑过的东西——你不知道自己不知道。进新代码区、做不熟的活（比如调设计）,这一格通常最满。

**怎么识别：** 你连「该问什么问题」都不知道，不清楚「好」长什么样，不知道前人踩过哪些坑。

**动作：** 让 Claude 帮你找盲区，并讲给你听。Thariq 建议**照字面用「blindspot pass」和「unknown unknowns」这两个词**,并且一定要给它「你是谁、你已知什么」的上下文：

> I'm working on adding a new auth provider but I know nothing about the auth modules in this codebase. Can you do a blindspot pass to help me figure out my relevant unknown unknowns and help me prompt you better.

Claude 能极快地扫代码库和全网，对绝大多数话题懂得比你多，失败迭代也比你快——它是把未知捞出水面最省力的工具。

## 串成流程：实现前 / 中 / 后

Thariq 把和 Fable 的协作描述成「an iterative process of discovering my unknowns before, during, and after implementation」——在实现前、中、后不断发现未知的迭代过程。把上面四格的动作沿时间轴铺开，就是一条完整流程：

**实现前（五个便宜的探测）:** 盲区扫描 → 原型 / brainstorm → 反向访谈 → 参照源码 → 实现计划。计划这一步他也有讲究：用 HTML 写，**把你最可能改的决策放最前面**——数据模型、类型接口、面向用户的流程；机械性的重构埋到底部（「那部分我信你」）。

**实现中（记账）:** 满意计划后另起一个 session,把 spec、原型这些 artifact 喂进去。但再多的计划也挡不住潜伏的未知，agent 干着干着可能因为一个 edge case 需要换打法。所以让它记一份临时的 `implementation-notes.md`:

> Keep an implementation-notes.md file. If you hit an edge case that forces you to deviate from the plan, pick the conservative option, log it under 'Deviations', and keep going.

撞到 edge case、被迫偏离计划时，选保守选项、记到 `Deviations` 名下、继续走——下一次尝试就能从这本账里学。

**实现后（拿共识 + 验收）:** 两件事。一是 pitch / explainer——把原型、spec、notes 打包成一份能直接丢进 Slack 拿 buy-in 的文档，demo GIF 打头；当审阅者和你起点一样满是未知时，这份东西能加速他们理解、也加速批准。二是 quiz——长会话结束后，Claude 干的往往比你以为的多，光读 diff 只能看个皮毛，让它出一份带上下文的变更报告 + 一份测验，**考满分才 merge**。

一句点破：这不是给你新增负担，而是**把四象限的动作按时间铺开**。用 Thariq 的话，每一个 explainer、brainstorm、interview、prototype、reference,都是「a cheap way to find out what you didn't know before it gets expensive to fix」——在变贵之前，先便宜地把你不知道的东西找出来。

## 经济学：模型越贵，挖未知的杠杆越大

为什么这套功夫在 Fable 身上比在任何前代模型上都值？看账单。

独立开发者 Simon Willison 在发布当天的实测里管 Fable 叫「a beast — slow, expensive」：一天烧掉 **$110**,但一次做完了「several days' worth of work」——好几天的活。Fable 的定价是 **$10 / M input、$50 / M output**,每一次跑都比前代贵；在 high effort 下，单次请求能跑数分钟，自主运行能延续数小时。

把这两件事叠起来看：模型越贵、单次跑得越久，一个没澄清的未知造成的返工就越贵。**cheap now < expensive later** 从一句格言，变成了会实实在在出现在账单上的数字。前面那五个便宜探测，每一个都是在用几毛钱的原型、访谈，买掉一次可能几十美元的重跑。模型越强越贵，挖未知的杠杆率越高——这正是「先挖未知」在 Fable 时代从「好习惯」升级成「省钱纪律」的原因。

## 从今天开始的五条

1. **下个项目的第一句话，先让 Claude 找 unknowns,别急着派活。** 照字面说「blindspot pass」和「unknown unknowns」。
2. **给目标时顺手给理由。** 用那个「I'm working on … for … They need … With that in mind: …」模板，让它有依据往对的方向 veer。
3. **待定的地方，让它一次一问地反向访谈你**,并要求先问会改架构的问题。
4. **说不清的东西，先原型、后参照源码**——把 Fable 指向那个已经做对了的文件夹。
5. **长会话结束，先过 quiz 再 merge**,并让它把偏离计划的决定记进 `Deviations`。

先挖未知、再设计循环——这套顺序，正是 [loop engineering](/zh/blog/loop-engineering-guide) 的前置功课：你得先知道自己要 verify 什么，那个循环才有意义。同一篇 Thariq 文，我们还做了一版白板精读视频（以四象限图为脊柱）。两者互为表里：这篇讲**怎么做**,视频讲**为什么这么想**。下一个把最难的活丢给 [Claude](/zh/glossary/claude) 之前，先花十分钟，让它帮你找出你还不知道自己不知道的那部分。

## 参考来源

- Thariq (@trq212), *A Field Guide to Fable: Finding Your Unknowns*, X Article, 2026-07-04 — <https://x.com/trq212/status/2073100352921215386>（配套示例 artifact:<https://thariqs.github.io/html-effectiveness/unknowns/>）
- Anthropic, *Prompting Claude Fable 5*（官方 prompting guide）— <https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5>
- Anthropic, *Introducing Claude Fable 5 and Claude Mythos 5* — <https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5>
- Simon Willison, *Claude Fable 5: initial impressions*, 2026-06-09 — <https://simonwillison.net/2026/Jun/9/claude-fable-5/>
