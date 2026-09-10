---
title: "Learn the Ropes, Then Trust the Wins: Self-imitation with Progressive Exploration for Agentic Reinforcement Learning"
year: 2025
venue: iclr-2026
paper_type: core-rl-method
lifecycle_role: frontier-candidate
boundary_risk: recipe

failure_modes: [sparse-delayed-reward, exploration-collapse, replay-bias]
design_knobs: [replay-off-policy, reward-shaping, exploration-strategy]

rl_env: mixed
rl_interaction: replay
rl_reward: dense
rl_credit: trajectory
---

## 一句话定位

给 GRPO/GiGPO 加 curriculum self-imitation replay。

## 难题 / Failure Modes

| Failure mode | 本文诊断 | 本文处理方式 | 仍未解决 |
|---|---|---|---|
| `sparse-delayed-reward` | long-horizon agent 只有最终成功信号，早期工具探索容易被惩罚。 | 用 tool-call intrinsic reward 促进早期环境交互。 | reward schedule 依赖先验，不能自动判断何时该停止工具探索。 |
| `exploration-collapse` | naive entropy maximization 在多轮分布漂移下可能崩溃或发散。 | 通过 self-imitation replay 与 entropy control 逐步从探索转向利用。 | curriculum 是预设调度，不是状态自适应。 |
| `replay-bias` | 旧 successful trajectories 来自旧 policy，直接 replay 会错估当前 advantage。 | 用 FIFO baseline buffer 重估 off-policy advantage，只保留双正 advantage 样本。 | 仍是启发式 off-policy correction。 |

## 方法机制

SPEAR 在 GRPO-like on-policy 更新之外维护 replay buffer `D` 和 baseline buffer `D_R`：当前 group rollout 后，正 advantage 轨迹进入 replay；当 buffer 满后，用最近 baseline 的中位数重算 replay trajectory 的 advantage，并把 `J_GRPO + gamma * J_SIL` 作为总目标更新 policy。[brief p.5-p.6] 它同时把 outcome reward、tool-call reward 和 format reward 合成训练 reward，并让 tool-call reward 随训练衰减，避免模型为了拿内在奖励而无意义延长工具交互。[brief p.7] 论文还提出 Dr.BoT 作为强 GRPO 变体基线，并报告 SPEAR 可插到 GRPO、GiGPO、Dr.BoT 上，在 ALFWorld/WebShop 和 AIME 上都有增益。[brief p.8-p.9]

## 相对方法

| 对比对象 | 对方问题 | 本文改动 | 代价 / 风险 |
|---|---|---|---|
| GRPO | 只用当前 batch 的 group advantage，探索利用切换粗。 | 加 positive replay 与 SIL auxiliary objective。 | 引入 off-policy replay bias。 |
| GiGPO | 已有 step/group credit，但不主动复用成功经验。 | 用 curriculum self-imitation 复用高收益轨迹。 | 与 GiGPO 的 credit 贡献需要拆开看。 |
| DAPO / Dr.GRPO tricks | 主要稳定训练或修正 bias。 | SPEAR 把 tricks 组合成 Dr.BoT，并另外加 replay / intrinsic reward。 | Dr.BoT 是 bag-of-tricks，方法归因可能混杂。 |

## 设计决策 / Design Knobs

| Design knob | 本文选择 | 常见替代选择 |
|---|---|---|
| `replay-off-policy` | replay positive-advantage trajectories and recalibrate with recent baseline. | no replay / raw replay / importance sampling. |
| `reward-shaping` | outcome + decayed tool-call intrinsic reward + format reward. | outcome-only / process reward / verifier reward. |
| `exploration-strategy` | curriculum shifts from skill/tool exploration to successful tactic exploitation. | entropy bonus / tree rollout / uncertainty branching. |

## 方法优缺点 / 适用边界

- 优势：补上了当前 GRPO-like agent 方法里常见的 replay/self-imitation 空位，且能作为 plug-in 接到 GRPO/GiGPO。
- 优势：明确处理 early exploration 和 late exploitation 的冲突，比单纯提高 entropy 更贴近长轨迹 agent。
- 不足 / 风险：SPEAR 和 Dr.BoT/GRPO/GiGPO 叠加，实验归因需要拆成 replay、intrinsic reward、entropy tricks 三部分看。
- 不足 / 风险：curriculum 调度和 reward 权重依赖先验，跨环境自动性不足。

<!-- meta:
authors: [Yulei Qin, Xiaoyu Tan, Zhengbao He, et al.]
url: https://arxiv.org/abs/2509.22601
arxiv_id: 2509.22601
pdf: papers/2509.22601-spear-self-imitation-progressive-exploration.pdf
brief: _meta/briefs/papers/2509.22601_spear-self-imitation-progressive-exploration.md
survey: user recall / SPEAR backward seed
rl_optimizer: grpo-like
rl_data_reuse: replay
rl_warm_start: standard
-->
