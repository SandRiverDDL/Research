---
title: "AsyncOPD: How Stale Can On-Policy Distillation Be?"
authors: [Wonjun Kang, et al.]
year: 2026
venue: neurips-2026
paper_id: arxiv:2606.24143
source: https://arxiv.org/pdf/2606.24143
---

- **一句话**：围绕有限 teacher-score cache 研究异步 OPD：FKL 更耐陈旧 rollout；RKL 用当前学生重算信号及 multi-sample MC 改善偏差/方差权衡。

- **Failure mode**：训练时学生已更新，但教师分数只缓存于采样时选中的动作；旧 student top-k 会漏掉当前需要的动作，单样本 RKL 又有高方差。（§4、6）

- **核心做法**

  1. 解耦 rollout、教师评分、learner update，异步重叠执行；同时保存行为策略概率与有限动作上的教师分数。（§4.1；§7）
  2. RKL learner 用当前学生概率重新计算 `A=log p_T-log p_current`，配合 old-to-current importance ratio；论文测试的设置中，不做 PPO ratio clipping 优于陈旧 advantage 及若干异步 RL surrogate。（§5；Figures 3–4）
  3. 每个位置缓存多个旧学生采样动作的教师分数，形成 multi-sample MC；importance sampling 可纠正动作分布陈旧性，增加样本降低单样本方差。（§6）

- **方法增量**：把异步问题拆成“当前信号怎么计算”与“缓存是否覆盖所需动作”；旧 top-k 内重加权无法补回缺失的教师分数。（§6）

- **关键证据与边界**

  - staleness 从 0 扫到 128；FKL 曲线更平稳，RKL 对陈旧性更敏感；异步系统报告吞吐 1.6–3.8× 且准确率相近。（Figure 2；§7）
  - 核心分析是固定已访问 prefix 的局部动作估计器；动作 IS 可纠正不等于整条陈旧轨迹的状态分布被完全恢复。（§3–6；解释）
  - 组织：FuriosaAI、Ajou、UC Berkeley、Microsoft Research、KRAFTON、Ludo Robotics。官方代码：[furiosa-ai/async-opd](https://github.com/furiosa-ai/async-opd)；使用公共 DeepMath 与 AIME/AMC，未提出新 benchmark。（PDF p.1；§4.1）
  - 会议身份：[官方目录](https://neurips.cc/Downloads/2026)，[对应条目](https://neurips.cc/virtual/2026/poster/156136)，2026-10-04 核验。
