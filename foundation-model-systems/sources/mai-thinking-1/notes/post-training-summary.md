# MAI-Thinking-1 Post-training Summary

```yaml
---
source_id: mai-thinking-1
stage: post-training
summary_role: current-practice-process-reference
priority_for_post_training: A
confidence: medium
---
```

## Verdict

MAI-Thinking-1 是一份 reasoning-model hill-climbing process report：它最有价值的是把 long-RL stability、self-distillation reset、domain specialists、trace consolidation 和 final alignment 描述成连续控制过程，而不是宣称某个 RL objective 单独解决问题。[31-49]

## Pipeline

```text
midtrained / long-context checkpoint
-> reasoning-oriented initialization
-> specialist RL climbs (STEM/code, agentic, helpfulness/safety)
-> self-distillation for reset / migration / format conversion
-> specialist trace SFT consolidation
-> lightweight final RL for style, safety and regression repair
```

- Base 侧已经通过 staged 16K -> 64K -> 256K training 和 mixture search 建立 reasoning/long-context prior；post-training 不是从通用短上下文 base 突然开始。[16-30]
- Specialists 分别优化 STEM/coding、agentic、helpfulness/safety，再由统一 student 吸收 traces，最后 RL 修正合并后的行为。[31, 49]

## Core Mechanisms

### Long RL as a Control System

- 训练持续监控 entropy、policy ratio spikes、language drift、response length、problem difficulty 和 off-policy mismatch。[31-36]
- 这套做法的核心不是“允许模型想更久”，而是让 rollout distribution 随训练逐步变化时保持可诊断、可回退。

### Self-distillation as Engineering

- Self-distillation 被用于 collapse recovery、checkpoint migration、reasoning-format conversion 和避免 policy 过窄，而不只是最终能力压缩。[34-37]
- 它相当于在 RL climb 中插入可控的 policy reset：保留成功行为，同时重建更平滑、可继续训练的起点。

### Specialist Consolidation

- MAI 更接近 `teacher traces -> SFT packing -> final RL repair`，不同于 DeepSeek/MiMo 在 student trajectories 上匹配 teacher logits。
- 优点是实现简单、可利用完整成功轨迹；风险是 student 被 teacher trace distribution 约束，且 specialist conflicts 主要留给 final RL 处理。[31, 49]

## Failure Modes / Controls

- Entropy collapse 与过长/过短 reasoning 需要独立监控，不能只看 reward 上升。[31-36]
- Policy/checkpoint 迁移可能造成行为格式与能力退化，self-distillation 作为恢复机制。
- Specialist packing 可能损失弱域能力或 general helpfulness，因此最终 RL 同时承担 safety/style 与 reasoning regression gate。

## Openness and Evidence

- API-only，不能作为开放 recipe 复现；但 TR 对 decision process、失败模式和系统控制披露较好。
- Reward data、exact objective、specialist mixtures 和 infra configs 未开放。其价值是 industrial taste，而非可下载训练栈。

## Transfer to Current Work

- 为长 RL 建 dashboard：entropy、ratio distribution、length、language、pass-rate/difficulty、policy lag，而不是只记 final benchmark。
- 把 self-distillation 设计为显式 recovery/migration experiment，并与直接继续 RL、普通 SFT reset 做对照。
- Consolidation comparison 应区分 trace-SFT 与 on-policy logit distillation，测 capability retention、sample efficiency 与继续 RL 的稳定性。

## Evidence Anchors

- [rl-training.md](rl-training.md): pages 31-36。
- [sft-distillation.md](sft-distillation.md): pages 34-37。
- [consolidation.md](consolidation.md): pages 31, 49。
- [eval.md](eval.md): pages 53-55, 101-106。
- [pretraining-engineering.md](pretraining-engineering.md): pages 21-30, 85-88, 106-109。
