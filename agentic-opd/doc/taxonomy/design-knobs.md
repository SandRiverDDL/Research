# Agentic OPD Design Knobs

> 初始化标签，用于跨论文定位；按原论文证据使用。

- `rollout-horizon`：student rollout 深度、截断与课程。
- `prefix-source`：prefix / state 的来源、replay 与覆盖。
- `teacher-intervention`：teacher 查询时机、介入与纠错。
- `supervision-signal`：logit、token、action、step 等监督形式。
- `loss-allocation`：token / action / turn 权重及训练预算分配。
- `termination-control`：终止、工具闭合、重复与截断处理。
- `evaluation-protocol`：任务成功率、泛化与公平对比条件。
- `compute-allocation`：student rollout、teacher query 与更新成本分配。
