# Agent Post-Training Data Design Knobs

> 维护跨论文稳定的 agent data pipeline decision tags。写卡时从这里选择 1-4 个 `data_knobs`，不要临时造词；确实需要新 knob 时先在这里登记。

## Data Acquisition

- `trajectory-source`: trajectories 来自 human、teacher、self-generated、environment rollout、real-world logs 或 replay。
- `task-generation`: task / prompt / benchmark-task 如何生成、扩展或采样。
- `environment-synthesis`: 生成 executable environment、simulator、GUI / tool state 或可验证任务实例。
- `real-log-mining`: 从 PR、IDE、browser、GUI、tool-call logs 等真实历史中挖监督信号。
- `teacher-rollout`: 使用强模型或 agent teacher 产生 demonstration / trajectory / critique。

## Validation / Selection

- `verifier-design`: verifier / judge / unit test / rule check 如何产生可用于 data selection 的信号。
- `success-filtering`: 用 final success、task completion、tool success 或 executable check 筛选轨迹。
- `step-level-masking`: 对错误 step / token / action 局部 mask，而不是整条轨迹丢弃。
- `reward-hacking-filter`: 识别 Git hacking、shortcut、format exploit、verifier exploit 等数据污染。
- `negative-transfer-control`: 判断哪些数据会拖累其他任务，并过滤 / 重加权。

## Supervision Transform

- `trajectory-to-sft`: 将 agent trajectories 转成 SFT / behavior cloning 样本。
- `search-to-sft-distillation`: 将 search / rollout / critic / lookahead 结果蒸馏为 supervised data。
- `failure-repair`: 将 failed trajectory 修复为可训练正例或局部正例。
- `failure-contrast`: 将 failure 与 success 对比，构造 preference / contrastive / negative supervision。
- `process-supervision`: 将 step / tool-call / state-level signal 实例化为训练监督。

## Adaptivity / Curriculum

- `difficulty-curriculum`: 按 task / interaction length / tool count / success rate 安排课程。
- `student-feedback-loop`: 根据 student model 的错误、uncertainty 或 capability 生成 / 选择数据。
- `online-data-flywheel`: 训练后 rollout、验证、筛选、再训练的闭环。
- `coverage-balancing`: 平衡 domain、tool、state、failure mode、difficulty 的覆盖。

## Interface

- `action-schema`: action grammar、JSON/function call、tool API schema 影响数据可学性。
- `observation-action-alignment`: observation、state 和 action 标注的一致性。
- `tool-call-grammar`: tool-call sequence / graph / topology 如何表达成训练数据。
- `environment-interface`: environment wrapper、state reset、execution feedback 或 simulator 接口影响数据生成。
