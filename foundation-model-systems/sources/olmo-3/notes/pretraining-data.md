# Olmo 3 Pretraining / Midtraining Data

```yaml
---
source_id: olmo-3
section_type: pretraining-data-mixture
stage: pretraining
depth: working
confidence: medium
need_expert_review: false
---
```

## Core Design / Innovation

- Base data 不是一次性 mixture，而是为后训练目标设计的三段 curriculum：通用 pretraining、能力定向 midtraining、long-context extension。[4-5]
- Pretraining 的关键改进是 trillion-token global dedup、olmOCR science PDFs、token-constrained mixing、quality-aware upsampling。[5]
- Midtraining 的关键不是简单加高质量数据，而是用“distributed source feedback + centralized integration tests”评估 candidate mix 对 base quality 和 post-trainability 的影响。[5]
- Long-context extension 依赖大规模 science PDFs，并明确服务 reasoning / tool-use 的长上下文需求。[5]

## Why It Matters

这里值得内化的是“pretraining data mix 要为后训练留接口”：不是只优化 base benchmark，而是让后续 SFT/DPO/RL 更容易唤出 reasoning、tool-use 和 long-context 行为。

## Mechanism Sketch

1. Dolma 3 Mix：约 6T token 的通用 pretraining mix。
2. Dolma 3 Dolmino Mix：约 100B token 的 midtraining mix，强化 code、math、QA、instruction following 和 reasoning traces。
3. Dolma 3 Longmino Mix：50B/100B token 的 long-context extension，重点利用长 science PDFs。
4. 用 OlmoBaseEval 在小规模和阶段转换时做 centralized integration test。

## Details / Evidence

- TR 明确说 pretraining 数据源大体常规，但新增了 global dedup、olmOCR science PDFs 和两种 token selection 方法。[5]
- Midtraining 不是只看单源效果，而是把 individual source feedback 和 centralized integration tests 结合，评估 mix 对 base model quality 与 post-trainability 的综合影响。[5]
- Long-context 数据披露了大量长文档规模：超过 22.3M 个 8K+ 文档和 4.5M 个 32K+ 文档。[5]

## Gaps / Open Questions

- First pass 还没有审计 appendix A.2/A.3 的具体 mix 比例、重复策略和 decontamination 细节。
- 需要和 MAI 的 scale-ladder mixture search 对比：Olmo 更开放，MAI 更像工业界 scale transfer / ablation recipe。

## Lookup-only

- 具体 token 数、文档数、training cost、各 stage hyperparameter 需要时回 appendix。[5, 84-95]

## Evidence Anchors

- 4-5: base model training and data curriculum.
- 13-35: pretraining, midtraining, long-context extension details.
- 87-95: appendix data details.

