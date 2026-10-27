---
title: "Learning from Language Feedback via Variational Policy Distillation"
authors: [Yang Li, et al.]
year: 2026
venue: neurips-2026
paper_id: arxiv:2605.15113
source: https://arxiv.org/pdf/2605.15113
---

- **一句话**：把语言反馈学习拆成 teacher preference refinement 与 student OPD 两个交替步骤，避免只靠 teacher 零样本理解反馈的能力上限。

- **Failure mode**：稀疏 reward 在全错 rollout group 中没有有效相对信号；反馈条件化的 self-teacher 虽提供密集监督，却没有被显式训练为更好的反馈解释者。（§2）

- **核心做法**

  1. 学生生成 rollout，获取执行错误、成功 sibling 或 self-critique 等语言反馈 C。（§3.4；§4.1）
  2. E-step：在反馈条件下，用学生已生成轨迹的 outcome 标签做 BCO 式 unpaired preference optimization；reference 取当前学生并在此步固定 likelihood，控制 teacher 的局部偏移。（§3.2，Eq.7–9）
  3. M-step：在学生 rollout 前缀上，以更新后的 feedback-conditioned teacher 为 detached target 做 RKL。实现中 teacher/student 共享权重，区别是输入条件；主设置每 5 个 M-step 做 1 个 E-step。（§3.3–3.4；Table 4）

- **方法增量**：相对 SDPO 的被动 feedback teacher，显式更新反馈条件化行为；相对同时加 RL+KD loss，采用交替优化和动态 reference。（§3；§4）

- **关键证据与边界**

  - Qwen3-1.7B/SciKnowEval、sibling feedback：GRPO 69.81，SDPO 66.34，VPD 74.34；固定 reference 67.84；E/M 频率 F1、F10 分别 70.21、69.27。（Tables 2、4–5）
  - 共享权重 E-step 后旧 rollout 对 M-step 已非严格 on-policy，作者凭小更新经验省略 IS；数学及 cold-start 仍显示 self-distillation 的局限。（§3.4；§4.2）
  - 组织：Salesforce AI Research。使用公共 SciKnowEval、LiveCodeBench、DAPO/数学 benchmark；本次原文未找到可核实的官方代码入口。反馈生成有额外成本。（PDF p.1；§4）
  - 会议身份：[官方目录](https://neurips.cc/Downloads/2026)，[对应条目](https://neurips.cc/virtual/2026/poster/152357)，2026-10-04 核验。
