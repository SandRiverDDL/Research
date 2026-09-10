# Qwen3.5 Section Index

## Source Map

- `[blog-qwen35]`: Qwen 官方 release blog —— 旗舰参数、hybrid attention、MoE sparsity、MTP、native multimodal、agent claim 的主源。
- `[blog-aliyun]`: 阿里云开发者博客 —— 中文 release 解读，可补充 lineup 和发布节奏。
- `[batch]`: DeepLearning.AI The Batch —— 独立第三方对架构和定位的复述，用于 sanity check claim。
- `[hf]`：HuggingFace model card，覆盖 license、checkpoint size 与 context length。
- `[qwen3-tr]`: Qwen3 TR，仅在解释 lineage / 对比 Qwen3 → Qwen3.5 改动时引用，不作为 Qwen3.5 fact。

## Read Order

1. README + source-bundle 先看，搞清边界。
2. 写 stage notes 时按以下顺序：
   - `notes/architecture.md`（hybrid attention、MoE、MTP）
   - `notes/multimodal-pretraining.md`（native early fusion、tokenizer、多语）
   - `notes/post-training.md`（agent / visual agent / instruction-following claim）
   - `notes/eval.md`（benchmark claim audit + 与 Qwen3 对比）
   - `notes/serving-cost.md`（部署显存、吞吐、价格 claim）
   - `notes/claims-and-gaps.md`（未披露项 + claim 可信度评级）
3. 任何强结论必须回到 blog 段落或 model card 字段；缺源就标 open question。

## Read Coverage

- 已读：官方 Qwen3.5-4B model card 的 highlights、architecture、eval setting 与 best practices。
- 已核验：Qwen3.6-35B-A3B 官方 release blog。
- 仅 tracking：Qwen3.7 Max/Plus API platform positioning。
- 待出现完整 TR 后再补 PDF/page-level anchor；当前不能填补具体 SFT/RL objective、reward 或 mixture。
