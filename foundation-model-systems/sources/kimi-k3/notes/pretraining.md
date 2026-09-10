# Kimi K3 Pretraining

```yaml
---
source_id: kimi-k3
section_type: stage-note
stage: pretraining
depth: working
confidence: medium
need_expert_review: false
---
```

## Core Design / Innovation

- K3 从训练起点就做 native multimodal next-token training，vision encoder 与 language backbone joint optimize，不做 language-pretrain 后的 post-hoc modality alignment。[11]
- data 由 Web Text、Code、Mathematics、Knowledge 四类 text 加大规模 vision corpus 构成；programmatic multimodal data 显著扩到 SVG、3D、Webpage、Game、CAD 等 code-render pairs。[10]
- long context 不是只改 position encoding：NoPE/KDA 免去 RoPE modification，但仍需要专门清洗、upsampling、synthetic scattered-dependency data 与 8K->64K->256K->1M curriculum。[12]
- K3 为 cosine 与 WSD 分别独立搜索最优 hyperparameters 后选择 cosine；这是比“共享超参直接比较 schedule”更可信的 recipe decision。[10-11]

## Why It Matters

可迁移的核心不是 K3 的具体数据量——它没有披露——而是 long-context capability 的分解：architecture extrapolation 只解决“能算”，coherent long data、task construction 与 progressive curriculum 才解决“会用”。同样，multimodal stability 由 initialization、objective 与 joint schedule 共同决定。

## Mechanism Sketch

1. 在较小模型上做 domain sampling / schedule / shape scaling studies。
2. 从 8K context 开始 native text+vision joint pretraining。
3. 扩到 64K，保持 KDA/NoPE architecture 不改 position parameters。
4. cooldown 进入 256K，再到 1M；提高 long coherent documents/videos 与 synthetic long-range tasks 的权重。
5. Per-Head Muon + weight clipping + QB，cosine schedule，1% warmup，weight decay 0.1。[10-12]

## Details / Evidence

- text pipeline 使用 rule heuristics、classifier quality scoring、dedup；domain sampling rates 来自 smaller-model ablations。[10]
- knowledge/math 沿用 K2 的 rephrasing：多 style/perspective prompting、chunk-wise autoregressive generation、source-fidelity verification。[10]
- vision data 混合 open collections 与 in-house filtering/synthesis/dedup；coordinate supervision 同时使用 absolute 与 normalized formats。[10]
- long natural documents/videos 经过 exact/fuzzy dedup、video perceptual hash、heuristic/classifier filtering、structural validation；稀缺长样本在 cooldown 中 upsample。[12]
- synthetic long-context data 将 multimodal documents/subtasks 重新组合，使答案依赖散布在完整 1M context 的信息，而非只靠局部 pattern。[12]

## Gaps / Open Questions

- 未披露 total training tokens、FLOPs、token-per-parameter optimum、各 domain/modality 比例、data cutoff、来源 license/provenance。
- 没有完整 decontamination list 或 benchmark leakage audit。
- scaling curve 只展示 K2 vs K3 aggregate loss/FLOPs；缺少拟合参数、置信区间、shape search grid 与每个 recipe component ablation。[10-11]
- 8K/64K/256K/1M 每阶段 token budget、batch、sequence packing 与 cooldown ratio 未公开。

## Transfer Hooks

- `worth-internalizing`: schedule comparison 必须分别 retune peak LR / batch，不能共享一组超参就宣布优劣。
- `worth-internalizing`: long-context curriculum 同时需要 source cleaning、coherence weighting 与 deliberately long-range dependency tasks。
- `try-at-small-scale`: from-scratch vision encoder vs contrastive initialization，用 training stability + downstream eval 双 gate。
- `lookup-only`: 1% warmup、weight decay 0.1、具体 context ladder。

## Evidence Anchors

- 9-10: native vision and data sources。
- 10-11: scaling law and schedule search。
- 11-12: joint training recipe and progressive context extension。
