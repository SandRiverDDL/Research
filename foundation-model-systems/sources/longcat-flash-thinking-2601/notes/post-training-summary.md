# LongCat-Flash-Thinking-2601 Post-training Summary

```yaml
---
source_id: longcat-flash-thinking-2601
stage: post-training
summary_role: agentic-environment-anchor
priority_for_post_training: S
confidence: high
---
```

## Verdict

LongCat-Flash-Thinking-2601 是 agentic RL environment scaling 的主源：structured agentic midtraining 先建立 tool prior，随后用自动生成的 10K+/32K 级 environments、DORA async rollout、pass-rate budget allocation 和 instruction/tool noise curriculum训练 robust agent。[1-16]

## Pipeline

```text
general pretraining lineage
-> structured agentic midtraining trajectories
-> generated tools / DB schemas / dependency graphs
-> multi-domain asynchronous environment RL with DORA
-> pass-rate / domain-aware sampling
-> instruction-noise + tool-noise curriculum
-> Heavy Thinking at inference
```

- Environment 构建从 domain specification 生成 tools、database schema 与 dependency graph，再按保留 verifiability 的规则扩展任务。[5-6]
- Midtraining 与 RL 的分工明确：前者让 policy 能基本使用 tools，后者在 environment feedback 中探索和提高成功率。[1-3]

## Core Mechanisms

### DORA Async Rollout

- Producer-consumer、virtual rollout groups、streaming pipeline、multi-version models、prefill/decode disaggregation 与 CPU KV swapping共同解决长 agent rollout 吞吐。[9-11]
- Virtual groups 在异步环境中近似组织同 prompt/group samples，但 policy versions 与 completion times不完全一致，需要额外 off-policy control。

### Domain Budget Allocation

- Oversampling 与 pass-rate-based budget allocation 防止易域/高吞吐域主导训练；难度与可学习性决定 rollout budget，而不是静态 mixture。[14]

### Robust RL

- 显式注入 instruction noise 与 tool noise，并通过 curriculum逐步加难，缩小 perfect 与 imperfect environment performance gap。[15-16]
- 这是比“训练时所有工具永远正确”更接近真实 agent deployment 的假设。

## Failure Modes / Controls

- 自动环境可能存在 schema漏洞、不可解任务、reward leakage 与重复模板；verifiability-preserving generation仍需人工/程序 audit。
- 异步 multi-version rollout 带来 stale-policy bias；吞吐收益必须和 policy age/importance correction一起报告。
- Noise curriculum 太早/太强会压制探索，太弱则只学会 perfect-env shortcut。

## Openness and Evidence

- Open weights + full TR，environment/infra方向披露强；完整 environment corpus、generators 与所有 configs未必完全开放。
- 2601 是当前 full-TR anchor，旧 LongCat-Flash-Thinking 只作 lineage。

## Transfer to Current Work

- 先建 environment validator：solvability、determinism、reward integrity、tool dependency consistency、replayability。
- Sampling scheduler应使用 learning progress/pass-rate band，而不只按domain size。
- Robustness eval 分离 instruction corruption、tool failure、partial output、latency和state inconsistency。

## Evidence Anchors

- [environment-scaling.md](environment-scaling.md): agentic midtraining and environment generation pages 1-6。
- [rl-infra-dora.md](rl-infra-dora.md): DORA pages 9-11 and asynchronous RL。
- [robust-heavy-thinking.md](robust-heavy-thinking.md): robustness curriculum pages 15-16 and evaluation signals。
