# Qwen3.5 Source Bundle

## Primary

- Release blog (Qwen Team): https://qwen.ai/blog?id=qwen3.5
- Alibaba Cloud developer blog: https://developer.aliyun.com/article/1712860
- Model hub: https://huggingface.co/Qwen
- Small dense model card: https://huggingface.co/Qwen/Qwen3.5-4B
- Flagship MoE model card: https://huggingface.co/Qwen/Qwen3.5-397B-A17B-FP8
- Repository (lineage): https://github.com/QwenLM/Qwen3

## Secondary / Independent Coverage

- DeepLearning.AI The Batch: https://www.deeplearning.ai/the-batch/alibabas-new-model-uses-hybrid-attention-layers-and-a-sparse-moe-architecture-for-speed-and-performance
- Baidu Baike (entry-level Chinese summary, treat as secondary): https://bkso.baidu.com/item/Qwen3.5/67312581

## Background / Lineage

- Qwen3 TR (前代 baseline): https://arxiv.org/abs/2505.09388
- Qwen3 dossier: `sources/qwen3/`

## Local Files

- 暂无 PDF；待官方放出 model card / tech report 后补到 `papers/qwen3.5/`。

## Source Role

Full TR equivalent for Qwen3.5 lineage based on blog bundle. 任何 architecture / training / serving claim 都要在 stage notes 里标注来自 official blog 还是 secondary report。

## Citation Labels

- `[blog-qwen35]`: 官方 release blog
- `[blog-aliyun]`: 阿里云开发者社区文章
- `[batch]`: DeepLearning.AI 二手报道
- `[hf-small]`: Qwen3.5-4B 官方 model card，包含 architecture、context、RL/infra highlights 与 eval setting。
- `[hf-flagship]`: Qwen3.5-397B-A17B 官方 model card。
- `[qwen3-tr]`: 历史 baseline，仅作 lineage 参考

## Checked

- last checked: 2026-07-21
- source status: 官方 model cards 已核验，第一版 stage notes 已完成；仍无完整 training TR。
