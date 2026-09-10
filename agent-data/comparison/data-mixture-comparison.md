# Data Mixture Comparison

> Supporting-method comparison。这里不回答“造什么 agent 数据”，而回答：已有 agent 数据包后，如何配比、选择、修复和防 regression。

## 0. 一句话

解释：对当前项目，数据配比不是独立于 agent data 的通用数学问题；它必须以 **benchmark failure slice** 为 validation objective，以 **agent data package** 为 source bucket。

所以正确顺序是：

```text
bad case taxonomy -> data package -> package-level ablation -> validation slices -> mixture optimization -> regression guardrail
```

不要一开始就优化全量 mixture。没有稳定 slice eval 时，FastMix / bilevel / scaling-law mixture 都会优化到错误目标。

## 1. 四类方法的区别

| method family | representative paper | 它优化什么 | 输入需要什么 | 输出是什么 | 最适合当前项目的阶段 | 最大风险 |
|---|---|---|---|---|---|---|
| Static SFT mixture optimization | [Data Mixing Optimization for SFT](../notes/2508_data-mixing-optimization-sft.md) | 固定预算下各 domain/source 权重 | 若干 source bucket、proxy runs、per-slice validation loss | 一组静态 mixture weights | 已有 3-6 个稳定数据包后，做第一版比例搜索 | validation slice 不代表真实 benchmark 时会误导 |
| Online / differentiable mixture optimization | [FastMix](../notes/2606_fastmix.md) | 训练中根据 validation feedback 更新 source 权重 | 单 proxy model、可迭代训练、稳定 validation objective | 动态或收敛后的 source weights | 有自动训练/评测闭环后，用来替代大规模 grid search | 工程要求更高；source 定义差会优化错 |
| Target-general data regularization | [Dr. Post-Training](../notes/2605_dr-post-training.md) | target failure data 的更新方向如何被 general data 约束 | target bucket、general bucket、能计算/近似 update direction | regularized update / target-general tradeoff | 窄 bad-case 数据很少但怕训坏通用能力时 | 不是直接给比例；实现和计算更复杂 |
| Offline selection + online repair | [Bilevel Data Curation](../notes/2511_bilevel-data-curation.md) | 先选有价值 task，再修复/重生成 response | noisy SFT data、validation set、regeneration pipeline | selected tasks + repaired responses + weights | 进入 mixture 前清洗每个 package 内部质量 | 原文是 response-level，迁移到 multi-step trajectory 需重做 |
| Negative-transfer diagnostic | [ProCUA-SFT](../notes/2606_procua-sft.md) | 证明“更多同类 agent data”可能伤害目标 | 原数据、增量数据、目标/非目标 benchmark | regression warning / filtering rule | 每次加入 GUI/tool/data-analysis 包都要做 guardrail | 只诊断，不提供通用优化算法 |

判断：如果你现在就要落地，最实用的是 **静态 mixture + target/general guardrail**，不是直接上 FastMix。FastMix 更像第二阶段自动化。

## 2. 对当前 agent SFT 的 bucket 设计

| bucket | role | target slice | target/general class | source sketch | first ablation |
|---|---|---|---|---|---|
| `artifact-self-check` | 修产物低分 | 文件名 / 字段 / 数值 / runtime / path | target | bad cases + synthetic artifact variants | `base + artifact-self-check` |
| `failed-loop-switch` | 修同源错误循环 | 元认知失败 / debugging | target | repeated failure -> inspect / repro / switch / fix | `base + failed-loop-switch` |
| `spec-ledger-long-task` | 修长程约束丢失 | hard multi-dependency | target | long task ledger + checkpoints | `base + spec-ledger-long-task` |
| `data-analysis-agent` | 补最低能力 slice | data cleaning / analysis | target | csv/xlsx/json + script/readback/checks | `base + data-analysis-agent` |
| `tool-skill-selection` | 修路线选择 | docx / pptx / tool/library choice | target-support | candidate tool routes + switch criteria | after M4/M5 packages |
| `agent-replay-general` | 防遗忘 | 原强项 / general agent tasks | general | previous SFT mix / successful traces / general tool-use | always included in mixture |
| `format-basic` | 保格式稳定 | action grammar / JSON / final answer format | general-support | existing instruction/tool-call data | always included, small but stable |

解释：bucket 不应该按论文分，也不应该按数据来源分。它应该按 **希望修复的 benchmark failure** 分；论文只是提供构造和筛选机制。

## 3. 推荐配比流程

### Stage A: 先做 package-level ablation

目的：确认每个数据包是否真的修对应 slice。

| run | data | accept condition | reject / revise condition |
|---|---|---|---|
| A0 | baseline | reproduce V0.4.1 slice metrics | eval 不稳定则停止 |
| A1 | baseline + `artifact-self-check` | 产物类 bad case 下降，原强项不明显掉 | 回复变长、简单任务变慢、过度检查 |
| A2 | baseline + `failed-loop-switch` | loop bad case 下降 | 过早换路线、正确路线也放弃 |
| A3 | baseline + `data-analysis-agent` | data-analysis slice 上升 | 泛化到其他任务时过度写代码 |
| A4 | baseline + `spec-ledger-long-task` | hard multi-dependency 上升 | 简单任务 over-planning |

事实：ProCUA-SFT 的 negative-transfer 结果说明，跳过 package-level ablation 直接混合是危险的。

### Stage B: 再做 coarse static mixture

目的：找到不会明显 regression 的粗比例，而不是追求数学最优。

建议不要一上来做连续优化，先做少量保守组合：

