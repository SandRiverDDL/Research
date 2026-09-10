# MiMo-V2-Flash Post-training / RL

```yaml
---
source_id: mimo-v2-flash
section_type: rl-training
stage: post-training
substage: sft-domain-rl-agentic-rl
depth: working
confidence: medium
need_expert_review: false
---
```

本 note 覆盖 SFT、domain-specialized RL 和 agentic RL environment。MOPD 机制单独写在 `mopd.md`。

## Core Design / Innovation

- Post-training 主线是先 specialist 再 consolidation：SFT 激活通用指令能力，domain-specific RL 训练多个 expert teachers，再由 MOPD 合并。[11-15]
- SFT 里一个有意思的稳定性指标是 MoE `num-zeros`：零梯度参数数量上升说明 expert load balance 变差，下降则可能过拟合；他们用它调 expert bias update rate 和 AdamW epsilon。[15]
- Non-agentic RL 覆盖 math、coding、logic、helpfulness/safety，reward 来源包括 programmatic tools、verifiers 和 reward models。[15]
- Agentic RL 比较具体：code agent、terminal agent、search agent、general agent 都有任务规模/环境设计，并强调真实环境、Docker/Kubernetes 和 minimal tools。[16-17]
- Code agent 的关键设计是用真实 GitHub issues + containerized environments + `bash` / `str_replace` / `finish` 三个原子工具，让模型在训练中自己学 workflow，而不是靠复杂 scaffold。[16]

## Why It Matters

MiMo 的 RL 部分值得学的是“specialist teacher 怎么来”。MOPD 本身是合并机制，但如果前面的 domain teachers 质量不够，MOPD 只是合并弱信号。TR 对 agentic RL environment 的披露比很多模型报告更实，尤其是任务来源、环境构建、并发 Kubernetes pods、工具设计和 scaling curves。

## Mechanism Sketch

1. SFT：用多域高质量 instruction-response pairs，让模型支持 thinking / non-thinking modes 和基础 agent tasks。
2. SFT 稳定性：监控 MoE `num-zeros`，用 expert bias update rate、AdamW epsilon、sequence aux loss 控制 expert balance 和过拟合。
3. Non-agentic RL：对单轮 verifiable tasks 使用 programmatic tools/verifiers/reward models。
4. Agentic RL：构建 code / terminal / search / general agent environments，模型多步交互并接受环境 reward。
5. 输出：多个 domain-specialized teachers 进入 MOPD，作为 token-level dense supervision 来源。

## Details / Evidence

### SFT stability

- SFT 数据包含 general conversation、reasoning、coding、agent tasks，覆盖 thinking 和 non-thinking modes，由内部 domain-specialized checkpoints 生成 response。[15]
- `num-zeros` 是 MoE SFT 的 stability metric：上升对应 load balance deterioration，下降对应 overfitting signal。[15]
- 关键超参包括 expert bias update rate、AdamW epsilon、sequence auxiliary loss coefficient。[15]

### Non-agentic RL

- Non-agentic RL 面向 single-turn tasks，目标是 verifiable domains 的 reasoning accuracy，以及 open-ended conversation 的 helpfulness/safety alignment。[15]
- 对 verifiable domains 使用 programmatic tools 和 verification signals；open-ended domains 依赖 reward models。[15-16]

### Agentic RL

- Table 8 披露 agentic training task composition：code agent 90K real/real、code agent 30K real/synthesized、search agent 150K real/synthesized、general agent 50K synthesized/synthesized。[16]
- Code agent 来自真实 GitHub issues，模型在 loop 中读写文件、执行命令，并基于 unit tests 得到 reward。[16]
- 环境构建 pipeline 从 repository snapshots 生成 containerized images，跨 8 种语言成功率约 70%，由 10,000+ concurrent pods 的 Kubernetes cluster 支撑。[16]
- 工具设计刻意 minimal：`bash`、`str_replace`、`finish`，不预设复杂 workflow，让模型在训练中发现策略。[16]
- Terminal agent 来自 Stack Overflow / Stack Exchange，转为 Dockerfile + test cases 的 computational tasks，并按 pass rate 过滤可靠性和难度。[16]

## Gaps / Open Questions

- Reward model / verifier implementation 没有完整公开。
- SFT 数据和 domain-specialized checkpoint 来源不透明。
- Agentic RL 的 rollout algorithm、KL/entropy/stability control、sampling temperature、pass-rate filter 阈值没有完整披露。
- Code agent scaling curves 能说明任务规模有效，但没有揭示环境质量、leakage、test robustness。

## Lookup-only

- SFT hyperparameters: LR decay 5e-5 to 5e-6, batch size 128, AdamW epsilon 1e-8, expert bias update 1e-4, sequence auxiliary loss 1e-6。[15]
- Agentic task counts in Table 8。[16]
- Code environment setup success rate: 70% across 8 languages; Kubernetes scale: 10,000+ concurrent pods。[16]

## Evidence Anchors

- 11-15: SFT and post-training overview。
- 15-17: non-agentic and agentic RL。
- 16: Table 8 and code agent environment details。
