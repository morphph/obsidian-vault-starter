---
type: source-summary
created: 2026-05-20
last-updated: 2026-05-20
sources:
  - raw/2026-05-14-openai-codex-hooks-docs.md
tags: [wiki, source, openai, codex, hooks, official-docs, determinism, guardrails]
---

# Source: OpenAI Codex Hooks (Official Docs)

## Summary
OpenAI Codex Hooks reached **general availability on 2026-05-14**. Six lifecycle events (SessionStart / PreToolUse / PermissionRequest / PostToolUse / UserPromptSubmit / Stop) with **exit-2-blocks-and-feeds-stderr-back** semantics — **functionally at parity with Claude Code hooks**. This invalidates the "Anthropic stack is thicker" claim made in long-horizon writing dated before 2026-05-14. Configuration via `hooks.json` or `[hooks]` in `config.toml`; layered precedence across user / project / plugin / enterprise; managed hooks via `requirements.toml` for enforced policy.

## Source Metadata
- **URL:** https://developers.openai.com/codex/hooks
- **Publisher:** OpenAI Developers (official docs)
- **GA date:** 2026-05-14
- **Fetch date:** 2026-05-20

---

## 要点解读（12-Section Comprehensive Study Guide）

### 1. 元信息
- **作者**：OpenAI Developers Docs（官方）
- **来源**：developers.openai.com/codex/hooks（一等公民页面，非 cookbook）
- **GA 时间**：2026-05-14（CLI 0.131 同期）
- **在 OpenAI Codex 输出中的位置**：与同周 GA 的 **mobile remote + access tokens + enterprise admin setup** 并列，**是 2026-05 Codex catch-up 周的核心**

### 2. 核心论点（Thesis）
OpenAI 主张：agent 工作流的可靠性不能只靠 prompt"请别动 X"——**必须有 deterministic 拦截层**。**因为** prompt 是请求，hook 是约束；**所以** 任何生产级 agent workflow 必须把 spec 里的 boundary 同步成 hook 配置。

简化压缩包：**"Hooks = 把 spec 里的『不要动』变成『动不了』。"**

### 3. 论证结构
```
1. 6 个 lifecycle event 覆盖 agent 工作的所有关键点
2. exit 2 = block + stderr 反馈 → 让 agent 学到为什么被拦
3. JSON output (permissionDecision / additionalContext / updatedInput)
   → 不只是拦，还可以改写、注入上下文
4. 多层配置 (user / project / plugin / enterprise)
   → 个人开发到企业合规一条链路
```

### 4. 关键概念字典

> **PreToolUse + exit 2（最关键的单一 mechanism）**
> - **是什么**：在 Bash/apply_patch/MCP tool 执行前的 interceptor。Exit 2 拒绝执行，stderr 被喂回 agent 作为反馈
> - **为什么重要**：这是把 `FROZEN` 文件、out-of-scope 路径、危险命令从"请求"变"约束"的唯一机制。**Codex Cloud 自动运行没有 permission prompt，PreToolUse 是 unattended 模式下的唯一 safety net**
> - **直觉类比**：像建筑工地的物理围栏——你写"请勿入内"是 prompt；建一道实体栅栏是 hook
> - **适用场景**：FROZEN spec 保护、敏感文件保护、scope boundary 强制、prompt injection 防御
> - **反面**：只在 spec 里写 `FROZEN` 不配 hook = label 不是 gate

> **PermissionRequest 自动决策（unattended 模式核心）**
> - **是什么**：当 agent 触发需要审批的操作时 fire，hook 可以返回 `"behavior": "allow"` 跳过 prompt，或 `"behavior": "deny"` 拒绝
> - **为什么重要**：让"半自动"模式可能 ——预先定义 *什么可以自动 allow*（如 `npm test`），*什么必须人审*（如 `rm -rf`）
> - **适用场景**：cloud routine 里的高频 safe 操作不要每次问；危险操作必须 escalation

> **PostToolUse + validation gate**
> - **是什么**：每次 tool 执行完后跑 validator；exit 2 让 validation 失败 = 操作回滚反馈给 agent
> - **为什么重要**：**把 validator 从"agent 跑一下"升级成"不能绕过的 gate"**。Spec 里说"每次改完跑测试"是请求；PostToolUse hook 跑测试 + exit 2 on fail 是约束
> - **直觉类比**：CI 在 PR 上的强制 check——通过才能 merge

> **Managed hooks via `requirements.toml`**
> - **是什么**：企业层定义的、用户不能 disable 的 hook
> - **为什么重要**：让 IT/security 能对所有员工的 Codex 用法强制策略（如"不能 push 到 prod branch"）
> - **直觉类比**：MDM 在企业 Mac 上的策略——员工无法 override

