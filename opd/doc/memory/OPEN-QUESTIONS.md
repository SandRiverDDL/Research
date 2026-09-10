# OPD 未决问题

> 记录长期悬而未决的问题。短期下一步放 `doc/memory/STATE.md`。

## ResearchStudio-Idea Integration

- 如何用全局 cards/venue landscape 扩大 Phase 0 recall，同时以 freshness search 补 cutoff 后缺口？
- 哪些 bottleneck claims 必须回读原文哪些部分；coverage saturation、反例和停止条件如何定义？
- 应做 raw-full-text、作者摘要、模型摘要和 L1 card 四种输入的受控对照，检验 summary compression 对 bottleneck reconstruction 与 idea taste 的影响。
- 《Measuring the Gap Between Human and LLM Research Ideas》(arXiv:2607.01233) 的 full-context ablation 使用模型生成的 summary 进入 ideation，不能直接证明 summary 可以替代原始全文。

## Failure-Mode Taxonomy

- `policy-gradient-variance`、`sgo-generation-cost`、`kld-gradient-explosion` 是否能干净覆盖现有 OPD failure modes？
- `compounding-error` 在 OPD 语境下应保持独立，还是合并为 `exposure-bias` 的 alias？

## Coverage Gaps

- preference signal / PRM step-level signal 覆盖不足。
- hardness / curriculum filtering 代表工作较少，可能需要补搜。
- survey references 中不含 OPD 字样但语义相关的 self-distillation / DAgger / on-policy learning refs，需要通过 semantic skim 维持召回，不应只靠标题正则。
