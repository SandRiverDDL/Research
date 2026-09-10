---
title: "Adversarial Dual On-Policy Distillation from Expressive Flow-based Teacher"
authors: [Zhenglin Wan, et al.]
year: 2026
venue: icml-2026
paper_id: arxiv:2605.27095
source: https://arxiv.org/abs/2605.27095
---

- **一句话**：从 demonstrations 学出一个 Flow Matching teacher，再用 reward 与 action 两条 on-policy 通道训练轻量 embodied policy。

- **Failure mode**

  - `exposure-bias`：behavioral cloning 只见 expert states；部署后 student 的早期错误会把状态带出 demonstration manifold。（§1）
  - Learned-reward extrapolation：student 偏离数据支持区后，discriminator reward 可能失真。（§3.4）
  - FM online-update instability：直接对 Flow Matching policy 做 policy gradient，需要昂贵的密度估计或不稳定的 BPTT。（§3.1；§4.4）

- **瓶颈（作者诊断）**：embodied learning 只有静态 demonstrations，没有标准 OPD 所假设的固定强教师；同时 expressive FM teacher 又不适合作为低成本在线 actor。（§1；§3.1）

- **核心做法**

  1. 从 expert demonstrations 学习 conditional Flow Matching teacher。
  2. FM-enhanced discriminator 在 student visits 上产生 expert-likeness reward，供 PPO 做长程探索。
  3. 同一 teacher 在 student-visited states 生成 action target，提供 DAgger-style 局部纠正。
  4. 部署时只保留轻量 MLP student，teacher 在训练中随 student 协同更新。（§3.2–§3.4）

- **方法增量**

  - 相比 diffusion/flow BC：加入 student-induced states 上的在线纠正。
  - 相比 adversarial imitation learning：用 FM 建模分布级 expert-likeness，并补充 action distillation。
  - 相比标准 OPD：teacher 不是预训练后冻结，而是从 demonstrations 学习并与 student 协同变化。

- **关键证据与边界**

  - 六个 navigation、manipulation、locomotion 环境中，除 Ant-goal 外取得最佳最终表现；扰动状态下也比 diffusion/flow BC 更稳。（§4.1–§4.2）
  - 当 demonstration 接近 novice 水平时，teacher 无法恢复有意义的 density-ratio reward，FA-OPD 反而不占优。（§4.3；Table 1）
  - 机制也可解释为 flow-based adversarial imitation learning 加 DAgger；其 OPD 定位并非唯一解释。代码已公开。（§3.2–§3.4；[code](https://github.com/vanzll/FA-OPD)）
