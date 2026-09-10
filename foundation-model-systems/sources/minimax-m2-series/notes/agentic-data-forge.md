# MiniMax-M2 Agentic Data / Forge

```yaml
---
source_id: minimax-m2-series
section_type: stage-note
stage: agentic-data-rl-infra
depth: working
confidence: high
need_expert_review: true
---
```

## Core Design / Innovation

- MiniMax-M2 最值得学的是 agent-driven data pipelines：训练数据不是静态 QA，而是带 runnable workspace、artifact、verifier 和 reward 的 trajectory。[7-16]
- SWE/AppDev/Terminal/Cowork/Reasoning/Conversation/Role-play 各有 domain-specific pipeline，但共同模式是“任务构造 -> 轨迹采样 -> 环境/产物验证 -> 过滤/增强”。[7-16]
- Forge 是 agent-native RL infra，目标是在 throughput、stability、agent flexibility 的 impossible triangle 中支持 white-box 和 black-box/API agents。[19-23]
- Mixed-domain RL 在每个阶段同时抽 reasoning、coding、agent、general 四类数据，避免单域 RL 造成 forgetting 或 negative transfer。[19]

## Why It Matters

这份 TR 对后训练岗位很有参考价值：它把“数据怎么来、reward 怎么对齐 artifact、agent 怎么在环境里跑、RL infra 怎么吃轨迹”连起来，而不是只讲最后的 PPO/GRPO。尤其 AppDev / Cowork / Terminal 这些场景，比传统数学/代码题更贴近真实 agent 产品。

## Mechanism Sketch

1. SWE pipeline 从 issue/PR 构建 Docker environment、F2P/P2P tests、task tags 和 reward。
2. AppDev pipeline 用 expert meta queries、expert system prompts、sandbox deploy 和 Agent-as-a-Verifier 做 rejection sampling。
3. Terminal pipeline 从 structured schemas 生成 Dockerfile/test script，再做 query evolution、unified testing 和 difficulty calibration。
4. Cowork pipeline 针对 search、office、finance、slides 等 artifact，用 pairwise comparison 和 artifact-specific verifier 过滤。
5. Forge 将 Agent Side、Training/Inference Side 和 Middleware/Data Pool 解耦，支持不同 agent scaffold 接入同一训练系统。

## Details / Evidence

- SWE pipeline 覆盖 10+ programming languages，按 bug fix / feature addition / performance optimization / code review 等任务类型构建不同 reward。[8-9]
- AppDev 使用专家 meta queries、技术栈/场景 seed、prompt distillation、rubric-based reward 和 AaaV 三层验证：execution、interaction、visual aesthetics。[9-11]
- Terminal-Gym 用 environment/test generation、query evolution/unified testing、difficulty calibration 构建复杂 terminal tasks，并继续扩展到 Anything2Docker / CVE-Factory。[12]
- Reasoning data scaling 明确分 query-side、response-side、training-side scaling，并动态调整 query expansion vs response expansion ratio。[15]
- Mixed-domain RL 调整 domain mixing ratios、context length 和 difficulty distribution，早期偏 foundational，后期提高 agent/coding 比例。[19]
- Forge 用 Gateway Server / Data Pool / LLM Server / Env Server / Reward Server 分离 agent loop 与训练 loop。[20-23]

## Gaps / Open Questions

- 大量 pipeline 是高层描述；具体数据量、filter thresholds、rubric、reward model training 和 verifier false-positive rate 未完整披露。
- Forge 的 off-policy 处理、windowed-FIFO scheduling、prefix-tree merging 和 sample efficiency 需要继续细读。
- White-box / black-box agent 混训的 credit assignment 和 policy update 边界仍不清楚。

## Lookup-only

- 各 domain pipeline 的原文细节回查 `[7-16]`。
- Forge architecture figure 和 system objectives 回查 `[19-23]`。

## Evidence Anchors

- 7-16: agentic data pipelines.
- 16-20: SFT / RL / mixed-domain training.
- 20-23: Forge infrastructure.
