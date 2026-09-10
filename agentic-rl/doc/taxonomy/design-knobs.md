# Agentic RL Design Knobs

> 维护跨论文稳定的 agentic RL training design decision tags。写卡时从这里选择 1-3 个 `design_knobs`，不要临时造词；确实需要新 knob 时先在这里登记。

## Reward / Feedback

- `reward-source`: reward 来自 terminal success、tool feedback、human、LLM judge、verifier 或环境信号。
- `reward-shaping`: 把 sparse outcome 转成 dense / process / milestone / intrinsic reward。
- `verifier-design`: verifier / judge / critic 如何产生可用于 policy update 的反馈。

## Objective / Credit

- `policy-objective`: 改 PPO / GRPO / DPO-like / actor-critic 等 policy update objective。
- `advantage-estimation`: 改 advantage / value / Q / baseline 的估计方式。
- `credit-unit`: 改 credit assignment 的粒度，例如 trajectory、segment、step、token、tool-call、state。
- `progress-signal`: 定义什么算阶段性进展，例如 milestone、subgoal、verified partial success。

## Rollout / Data Use

- `rollout-source`: 决定 trajectories 从 online env、offline rollout、teacher、self-play、tree search、world model 等哪里来。
- `trajectory-filtering`: 训练前/训练中筛选、拒绝、重加权或修复 trajectories。
- `replay-off-policy`: replay buffer、off-policy correction、reuse old trajectories。
- `exploration-strategy`: 促进 online exploration 或防止 exploration collapse。

## Interface / Warm Start

- `prompt-action-interface`: prompt、action schema、tool-call format 或 response format 参与训练闭环。
- `warm-start`: SFT / behavior cloning / skill initialization 如何影响 RL 上限或探索范围。
- `environment-interface`: environment wrapper、tool API、state observation 或 simulator 接口影响 RL loop。
