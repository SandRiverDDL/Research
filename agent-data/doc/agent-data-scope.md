# Agent Post-Training Data 课题边界

## 总原则

当前项目研究 `Agent Post-Training Data`，是 `llm-post-training-data` 下的 agent 子方向。

核心判断问题：

> 这篇论文到底在改变“agent 后训练数据如何产生、验证、筛选、局部保留和被使用”，还是在改变“优化器如何更新 policy”？

前者进本项目；后者进 `/Users/chy/Research/agentic-rl/`。

## 收录范围

收录：

- task / prompt / benchmark-task generation。
- agent demonstration / trajectory tuning。
- tool-call / action grammar data。
- observation-action trace / state transition supervision。
- behavior cloning / imitation data。
- DAgger-like data collection。
- synthetic trajectory / task / tool-call data。
- verifiable environment / executable task generation，如果目的在于产生或验证训练数据。
- real-world long-horizon interaction logs，例如 PR sequence、IDE / browser / GUI history。
- failed trajectory repair / filtering / masking / mining。
- teacher-generated or self-generated agent traces。
- verifier / judge / format-validity / success signal 做 data selection。
- search / rollout / critic / process feedback 蒸馏成 SFT / pre-RL data。
- rollout / replay / buffer selection，如果论文重点是数据选择而不是 RL update。
- SFT warm-start data。
- RL training data pipeline，只要核心贡献是数据机制。

## 迁出范围

迁到 `agentic-rl/`：

- reward design / reward model 本身。
- policy optimization objective。
- RL algorithm modification。
- online exploration strategy。
- long-horizon credit assignment。
- on-policy/off-policy update mechanics。
- environment interaction protocol，如果重点是 RL learning loop 而不是数据生成/筛选。
- benchmark 主要用于评测 RL agent，而不是构造训练数据。
- 普通 LLM instruction / alignment data，除非直接触及 agent trajectory、tool/action 或 environment interaction。
- pretraining corpus、web-scale dedup、token mixture、版权/污染等通用数据治理问题。

## 混合论文处理

- **data pipeline 新，RL 只是消费者**：Agent Data。
- **RL 算法新，data pipeline 普通**：Agentic RL。
- **两边都新**：Agent Data 写 data 视角卡；Agentic RL queue 记录 RL 视角，未来再抽。
- **不确定**：先进 Agent Data novelty-risk queue，卡里标 `rl_overlap: true`，并说明为什么暂不迁出。

## Data Mechanism Axes

每篇卡都要记录：

| axis | values |
|---|---|
| `agent_domain` | code / gui / web / browser / tool / search / game / mixed / general |
| `data_object` | prompt / task / demo / trajectory / tool-call / observation / benchmark-task / replay-buffer / environment |
| `data_source` | human / teacher / self-generated / environment-generated / replay / synthetic / web / real-world-log |
| `selection_signal` | success / verifier / difficulty / novelty / uncertainty / cost / format-validity / coverage / reward |
| `adaptivity` | static / iterative / curriculum / student-feedback / environment-feedback / online |
| `failure_use` | discard / mask / repair / contrast / mine / replay / ignore |
| `training_consumer` | sft / pre-rl / rl / eval-only / background |

## Seed 时间口径

- Survey seed 默认优先 2026。
- 最早只放宽到 2025Q4，且必须直接服务 agent data generation / filtering / verification / repair。
- 2023/2024 agent 总综述只作为 historical background / terminology，不作为当前优先 seed。
- 方法类 anchor 不严格受 survey 时间口径限制；早期方法如果仍是 strong baseline 或机制起点，可以进入 method card 队列。

## 第一阶段成功标准

- 写出 10-15 张 Agent Post-Training Data method L1 cards。
- 能回答：agent 后训练数据的主要对象是什么、哪些 selection signals 真能提升泛化、失败轨迹应该丢弃 / mask / 修复 / 对比、数据机制什么时候只是 RL pipeline 的普通组件。
- 生成第一版 `comparison/` 总结，服务后续 idea generation。
