---
title: "KDRL: Post-Training Reasoning LLMs via Unified Knowledge Distillation and Reinforcement Learning"
authors: [Hongling Xu, et al.]
org: huawei-noah-hit
year: 2025
venue: arxiv
arxiv_id: 2506.02208
url: https://arxiv.org/abs/2506.02208

confidence: 3
verified: a

surveys:
  song-2026: "§4.3 reward-augmented distillation; §8.3 compute budget allocation"

addresses:
  - coarse-credit-assignment
  - no-new-capability

decisions:
  rollout: student
  loss: reward
  signal: logit
  iteration: one-shot
  filter: none
  extra: rm
---

> **一句话**：KD 与 RL 联合优化的 post-training 桥接基线。

## 核心做法

KDRL 把 teacher supervision 与 self-exploration 放进同一 post-training objective：一边用 policy gradient 最大化 rule-based reward，一边最小化 student/teacher 分布间的 reverse KL。它试图解决纯 RL 初始策略难以探索高 reward trajectory、纯 KD 又受 teacher ceiling 限制的问题。

$$\mathcal{L}_{\mathrm{KDRL}}\approx -\mathbb{E}[R_{\mathrm{rule}}\log\pi_\theta]+\alpha D_{\mathrm{KL}}(\pi_\theta\|\pi_T)$$

实操含义：KDRL 是“KD as dense variance-reducing teacher prior + RL as beyond-teacher exploration”的代表，后续 TGPO/RLAD 主要批评并改进它的 additive/uniform coupling。

## 谱系位置

- 上游：GKD / OPD — 使用 teacher logits 作为 dense guidance。
- 同期：LUFFY — LUFFY 用 off-policy traces + on-policy rollouts，KDRL 用 teacher distribution + reward joint objective。
- 下游：TGPO / RLAD — survey 明确把它们看作对 KDRL uniform KL regularization 的更紧耦合或 selective trust-region 改进。

## 优缺点

- ✅ [song-2026 §4.3]: KD+RL 组合能在小模型 bootstrap 与 reward-guided refinement 之间折中。
- ✅ [作者 ack Abstract]: 统一 teacher supervision 与 self-exploration，改善 reasoning benchmark 上的效率与性能。
- ⚠️ [song-2026 §4.3]: additive KL penalty 需要平衡超参，且可能盲目把 student 拉向 teacher 自身不能解决的 suboptimal trajectory。

## headline number

无 Table/Fig anchor 的摘要数字不放入 headline number。

<!-- pdf: arXiv abstract -->
<!-- song-2026: §4.3 Reward-Augmented Distillation / §8.3 Compute Budget Allocation -->