| run | design | question |
|---|---|---|
| B1 | target-light | 少量 target data 是否已经修主要 bad case？ |
| B2 | target-heavy | 增加 target data 是否继续收益，还是开始 regression？ |
| B3 | balanced-targets | M5/M4/M2/data-analysis 均衡是否比单一最大包更稳？ |
| B4 | general-heavy | 加大 `agent-replay-general` 是否能保住原强项？ |

解释：这一步对应 Data Mixing Optimization for SFT 的实用前置条件：你需要先知道哪些 domain/source 会互相影响，然后再拟合 validation-loss / scaling-law 参数。

### Stage C: 用 target/general regularization 防回退

把数据分成两层：

| layer | contains | objective |
|---|---|---|
| target data | M5/M4/M2/data-analysis 等 failure-targeted packages | 修坏例 |
| general data | 原 SFT mix、成功 traces、基础 tool-call / instruction-following | 防止通用能力和原强项掉 |

Dr. Post-Training 的启发是：general data 不只是“陪跑数据”，而是约束 target update 的 regularizer。工程上可以先用简单近似：

- 每个 target-heavy run 都必须有 paired general-heavy run。
- 每个 target slice gain 都要同时报告 general regression。
- 如果 target gain 需要牺牲原强项，先调高 general replay，而不是继续加 target。

### Stage D: 有自动闭环后再上 FastMix

FastMix 适合的前提：

- source bucket 已稳定。
- validation slices 已稳定。
- 每个训练 run 能自动产出 slice metrics。
- proxy model 的趋势能代表 30B A3B MoE。

如果这些不成立，FastMix 只会把错误 objective 优化得更快。

## 4. Validation slice 设计

数据配比的核心其实是 validation set，而不是 optimizer。

| slice | purpose | should include | should not include only |
|---|---|---|---|
| `artifact-quality` | 测 M5 自检 | 文件存在、字段、数值、runtime、路径、readback | final answer 文本相似度 |
| `loop-switch` | 测 M4/M6 | repeated error、stderr、unchanged artifact、switch/repro behavior | “是否提到反思” |
| `long-constraint` | 测 M2/M5 | 多约束 ledger、跨步骤一致性、最终 checklist | 单轮复杂 prompt |
| `data-analysis` | 测数据处理 | schema、row count、recompute、chart/table artifact | 只问 Pandas 知识 |
| `tool-selection` | 测 M3/M4 | 多工具可选、明确 unsupported feature、fallback | 单一工具调用成功 |
| `general-agent-regression` | 防遗忘 | 原强项任务、短任务、信息查询、普通 tool-use | 只有总分 |

判断：如果只能维护一个额外 slice，优先做 `general-agent-regression`。因为 target slice 上升很容易，难的是不把原来会的训坏。

## 5. 什么时候用哪篇论文

| situation | read / use | reason |
|---|---|---|
| 你还没决定数据包怎么分 | 不先读 mixture 论文，先看 synthesis / benchmark backlog | mixture 论文不会告诉你 agent bucket |
| 已有 3-6 个数据包，想定第一版比例 | Data Mixing Optimization for SFT | 静态 SFT mixture 的直接 anchor |
| 你发现 target data 提升坏例但损害原强项 | Dr. Post-Training | target/general regularization lens |
| 你有很多 noisy bad-case tasks，不知道丢还是修 | Bilevel Data Curation | task 保留、response/trajectory 修复 |
| 你有稳定自动训练和 slice eval | FastMix | 用 validation feedback 替代手工 grid search |
| 某个数据包单独训练后明显掉分 | ProCUA-SFT | negative-transfer 思维和诊断方式 |

## 6. 对当前项目的具体建议

当前不要把数据配比理解成“论文给一个算法，我照着跑”。更稳的路线：

1. 先把五个 target bucket 做出来：`artifact-self-check`、`failed-loop-switch`、`spec-ledger-long-task`、`data-analysis-agent`、`tool-skill-selection`。
2. 每个 bucket 单独跑 ablation，保留能修对应 slice 且无明显 regression 的。
3. 固定一个 `agent-replay-general`，所有 target run 都混它。
4. 第一版 mixture 用 coarse grid，而不是直接 FastMix。
5. 如果 coarse grid 显示明显 target/general tradeoff，再精读 Dr. Post-Training。
6. 如果 run 数量太多、eval 自动化稳定，再考虑 FastMix。

## 7. 最小实验矩阵

| experiment | target data | general data | decision |
|---|---|---|---|
| E1 | M5 only | fixed replay | `artifact-self-check` 是否值得进 mix |
| E2 | M4 only | fixed replay | `failed-loop-switch` 是否真能 SFT 学到 |
| E3 | data-analysis only | fixed replay | 是否补最低 slice |
| E4 | M5 + M4 | fixed replay | 两个最大 failure 是否互补 |
| E5 | M5 + M4 + data-analysis | fixed replay | 初版 target mix |
| E6 | E5 target-light | more replay | 是否更稳 |
| E7 | E5 target-heavy | less replay | target 是否继续增益或开始伤害 |
| E8 | best E5-E7 + M2 | fixed replay | long-task 数据是否应进第一版 |

Stop rule：如果某个 target bucket 在单包 ablation 中不能修对应 slice，先回去改数据构造 / verifier，不要用 mixture 权重掩盖它。

## 8. 开放问题

1. proxy model 上学到的 mixture 是否能迁移到 30B A3B MoE？这会决定 FastMix / static scaling-law 方法的可信度。
2. benchmark validation slices 会不会被数据包过拟合？需要 held-out bad-case families。
3. `agent-replay-general` 应该来自原训练 mix、成功 traces，还是通用 instruction/tool data？
4. 多个 target bucket 是否冲突：例如 `failed-loop-switch` 会不会削弱 `spec-ledger-long-task` 的坚持执行？
5. mixture objective 应该优化总分、slice 平均、worst-slice，还是加权 utility？

