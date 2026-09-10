# DeepSeek-V4 Source Dossier

```yaml
---
source_id: deepseek-v4
source_type: model-tr
org: DeepSeek AI
release_date: 2026-04-24
priority: S
status: section-notes
openness: open-weights
confidence: medium
---
```

## 一句话

DeepSeek-V4 是当前项目中最完整的 frontier-industrial anchor 之一：它用 hybrid CSA/HCA 和 1M context 改变长轨迹成本，再以 domain-specialist GRPO、multi-teacher full-vocabulary OPD、GRM signals 和可 replay sandbox 组成一套面向 reasoning / agentic work 的后训练系统。[6-14, 28-36]

## 为什么重要

- 事实：V4-Pro 是 1.6T total / 49B active，V4-Flash 是 284B total / 13B active；两者都以 long-context efficiency 和 agentic workloads 为主要定位。[1, 9-14]
- 对后训练最重要的变化是把上一代 mixed RL consolidation 替换为 OPD：十多个 domain experts 在 student-generated trajectories 上提供 full-vocabulary distributions，再用 reverse-KL-style objective 合并到统一 policy。[28, 32-35]
- agentic recipe 同时依赖 reasoning-mode-specific RL、rubric/GRM signals、tool schema、跨 turn reasoning retention、token-granular WAL、shared-memory dispatch 和 deterministic replay sandbox。[29-36]
- 它的公式级 recipe 仍不 fully reproducible，但适合建立“architecture economics -> rollout infra -> specialist training -> consolidation”一体化 intuition。

## 核心机制 / Takeaways

- Hybrid CSA/HCA：压缩长历史的 KV 表示并保留 sliding-window local branch，使 1M context 的 inference / rollout 成本可控。[9-14]
- Specialist GRPO：按 domain prompt 与 reward 分开训练 experts，而不是用一个 mixed RL 直接兼顾所有能力。[28]
- Multi-teacher OPD：student 自采 trajectories，teachers 提供 full-vocabulary logits，以 policy-level distribution matching 合并能力。[32-35]
- Reasoning effort modes：Non-think / Think High / Think Max 使用不同 length/context incentives，属于训练出的 product modes，不只是 prompt label。[29-31]
- Agent system：DSML tool schema、retained tool reasoning、preemption-safe rollout、trajectory provenance 和 deterministic replay 都是训练系统的一部分。[30-36]

## Source Bundle

- technical report: see `source-bundle.md`
- model card: see `source-bundle.md`
- announcement / blog: see `source-bundle.md`
- code / repo:
- weights: see `source-bundle.md`
- external eval: see `source-bundle.md`
- local pdf:
  - `/Users/chy/Research/foundation-model-systems/papers/deepseek-v4/deepseek-v4-tech-report.pdf`
  - `/Users/chy/Research/foundation-model-systems/papers/deepseek-v4/deepseek-v4-model-card.pdf`
- last checked: 2026-06-16

## 最大证据缺口

- expert domains、teacher routing/weights、GRM procedure 和 tool/agent training data composition 未公开。
- Full-vocabulary OPD 有较多 system detail，但缺少公开 code/config 和完整 compute/ablation accounting。
- 1M context 与内部 agentic eval 仍需要 independent replication；不能从 context-window number 推断所有长任务已解决。

## Lens Hooks

- architecture: MoE, long-context, attention/efficiency route.
- data-pipeline:
- training-recipe:
- rl-training:
- eval: coding, reasoning, long-context, agentic benchmarks.
- infra: long-context serving / domestic hardware / cost claims if supported by primary source.

## 阅读入口

- `section-index.md` first.
- `source-bundle.md` first.
- `notes/architecture.md` for model-system structure.
- `notes/consolidation.md` for OPD / specialist consolidation.
- `notes/reward-verifier.md` for GRM and hard-to-verify reward signals.
- `notes/tool-agent-training.md` for tool schema, retained reasoning traces, and sandbox infrastructure.
- `notes/eval.md` for claim audit.
- `notes/claims-and-gaps.md` before comparison.
