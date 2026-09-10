# Step 3.5 Flash Eval / Step 3.7 Delta

```yaml
---
source_id: step-3.5-flash
section_type: eval-release-delta
stage: evaluation
depth: working
confidence: medium
need_expert_review: false
---
```

## Core Design / Innovation

- Eval 覆盖 reasoning、coding agent、general agent、long-context 和 general benchmarks，重点支撑“11B active 也能接近 frontier”的 efficiency claim。[21-24]
- PaCoRe 用并行 reasoning trajectories + multi-round coordination 做 test-time scaling，配置为 `K=[4,4,4,4]`。[23]
- BrowseComp with Context Manager、Terminal-Bench、τ2-Bench、ResearchRubrics 等 agentic eval 比纯数学/代码分数更贴近 Step 的定位。[23-24]
- Step 3.7 Flash 是后续更新模型，加入 vision/multimodal；截至本次核查，它是最新模型但不是同等完整 TR。[hf-3.7]

## Why It Matters

Step 的 eval 应该看“低 active + 低延迟 + agent workflow”的组合，而不是只看某个数学分数。PaCoRe 也说明高效基础模型可以把省下来的 latency/成本转为 test-time parallel reasoning。

## Mechanism Sketch

1. Pretraining eval 对比 base 模型能力密度。
2. Post-training eval 按 reasoning、code agent、general agent、long context 分组。
3. PaCoRe 在推理时发起并行 trajectories，并综合多轮结果。
4. 3.7 作为 release delta 记录：native multimodal / vision-language，但不把它当 3.5 TR 的训练事实。

## Details / Evidence

- TR 对 post-training eval 使用最大 256K sequence length、temperature/top-p 1.0，并对不同 benchmark 设置多次独立采样。[23]
- Table 5 中很多 baseline 分数带 `*` 或 `†`，说明有复现/非官方来源，comparison 时要小心可比性。[24]
- Limitation 明确承认 Step 3.5 Flash 相比 Gemini 3.0 Pro 需要更长 generation trajectories，下一步要压缩 thinking。[23]

## Gaps / Open Questions

- Step 3.7 的训练流程、multimodal data、post-training recipe 暂无同等 TR，不能直接 full dossier 继承。
- PaCoRe 的成本/latency 与普通 decoding 的公平对比需要另查 PaCoRe source。

## Lookup-only

- Table 5 benchmark 数字仅在做 positioning 时查。[24]

## Evidence Anchors

- 21-24: eval design and results.
- `[hf-3.7]`: Step 3.7 model card / release-delta.

