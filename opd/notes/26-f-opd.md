---
title: "f-OPD: Stabilizing Long-Horizon On-Policy Distillation with Freshness-Aware Control"
authors: [Xianwei Chen, et al.]
year: 2026
venue: neurips-2026
paper_id: arxiv:2605.17862
source: https://arxiv.org/pdf/2605.17862
---

- **一句话**：用样本新鲜度加权、rollout-policy 正则和按需刷新 buffer，缓解长链路异步 OPD 的陈旧数据失配。

- **Failure mode**：异步提升吞吐，却让旧 rollout 与当前学生不一致；交互任务中，缓存的 teacher-conditioning context 也可能偏离当前上下文。作者区分 rollout drift 与 supervision drift，后者在工具和代码交互中更突出。（§3；Figure 3）

- **核心做法**

  1. 保存采样时学生版本、前缀、教师条件上下文，在可对齐位置 replay，分别计算当前/旧学生 KL 与当前/缓存教师上下文下的 KL。（§4.1，Eq.10）
  2. 将更新延迟与两种 drift 合成新鲜度：`f_i = exp(-α√D_roll-β√D_sup)/(lag_i+1)`；用 `ReLU(f_i-ξ)` 加权样本及其 rollout-policy KL 正则。（§4.2，Eq.11–16）
  3. buffer 平均新鲜度过低或可对齐位置覆盖不足时，刷新 buffer。（§4.2）

- **方法增量**：相对按 lag 丢弃或固定刷新，显式度量样本内容与教师上下文的漂移；新鲜度是单调 surrogate，不是精确偏差估计。（§4.1）

- **关键证据与边界**

  - SWE-bench Verified：同步 OPD resolve 41.8；普通异步 26.8、吞吐 1.61×；f-OPD 39.4、吞吐 1.46×，五个 seed 中 collapse 从 3/5 降至 0/5。（Table 1；§5.1）
  - 依赖保留旧策略/上下文 provenance、可对齐 replay 与多个阈值；固定教师、固定文本前缀的普通 OPD 不应自动被描述为存在同样的 supervision drift。（§3–4；解释）
  - 作者组织：香港理工大学，无大厂署名。原文未找到本方法的公开代码入口；公共数据含 DAPO、SWE-bench Verified，自建工具评测集的发布状态未核实。（PDF p.1；§5.1）
  - 会议身份：[NeurIPS 2026 官方目录](https://neurips.cc/Downloads/2026)，[对应条目](https://neurips.cc/virtual/2026/poster/150017)，2026-10-04 核验。
