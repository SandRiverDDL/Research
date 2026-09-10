---
title: "Self-Supervised On-Policy Distillation for Reasoning Language Models"
authors: [Zhiquan Tan, et al.]
org: tsinghua-beihang
year: 2026
venue: arxiv
arxiv_id: 2605.17497
url: https://arxiv.org/abs/2605.17497

confidence: 4
verified: a

addresses:
  - cross-rollout-credit
  - privileged-context-gap
  - coarse-credit-assignment

decisions:
  rollout: student
  loss: preference
  signal: verifier
  iteration: iterative
  filter: verifier-pass
  extra: none
---

> **一句话**：correct-wrong 对比的自监督路线。

## 核心做法

SSOPD 从 GRPO group 里抽取 process signal：correct completion 是当前 policy 已能解题的 witness，wrong completion 提供需要 correction 的 on-policy prefixes。它把 shortest correct completion 条件下的 teacher distribution 蒸馏到 longest wrong completion 的 prefixes，并用 frontier weight 聚焦 correct/wrong branches 共存的 prompts。

$$\mathcal{L}=\sum_tD(\pi(\cdot|y^{+}_{\le T^+},y^{-}_{<t})\|\pi_\theta(\cdot|y^{-}_{<t}))$$

实操含义：非 privileged 场景下，可以从同组成功/失败轨迹中抽取过程监督，而不是只依赖最终 verifier。

## 机制发现（可选）

- [作者 ack paper brief Abstract / §3.1]: mixed GRPO group 包含 correct witness 与 wrong prefixes，可转化为 dense process supervision。
- [作者 ack paper brief §3.2]: shortest-correct / longest-wrong 规则来自 stopping-time view，是 finite-group witness 近似。
- [作者 ack paper brief §3.3]: prompt-level frontier weight 把 auxiliary loss 集中到 correct 与 wrong branches 共存的位置。

## 谱系位置

- 上游：MOPD (2026) — 利用多 rollout 成败结构。
- 同期：ReNIO (2026) — 都强调错误轨迹的信息价值；SSOPD 更偏 correct-wrong 对比监督。
- 同期：HDPO / OPSD (2026) — 都用额外条件构造 teacher，但 SSOPD 更强调非外部 solution trace。

## 优缺点

- ✅ [作者 ack paper brief Abstract / §3]: 不需要外部 solution traces，就能把 terminal reward group 变成 dense correction signal。
- ⚠️ [作者 ack paper brief §4.3 / Appendix E]: frontier weight 和 selector choice 是关键超参，需要 ablation 支撑。

## headline number

未从 paper brief 核到 Table/Fig anchor 的数字不放入 headline number。

<!-- pdf: cached arXiv HTML brief Abstract / §3 / §4 / Appendix E -->
