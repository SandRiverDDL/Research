# MoE-Aware RL Optimization failure-modes

初始分析标签，表示待核查的机制维度，不代表已证实的普遍失效。

- `routing-mismatch`: rollout 与训练路由差异引入不一致。
- `importance-weight-instability`: 概率比波动导致高方差或更新不稳定。
- `expert-update-imbalance`: router / expert 更新失衡或有效专家利用下降。
