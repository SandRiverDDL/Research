---
title: "Learning beyond Teacher: Generalized On-Policy Distillation with Reward Extrapolation"
authors: [Wenkai Yang, et al.]
org: ruc-tencent
year: 2026
venue: arxiv
arxiv_id: 2602.12125
url: https://arxiv.org/abs/2602.12125

confidence: 3
open_source: yes
verified: a

surveys:
  song-2026: "References; OPD method coverage audit"

addresses:
  - no-new-capability
  - capacity-gap
  - reward-hacking

decisions:
  rollout: student
  loss: advantage
  signal: logit
  iteration: one-shot
  filter: none
  extra: none
---

> **一句话**：OPD 奖励外推的统一框架。

## 核心做法

论文把标准 OPD 推成 dense KL-constrained RL 的一个特例：reward 项和 KL regularization 默认等权，reference model 也可以更灵活。G-OPD 在这个框架里加入 reward scaling factor，λ>1 的 ExOPD 允许 student 沿 teacher reward 方向外推，从而尝试超出 teacher 当前边界。

$$\max_\theta\ \mathbb{E}_{y\sim\pi_\theta}[\,\lambda r_T(x,y)-\mathrm{KL}(\pi_\theta\|\pi_{\mathrm{ref}})\,]$$

实操含义：OPD 不只能“贴近 teacher”；当 teacher 是同一 base 经 domain RL 得到的专家时，适度 reward extrapolation 可以把多个专家能力合并回统一 student。

## 机制发现（可选）

- [作者 ack §3.2]: 标准 OPD 对应 λ=1；λ∈(0,1) 是 reward interpolation，λ>1 是 reward extrapolation。
- [作者 ack Abstract / §4]: 在 multi-teacher setting 中，ExOPD 可让统一 student 超过单个 domain teacher 的边界。
- [作者 ack §4.2.3 / §5]: strong-to-weak setting 下，把 reference 设为 teacher pre-RL base 可做 reward correction，但需要访问额外大模型并计算其 log-prob。

## 谱系位置

- 上游：GKD / MiniLLM (2024) — 继承 student-generated trajectories 上的 teacher logit supervision。
- 同期：Extrapolation Cliff (2026) — 本文强调 λ>1 的收益；Extrapolation Cliff 给出 structured-output 场景中过大 λ 的安全阈值。
- 同期：OPD+ (2026) — 两者都把 OPD 写成 RL-style objective；OPD+ 关注 advantage / stop-gradient 的目标偏差。

## 优缺点

- ✅ [作者 ack §3.2]: 把 OPD、reference model choice 和 reward/KL relative weight 放进同一个可调框架。
- ✅ [作者 ack Abstract / §4]: 给出“超过 teacher 边界”的具体机制，而不是只把 OPD 当压缩方法。
- ⚠️ [作者 ack §4.2.3 / §5]: reward correction 依赖 teacher pre-RL variant，强模型不可得或 API-only teacher 场景难用。

## headline number

无 Table/Fig anchor 的摘要级提升不放入 headline number；multi-teacher surpass claim 保留在机制发现中。

<!-- pdf: arXiv HTML Abstract / §3.2 Generalized OPD / §4 Experiments / §5 Conclusion and Discussion -->
<!-- song-2026: References / survey-reference-audit -->
