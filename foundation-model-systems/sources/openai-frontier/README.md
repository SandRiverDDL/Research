# OpenAI Frontier Family

```yaml
---
source_id: openai-frontier
source_type: blog-bundle
org: OpenAI
release_date: ongoing
priority: S
status: stub
openness: closed-weights
confidence: medium
lineage: openai-frontier
role: family-bundle
---
```

## 一句话

OpenAI 当前 frontier 模型与 agent 产品（o-series reasoning model、GPT-5 系列、Operator、Deep Research、Codex agent 等）共享一个 family dossier：没有 TR，但 system card / safety report / product blog 在 agent post-training（trajectory、tool-use RL、refusal & reward hacking 数据）上的披露密度够支撑横向比较。

## 为什么重要（对本项目）

- frontier closed-weights agent 的另一极端样本，与 Anthropic Claude 的 framing 互补：OpenAI 偏重"reasoning + product agent"组合，data construction 提示散在 system card 和 safety eval。
- Operator / Deep Research / Codex 是 production-grade agent 的早期样本，trajectory / verifier / reward 设计的间接证据集中在这里。
- comparison 中是 GLM-5 / DeepSeek V4 / Kimi K2.x / Qwen3.5 的天然对照。

## Family Lineup（按公开节点）

- o1 / o3-mini / o3 / o4-mini —— extended reasoning 系列。
- GPT-4.1 / GPT-4.5 / GPT-5（含 mini / nano / pro 变体）—— 主线 chat + agent。
- **Agent 产品**：Operator、Deep Research、Codex（cloud agent）、ChatGPT Agent。
- 各代 system card / safety report 单独是材料，但归到对应 release 的 delta 文件下。

## 已知公开材料

- **System cards / safety reports**：每代主要 release 都有 PDF，含 agentic capability eval、refusal / reward hacking 数据、red-team 结果。
- **Engineering / research blog**：openai.com/index 大量 blog；agent-related 的有 Operator、Deep Research、Codex、ChatGPT Agent、Function calling / Responses API。
- **Spec / Model spec**：Model Spec、Operator usage policy 等政策文件，间接暴露 reward / refusal 设计。

## Source Bundle

见 `source-bundle.md`。

## 收录策略

- 一个 family 一个目录；release 级 delta 走 `release-deltas/<id>.md`，信息够再独立。
- 优先 release-delta：
  1. `release-deltas/gpt-5.md` —— 主线最新基础模型。
  2. `release-deltas/o-series.md` —— extended reasoning lineage（先合写一份，后期分代再拆）。
  3. `release-deltas/operator.md` —— browser/computer agent，agent data 视角的核心。
  4. `release-deltas/deep-research.md` —— 长 horizon research agent。
  5. `release-deltas/codex-agent.md` —— coding agent。

## Caveats

- closed-weights，零 TR；training recipe / data scale 全部 unknown，禁止从 OpenAI 论文老作（InstructGPT、RLHF paper）反推现行 GPT-5 / o-series 训练设计。
- product blog 容易 marketing-heavy，引用必须到 system card / model spec 这类相对硬的 anchor。
- 同一时间点的 model 版本号（"gpt-4o-2024-XX-YY" 之类）经常变，写 anchor 要带 snapshot 日期。
