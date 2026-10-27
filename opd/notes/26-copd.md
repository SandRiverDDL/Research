---
title: "Co-Evolving Policy Distillation"
authors: [Naibin Gu, et al.]
year: 2026
venue: neurips-2026
paper_id: arxiv:2604.27083
source: https://arxiv.org/pdf/2604.27083
---

- **一句话**：让多个领域分支在各自 RLVR 训练过程中持续互做 OPD，使能力互补与行为可吸收性共同维持。

- **Failure mode**：单模型 mixed RLVR 可能有跨能力梯度干扰；先独立训完专家再静态 OPD，则行为模式已拉开，学生无法充分吸收。（§2；Figures 1–2）

- **核心做法**

  1. 从共同 base 初始化领域分支，各自在文本、图像或视频数据上做 GRPO，产生互补能力。（§3.1）
  2. 分支 k 在分支 j 的领域题目上生成自己的 rollout，由 j 在这些前缀上计算 `log p_j-log p_k`，进行 token-level OPD；交换角色做双向传递。（§3.2）
  3. 按 `S_RL` 与 `S_OPD` 交替循环；三分支扩展用文本分支为 hub，分别与图像、视频分支互教。（§3.3–3.4）

- **方法增量**：把 OPD 从“专家训练结束后的汇总步骤”前移到专家共同成长过程；不是仅增加一个固定 teacher 或合并专家权重。（§3）

- **关键证据与边界**

  - 文本/图像整体均分：mixed RLVR 55.60；两方向静态 OPD 56.09/56.29；CoPD 57.71，文本、图像分组并非每个单项都最佳。（Table 1）
  - 多分支需同时维护和评分；相同训练 steps/data throughput 不等于相同 GPU-hours。行为 overlap 与吸收效率的相关性不能单独证明因果。（§2、4；解释）
  - 组织：中科院信工所、UCAS、JD.COM，含京东参与。使用公共多模态/数学数据及评测；本次原文未找到 CoPD 专属公开代码入口，不能把其依赖 EasyVideoR1/verl 当成方法已开源。（PDF p.1；§4.1）
  - 会议身份：[官方目录](https://neurips.cc/Downloads/2026)，[对应条目](https://neurips.cc/virtual/2026/poster/152206)，2026-10-04 核验。
