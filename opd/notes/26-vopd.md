---
title: "KL for a KL: On-Policy Distillation with Control Variate Baseline"
authors: [Minjae Oh, et al.]
year: 2026
venue: neurips-2026
paper_id: arxiv:2605.07865
source: https://arxiv.org/pdf/2605.07865
---

- **一句话**：用负 token-level reverse KL 作为 detached control-variate baseline，降低单样本 OPD 梯度方差，不需要训练 critic。

- **Failure mode**：sampled-token OPD 的 log-ratio reward 有负长尾与高方差；full-vocabulary KL 稳定但更昂贵，直接把 loss 截到 top-k 又改变目标。（§2–3）

- **核心做法**

  1. 学生生成 rollout，老师在学生前缀上给出 token 分布，得到 `r=log p_T(y)-log p_S(y)`。（§2.1）
  2. 计算 `b=E_student[r]=-KL(p_S||p_T)`，把 sampled-token 更新中的 reward 换成 detached `r-b=r+KL`。（§3.1，Eq.9–10）
  3. 可在学生 top-k 支持集重归一化后近似 baseline；top-k 用于 action-independent baseline，而不是替换完整优化目标。（§3.2）

- **方法增量**：相对 clip/mask 改变反馈，baseline 利用 score-function 零均值性质保持期望梯度；近似 baseline 不一定最优，但在对应采样假设下不引入 action bias。（§2.2、3.2）

- **关键证据与边界**

  - Qwen3-1.7B 同尺寸 distillation：OPD 数学均分 29.8；full-vocabulary OPD 33.0；vOPD top-k 33.0、full-V 33.1；另覆盖 Qwen3-4B 与 OLMo-7B。（Table 2）
  - 对已经精确枚举全词表动作期望的梯度，baseline 项严格消失，不能继续降低该位置的动作采样方差；主要服务 MC estimator。（§3.1，Eq.12–13）
  - 组织：Seoul National University，无大厂署名。公开代码：[holi-lab/vOPD](https://github.com/holi-lab/vOPD)，仓库可访问，GitHub 未识别许可证；使用公共数学、SciKnowEval、GPQA benchmark。（PDF p.1；§4）
  - 会议身份：[官方目录](https://neurips.cc/Downloads/2026)，[对应条目](https://neurips.cc/virtual/2026/poster/149290)，2026-10-04 核验。
