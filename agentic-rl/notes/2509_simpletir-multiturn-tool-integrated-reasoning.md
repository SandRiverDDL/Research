---
title: "SimpleTIR: End-to-End Reinforcement Learning for Multi-Turn Tool-Integrated Reasoning"
year: 2025
venue: arxiv
paper_type: core-rl-method
lifecycle_role: frontier-candidate
boundary_risk: reasoning

failure_modes: [state-distribution-drift, action-space-fragility, sparse-delayed-reward]
design_knobs: [trajectory-filtering, prompt-action-interface, environment-interface]

rl_env: tool
rl_interaction: online
rl_reward: outcome
rl_credit: trajectory
---

## 一句话定位

用 void-turn filtering 稳定多轮工具 GRPO。

## 难题 / Failure Modes

| Failure mode | 本文诊断 | 本文处理方式 | 仍未解决 |
|---|---|---|---|
| `state-distribution-drift` | 外部工具 feedback 拼回 prompt 后偏离模型预训练分布。 | feedback token masking，且过滤含 void turns 的整条 trajectory。 | 只验证在 multi-turn TIR/math 场景。 |
| `action-space-fragility` | 低概率 token 和格式错误在后续 turns 中放大。 | 检测既无完整 code block 又无 final answer 的 void turn。 | void-turn heuristic 对非代码工具不一定成立。 |
| `sparse-delayed-reward` | 后续 collapse 会让早期有效工具调用一起吃负 reward。 | 含 void turn 的 trajectory 不进入 GRPO loss。 | 牺牲了部分失败轨迹里的可学习信号。 |

## 方法机制

SimpleTIR 把 multi-turn tool-integrated reasoning 建模为 hierarchical MDP，但训练上仍使用统一 policy 和 GRPO：trajectory reward 来自最终答案，agent action tokens 参与 loss，环境返回的 tool feedback tokens 被 mask 掉。[brief p.3] 它的核心是 void-turn filtering：如果 trajectory 中任何 turn 既没有完整 code block 也没有 final answer，就在 GRPO 更新前 mask 整条 trajectory 的 policy loss。[brief p.6] 作者认为这能同时阻止低概率 token 的大梯度反传，并避免早期成功工具调用因后续 collapse 被负 reward 错罚。[brief p.6] 实验显示它比 naive multi-turn training、low-prob filtering 和 high-ratio filtering 更稳定。[brief p.7-p.9]

## 相对方法

| 对比对象 | 对方问题 | 本文改动 | 代价 / 风险 |
|---|---|---|---|
| GRPO / DAPO / Dr.GRPO | 稳定普通 RLVR，但不处理工具 feedback 分布漂移。 | 加 feedback masking 和 void-turn trajectory filtering。 | 规则和代码工具格式绑定。 |
| Search-R1 / ReTool / ToRL | 训练工具使用，但依赖 domain data、SFT 或 recipe。 | 从 base model 做 Zero RL 式 multi-turn TIR。 | 任务主要是数学工具推理。 |
| high-ratio / low-prob filtering | 阈值难调，仍会错罚早期有效 turns。 | 按 trajectory 是否出现 void turn 过滤。 | 丢掉整条 trajectory 比较粗。 |

## 设计决策 / Design Knobs

| Design knob | 本文选择 | 常见替代选择 |
|---|---|---|
| `trajectory-filtering` | mask entire trajectories containing void turns before GRPO update. | token filtering / ratio filtering / train all failures. |
| `prompt-action-interface` | only action tokens get gradient; tool feedback tokens are masked. | include all tokens / separate tool channel / external wrapper. |
| `environment-interface` | code interpreter feedback becomes next-turn context. | search feedback / browser observation / database execution feedback. |

## 方法优缺点 / 适用边界

- 优势：指出 multi-turn tool feedback 会造成训练分布漂移，这是 GRPO-like agent training 的真实失败模式。
- 优势：机制简单，可作为工具/代码类 agent RL 的 hygiene baseline。
- 不足 / 风险：`boundary_risk: reasoning`，主要实验是 math/code interpreter，不应直接等同 web/GUI agent。
- 不足 / 风险：void-turn filtering 是粗粒度过滤，可能丢弃可用失败前缀；作者也把 asynchronous rollout、memory、credit 留作 future work。

<!-- meta:
authors: [Zhenghai Xue, Longtao Zheng, Qian Liu, et al.]
url: https://arxiv.org/abs/2509.02479
arxiv_id: 2509.02479
pdf: papers/2509.02479-simpletir-multiturn-tool-integrated-reasoning.pdf
brief: _meta/briefs/papers/2509.02479_simpletir-multiturn-tool-integrated-reasoning.md
survey: SPEAR backward reference [19]
rl_optimizer: grpo-like
rl_data_reuse: none
rl_warm_start: none
-->
