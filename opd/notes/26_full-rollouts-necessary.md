---
title: "Are Full Rollouts Necessary for On-Policy Distillation?"
authors: [Yaocheng Zhang, et al.]
org: casia-meituan
year: 2026
venue: arxiv
arxiv_id: 2605.31490
url: https://arxiv.org/abs/2605.31490

confidence: 4
verified: a

addresses:
  - sgo-generation-cost
  - flawed-prefix-trap
  - compounding-error

decisions:
  rollout: student
  loss: reverse-kl
  signal: logit
  iteration: one-shot
  filter: support-truncation
  extra: none
---

> **一句话**：full-rollout 必要性的直接挑战。

## 核心做法

论文把 OPD 的 rollout horizon 从默认工程细节提升为优化决策：full rollout 既贵，又会在训练早期把 student 带到 teacher 不熟悉的 late-prefix states。它提出 Progressive OPD 逐步扩展 rollout horizon，以及 Truncated OPD 固定只用短前缀训练。

$$\mathcal{L}_{\mathrm{OPD}}^{\le H}=\mathbb{E}_{y_{\le H}\sim\pi_\theta}\sum_{t\le H}D(\pi_T(\cdot|y_{<t})\|\pi_\theta(\cdot|y_{<t}))$$

实操含义：如果后缀 teacher 信号随 student prefix 漂移而变差，缩短 rollout 可能同时省算力和减少错误监督。

## 机制发现（可选）

- [作者 ack paper brief Abstract / §3-4]: OPD 的学习信号来自中间 token teacher feedback，不依赖 final-answer reward，因此 full rollout 不是目标定义上的硬需求。
- [作者 ack paper brief §3.1-3.3]: 长 horizon 同时带来 degraded teacher reliability 和 future-noise accumulation，论文给出 shorten log-ratio horizon 与 control rollout horizon 两条设计原则。
- [作者 ack paper brief §4.1-4.2]: POPD 逐步扩展 horizon，TOPD 固定用 truncated rollouts，二者分别服务于效率提升和 cost-performance tradeoff。

## 谱系位置

- 上游：GKD / MiniLLM (2024) — 默认把 student rollout 当作完整序列处理。
- 同期：Less is More (2026) — 同样怀疑长后缀 teacher signal，区别是本篇把问题抽象成 horizon necessity。
- 同期：Revisiting OPD (2026) — Revisiting 诊断 sampled-token 支持集失真，本篇关注 rollout 长度是否本身过度。

## 优缺点

- ✅ [作者 ack paper brief §3-4]: 把 OPD 计算成本、teacher reliability 和 horizon 控制统一成一个明确设计轴。
- ✅ [作者 ack §5.1]: 所有 LLM 方法固定训练 2 epochs、每 5 steps 用 full rollout 做 avg@16 evaluation；主表报告最后 10 次 evaluation 的平均值，不靠挑最佳 checkpoint 获得 speedup。
- ⚠️ [作者 ack paper brief §5.2]: TOPD 在 autoregressive control task 中失败，说明 truncated rollout 不是通用替代 full rollout 的免费午餐。
- ⚠️ [解释]: “更快”指相同 epochs 下每步生成、teacher scoring 和反向传播的 token 更少，从而降低 wall-clock；不是用更少 optimizer steps 收敛。

## headline number

- R1-Distill-1.5B：OPD 29.7h；POPD 10.1h；TOPD-25% 10.2h；TOPD-10% 5.3h（§Table 1）
- OpenMath-1.5B：OPD 39.6h；POPD 10.0h；TOPD-10% 5.2h（§Table 1）

<!-- pdf: arXiv PDF v1 §3-6 / Tables 1-2 -->
