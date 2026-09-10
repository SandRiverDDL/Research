---
title: "Prune-OPD: Efficient and Reliable On-Policy Distillation for Long-Horizon Reasoning"
authors: [Zhicheng Yang, et al.]
org: hkust-mbzuai
year: 2026
venue: arxiv
arxiv_id: 2605.07804
url: https://arxiv.org/abs/2605.07804

confidence: 3
open_source: yes
verified: a

surveys:
  song-2026: "§6 Training Efficiency; Table 9; References"

addresses:
  - flawed-prefix-trap
  - compounding-error
  - sgo-generation-cost

decisions:
  rollout: student
  loss: adaptive-kl
  signal: logit
  iteration: continuous
  filter: support-truncation
  extra: none
---

> **一句话**：长程 OPD 的 prefix drift 动态剪枝路线。

## 核心做法

针对 long-horizon reasoning 中 student prefix 逐渐偏离 teacher thinking path 后 dense reward 失去局部可利用性的问题，Prune-OPD 用 student/teacher top-k overlap 实时监控 local compatibility；一旦检测到 prefix drift，就单调下调后续 token loss 权重并触发 dynamic rollout truncation。

$$c_t=\frac{|\mathrm{TopK}(\pi_\theta(\cdot|s_t))\cap \mathrm{TopK}(\pi_T(\cdot|s_t))|}{K}$$

实操含义：OPD 训练预算不应按固定 response length 分配，而应按“teacher signal 是否仍可执行”动态分配。

## 机制发现（可选）

- [作者 ack §2-3]: student prefix drift 后，teacher 条件分布虽然仍能给 dense token reward，但这些 reward 不再局部可利用，继续生成/打分会同时浪费算力和传播噪声。
- [作者 ack §3.1 / Appendix A.10]: top-k overlap 是主 metric；top-p action acceptance 更严格，但在实验中容易过早截断。
- [作者 ack §3.2-3.3]: cumulative reliability 同时控制 loss weighting 和 response budget，不是简单短输出 trick。

## 谱系位置

- 上游：Rethinking OPD (2026) — 继承“OPD 成功依赖 local thinking-pattern compatibility”的诊断，把它做成在线预算控制。
- 同期：Rock Tokens (2026) — 两者都反对等权 dense supervision；Prune-OPD 管 trajectory suffix，Rock Tokens 管 token/window 冗余。
- 同期：FOPD / fixed schedule efficiency methods — FOPD 预先设定训练日程，Prune-OPD 按实时 compatibility 调整。

## 优缺点

- ✅ [作者 ack §3 / §4]: 把 long-horizon OPD 的可靠性和算力成本合并成一个 online pruning 规则。
- ✅ [song-2026 §6 / Table 9]: 综述将其归入 training efficiency / dynamics 类方法，强调 top-k overlap drift detection。
- ✅ [作者 ack §4 / Appendix A.1]: 主实验固定训练 203 steps；动态控制器只改变每步 response budget 与 suffix 权重。因此 wall-clock speedup 来自减少 rollout/scoring/training token，不是减少 optimizer steps。
- ⚠️ [作者 ack Appendix A.3]: top-k overlap 只看 support overlap，不能完整反映 rank / probability gap；top-p action acceptance 又可能过严。

## headline number

- Training time -37.6% to -68.0% while preserving or improving AMC/AIME/HMMT performance（§Table 1）

<!-- pdf: arXiv HTML v3 Abstract / §2.3 / §3.1-3.3 / §4.2-4.6 / Appendix A.3 / Appendix A.10 -->
<!-- song-2026: §6 Training Efficiency / Table 9 / References -->
