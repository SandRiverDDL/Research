---
title: "Bridging Reasoning Trajectories in On-Policy Distillation via Near-Future Guidance"
authors: [Yuxuan Jiang, et al.]
org: umbc
year: 2026
venue: arxiv
arxiv_id: 2606.00305
url: https://arxiv.org/abs/2606.00305

confidence: 4
verified: a

addresses:
  - flawed-prefix-trap
  - coarse-credit-assignment
  - compounding-error

decisions:
  rollout: student
  loss: adaptive-kl
  signal: logit
  iteration: one-shot
  filter: trajectory-level
  extra: none
---

> **一句话**：reasoning fork 判别的近未来路线。

## 核心做法

论文指出 OPD 是 trajectory-sampled 但 token-learned：局部 high-loss token 可能只是措辞差异，即使找到真实分叉，单点 reverse-KL 也未必能修复后续路径。对每个 high-loss 候选位置，TOPD 回到同一个 student prefix，让 teacher/student 各生成 $K=50$ 个 token，用 embedding-space Optimal Transport 距离判断是否发生真实 reasoning fork；再用 OT transport plan 将 teacher 的短未来轨迹变成多个 student 位置的 soft targets。

$$
D_{\mathrm{OT}}(T_{t:t+K},S_{t:t+K}),\qquad
\mathcal L_{\mathrm{TOPD}}=\mathcal L_{\mathrm{OPD}}+\lambda\sum_{i=0}^{K-1}
\mathrm{KL}(\tilde y_{t+i}\|p_S(\cdot|c_{t+i})).
$$

实操含义：OPD token 选择不应只看局部 loss，还要看该位置是否真的改变后续解题轨迹；这里的 TOPD 是 Trajectory-aware OPD，与 Truncated OPD 重名。

## 机制发现（可选）

- [作者 ack §2.1]: token loss 与 50-token OT distance 的相关性很弱（Pearson 0.126 / Spearman 0.143）；29.23% high-loss tokens 落在典型 low-divergence 区域。
- [作者 ack §2.2]: 即使是真 divergent token，孤立 token correction 也可能进入新的错误分支，形成 token-by-token learning trap。
- [作者 ack §3]: TOPD 包含 high-loss + high-OT divergence detection，以及 OT-aligned short-window teacher signal injection。

## 谱系位置

- 上游：TIP (2026) — TIP 从 token importance 选择监督；本篇用近未来轨迹判断 importance。
- 同期：Revisiting OPD (2026) — 都关心 sampled/local token 信号不可靠，本篇更强调后续 trajectory consequence。
- 同期：Trajectory-Refined Distillation (2026) — 都从单点 token supervision 转向 trajectory-aware correction。

## 优缺点

- ✅ [作者 ack paper brief Abstract / §3]: 把 high-loss token filtering 从局部 loss 判断升级为 near-future trajectory consequence 判断。
- ⚠️ [作者 ack §4.1]: 额外 teacher/student short continuation 与 OT 使训练时间达到标准 OPD 的 1.41×。
- ⚠️ [解释]: OT 只判断 student 是否接近 teacher trajectory，不验证 teacher 路径是否正确或是否真正决定最终 outcome。

## headline number

- 三个数学 benchmark 平均：OPD 47.8 → TOPD 52.2（§Table 1）
- AIME24 60.0 → 63.3；AIME25 46.7 → 53.3（§Table 1）
- 固定-prefix 局部修复：OT distance 0.538 → OPD 0.350 → TOPD 0.204（§5.2 Figure 5）

<!-- pdf: arXiv PDF v2 §2-5 / Tables 1-2 / Figure 5 -->
