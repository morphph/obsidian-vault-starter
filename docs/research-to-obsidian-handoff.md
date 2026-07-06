# Handoff：把 `/research` 能力建进 Obsidian 项目

> 收件人：**Obsidian 项目的 Claude Code**。
> 寄件人：content-ops 编排层。
> 目的：把「调研」能力固化成 obsidian 内的一个 skill `/research`，与现有 `/ingest`、`/draft` 并列。
> content-ops 从此**只负责编排**（给话题、写中央 ledger、把人工 Gate），不在自己这边跑调研。

---

## 1. 你要做什么（一句话）

在 obsidian 项目里建一个 skill `/research "<topic>"`：输入一个话题，产出**调研报告 + 文章 outline + 「建议 ingest 候选清单」**，落到一个**非 vault 的工作区**。它不发布、不写 ledger、不自动把素材塞进 vault。

做完后 obsidian 同时拥有 `/research`（调研）+ `/draft`（写稿）+ `/ingest`（消化进库）——内容生产闭环都在你这。

## 2. skill 内部流程

1. **先查内**（零成本）：query gbrain + vault —— "这话题 vault 里有什么、我写过哪些角度"。把已有 Tier-1 锚点带进 outline，避免重复表达。
2. **再扫外**（engagement 加权，采一批外部素材）：
   - `last30days` —— web / Reddit / HN / YouTube 趋势（⚠️ 见 §6 前置，VPS 可能还没装）
   - `bird` —— X 定向搜索 / 线程 / 互动数（VPS 已装）
   - `deep-research` —— Claude Code 内置深度网页调研
   - `summarize` —— YouTube
   - **原始素材是重污染**：建议用一个 sub-agent 跑这步扇出，主会话只收回综合结果，别让原始抓取灌满上下文。
3. **综合**（以 `audience-profile.md` 为品味锚，见 §5）：产出三个文件 —
   - `report.md` —— 调研综合：A 事实锚定（官方文档核验）+ B 竞品缺口 + 制胜写法
   - `outline.md` —— 文章大纲
   - `ingest-candidates.md` —— 建议进 vault 的外部原文清单，**每条一句理由 + 链接**
4. **停**。不自动 ingest。候选清单交回编排层 / 作者圈选，**圈过的才走你现有的 `/ingest` 进 vault**。

## 3. 硬约束（务必保留——这几条是原设计的安全不变量）

- **不批量把调研结果塞进 vault**。原因：Tier-1 稀释（vault 是作者品味锚，灌机器按 engagement 挑的内容会让选题漂向 engagement-bait）/ 双重入库（同文经两路进 gbrain → 重复 atoms）/ 不可逆。**只产候选清单，人圈选后才 `/ingest`**。
- **输出落非 vault 工作区**（你定个 idiomatic 路径，建议 `research/<topic-slug>/`），**不混进 `raw/`、`wiki/`**，不被 `gbrain sync` 当 Tier-1 收。
- 调研报告**本身** = Tier-4 衍生品：归档可检索，但排除出 vault / 选题输入（否则选题会引用自己的调研结论 → 塌缩）。
- 调研报告**引用的外部原文** = Tier-3：圈选后可作来源。
- `/research` 自身**不写 ledger、不 push、不发布**。

## 4. 输出契约（给编排层对接）

skill 跑完，**打印一段机器可读结果**，让 content-ops 据此写 ledger（`researching → outline_review`）：

```json
{
  "ok": true,
  "topic": "<topic>",
  "artifacts": {
    "report":     { "path": "research/<slug>/report.md",            "sha256": "..." },
    "outline":    { "path": "research/<slug>/outline.md",           "sha256": "..." },
    "candidates": { "path": "research/<slug>/ingest-candidates.md", "sha256": "..." }
  },
  "warnings": [], "errors": []
}
```

envelope 形态对齐 obsidian 现有 `obsidian_content.py` 的 contract 1.0 同形 envelope（`{contract_version, ok, verb, data, warnings, errors}`）即可。content-ops 用这里的 `sha256` 做 Gate 的 stale 校验。

## 5. `audience-profile.md`（品味锚）

`/research` 综合 outline 时要以受众画像为锚（受众 = 全背景 AI builder，锚点「能上手但非资深工程师」，分层深度 + 角色化入口；含 GEO 写作规范：加引用来源 +40% AI 引用率、加统计数据 +37% 等）。

这份文件现在在 content-ops 仓库根。**请确认共享方式**（默认：把当前快照拷一份进 obsidian 项目，后续以 content-ops 版为准定期同步）。

## 6. 前置 / 边界

- **谁做什么**：obsidian = `/research` + `/ingest` + `/draft`（内容生产）；content-ops = 给话题、写中央 ledger、把 Gate 1（审 report+outline）、归档指针。**调研不在 content-ops 跑。**
- **可被 headless 调用**：设计成 headless claude 以话题为参数调起、输出落确定性路径（content-ops 经会话 SSH / Telegram→VPS 调你）。
- **工具前置**：`bird` ✅ 已装；`deep-research` ✅ 内置；`last30days` ❌ 待装 VPS；X 在 headless 下的登录方式（cookie 注入）仍待验。

## 7. 现成参考（强烈建议先读）

- content-ops `outputs/codex-guide/PILOT.md` —— 一次**人肉跑通的 `/research` 样例**（两轨：A 事实锚定官方文档 / B 竞品缺口 + 制胜点 + ingest 思路）。把它当**产出格式参照 + 回归样例**：你建好 skill 后，用同一个话题（OpenAI Codex 指南）跑一遍，产出应与该 pilot 同形。
- `outputs/codex-guide/draft-zh-v1.md` —— 该话题的下游初稿，看 research → outline → draft 的衔接。

---

## 验收（建议）

- [ ] `/research "OpenAI Codex 指南"` 跑通，产出 `report.md` + `outline.md` + `ingest-candidates.md`，落在非 vault 工作区。
- [ ] 产出与 `outputs/codex-guide/PILOT.md` 同形（两轨调研 + 候选清单）。
- [ ] 全程**没有**任何东西自动进 `raw/`/`wiki/`。
- [ ] 打印 §4 的机器可读 envelope，含三个 artifact 的 sha256。
- [ ] 可被 headless 以话题为参数调起。
