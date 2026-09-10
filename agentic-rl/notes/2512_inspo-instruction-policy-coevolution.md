---
title: "Agentic Policy Optimization via Instruction-Policy Co-Evolution"
year: 2025
venue: arxiv
paper_type: core-rl-method
lifecycle_role: frontier-candidate
boundary_risk: recipe

failure_modes: [warm-start-ceiling, exploration-collapse, replay-bias]
design_knobs: [prompt-action-interface, trajectory-filtering, replay-off-policy]

rl_env: tool
rl_interaction: online
rl_reward: verifier
rl_credit: trajectory
---

## 一句话定位

把 instruction population 放进 GRPO loop。

## 难题 / Failure Modes

| Failure mode | 本文诊断 | 本文处理方式 | 仍未解决 |
|---|---|---|---|
| `warm-start-ceiling` | 静态人工 instruction 可能不适合当前 policy，且最优 instruction 会随训练变化。 | 维护 instruction candidates population，和 policy 一起在线演化。[PDF §3] | 依赖强 LLM optimizer。 |
| `exploration-collapse` | 固定 instruction 会限制 agent 探索策略空间。 | 低表现 instruction 被 prune，高表现 instruction 生成新候选。 | 可能更像 prompt/protocol recipe。 |
| `replay-bias` | failure trajectories 可提供 instruction 修正信号。 | replay buffer 记录低 reward 经验，供 reflection-based instruction generation 使用。 | replay 主要服务 instruction，不是 off-policy RL update。 |

## 方法机制

INSPO 把 instruction 当作 agent policy context 的一部分：训练时从 instruction population 中采样 instruction，reward 同时用于 GRPO-style policy gradient 和 instruction importance weight 更新。低权重 instruction 被 successive halving pruning，高权重 instruction 作为 parent，由 LLM optimizer 基于 replay buffer 里的失败轨迹生成新 instruction。[PDF §3.1-3.2] 机制增量是 **让 prompt/instruction 和 policy 在 online RL loop 中共同进化**。

## 相对方法

| 对比对象 | 对方问题 | 本文改动 | 代价 / 风险 |
|---|---|---|---|
| GRPO with static prompt | instruction 固定。 | instruction population 动态采样/加权。 | prompt optimizer 依赖强模型。 |
| ReSkill / SAPO | 演化 skill。 | INSPO 演化 instruction/protocol。 | 更像 prompt-level 机制。 |
| Replay / reflection methods | 只做离线改 prompt。 | 用 on-policy failure 生成新 instruction。 | replay bias 可能影响 instruction selection。 |

## 设计决策 / Design Knobs

| Design knob | 本文选择 | 常见替代选择 |
|---|---|---|
| `prompt-action-interface` | dynamic instruction population | static prompt / hand-written protocol |
| `trajectory-filtering` | low-reward trajectories drive instruction generation | all trajectories / success-only / heuristic filters |
| `replay-off-policy` | replay buffer for reflection, not direct policy update | no replay / off-policy gradient / data curation |

## 方法优缺点 / 适用边界

- 优势：把 prompt/instruction 从固定超参变成 RL loop 中可学习的协议变量，适合 search-tool QA。
- 不足 / 风险：边界风险是 recipe/prompt；主要贡献不在 optimizer 本体，且依赖 Gemini 2.5 Pro 等强 LLM optimizer。[Appendix A]

<!-- meta:
authors: [Han Zhou, Xingchen Wan, Ivan Vulić, Anna Korhonen]
url: https://arxiv.org/abs/2512.01945
arxiv_id: 2512.01945
pdf: papers/2512.01945-inspo-instruction-policy-coevolution.pdf
brief: _meta/briefs/papers/2512.01945_inspo-instruction-policy-coevolution.md
survey: post-survey strict-core recall
rl_optimizer: grpo-like
rl_data_reuse: replay
rl_warm_start: standard
-->
