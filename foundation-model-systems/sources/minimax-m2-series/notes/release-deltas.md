# MiniMax Release Deltas

```yaml
---
source_id: minimax-m2-series
section_type: stage-note
stage: release-delta
depth: working
confidence: medium
need_expert_review: false
---
```

## Core Design / Innovation

- M2 series TR 同时覆盖 M2、M2.5、M2.7 的 progression；它适合做 lineage-reference，不应在当前先进实践总结中压过 M3。[25-30]
- M2.7 的新增重点是 self-evolution：模型进入自己的 RL / scaffold 迭代工作流，读 logs、诊断异常、修改配置和 scaffold。[24-30]
- MiniMax-M3 是 current-practice delta：MSA paper / M3 model card 公开 sparse attention、kernel、1M context、native multimodality 等后续设计，但不是 M3 的完整训练 TR。[m3-msa:1-6]

## Why It Matters

这解决了 MiniMax “是否单独建 M3” 的边界：如果研究 training recipe 和后训练，M2 series 是可读性最强的 lineage-reference；如果总结当前 MiniMax 或 long-context architecture / sparse attention，M3/MSA 优先。当前不把 M3 当完整 training anchor，只是因为训练流程披露不足，不代表 M2 设计更新。

## Mechanism Sketch

1. M2 -> M2.5 -> M2.7：同一训练系统继续扩充 agentic data、Forge RL 和 self-evolution。
2. M2.7 self-evolution：human 设目标和审查，agent 自主 profile runs、读 logs、debug、改配置、写报告。
3. M3/MSA：Index Branch 选择 KV blocks，Main Branch 做 block-sparse attention；KL loss 对齐 indexer 和 main branch；kernel 用 exp-free TopK 和 KV-outer sparse attention。

## Details / Evidence

- M2.7 在内部 RL team workflow 中承担 30%-50% 日常 iteration workload，并能 100-round autonomous scaffold iteration，报告内部评测提升。[25]
- Eval 部分显式把 M2.5 作为 previous public release，M2.7 作为当前 release，对 11 个 benchmark 展示 within-series progression。[25-29]
- MSA 在 109B native multimodal MoE 上报告与 GQA 接近，并在 1M context 降低 attention compute / prefill / decode wall-clock cost。[m3-msa:1-2]
- MSA 的 Index Branch 为每个 GQA group 选 top-k KV blocks，并强制 local block；训练用 KL loss、gradient detach、indexer warmup。[m3-msa:4-6]

## Gaps / Open Questions

- M2.5 的独立 release details 如果用户关注 OPD/MOPD 或具体 model behavior，可能仍需单独补 delta。
- M3 是否继承 M2 series 的 agentic data / Forge / interleaved thinking，当前 MSA paper 不能证明。

## Lookup-only

- M2.5/M2.7 benchmark table 和 progression 回查 `[25-29]`。
- MSA kernel 细节回查 `[m3-msa:6-8]`。

## Evidence Anchors

- 24-30: self-evolution and M2.5/M2.7 eval progression.
- `[m3-msa:1-6]`: MiniMax-M3 / MSA architecture delta.
