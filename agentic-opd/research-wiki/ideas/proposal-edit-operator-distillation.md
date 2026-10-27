---
type: idea
node_id: idea:proposal-edit-operator-distillation
title: "把 teacher 的纠错操作蒸馏为部署时的行动编辑器"
stage: proposed
outcome: pending
added: 2026-10-14T15:02:56Z
based_on: []
target_gaps: []
tags: ["agentic-opd", "method", "idea-creator-2026-10-14", "reserve"]
---

# 把 teacher 的纠错操作蒸馏为部署时的行动编辑器

**stage:** `proposed`  ·  **outcome:** `pending`

2026-10-14 idea-creator：A8；生成模型 `gpt-6-astra`；未验证储备。同家族模型评审为provisional，未运行pilot。见[排序报告](../../idea-stage/IDEA_REPORT.md)及[原始候选](../../idea-stage/candidates-2026-10-14.json)。

## Thesis
具体方法：

1. student 在真实状态 h 生成尚未执行的结构化工具行动 a0；独立 teacher 对它给出最小 edit script eT，例如修改工具名或参数字段。
2. student 的 editor mode 学习从 h、a0 直接预测 eT；训练 rollout 使用 student 自己预测的编辑，再执行最终行动。
3. 部署仍采用 proposal→student edit→execution，不调用 teacher。所有编辑标签来自独立 teacher。

更新规则：Ledit=−log πθ(eT|h,a0)，最终行动 a=Apply(a0,eθ)。pilot 固定 proposal policy，只训练 editor adapter，避免把 draft 改善与编辑器贡献混在一起；编辑格式限制为少量结构化操作。

待验证假设：小 student 可能已经能够提出接近正确的行动，但难以稳定发现参数、前置条件或证据引用错误；模仿 teacher 的局部纠错操作可能比重新生成完整行动更容易学会。

查新结论（早期文献核查，不是效果验证）：C。[SCoRe](https://proceedings.mlr.press/v306/lyu26j.html)已有teacher修复student错误；[DCR](https://arxiv.org/abs/2407.02397)已有学习refinement。剩余是**部署保留结构化edit policy**，单凭edit格式不足。

最小验证：在参数约束明确的文本工具环境，固定同一 draft policy；比较独立 teacher final-action CE、teacher edit CE、相同两次推理预算的普通 OPD。报告端到端成功率、错误修复率和错误引入率。

同数据、同总成本的关键对照：固定draft，同一修复标签转final-action或edit；比较等推理预算两遍重写，测误改率。

## Key risks
最小编辑可能无法表达真正需要的策略变化；如果允许任意重写，又可能退化为普通 action CE。

评审补充：edit太局部不能换策略，太自由则退化为完整重写；两遍推理混淆效果。

证伪条件：收益被相同推理预算的完整重生成消除；或者编辑器经常把正确 proposal 改错。

资源条件：Black-box teacher；结构化行动及 edit interpreter；student adapter 训练。无需环境分叉，但需要保存执行前的 proposal 和完整可见状态。

估算：条件估算：约 1–2 人周；每训练状态一次 teacher 编辑标注，部署多一次短编辑推理。应完整计入额外延迟与 tokens。 本轮没有GPU计时与效果数据。

## Connections
最近前作及剩余差异见上方查新结论；完整证据见[查新表](../../idea-stage/novelty-evidence-2026-10-14.md)。

