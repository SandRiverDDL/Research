# LongCat-2601 DORA / Agentic RL

```yaml
---
source_id: longcat-flash-thinking-2601
section_type: rl-training
stage: post-training
depth: working
confidence: high
need_expert_review: true
---
```

## Core Design / Innovation

- DORA 的核心是把 multi-turn agentic rollout 从 batch barrier 改成 fully streaming asynchronous pipeline，避免环境执行长尾拖死 accelerator。[9-10]
- Multi-version asynchronous training 允许不同模型版本生成的 trajectories 完成后立即入队，同时用 SampleQueue 控制 staleness。[9-10]
- 为 560B MoE 多轮长上下文 rollout，LongCat 引入 PD disaggregation 和 CPU KV-cache swapping，减少 prefill/decode 干扰和 KV 不足导致的 recomputation。[10-11]
- Multi-domain environment training 用 domain oversampling 和 pass-rate-based oversampling 系数，把动态预算分配近似成可异步调度的系统问题。[14]

## Why It Matters

Agentic RL 的工程难点不是 objective 一行公式，而是 rollout 的长尾、环境延迟、KV cache、staleness 和 domain balance。LongCat 这部分适合进入 infra / RL scaling lens。

## Mechanism Sketch

1. RolloutManager / SampleQueue / Trainer 分离，逻辑控制走 RPC，worker 执行 LLM generation、ENV execution、reward。
2. 单样本粒度 streaming，去掉 batch barrier。
3. 用 Lightweight-RolloutManager + 多个 RolloutController 管 virtual rollout groups。
4. Prefill 和 decode 部署在不同 device groups，并异步传输 chunked KV cache。
5. 训练阶段按 domain 和历史 pass rate 调 oversampling，既保证难任务样本量，又尽量不破坏异步吞吐。

## Details / Evidence

- TR 披露 DORA 支持 up to 32,000 environments，约 400 physical machines，数千 accelerators。[10]
- DORA 在不同 production jobs 中比 synchronous training 快 2-4x，但为控制 staleness 牺牲了一部分 request load ratio。[11]
- Training objective 采用 GSPO，理由是 MoE 和 long-horizon agentic trajectories 上 sequence-level optimization 更稳定。[11]
- Multi-domain training 中，低成功率任务获得更高 oversampling coefficient，每组独立算 advantage，近似 dynamic budget allocation。[14]

## Gaps / Open Questions

- GSPO 的具体 objective、advantage estimator、staleness correction 需要更细读原文或相关 LongCat/DORA source。
- DORA 是否完整开源、能否迁移到 verl/slime 生态未确认。

## Lookup-only

- Request load ratio、requests per device、环境/机器数量、训练曲线数字作为 lookup。[10-15]

## Evidence Anchors

- 9-11: DORA system and PD disaggregation.
- 11-14: RL strategy.
- 14-15: multi-domain environment training.

