# Agentic OPD Failure Modes

> 初始化标签，是阅读维度；不代表已经证实每篇论文存在这些问题。

- `prefix-mismatch`：student 错误 prefix / state 上 teacher 信号失效。
- `long-horizon-degradation`：多轮交互中覆盖或监督可靠性下降。
- `credit-dilution`：重要 action / 深 turn 的更新被其他 token 稀释。
- `action-boundary-drift`：工具调用结构与关键 action 行为漂移。
- `termination-instability`：重复、循环、超长轨迹或工具调用无法闭合。
- `teacher-pattern-mismatch`：teacher continuation 形式与 student 可学行为不匹配。
- `weak-baseline`：对照不足以建立机制主张。
- `metric-gaming`：指标改善未对应任务完成。
- `source-gap`：主张缺乏原论文或实验锚点。
