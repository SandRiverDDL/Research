# DeepSeek-V4 OPD Consolidation

```yaml
---
source_id: deepseek-v4
section_type: consolidation
stage: post-training
substage: consolidation
depth: working
confidence: medium
need_expert_review: false
---
```

## Scope / Coverage

- 覆盖页段：TR pages 28-35。
- 覆盖阶段：specialist training -> multi-teacher OPD -> full-vocabulary OPD infrastructure。
- 子问题：
  - DeepSeek-V4 为什么把 V3.2 的 mixed RL stage 换成 OPD？
  - OPD 如何把多个 specialist teachers 合并到一个 student？
  - 它和 MAI 的 trace-SFT consolidation 有什么关键差异？
  - 哪些部分是可迁移 recipe，哪些主要是 infra-heavy implementation？

## Core Summary

- 事实：DeepSeek-V4 post-training pipeline 大体沿用 V3.2，但把 mixed RL stage 完全替换成 On-Policy Distillation (OPD)。[28]
- 事实：specialist models 仍按 V3.2 路线训练：initial fine-tuning 后，用 domain-specific prompts 和 reward signals 做 GRPO-style RL。[28]
- 事实：multi-teacher OPD 将十多个 domain expert teachers 合并到一个 student；目标是在 student-generated trajectories 上对齐 expert distributions，形式上是 reverse-KL-style distillation。[32-33]
- 解释：OPD 的关键不是普通 trace imitation，而是 student trajectory 上的 teacher distribution matching；这使 consolidation 更接近 policy-level aggregation。[32-34]
- 解释：full-vocabulary OPD 是 infra-heavy method，能否成立依赖 teacher scheduling、full-logit reconstruction、rollout persistence 和 memory management。[33-35]

## Stage Flow / Mechanism Map

1. 先训练多个 specialist teachers。每个 specialist 使用 domain-specific prompts 和 reward signals，训练方式是 GRPO-style RL。[28]
2. Student 自己生成 trajectories，而不是只被动模仿 teacher sampled traces。[32-33]
3. 多个 expert teachers 在 student trajectories 上提供 distributions，student 通过 reverse-KL-style objective 对齐这些 expert distributions。[32-33]
4. DeepSeek 使用 full-vocabulary logit distillation，因为报告认为 token-level KL estimates 方差高且不稳定。[33-34]
5. Post-training infra 为 OPD 提供 centralized teacher storage、on-demand teacher loading、hidden-state caching、on-the-fly full-logit reconstruction、token-granular WAL 和 shared-memory dispatch。[33-35]

## Reasoning Modes 与 Consolidation 的关系

- 事实：V4 支持 Non-think、Think High、Think Max 三种 reasoning modes。不同 mode 在 RL training 中使用不同 length penalties 和 context windows；Think Max 还注入特殊 system prompt。[29]
- 解释：reasoning effort 在 DeepSeek-V4 里更像训练出来的 product/runtime mode，而不是简单 inference-time temperature 或 prompt setting。[29-31]
- 开放问题：Think Max 的收益有多少来自 RL training，有多少来自 prompt/context budget，报告没有拆开量化。[29-31, 40]

## Full-vocabulary OPD 的工程含义

- 事实：DeepSeek 明确选择 full-vocabulary logit distillation，并配套 centralized teacher storage、on-demand teacher loading、hidden-state caching 和 on-the-fly full-logit reconstruction。[33-34]
- 解释：这里的主要壁垒可能不是公式，而是把 teacher logits、long rollouts 和 preemptible training 组织成稳定数据通路。[33-35]
- 解释：与 MAI 的 trace-SFT consolidation 相比，DeepSeek 的 OPD 更强调在 student 自身分布上对齐 teacher distributions；MAI 更像 specialist traces 的 SFT packing 后再 final RL 修正。

## Gaps / Open Questions

- Domain experts 具体有哪些、各自权重和 OPD weights 没有公开。
- OPD samples 如何按 task context 路由到 teachers 没有公开。
- Full-vocabulary OPD 是否有完整 ablation 证明优于 token-level approximation，还是主要来自稳定性和工程直觉，报告信息不足。
- OPD 和 GRM / reasoning mode / tool-agent data 之间的耦合没有完整拆解。

## Transfer Hooks

- worth-internalizing: specialist -> policy distillation consolidation 是和 mixed RL / trace-SFT 不同的合并哲学，适合放进后续 consolidation lens。
- try-at-small-scale: 可以先做简化版 student-trajectory teacher-logit distillation，验证是否比 teacher trace SFT 更稳。
- lookup-only: full-vocab reconstruction、teacher scheduling、WAL、shared-memory dispatch 的工程细节，除非研究 infra 可复现性，否则主要回查即可。

## Split Check

- current scope: consolidation / OPD only；GRM 和 tool-agent infra 分别在 `reward-verifier.md`、`tool-agent-training.md`。
- if this file grows beyond ~220 lines, split by: OPD objective vs full-vocab OPD infrastructure。

## Evidence Anchors

- 28: post-training pipeline 和 mixed RL -> OPD replacement。
- 29-30: reasoning effort modes 和 GRM 邻近设置。
- 32-34: OPD objective 和 full-vocabulary distillation。
- 34-35: post-training infrastructure、teacher scheduling、WAL、shared-memory dispatch。
