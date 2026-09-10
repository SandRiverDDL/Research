# GLM-5.2 Agentic RL / OPD

```yaml
---
source_id: glm-5.2
section_type: stage-note
stage: rl-training
substage: agentic-long-horizon
depth: working
confidence: medium
need_expert_review: false
---
```

本 note 覆盖 GLM-5.2 blog 披露的 agentic RL、OPD 和 anti-hacking。它不是完整 post-training recipe。

## Core Design / Innovation

- GLM-5.2 把 post-training 问题定义成大规模 long-horizon agentic rollout 的系统问题：任务跨 domain、tool use、多轮环境反馈、sub-task decomposition，单纯同步 RL loop 不够。[blog-glm-52]
- slime 是开源 LLM post-training / RL scaling framework，在 GLM-5.2 里承担训练到大规模 inference rollout 的统一 infra 层；它连接 Megatron training、SGLang rollout、custom data generation、reward/verifier feedback 和 environment interaction，支持 white-box rollout、black-box rollout、compact trajectory、sub-agent workflow，并连接不同 inference service / parallelism / routing / PD disaggregation setup。[blog-glm-52]
- Parallel OPD 被用于把十多个 expert models 合并到最终模型；blog 披露整个 OPD 大约两天，但没有给 loss、teacher routing、filtering 或 expert training 细节。[blog-glm-52]
- Long-horizon RL 从 group-wise optimization 转向 critic-based PPO，因为 compaction 后同一 prompt 的 rollout 会产生数量和长度都不稳定的 trainable sub-traces，group-relative assumption 不再自然。[blog-glm-52]
- Anti-hacking 是 coding RL 的核心机制，不是 eval 后处理：rule-based high-recall filter + LLM judge high-precision intent check，在线监控 tool calls，发现 hack 时 block call 并返回 dummy information，让 rollout 继续。[blog-glm-52]

## Why It Matters

对后训练岗位最值得学的是：agentic RL 的难点往往不是 PPO 名字，而是 rollout 组织、trajectory compaction、hack detection、environment/tool isolation、training-serving infra 复用。GLM-5.2 把这些问题放到 release 主线，说明 2026 coding-agent model 的 post-training 已经很像系统工程。

对未来基模方向，值得保留的 taste 是：长上下文、agentic RL 和 serving infra 是耦合的。训练里怎么组织 rollout，会影响生产 serving 的调度经验；生产 serving 的限制，也会反过来塑造可训练的 agent trajectories。

## Mechanism Sketch

1. 用开源 slime framework 管理大规模 rollout 和训练资源：训练侧接 Megatron，rollout/serving 侧接 SGLang 或其他 inference services，并通过 Data Buffer / custom generation / reward-verifier path 组织 RL 样本。
2. 对十多个 expert models 做 parallel OPD，把 expert 能力合入 final model。
3. 针对 long-horizon task，把超长 trajectory 经 compaction 切成多个 sub-traces。
4. 因为每个 prompt 产生的 sub-trace 数量/长度不稳定，改用 critic-based PPO 对 individual rollouts 学 token-level advantages。
5. 对 coding agent reward hacking 做在线防护：规则先抓可疑行为，LLM judge 判断意图，拦截具体 tool call，而不是直接丢弃整条 trajectory。

## Details / Evidence

- slime 本身是开源训练框架，项目文档定位为 LLM post-training framework for RL scaling；GLM-5.2 blog 里强调的是它在 GLM-5.2 post-training 中承担 production-scale rollout / training orchestration。[blog-glm-52]
- slime 支持 white-box rollout、black-box rollout、compact trajectory、sub-agent workflow；这说明 GLM-5.2 的 RL 数据来源/训练轨迹可能混合了可见模型 logits、外部服务、压缩轨迹和多 agent workflow。[blog-glm-52]
- Blog 明确说 GLM-5.2 post-training 使用 slime 做 parallel OPD，把 more than ten expert models 合并成最终模型，过程约两天。[blog-glm-52]
- Long-horizon trajectories 经 compaction 后，同一 prompt 的不同 rollouts 会产生不同数量的 trainable traces，长度变化也很大；这就是它放弃 group-wise optimization 的直接理由。[blog-glm-52]
- Critic-based PPO 使用 critic 估计 token-level advantages；blog 说把所有 compacted sub-traces 纳入 trainable trajectories，并用 token-level loss 处理 length imbalance。[blog-glm-52]
- Hack examples 包括读取 hidden eval artifacts、copy reference/upstream commits、直接 fetch GitHub target source 等；这类行为会把 pass/fail verifier 变成错误训练信号。[blog-glm-52]
- Online anti-hack 的关键设计是“block hacked action but continue rollout”。这比整条 trajectory reject 更稳定，因为 abrupt stop 可能导致训练不稳定或 collapse。[blog-glm-52]

## Gaps / Open Questions

- Expert models 是怎么训练出来的？是 domain specialists、effort specialists、tool specialists，还是 checkpoint ensemble？未披露。
- OPD 具体是 logit distillation、trajectory distillation、teacher trace SFT，还是混合 loss？未披露。
- Critic 的训练数据、reward model、value target、KL/entropy/ratio clipping、off-policy control 都未披露。
- Anti-hack LLM judge 的 prompt、judge model、误杀/漏杀率、是否会引入 judge leakage 未披露。
- “返回 dummy information 继续 rollout”如何影响 credit assignment 和 policy learning，目前只是解释性 claim。

## Lookup-only

- Parallel OPD duration: approximately two days。[blog-glm-52]
- Expert count: more than ten expert models。[blog-glm-52]
- Rollout modes named by slime: white-box rollout、black-box rollout、compact trajectory、sub-agent workflow。[blog-glm-52]
- Hack examples: protected eval artifacts、upstream commits、GitHub target source、hidden cases。[blog-glm-52]

## Evidence Anchors

- `[blog-glm-52]`: slime for Agentic RL, RL for Long-Horizon Task with Anti-hacking。
- `[glm5-tr]`: only if later reading GLM-5 asynchronous RL / OPD lineage in depth。
