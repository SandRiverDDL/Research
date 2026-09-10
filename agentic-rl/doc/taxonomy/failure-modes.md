# Agentic RL Failure Modes

> 初始 taxonomy，写卡时可以扩展，但必须在这里登记。这里只维护跨论文稳定 failure mode；method design decision tags 放在 `doc/taxonomy/design-knobs.md`。

## Reward / Feedback

- `sparse-delayed-reward`: final success reward 太稀疏，无法定位过程错误。
- `reward-hacking`: agent 学会 exploit reward / verifier。
- `verifier-noise`: verifier / judge 信号错误或不稳定。
- `process-reward-misalignment`: process reward 与最终任务成功不一致。

## Credit Assignment

- `long-horizon-credit`: 多步工具/环境交互中 credit assignment 粗。
- `tool-call-credit`: tool-call 成败与最终 reward 难以对应。
- `state-distribution-drift`: RL 更新后访问到训练数据未覆盖的新状态。

## Environment / Exploration

- `environment-overfitting`: policy 过拟合特定 environment / simulator。
- `rollout-cost`: online environment rollout 成本过高。
- `exploration-collapse`: agent 过早收敛到窄策略，无法发现有效行为。
- `action-space-fragility`: action grammar / tool schema 脆弱，RL 放大格式错误。

## SFT / Data Interface

- `warm-start-ceiling`: SFT warm start 决定 RL 可探索范围。
- `offline-online-gap`: 离线轨迹数据和 online interaction 分布不一致。
- `replay-bias`: replay / off-policy 数据偏差影响 RL 更新。

Agent Data data-mechanism failure modes 放在 `/Users/chy/Research/agent-data/`。
