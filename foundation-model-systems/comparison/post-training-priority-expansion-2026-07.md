# Post-training Priority Expansion — 2026-07

```yaml
---
comparison_id: post-training-priority-expansion-2026-07
sources:
  - deepseek-r1
  - ling-ring-2.6
  - open-reasoner-zero
  - open-r1
  - skywork-or1
  - qwen3.5
  - minimax-m2-series
  - kimi-k2.6
  - olmo-3
status: reviewed
confidence: high
---
```

## Question

本轮第一、第二优先级 sources 应如何进入现有 post-training landscape：哪些是独立 method anchor，哪些只是 release delta，哪些能作为 reproducible baseline？

## Executive Takeaway

本轮新增的五个 source 并不属于同一层级：

- **DeepSeek-R1** 是 reasoning RL 的 lineage-reference；已有旧 L1 卡，本轮升级成可回原文的 dossier。
- **Ling/Ring 2.6** 是最新 current-practice TR，重点在 token-efficient alignment、agent environments、KPop 与 asynchronous RL system。
- **Open-Reasoner-Zero** 是 fully-open pure-RL/PPO baseline，用来检验 critic、GAE、KL 和 data-scale claims。
- **Open-R1** 是 living open project，最适合查 runnable SFT/GRPO/data-generation recipe，不能写成冻结的单一模型流程。
- **Skywork-OR1** 是 post-distillation long-CoT RL source，核心是 MAGIC、entropy collapse、data/verifier audit 与 rollout resource allocation。

第二优先级四条 lineage 则不应升级成新 dossier：Qwen3.6/3.7、MiniMax M3、Kimi K2.7 Code、Olmo 3.1 都以 release delta 记录。它们更新 current-practice，但公开程度不足时不能覆盖旧 full TR 的 recipe 事实。

## Source Matrix

| Source | 正确角色 | 最重要的 post-training 价值 | 证据 / 开放度 | 结论 |
|---|---|---|---|---|
| [DeepSeek-R1](../sources/deepseek-r1/README.md) | lineage-reference model TR | R1-Zero pure RL；cold-start -> reasoning RL -> rejection SFT -> general RL；distillation | open weights，data/code 不完整 | **S-classic**：必须保留，但 current DeepSeek practice 看 V4 |
| [Ling/Ring 2.6](../sources/ling-ring-2.6/README.md) | current-practice model TR | Ling token efficiency；Ring agent RL；KPop；partial rollout 与 bounded staleness | 全系列 checkpoints；非 fully reproducible | **S-current**：本轮最新、信息密度最高的 agentic source |
| [Open-Reasoner-Zero](../sources/open-reasoner-zero/README.md) | fully-open reasoning-RL recipe | vanilla PPO + critic、`γ=λ=1`、no KL、minimal reward、data scale | code/data/policy/critic 全开 | **S-open**：复杂新算法必须对比的 baseline |
| [Open-R1](../sources/open-r1/README.md) | living open project | Verified trace SFT、GRPO、data generation、code sandbox、eval harness | 工程 artifacts 高开放；无冻结 TR | **A-open**：实践入口，不做强 method causality claim |
| [Skywork-OR1](../sources/skywork-or1/README.md) | post-distillation RL recipe | MAGIC、entropy floor、on-policy freshness、verifier audit | code/data/weights + detailed TR | **A+/open**：稳定性与数据/验证器实验价值高 |
| [Qwen3.5 lineage](../sources/qwen3.5/README.md) | current model tracking | million-agent environments 与 async RL 只有高层披露；3.6 coding delta；3.7 API metadata | open weights 到 API-only 混合 | **S-capability / low-recipe**：重要但不能补写 recipe |
| [MiniMax M3 delta](../sources/minimax-m2-series/notes/release-minimax-m3.md) | current-practice delta | native multimodal、1M context、MSA、reasoning modes | weights + MSA paper；无完整 M3 post-training TR | M2 仍是 recipe anchor，M3 只更新系统边界 |
| [Kimi K2.7 Code delta](../sources/kimi-k2.6/notes/release-kimi-k2.7-code.md) | coding-agent release delta | 4K+ tool-call horizon、thinking-token efficiency、multimodal tools | announcement + weights；无 full TR | K2.5 仍是 method anchor |
| [Olmo 3.1 delta](../sources/olmo-3/notes/release-olmo-3.1.md) | fully-open continuation delta | Think 32B 延长 RL；Instruct recipe 扩到 32B；refreshed RL-Zero | fully-open lineage + official continuation details | 最适合研究 RL schedule headroom |

## Cross-source Judgment

### R1-Zero 命题现在有三种互补证据

1. DeepSeek-R1：frontier-scale 原始命题，但 recipe 不完全开放。
2. Open-Reasoner-Zero：从 base 直接 PPO，重点检验 critic、GAE 和 no-KL。
3. Open-R1：提供可执行的社区工程入口，但 full multi-stage roadmap 不能当作已全部完成。

因此后续讨论“pure RL 是否足够”时，不能只引用 DeepSeek-R1；至少应同时检查 ORZ 的 critic evidence 与 Open-R1 的 artifact status。

### ORZ 与 Skywork-OR1 不应合并成一种 open recipe

- ORZ 从 base model 直接 RL，研究 capability emergence 与 critic-based PPO。
- Skywork 从 R1-Distill checkpoint 开始，研究已有 long-CoT policy 的继续强化、entropy collapse 与 data/verifier quality。

它们分别是 base-RL baseline 与 post-distillation RL baseline。

### 最新 release 必须更新 current-practice，但不自动升级 recipe confidence

- Qwen3.7、MiniMax M3、Kimi K2.7 Code 的能力与产品形态很新。
- 但它们没有与旧 anchor 同等级的 training disclosure。
- Olmo 3.1 是例外：同一 fully-open flow 中明确公开 continuation schedule，因此可以形成更强的 training delta。

## What Changes in the Main Landscape

- “经典 reasoning RL”新增 DeepSeek-R1，而不是继续让 Qwen3 代替该历史角色。
- “fully-open auditability”从只有 OLMo 3 扩为两种用途：OLMo 3 负责完整 model flow，ORZ 负责 focused pure-RL reproduction。
- “agentic environment / rollout systems”新增 Ling/Ring 2.6 的 KPop、ARouter、partial rollout 与 bounded staleness。
- “RL stability”新增 Skywork 的 entropy-collapse 与 rollout-freshness 证据。
- “open practical recipe”新增 Open-R1，但其 roadmap 与 completed milestone 必须分开。

## Evidence Used

- DeepSeek-R1 TR pages 2-10、60-63。
- Ling/Ring 2.6 TR pages 13-19、28-31、33。
- Open-Reasoner-Zero TR pages 3-12、17-21 与公开 repository。
- Open-R1 官方 repository、launch blog 与 HF artifacts。
- Skywork-OR1 TR pages 7-37 与公开 repository/data。
- Qwen、MiniMax、Kimi、Olmo 的官方 model cards、release blogs 或 API metadata；未用二手材料补 training facts。

## Limits

- 截止日期：2026-07-21。
- 本轮没有把 release leaderboard 改写成模型能力总排名。
- Open-R1 是 living repository，后续使用时必须 pin commit。
- Ling/Ring、Qwen3.5、MiniMax M3、Kimi K2.7 Code 的关键数据和训练配置仍未完全公开。
