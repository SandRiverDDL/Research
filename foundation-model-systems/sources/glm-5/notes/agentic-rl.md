# GLM-5 Agentic RL / slime

```yaml
---
source_id: glm-5
section_type: stage-note
stage: rl-training
depth: working
confidence: high
need_expert_review: true
---
```

## Core Design / Innovation

- GLM-5 的后训练核心是多阶段 RL：Reasoning RL、Agentic RL、General RL，最后用 On-Policy Cross-Stage Distillation 恢复/融合前面阶段能力。[10-14]
- Agentic RL 的核心创新更偏系统：把 training engine、inference engine、rollout services、reward/env logic 解耦，用 fully asynchronous rollout 提高长轨迹训练吞吐。[12-17]
- slime 的价值是把 rollout 变成 server-based、customizable、fault-tolerant 的统一后训练 infra，而不是只服务某个 RL loss。[14-15]
- 稳定性靠组合约束：DSA deterministic top-k、freeze indexer、TITO、direct double-sided IS、stale sample filtering、environment-failure filtering、DP-aware routing。[12, 16-17]

## Why It Matters

如果做 coding/search/terminal agent，瓶颈往往不是“有没有 PPO/GRPO”，而是 rollout 长短极不均、环境会失败、tokenization 会错位、policy lag 会出现、KV cache 会浪费。GLM-5 把这些工程问题当成 RL recipe 的主体，这是它比普通 post-training 描述更有学习价值的地方。

## Mechanism Sketch

1. SFT 先覆盖 general chat、reasoning、coding/agent 数据，形成可 RL 的初始策略。
2. Reasoning RL 混合 math、science、code、TIR 四个 domain，用 domain/source-specific judge 或 evaluation system 给 binary outcome reward。
3. Agentic RL 中，rollout engine 持续产生轨迹；达到阈值后送 trainer 更新；inference weights 周期同步。
4. TITO Gateway 保留 rollout 生成的 exact token IDs 和 metadata，避免 text round-trip retokenization 破坏 action/reward 对齐。
5. Direct double-sided IS 用 rollout log-prob 当 behavior proxy，对过度偏离的 token 直接 mask gradient。
6. 最后用 cross-stage distillation，从各阶段 teacher checkpoints 拉 logits，减少 sequential RL 的遗忘。

## Details / Evidence

- Reasoning RL 四域大致 balanced：math、science、code、tool-integrated reasoning；样本难度筛选要求 GLM-4.7 难以解但 stronger teacher 可解。[12]
- Agentic RL 支持 SWE、terminal、high-difficulty multi-hop search，构建超过 10K real-world SWE/terminal-style verifiable scenarios。[13, 17-19]
- Direct double-sided IS 使用 `r_t = exp(log pi_theta - log pi_rollout)`，在 `[1-eps_l, 1+eps_h]` 外直接将 token loss 权重置 0；这和标准 PPO clip 不同，后者通常仍在 clipped surrogate 中保留梯度路径。[16-17]
- Stale sample 通过 rollout weight version 与 current policy version 的差距过滤；环境崩溃样本被排除，GRPO group 不完整时根据有效样本比例 pad 或 drop。[17]
- DP-aware routing 让同一 rollout 固定到同一 DP rank，保留 multi-turn prefix KV cache，降低长上下文反复 prefill。[17]

## Gaps / Open Questions

- 异步 RL 的 policy lag 阈值、optimizer reset 频率、task ratio 调度策略和 reward 细节没有完整 ablation。
- On-Policy Cross-Stage Distillation 名字接近 OPD，但这里披露的是 teacher logits / advantage replacement 形式；和 DeepSeek/MiMo/Nemotron 的 MOPD/OPD 需要单独比较，不能直接等同。
- Agentic search judge 使用 proprietary judge；eval 可复现性和 benchmark comparability 需要谨慎。

## Lookup-only

- β、eps_low、eps_high、group size、batch size 等具体超参回查 `[12-14, 16-17]`。
- slime 的 FP8 rollout、MTP、PD disaggregation、heartbeat fault tolerance 细节回查 `[14-15]`。

## Evidence Anchors

- 10-14: post-training pipeline and cross-stage distillation.
- 12-17: asynchronous RL, TITO, direct double-sided IS, stale/noisy sample filtering.
- 17-19: SWE / terminal / search environment scaling.
