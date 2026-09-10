---
title: "Group-in-Group Policy Optimization for LLM Agent Training"
year: 2025
venue: neurips-2025
paper_type: core-rl-method
lifecycle_role: canonical-anchor
boundary_risk: none

failure_modes: [sparse-delayed-reward, long-horizon-credit]
design_knobs: [credit-unit, advantage-estimation]

rl_env: mixed
rl_interaction: online
rl_reward: sparse
rl_credit: step
---

## 一句话定位

GRPO-family agentic step-credit anchor。

## 难题 / Failure Modes

| Failure mode | 本文诊断 | 本文处理方式 | 仍未解决 |
|---|---|---|---|
| `sparse-delayed-reward` | trajectory outcome 太粗，无法判断哪个中间动作真正有贡献。 | 在 episode-level advantage 外加入 step-level micro advantage。 | 仍依赖相同/可对齐状态形成局部比较组。 |
| `long-horizon-credit` | GRPO 把整条轨迹成败摊给所有动作。 | 用 anchor-state grouping 比较同一 state 下不同 actions。[PDF abstract] | 开放 web/GUI/code 环境里 state recurrence 未必足够。 |

## 方法机制

GiGPO 对同一 task 采样一组 multi-turn trajectories，先按完整 trajectory 计算 macro relative advantage，再用 repeated/shared anchor state 构造 step-level action groups 计算 micro relative advantage。[PDF abstract] 最终 policy update 同时使用 trajectory-level 和 step-level group-relative signal。机制增量是 **把 GRPO 的 credit unit 从 trajectory 推到 anchor-state step group**，不是引入 critic 或新 reward model。

## 相对方法

| 对比对象 | 对方问题 | 本文改动 | 代价 / 风险 |
|---|---|---|---|
| GRPO | trajectory credit 太粗。 | 加 step-level micro relative advantage。 | 需要能构造 anchor-state groups。 |
| BEACON | 不依赖 repeated state，而依赖 milestone。 | GiGPO 更轻量，不需要 milestone detector。 | 长 horizon 下 repeated state 可能稀疏。 |
| HCAPO | 用 hindsight critic 回推 step Q。 | GiGPO 保持 critic-free。 | credit 更受 state matching 质量限制。 |

## 设计决策 / Design Knobs

| Design knob | 本文选择 | 常见替代选择 |
|---|---|---|
| `credit-unit` | anchor-state step group | trajectory / milestone segment / token / tool-call |
| `advantage-estimation` | macro trajectory advantage + micro step relative advantage | trajectory-only GRPO / critic Q / process reward |

## 方法优缺点 / 适用边界

- 优势：机制简单、critic-free，并且成为后续 BEACON/HGPO/HCAPO 等 credit 方法的直接 anchor。
- 优势：作者报告 ALFWorld/WebShop/search QA 上优于 GRPO，且不增加 GPU memory、rollout 或明显时间成本。[PDF abstract]
- 不足 / 风险：核心假设是存在足够 anchor-state recurrence；状态唯一性强或历史上下文差异大时，step group 会稀疏或 biased。

<!-- meta:
authors: [Lang Feng, Zhenghai Xue, Tingcong Liu, Bo An]
url: https://arxiv.org/abs/2505.10978
arxiv_id: 2505.10978
pdf: papers/2505.10978-gigpo-agent-training.pdf
brief: _meta/briefs/papers/2505.10978_25_gigpo-agent-training.md
survey: Credit Assignment / GFCR / Landscape
rl_optimizer: grpo-like
rl_data_reuse: none
rl_warm_start: standard
-->
