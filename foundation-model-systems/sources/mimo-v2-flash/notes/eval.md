# MiMo-V2-Flash Evaluation

```yaml
---
source_id: mimo-v2-flash
section_type: eval
stage: eval
substage: benchmark-and-mopd-ablation
depth: working
confidence: medium
need_expert_review: false
---
```

## Core Design / Innovation

- Eval 不是只有 final leaderboard；TR 里最有价值的是 MOPD ablation：ORM-only、MOPD without ORM、MOPD 三条曲线比较，直接支撑 MOPD 的方法 claim。[19]
- Final benchmark suite 覆盖 reasoning、general writing、long context、code agent、general agent，和 Kimi-K2、DeepSeek-V3.2、Gemini、Claude、GPT-5 比较。[20]
- Agentic eval 包括 SWE-Bench Verified / Multilingual、Terminal-Bench、BrowseComp、Tau2-Bench；这与 MiMo 的 agentic RL training environments 对齐。[20]
- 论文承认和最强 closed models 仍有 gap，这比只做 frontier rhetoric 更稳健。[22]

## Why It Matters

MiMo 的 eval 值得学的是：method claim 需要 ablation 支撑。MOPD 如果只给 final table，很难判断贡献来自 specialist teachers、ORM、SFT 还是 benchmark选择；Figure 6 至少把 ORM-only、MOPD w/o ORM 和完整 MOPD 分开了。

## Mechanism Sketch

1. 用 Table 7 看 MOPD 是否能接近/超过 best teacher。
2. 用 Figure 6 看 MOPD vs ORM-only / MOPD w/o ORM 的训练曲线。
3. 用 Table 9 看 final model 在 reasoning、writing、long context、code/general agent 上的外部定位。
4. comparison 时优先看 setting / benchmark scope / ablation，而不是只摘分数。

## Details / Evidence

- Table 7 显示 MOPD 后 student 在 AIME 2025、HMMT、LiveCodeBench、Tau2-Bench 等任务上达到或超过 best teacher，但在 GPQA-Diamond、creative writing、SWE-Bench Verified、BrowseComp 有下降。[14]
- Figure 6 显示在 AIME 2025 和 LiveCodeBench 上，MOPD 优于 ORM-only 和 MOPD w/o ORM。[19]
- Table 9 的 final comparison 覆盖 MMLU-Pro、GPQA-Diamond、HLE、AIME、HMMT、LiveCodeBench、Arena-Hard、LongBench V2、MRCR、SWE-Bench、Terminal-Bench、BrowseComp、Tau2-Bench。[20]

## Gaps / Open Questions

- Evaluation setting 细节不如 GLM-5.2 blog 详细；sampling、scaffold、tools、timeouts、judge model 需要补查。
- Table 9 混合 open/closed models，但不清楚是否完全 same scaffold / same context / same tool access。
- BrowseComp 和 creative writing 下降没有解释，可能反映 teacher/domain routing 或 reward mixture tradeoff。

## Lookup-only

- Table 7 and Table 9 exact benchmark numbers。[14, 20]
- Figure 6 curve shape and task names。[19]

## Evidence Anchors

- 14: Table 7 MOPD before/after vs teacher。
- 19: Figure 6 method ablation。
- 20: Table 9 final benchmark comparison。
- 22: conclusion and limitation。
