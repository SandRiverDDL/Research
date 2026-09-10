---
title: "Hybrid Policy Distillation for LLMs"
authors: [Wenhong Zhu, et al.]
year: 2026
venue: icml-2026
paper_id: arxiv:2604.20244
source: https://arxiv.org/abs/2604.20244
---

- **一句话**：在离线 expert prefixes 上同时检查 expert token 与 student-sampled token，按局部概率误差决定压制或补强。

- **Failure mode**

  - `source-divergence-mismatch`：expert token 与 student-sampled token 承载不同信号，却常被同一种 divergence 统一处理。
  - Mode coverage / seeking conflict：forward KL 容易过度覆盖，reverse KL 又偏向少数 mode；全局固定混合无法判断某个 token 应该补强还是压制。（§3–§4.1）
  - Off-policy blind spot：纯 expert prefixes 看不到 student 当前偏好的错误 token。

- **瓶颈（作者诊断）**：distillation 的 divergence direction、data source 与 optimization strategy 相互耦合；真正需要修正的是 token-level probability mass 的局部错配，而不是全局选择一种 KL。（§4.1）

- **核心做法**

  1. 把 SFT、FKL、RKL 等统一写成 token-level reweighted likelihood。
  2. 在每个离线 prefix 上，以 expert token 为主要目标，同时采一个 student non-expert token。
  3. 只压制被 student 过高估计的 non-expert token，避免错误强化。
  4. 将释放的概率质量补回被低估的 expert token，形成 masked forward/reverse-KL hybrid。（§4.2）

- **方法增量**

  - 相比固定 FKL/RKL：按 token 当前错配方向决定是否启用 forward 或 reverse correction。
  - 相比简单加权混合：用 masking 避免两个 KL 方向产生冲突梯度。
  - 相比完整 OPD：保留离线数据吞吐，只加入轻量 student token sampling；它不是完整 student rollout。

- **关键证据与边界**

  - Reasoning、personalization、code 的多模型实验中，HPD 平均表现和稳定性优于 SFT/KD/RKLD/JSD。（§5；Table 2–4）
  - Qwen 2.5 7B→1.5B 上，HPD 初始化再接 OPD 的平均分为 33.41，SFT→OPD 为 29.56。（§5.4；Table 5）
  - 消融显示 student sampling 防止过早 plateau，expert reinforcement 加快 KL 对齐。（§6；Figure 3）
  - 仍未充分证明 token-level approximate on-policy 能替代完整 student-trajectory coverage。代码公开。（[code](https://github.com/zwhong714/Hybrid-Policy-Distillation)）
