# DeepSeek-R1 Reward and Verifier Design

```yaml
---
source_id: deepseek-r1
section_type: reward-verifier
stage: post-training
substage: reward-verifier
depth: working
confidence: high
need_expert_review: false
---
```

## Core Design / Innovation

- R1-Zero 使用 accuracy reward 与 format reward；数学 final answer 和代码测试提供确定性 outcome supervision。[3-4]
- DeepSeek 明确避免在可验证 reasoning 上使用 neural process/outcome RM，因为大规模优化容易产生 reward hacking，且反复训练 RM 增加系统复杂度。[4]
- 最终 R1 只在 general behavior 上引入 learned helpfulness/safety reward：helpfulness 只判断 final summary，safety 判断包含 reasoning 在内的完整回答。[6-7]

## Why It Matters

最值得内化的是 reward-source matching：能执行或符号验证的任务优先使用硬 verifier；只有主观行为才使用 learned preference model。否则 reward hacking 与 capability regression 会更难定位。

## Mechanism Sketch

1. 解析 final answer 或执行代码测试。
2. R1-Zero 额外检查 `<think>`/`<answer>` format。
3. General helpfulness 使用长度平衡的 pairwise preference data 训练 RM。
4. Safety 使用 safe/unsafe point-wise classifier。
5. 最终 RL 按 prompt 类型路由到对应 reward family。[3-7]

## Details / Evidence

- Format reward 只约束结构，不判断 reasoning process 是否正确。[3-4]
- Helpfulness pair 会重复交换 A/B 顺序评审以缓解 positional bias，并只保留差异足够明确的样本。[7]
- “final-summary helpfulness / full-response safety”的切分是明确的 response-surface 设计。[6-7]

## Gaps / Open Questions

- Verifier parser edge cases、false positive 和 code sandbox security 未达到开放 recipe 深度。
- Reward models 与训练数据没有开放。
- 最终 RL 中多 reward 聚合和 anti-hacking monitoring 披露不完整。

## Lookup-only

- RM 数据规模和训练超参：第 7 页。

## Evidence Anchors

- 3-4：rule-based accuracy/format reward。
- 6-7：helpfulness 与 safety RM。
