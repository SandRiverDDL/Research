# Open-Reasoner-Zero Claims and Gaps

```yaml
---
source_id: open-reasoner-zero
section_type: claims-and-gaps
stage: claims-and-gaps
substage: none
depth: working
confidence: high
need_expert_review: false
---
```

## Core Design / Innovation

- 强证据：公开 recipe 能让多个 scale 的 base model 同时提高 reward 与 response length。[3-9]
- 在本实验内有证据：`γ=λ=1`、no KL 和更大的 curated data 优于所测试替代项。[5-9]
- 尚未普遍成立：带 critic 的 PPO 在所有 reasoning/agentic RL 设置下都优于 GRPO。[5, 10-11]

## Why It Matters

应把 ORZ 当作 reproducible baseline 与 falsification tool，而不是 RL algorithm design 的最终答案。

## Mechanism Sketch

1. 先复现已发布 config。
2. 检查 policy 与 critic curves。
3. 固定 data/compute 后再比较 GRPO variants。
4. 把 no-KL 结论迁移到 general task 前，加入 behavior-regression gates。

## Details / Evidence

- 项目开放 code、data、多种 policy weights 与 critic weights。[3, repo]
- Benchmark superiority 仍需控制 training steps、data 与 evaluation harness 差异。[5, 11]
- MMLU 改善说明存在一定 reasoning 之外的 transfer，但不能证明 assistant alignment。[8]

## Gaps / Open Questions

- Artifact/version pinning 与 end-to-end rerun cost。
- Unconstrained RL 后的 safety、instruction following 与 multilingual behavior。
- Base-model contamination 与对 Qwen2.5 pretraining 的依赖。
- Matched-compute PPO vs GRPO 对比。

## Lookup-only

- Evaluation tables：第 5、8、11 页。
- Training hyperparameters：第 17-19 页。

## Evidence Anchors

- 3-12：claim、ablation 与 evaluation。
- `[repo]`：reproducibility artifacts。
