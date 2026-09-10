# Qwen3-Coder-Next Source Dossier

```yaml
---
source_id: qwen3-coder-next
source_type: model-tr
org: Qwen Team
release_date: 2026-03-03
priority: A
status: section-notes
openness: open-weights
confidence: high
lineage: qwen3-next
role: full-tr
base_source: qwen3-next
---
```

## 一句话

Qwen3-Coder-Next 是 2026 agentic coding recipe 的高价值 open-weight source：80B total / 3B active，围绕 executable coding tasks、agentic mid-training、domain expert post-training 和 expert distillation，探索小 active footprint 模型能否通过训练 recipe 接近大模型 coding-agent 能力。

## 为什么重要

它和 MiMo-V2-Flash 是同一条线：小 active 参数 + coding agent + executable environments + expert distillation。不同点是 Qwen 更聚焦 coding/webdev/UX/SWE experts，适合做 agentic coding source dossier，而不是泛 reasoning TR。

## 核心机制 / Takeaways

- 训练核心是 large-scale synthesis of verifiable coding tasks + executable environments，让模型能从环境反馈中学习，而不是只靠静态代码数据。[1-3]
- Mid-training 阶段引入 natural data、synthetic data、multi-turn agentic coding、instruction-following data 和 FIM code completion。[3-6]
- Post-training 从 SFT checkpoint 出发，训练多个 experts：web development、UX-focused coding、single-turn QA、software engineering，再 distill 回 unified model。[6-11]
- 80B total / 3B active 的小 active footprint 是核心定位：不是最大模型，而是 efficient local/agentic coding model。[1]
- Infra 部分披露了大规模 RL/agentic training 的启动和调度瓶颈，例如 Slurm RPC、Ray actors/GCS startup 问题。[13]

## Source Bundle

- technical report: https://arxiv.org/abs/2603.00729
- model card: https://huggingface.co/Qwen/Qwen3-Coder-Next
- blog: https://qwen.ai/blog?id=qwen3-coder-next
- repo: https://github.com/QwenLM/Qwen3-Coder
- local pdf: `/Users/chy/Research/foundation-model-systems/papers/qwen3-coder-next/qwen3-coder-next.pdf`
- last checked: 2026-06-23

## Lineage / Delta

- lineage: Qwen3-Next / Qwen3-Coder
- role: full TR for coder-next release
- base source: Qwen3-Next
- newly disclosed: agentic task synthesis, executable environments, coding experts, expert distillation, infra bottlenecks
- not safe to inherit: Qwen3.5 / Qwen3.6 release details

## Citation Labels

- default TR pages: `[1-13]`

## 最大证据缺口

- 数据和训练代码开放程度弱于 NVIDIA Cascade；很多 synthesis/filtering details 仍是 high-level。
- Expert distillation 的 exact objective、teacher weighting、filtering 和 OPD vs SFT distillation 边界需要深读。
- Eval setting 和 third-party comparability 需要单独审计。

## Lens Hooks

- agentic-training: executable environments, synthetic coding tasks, mid-training。
- opd/distillation: multi-expert distillation into unified model。
- infra: Slurm/Ray startup bottlenecks, large-scale agentic training。
- eval: SWE-Bench, Terminal-Bench, local coding agent benchmarks。

## 阅读入口

- `section-index.md`
- `notes/agentic-training.md`
- `notes/expert-distillation.md`
- `notes/eval.md`
