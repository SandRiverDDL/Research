# Open-Reasoner-Zero Source Dossier

```yaml
---
source_id: open-reasoner-zero
source_type: open-project
org: StepFun / Tsinghua University
release_date: 2025-03-31
priority: S
status: section-notes
openness: fully-open
confidence: high
lineage: reasoner-zero
role: full-tr
base_source: qwen2.5-base
---
```

## 一句话

Open-Reasoner-Zero 是对 R1-Zero 命题最有价值的开放检验之一：它从 Qwen2.5 Base 直接训练，使用 vanilla PPO、learned critic、GAE(γ=λ=1)、binary correctness reward 且不使用 KL regularization，并开放代码、数据、policy/critic 权重与训练参数。[3-12]

## 为什么重要

- 它把“pure RL reasoning”从 DeepSeek 的不可完整复现 recipe 变成可审计实验。
- 它与 R1-Zero 的关键分歧不是小调参，而是 PPO critic vs GRPO group baseline；critic 是否能为重复/退化 token 提供更好的 credit assignment 是核心研究问题。[5, 10]
- 它显示 data scale/diversity、GAE horizon 与 KL removal 可能比新算法命名更重要。[5-9]

## 核心机制 / Takeaways

- 从 Qwen2.5-{0.5B,1.5B,7B,32B} Base 直接 RL，不做 SFT 或 distillation。[3-7]
- PPO 的 value function 为每个 token 估值；终局 binary reward 配合 γ=λ=1，使 advantage 简化为 `R - V(s_t)`。[4-6]
- 移除 KL loss/reward shaping，降低 reference-model 开销并放开 policy exploration。[6, 9]
- 只验证答案正确性，不另加 format reward；base model 很快学会 answer tags。[6-9]
- 57K 级、经过难度过滤的多域 reasoning data 比小型 MATH train 更能持续扩展 reward/response length。[7, 9]

## Source Bundle

- technical report: https://arxiv.org/abs/2503.24290
- repository: https://github.com/Open-Reasoner-Zero/Open-Reasoner-Zero
- local PDF: `/Users/chy/Research/foundation-model-systems/papers/open-reasoner-zero/open-reasoner-zero.pdf`
- last checked: 2026-07-21

## Lineage / Delta

- lineage：DeepSeek-R1-Zero replication family。
- role：open recipe 与 algorithmic counterpoint，不是 frontier general assistant。
- base source：Qwen2.5 Base。

## 最大证据缺口

- 主要 eval 仍集中在 math/science reasoning；对 general assistant、safety 和 agent behavior 的外推有限。
- “critic 优于 GRPO”由本项目实验支持，但不是跨所有实现、scale 和 data 的普遍定论。
- Fully-open 指该项目核心 artifacts；底层 base model 的预训练仍不是 fully open。

## Lens Hooks

- rl-training: PPO vs GRPO, GAE horizon, no-KL RL.
- reward-verifier: minimalist binary reward.
- data: difficulty filtering and scale.
- openness：公开 critic，将其作为 reproducibility artifact。

## 阅读入口

- `section-index.md`: method/ablation/appendix 路由。
- `notes/rl-training.md`: PPO recipe。
- `notes/critic-and-advantage.md`: critic 与 credit assignment。
- `notes/data-reward.md`: 数据和 reward 最小化。
- `notes/claims-and-gaps.md`: 结论边界。
