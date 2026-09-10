---
title: "Self-Distillation Enables Continual Learning"
authors: [Idan Shenfeld, et al.]
year: 2026
venue: icml-2026
paper_id: arxiv:2601.19897
source: https://arxiv.org/abs/2601.19897
---

- **一句话**：让看到 demonstration 的 EMA self-teacher，在 student 自己的 rollout 上提供 dense supervision，以学习新任务并减少遗忘。

- **Failure mode**

  - `exposure-bias`：SFT 只训练 demonstration trajectories，student 推理时进入未见状态后容易累积错误。（§1；§4.2）
  - Catastrophic forgetting：顺序 SFT 学到新任务后，旧能力快速下降。（§4.3）
  - Reasoning-style collapse：answer-only SFT 会压短已有 reasoning traces，并同时降低准确率。（§4.5）

- **核心做法**

  1. 同一模型构造两个 context：teacher 看到 prompt 与 demonstration，student 只看到 prompt。
  2. Student 从当前 policy 生成自己的 trajectory。
  3. Student 在该 trajectory 上最小化对 demonstration-conditioned teacher 的 reverse KL。
  4. Teacher 默认使用 student 参数的 EMA，并在计算监督时停止梯度。（§3）

- **方法增量**

  - 相比 SFT：把静态 demonstration 转成 student-visited states 上的 on-policy signal。
  - 相比标准 OPD：不需要独立强 teacher；能力差异来自同一模型是否看到 demonstration。
  - 相比 RL：无需显式 reward，并以一次 rollout 获得 token/logit-level credit。

- **关键证据与边界**

  - 知识注入 strict accuracy 为 89%，高于 SFT 的 80%；OOD 为 98% 对 80%。（§4.2；Table 1）
  - Answer-only 医疗数据上，SDFT 将 Olmo-3-7B-Think 从 31.2% 提到 43.7%，SFT 则降至 23.5%。（§4.5；Table 2）
  - 3B 模型因 ICL teacher 太弱而落后于 SFT；训练约需 SFT 的 2.5× FLOPs、4× wall time，还可能继承 teacher 的提示语痕迹。（§4.4；§5）
  - 代码和数据已公开。（[code](https://github.com/idanshen/Self-Distillation)）
