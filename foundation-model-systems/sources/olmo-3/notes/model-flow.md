# Olmo 3 Model Flow

```yaml
---
source_id: olmo-3
section_type: model-flow
stage: full-lifecycle
depth: working
confidence: high
need_expert_review: false
---
```

## Core Design / Innovation

- Olmo 3 的核心创新是完整开放 model flow，而不是单点模型技巧：base、Think、Instruct、RL-Zero、数据、代码、logs 和中间 checkpoints 都被纳入 release。[1-6]
- 它把 model development 拆成 base training 与 post-training 两大块，base 又分 pretraining / midtraining / long-context extension，post-training 又分 Think / Instruct / RL-Zero。[4]
- Open recipe 的研究价值在于可介入任意阶段：你可以研究 base data 对 RL 的影响、midtraining 对 post-trainability 的影响、SFT/DPO/RL 各阶段的边际收益。[3-6]

## Why It Matters

Olmo 3 是“学流程”的 source。它不适合当作 frontier SOTA 方法库，但很适合建立 taste：一个可审计模型系统应该公开哪些材料、如何用 eval 做阶段决策、如何避免只在终点模型上讲故事。

## Mechanism Sketch

1. 先训练 Olmo 3 Base：Dolma 3 Mix pretraining -> Dolma 3 Dolmino Mix midtraining -> Dolma 3 Longmino Mix long-context extension。
2. 从同一个 base 分出 Olmo 3 Think：SFT -> DPO -> RLVR，保留 reasoning traces。
3. 分出 Olmo 3 Instruct：SFT -> DPO -> RLVR，优化短回答、function calling 和低延迟。
4. 另做 Olmo 3 RL-Zero：从 base 直接 RLVR，服务开放 RL 研究。

## Details / Evidence

- TR 首页列出 Base/Think/Instruct/RL-Zero checkpoints、Dolma/Dolci data、pretrain/posttrain code、data code、eval code、training logs 和 demos。[1]
- Introduction 明确将 fully-open 定义为开放完整 lifecycle，而不是只开放最终 weights。[3]
- Figure 2 把训练流程画成可追踪 pipeline，说明 release 目标是“model flow”，不是单模型 endpoint。[4]

## Gaps / Open Questions

- First pass 尚未逐项验证所有 Hugging Face dataset / logs 是否仍可下载、是否能机械复现。
- 需要后续 lens 判断：Olmo 3 的 fully-open 标准是否能迁移到 Kimi/GLM/DeepSeek 这种只开放 weights 或 API 的 source audit。

## Lookup-only

- 32B Think 训练成本估算和 H100 时间放在 cost audit，不进入主线。[6-8]

## Evidence Anchors

- 1: artifact list and abstract.
- 3-6: model-flow framing.
- 63-65: RL-Zero motivation.

