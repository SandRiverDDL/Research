# MiniMax-M2 Eval

```yaml
---
source_id: minimax-m2-series
section_type: stage-note
stage: eval
depth: working
confidence: medium
need_expert_review: false
---
```

## Core Design / Innovation

- MiniMax-M2 eval 按 design priorities 组织：agentic coding、agentic cowork、reasoning & knowledge，而不是只报通用 QA 分数。[25-28]
- Eval 的方法价值在于 shared scaffold / tool environment：TR 尽量让对比模型在同一 agent scaffold 下跑 coding/search/workspace tasks。[26-28]
- Within-series progression 比 cross-model single score 更有信息量：它把 M2 -> M2.5 -> M2.7 的提升和数据/Forge/self-evolution investment 对齐。[28-29]

## Why It Matters

MiniMax 的 eval 适合拿来比较“agentic data pipeline 是否转化成真实任务能力”。特别是 SWE、AppDev、Cowork、Excel/Finance、MLE Bench Lite，这些比普通 AIME/GPQA 更能反映训练 recipe 的设计目标。

## Mechanism Sketch

1. 对 closed frontier baseline 使用其最强 reasoning mode。
2. 对 agentic benchmarks 尽量共享 scaffold / tool environment。
3. 把 benchmark block 对齐到训练 pipeline：coding、AppDev、search、office/tools、reasoning。
4. 报 M2.5 作为 previous public release，并用 M2 -> M2.5 -> M2.7 曲线说明系列进步。

## Details / Evidence

- SWE-bench Pro / Multilingual / Multi-SWE / NL2Repo 等在 internal infra 上运行；部分使用 Claude Code unified scaffold，GPT 使用 native CodeX scaffold。[26-27]
- Terminal-Bench 2.0 使用 8 vCPU / 16GB sandbox、2h timeout、Terminus-2 XML scaffold、4 trials。[27]
- BrowseComp / Wide Search / RISE 共享 WebExplorer agent framework；token usage 超过最大 context 30% 时丢弃 assistant replies 和 tool returns 保持 search alive。[27]
- Reasoning/knowledge 使用 Artificial Analysis Index v4.0 protocol，无工具，single sample。[27]

## Gaps / Open Questions

- 多个 benchmark 是 internal 或 internal scaffold；可比性强于纯 release blog，但仍不能视作完全独立评测。
- 不同模型使用 native scaffold 的例外会影响 coding-agent fairness。
- Eval 数值不是 notes 主体，重点应放在 scaffold、timeout、tool、judge 和任务类型。

## Lookup-only

- 完整分数表回查 `[28]`。
- Within-series progression figure 回查 `[29]`。

## Evidence Anchors

- 25-28: eval settings.
- 28-29: main result table and within-series progression.
