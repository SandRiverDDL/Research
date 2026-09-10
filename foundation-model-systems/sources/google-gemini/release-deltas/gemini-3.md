# Gemini 3 Release Delta

```yaml
---
delta_id: gemini-3
parent_source: google-gemini
release_date: 2025-late  # Pro 公告时间需 stage notes 阶段核对
role: release-delta
confidence: medium
status: section-notes
openness: closed-weights
---
```

## 定位

Gemini 3 是 Google DeepMind 当前 frontier 主线，与 Gemini 2.5 的关键差异是 **disclosure 形态退化**：到目前为止没有 Gemini 1.5 / 2.5 那种 arxiv paper，公开材料退到 blog + model card + 产品集成。同时 Google 在这一代推出了 **Antigravity（agent IDE）**，使得 closed 阵营 coding-agent 产品形态首次形成 Anthropic Claude Code / OpenAI Codex / Google Antigravity 三方对照。

## 关键 release / 演进

- **Gemini 3 Pro** — frontier 主线，对标 Claude 4.5 Sonnet / GPT-5。
- **Gemini 3 Flash / 其他 tier** — capability tier 补全（具体名字以 stage notes 核对为准）。
- **Antigravity** — Google 在 Gemini 3 时代推出的编程 agent IDE，是 Claude Code / Codex 的对应物。
- **Gemini 3 Deep Research / Mariner 升级** — 基于 3 的 agent 产品迭代。

## 公开材料范围

- **DeepMind / Google blog 公告**：deepmind.google 和 blog.google 都有 release post，含 multimodal / reasoning / agent 定位。
- **Model cards / API docs**：ai.google.dev 提供 context length、pricing、capability tier。
- **Antigravity 公告**：blog.google / Google Cloud / DeepMind 上的产品介绍，是 agent product 主源。
- **Deep Think 模式延续**：blog 提到 Deep Think 在 3 上延续，但相对 2.5 paper 没有新的 paper-level 解释。
- **没有的**：paper / TR / arxiv 形式的完整公开（这是相对 2.5 的明显退步信号，需要在引用时如实标注）。

## Agent data 视角的可用信号

> confidence: medium，证据强度与 Anthropic Claude 4.5 / OpenAI Operator 同档，**低于** Gemini 2.5（因为没 paper anchor）。

- **Antigravity 作为 coding-agent 产品**：与 Claude Code / Codex 形成 frontier 三方对照样本。Antigravity 的 product framing（IDE 内多 agent / 任务分解）暗示训练时 trajectory 可能也偏 multi-agent 组织——但**具体 trajectory 数据 / 合成方式零披露**。
- **Long-horizon agent / Mariner / Deep Research 升级**：blog 提到 Gemini 3 在长 horizon web 任务上的能力提升；评测 setup 没有 2.5 paper 那种 page anchor，仅 blog framing。
- **Multimodal 一线产品集成**：Gemini 3 在 video / image / 文本一线集成层比 2.5 更深，间接暗示训练 trajectory 里 multimodal token 与 agent action 共存的程度更高，但**没有 pipeline 公开**。

## 不能从 Gemini 3 推出的事

- **任何训练 recipe / data scale / RL 设计**。
- **Antigravity 训练数据来源**：是否使用 IDE-内 trajectory、人类示范、合成数据，全部 unknown。
- **Gemini 2.5 → 3 的 architecture / training delta**：blog 不解释架构变化，paper 缺位。
- **Deep Think 在 Gemini 3 的实现是否变化**：仅 blog framing，无 mechanism 公开。

## Disclosure 退步信号（值得记录）

- Gemini 1.5 → 2.5 → 3 的公开材料形态：paper → paper → blog-only，是 frontier closed 阵营 disclosure 退步的样本。可与 Anthropic（一直 closed + system card）/ OpenAI（一直 closed + system card）/ Meta（Llama 系开 → frontier 退）形成 frontier disclosure dynamics 的对照。
- 这一信号本身有研究价值：它提示 frontier closed 阵营**整体在收敛到 blog + system card 这种 disclosure floor**，不再出 paper-level 材料；如果这个趋势持续，"agent data 公开实践"将主要由开源阵营（Qwen / GLM / DeepSeek / Kimi / MiniMax / Step）支撑。

## 与本项目其他 source 的横向对照（待 lens 沉淀）

- vs **Anthropic Claude Code / OpenAI Codex**：三方 frontier coding-agent 产品对照；Antigravity 信息量目前最低（blog only），Claude Code 有 engineering blog 系列，Codex / ChatGPT Agent 有 system card。
- vs **Gemini 2.5**：同一 lineage 内 disclosure 退步样本；引用 Gemini family 的 frontier capability claim 时，应优先用 2.5 paper anchor，把 3 当 product evolution 信号。

## Source

- 引用标签遵循 `sources/google-gemini/source-bundle.md`：`[blog-dm-gemini-3]`、`[blog-google-antigravity]`、`[model-card-gemini-3]`、`[api-docs]`。
- stage notes 升级时按以下顺序锚定：
  1. Gemini 3 Pro 公告 blog（DeepMind 或 blog.google）
  2. Antigravity 产品介绍 blog
  3. Model card / API docs
  4. Deep Think / Deep Research / Mariner 在 Gemini 3 时代的更新 blog

## 升级 trigger

- **不**升级为独立 dossier，因为 disclosure 形态没到独立 dossier 级别。
- 例外：如果后续 Google 重新出 Gemini 3 paper / TR，应立即升级；这是 frontier disclosure 趋势能否反转的关键观察点。

## Caveats

- closed-weights + 无 paper：Gemini 3 引用必须明确 source 是 blog / model card，**不**借用 Gemini 2.5 paper 的证据强度复述给 3。
- Antigravity 是产品名，与 model checkpoint 不是 1-1 对应；引用时区分"Antigravity 用 Gemini 3 做后端"与"Antigravity 是独立模型"。
- "Gemini 3 在 X 任务上比 2.5 提升 Y%"这种数字主要在 blog framing，没有第三方独立 eval 配套时按 marketing claim 处理。
