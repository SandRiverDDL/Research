---
title: "Rethinking On-Policy Self-Distillation for Thinking Models"
authors: [Simran Kaur, et al.]
year: 2026
venue: neurips-2026
paper_id: arxiv:2607.05184
source: https://arxiv.org/pdf/2607.05184
---

- **一句话**：发现 reference-solution privileged OPSD 会损害强 thinking models 的长预算推理，并把退化关联到分岔、自我纠错和 deliberation 信号被压制。

- **Failure mode**：看到答案/解法的 teacher 不再需要学生的试探与回溯，沿学生 rollout 评分时可能压低这些行为；训练 loss 改善不意味着保留长预算搜索能力。（§3–4）

- **核心做法**

  1. 学生只看问题生成 rollout；初始 checkpoint 的冻结 self-teacher 额外看到 reference solution，在同一学生前缀上提供 token divergence 监督。（§2）
  2. 比较 thinking/instruct、最终答案/完整解法、普通 OPD/privileged OPD、不同训练与评测长度、训练关闭 thinking 等受控设置。（§3；Tables 1–4）
  3. 追踪高熵分岔、自我纠错 token advantage，以及长度归一化的检查、回溯和犹豫标记。（§4；Table 5）

- **方法增量**：这是机制诊断，未提出新的修复算法；强调 teacher 的 privileged context 可能破坏学生推理策略，不应把它等同于所有 OPD 都有害。（§3–6）

- **关键证据与边界**

  - Qwen3-1.7B 三项均分：base 37.2%，OPSD 30.8%，普通大教师 OPD 39.2%，privileged OPD 35.0%；OPD/OPSD 训练 cap 4096，评测 cap 38912。（Table 4）
  - 五个 thinking 模型均分都降低，但 Countdown 的 OLMo thinking 有提升；结论依赖任务、上下文与预算。主差异 paired bootstrap 在四个模型排除零，不能把相关诊断全部当成已证明的因果链。（Tables 1–3；Appendix C.1）
  - 组织：Princeton University，无大厂署名。数据来自公共 OpenThoughts 与 Countdown；本次原文未找到公开方法代码入口，不能据此断言代码未发布。（PDF p.1；§2）
  - 会议身份：[官方目录](https://neurips.cc/Downloads/2026)，[对应条目](https://neurips.cc/virtual/2026/poster/152392)，2026-10-04 核验。
