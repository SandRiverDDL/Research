# Qwen3-Coder-Next Post-training Summary

```yaml
---
source_id: qwen3-coder-next
stage: post-training
summary_role: current-agentic-coding-reference
priority_for_post_training: A
confidence: high
---
```

## Verdict

Qwen3-Coder-Next 的研究价值是“小 active footprint 如何靠 data/environment/post-training 逼近大 coding agent”：80B total / 3B active，从可执行合成任务和 agentic midtraining 起步，再训练 web/UX/QA/SWE experts 并 distill 到 unified model。[1-13]

## Pipeline

```text
code-capable base
-> natural + synthetic code midtraining
-> multi-turn executable agentic coding data
-> general SFT checkpoint
-> domain RL / post-training experts
   (web, UX, single-turn QA, SWE)
-> expert distillation into unified coding agent
```

- Large-scale verifiable coding task synthesis 与 executable environments 是能力来源核心，不是普通 instruction dataset 的附属品。[1-6]
- FIM、repo/context data 与 multi-turn tool trajectories 在 midtraining 就进入，使 final RL 不必从静态 code completion model 硬拉出 agent behavior。

## Core Mechanisms

### Executable Data

- Tasks 绑定可运行 environment、tests 或 artifact checks，reward 来自执行反馈；这提高 correctness signal，但也引入 tests leakage 和 environment shortcut 风险。[1-6]
- 合成 task quality 应按可执行性、难度、修复范围和 hidden-test integrity 分层，而不是只按 teacher score 过滤。

### Domain Experts and Distillation

- Web development、UX、single-turn QA 与 SWE specialists 分别优化不同目标，再合并到一个小 active model。[6-11]
- 公开材料对 distillation target 与 teacher routing 细节有限；当前可以确认 specialize-then-pack 的系统哲学，不能确认与 OPD/MOPD 等价。

### Infra Constraint

- 报告记录 Slurm RPC、Ray actors/GCS startup 等大规模 agentic training 启动/调度瓶颈，说明大量短 environment workers 的 orchestration 成本不可忽略。[13]

## Failure Modes / Controls

- Test-only reward 容易过拟合 visible tests、篡改 tests 或生成不可维护 patch。
- 小 active model 容易在 specialist packing 时出现 capacity conflict，需要 domain regression 与 code-quality eval。
- Worker startup、sandbox provisioning 和 long-tail episodes 可能吞掉理论 MoE inference 优势。

## Openness and Evidence

- Open weights + TR；training data generation high-level 公开，但完整 synthesized corpus、environment configs、expert checkpoints 与 distillation code 不完全开放。

## Transfer to Current Work

- 把 environment validity、hidden tests、patch scope、maintainability 与 task success同时作为 eval gate。
- 对 expert consolidation 报告 per-domain retention，而非只看综合 coding score。
- 测量 end-to-end cost：model FLOPs、sandbox startup、tool execution、failed rollout 与 retries。

## Evidence Anchors

- [agentic-training.md](agentic-training.md): executable environments、midtraining 和 page 13 infra signals。
- [expert-distillation.md](expert-distillation.md): domain experts and consolidation。
- [../README.md](../README.md): source-level summary and gaps。
