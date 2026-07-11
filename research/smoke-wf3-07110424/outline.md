# Outline: 三家 AI coding agent 怎么管上下文：Claude Code × Codex × Cursor 入门对照
> 基于角度: report §7 角度1（推荐）· 目标渠道/形式: 博客长文（中文主体 + GEO 优化）

## prior_coverage（强制字段——对「已表达角度清单」逐条声明关系）
- **五回合决策框架（纯 Claude Code）→ `drafts/claude-code-context-management-guide.md`** → **不同角度**：
  现有稿是「单工具 × 5 操作决策」；本 outline 是「跨三工具 × 同问题不同解」的对照入门。**本稿把 5 选项框架
  压成一节并显式外链现有稿（"Claude Code 的操作细节见 X"），主体篇幅给 Codex/Cursor 对照与底层实证——
  不复述 5 选项的展开。** 若写稿时又把 5 选项逐条铺开 → 塌回旧角度，Gate 1 应拒。
- **7 层记忆系统逆向工程 → [[context-management]] wiki 页** → **明确不覆盖**：那是深水区/架构向，本稿是「入门」，
  7 层最多作为「Anthropic 有多认真」的一句话旁注 + 外链，不展开。
- **context engineering 三层模型 → [[four-files-context-architecture]]（Khairallah）** → **不同角度**：
  那是「怎么组织持久上下文文件」；本稿是「运行时窗口怎么管」，只在结尾指路，不重叠。

## take 占位（Gate 1 由作者填，3–5 句: thesis / 不同意主流叙事哪点 / 对 AI builder 的含义）
> ⏳ 待作者 take —— 本 outline 每个主张段都要能挂到 take 上，writer 无 take 不开工。
> 候选立场（供作者定夺，非既定 take）：「上下文管理不是某个工具的技巧，是所有 coding agent 共享的一门
> 手艺；一旦你看懂三家在解同一个『有限 + 会腐烂』的问题，换工具就不用重学。」

## 结构（逐节: 论点 + 挂哪些 report 论断/出处 + 预估篇幅占比）
1. **开场：一句话价值 + 谁该读** — 论点：上下文管理是跨工具通用手艺，不是 Claude Code 专属技巧 —
   证据：[外部: anthropic.com/…/effective-context-engineering-for-ai-agents] — ~8%
2. **底层事实：context 有限且会腐烂** — 论点：不是越大越好，越满越笨 — 证据：
   [外部: anthropic.com「attention budget」] + [外部: trychroma.com/research/context-rot「18 模型全退化」]
   —【GEO：此处加官方引用 + 统计数字】— ~18%
3. **同一个问题：三家都要回答「留什么、丢什么、隔离什么」** — 论点：建立对照心智模型 —
   证据：report §2 对照表 [内部/Tier-1: [[context-management]]] — ~12%
4. **压缩（compaction）三家怎么做** — Claude `/compact`（有损可加方向）· Codex `/responses/compact`+
   `encrypted_content` · Cursor 窗口填满即退化 — 证据：[外部: openai.com/…/unrolling-the-codex-agent-loop]
   —【GEO：Codex 机制加官方链接】— ~15%
5. **隔离（subagent / Skills）** — 论点：核心价值是把中间过程挡在主窗口外，不是并行 — 证据：
   [外部: x.com/bcherny/status/2038454336355999749] [内部/Tier-1: [[session-memory]]] + Cursor Skills 动态加载 — ~12%
6. **隐形的第 6 招：保护 prompt cache** — 论点：别中途改系统级文件；200x 成本差 — 证据：
   [外部: openai.com「别改 AGENTS.md」] [内部/Tier-1: [[prompt-cache-optimization]]] —【GEO：200x 数字】— ~12%
7. **Claude Code 用户的每回合 5 选项（压缩版 + 外链现有稿）** — 论点：把决策反射落到具体命令 —
   证据：[内部/Tier-1: [[source-thariq-session-management-1m]]] + 外链 `drafts/claude-code-context-management-guide.md`
   — ⚠️ **仅一节、不展开**，避免塌回旧角度 — ~13%
8. **收尾：一张跨工具对照表 + 换工具不用重学** — 呼应 take；指路 [[four-files-context-architecture]] 深水区 — ~10%

> 写稿前置依赖（见 report §2 warning）：Codex / Cursor 官方页本次 quick 扫描未逐字核验（403/thin）。
> §4、§6 若把这两条作硬 claim，**须先 ingest 候选 #2、#4 逐字核验**再落笔。
