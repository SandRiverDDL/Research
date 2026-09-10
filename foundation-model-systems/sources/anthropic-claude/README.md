# Anthropic Claude Family

```yaml
---
source_id: anthropic-claude
source_type: blog-bundle
org: Anthropic
release_date: ongoing
priority: S
status: stub
openness: closed-weights
confidence: medium
lineage: anthropic-claude
role: family-bundle
---
```

## 一句话

Anthropic Claude 家族是当前 frontier closed-weights agent 模型的核心样本：没有公开 TR，但 system card、engineering blog、Claude Code / Computer Use / Skills 等产品层材料合起来，对 agent post-training（trajectory 数据构造、tool-use SFT/RL、subagent / skill 设计）的披露密度足够撑一个 family 级 dossier。

## 为什么重要（对本项目）

- 它是 lineage / comparison 中绕不开的 frontier baseline；不收会让所有 closed-weights agent insight 失去对照点。
- Anthropic 的 agent data 材料偏 "engineering recipe + safety eval"，和 DeepSeek / Qwen / GLM 的 RL recipe 视角互补。
- 后续如果在 `~/Research/agent-data/` 做 lens（trajectory 构造 / verifier / reward model），需要这边有一个稳定的 source dossier 可引用。

## Family Lineup（按时间）

记录原则：family-level README 给定位 + 关键 release 列表；每个 release 的具体 delta 写到 `release-deltas/<id>.md`，信息密度够再升级独立目录。

- Claude 3.7 Sonnet (2025) — 首次明确 reasoning / extended thinking。
- Claude 4 (Opus / Sonnet, 2025) — agent 能力 + system card。
- Claude 4.5 (Opus / Sonnet / Haiku, 2025-2026) — Claude Code、Skills、Computer Use 的主要 anchor。
- Claude 4.6 / 4.7 / 4.8（2026 H1，按需补 release-delta 文件）。

## 已知公开材料（待 release-delta 文件分别 anchor）

- **Engineering blog 系列**：`Building effective agents`、`Claude Code` 工程文章、`Skills`、`Sub-agents`、`Computer Use` 等。
- **System card**：每代 Claude 的 system card 含 agentic eval、refusal、reward hacking、tool-use safety 数据。
- **Product 层 trajectory**：Claude Code、Computer Use 的 demo / 评测构成 agent trajectory 的间接披露。

## Source Bundle

见 `source-bundle.md`。

## 收录策略

- **不**为每个 minor release 单独建子目录；除非未来某个 release 有 architecture / training-level 改动且信息密度够 ≥2 个 stage notes，否则全部以 single-file release-delta 留在本目录下。
- **family-level note** 只写定位、lineage、跨 release 的横向 take；不重复每个 release 的 delta 详情。
- closed-weights 默认 confidence ≤ medium；任何强结论必须标 `[blog-...]` / `[system-card-...]` anchor，不写"据 Anthropic 透露"这种无源 framing。

## Caveats

- 没有 TR：所有 pretraining / RL recipe / data scale 默认 unknown。
- system card 是 safety/eval 文件，不是 training recipe；不要把 eval 数字当作 training 设计证据。
- product-level claim（"Claude Code 能做 X"）≠ 模型训练时的明确数据 pipeline；区分 inference-time scaffolding 和 post-training data construction。
