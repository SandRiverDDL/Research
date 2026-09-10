# Arcee Trinity Large Pretraining / Data

```yaml
---
source_id: arcee-trinity-large
section_type: pretraining-data
stage: pretraining
depth: working
confidence: medium
need_expert_review: false
---
```

## Core Design / Innovation

- Trinity Nano/Mini 是 scaling ladder，不只是小模型：它们用于验证 data pipeline、architecture、training recipe 和 infra，然后再上 Trinity Large。[2]
- Trinity Large 训练 17T tokens，来自一个 20T mix，按 13:4:3 三阶段比例采样。[9]
- 数据目标覆盖 general English、programming、STEM、reasoning 和多语言；DatologyAI 生成了 8T+ synthetic web/code/STEM tokens。[9]
- Muon optimizer 是训练 recipe 的重要组成，TR 强调三种规模模型都 zero loss spikes。[1-2]

## Why It Matters

Arcee 的价值是从 open team 角度展示“做大模型前先用小/中模型验证 recipe”的工程纪律。它和 MAI scale-ladder 有相似精神，但更偏开放 MoE pretraining 稳定性。

## Mechanism Sketch

1. Nano/Mini 用 10T mix，验证 pipeline 和架构。
2. Large 用 distinct 20T mix 中的 17T tokens，三阶段推进。
3. 结合 curated web-scale data 和大规模 synthetic data。
4. 使用 Muon，并配合 QK-Norm、SMEBU、norm/init 等稳定组件。

## Details / Evidence

- Trinity Nano/Mini 各训 10T tokens，Trinity Large 训 17T tokens。[1, 9]
- 20T mix 三段为 13T / 4T / 3T，Large 按比例采样。[9]
- 数据显式 target Arabic、Mandarin、Japanese、Spanish、German、French、Italian、Portuguese、Indonesian、Russian、Vietnamese、Hindi、Korean、Bengali 等语言。[9]

## Gaps / Open Questions

- DatologyAI 数据清洗、过滤、合成质量控制和版权/provenance 细节仍不够开放。
- Post-training 细节不足；如果关注 agentic post-training，要另读 Trinity-Large-Thinking release。

## Lookup-only

- 精确数据比例、synthetic token 类型、optimizer hyperparameters 需要时回 pages 9-14。

## Evidence Anchors

- 1-2: scale and zero-loss-spike claim.
- 9-14: data and training.

