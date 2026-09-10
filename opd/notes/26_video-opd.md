---
title: "Video-OPD: Efficient Post-Training of Multimodal Large Language Models for Temporal Video Grounding via On-Policy Distillation"
authors: [Jiaze Li, et al.]
year: 2026
venue: icml-2026
paper_id: arxiv:2602.02994
source: https://arxiv.org/abs/2602.02994
---

- **一句话**：用单条 student rollout 和逐 token teacher supervision，替代 TVG 中昂贵且稀疏的 GRPO。

- **Failure mode**

  - `compounding-error`：SFT 只训练 expert trajectory；推理时早期定位错误会持续传播。作者归因于 train–inference state mismatch。（§2.1）
  - `coarse-credit-assignment`：GRPO 每条 trajectory 只有一个 reward，无法定位错误 decision。（§2.2）
  - `sgo-generation-cost`：视频上的 grouped rollouts 成本很高。（§2.2）

- **核心做法**

  1. Student 生成一条当前 policy trajectory。
  2. 固定 teacher 不生成答案，只在相同 prefix 上逐 token 评分。
  3. Teacher/student log-ratio 转成 dense reverse-KL reward。
  4. TVDF 先过滤 teacher 不可靠样本，再优先训练双方分歧最大的 trajectory。（§3.1–§3.2）

- **方法增量**

  - 相比 SFT：训练状态换成 student 自己访问的状态。
  - 相比 GRPO：dense credit 取代 sequence reward，并取消 grouped rollouts。
  - 相比标准 OPD：增加“teacher 可靠且 student 不会”的样本选择。

- **关键证据与边界**

  - 三个 TVG benchmark 均超过 GRPO 和 off-policy FKL/RKL；TVDF 额外约提升 2%。（§4.2；Table 1–2）
  - 作者报告其达到最优策略的训练成本约为 GRPO 的 20%。（§5）
  - 依赖能返回 conditional log-prob 的可靠 teacher；teacher 错误会直接进入监督。（Limitations）
