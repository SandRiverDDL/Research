---
type: idea
node_id: idea:post-update-transfer-selected-demonstrations
title: "按 student 更新后的自主收益选择 teacher 演示"
stage: proposed
outcome: pending
added: 2026-10-14T15:02:56Z
based_on: ["paper:chen2026_look_ahead_before"]
target_gaps: []
tags: ["agentic-opd", "method", "idea-creator-2026-10-14", "reserve"]
---

# 按 student 更新后的自主收益选择 teacher 演示

**stage:** `proposed`  ·  **outcome:** `pending`

2026-10-14 idea-creator：A6；生成模型 `gpt-6-astra`；高上限储备。同家族模型评审为provisional，未运行pilot。见[排序报告](../../idea-stage/IDEA_REPORT.md)及[原始候选](../../idea-stage/candidates-2026-10-14.json)。

## Thesis
具体方法：

1. 在 student 访问的 h，请固定独立 teacher 提供 K 个短纠错 demonstration。
2. 对每个 demonstration，用独立的影子 adapter 做一次相同规模的蒸馏更新。
3. 在不带 teacher 帮助的独立 sibling episodes 上评估更新后策略，只把自主迁移收益最大的 demonstration 用于实际更新。

更新规则：θk=θ−α∇CE(dk;θ)；k*=argmaxk mean[R(πθk,E)−R(πθ,E)]；实际更新 θ←θ−α∇CE(dk*;θ)。最终 policy update 仍来自独立 teacher demonstration。

待验证假设：能救好当前任务的演示不一定最容易被 student 学会；直接选择产生实际学习迁移的演示，可以改善 assistance 到 competence 的转化。

查新结论（早期文献核查，不是效果验证）：P。[MetaDistil](https://aclanthology.org/2022.acl-long.485/)已用更新后student反馈优化teacher；[SmartAD](https://aclanthology.org/2026.findings-acl.1349/)按student NLL选演示。这里**teacher固定，按独立自主迁移收益选择演示**，区别明确。

最小验证：只训练小型 LoRA，K=2，每次使用 4 个独立 sibling episodes；比较随机选择、当前任务回报选择、更新后自主收益选择，并加入使用全部 demonstration 的同总预算基线。

同数据、同总成本的关键对照：同一K份演示，比较随机、NLL、当前成功率、更新后收益选择；必须含同总成本“全部演示”。

## Key risks
短期更新收益噪声大，可能过拟合很小的选择集；计算成本也可能高于所得收益。

评审补充：影子更新收益高方差，赢家偏差与选择集过拟合；正式样本效率可能抵不过选择成本。

证伪条件：选择排序在独立重复中不稳定；或者计入影子更新和评测后，固定使用全部 demonstration 更有效。

资源条件：Student 参数与可复制 adapter；独立 teacher；可重置任务族及可靠成功信号。选择集与最终测试集必须分开。

估算：条件估算：约 2–4 人周；每锚点增加 K 次影子更新与 K×4 次自主评估。先限制 50–100 个锚点，不能预设完整训练的 GPU 时长。 本轮没有GPU计时与效果数据。

## Connections
已有wiki背景：[chen2026_look_ahead_before](../papers/chen2026_look_ahead_before.md)。

最近前作及剩余差异见上方查新结论；完整证据见[查新表](../../idea-stage/novelty-evidence-2026-10-14.md)。

