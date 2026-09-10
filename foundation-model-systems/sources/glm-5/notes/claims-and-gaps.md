# GLM-5 Claims / Gaps

```yaml
---
source_id: glm-5
section_type: claims
stage: source-audit
depth: working
confidence: medium
need_expert_review: false
---
```

## Strong Claims

- GLM-5 是 GLM-5 lineage 的完整训练/系统 anchor，GLM-5.1 和 GLM-5.2 更适合按 delta 读。
- DSA + long-context midtraining + slime agentic RL 是一条连贯系统主线，不能只抽成“RL trick”。
- Long-horizon agentic RL 的关键证据在 infra / environment / context management，而不是普通数学 benchmark。

## Weaker / Underdisclosed Claims

- “best open-source / closing frontier gap”依赖 benchmark selection、scaffold、judge 和 tool permissions，不能直接当作通用能力结论。
- On-Policy Cross-Stage Distillation 与 OPD/MOPD 的关系需要单独比较；目前只能说它是 cross-stage teacher distillation，不等同于所有 OPD family 方法。
- DSA 在 RL 阶段的 deterministic top-k / freeze indexer 是很重要的实践 insight，但公开 ablation 仍有限。

## Comparison Hooks

- vs Kimi K2.5: GLM-5 更偏 coding/search/terminal agentic engineering，Kimi K2.5 更偏 multimodal + Agent Swarm。
- vs MiniMax-M2: 两者都重视 agent-native RL infra；GLM 用 slime/Multi-Task Rollout Orchestrator，MiniMax 用 Forge。
- vs DeepSeek/MiMo/Nemotron: cross-stage distillation / OPD / MOPD 需要统一 lens。

## Evidence Anchors

- 4-9: architecture and pretraining.
- 10-17: post-training and asynchronous RL.
- 17-23: agentic environments and eval.
