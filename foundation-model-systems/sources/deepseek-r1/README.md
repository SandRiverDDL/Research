# DeepSeek-R1 Source Dossier

```yaml
---
source_id: deepseek-r1
source_type: model-tr
org: DeepSeek-AI
release_date: 2025-01-20
priority: S
status: section-notes
openness: open-weights
confidence: high
lineage: deepseek
role: full-tr
base_source: deepseek-v3-base
---
```

## 一句话

DeepSeek-R1 是 reasoning post-training 的关键 lineage anchor：R1-Zero 展示从 base model 直接用 GRPO 与可验证奖励获得长 CoT，R1 再用 cold-start SFT、reasoning RL、rejection-sampling SFT 和 general RL 修复可读性、通用能力与安全行为。[2-8]

## 为什么重要

- 它把“pure RL 能否从 base 激励 reasoning”与“怎样把 reasoning model 做成可用 assistant”拆成 R1-Zero 和 R1 两条证据链。
- 它不是当前 DeepSeek practice 的替代品；DeepSeek-V4 是 current-practice，R1 是解释后续 reasoning RL、distillation 和 reward design 的 lineage-reference。
- 旧 OPD L1 卡已经覆盖核心流程，本 dossier 复用并校准它，而不是重新写泛化 summary。

## 核心机制 / Takeaways

- R1-Zero 从 DeepSeek-V3-Base 直接做 GRPO，不经过 SFT；reward 只含 accuracy 与 format，避免 neural RM 在大规模 reasoning RL 中被 hack。[2-4]
- RL 同时推高正确率与 response length，并出现 reflection、alternative exploration 等行为；这证明的是 outcome incentive 下的行为演化，不等于“模型获得了人类式推理”。[4-5]
- R1 用四阶段修复 pure-RL failure：cold-start long-CoT SFT -> reasoning RL -> reasoning/general rejection-sampling SFT -> all-scenario RL。[6-8]
- reasoning tasks 使用 rule verifier；general helpfulness/safety 使用 model-based reward。两类 reward 被有意分开，避免 neural RM 污染可验证 reasoning signal。[3-7]
- Distill models 主要来自 R1 生成的约 800K 样本做 SFT；报告发现，对小模型直接做这一路径的 RL 不如从大模型 trace distillation。[60-62]

## Source Bundle

- technical report: https://arxiv.org/abs/2501.12948
- model release: https://huggingface.co/deepseek-ai/DeepSeek-R1
- repository: https://github.com/deepseek-ai/DeepSeek-R1
- local PDF: `/Users/chy/Research/foundation-model-systems/papers/deepseek-r1/deepseek-r1.pdf`
- 复用的 L1 card：`/Users/chy/Research/opd/_meta/off-scope/25_deepseek-r1.md`
- last checked: 2026-07-21

## Lineage / Delta

- lineage：DeepSeek-V3-Base -> R1-Zero / R1 -> 后续 DeepSeek reasoning systems。
- role：lineage-reference，不代表 current-practice。
- 不可直接继承：不能默认 DeepSeek-V4 仍使用 R1 的 GRPO、reward mix、data mix 和 infra。

## 最大证据缺口

- 已开放 weights，但完整训练数据、训练代码、verifier 实现与集群运行细节没有公开。
- “aha moment”是行为样例，不是机制因果证据；不能据此推出 RL 创造了全新的 reasoning primitives。
- rejection-sampling 数据选择、污染控制与 general-data composition 披露不完整。

## Lens Hooks

- rl-training：pure RL 与 cold-start RL、GRPO、length growth。
- reward-verifier：rule reward 与 neural preference reward 的分工。
- sft-distillation：rejection sampling 与 teacher-trace distillation。
- eval：training-time AIME curve、pass@1 与 consistency、general capability repair。

## 阅读入口

- `section-index.md`: 主文和附录回读地图。
- `notes/rl-training.md`: R1-Zero 与 R1 的两段 RL。
- `notes/sft-distillation.md`: cold start、rejection sampling 与小模型蒸馏。
- `notes/reward-verifier.md`: reward 分层及其风险。
- `notes/claims-and-gaps.md`: 可复现性和 claim 边界。
