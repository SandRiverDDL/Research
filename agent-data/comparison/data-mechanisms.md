# Agent Post-Training Data Mechanisms

> 这是 agent post-training data 的横切分析规范，不是独立综述，也不是人工维护的论文总表。等 method cards 足够后，再从 card 字段自动汇总矩阵。

## Why This Exists

Agent 后训练数据机制会出现在很多社区分类里：

- tool-use / tool learning。
- web / GUI / coding agent。
- data-centric alignment。
- llm post-training / instruction tuning / alignment data。
- agentic RL pipeline。
- synthetic data / self-improvement。

所以本项目不按场景建文件夹，而是用 data mechanism axes 重排论文。

## Required Axes

| axis | question | common values |
|---|---|---|
| `agent_domain` | agent 场景是什么？ | code / gui / web / browser / tool / search / game / mixed / general |
| `data_object` | 被训练或筛选的对象是什么？ | prompt / task / demo / trajectory / tool-call / observation / benchmark-task / replay-buffer / environment |
| `data_source` | 数据从哪里来？ | human / teacher / self-generated / environment-generated / replay / synthetic / web / real-world-log |
| `selection_signal` | 为什么保留、丢弃、修复或加权？ | success / verifier / difficulty / novelty / uncertainty / cost / format-validity / coverage / reward |
| `adaptivity` | 数据分布是否随模型能力或反馈变化？ | static / iterative / curriculum / student-feedback / environment-feedback / online |
| `failure_use` | 失败样本如何处理？ | discard / mask / repair / contrast / mine / replay / ignore |
| `training_consumer` | 数据服务哪个训练阶段？ | sft / pre-rl / rl / eval-only / background |
| `downstream_effect` | 数据决策主要影响什么？ | imitation quality / action validity / exploration / reward gradient / generalization / cost / safety |

## Card Requirement

每张 L1/L2 card 至少要写清：

```yaml
agent_domain:
data_object:
data_source:
selection_signal:
adaptivity:
failure_use:
training_consumer:
```

如果论文没有直接贡献训练数据机制，就写 `eval-only` 或 `background`，不要强行填成 Agent Data 方法。

## Boundary With Agentic RL

- Data pipeline 新，RL 只是消费者：本项目。
- RL algorithm 新，data pipeline 普通：`agentic-rl/`。
- 两边都新：本项目写 data 视角卡，并在 `agentic-rl` queue 记录 RL 视角。

## Auto-Generated Matrix Policy

后续如果需要论文矩阵，应该由脚本或 Codex 从 cards 自动生成到 `_meta/generated/data-mechanism-matrix.md`，不要人工长期维护 `comparison/data-mechanisms.md`。

矩阵生成前提：

- 至少 10-15 张 method cards。
- 每张 card 都有完整 data axes。
- validator 能检查字段 vocab。

## Working Hypotheses

事实：agent 综述通常按 agent 架构、工具、应用和评测切，不按 data mechanism 切。

解释：Agent Data 的核心不是“更多数据”，而是 data object、source、selection signal、failure use 和 adaptivity 如何改变训练分布。

猜测：失败轨迹在 agent training 中可能比普通 instruction tuning 更有价值，因为 failure often localizes missing tool/action/state transitions；但需要区分 noisy failure 与 informative failure。

解释：`Agent Post-Training Data` 是 `llm-post-training-data` 的 agent 子方向；它覆盖 SFT、pre-RL 和 RL consumer，但不把 pure optimizer 当主线。

开放问题：

- tool-call format validity 是训练目标、筛选规则，还是 evaluation metric？
- failed trajectory 应该 repair 成成功轨迹，还是保留为 contrastive negative？
- data distribution 是否应该随 student capability 迭代，类似 DAgger-like data collection？
- environment-generated data 与 teacher-generated trajectory 的可信度如何比较？
- real-world logs 与 synthetic verifiable environments 谁更适合 long-horizon agent supervision？
