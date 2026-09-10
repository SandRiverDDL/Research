# Benchmark To Data Actions

> 用于把 V0.4.1 bad case 归因转成 SFT 数据决策。事实来自用户提供的 benchmark report；论文 card 只作为可借鉴 recipe。

## Working Goal

```text
benchmark failure slice -> missing meta-skill -> data action -> candidate dataset -> ablation
```

## Initial Mapping

| failure slice | missing skill | data action | candidate references | ablation target |
|---|---|---|---|---|
| 已产出但低分：文件名 / 字段 / 数值 / runtime | M1 指令对齐 + M5 自检 | artifact verification trajectories: write -> read/list/run/count -> compare to spec -> fix -> deliver | SWE-Lego, ProCUA-SFT, ACC | 文件产出类、文档、网页、数据处理 slice |
| 元认知失败：同源错误循环，不换层 | M4 换思路 + M6 调试 | failed-loop-switch trajectories: 2 次同源失败 -> minimal repro / inspect real output / switch library / rewrite small script | SWE-Lego, ProAct, MARS hold | docx 工具循环、runtime debugging slice |
| docx 工具路线错误 | M3 工具规划 + M4 换路 | tool/skill selection data: npm docx vs python-docx vs libreoffice; explicit switch criteria | PC Agent-E, ADP, Anthropic patterns | docx / pptx / file generation slice |
| 长程多约束丢失 | M2 任务分解 + M5 自检 | spec ledger trajectories: constraints ledger -> subtask execution -> checkpoint -> final verification | ACC, DeNovoSWE, Open-SWE-Traces | hard multi-dependency tasks |
| 数据处理与分析弱 | M2 + M5 + M6 | data-analysis trajectories with file readback, recomputation, schema/row checks, script rerun | DataMind, ACC | data cleaning / analysis slice |

## Data Package Backlog

| package | purpose | source sketch | selection signal | likely paper support | expected win | regression risk |
|---|---|---|---|---|---|---|
| `artifact-self-check` | 修文件名、字段、数值、runtime、产物路径 | benchmark bad cases + synthetic artifact variants | file existence, field match, count/value recomputation, runtime pass | SWE-Lego, ProCUA-SFT, ACC | 已产出但低分 slice 下降 | verbosity / unnecessary checks / latency |
| `failed-loop-switch` | 卡 bug 后换思路 / 换工具 / 最小复现 | failed traces -> repair trajectories; repeated-error mining | repeated exception, unchanged output, failed verifier then fixed verifier | ProAct, SWE-Lego, Bilevel Data Curation | 元认知循环下降 | premature switching / abandoning good path |
| `spec-ledger-long-task` | 多约束任务保持初始要求 | long tasks with explicit constraint ledger and checkpoints | final constraint checklist + intermediate readback | ACC, DeNovoSWE, daVinci-Agency | hard multi-dependency 上升 | short-task over-planning |
| `tool-skill-selection` | 选库、换库、加载 skill | same task with multiple tool/library routes and switch criteria | tool support matrix, executable success, unsupported-feature detection | ADP, ASTRA, PC Agent-E | docx / pptx / file generation slice | frequent tool switching / ignoring local skill |
| `data-analysis-agent` | 数据清洗/分析链路 | csv/xlsx/json files + analysis tasks + script/readback traces | schema check, row count, recomputation, chart/table artifact check | DataMind, ACC | data cleaning / analysis slice | code execution overuse |
| `mixture-guardrail` | 防止单包数据造成负迁移 | all data packages as sources + validation slices | slice-level validation loss / benchmark score | FastMix, Dr. Post-Training, Data Mixing Optimization | total score up with no slice regression | optimizing wrong validation objective |

## Ablation Plan Stub

Do not assume mixture by intuition. After data packages exist, compare:

| run | added data | expected slice gain | regression watch |
|---|---|---|---|
| baseline | none | current V0.4.1 | N/A |
| +M5 | `artifact-self-check` | 已产出但低分下降 | verbosity / unnecessary checks |
| +M4 | `failed-loop-switch` | 元认知循环下降 | premature tool switching |
| +M2 | `spec-ledger-long-task` | hard multi-dependency 上升 | over-planning short tasks |
| +data-analysis | `data-analysis-agent` | 数据处理与分析上升 | code execution overuse |
| mixture | all with tuned weights | total score up | original strong 信息查询 slice regression |

See also: `comparison/agent-sft-data-synthesis.md`.
