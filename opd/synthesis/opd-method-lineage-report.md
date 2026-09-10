# OPD 方法谱系总结报告

> 这是当前报告入口。旧单文件报告已拆成分卷，避免一个 Markdown 继续膨胀。
>
> 当前证据基线：2026-06-15 `scripts/autoresearch.py status` 显示核心卡 71、候选论文 68、validation issues 0。报告默认基于已验证 L1 cards、`_meta/generated/research-map.md`、`_meta/generated/idea-context.md` 和必要 bounded briefs；没有新增完整 PDF 精读。

## 怎么读

- 只想获得主论点：读 [`README.md`](opd-method-lineage/README.md)。
- 想理解 OPD 方法谱系：读 [`01-lineage.md`](opd-method-lineage/01-lineage.md)。
- 想理解方法为什么这么设计：读 [`02-mechanisms-and-decision-axes.md`](opd-method-lineage/02-mechanisms-and-decision-axes.md)。
- 想查 failure mode、证据可信度和未解问题：读 [`03-failure-modes-and-evidence.md`](opd-method-lineage/03-failure-modes-and-evidence.md)。
- 想服务 idea 生成：读 [`04-idea-hooks.md`](opd-method-lineage/04-idea-hooks.md)。
- 想追溯证据和知道哪些地方没精读：读 [`05-evidence-and-limits.md`](opd-method-lineage/05-evidence-and-limits.md)。

## 总论

事实：OPD 起点是修复 off-policy KD / SeqKD 的 exposure bias。GKD 把 student rollout 纳入蒸馏目标，MiniLLM 选择 sequence-level reverse-KL policy-gradient 路线，DistiLLM 用 skew-KL 和 replay buffer 处理 KL 梯度爆炸与 SGO 生成成本。

解释：2025-2026 年主线已经不再是“换一个 KL”。更核心的矛盾是：student on-policy state coverage 带来更真实的训练状态，但这些 state 不一定落在 teacher 的可靠监督区域内。OPD 解决了 state mismatch，同时制造了 teacher reliability mismatch。

开放问题：真正有价值的 OPD idea 不应只是再提出一个 token weight 或 rollout schedule，而应显式控制 state、signal、granularity、trust region、privileged information 可内化性、以及 evaluation protocol 之间的关系。

## 文件状态

本入口是人读的 canonical entry；`_meta/generated/*` 仍由脚本维护，不手改。后续修改报告时优先改分卷文件，而不是重新扩写本入口。
