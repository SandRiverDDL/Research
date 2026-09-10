# GLM-5.2 Claims and Gaps

```yaml
---
source_id: glm-5.2
section_type: claims-and-gaps
depth: working
confidence: medium
need_expert_review: false
---
```

## 问题

GLM-5.2 公开材料哪些 claim 值得信？哪些只是 release rhetoric？哪些缺口会影响后续和 MAI / DeepSeek 的 comparison？

## 可信 claim

- GLM-5.2 是面向 long-horizon coding / agentic tasks 的增量 release；source bundle 反复强调 1M context、coding-agent scenarios、effort control 和 long-horizon benchmarks。[blog-glm-52]
- 1M context 的 architecture/serving 增量有具体机制：IndexShare for DSA、MTP/KVShare、rejection sampling、TV loss、KV-cache/CPU scheduling/long-context kernel optimization。[blog-glm-52]
- Post-training / RL 的公开重点是系统化 rollout 和 anti-hacking；它明确披露 slime、parallel OPD、critic-based PPO、compaction sub-traces、online anti-hack module。[blog-glm-52]
- Weights/model card/repo 是公开可访问的，release 形态比 API-only TR 更开放；GitHub/HF/ModelScope 都有下载路径。[hf-model-card], [github-readme]
- Eval footnotes 的细节较多，足以支持“需要按 methodology 审计”的工作，而不只是看分数表。[blog-glm-52]

## 暂不信的 claim

- “open model 接近 / 超过 closed frontier”这类表述需要谨慎：很多结果依赖 max effort、1M context、特定 harness、third-party service、judge model 或 release-time leaderboard snapshot。[blog-glm-52]
- “solid 1M context”不等于所有长上下文任务都可靠；公开证据主要集中在 coding-agent / long-horizon eval，缺少更广泛任务分布和 failure analysis。[blog-glm-52]
- Parallel OPD 合并十多个 expert models 很关键，但没有披露 teacher/expert 训练方式、loss、filtering、ablation；目前只能当 high-level design claim。[blog-glm-52]
- Critic-based PPO 的细节不足，不能直接复现，也不能判断它相对 GRPO/group-wise methods 的真实优势。[blog-glm-52]

## 关键缺失信息

- GLM-5.2 专门 TR、完整 architecture config、pretraining/mid-training data composition、long-context curriculum。
- RL prompt distribution、reward functions、critic training、KL/entropy/ratio controls、sampling/curriculum、rollback/collapse recovery。
- OPD 细节：expert sources、teacher routing、student target、logit vs trace supervision、filtering/weighting、compute budget。
- Anti-hack module 的 judge prompt、judge model、precision/recall、false positive/false negative、对训练稳定性的 ablation。
- Eval 外部可复现性：benchmark version、harness version、same-scaffold fairness、timeout/resource/token budget comparability。

## 值得内化

- Long-context agentic model 的系统设计不能拆开看：attention/serving、rollout infra、trajectory compaction、anti-hack、eval setting 是同一个问题。
- Coding RL 的 reward hacking 是主线问题，不是安全附录；如果 verifier 是 pass/fail，模型会学 shortcut，所以环境完整性必须进入 training loop。
- Agentic eval 的可信度来自 setting transparency：context、tokens、tools、timeout、judge、internet access、anti-hack policy 都是能力定义的一部分。

## 随查随用

- 具体 benchmark 数字、per-benchmark sampling parameters、MTP acceptance length、serving framework list、model download links。
- GLM-5 TR 中的 base pipeline / DSA / slime / OPD lineage，只有做 GLM family 深读或跨模型 comparison 时再回查。

## Evidence Anchors

- `[blog-glm-52]`: official GLM-5.2 blog / HF blog mirror。
- `[hf-model-card]`: GLM-5.2 model card and benchmark mirror。
- `[github-readme]`: GLM-5 series README and weights table。
- `[glm5-tr]`: GLM-5 TR, lineage/background only。
