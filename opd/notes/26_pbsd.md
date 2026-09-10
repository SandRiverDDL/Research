---
title: "PBSD: Privileged Bayesian Self-Distillation for Long-Horizon Credit Assignment"
authors: [Yang Tian, et al.]
org: msr
year: 2026
venue: arxiv
arxiv_id: 2606.09348
url: https://arxiv.org/abs/2606.09348

confidence: 2
verified: a

surveys:
  song-2026: "§5.2 privileged information; §7.2 long-horizon credit assignment; Table 9"

addresses:
  - privileged-context-gap
  - cross-rollout-credit
  - coarse-credit-assignment

decisions:
  rollout: student
  loss: advantage
  signal: logit
  iteration: one-shot
  filter: step-level
  extra: privileged-info
---

> **一句话**：Bayes-calibrated privilege 的 turn-level credit 路线。

## 核心做法

PBSD 把 sparse final reward 的 credit assignment 写成 posterior-to-prior probability ratio of verified answer，再用 Bayes rule 转成 standard student 与 answer-conditioned privileged teacher 的 likelihood ratio；自回归分解后得到 turn-level signals，判断每个 intermediate turn 是支持还是削弱最终 outcome。

$$\frac{P(a^\star|\tau)}{P(a^\star)}\ \propto\ \prod_t\frac{\pi_{\mathrm{priv}}(y_t|h_t,a^\star)}{\pi_\theta(y_t|h_t)}$$

实操含义：不是直接模仿 privileged teacher 的每个 token，而是把 privilege 转成和最终答案相关的 Bayes-calibrated credit signal。

## 谱系位置

- 上游：OPSD / privileged self-distillation — 使用 answer-conditioned teacher，但 PBSD 把它解释为 Bayesian evidence ratio。
- 同期：RLCSD / SOD — 都试图把 sparse outcome 转成更细粒度 token/step signal；PBSD 给出 Bayesian derivation。
- 下游：long-horizon agentic OPD — turn-level signals 适合搜索/工具调用类 sparse-reward 任务。

## 优缺点

- ✅ [作者 ack Abstract]: 将 sparse outcome supervision 转成 Bayes-calibrated turn-level credit signals。
- ✅ [song-2026 §5.2]: 相比强制模仿 privileged teacher，PBSD 用 reward-regularized optimum 避免直接匹配导致的能力退化。
- ⚠️ [song-2026 §7.2]: 仍依赖 privileged answer-conditioned teacher，instance-specific PI 的推理期缺失风险需要和 Many Faces 的结论一起看。

## headline number

无 Table/Fig anchor 的摘要数字不放入 headline number。

<!-- pdf: arXiv abstract -->
<!-- song-2026: §5.2 Privileged Information / §7.2 Long-Horizon Credit Assignment / Table 9 -->
