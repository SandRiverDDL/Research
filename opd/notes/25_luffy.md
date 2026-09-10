---
title: "Learning to Reason under Off-Policy Guidance"
authors: [Yifan Yan, et al.]
org: other
year: 2025
venue: arxiv
arxiv_id: 2504.14945
url: https://arxiv.org/abs/2504.14945

confidence: 4
open_source: yes
verified: a

surveys:
  song-2026: "§5.2 black-box and API-constrained distillation; §8.3 compute budget allocation"

addresses:
  - capacity-gap
  - reward-hacking

decisions:
  rollout: mixed
  loss: advantage
  signal: outcome
  iteration: continuous
  filter: none
  extra: none
---

> **一句话**：reasoning RL 与示范轨迹混合训练路线。

## 核心做法

LUFFY 针对 zero-RL 只能从模型自身输出中学习、难以越过初始能力边界的问题，把 stronger policy 的 off-policy reasoning traces 引入 GRPO/RLVR 训练；同时用 regularized importance sampling 做 policy shaping，避免 student 只表面模仿高概率 token 而忽视低概率但关键的 reasoning action。

$$\hat{A}\leftarrow \hat{A}_{\mathrm{on}}+\rho_{\mathrm{reg}}(y)\hat{A}_{\mathrm{off}}$$

实操含义：LUFFY 不是严格 white-box OPD，但它定义了 OPD/RL 之间的重要边界：off-policy guidance 可以扩展探索空间，但必须校正 superficial imitation。

## 谱系位置

- 上游：GRPO / RLVR — zero-RL 只靠 on-policy rollouts，LUFFY 引入 off-policy reasoning traces。
- 同期：KDRL — KDRL 结合 teacher distribution 与 reward；LUFFY 结合 off-policy demonstrations 与 on-policy exploration。
- 下游：TGPO / RLAD — 都试图把 teacher/off-policy guidance 更选择性地接入 policy update。

## 优缺点

- ✅ [song-2026 §5.2]: regularized importance sampling 强调 unfamiliar yet effective actions，缓解 superficial imitation。
- ✅ [作者 ack Abstract]: off-policy guidance 能让 student 学到自身初始策略之外的 reasoning behavior。
- ⚠️ [song-2026 §5.2]: 训练信号不全来自 on-policy teacher scoring，作为 OPD 证据时应标注为 adjacent RL/KD bridge。

## headline number

无 Table/Fig anchor 的摘要数字不放入 headline number。

<!-- pdf: arXiv abstract -->
<!-- song-2026: §5.2 Off-Policy Knowledge Integration / §8.3 Compute Budget Allocation -->
