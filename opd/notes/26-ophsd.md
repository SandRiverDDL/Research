---
title: "Training with Harnesses: On-Policy Harness Self-Distillation for Complex Reasoning"
authors: [Zhengyang Zhao, et al.]
year: 2026
venue: neurips-2026
paper_id: arxiv:2605.08741
source: https://arxiv.org/pdf/2605.08741
---

- **一句话**：用运行 harness 的当前模型构造 self-teacher，把 draft–verify 或 plan–solve 形成的上下文监督蒸馏到单模型。

- **Failure mode**：harness 提升的是外部系统推理表现，移除工作流后 base model 的固有能力未必改善；静态 privileged solution 也未体现工作流的处理过程。（§1、3）

- **核心做法**

  1. 学生在原问题上生成 rollout；harness 驱动当前模型处理训练时可用的 memory/reference solution，生成结构化 terminal context。（§3.2）
  2. teacher 在该上下文和学生 rollout prefix 上提供 token-level 分布，学生以 reverse KL 内化监督。分类用 draft/confirm/challenge；数学用 planner 形成 plan–solve 上下文。（§3；Figure 1）
  3. 评测训练后的独立学生，并测试重新挂载 harness 是否仍有收益。（§4.2–4.3）

- **方法增量**：相对 OPSD/SDFT 直接追加静态解法，增加可执行 harness 对 privileged 信息的加工；监督仍包含训练时 oracle，不是纯无标签自我提升。（§3；Table 1）

- **关键证据与边界**

  - 数学四项平均 pass@8：OPHSD 69.50，OPSD 66.68，GRPO 66.57；重新挂 harness 69.13。在线分类也比较 GRPO、OPSD。（§4.2–4.3；Tables 2、5）
  - 数学表采用训练期间最佳观察分数，需注意 checkpoint 选点和公平成本；“外挂不再有效”只在测试的两类 harness 上成立，未覆盖通用工具 agent。（§4.3；解释）
  - 组织：Peking University，无大厂署名。作者公开代码和训练数据：[OPHSD repository](https://github.com/zzy1127/OPHSD-On-Policy-Harness-Self-Distillation)；仓库可访问，GitHub 未识别许可证；评测含 LawBench、USPTO 与公共数学 benchmark。（PDF p.1；§4）
  - 会议身份：[官方目录](https://neurips.cc/Downloads/2026)，[对应条目](https://neurips.cc/virtual/2026/poster/149380)，2026-10-04 核验。
