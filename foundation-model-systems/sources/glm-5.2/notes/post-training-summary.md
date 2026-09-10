# GLM-5.2 Post-training Summary

```yaml
---
source_id: glm-5.2
stage: post-training
summary_role: current-practice-release-delta
priority_for_post_training: S
confidence: medium
---
```

## Verdict

GLM-5.2 是当前 GLM post-training 的重要 release delta：它把 compacted long-horizon trajectories、critic-based PPO、online anti-hacking、slime rollout infra 和 parallel OPD 组合起来；方法信号强，但证据仍是 blog-bundle，不能获得与 full TR 相同的可信度。[blog-glm-52]

## Pipeline / Delta

```text
GLM-5 lineage SFT / reasoning / agentic base
-> long-horizon coding and tool-use rollouts
-> critic-based PPO over variable compacted sub-traces
-> online anti-hack filtering during rollout
-> multiple specialist experts
-> parallel OPD consolidation
```

- GLM-5 的 full TR 提供 SFT -> reasoning RL -> agentic RL -> general RL -> cross-stage distillation lineage；5.2 只记录明确改变的 current practice。
- 5.2 的核心训练目标从普通 group-wise formulation 转向 critic-based PPO，原因是 trajectory compaction 后可训练 sub-traces 数量与长度高度不稳定。[blog-glm-52]

## Core Mechanisms

### Critic-based PPO for Compacted Traces

- Long-horizon agent 会在 context pressure 下压缩历史，产生多个长度不一的 trainable segments；group-relative normalization 在这种结构上未必稳定。
- Critic 提供 segment/token-level value baseline，使不同数量、不同长度 sub-traces 的 credit assignment 不完全依赖同组样本比较。
- Blog 没公开 critic architecture、GAE/value loss、bootstrap 与 compaction boundary handling，当前只能确认设计方向。

### Online Anti-hacking

- Rule filter 与 LLM judge 联合识别可疑 tool calls / reward hacking；可疑行为被拦截，但 rollout 继续，而不是整条 trajectory 丢弃。[blog-glm-52]
- 这比 post-hoc 删除样本更可能保留探索成本，但 judge false positive、adaptive hacking 与训练分布偏移均未量化。

### Parallel OPD

- 十多个 expert policies 通过 parallel OPD 合并到 final model；这表明 GLM 当前实践更偏“分别训练 specialists，再 consolidation”，而非单 policy 混合所有 domain RL。
- 相比 MiMo/DeepSeek，公开材料没有足够公式细节说明 teacher logits、student rollouts、routing 和 loss weighting。

## Failure Modes / Controls

- Compaction 改变可训练 token 分布与 credit boundary，是长 agent RL 特有问题，不能用普通短 response GRPO 假设处理。
- Coding reward 容易被 test tampering、tool misuse、环境漏洞或 judge shortcut 攻击，必须在 rollout 时监控。
- 1M context、serving 与 post-training 是 coupled system；IndexShare/MTP 等 architecture delta 主要影响 rollout economics。

## Openness and Evidence

- 权重开放，但 post-training 证据来自官方 blog，缺少 TR、代码、数据与 ablation。
- 应将 critic PPO、anti-hacking、parallel OPD 标为 current-practice signals，而非已验证可复现 recipe。

## Transfer to Current Work

- 在 agent trajectory schema 中保留 compaction boundaries，分别统计 pre/post-compaction loss、reward 与 success。
- Anti-hack 应同时有 rule、model judge 和 executable integrity check，并报告误杀率，而不只是“过滤后分数提高”。
- 小规模实验可先比较 whole-trajectory reward、sub-trace GRPO 与 learned critic 三种 credit assignment。

## Evidence Anchors

- [rl-training.md](rl-training.md): critic PPO、anti-hacking、long-horizon agentic RL。
- [rl-training.md](rl-training.md): critic PPO、anti-hacking、expert models 与 parallel OPD。
- [architecture.md](architecture.md): 1M context / serving economics。
- [../README.md](../README.md): `[blog-glm-52]` source boundary。
