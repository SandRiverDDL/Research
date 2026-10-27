---
title: "Trust Region Policy Distillation"
authors: [Zhengpeng Xie, et al.]
year: 2026
venue: neurips-2026
paper_id: arxiv:2607.04751
source: https://arxiv.org/pdf/2607.04751
---

- **一句话**：TOP-D 用老师/学生概率混合构造 proximal teacher，限制极端负 log-ratio；再用 PPO 式多步更新提高 rollout 利用率。

- **Failure mode**：原始 OPD 中老师给 sampled token 的概率趋近零，负反馈无界；严格每次更新重采样又限制样本效率。（§3）

- **核心做法**

  1. 学生每题生成 8 个回答，构造 `p_prox=αp_teacher+(1-α)p_rollout_student`；反馈直接算 `r=log(α p_teacher/p_rollout_student+1-α)`，下限为 `log(1-α)`。（§3.1；Algorithm 1）
  2. return 为当前位置反馈加未来反馈的长度归一化均值；在同题所有回答的所有 token 上做均值/标准差归一化。（§3.2，Eq.8）
  3. 固定该批反馈，以 current/rollout likelihood ratio 和 PPO clipping 做 internal epochs/mini-batch 更新。实验 α 为 0.1 或 0.2。（§3.2；§5.1）

- **方法增量**：相对 REOPOLD 的硬截断，是平滑概率混合；相对只缩放 log-ratio，负反馈有有限下界。与三星 Xingrun Xing 的 TrOPD（arxiv:2606.01249）为不同论文。（§3.1；身份核对）

- **关键证据与边界**

  - Qwen3-30B-A3B teacher→8B-Base：AIME24 avg@32，OPD 24.58、TOP-D 50.42；AIME25 23.33→34.06。主表比较 GRPO、DAPO、普通 OPD，未证明优于完整近年 OPD 方法集合。（Table 2）
  - 消融包含 α=1（去 proximal teacher）与去 off-policy 更新；理论依赖 bounded score 等假设；完整收益含 return/normalization/复用，不能全部归因于混合教师。（Figure 5；§4；解释）
  - 组织核验：首页作者联系邮箱包含 Microsoft 与 HKUST(GZ)，未给完整机构列表，本卡不把全体作者认定为微软。使用公共 DAPO/AIME/AMC/MATH/Olympiad，未提出新 benchmark；本次原文未找到官方代码入口。（PDF p.1；§5.1）
  - 会议身份：[官方目录](https://neurips.cc/Downloads/2026)，[对应条目](https://neurips.cc/virtual/2026/poster/150346)，2026-10-04 核验。
