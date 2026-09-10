# MAI-Thinking-1 Specialist Consolidation

```yaml
---
source_id: mai-thinking-1
section_type: consolidation
stage: post-training
substage: consolidation
depth: working
confidence: medium
need_expert_review: false
---
```

## Core Design / Innovation

- 核心设计是 specialist -> trace-SFT consolidation -> final RL：MAI 不做权重 merge，也不做 DeepSeek-style OPD/logit distillation，而是用 traces 把三个 specialists pack 到一个 model，再用 RL 修边界行为。[31, 49]
- SFT 在这里不是“万能聚合器”，而是 capability packing / policy initialization；它能工作依赖同源 specialists、兼容格式、分 teacher filtering，以及后续 final RL 修正。[49]
- 最值得学的 recipe 是 sample-weight vs token-weight 的 tension：按样本要平衡 STEM/agentic/helpfulness-safety，按 token 又天然被长 reasoning traces 主导。[49]
- Final RL 不是可有可无；它主要修 safety、over-refusal 和 style，同时保留 STEM/coding data 防止 complex reasoning 慢慢退化。[49]

## Why It Matters

这部分是 MAI 和 DeepSeek 最适合直接比较的地方。DeepSeek 用 student-generated trajectories 上的 teacher distribution matching；MAI 用 specialist traces 做 SFT packing。MAI 的方法没那么“新”，但更接近可复刻的小/中规模 recipe：训练 specialists、筛 traces、调 mixture、最后用 RL 防遗忘和修行为边界。

## Mechanism Sketch

1. 从 MAI-Base-1 mid-trained model 出发，训练 STEM/coding、agentic、helpfulness/safety 三个 specialists。[31, 49]
2. 对不同 teacher 使用不同 filtering / rejection sampling 采 traces。[49]
3. 用 trace SFT 聚合成 consolidated model，并用 public benchmarks、internal benchmarks、human evaluation 调 mixture 和 hyperparameters。[49]
4. 做 lightweight final RL，修 safety/over-refusal/style，同时保留 STEM/coding 防 reasoning regression。[49]

## Details / Evidence

- STEM 和 agentic teachers 从多个 RL climb checkpoints 采样 rollouts，偏向 later checkpoints；保留同一 context 的多个 correct rollouts，只轻度过滤 degenerate CoTs。[49]
- Helpfulness/safety teacher 使用 LLM judges 和 heuristic filters，从 style、structure、known defects 和 correctness 等维度筛 traces。[49]
- 最终 mixture 按 sample weight 是 STEM/coding 56%、agentic 11%、helpfulness/safety 33%。[49]
- 按 token weight，STEM/coding 占 89%，agentic 9%，helpfulness/safety 2%，因为 reasoning traces 更长。[49]
- Consolidation SFT 做 4 epochs，最大 learning rate 1e-5，并 decay 2x。[49]
- Final consolidation RL 训练到 128K max sequence length，并在 RL mixture 中保留少量 STEM/coding data；否则 complex reasoning 会在 climb 中慢慢退化。[49]

## Gaps / Open Questions

- 三个 specialist teachers 的 exact data composition、reward functions、checkpoint selection 规则没有完整公开。
- Consolidation SFT 后各 domain 的能力 tradeoff 曲线没有完整 ablation。
- Final RL 的 exact objective、RL mixture 比例和 gating criteria 没有公开。
- SFT 是否能在更强冲突的 specialists 之间聚合，需要和 DeepSeek OPD、其他 TR 对比。

## Lookup-only

- 56/11/33 sample weights、89/9/2 token weights、4 epochs、LR 1e-5、128K max sequence length。

## Evidence Anchors

- 31: specialist climbs + trace distillation SFT + final climb 总览。
- 49: teacher trace sampling、filtering、mixture weights、4-epoch SFT、final RL。
