# Nemotron 3 Post-training Summary

```yaml
---
source_id: nemotron-3
stage: post-training
summary_role: current-open-frontier-system
priority_for_post_training: S
confidence: medium
---
```

## Verdict

Nemotron 3 展示了大公司级 open frontier system 的后训练形态：Super 用 multi-environment RLVR、SWE-RL、RLHF 和 MTP healing，Ultra 进一步使用 specialized teachers、MOPD warmup、reasoning-control 与更大规模 rollout infrastructure。[Super:18-30] [Ultra:15-33]

## Pipeline

### Super

```text
SFT
-> multi-environment RLVR
-> SWE / agentic RL
-> RLHF
-> MTP healing / deployment preparation
```

### Ultra Delta

```text
specialist teachers
-> MOPD warmup / consolidation
-> multi-domain RL and reasoning control
-> scaled asynchronous rollout
-> quantization-aware release path
```

## Core Mechanisms

- Multi-environment RL 把 math/code/reasoning/tool/SWE tasks 放入不同可验证环境，而不是依赖单一 scalar reward。[Super:18-30]
- Ultra 用 MOPD 聚合 specialists，说明 NVIDIA 当前路线也从“一个大 RL mixture”转向“specialize then consolidate”。[Ultra:15-33]
- MTP 不只是 pretraining auxiliary head；它用于 speculative decoding/rollout acceleration，并在 post-training 后进行 healing，避免主模型与 MTP heads 行为错位。
- Quantization、NVFP4/FP8 和 rollout throughput 是 recipe 的组成部分，因为它们决定同等预算下可生成多少 on-policy experience。[Super:33-37] [Ultra:41-47]

## Failure Modes / Controls

- 多环境 reward scales、episode lengths 与 verifier reliability 不一致，需要 domain-balanced sampling 和 regression gates。
- Specialist MOPD 可能继承 teacher blind spots；没有公开足够 teacher disagreement/routing ablation。
- MTP/quantization 优化可能影响 rollout/serving distribution，需在最终 deployment precision 下复测 agent tasks。

## Openness and Evidence

- 权重、部分数据与 recipe openness 很强，是 open frontier system 的重要参考；仍不是像 OLMo 3 那样完整开放每个 checkpoint/log/config。
- Super 与 Ultra 是同一 lineage 的两个报告，current practice 应优先 Ultra delta，Super 用于补完整流程。

## Transfer to Current Work

- 建立 environment-level dashboard：success、reward calibration、rollout length、verifier disagreement、GPU time/task。
- 将 distillation 与 rollout acceleration共同计入 cost：MOPD 的 teacher serving 额外成本可能抵消 sample-efficiency 收益。
- 最终 policy 应在 quantized/deployment stack 中做 regression，避免只验证 BF16 training checkpoint。

## Evidence Anchors

- [post-training.md](post-training.md) 或对应 stage note: Super pages 18-30, Ultra pages 15-33。
- [architecture-pretraining.md](architecture-pretraining.md): Hybrid Mamba-Attention、MTP、active parameters。
- [post-training.md](post-training.md): openness gaps and Super/Ultra post-training boundary。
- [../README.md](../README.md): source-level current-practice verdict。
