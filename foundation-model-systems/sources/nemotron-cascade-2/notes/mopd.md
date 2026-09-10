# Nemotron-Cascade 2 MOPD

```yaml
---
source_id: nemotron-cascade-2
section_type: opd
stage: post-training
substage: multi-domain-on-policy-distillation
depth: working
confidence: high
need_expert_review: false
---
```

## Core Design / Innovation

- Cascade 2 把 MOPD 放在 Cascade RL 中间，用每个 domain 最强 intermediate teacher 给 student dense token-level distillation signal，以恢复复杂 RL stage 中出现的 benchmark regression。[1, 10, 13-14]
- 相比 GRPO 的 sequence-level sparse outcome reward，MOPD 提供 token-level dense advantage，所以在报告中表现为更快 convergence。[14]
- MOPD 不是最终 alignment 阶段，而是 Cascade RL 中的 consolidation / regression-recovery stage；后面还接 RLHF、long-context RL、code RL 和 SWE RL。[10]
- 它和 MiMo 的 MOPD 同属 2026 OPD 主线，但 Cascade 2 更强调“在 Cascade RL 过程中用 intermediate teachers 恢复能力”，MiMo 更强调 multi-teacher consolidation 到最终 student。

## Why It Matters

这是 2026 后训练最值得跟的模式之一：随着 domain-specific RL 增多，模型会在某些能力上回退。MOPD 提供一种比 offline SFT 更贴近当前 policy distribution 的修复方式。

## Mechanism Sketch

1. 先通过 IF-RL / multi-domain RL 产生多个中间 checkpoints / teacher candidates。
2. 对特定 domain 选择最强 intermediate teacher。
3. Student 在当前分布上 rollout。
4. Teacher 提供 token-level distillation advantage。
5. 用 MOPD 快速恢复或超过 teacher-level performance，再继续后续 Cascade RL stages。

## Details / Evidence

- Figure 3 展示 MOPD 与 GRPO 的训练动态；AIME25 上 MOPD 更快恢复 teacher-level performance。[13-14]
- Table 3 显示 ArenaHard 上 MOPD 52 steps 达到 Hard Prompt 85.5 / Creative Writing 71.0，而 RLHF 160 steps 仍 Hard Prompt 80.7 / Creative Writing 71.2。[14]
- 报告明确解释效率来源：MOPD 是 dense token-level advantage，GRPO 是 shared across generated tokens 的 sparse sequence-level reward。[14]

## Gaps / Open Questions

- 具体 MOPD objective 细节、teacher routing、teacher logits serving 和多 teacher weighting 需要进一步回读公式/appendix/repo。
- 报告主线更关注效果和效率，未完整披露所有 teacher selection criteria。
- MOPD 后还继续 RLHF / long-context / code / SWE RL，因此最终能力提升不能全归因于 MOPD。

## Lookup-only

- Table 3 matched checkpoint numbers。[14]
- MOPD rollout size: 4, steps: 52, max response length: 98K。[25]

## Evidence Anchors

- 1: high-level MOPD contribution。
- 10: Cascade placement。
- 13-14: MOPD dynamics and efficiency comparison。
- 25: hyperparameters。
