---
type: idea
node_id: idea:evidence-belief-ledger-transfer
title: "蒸馏有证据出处的工作状态"
stage: proposed
outcome: pending
added: 2026-10-14T15:02:56Z
based_on: ["paper:agarwal2023_onpolicy_distillation_language", "paper:liu2026_memopd_onpolicy_distillation"]
target_gaps: []
tags: ["agentic-opd", "method", "idea-creator-2026-10-14", "reserve"]
---

# 蒸馏有证据出处的工作状态

**stage:** `proposed`  ·  **outcome:** `pending`

2026-10-14 idea-creator：S2；生成模型 `gpt-6.1-sol`；未验证储备。同家族模型评审为provisional，未运行pilot。见[排序报告](../../idea-stage/IDEA_REPORT.md)及[原始候选](../../idea-stage/candidates-2026-10-14.json)。

## Thesis
具体方法：

1. student 正常 rollout；在选定状态，teacher 仅根据可见历史生成紧凑 ledger：已确认事实、已改变资源、未完成条件及对应 observation 引用。
2. student 在同一历史上通过辅助输出预测 ledger，主 actor 继续接受独立 teacher 的常规 action OPD。
3. 部署时只运行 student actor；teacher ledger 不作为额外输入。

更新规则：L=L_OPD+λ[-log p_S(b_T|h)]，其中 b_T 是 teacher 标注的结构化工作状态；辅助输出与 actor 共享主体表示。核心改变是增加跨 turn 状态监督，而非调整 action-token 权重。

待验证假设：长程失败常发生于行动所依据的工作状态已经过时。显式预测哪些事实仍成立、哪些要求尚未满足，可使 action policy 更稳定地使用工具反馈。

查新结论（早期文献核查，不是效果验证）：C。[MAPD](https://arxiv.org/html/2607.24280)已有plan/evidence JSON，[MemOPD](https://arxiv.org/html/2608.07068v1)已有memory机制。现方案主要是**常规OPD加结构化状态辅助CE**，算法delta偏薄。

最小验证：固定 action OPD 数据，比较无辅助任务、等长普通摘要辅助任务、证据 ledger 辅助任务；匹配训练 tokens，测长程 success、过时事实导致的行动错误及 observation 引用准确率。

同数据、同总成本的关键对照：相同actor数据、训练tokens：普通摘要辅助与ledger辅助；测实际状态错误及成功率。

## Key risks
teacher ledger 可能遗漏或误判状态；固定字段也可能只适用于特定工具域。

评审补充：ledger部署不使用，正确预测不保证actor使用；辅助任务也可能抢容量。

证伪条件：ledger 预测显著改善但 task success 不变；或等长普通摘要获得相同收益。

资源条件：独立 text teacher；完整可见工具历史；支持共享主体辅助输出的 student 训练。无需环境分叉或隐藏状态。

估算：上述模型规模假设下，先标注 10^3–10^4 个 student 状态；每状态新增一次短 teacher 输出与辅助 CE。预计一至两周完成最小实现，训练成本由 ledger 长度决定。 本轮没有GPU计时与效果数据。

## Connections
已有wiki背景：[agarwal2023_onpolicy_distillation_language](../papers/agarwal2023_onpolicy_distillation_language.md)；[liu2026_memopd_onpolicy_distillation](../papers/liu2026_memopd_onpolicy_distillation.md)。

最近前作及剩余差异见上方查新结论；完整证据见[查新表](../../idea-stage/novelty-evidence-2026-10-14.md)。

