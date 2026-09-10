---
title: "SWE-Master: Unleashing the Potential of Software Engineering Agents via Post-Training"
year: 2026
venue: arxiv
paper_type: trajectory-curation
lifecycle_role: frontier-candidate
boundary_risk: rl

failure_modes: [coverage-gap, long-horizon-drift, low-quality-demonstration]
data_knobs: [teacher-rollout, trajectory-to-sft, verifier-design]

agent_domain: code
data_object: trajectory
data_source: teacher
selection_signal: verifier
adaptivity: iterative
failure_use: repair
training_consumer: sft
---

## 一句话

SWE agent post-training recipe seed。

## 难题 / Failure Modes

| Failure mode | 本文诊断 | 本文处理方式 | 仍未解决 |
|---|---|---|---|
| `coverage-gap` | 开源 base model 初始 SWE 能力有限，长程任务轨迹不足。 | teacher-trajectory synthesis + data curation + long-horizon SFT。 | 摘要未说明失败轨迹如何局部 mask 或过滤。 |
| `long-horizon-drift` | SWE task 需要多步执行和环境反馈。 | 后训练管线加入真实执行反馈和 test-time scaling。 | RL / inference framework 部分需要和纯 data contribution 分开。 |

## 核心做法

SWE-Master 是完整 SWE agent post-training 技术报告，覆盖 teacher-trajectory synthesis、data curation、long-horizon SFT、real execution feedback RL 和 inference framework design。[Brief] 摘要称 Qwen2.5-Coder-32B 在 SWE-bench Verified 达到 61.4% resolve rate，结合 TTS@8 和 LLM-based environment feedback 达到 70.8%。[Brief] 对本项目的价值在于学习 SWE 数据管线：teacher 轨迹如何来、如何做 curation、SFT 与 execution feedback 如何衔接。

## Data Mechanism / Design Knobs

| Data knob | 本文选择 | 常见替代选择 |
|---|---|---|
| `teacher-rollout` | 用 teacher trajectory synthesis 补 SWE 长程监督。 | 只用人工 patch / issue 数据。 |
| `verifier-design` | 引入 real execution feedback。 | 只用文本 judge 或 final answer。 |

## 相对方法

| 对比对象 | 对方问题 | 本文改动 | 代价 / 风险 |
|---|---|---|---|
| 单纯 SWE SFT | 长程执行与环境反馈不足。 | SFT + execution feedback + TTS 组合 recipe。 | data 和 RL / inference gain 的贡献需要 ablation 拆开。 |

## 谱系位置

- 上游：SWE-bench、SWE-agent、teacher trajectory synthesis。
- 同期：SWE-Lego、Open-SWE-Traces、DeNovoSWE。
- 下游：内部 coding/SWE agent SFT 数据 recipe。

## 和 Agentic RL 的关系

- agentic_rl_overlap: true
- 本项目只读 data curation / teacher trajectory / long-horizon SFT；RL with execution feedback 可登记到 `agentic-rl`。
- 需要在后续 queue 里 cross-link RL 视角。

## 优缺点

- 优势：接近大厂/强团队 recipe 形态，比单点方法更适合学工程闭环。
- 不足 / 风险：摘要级证据无法拆分 SFT 数据、RL、TTS 各自贡献。

<!-- meta:
authors: [Huatong Song, et al.]
url: https://arxiv.org/abs/2602.03411
arxiv_id: 2602.03411
pdf:
brief: _meta/briefs/papers/2602.03411_swe-master.md
survey: Codex HF/arXiv recall
agentic_rl_overlap: true
agentic_rl_queue: pending
-->
