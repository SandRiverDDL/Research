---
title: "Escaping the KL Agreement Trap in On-Policy Distillation"
authors: [Haoran Xin, et al.]
org: hkust-eit
year: 2026
venue: arxiv
arxiv_id: 2606.09471
url: https://arxiv.org/abs/2606.09471

confidence: 4
verified: a

addresses:
  - flawed-prefix-trap
  - no-new-capability

decisions:
  rollout: student
  loss: adaptive-kl
  signal: logit
  iteration: one-shot
  filter: support-truncation
  extra: none
---

> **一句话**：KL agreement trap 的失败模式卡。

## 核心做法

论文指出一种低 KL 假象：student rollout 进入退化状态后，teacher 可能因为局部 vocabulary shift 与 degraded prefix 产生 low-KL agreement，导致 OPD 更新落入无效或错误方向。KAT 用在线 local KL statistic 和 adaptive threshold 触发 rollout termination。

$$\mathrm{trap}(s_t)=\mathbb{1}[D_{\mathrm{KL}}(\pi_T(\cdot|s_t)\|\pi_\theta(\cdot|s_t))<\tau_t]$$

实操含义：低 KL 不一定代表 student 接近 teacher，也可能代表 teacher 被错误 prefix 困住。

## 机制发现（可选）

- [作者 ack paper brief §3.1]: low-KL dynamics 被作为 OPD rollout 中的系统现象分析，而不是单个异常样本。
- [作者 ack paper brief §3.2-3.3]: 论文用 gradient geometry 和 teacher vocabulary shift 解释 low-KL agreement 为什么会变成 trap。
- [作者 ack paper brief §4.1-4.3]: KAT 由 local KL statistic、adaptive threshold calibration 和 online trigger / termination 组成。

## 谱系位置

- 上游：Revisiting OPD (2026) — flawed-prefix trap 的近邻诊断。
- 同期：Trust Region OPD (2026) — 都在判断 teacher signal 何时可信；本篇强调 low-KL agreement 也可能不可信。
- 同期：Your Teacher Can't Help You Here (2026) — 都把长程 prefix 漂移视为 teacher supervision 衰减源。

## 优缺点

- ✅ [作者 ack paper brief §3-4]: 明确区分“KL 小”与“teacher supervision 可靠”，补上 OPD trust 判断的反例。
- ⚠️ [作者 ack paper brief §5.3]: termination threshold 和 stage-wise supervision 的稳健性依赖 ablation，不宜只凭主结果外推。

## headline number

未从 paper brief 核到 Table/Fig anchor 的数字不放入 headline number。

<!-- pdf: cached arXiv HTML brief Abstract / §3 / §4 / §5 / Appendix B-C -->
