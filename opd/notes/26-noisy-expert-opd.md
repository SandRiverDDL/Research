---
title: "Behavior Cloning is Not All You Need: The Optimality of On-Policy Distillation for Noisy Expert Feedback"
authors: [Ved Sriraman, et al.]
year: 2026
venue: neurips-2026
paper_id: arxiv:2606.30923
source: https://arxiv.org/pdf/2606.30923
---

- **一句话**：在 noisy-expert 模型下证明 offline BC 与 online imitation 的样本复杂度分离，并提出面向噪声专家的 NAIL/NAILGUN。

- **Failure mode**：模仿带噪教师，却希望达到干净专家的表现；即使知道噪声机制，offline noisy trajectories 在最坏情况下也需要随 horizon 指数增长的样本。（§2–3，Proposition 1）

- **核心做法**

  1. 将观测专家建模为 `(1-η)π*+ην`，区分已知与未知 corruption；比较目标为干净专家，而非拟合带噪教师本身。（§2）
  2. 在 learner 访问的状态查询带噪专家；比较同一 rollout 状态分布下的教师标签与加入相同 corruption 的 learner 标签，以 augmented trajectory divergence 控制 clean-policy regret。（§4，Theorem 7、Corollary 1）
  3. 理论 NAIL 使用策略类混合与在线更新；实验 NAIL-F/R 改用 greedy student rollout 和梯度下降。未知噪声的 NAILGUN 还依赖 deterministic expert、smooth corruption 与可识别 margin。（§4–6）

- **方法增量**：说明带噪专家访问方式可改变 horizon 依赖：online 一般得到多项式依赖，额外 domination 条件下可 horizon-free；不等于普通 OPD 无条件最优。（Theorems 7–9）

- **关键证据与边界**

  - modular addition 与 GSM8K 比较 BC、OPD-F/R、NAIL-F/R，支持噪声设置下的实证优势。（§6；Appendix A）
  - 有限、可实现策略类与噪声模型等假设很强；理论 exponential-weights 算法并非实验实现，不能直接把定理套到任意大模型 recipe。（§4–6）
  - 作者组织：Columbia University，无大厂署名。官方代码：[plau666/NAIL](https://github.com/plau666/NAIL)；数据为可构造 modular addition 与公共 GSM8K。（PDF p.1；§6）
  - 会议身份：[官方目录](https://neurips.cc/Downloads/2026)，[对应条目](https://neurips.cc/virtual/2026/poster/150673)，2026-10-04 核验。
