---
type: idea
node_id: idea:teacher-evidence-bottleneck
title: "把 teacher 的证据选择蒸馏成行动前的上下文瓶颈"
stage: proposed
outcome: pending
added: 2026-10-14T15:02:56Z
based_on: ["paper:liu2026_memopd_onpolicy_distillation"]
target_gaps: []
tags: ["agentic-opd", "method", "idea-creator-2026-10-14", "reserve"]
---

# 把 teacher 的证据选择蒸馏成行动前的上下文瓶颈

**stage:** `proposed`  ·  **outcome:** `pending`

2026-10-14 idea-creator：A3；生成模型 `gpt-6-astra`；未验证储备。同家族模型评审为provisional，未运行pilot。见[排序报告](../../idea-stage/IDEA_REPORT.md)及[原始候选](../../idea-stage/candidates-2026-10-14.json)。

## Thesis
具体方法：

1. 在 student 历史 h 上，teacher 标注支持下一行动的少量原始 observation span IDs，并给出行动 aT；不生成额外事实。
2. student 先预测证据指针集合 M，再仅使用任务说明与所选原始片段生成行动。
3. 持续从部署形态的 student rollout 收集新历史，用 teacher 修正证据选择和行动。

更新规则：L = −log πθ(MT|h) − log πθ(aT|task, extract(h,MT))。训练对证据指针做 teacher forcing；部署使用预测的 M，因此必须单独测量指针误差造成的性能损失。

待验证假设：长程 agent 的错误经常来自旧证据遗失、过时 observation 干扰或无依据状态推断；显式学习选择证据可能比直接匹配行动 logits 更容易跨任务迁移。

查新结论（早期文献核查，不是效果验证）：P。[MemOPD](https://arxiv.org/html/2608.07068v1)恢复评分接口；[MAPD](https://arxiv.org/html/2607.24280)已有结构化证据中间表示。剩余delta是**独立teacher证据指针实际约束行动上下文**。

最小验证：在检索加文件编辑任务中插入可控的过时返回和无关工具输出；比较 full-history OPD、等长摘要 OPD、证据指针瓶颈；报告自主成功率、证据遗漏率和上下文成本。

同数据、同总成本的关键对照：同一证据/行动标签：full-history、等长摘要、硬证据瓶颈；分别测oracle与预测指针。

## Key risks
下一步所需证据可能不足以维持长期任务状态；硬瓶颈也可能删除 teacher 未注意到的信息。

评审补充：teacher-forced指针造成部署落差；下一步充分证据未必维持长期状态。

证伪条件：使用 oracle 证据指针仍无收益；或者实际预测指针的误差抵消全部收益。

资源条件：Teacher 文本标注；带稳定 span IDs 的历史；可控制行动输入上下文的运行时。无需 teacher logits 或环境隐藏状态。

估算：条件估算：约 1–2 人周实现；每状态一次 teacher 证据与行动标注，部署增加一次短指针预测。必须同时计入检索阶段和行动阶段推理量。 本轮没有GPU计时与效果数据。

## Connections
已有wiki背景：[liu2026_memopd_onpolicy_distillation](../papers/liu2026_memopd_onpolicy_distillation.md)。

最近前作及剩余差异见上方查新结论；完整证据见[查新表](../../idea-stage/novelty-evidence-2026-10-14.md)。

