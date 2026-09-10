# Olmo 3 Source Dossier

```yaml
---
source_id: olmo-3
source_type: model-tr
org: Allen Institute for AI
release_date: 2026-04-14
priority: S
status: section-notes
openness: fully-open
confidence: high
lineage: olmo
role: full-tr
base_source: olmo-2
---
```

## 一句话

Olmo 3 不是最强 frontier 模型，但它是当前最值得精读的 fully-open model flow：base、midtrain、long-context、Think、Instruct、RL-Zero、数据、代码、训练日志、checkpoint 和 eval/decontam 工具都公开，适合当作“开放 recipe 可复现性”的标尺。[1-6]

## 为什么重要

对后训练岗位，它给了 SFT -> DPO -> RLVR、Think/Instruct 分流、RL-Zero from base 的完整对照；对未来基模方向，它更重要的是展示如何把 data mix、centralized eval、midtraining、long-context extension 和 post-training 组织成一条可审计 model flow。

## 核心机制 / Takeaways

- Fully-open 的核心不是只开 weights，而是开完整 model flow：每个阶段 checkpoint、实际训练 tokens、data pools、训练代码、eval/decontam 代码和 logs。[1, 5]
- Base training 分三段：Dolma 3 Mix pretraining、Dolma 3 Dolmino Mix midtraining、Dolma 3 Longmino Mix long-context extension；后两段明显服务 post-training 所需的 reasoning、tool-use、long-context 能力。[4-5]
- Data 侧最值得学的是 token-constrained mixing、quality-aware upsampling、global dedup、olmOCR science PDFs，以及“distributed source feedback + centralized integration test”的 midtraining 评估闭环。[5]
- Post-training 明确分出 Think 和 Instruct 两条产品目标：Think 追求长 reasoning trace 和 test-time scaling，Instruct 追求短回答、function calling 和低延迟。[5-6]
- RL-Zero 直接从 base 做 RLVR，价值在于研究 base data 对 RLVR 的影响，而不是把它包装成最强模型。[4, 6, 63-64]

## Source Bundle

- technical report: https://arxiv.org/abs/2512.13961
- tech-report-pdf: https://arxiv.org/pdf/2512.13961
- release blog: https://allenai.org/blog/olmo3
- local pdf: `/Users/chy/Research/foundation-model-systems/papers/olmo-3/olmo-3.pdf`
- last checked: 2026-07-21

## Lineage / Delta

- lineage: Olmo
- role: full TR for Olmo 3 / 3.1 model flow
- newly disclosed: Dolma 3/Dolci data suites, full training flow, post-training datasets, RL-Zero, logs/checkpoints/data release.
- not safe to inherit: exact Olmo 2 recipe details unless rechecked against Olmo 2 source.

## Citation Labels

- default TR pages: page-only anchors like `[4-6]`
- non-TR labels:
  - `[blog-release]`

## 最大证据缺口

- 完整可复现性强，但 first-pass notes 还没有逐表审计 appendix 里的 decontamination、post-training data 和 training logs。
- Olmo 3 的价值主要是 openness / workflow，不应和 Kimi/GLM/DeepSeek 这类 frontier-scale claim 直接按分数比较。

## Lens Hooks

- open-recipe: fully-open model flow and reproducibility boundary.
- pretraining: data mix search, midtraining integration tests, long-context PDFs.
- rl-training: RLVR, OlmoRL, RL-Zero from base.
- eval: centralized eval as training decision system, not leaderboard reporting.

## 阅读入口

- `section-index.md`: 118 页 TR 的回读地图。
- `notes/model-flow.md`: fully-open model flow 和读法。
- `notes/pretraining-data.md`: pretraining/midtraining/long-context 数据机制。
- `notes/post-training.md`: Think/Instruct/RL-Zero 后训练结构。
- `notes/release-olmo-3.1.md`: 更长 RL schedule、32B Instruct scaling 与 refreshed RL-Zero delta。
- `notes/eval.md`: eval 作为开发 gate 的设计。
