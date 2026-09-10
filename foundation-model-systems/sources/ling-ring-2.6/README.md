# Ling / Ring 2.6 Source Dossier

```yaml
---
source_id: ling-ring-2.6
source_type: model-tr
org: inclusionAI
release_date: 2026-06-13
priority: S
status: section-notes
openness: open-weights
confidence: high
lineage: ling-ring
role: full-tr
base_source: ling-2.0
---
```

## 一句话

Ling/Ring 2.6 是 2026 年高信息密度的 agentic post-training TR：Ling 路线优化即时响应与 capability-per-token，Ring 路线用环境数据、长程 agentic RL 与 KPop 训练深度 reasoning/agent 行为，并把异步 rollout、training-inference mismatch 和 sandbox 编排纳入同一系统设计。[13-19, 28-31]

## 为什么重要

- 不是只靠 trillion-parameter positioning：报告给出了 Ling 和 Ring 两条不同 post-training objective，以及 agent environment/filtering/infra 的具体机制。
- 对当前工作最有价值的是 token-efficiency alignment、agentic data frontier selection、KPop 与 partial-rollout asynchronous RL。
- 开放全部 2.6 checkpoints，但训练数据和完整训练代码未完全开放，因此定位是 frontier open-weight TR，不是 fully reproducible recipe。

## 核心机制 / Takeaways

- Ling：SFT 后训练 specialists，再围绕输出 token efficiency 做 Evolutionary CoT、Linguistic Unit Policy Optimization、shortest-correct-response distillation 和 bidirectional preference alignment。[13-15]
- Ring：构建 coding/search/tool-use mixture，以 environment execution 提供可验证 feedback，并用 Dynamic Pass Rating 保留当前 policy 能学到但未掌握的任务。[16-18]
- KPop 用 sampled-token vs rest-of-vocabulary 的 symmetric binary KL 约束 training/inference policy mismatch，替代 IcePop 的统一 ratio threshold。[18-19]
- ASystem 以 token budget、partial rollout、cross-version buffer 和 bounded staleness 提高长尾 reasoning/agent rollout 利用率。[28-31]
- Agent infrastructure 将 inference 与 environments 独立扩缩，统一 sandbox/verifier HTTP/MCP contract，避免 GPU 等待工具调用。[29-31]

## Source Bundle

- technical report: https://arxiv.org/abs/2606.15079
- model collection: https://huggingface.co/collections/inclusionAI/ling-26
- Ring collection: https://huggingface.co/collections/inclusionAI/ring-26
- environment: https://github.com/inclusionAI/AEnvironment
- local PDF: `/Users/chy/Research/foundation-model-systems/papers/ling-ring-2.6/ling-ring-2.6.pdf`
- last checked: 2026-07-21

## Lineage / Delta

- lineage：Ling 2.0 / Ring 1T -> Ling and Ring 2.6。
- Ling 定位：instant/token-efficient model line。
- Ring 定位：deep-reasoning 与 long-horizon agentic line。
- 不可直接继承：2.6 已明确修改的 IcePop behavior、旧 architecture 与 data mixture。

## 最大证据缺口

- “all checkpoints”开放不等于 data/code/environment 完整可复现。
- KPop 的核心公式公开，但完整 thresholds、per-domain reward、routing 与 end-to-end ablation 仍有限。
- 大量 agent benchmark 使用特定 scaffold/tool setup，跨模型 leaderboard 不能直接视为同条件能力比较。

## Lens Hooks

- RL 训练：KPop、bounded-staleness async RL 与 token-efficient objective。
- tool-agent-training：coding/search/tool environments 与 Dynamic Pass Rating。
- sft-distillation：specialist training 与 shortest-correct-response distillation。
- 基础设施：ASystem、ARouter 与训练—推理 numerical alignment。

## 阅读入口

- `section-index.md`: 训练与 infra 页码。
- `notes/post-training.md`: Ling/Ring 两条 post-training flow。
- `notes/tool-agent-training.md`：agentic data、筛选与 reward hacking 防护。
- `notes/rl-infrastructure.md`: KPop、ASystem 与 asynchronous rollout。
- `notes/claims-and-gaps.md`: 开放性和 eval 边界。
