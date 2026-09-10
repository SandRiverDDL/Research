# Agent SFT Data Synthesis

> 第一版 comparison，目标不是总结领域，而是服务当前 30B A3B MoE agent SFT：`benchmark failure -> data package -> ablation -> regression guardrail`。

## 0. 一句话结论

解释：当前最值得学的不是“agent data 有哪些方向”，而是四个可迁移范式如何组合：

1. **真实日志挖掘**：Open-SWE-Traces / daVinci-Agency 说明真实 PR / 任务历史比纯合成长程轨迹更接近部署分布。
2. **可验证合成**：SWE-Lego / DeNovoSWE / ProCUA-SFT / DataMind / ASTRA 说明 synthetic data 只有配 verifier、environment、precondition check 才值得信。
3. **失败轨迹局部利用**：SWE-Lego / Bilevel Data Curation 提醒不要整条丢弃失败样本；坏轨迹里可能有好 step、好 task、坏 response。
4. **配比与防回退**：FastMix / Dr. Post-Training / Data Mixing Optimization 说明最后问题不是“加哪包数据”，而是按 validation slice 优化 mixture，同时监控 negative transfer。

对你的 benchmark report，优先级应是：

```text
M5 artifact self-check > M4 failed-loop-switch > M2 spec-ledger-long-task > data-analysis trajectories > tool/skill selection
```

事实依据：用户报告中 “已产出但低分” 和 “元认知失败” 是最大坏例来源；DataMind 对应最低 L1 slice；SWE-Lego / ProCUA-SFT / ACC / DataMind / ProAct 分别给出可迁移的数据机制。

## 1. 论文地图：每篇到底学什么

| paper                                                                     | 在项目里的角色                             | 该学什么                                                                 | 不该被它带偏到哪里                                 |
| ------------------------------------------------------------------------- | ----------------------------------- | -------------------------------------------------------------------- | ----------------------------------------- |
| [SWE-Lego](../notes/2601_swe-lego.md)                                     | 局部错误 mask / 自检 seed                 | step-level error masking、trajectory curriculum、Git hacking filtering | 不要只学 SWE-bench 分数；核心是“坏步骤局部 mask”         |
| [ACC](../notes/2605_acc-agent-context-compilation.md)                     | observation grounding seed          | 把 tool responses / stdout / 文件内容编译成长上下文监督                            | 不要把它当完整 agent policy；它更像读轨迹回答             |
| [DataMind](../notes/2509_datamind.md)                                     | 数据分析 slice seed                     | task taxonomy、easy-to-hard composition、rule/model filtering          | 不要直接照搬 RL objective；先拆 data-only 贡献       |
| [ProAct](../notes/2602_proact.md)                                         | failed-loop-switch / lookahead seed | environment search -> causal reasoning SFT                           | MC-Critic 是 RL overlap，不是 agent-data core |
| [daVinci-Agency](../notes/2602_davinci-agency.md)                         | real long-horizon seed              | PR chain / evolving state /少样本长轨迹                                    | 不要忽略 repo selection bias 和样本少的问题          |
| [Open-SWE-Traces](../notes/2606_open-swe-traces.md)                       | 大规模真实 PR trajectory seed            | real-world PRs -> agentic traces；Qwen3-30B-A3B 相关                    | 不要假设真实 PR 分布等于你的 benchmark 分布             |
| [DeNovoSWE](../notes/2606_denovoswe.md)                                   | whole-repo synthetic seed           | sandboxed workflow、critic-repair、difficulty filtering                | 不要把 repo generation 特化误当通用长程能力            |
| [ProCUA-SFT](../notes/2606_procua-sft.md)                                 | GUI / artifact verifier seed        | live desktop、precondition checking、negative transfer                 | 不要认为更多 GUI 数据一定更好                         |
| [PC Agent-E](../notes/2505_pc-agent-e.md)                                 | 低成本 GUI seed                        | 少量 human trajectories + teacher action augmentation                  | 不要忽略 teacher action 可执行性                  |
| [ASTRA](../notes/2601_astra.md)                                           | tool graph / verifiable arena seed  | tool-call graph、MCP schema、rule-verifiable environment               | 不要把规则可验证任务当成所有开放任务                        |
| [Agent Data Protocol](../notes/2510_agent-data-protocol.md)               | 内部 schema seed                      | 异构 agent 数据统一格式                                                      | 协议统一不等于质量统一                               |
| [SWE-Master](../notes/2602_swe-master.md)                                 | 大厂式 SWE recipe seed                 | teacher trajectories、curation、long-horizon SFT、execution feedback    | 需要拆 SFT / RL / TTS 贡献                     |
| [FastMix](../notes/2606_fastmix.md)                                       | mixture optimizer seed              | validation-driven source weights                                     | 不告诉你 agent bucket 怎么定义                    |
| [Dr. Post-Training](../notes/2605_dr-post-training.md)                    | target/general regularization seed  | target failure data 与 general data 的更新方向约束                           | 不是生成 agent 数据的方法                          |
| [Data Mixing Optimization](../notes/2508_data-mixing-optimization-sft.md) | SFT mixture math anchor             | validation loss -> domain weights                                    | 不是 agent-specific，validation slice 设计更关键  |
| [Bilevel Data Curation](../notes/2511_bilevel-data-curation.md)           | failure repair flywheel seed        | 保留高价值 task，重生成 / 修复坏 response                                        | 原文是 response-level，迁到 trajectory 需重设计     |

