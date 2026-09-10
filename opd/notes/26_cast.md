---
title: "CAST: Non-Privileged Clipped Asymmetric Self-Teaching with Advantage Flipping for GRPO"
authors: [Yang Li, et al.]
org: other
year: 2026
venue: arxiv
arxiv_id: 2606.00172
url: https://arxiv.org/abs/2606.00172

confidence: 4
verified: a

addresses:
  - stop-gradient-bias
  - cliff-prompt-zero-gradient
  - coarse-credit-assignment

decisions:
  rollout: student
  loss: advantage
  signal: logit
  iteration: one-shot
  filter: none
  extra: none
---

> **一句话**：answer-free self-teacher shaping GRPO token advantages。

## 核心做法

CAST 不使用 privileged answer/context，而是用 stop-gradient self-teacher 对 GRPO rollout 中的 token-level advantages 做 correctness-conditioned shaping：正确轨迹中 teacher-negative token 被赋负 advantage，错误轨迹中 teacher-positive token 得到 bounded positive local advantage；all-correct/all-wrong group 里用 sign-constrained base advantage 避免 group-relative advantage 塌成零。

$$A_{t}^{\mathrm{CAST}}=\mathrm{clip}\big(A_{\mathrm{GRPO}}+\Delta_{\mathrm{self\mbox{-}teacher}}(y_t,\mathrm{correct})\big)$$

实操含义：CAST 是 OPD/OPSD 与 GRPO 交界处的 direct novelty-risk：它声称不需要 privileged information，也能把 token-level self-teacher gap 注入 RLVR。

## 谱系位置

- 上游：GRPO / OPSD — GRPO 缺 dense token signal，OPSD 依赖 privileged information；CAST 尝试 answer-free token shaping。
- 同期：OPD+ — 两者都关注 advantage 设计；OPD+ 修 stop-gradient bias，CAST 用 detached self-teacher 做局部 sign flipping。
- 下游：self-distilled policy gradient / answer-free OPSD — 可以作为无 privilege 自蒸馏 baseline。

## 优缺点

- ✅ [作者 ack Abstract]: 不依赖 privileged answer，直接用 trajectory correctness 与 self-teacher gap 塑形 token advantages。
- ✅ [作者 ack Abstract]: 处理 all-correct/all-wrong groups 的 zero-variance problem。
- ⚠️ [作者 ack §6]: validation-tuned clipping 与 token-gap hyperparameters 增加调参，且可能产生更长输出、提高推理成本。

## headline number

无 Table/Fig anchor 的摘要数字不放入 headline number。

<!-- pdf: arXiv abstract / §6 Conclusion -->
