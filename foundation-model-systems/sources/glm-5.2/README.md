# GLM-5.2 Source Dossier

```yaml
---
source_id: glm-5.2
source_type: blog-bundle
org: Z.ai
release_date: 2026-06-17
priority: A
status: section-notes
openness: open-weights
confidence: medium
lineage: glm-5
role: release-delta
base_source: glm-5
---
```

## 一句话

GLM-5.2 目前不是一份完整 TR，而是 GLM-5 lineage 上的增量 release：核心价值在于把 1M context、long-horizon coding/agentic RL、effort control、anti-hacking 和 open-weight deployment 绑定成一个面向 coding agent 的系统，而不是披露完整 pretraining recipe。

## 为什么重要

它值得放进本项目，不是因为榜单宣称“open model 接近 closed frontier”，而是因为它公开了几个 2026 agentic model system 的关键方向：长上下文必须和 inference architecture / serving 一起设计，coding RL 必须处理 compaction 后的长轨迹和 reward hacking，release eval 必须看 long-horizon agentic benchmarks 而不只是 AIME/SWE-Bench 单点分数。

## 核心设计 / Takeaways

- 1M context 是 GLM-5.2 的主线，但它强调的是“engineering-usable long context”：覆盖大型实现、自动化研究、性能优化、复杂 debugging 等 coding-agent 场景，而不是单纯扩大 context window。[blog-glm-52]
- Architecture 增量包括 IndexShare for DSA、MTP 上的 IndexShare/KVShare、rejection sampling 和 end-to-end TV loss；目标是同时降低 1M context FLOPs 和提高 speculative decoding acceptance length。[blog-glm-52]
- Post-training 主线是 agentic RL / OPD 工程化：用 slime 支撑复杂 rollout、parallel OPD，并把十多个 expert models 合并到最终模型。[blog-glm-52]
- RL 方法从 group-wise optimization 转向 critic-based PPO，原因是 long-horizon trajectory 被 compaction 后会产生数量和长度不稳定的 trainable sub-traces。[blog-glm-52]
- Coding RL 的核心风险是 reward hacking；GLM-5.2 用 rule filter + LLM judge 的 online anti-hack module，在训练和 eval 中拦截可疑 tool calls，同时让 rollout 继续而不是整条丢弃。[blog-glm-52]
- Eval 设计明显偏 long-horizon agentic coding：FrontierSWE、PostTrainBench、SWE-Marathon、Terminal-Bench、MCP-Atlas、Tool-Decathlon 等比普通 leaderboard 更能说明它想证明的能力。[blog-glm-52]

## Source Bundle

- technical report: GLM-5 TR only, used as lineage/background: https://arxiv.org/abs/2602.15763
- model card: https://huggingface.co/zai-org/GLM-5.2
- announcement / blog:
  - https://z.ai/blog/glm-5.2
  - https://huggingface.co/blog/zai-org/glm-52-blog
- code / repo: https://github.com/zai-org/GLM-5
- weights:
  - https://huggingface.co/zai-org/GLM-5.2
  - https://modelscope.cn/models/ZhipuAI/GLM-5.2
- external eval:
  - FrontierSWE: https://www.frontierswe.com/
  - PostTrainBench: https://posttrainbench.com/
  - SWE-Marathon: https://swe-marathon.vercel.app/
- local pdf: none for GLM-5.2 as of initial intake
- last checked: 2026-06-22

## Citation Labels

- default source is the GLM-5.2 blog / model card bundle, not a PDF TR.
- non-TR source labels used:
  - `[blog-glm-52]`: official GLM-5.2 release blog / HF mirrored blog.
  - `[hf-model-card]`: GLM-5.2 Hugging Face model card.
  - `[github-readme]`: zai-org/GLM-5 repository README.
  - `[glm5-tr]`: GLM-5 technical report, only for lineage/background.

## 最大证据缺口

- 没有 GLM-5.2 专门 TR；pretraining data、mid-training data、RL data composition、reward functions、critic details、expert model training recipe 基本未公开。
- “十多个 expert models 通过 OPD 合并”很重要，但 teacher/expert 来源、OPD loss、filtering、routing、数据比例和 ablation 都缺。
- Long-context training 只披露“从 mid-training 128K 开始使用 IndexShare”和 coding-agent scenario 扩展；没有完整 long-context curriculum。
- Eval 设置披露不少，但多个 long-horizon benchmarks 由第三方/官方服务执行，scaffold、judge、timeout、sampling 和 internet/tool permissions 的可比性需要逐项审计。

## Lens Hooks

- architecture: 1M context、DSA、IndexShare、MTP/KVShare、speculative decoding。
- data-pipeline: 只披露 coding-agent long-context training scenarios；缺完整 data mixture。
- training-recipe: GLM-5 TR 可提供 lineage，但 GLM-5.2 增量 recipe 不完整。
- rl-training: critic-based PPO for compacted long trajectories、online anti-hack、slime rollout infra。
- eval: long-horizon coding / agentic eval methodology and comparability。
- infra: 1M context serving、KV-cache capacity、long-context kernels、CPU-side scheduling、slime training-serving connection。

## 阅读入口

- `section-index.md`: 先看 source bundle 的可读地图。
- `notes/architecture.md`: 1M context、IndexShare、MTP、serving design。
- `notes/rl-training.md`: agentic RL、OPD、critic-based PPO、anti-hacking。
- `notes/eval.md`: long-horizon coding eval 的设计和可比性。
- `notes/claims-and-gaps.md`: comparison 前先读，避免把 release rhetoric 当作完整 TR 事实。