## 2. 方法家族对比

| family | representative papers | data source | selection signal | 最适合解决 | 最大风险 |
|---|---|---|---|---|---|
| Real-world trajectory mining | Open-SWE-Traces, daVinci-Agency | PR / repo / task history | success, coverage, evolving state | 长程任务、真实工具状态、部署分布 | privacy / license / selection bias；难覆盖罕见失败 |
| Synthetic verifiable data | SWE-Lego, DeNovoSWE, ProCUA-SFT, DataMind, ASTRA | synthetic tasks / environments / tool graphs | verifier, rule, precondition, test | 可控覆盖、M5 自检、data-analysis、tool-call graph | synthetic bias；verifier 被 game；环境状态不真实 |
| Teacher trajectory curation | SWE-Master, PC Agent-E, Open-SWE-Traces | strong teacher / human seed | verifier, coverage, teacher quality | 快速拉起 agent behavior | 学 teacher artifact；失败轨迹处理粗糙 |
| Search-to-SFT distillation | ACC, ProAct | rollout / search / tool observations | coverage, reward, environment feedback | observation grounding、lookahead、换思路 | 可能训练成“读轨迹”而非“主动行动” |
| Failure repair / partial supervision | SWE-Lego, Bilevel Data Curation | failed / noisy trajectories or responses | step attribution, validation | M4/M5 bad cases、避免丢有价值任务 | step attribution 错会放大噪声 |
| Mixture / flywheel | FastMix, Dr. Post-Training, Data Mixing Optimization | data buckets / replay buffer | validation slices | 数据配比、negative transfer guardrail | validation objective 设计错则优化错方向 |

解释：这些 family 不是互斥路线。更合理的工程组合是：

```text
real logs 给分布真实性
synthetic/verifiable 给覆盖和可控标签
failure repair 给局部高价值监督
mixture/flywheel 决定各包权重和防回退
```

## 3. Data Action Matrix

