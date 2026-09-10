# Agent Post-Training Data Failure / Data Modes

> 初始 taxonomy，写卡时可以扩展，但必须在这里登记。

## Data Quality / Coverage

- `format-only-imitation`: 学会输出格式或 tool-call schema，但没有学会真实决策。
- `trajectory-distribution-mismatch`: 训练轨迹分布和部署时 agent state 分布不一致。
- `low-quality-demonstration`: teacher / human demo 自身错误或不可执行。
- `synthetic-data-bias`: synthetic tasks / trajectories 覆盖窄或带 teacher artifact。
- `coverage-gap`: 数据没有覆盖关键任务、工具、状态或失败恢复路径。
- `negative-transfer`: 某类 trajectory / task 数据提升一个 domain，同时拖累其他 domain 或能力。
- `long-horizon-drift`: 长程合成轨迹中间状态逐步偏离真实任务分布。
- `step-label-noise`: 轨迹整体成功或失败标签无法定位到具体错误 step / token / action。

## Tool / Action Data

- `tool-call-cascade`: 一次错误 tool call 导致后续 observation / state 全部污染。
- `action-grammar-fragility`: action schema / JSON / function call 格式脆弱。
- `observation-action-misalignment`: observation 与 action 标注不匹配，导致模型学到错误 state transition。
- `invalid-environment-state`: synthetic / executable environment 的状态、约束或反馈不一致。

## Selection / Filtering

- `failure-signal-waste`: informative failed trajectories 被简单丢弃。
- `over-filtering`: 只保留成功轨迹导致 recovery behavior 不足。
- `verifier-noise`: verifier / judge 信号错误或不稳定。
- `difficulty-mismatch`: task / prompt 太易或太难，训练信号低。
- `reward-proxy-bias`: 用 reward / judge 做 data selection 时引入代理偏差。
- `reward-hacking-data`: 训练数据中包含利用 evaluator / verifier / repository loophole 的 shortcut trajectory。

## Adaptivity / Curriculum

- `static-data-ceiling`: 静态数据无法覆盖 student 新错误和新状态。
- `curriculum-mismatch`: difficulty curriculum 和 student capability 不匹配。
- `student-feedback-loop-instability`: 基于 student feedback 生成数据时，错误反馈被放大。
- `metacognitive-switch-gap`: 失败后缺少可监督的 strategy switching / abandon-and-replan 数据。
- `real-log-privacy-bias`: 真实日志因隐私、权限或产品分布导致可用监督片面。

Agentic RL algorithm failure modes 不在本 taxonomy 维护；放到 `/Users/chy/Research/agentic-rl/`。
