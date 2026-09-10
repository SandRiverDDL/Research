---
title: "TurnOPD: Making On-Policy Distillation Turn-Aware for Efficient Long-Horizon Agent Training"
authors: [Yuhang Zhou, et al.]
year: 2026
venue: arxiv
paper_id: arxiv:2607.05804
source: https://arxiv.org/abs/2607.05804
---

- **一句话**：TurnOPD 同时控制“rollout 到第几个 turn”和“各 turn 分到多少 loss”，以减少长程 agent OPD 的无效后缀计算，并避免浅层 token 吞掉几乎全部训练权重。

- **Failure mode**

  - 固定 full-horizon rollout 会继续生成弱信号或重复的尾部 turn，浪费 rollout 与 teacher scoring 成本。
  - trajectory-level token mean 受存活轨迹数和 token 数支配：ALFWorld 最深三分之一 turn 只获得 3.6%–4.5% 的总 KL loss，深层决策训练不足（§3.3；Table 1）。
  - 失败轨迹进入循环或模板后，context 会强制 student/teacher 给出相似 continuation；因此 late-turn 低 KL 既可能表示对齐，也可能只是“contamination-compression”，不能直接解释为 teacher 监督可靠（§3.2）。

- **瓶颈（作者诊断）**：单独根据 late-turn KL 截断不可辨识——低 KL 同时对应真正对齐与坏 prefix 下的分布压缩；只看信号会过早截断，只看成功轨迹长度又不能衡量训练价值。因此作者用 signal centroid 与成功轨迹 coverage floor 共同决定 horizon（§3.2；§4.1）。

- **核心做法**

  1. 每隔 8 step 做一次 full-depth probe；普通 step 使用动态 turn cap，截断轨迹仍参与 OPD，但不参与下一次 controller 估计（§4.1；Table 7）。
  2. 对 turn (t) 计算正 KL 乘存活率 (m_t=[K_t]_+n_t/n_0)，其加权重心给出有效深度 (H_{eff})；再取成功轨迹完成深度的 P80 得到 (H_{cov})，最终控制目标为 \(\max(H_{eff},H_{cov})\)（Eq. 7–10）。
  3. 对目标 horizon 做 EMA（系数 0.30）并额外加 1 turn exploration margin；参考范围为 2–50 turns（Eq. 11；Table 7）。
  4. loss 从按 token/trajectory 归一化，线性过渡到各 turn 均分预算；blend 系数随训练进度从 0 增至 1，使后期深层 turn 不再被浅层 token 数量压制（§4.2）。

- **方法增量**

  - 相比 TCOD 的预设 front-to-back curriculum，TurnOPD 用周期 probe 的 KL、survival 与成功完成深度在线调整 horizon。
  - 相比 SOD 的 step-wise reliability weighting，它不直接判断某个 step 是否可信，而是控制生成深度并重分配跨 turn 的 loss budget。
  - 两个组件缺一不可：仅 adaptive depth 把 ALFWorld 1.7B wall time 从 4.42h 降到 1.96h，但同 step Avg@4 为 82.8、未超过 vanilla 83.0；再加 turn blend 后达到 86.3、1.93h（Table 5）。

- **关键证据与边界**

  - ALFWorld 1.7B：vanilla same-step Avg@4 83.0、4.42h；TurnOPD 86.3、1.93h（2.29×）。WebShop 为 81.65→82.80、1.57h→1.24h（Table 2）。
  - Multi-Hop Search 上 TurnOPD least-time 更好，但 same-step 47.24 略低于 vanilla 47.82；它不是稳定提升最终算力等额性能（Table 2）。
  - 实验使用 task-specialized GRPO teacher、100 steps、batch 64、Top-50 reverse KL，并运行在 32×H20 80GB；不能直接外推到 8 卡、sampled-token OPD 或通用 agent（§5；Table 7）。
  - P80、8-step probe 与 EMA 0.30 是经验设定；controller 还依赖环境 success reward。论文只报告最后四次 eval checkpoint 的均值与标准差，不是多随机种子误差；截至本卡阅读时未定位到公开代码。
