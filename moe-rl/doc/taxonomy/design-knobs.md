# MoE-Aware RL Optimization design-knobs

初始分析标签，表示待核查的机制维度，不代表已证实的普遍失效。

- `importance-sampling-unit`: token / sequence / route 层面的概率比构造。
- `routing-correction`: route replay、校正或选择规则。
- `router-expert-update`: router 与 expert 的更新与约束。
