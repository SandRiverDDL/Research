# Open-Reasoner-Zero Data and Reward

```yaml
---
source_id: open-reasoner-zero
section_type: reward-verifier
stage: post-training
substage: reward-verifier
depth: working
confidence: high
need_expert_review: false
---
```

## Core Design / Innovation

- Reward 只检查 answer tags 中的正确性，不另加 format reward。[6-7]
- Data 包含数学和 programmatically synthesized general reasoning；proof 与难以可靠验证的 prompts 被剔除。[7]
- Difficulty filtering 删除极端 pass-rate 样本，使 rollout 保留有效学习信号。[7]
- 从小型 MATH train 扩展到更广的 ORZ corpus 后，reward 与 response length 不再过早 plateau。[6-9]

## Why It Matters

ORZ 把复杂度从 reward engineering 转移到 data engineering。Minimal reward 只有在答案能可靠验证、任务处于 policy capability frontier 附近时才成立。

## Mechanism Sketch

1. 汇总公开 math/reasoning sources。
2. 删除无法可靠 rule verification 的 proof/open-ended tasks。
3. 用 model rollouts 估计难度。
4. 删除几乎全对或全错的 prompts。
5. 使用 exact/binary answer reward 训练。[7]

## Details / Evidence

- 即使没有显式 format reward，base checkpoints 也能很快学会规定的 answer format。[7-9]
- Data-scale ablation 对比更大的 57K corpus 与 MATH train，只有更广数据保持持续增长。[6, 9]

## Gaps / Open Questions

- Programmatic synthesis 与 cross-source contamination 仍需 repo-level 审计。
- Exact-match verification 可能把数学等价表达误判为错误。
- 该 recipe 没有覆盖主观 general-assistant reward。

## Lookup-only

- 数据来源与 filtering：第 7 页。
- Data-scale curves：第 6、9 页。

## Evidence Anchors

- 6-9：minimal reward、data curation 与 scale ablation。
- `[repo]`：公开 dataset/config 版本。
