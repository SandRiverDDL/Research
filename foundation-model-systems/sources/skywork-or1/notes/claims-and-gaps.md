# Skywork-OR1 Claims and Gaps

```yaml
---
source_id: skywork-or1
section_type: claims-and-gaps
stage: claims-and-gaps
substage: none
depth: working
confidence: high
need_expert_review: false
---
```

## Core Design / Innovation

- 强证据：公开 recipe 能在报告 harness 下提升 distilled 7B/32B 的 math/code 能力。[35-37]
- 在本实验范围内有强证据：on-policy freshness、no-KL training 与 entropy control 会影响稳定性和最终表现。[16-30]
- 尚未建立：相同 entropy target 与 recipe 对 base-model RL、general alignment 或 agentic environment 仍最优。

## Why It Matters

Skywork-OR1 最适合作为 controlled methods source。它发布时的 SOTA table 会过时，但 failure-mode 与 resource-allocation 证据更耐用。

## Mechanism Sketch

1. Optimizer comparison 前先复用 data/verifier audit。
2. 同时跟踪 entropy、policy lag、train reward 与 held-out performance。
3. Baselines 之间匹配 rollout budget 与 update compute。
4. 迁移 recipe 前增加 general capability/safety gates。

## Details / Evidence

- Models、data 与 code 均已开放。[repo, rl-data]
- Evaluation 固定 max generation length，并报告 repeated-sample average；但跨模型 scaffold/token-cost 仍不完全一致。[35-37]
- Base checkpoints 已含 R1-distilled reasoning traces，因此这些 gain 不是 base 上 reasoning emergence 的证据。[35]

## Gaps / Open Questions

- Seed variance 与完整 compute accounting。
- Training data 与 AIME/code eval 的 overlap。
- General behavior 与 safety regression。
- 与 ORZ PPO、后续 on-policy GRPO systems 的 matched comparison。

## Lookup-only

- 历史 benchmark values：第 36-37 页。

## Evidence Anchors

- 7-35：机制与 ablation evidence。
- 35-37：最终设置与 claims。
- `[repo]`、`[rl-data]`：reproducibility artifacts。
