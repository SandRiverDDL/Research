# GLM-5 Architecture / Pretraining

```yaml
---
source_id: glm-5
section_type: stage-note
stage: architecture-pretraining
depth: working
confidence: high
need_expert_review: false
---
```

## Core Design / Innovation

- GLM-5 的 architecture 主线是“扩大 MoE 容量，同时把长上下文 attention 成本压下来”：744B total / 40B active，80 layers，256 experts，配合 MLA、DSA 和 MTP。[4-6]
- DSA 不是附属技巧，而是让 200K+ context 和 agentic long-horizon deployment 可承受的关键。GLM-5 先从 dense base 做 DSA warmup，再做 sparse adaptation，试图保留 dense attention 的 long-context fidelity。[5-6]
- MTP with parameter sharing 让多个 MTP layers 共享参数，目标是在类似 memory cost 下提高 speculative decoding acceptance length。[5]
- Pretraining data 侧围绕 agentic engineering 重做：web quality、code、math/science、long documents、repo-level code、issue/PR 数据都服务复杂系统工程任务。[8-9]

## Why It Matters

GLM-5 的重点不是“MoE 又变大”，而是把 architecture 和数据任务目标绑定：如果目标是长轨迹 coding/search/terminal agent，那么 long-context attention、repo-level data、issue/PR data、tool-integrated reasoning data 都必须一起设计。这个思路比单独记某个模型参数更值得保留。

## Mechanism Sketch

1. Dense/MLA base 完成主要 pretraining 和 midtraining。
2. 在 midtraining 末端引入 DSA，先 dense warmup indexer，再 sparse adaptation。
3. Long-context curriculum 从 4K 扩到 32K/128K/200K，并加入 repo-level code、issues、PR、long documents 和 MRCR-like synthetic tasks。
4. MTP 作为训练/推理一体化设计，为 speculative decoding 和 RL rollout tail latency 服务。

## Details / Evidence

- GLM-5 相比 GLM-4.5 从 355B/32B active 扩到 744B/40B active，pretraining data 从 23T 增到 28.5T。[3-4]
- DSA adaptation 包含 1000-step dense warmup 和 20B token sparse adaptation；报告对 long sequences 的 attention compute 有 1.5-2x 降低，同时 long-context performance 接近 MLA。[5-6]
- 数据筛选包括 DCLM classifier、world knowledge classifier、code language classifier、math/science LLM scoring、long-document chunk aggregation，并过滤 synthetic / AI-generated / template-like low-quality data。[8]
- Midtraining context curriculum 为 32K 1T tokens、128K 500B tokens、200K 50B tokens；code 数据包括 repo files、commits、issues、PRs，并构建约 10M issue-PR pairs。[8-9]

## Gaps / Open Questions

- DSA 和 dense MLA 的质量差异主要靠 benchmark 展示，训练稳定性和 failure cases 披露有限。
- Data mixture 的比例、filter threshold、teacher model 使用和污染控制没有完整公开。
- MTP 的 acceptance length 提升与不同 serving stack 的真实收益需要结合 GLM-5.2/IndexShare、MiniMax MSA、DeepSeek sparse attention 横向比较。

## Lookup-only

- 具体 layer/expert/head 参数、optimizer细节和 training infra tricks 回查 `[4-10]`。
- 精确 DSA warmup / sparse adaptation hyperparameters 回查 `[5-6]`。

## Evidence Anchors

- 4-6: architecture, MLA, MuON Split, MTP, DSA.
- 8-9: pretraining / midtraining data and long-context curriculum.
- 9-10: training infrastructure details.