| benchmark failure | data package | construction sketch | paper support | expected win | regression guardrail |
|---|---|---|---|---|---|
| 已产出但低分：文件名、字段、数值、runtime、路径 | `artifact-self-check` | 轨迹必须包含 `write -> read/list/run/count -> compare spec -> fix -> final answer`；错误 step 局部 mask | SWE-Lego, ProCUA-SFT, ACC | M5 自检；产物类任务质量 | 防止模型过度检查、回复变长、短任务 latency 上升 |
| 元认知失败：同一错误循环，不换思路 | `failed-loop-switch` | 构造 “两次同源失败 -> inspect real output / minimal repro / switch library / rewrite small script” 的轨迹 | ProAct, SWE-Lego, Bilevel Data Curation | M4 换路、M6 调试 | 防止过早换工具、放弃正确路线 |
| 长程多约束丢失 | `spec-ledger-long-task` | 任务初始约束 ledger；每步更新 checked / unchecked；最终逐项验收 | ACC, DeNovoSWE, daVinci-Agency | M2 分解、M5 final verification | 防止简单任务过度 planning |
| 数据处理与分析弱 | `data-analysis-agent` | 文件 schema readback、row/count check、脚本重跑、结果交叉验证、图表/表格 artifact check | DataMind, ACC, ProCUA-SFT | 最弱 data-analysis slice | 防止所有任务都倾向写代码或过度执行 |
| tool / skill / library 选错 | `tool-skill-selection` | 相同任务给多条候选工具路线；标注 switch criteria、unsupported feature、fallback | ASTRA, ADP, PC Agent-E | M3 工具规划、M4 换工具 | 防止模型频繁换库、忽略现有 skill |
| 单域增强拖累其他能力 | `mixture-guardrail` | 将上面每个 package 作为 source；用 benchmark validation slices 学比例 | FastMix, Dr. Post-Training, Data Mixing Optimization | overall score up，不只局部涨 | 原强项 slice、通用问答、短任务效率 |

事实：ProCUA-SFT 明确报告旧 human trajectory 继续训练会造成 OSWorld negative transfer；因此任何 package 都不能只看目标 slice 增益。

解释：对你当前情况，`artifact-self-check` 和 `failed-loop-switch` 应该优先进入第一批数据包，因为它们覆盖最多坏例，同时能借 SWE-Lego 的局部 mask 和 ProAct 的 environment-search lookahead 思路。

## 4. 关键取舍：真实日志 vs 合成可验证

| decision | choose real logs when | choose synthetic verifiable when | hybrid recipe |
|---|---|---|---|
| 长程任务 | 你能拿到内部 PR / task / tool logs，且能重建上下文 | 真实日志少、隐私强、状态难复现 | 用真实日志抽 task skeleton，再合成可验证 variants |
| 自检 / artifact | 有历史失败输出和最终人工修正 | 能写 rule/verifier，如文件存在、字段一致、数值一致 | 从真实 bad case 抽 spec，合成多 artifact variants |
| 数据分析 | 有真实表格和分析请求 | 能用 schema / row count / recomputation 验证 | 真实文件 + 合成 query + script verifier |
| tool selection | 有真实工具切换记录 | 有 tool docs / schema / dependency graph | ASTRA-style tool graph + PC Agent-E-style action augmentation |

判断：你现在不应该在“真实日志还是合成数据”里二选一。真实日志负责告诉你模型真实会遇到什么状态；synthetic/verifiable data 负责把这些状态扩大成可训练、可筛选、可消融的数据包。

## 5. 失败样本怎么处理

| failure data type | recommended action | why | supporting papers |
|---|---|---|---|
| 任务本身有价值，response / trajectory 坏 | repair / regenerate | 丢掉会损失 task diversity | Bilevel Data Curation |
| 轨迹大部分对，某些 step 错 | step-level mask | 保留好 token / 好动作，屏蔽坏局部 | SWE-Lego |
| 错误导致后续 observation 全污染 | cut after first corrupt step | 后续状态不再可信 | SWE-Lego, tool-call-cascade taxonomy |
| 失败展示了 evaluator loophole | discard + blacklist pattern | 这是 reward hacking data，不是有用 failure | SWE-Lego |
| 失败体现缺少 switch / debug behavior | mine as negative-to-positive pair | 正是 M4/M6 监督来源 | ProAct, Bilevel Data Curation |

开放问题：目前还缺一篇很强的 “agent failed trajectory repair / contrastive data” 论文作为直接 anchor。MARS / MIRROR 可能提供 metacognitive scaffold 或 benchmark 视角，但还不是强训练方法 seed。

## 6. 学习顺序

### 第一轮：只学数据 taste

| order | read | 只抓这一点 |
|---:|---|---|
| 1 | SWE-Lego | 为什么失败轨迹不能简单丢；step-level mask 怎么想 |
| 2 | ACC | 为什么 tool observation / stdout / 文件内容需要显式监督 |
| 3 | DataMind | 数据分析 agent 的 task taxonomy 和 verifier/filtering |
| 4 | ProCUA-SFT | 为什么 “加更多 agent 数据” 会 negative transfer |
| 5 | FastMix / Dr. Post-Training | 为什么最后必须做 mixture / guardrail |

