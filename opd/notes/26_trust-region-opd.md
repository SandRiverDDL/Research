---
title: "Trust Region On-Policy Distillation"
authors: [Xingrun Xing, et al.]
org: samsung-oxford-pku
year: 2026
venue: arxiv
arxiv_id: 2606.01249
url: https://arxiv.org/abs/2606.01249

confidence: 4
verified: a

addresses:
  - large-policy-divergence
  - flawed-prefix-trap
  - capacity-gap

decisions:
  rollout: mixed
  loss: adaptive-kl
  signal: logit
  iteration: iterative
  filter: support-truncation
  extra: none
---

> **一句话**：teacher trust region 的稳定化路线。

## 核心做法

TrOPD 针对 teacher/student distribution mismatch 下的 sampled-token gradient outlier。对 student 实际生成的 token $x$，它借用 speculative decoding acceptance ratio 随机划分 trust region：

$$
P_{\mathrm{trust}}(x)=\min\left(\frac{\pi_T(x)}{\pi_S(x)},1\right),\qquad
M_x\sim\mathrm{Bernoulli}(P_{\mathrm{trust}}(x)).
$$

trust token 继续使用 sampled-token reverse-KL；outlier 不再承受极端 log-ratio，而改用 teacher Top-K forward-KL 提供“往哪里走”的支持集信号。训练初期还使用 teacher prefix + student continuation，teacher-prefix 长度按 cosine schedule 退火到 0。

实操含义：这是 token-level estimator stabilization，不是经典 TRPO 那种约束新旧 policy KL 的 trust region；“trust”表示 teacher 没有强烈否定该 sampled token，不等于 teacher 在语义上正确。

## 机制发现（可选）

- [作者 ack §3.2 / §4.2]: 当 $\pi_T(x)\ll\pi_S(x)$ 时，K1 reverse-KL 的 sampled-token log-ratio 产生极端负梯度；$P_{\mathrm{trust}}$ 将其变成平滑的随机分区，而不是固定阈值。
- [作者 ack §4.2]: 接受质量满足 $\pi_S(x)P_{\mathrm{trust}}(x)=\min(\pi_S(x),\pi_T(x))$，对应 teacher/student 的公共概率质量；outlier 使用 Top-K FKL 恢复 teacher-supported alternatives。
- [作者 ack §4.3]: Off-Policy Trust-Region Guidance 让 student 从 teacher prefixes 继续生成，并将 teacher-prefix 长度逐步退火到 0。

## 谱系位置

- 上游：TGPO (2026) — 同样处理 large policy divergence。
- 同期：Revisiting OPD (2026) — support truncation 是局部 token 可信区；TrOPD 是 state/region 可信区。
- 同期：KL Agreement Trap (2026) — 都指出局部分布指标需要小心解释。

## 优缺点

- ✅ [作者 ack paper brief §4]: 给 OPD 增加显式可靠区域和 outlier 处理，直接服务 large-policy-divergence。
- ⚠️ [解释]: likelihood ratio 只衡量相对概率；即使 $\pi_T(x)\ge\pi_S(x)$，两者也可能都几乎不认可该 token，更不能保证该 token outcome-relevant。
- ⚠️ [作者 ack §5.3]: adaptive trust region、outlier estimation 和 off-policy guidance 是组合包，需要依赖 ablation 判断各自贡献。

## headline number

- 数学设置：OPD 46.79 → TrOPD 49.85（§Table 5）
- DeepSeek 1.5B multi-domain：OPD 32.99 → TrOPD 37.61（§Table 3）
- Qwen3-SFT-1.7B multi-domain：OPD 48.29 → TrOPD 51.73（§Table 4）

<!-- pdf: arXiv PDF v3 §3.2 / §4.2-4.3 / §5 / Tables 3-5 -->
