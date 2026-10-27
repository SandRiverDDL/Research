---
type: idea
node_id: idea:teacher-choice-over-student-options
title: "让 teacher 在 student 能执行的短程方案之间教学"
stage: proposed
outcome: pending
added: 2026-10-14T15:02:56Z
based_on: ["paper:chen2026_look_ahead_before"]
target_gaps: []
tags: ["agentic-opd", "method", "idea-creator-2026-10-14", "reserve"]
---

# 让 teacher 在 student 能执行的短程方案之间教学

**stage:** `proposed`  ·  **outcome:** `pending`

2026-10-14 idea-creator：A5；生成模型 `gpt-6-astra`；未验证储备。同家族模型评审为provisional，未运行pilot。见[排序报告](../../idea-stage/IDEA_REPORT.md)及[原始候选](../../idea-stage/candidates-2026-10-14.json)。

## Thesis
具体方法：

1. 从 student 自主访问的 h，采样 K 个固定长度短程 option，并在环境副本中实际执行。
2. teacher 观察这些 student 行动及其结果，给出方案选择或排序，不生成新的行动。
3. 用 teacher 的选择监督 student 对自身方案的概率分配，下一轮仍由 student 自主产生候选和轨迹。

更新规则：对等长轨迹 τk，pθ(k|h)=softmaxk(log πθ(τk|h))，L=−Σk qT(k|h,{τ}) log pθ(k|h)。轨迹概率只包含 policy action likelihood，不包含环境转移概率。

待验证假设：teacher 的最优演示可能依赖 student 暂时不具备的技能；在已实际执行的 student 方案之间传递偏好，可以把监督集中在当前可实现的行为改进。

查新结论（早期文献核查，不是效果验证）：C。[AGGREVATE](https://arxiv.org/html/1406.5979#S2)、[LOLS](https://arxiv.org/html/1502.02206#S3)已有learner roll-in及候选rollout改进。剩余为独立teacher排序**student实执行短option**；与普通轨迹偏好学习的差异偏薄。

最小验证：K=3、H=2 的小规模 pilot；比较 teacher continuation CE、单步候选选择、短程 option 选择。记录成功率、teacher 偏好准确性、候选支持集覆盖和全部分叉成本。

同数据、同总成本的关键对照：同一options及排序：逐轨迹CE、偏好目标、token teacher监督；匹配分叉与训练量。

## Key risks
student 候选支持集可能缺失关键策略；teacher 也可能偏好看起来合理但无法完成任务的短程方案。

评审补充：候选内softmax不约束候选外行为；短option偏好不一定改善最终任务。

证伪条件：teacher 选出的方案不能提高后续自主成功率；或者需要过大的 K 才出现可学习的优质方案。

资源条件：Black-box teacher 排序；student trajectory logprob；环境分叉。训练不依赖外部 task reward，但评测需要可验证成功指标。

估算：条件估算：约 1–2 人周；每锚点约 K×H=6 次工具执行，加一次 teacher 比较。长观察会显著增加 teacher 输入成本。 本轮没有GPU计时与效果数据。

## Connections
已有wiki背景：[chen2026_look_ahead_before](../papers/chen2026_look_ahead_before.md)。

最近前作及剩余差异见上方查新结论；完整证据见[查新表](../../idea-stage/novelty-evidence-2026-10-14.md)。

