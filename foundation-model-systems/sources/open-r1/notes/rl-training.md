# Open-R1 RL Training

```yaml
---
source_id: open-r1
section_type: rl-training
stage: post-training
substage: rl-training
depth: working
confidence: medium
need_expert_review: false
---
```

## Core Design / Innovation

- Open-R1 提供的是 reusable GRPO scripts，而不是单一的新算法 claim。[repo]
- TRL 的 vLLM backend 支持小规模 colocated run，也支持把 rollout 与 trainer 分到不同节点。[repo]
- Verifiable code reward 通过 external/local sandbox 执行程序；pass-rate filtering 保留有有效学习信号的任务。[repo]
- Dataset-mixture config 把 domain composition 显式暴露为实验变量。[repo]

## Why It Matters

它的价值是 operational：降低验证 data、reward 和 base-model hypothesis 的成本。默认 config 应被当作 runnable baseline，而不是 SOTA 证据。

## Mechanism Sketch

1. 选择 base/instruct checkpoint 与 chat template。
2. 根据 rollout pass rate 过滤 verifiable prompts。
3. 通过 vLLM 生成 response groups。
4. 计算 math/code reward，必要时调用 sandbox。
5. 使用 TRL/DeepSpeed 做 GRPO update。
6. 用项目自身 eval harness 验证，并记录 pinned config。[repo]

## Details / Evidence

- Code contest 可通过 E2B、Morph 或 Piston-style workers 执行。[repo]
- Multi-node recipe 可以用一个节点跑 vLLM、N 个节点训练，rollout topology 是显式配置。[repo]
- 项目支持 SFT 和 GRPO，但 roadmap 中的完整 multi-stage R1 reproduction 不能在没有 dated artifact 时标为完成。[blog-launch, repo]

## Gaps / Open Questions

- Pure-RL 规模和最终 checkpoint 会随 repository history 变化。
- 默认 reward/filter 主要覆盖 verifiable reasoning/code，不覆盖 general assistant RL。
- 没有冻结的 paper-level ablation 证明哪些 framework choices 是必要条件。

## Lookup-only

- Launch commands、GPU topology 与 reward providers：`[repo]`。

## Evidence Anchors

- `[repo]`：GRPO、filtering、code interpreter 与 Slurm sections。
- `[blog-launch]`：只用于 roadmap。
