# MAI-Thinking-1 RL Training

```yaml
---
source_id: mai-thinking-1
section_type: rl-training
stage: post-training
substage: rl-training
depth: working
confidence: medium
need_expert_review: false
---
```

## Core Design / Innovation

- 核心设计是 long reasoning RL 的 stability control surface：MAI 没有把能力提升归因于单个算法名，而是同时控制 entropy、ratio spikes、language drift、length、problem difficulty、rollout freshness 和 eval gating。[31-36]
- Adaptive entropy control 通过动态调整 upper clip bound 控制 policy entropy，不是简单加 entropy bonus 或固定调大 PPO clip。[31-32]
- Outer ratio clip 是额外的 ratio 安全阀，用来限制 PPO/GRPO-style objective 中 inner clip 没覆盖的极端分支，避免 catastrophic gradient-norm spikes。[32-33]
- Sampling/curriculum 的核心是把 rollout budget 花在“可学习区间”的问题上：early-exit pass-rate filter、top-p mask replay、length curriculum 共同提高稳定性和效率。[34-36]

## Why It Matters

MAI 这部分最值得学的是 post-training taste：长推理 RL 不是“把 GRPO 跑久一点”，而是一个多控制变量系统。真正的 recipe 是如何防止模型在长 CoT、长 rollout、tool/environment interaction 中因为 entropy、ratio、长度、语言漂移或 off-policy mismatch 失控。

## Mechanism Sketch

1. 从 mid-trained MAI-Base-1 启动 post-training，不是从随机参数或 raw base 直接开始。[2, 31]
2. 训练三个 specialists：STEM/competitive coding、agentic capabilities、helpfulness/safety。[31]
3. 使用 GRPO-derived token-level policy gradient，response-level group-normalized reward 共享给 response tokens。[31-33]
4. 用 adaptive entropy、outer ratio clip、reward decomposition、pass-rate filtering、top-p mask replay 和 length curriculum 稳定 long climb。[31-36]
5. RL 过程中反复 self-distill 到 checkpoint，最后再做 specialist consolidation。[34-37, 49]

## Details / Evidence

### Objective / Stability

- RL objective derived from GRPO，并使用 token-level policy gradient。[31-33]
- Adaptive entropy control 通过调整 upper clip bound 控制 policy entropy，没有额外加 entropy bonus。[31-32]
- Outer ratio clip 先把 importance ratio 限制在更宽安全范围内，再进入 PPO/GRPO-style objective；它不是 gradient clipping。[32-33]

### Reward / Behavior Constraints

- Reward decomposition 是 `task reward + language consistency reward - length penalty`。[33]
- Language consistency reward 处理 CoT 中的 foreign-language drift；length penalty 用 pass rate 做 difficulty-aware adjustment，避免无差别惩罚难题长推理。[33]

### Sampling / Curriculum

- Early-exit sampling 先采 `G_early=16` 个 rollouts，只有 pass rate 落在可学习区间时才采完整 `G=128` 个 rollouts；完整 group 也再做 pass-rate filter。[34, 36]
- Rollout sampling 使用 top-p；训练时 replay top-p truncation mask，把采样时 nucleus 外的 logits 设为 `-inf`，减少 off-policy mismatch。[34]
- Length curriculum 从 8K rollout cap 开始，逐步扩到 16K、32K、64K、128K。[34, 36]

### Specialist Climbs

- STEM climb 使用 math、science、competitive coding tasks，并研究 CoT evolution。[37-39, 89-94]
- Agentic climb 聚焦 SWE/tool tasks，包含 tool schemas、SWE environment-building infrastructure 和 ReAct-style loops。[39-44, 94, 97, 101]
- Helpfulness/safety climb 包含 instruction-following data、constraint taxonomy、hybrid reward signals，以及 unsafe compliance / over-refusal 数据。[44-49]

## Gaps / Open Questions

- STEM、agentic 和 safety climbs 的 exact prompt distributions、reward functions、environment mixture 没有公开。
- Off-policy 大 run 和 on-policy debug run 的差异、staleness 对最终能力的影响没有充分公开。
- MAI 如何判断某条 climb 饱和、何时切到 self-distillation 或 consolidation，没有可复现 gating criteria。

## Lookup-only

- Group size、rollout cap、sequence length、具体 appendix traces、各 benchmark entries。
- 这些细节用于核查和复现设计，不是首读重点。

## Evidence Anchors

- 1-2: hill-climbing framing 和 from-scratch/no-CoT-distillation claims。
- 31-33: RL objective、adaptive entropy control、outer ratio clip、reward decomposition。
- 34-36: early-exit sampling、top-p mask replay、length curriculum。
- 37-44: STEM 和 agentic climbs。
- 44-49: helpfulness/safety climb 和 reward/data design。
- 89-101: qualitative traces、tool schema、IF taxonomy、SWE infra。
