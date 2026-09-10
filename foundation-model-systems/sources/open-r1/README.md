# Open-R1 Source Dossier

```yaml
---
source_id: open-r1
source_type: open-project
org: Hugging Face
release_date: 2025-01-28
priority: A
status: section-notes
openness: fully-open
confidence: high
lineage: deepseek-r1-reproduction
role: major-release
base_source: deepseek-r1
---
```

## 一句话

Open-R1 是把 DeepSeek-R1 缺失的 code/data/eval pieces 做成可执行公共工程的开放项目：它提供 SFT、GRPO、synthetic-data generation、verifiable reward、code sandbox、evaluation recipes，并已完成 R1-Distill 复现，但“完整复现 R1-Zero 多阶段训练”仍是进行中的目标。[repo, blog-launch]

## 为什么重要

- 它不是一份新的 frontier model TR，而是实践入口：适合查命令、数据、配置、sandbox 和训练框架。
- 项目公开 Mixture-of-Thoughts、OpenR1-Math、CodeForces-CoTs 等数据与对应训练 recipe，可用于小中规模 recipe 验证。[repo]
- 与 Open-Reasoner-Zero 的区别：Open-R1 更广、更工程化；ORZ 对 pure-RL/PPO 机制给出更集中、完整的论文证据。

## 核心机制 / Takeaways

- 三步 roadmap：复现 R1-Distill -> 复现 R1-Zero pure RL -> base-to-SFT-to-RL multi-stage pipeline。[blog-launch, repo]
- 当前稳定产物包括 R1 trace distillation、SFT、GRPO、数据生成和统一评测；roadmap 不等于每一步都已完成。[repo]
- GRPO training 基于 TRL/vLLM，可在多节点上分离 rollout server 与 trainer。[repo]
- Code reward 通过 E2B、Morph 或 Piston 等 sandbox 执行测试；数据可按 mixture config 组合。[repo]

## Source Bundle

- launch blog: https://huggingface.co/blog/open-r1
- repository: https://github.com/huggingface/open-r1
- organization: https://huggingface.co/open-r1
- last checked: 2026-07-21

## Lineage / Delta

- lineage：DeepSeek-R1 community reproduction。
- role：living open project，不是 frozen technical report。
- 已完成 anchor：distilled-model/data recipe。
- 仍变化的 anchor：pure-RL 与完整 multi-stage R1 reproduction 状态以 repository release 为准。

## 最大证据缺口

- 缺少单一冻结 TR；repo 主分支会变化，任何 recipe 结论都要记录版本/日期。
- “fully open reproduction”是项目目标与 artifact policy，不代表 DeepSeek 原始 run 已被逐项复现。
- 不同 recipe 使用不同 base、data 和 compute，不能合成一个虚构的 Open-R1 model training flow。

## Lens Hooks

- open-recipe：可直接使用的 SFT / GRPO / data-generation 入口。
- data: verified reasoning traces and code datasets.
- infra: TRL, vLLM, DeepSpeed and code sandboxes.
- eval：可复现地评测 R1-family checkpoint。

## 阅读入口

- `section-index.md`: 按 repo/blog artifact 路由。
- `notes/sft-distillation.md`: distilled-data recipe。
- `notes/rl-training.md`: GRPO 与 code reward 工程入口。
- `notes/claims-and-gaps.md`: roadmap 与已完成 artifacts 的边界。
