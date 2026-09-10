# DeepSeek-V4 Post-training Summary

```yaml
---
source_id: deepseek-v4
stage: post-training
summary_role: current-practice
priority_for_post_training: S
confidence: medium
---
```

## Verdict

DeepSeek-V4 的价值不是一个新 RL loss，而是把 reasoning modes、domain specialists、full-vocabulary OPD、generative reward、tool interface 和 million-token rollout infrastructure 组织成同一套 frontier post-training system。[28-36]

## Pipeline

```text
initial fine-tuning
-> domain-specific GRPO specialists
-> rubric / GRM signals for hard-to-verify tasks
-> student-generated trajectories
-> multi-teacher full-vocabulary OPD
-> unified Non-think / Think High / Think Max policy
```

- V4 大体继承 V3.2 的 post-training 骨架，但明确用 OPD 完全替换 mixed RL consolidation stage。[28]
- Specialist teachers 使用 domain-specific prompts 和 rewards 做 GRPO-style RL；报告称最终有十多个 experts，但没有公开完整 domain/routing 清单。[28, 32]
- 不同 reasoning modes 使用不同 context windows、length penalties；Think Max 还加入专用 system prompt。这些 mode 是训练行为，不只是 inference prompt preset。[29-31]

## Core Mechanisms

### Full-vocabulary OPD

- Student 自己生成 trajectories，teachers 在 student distribution 上提供 token distributions，student 用 reverse-KL-style objective 对齐 experts。[32-34]
- 选择 full-vocabulary logits 是为了避免 sampled/token-subset KL 的高方差与不稳定；代价是 teacher inference、logit transport 和存储非常重。[33-35]
- 配套系统包括 centralized teacher storage、on-demand loading、hidden-state caching、on-the-fly full-logit reconstruction、token-granular WAL 和 shared-memory dispatch。[33-35]

### Reward and Hard-to-verify Tasks

- 对 hard-to-verify prompts，V4 使用 rubric-guided RL data 和 Generative Reward Model signals。[29-30]
- “actor itself functions as GRM” 是重要方向信号，但缺少训练目标、输入输出格式和 calibration，当前只能视为高层设计而非可复现 recipe。

### Agentic Training Surface

- DSML special-token schema 降低 tool-call escaping/parsing failures；tool conversations 跨 turn 保留 reasoning history，普通聊天会在新 user turn 丢弃旧 reasoning。[30-31]
- DSec sandbox 提供 trajectory logging、provenance、preemption-safe resumption 和 deterministic replay，说明 environment/replay 是训练基础设施而非单纯 eval harness。[34-36]

## Failure Modes / Controls

- MoE/long-context economics 决定能否负担超长 rollout；CSA/HCA、KV compression 与 post-training 不是独立模块。[9-14]
- Token-level WAL 处理长 rollout 被抢占或失败后的恢复；shared-memory path 处理 million-token RL/OPD sample transport。[34-35]
- 未披露 teacher routing、expert weighting、GRM reward hacking control 和 tool-data composition，是迁移时最大的风险。

## Openness and Evidence

- 开放权重 + 完整 TR，pipeline 与 infra claim 具体；训练 data、reward implementation、OPD configs/code 未开放。
- Internal agentic/coding eval 对 product fit 有信号，但不能替代 public reproduction；1M context 也不能解释为所有长任务均已解决。[36-44]

## Transfer to Current Work

- 优先复现简化版 `student rollout -> teacher logits -> dense distillation`，再比较 teacher-trace SFT，而不是一开始做 full-vocab multi-teacher system。
- 把 tool schema、trajectory provenance、deterministic replay 和 rollout recovery 纳入 recipe；这些往往比微调 GRPO clip 更影响 agentic training 成功率。
- Eval 必须按 reasoning effort/context/tool budget 分层，避免把额外 inference compute 当训练收益。

## Evidence Anchors

- [architecture.md](architecture.md): pages 9-14, 24-26。
- [consolidation.md](consolidation.md): pages 28-35。
- [reward-verifier.md](reward-verifier.md): pages 29-30。
- [tool-agent-training.md](tool-agent-training.md): pages 30-36。
- [eval.md](eval.md): pages 36-44。
