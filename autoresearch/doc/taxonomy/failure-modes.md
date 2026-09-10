# Autoresearch Failure Modes

> Stable cross-paper failure tags. Extend only when a tag will be reused.
>
> **Scope**：本 taxonomy 只收 method-intrinsic failure（"换诚实作者用同方法这问题还在吗？在"）。
> 汇报 / 证据 pathology（cherry-pick / metric bias / reproducibility gap / weak baseline / metric gaming / source gap / evidence-tier mixing）走 `../review-checklist.md`，不进 frontmatter tag。
> `human-in-the-loop-hidden` 特殊：既是方法结构常态（作者不写清就默认发生）又是 autoresearch 特有作弊向量，暂保留在此 tag 池并在 checklist Tier A 强制审查。

## Core Failures (method-intrinsic)

- `hallucinated-novelty`: 系统自评"novel"但实际是已发表工作的重述或琐碎变体。
- `citation-fabrication`: 引用文献不存在、作者/年份错误、或引文语义与被引论文不符。
- `weak-experimental-design`: 生成的实验缺 baseline、缺 ablation、样本量不足、metric 与 claim 不匹配。
- `reviewer-model-hacking`: 生成的 paper 针对 LLM reviewer 的偏好过拟合，专家评审下不成立。
- `code-execution-fake-success`: 生成代码"跑通"但结果来自 mock / hard-coded / 错误验证。
- `human-in-the-loop-hidden`: 论文声称端到端，实际关键步骤由人工挑选、修改、重试。（Tier A 每卡强制审查，见 `../review-checklist.md`）
- `verifier-blind-spot`: 内置 verifier 只能捕捉 surface error，对方法/推理错误无感。
- `scope-drift`: 生成的 research 与初始 hypothesis 脱节，最终 claim 是 post-hoc 拼凑。
- `benchmark-contamination`: autoresearch benchmark 与训练数据重叠导致虚高分数。

## Retired / moved to review-checklist.md

以下 tag 属于汇报/证据 pathology，已从 frontmatter tag 池移出，改到 `../review-checklist.md` Tier B 触发式审查：

- `cherry-picked-showcase`
- `metric-selection-bias`
- `reproducibility-gap`
- `evidence-tier-mixing`（另由 DECISIONS.md 2026-07-15 强制标注）
- `weak-baseline`
- `metric-gaming`
- `source-gap`

已有卡的 frontmatter 里出现上述 tag 属于历史遗留，**不需要回填清理**；新卡不再使用。
