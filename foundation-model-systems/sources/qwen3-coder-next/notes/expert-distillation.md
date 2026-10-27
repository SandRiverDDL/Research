# Qwen3-Coder-Next Expert Distillation

```yaml
---
source_id: qwen3-coder-next
section_type: sft-distillation
stage: post-training
substage: expert-distillation
depth: working
confidence: medium
need_expert_review: false
---
```

## Core Design / Innovation

- Post-training 从高质量 agentic coding SFT checkpoint 出发，训练多个 expert models，再把能力 distill 回统一模型。[2, 6-11]
- Experts 覆盖 web development、user experience focused coding、single-turn QA、software engineering 等 domain；这是 specialist-to-generalist consolidation 的 coding-agent 版本。[6-11]
- 和 MiMo/Nemotron 的 MOPD 相比，Qwen 披露更偏工程流程和 expert domains，公式/OPD objective 披露较少。[11]

## Why It Matters

这条线说明 2026 coding-agent model 也在走 specialist consolidation：不是一个模型直接吃所有任务，而是先把 WebDev、UX、SWE、QA 等专家训练出来，再压回 unified model。后续值得和 MiMo MOPD / Cascade MOPD / GLM parallel OPD 做横向 lens。

## Method Blocks

### Expert distillation

- 官方披露：多个 expert models 被训练并 distill 回 unified model。[6-11]
- 合理解释：这是 coding-agent 领域的 multi-teacher consolidation，但不一定是 MiMo 式 token-level MOPD。
- 未披露 / 不能下结论：exact loss、teacher weighting、student sampling policy、filtering 和是否 on-policy 尚需深读或查 repo。

## Code Expert Recipe 补核（2026-10-19）

- **解释（用户追问后的术语澄清）**：四类 expert 是按 task/workflow、交互形态、优化目标与验证方式混合划分的训练分支，并非互斥的基础能力 taxonomy。WebDev 是应用场景，UX 是跨 CLI/IDE 的使用质量与 tool-format 目标，Single-turn QA 是交互/反馈形态，SWE 是 repository-level 多步开发工作流；任务之间可以重叠。这里的 expert 是独立 checkpoint/policy，不是 MoE 内部 FFN expert。[6-11]
- **事实**：四类 experts 共享初始模型，但 data、recipe 和 eval 不同；不能把全部 experts 概括为同一种 RL。[6-11]
- **事实**：WebDev expert 用浏览器渲染 + VLM 静态截图检查 + 自动交互验证过滤 trajectories；UX expert 强调跨 CLI/IDE scaffold 的 tool-call format 验证与 data-mixture ablation。[6-9]
- **事实**：Single-turn QA expert 用 execution-based RL，任务包括竞赛题、library/API usage、多语言和 secure coding；合成 tests 通过多份独立 solutions 的 majority consensus 选择。[9-10]
- **事实**：SWE expert 在真实/合成 repository environments 做多轮 RL；SFT/RL prompts disjoint，按 pass rate 筛选，最终 completion reward 外加 unfinished-trajectory 与 malformed-tool-call penalties。运行时 blocker 拦截恢复 GitHub history / reference patches 的行为。[10-11]
- **事实**：最终蒸馏回 SFT model；TR 没有给出足以判定其为 token-logit MOPD 的 objective。[11]
- **原文入口**：https://arxiv.org/html/2603.00729#S4.SS2

## Gaps / Open Questions

- Distillation objective 不够明确。
- 各 expert 的机制已补核；exact training configs、mixture weights、filter thresholds 与独立 ablations 仍不足。
- 需要确认是否有公开训练数据或只开放 weights/repo。

## Evidence Anchors

- 2: high-level expert model consolidation。
- 6-11: expert models and distillation。