### 第二轮：学长程和真实分布

| order | read | 只抓这一点 |
|---:|---|---|
| 1 | daVinci-Agency | PR chain 如何保留 evolving state |
| 2 | Open-SWE-Traces | 大规模 real PR traces 如何组织 |
| 3 | DeNovoSWE | synthetic whole-repo task 如何可验证 |
| 4 | ProAct | 外部 search 如何蒸馏成 lookahead SFT |

### 第三轮：学工具和格式

| order | read | 只抓这一点 |
|---:|---|---|
| 1 | Agent Data Protocol | 内部统一 agent data schema |
| 2 | ASTRA | tool graph 如何生成多工具轨迹 |
| 3 | PC Agent-E | 少量 human seed 如何用 teacher 扩增 |

## 7. 最小可执行 ablation plan

不要先做大而全 mixture。建议顺序：

| run | added data | purpose | pass condition | stop condition |
|---|---|---|---|---|
| R0 | baseline V0.4.1 | 锁定 slice 指标和坏例归因 | reproduce current score | 指标不稳定则先修 eval |
| R1 | `artifact-self-check` | 验证最大 failure slice 是否可被数据修 | 产物类 bad case 显著下降 | verbosity / latency /短任务明显恶化 |
| R2 | `failed-loop-switch` | 验证 M4/M6 是否能被 SFT 学到 | loop bad case 下降 | premature switching 上升 |
| R3 | `data-analysis-agent` | 补最低 L1 slice | data-analysis slice 上升 | code execution overuse |
| R4 | `spec-ledger-long-task` | 补 hard multi-dependency | hard tasks 上升 | 简单任务 over-planning |
| R5 | tuned mixture | 合并收益 | 总分上涨且无核心 regression | 任一强项 slice 明显下降 |

解释：`tool-skill-selection` 可以插到 R2 或 R4 后面；但如果你的人力有限，它不应优先于 M5/M4/data-analysis。

## 8. 证据强弱

| claim | evidence strength | why |
|---|---|---|
| step-level / process-level supervision 对 agent SFT 关键 | medium-high | SWE-Lego、ProCUA-SFT 都朝这个方向；但跨域 verifier 还需自己做 |
| real-world long-horizon logs 比纯合成长任务更可靠 | medium | Open-SWE-Traces / daVinci-Agency 支持 code/SWE；其他 domain 证据不足 |
| data-analysis agent 值得单独做数据包 | high for this project | 用户 benchmark 最弱 slice + DataMind 直接相关 |
| metacognitive switch 可以靠 SFT 定向增强 | low-medium | ProAct 提供 lookahead seed，但不是失败切换专门方法；MARS/MIRROR 还需补证据 |
| mixture optimization 必须做 | high | ProCUA-SFT negative transfer + data-flywheel 方法共同支持 |

## 9. 当前最重要的开放问题

1. `artifact-self-check` 的 verifier 能否覆盖 docx / pptx / html / xlsx / csv / code runtime，而不只覆盖 SWE？
2. `failed-loop-switch` 的 step attribution 怎么做：按工具错误、stderr、重复编辑、相同 exception，还是按 evaluator bad-case 标签？
3. `spec-ledger-long-task` 是否会让短任务过度 planning？需要短任务 regression set。
4. data-analysis trajectories 是偏 Python code，还是也覆盖 spreadsheet / BI / chart artifact？
5. mixture 优化用哪些 validation slices？只用总分会掩盖 negative transfer。

## 10. 下一步建议

先不要继续扩论文 queue。下一步应该把这份 comparison 落成训练数据 backlog：

```text
package -> source -> generation recipe -> verifier -> filtering/masking -> expected slice -> regression set -> ablation run
```

然后只针对 backlog 里的证据缺口补论文：

- 如果 `failed-loop-switch` 证据不足，再读 MARS / MIRROR / failed trajectory papers。
- 如果 `artifact-self-check` verifier 不够，再找 GUI / document artifact verification papers。
- 如果 mixture 要落地，再精读 FastMix / Dr. Post-Training 的算法细节。

数据配比细化见：`comparison/data-mixture-comparison.md`。
