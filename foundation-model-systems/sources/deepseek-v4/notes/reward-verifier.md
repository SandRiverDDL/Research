# DeepSeek-V4 Reward / Verifier Signals

```yaml
---
source_id: deepseek-v4
section_type: reward-verifier
stage: post-training
substage: reward-verifier
depth: surface
confidence: medium
need_expert_review: false
---
```

## Scope / Coverage

- 覆盖页段：TR pages 29-30。
- 覆盖阶段：hard-to-verify tasks 的 reward / verifier design。
- 子问题：
  - DeepSeek 公开了哪些 GRM / rubric-guided RL 信息？
  - GRM 能否当成可复用 recipe？
  - 它和 reasoning modes、OPD teachers 的关系哪里不清楚？

## Core Summary

- 事实：DeepSeek-V4 在 hard-to-verify tasks 上使用 rubric-guided RL data 和 Generative Reward Model (GRM)。[29-30]
- 事实：报告称 actor model 本身充当 GRM，而不是依赖传统 scalar reward model。[29-30]
- 解释：GRM-as-actor 可能是重要方向，但当前披露更像 high-level design claim，不是完整可复现 recipe。[29-30]
- 解释：这至少说明 DeepSeek 对 hard-to-verify tasks 不只依赖 binary verifier，而是尝试用生成模型按 rubric 产生 reward-like judgment。[29-30]

## Mechanism Map

- Rubric-guided RL data 提供 hard-to-verify tasks 的评价标准。[29-30]
- Actor model 被描述为能够 natively function as GRM，用于生成 reward-like judgment。[29-30]
- GRM 描述与 Non-think / Think High / Think Max reasoning modes 相邻；不同 reasoning modes 有不同 length penalties 和 context windows。[29]

## What Is Not Disclosed

- GRM 如何训练、输入输出格式是什么、如何接入 RL objective，没有公开。
- Actor-as-GRM 是否共享 weights，还是指同一 model family / checkpoint，表述不够明确。
- Rubric-guided data 的规模、来源和质量控制没有公开。
- GRM 和 OPD teachers 的关系不清楚：它是 specialist training 的 reward source，还是也参与 consolidation/evaluation。

## Transfer Hooks

- worth-internalizing: hard-to-verify tasks 需要 rubric / generative judgment，而不只是 binary verifier。
- try-at-small-scale: 更可行的实验是比较 verifier、LLM judge、rubric judge、self-critique reward 的稳定性。
- lookup-only: DeepSeek 的 GRM 名称和 actor-as-GRM claim；在更多细节公开前不要当作完整 recipe。

## Split Check

- current scope: GRM / rubric-guided reward only。
- if this file grows beyond ~220 lines, split by: GRM procedure vs reward-verifier comparison。

## Evidence Anchors

- 29-30: reasoning modes、rubric-guided RL data、GRM-as-actor。
