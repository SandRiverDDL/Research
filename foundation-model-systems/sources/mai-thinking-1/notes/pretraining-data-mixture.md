# MAI-Thinking-1 Pretraining Data Mixture

```yaml
---
source_id: mai-thinking-1
section_type: pretraining-data-mixture
stage: pretraining
substage: none
depth: working
confidence: medium
need_expert_review: false
---
```

## Core Design / Innovation

- 核心设计是 data mixture optimization，而不是 data cleaning 本身：MAI 把 hundreds of sources 的比例选择做成一个经验优化问题，用 NLL held-out eval、scale-ladder ablations、local/global search 和 repetition caps 逐步选 mix。[16-20]
- 最关键发现是 rank non-invariance：一个 STEM-heavy mix 在小规模更好，但在目标规模输给 code-heavy mix；这说明“小模型 ablation 胜出”不能直接外推到大模型。[17-18]
- Repetition caps 是配比搜索的一部分：高质量小数据即使短期 NLL 好，也可能因为重复过多和 diversity 不足在大规模训练中变差。[17-20]
- MAI 的 final mix 数字不是最该学的东西；真正该学的是“用 ladder 预测 scale transfer，用 held-out eval 和 repeat control 约束数据比例”。[16-20]

## Why It Matters

这部分直接关系到 base-model taste：数据比例不是按直觉拍出来，也不是小模型 sweep 赢了就结束。MAI 展示的是一种工业界选数据的闭环：小规模探索、跨 scale 验证、发现 rank flip、再限制重复和调整全局比例。对想做基模的人，这比记住 Code 54.6% 更重要。

## Mechanism Sketch

1. 把大量 source family 和子 source 放进 mixture search，而不是只按粗类别调比例。[16-20]
2. 用 held-out NLL eval 作为早期选择信号，并做 scale-ladder ablations 检查小规模结论能否迁移。[16-18]
3. 先做 local search 调某类内部来源，再做 global search 调大类之间比例。[16-20]
4. 用 repetition caps 控制小而高质量数据源被过度重复，避免 diversity 不足。[17-20]
5. Mid-training 继续偏 STEM/math/code；continued pretraining、context extension 和 YOLO/cluster engineering 另见 `pretraining-engineering.md`。[20-21]

## Details / Evidence

- MAI-Thinking-1 是 35B active / 1T total MoE；Microsoft 声称没有使用 third-party model distillation，也没有在 pretraining 中使用 language-model-generated synthetic data。[1-2]
- MAI-Base-1 使用 30T pretraining tokens，再经过 3.55T mid-training tokens；pretraining data 来自 publicly available + licensed human-generated data，并全部 in-house processing。[2, 5]
- Source families 包括 web HTML、web PDFs、public GitHub code、books/journals、news、multilingual text、domain-specific materials。[12-13]
- Governance claims 包括尊重 web controls、排除 policy-violating sources、third-party commercial diligence、不使用 private customer data（除 opt-in/covered cases）、PII-risk filtering 和 safety filtering。[13]
- Final pretraining composition 按 source family 公开：Code 54.6%、STEM 15.8%、Math 5.4%、Books/Journals 3.1%、PDFs 4.7%、Web text 14.9%、other multilingual 1.6%。[19-20]
- Mid-training 只复用 pretraining corpus，不引入 new/synthetic sources；配比偏 STEM/math/code：STEM/math 35%、code 55%、background 10%。[20]
- Appendix B 给出 pipeline 细节：web crawl filtering/dedup/quality scoring、AI-content filtering、STEM classifiers、PDF OCR/normalization、GitHub filtering/dedup/semantic dedup/decontamination、quality-aware sampling。[82-85]

## Gaps / Open Questions

- Exact dataset/provider identities 和 filtering thresholds 没有公开。
- NLL objectives 对 downstream RL/post-training results 的预测力没有充分拆解。
- AI-generated-content detector 的 precision/recall 和 false positive 没有公开。
- Decontamination 对 coding 和 common ML datasets 之外的 benchmark-like content 如何处理，仍不清楚。

## Lookup-only

- Final source-family percentages、Math 5.28x epochs、cutoff tables、Appendix B 的具体 pipeline steps。
- 这些数字用于回查和比较，不应当作可直接迁移的 recipe。

## Evidence Anchors

- 1-2: from-scratch/no-distillation/no-synthetic pretraining claims。
- 5: 30T pretraining + 3.55T mid-training。
- 12-13: source families 和 governance。
- 16-20: data mixture optimization、scale ladder、rank non-invariance、final composition。
- 21: mid-training data mixture handoff to context-extension engineering。
- 82-85: web/PDF/books/GitHub pipeline details。
