# MAI-Thinking-1 Self-distillation

```yaml
---
source_id: mai-thinking-1
section_type: sft-distillation
stage: post-training
substage: sft-distillation
depth: working
confidence: medium
need_expert_review: false
---
```

## Core Design / Innovation

- 核心设计是把 self-distillation 作为 long RL 的工程控制手段，而不是普通 SFT：它负责 collapse recovery、checkpoint migration、prompt-to-chat format conversion 和 policy reset。[34-35]
- MAI 的关键经验是“trace 不越多越好”：O(1M) reasoning traces 已足以 match teacher，更多可能 over-constrain policy，降低后续 RL exploration。[35]
- Trace diversity 比单 prompt 多采样更重要：later checkpoints 更有价值，跨多个强 checkpoint 比 final-only 更好，固定 token budget 下 prompt diversity 优先。[36]
- SFT 本身也被当成稳定性控制：混入 mid-training data 防 long-context forgetting，调 dropout/MoE balancing 防 collapse 和 expert imbalance。[36-37]

## Why It Matters

这部分改变了对 SFT 的理解。MAI 不是把 SFT 当“最后对齐”或“能力注入”那么简单，而是把它作为长 RL climb 的重启点和迁移层。对小规模 post-training 来说，最可学的是 reset / transfer / diversity control，而不是 1M traces 这个数字。

## Mechanism Sketch

1. RL climb 生成 rollouts，筛选后对 mid-trained checkpoint 做 SFT。[34-35]
2. SFT 后的 checkpoint 成为下一段 RL climb 起点。[34-35]
3. 如果 RL run collapse，用 self-distillation carry over progress，而不是简单回退到 collapse 前 checkpoint。[34-35]
4. 如果 pre-/mid-trained base 更新，用 self-distillation 把旧 climb progress 搬到新底座。[35]
5. 用 trace count、checkpoint diversity、prompt diversity 和 mid-training data mix 控制 exploration 与 forgetting。[35-37]

## Details / Evidence

- 初始 climb 会用 task-specific prompts 诱导目标行为；self-distillation 可以把 prompt-induced behavior 转成 native chat format 下的 SFT data。[34]
- Self-distillation 时可以过滤 reward hacking 或 undesired samples。[35]
- MAI 最终只用 successful traces，但报告指出包含错误 final answer 的 traces 也能达到相近表现。[35]
- Later-stage traces 更重要；很早期 checkpoint traces 会拉低性能，只用 final checkpoint traces 也更弱。[36]
- 固定 token budget 下，prompt diversity 比每个 prompt 更多 traces更有价值；simple random sampling 优于 shortest-trace sampling 和一些 heuristic filtering。[36]
- Self-distillation 可能遗忘 mid-training 学到的 long-context behavior，因此在 length extension 前会混入 mid-training data。[36]
- Self-distillation SFT 使用 128K packed sequences、global batch size 2048、cosine LR schedule、dropout 0.15 和 MoE load balancing coefficient 1e-2。[36-37]

## Gaps / Open Questions

- Self-distillation traces 的 exact prompt/task distribution 没有公开。
- Reward hacking filter 的规则和阈值没有公开。
- “successful traces only” 与 “incorrect traces similar” 的取舍缺少完整 ablation。
- Self-distillation 和禁止 third-party distillation 的 provenance 边界清楚，但行为学习机制仍值得和其他 TR 比较。

## Lookup-only

- 128K packed sequences、global batch 2048、dropout 0.15、MoE balancing coefficient 1e-2。
- 这些 hyperparameters 用于回查，不应直接迁移。

## Evidence Anchors

- 34-35: self-distillation 用途、collapse recovery、checkpoint transfer、reward-hacking filter。
- 35-36: O(1M traces、successful vs incorrect traces、later checkpoints、prompt diversity。
- 36-37: long-context forgetting、SFT hyperparameters、dropout 和 MoE balancing。
