---
title: "SEAD: Competence-Aware On-Policy Distillation via Entropy-Guided Supervision"
authors: [Chia-Hsuan Lee, et al.]
year: 2026
venue: neurips-2026
paper_id: arxiv:2606.28562
source: https://arxiv.org/pdf/2606.28562
---

- **一句话**：联合师生熵选 token 和 KL 方向，再配合 FKL 权重退火及 easy-to-hard prompt curriculum，按学生能力分配监督。

- **Failure mode**：作者认为学生能力太弱时 rollout 不连贯，监督含噪；已掌握位置监督冗余；统一 token、阶段、prompt 配方因此浪费训练。（§1–2）

- **核心做法**

  1. 在学生 rollout 上计算师生熵：两者低熵为 Zone A、跳过；教师低熵/学生高熵为 B、用 RKL；教师高熵为 C、用 FKL。默认 A/B/C 比例 50/40/10。（§2.3）
  2. 对 C 区 FKL 权重采用 cosine schedule，由 0.8 衰减到 0；B 区 RKL 保留，并按参与训练的位置数归一化。（§2.2、2.4，Eq.4、7）
  3. 用初始学生 rollout pass rate 估计题目难度，逐步扩大可采样 prompt 集合。（§2.5；Algorithm 1）

- **方法增量**：相对 teacher-entropy-only 的 EOPD，同时决定位置选择与 divergence 类型，并把 token routing、时间和 prompt 课程组合。（§2.3–2.6）

- **关键证据与边界**

  - OLMo 7B student/32B teacher：普通 OPD 均分 59.2，完整 SEAD 64.0；但 curriculum-only 63.38，annealing+curriculum 63.97，不能据此认定三个模块各自都必要。（Tables 1–2）
  - 两者低熵不保证预测相同；其稀疏梯度定理额外假设师生 TV 小。初始难度排序也可能随训练失效。（Theorem 1；§2.5）
  - 原文称竞赛指标 Pass@32，却定义为 32 个样本的平均通过率；指标命名和含义需复现时确认。50/40/10 与正文“约20% active”亦不一致，本卡使用显式算法默认值。（§2.3；§3.1）
  - 组织：Capital One。数据为公共 DAPO 与数学评测集；本次原文未找到可核实的官方代码仓库。（PDF p.1；§3、Appendix B）
  - 会议身份：[官方目录](https://neurips.cc/Downloads/2026)，[对应条目](https://neurips.cc/virtual/2026/poster/155569)，2026-10-04 核验。