### 5. 框架与心智模型

**Hook 的 4 个职责类别**：

| 用途 | Hook 类型 | exit 2 行为 |
|---|---|---|
| **FROZEN 文件保护** | PreToolUse matcher `Edit\|Write\|apply_patch` + path filter | 阻止编辑 |
| **Validator gate** | PostToolUse matcher `Edit\|Write` | 失败时反馈让 agent 修 |
| **Auto-approval** | PermissionRequest | `behavior: allow` 跳过 prompt |
| **Context injection** | UserPromptSubmit / SessionStart | `additionalContext` 注入 |

### 6. 关键数据与例证
- **6** 个 lifecycle event
- **600s** 默认 hook timeout
- **4** 个配置层（user / project / plugin / enterprise）
- exit code 约定：**0 = pass / 2 = block**

### 7. 关键引语

> **"Higher-precedence config layers don't replace lower-precedence hooks."**
> 高优先级配置层不替换低优先级 hook —— 多源同 matcher 都会 fire。
> ⭐ Layering 哲学一句话。

> **"To deny a supported tool call, return this hook-specific shape with `permissionDecision` set to deny."**
> ⭐ JSON output 拦截语法的关键。

### 8. 实操指南

**FROZEN 文件保护 minimal config**：

`.codex/hooks.json`:
```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "apply_patch|Edit|Write",
        "hooks": [
          { "type": "command", "command": ".codex/scripts/guard-frozen.sh" }
        ]
      }
    ]
  }
}
```

`.codex/scripts/guard-frozen.sh`:
```bash
#!/usr/bin/env bash
input=$(cat)
path=$(echo "$input" | jq -r '.tool_input.path // .tool_input.file_path // empty')
case "$path" in
  PROMPT.md|PLANS.md|raw/*)
    echo "BLOCKED: $path is FROZEN" >&2
    exit 2 ;;
esac
exit 0
```

### 9. 对比与反对意见

**vs Claude Code hooks**：
- **形状几乎完全一致**：6 lifecycle events / exit 2 block / JSON additionalContext
- **Codex 多了 `PermissionRequest`**（Anthropic 把这个能力放在 channels permission relay 里）
- **Anthropic 多了 `PreCompact` / `SessionEnd`**（Codex 把上下文管理放在 memory summaries 里）
- **大方向一致：两家在 5/14 之后是 functional parity**

### 10. 与 wiki 知识的连接

**强连接**：
- [[source-claude-code-hooks-docs]] —— 跨厂商等价物。**两家在 5/14 之后是 parity**
- [[claude-code-goal]] —— hook 是 goal 里 boundary 落地的唯一机制
- [[source-openai-codex-cookbook-trilogy]] —— cookbook 给方法论，hooks 给 enforcement

**强化已有概念**：
- 强化 [[determinism-as-guardrail]]（如果有该页）—— hook 是 spec→约束的桥
- **挑战旧观点**：之前 wiki 暗示"Codex 等价物大多用 `codex -p` 拼起来"——**5/14 GA 之后这个说法过时**

### 11. 对用户（vfan）的启示

#### 短期
- **更新 pm-long-horizon-methodology.md 文章中"Anthropic stack 更厚"的判断** —— 已经过时
- 如果未来 blog2video 移植到 Codex，hook 配置 90% 可以直接抄 Claude Code 的 settings.json 结构（语法不同但 conceptual mapping 一致）

#### 中期
- 写"跨厂商 hook 对照"中文短文 —— 时效性强、SEO 空白、给国内 PM 看的"hook 是什么"科普

#### 长期
- 把 hook 作为 PM craft 升级窗口的核心 leverage —— spec 写得准 + hook 配得对 = AFK 安全度跃升

### 12. 一句话总结

**"2026-05-14 Codex Hooks GA，Anthropic 在 determinism 层的领先消失；现在选 vendor 不再因为'谁有 hooks'，而是因为生态匹配。"**

---

## Pages updated from this source
- [[source-claude-code-hooks-docs]] — to be cross-referenced
- [[pm-long-horizon-methodology]] — needs revision of "Anthropic stack thicker" claim

## Connections
- Related: [[source-claude-code-hooks-docs]], [[claude-code-goal]], [[source-openai-codex-cookbook-trilogy]], [[source-openai-codex-automations-docs]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-05-20 | raw/2026-05-14-openai-codex-hooks-docs.md | Initial creation — Codex Hooks GA captures parity with Claude Code hooks |
