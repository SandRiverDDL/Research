# ResearchStudio-Idea：pattern induction

> 返回 [overview.md](overview.md)。主要证据为论文 [§3–§6, pp. 9–17](../../papers/researchstudio-idea-2607.04439.pdf) 与仓库中的 [15 pattern cards](https://github.com/microsoft/ResearchStudio/tree/298ca64ae5e3f242d58278601db34bfa6daa53b8/ResearchStudio-Idea/skills/idea_spark/references/ideation-patterns)、[31 subpattern cards](https://github.com/microsoft/ResearchStudio/tree/298ca64ae5e3f242d58278601db34bfa6daa53b8/ResearchStudio-Idea/skills/idea_spark/references/ideation-sub-patterns)。

## 1. Conference corpus 不是普通 accepted-paper list

**事实**：作者从 OpenReview 与 Semantic Scholar 构建 2021–2025 的 ICLR/ICML/NeurIPS corpus。去重后有 1,947 篇：Oral 1,014；High-Cited 260；Reject 722；其中 Oral∩HC 49，所以 label 可重叠。Reject 必须有明确拒稿决定和非平凡 review set。论文把 Oral 当 program-committee preference、HC 当 community adoption、Reject 当 failure signal。[论文 pp. 9–10, §3.1](../../papers/researchstudio-idea-2607.04439.pdf)

**事实**：数据并不均匀。仅 1,074 篇有 full abstract、716 有 parsed reviews、682 有 extracted introduction、340 有 meta-review；没有 recoverable review text 的记录仍可参加 signature extraction，但 review-derived fields 被降为低证据 auxiliary fields。[论文 pp. 9–10, §3.2](../../papers/researchstudio-idea-2607.04439.pdf)

**解释**：这比只看 accepted examples 强，因为它能告诉 pattern card“什么形态经常失败”；但 Oral/Reject 并非纯粹的机制因果标签。venue policy、年份、topic saturation、执行质量和 review 可得性都混在 label 中。

## 2. 从论文到 12-field innovation signature

**事实**：Stage 1 用 Claude Sonnet 4.6 读取 title、可用 abstract/introduction/reviews/meta-review，抽取 8 个字段：

- mechanism 侧：`innovation approach`、`key step`、`why non obvious`、`trigger condition`；
- outcome/review 侧：`reviewer praise`、`reviewer concern`、`acceptance signal`、`contribution type`。

Stage 2 再用 Sonnet 4.6 把前四个字段改写为 domain-agnostic、imperative 的 strategy descriptions，尽量移除 “Transformer / diffusion / molecule” 等主题词，只保留动作结构。1,947 篇完成 Stage 1；其中 1,891 篇四个 abstract fields 非空，进入 embedding。[论文 pp. 10–11, §4](../../papers/researchstudio-idea-2607.04439.pdf)

**风险**：所谓“strategy-only representation”是两次 LLM interpretation，不是对原论文机制的无损变换。模型可能把领域中决定成败的约束一并抽掉，或把不同方法改写成相似的高层动词。论文给出聚类 ablation，但没有逐项 human fidelity audit 的充分证据。[论文 §11 与 §15, pp. 28–29, 39–40](../../papers/researchstudio-idea-2607.04439.pdf)

## 3. Embedding → 31 clusters

**事实**：四个抽象字段拼接后，用 OpenAI `text-embedding-3-large` 得到 3,072 维向量并 L2 normalize；UMAP 以 cosine geometry 降到 10 维（`n_neighbors=15, min_dist=0, seed=42`）；HDBSCAN 对 `min_cluster_size ∈ {10,15,20,25,30,40}` sweep。作者选择 `min_cluster_size=10`：31 clusters，clustered points 上 silhouette 0.584。[论文 pp. 11–12, §5.1–5.2](../../papers/researchstudio-idea-2607.04439.pdf)

**关键事实**：902/1,891，即 **47.7%** 的记录未进入任何 density cluster，只有 989 个 clustered samples 直接支撑 31-cluster inventory。作者称其为 “unclustered” 而非 noise，并解释它们可能处于多个 modal strategy 之间。[论文 p. 12, §5.2](../../papers/researchstudio-idea-2607.04439.pdf)

**判断**：silhouette 0.584 只能说明选定 embedding/UMAP/HDBSCAN 配置下 clustered subset 的几何分离；它不证明“自然界恰好有 31 种创新动作”，也不覆盖近半未聚类样本。若把 31 clusters 当经验原料是合理的，把它当稳定 ontology 则证据不足。

## 4. 31 clusters → 15 patterns 与 31 subpatterns

**事实**：每个 cluster 先由 Opus 4.7 读取 8 个 centroid-nearest papers，生成短 label 与描述；第二个 pass 生成 tactic-level disambiguation card，含 5-step recipe、siblings distinction、trigger、Reject-derived failure mode 和 paper-agnostic lessons。[论文 p. 12, §5.3](../../papers/researchstudio-idea-2607.04439.pdf)

**事实**：再由 Claude Opus 4.7 在一个 structured call 中把 31 clusters 归成 15 个 Level-1 patterns，并将每个 cluster 映射到一个 primary、可选 secondary pattern。约束是 6–18 个 domain-agnostic reusable strategies，且每项有 definition、operational signature、when-to-apply。作者声明没有人工修改输出。[论文 pp. 13–15, §6](../../papers/researchstudio-idea-2607.04439.pdf)

**解释**：

- 31 subpatterns 是 clustering 对应的细粒度 tactic cards；
- 15 patterns 是 LLM 对 cluster inventory 的上位归纳；
- “15”不是由 HDBSCAN 直接发现，也不是经人工 Delphi/专家共识确定。

这也是它相对普通 prompt 的增益所在：prompt 不再凭空说“换个表示/拆解问题”，而是携带 trigger、operational signature、accepted/rejected lessons 与 sibling boundary。但其权威性仍是 **empirical heuristic taxonomy**。

## 5. Accepted / HC / Reject contrast 到底提供了什么

**事实**：clusters 中 Oral、HC、Reject 广泛交错。作者按 Oral share 标出 6 个 `Oral-safe`、1 个 `Reject-warn`、24 个 mixed clusters，但明确说这些只是 risk signals，不能作为推荐/禁止 gate；样本量、年份、会议与执行因素都会影响比例。[论文 pp. 12–13, §5.4](../../papers/researchstudio-idea-2607.04439.pdf)

**判断**：contrast 最有价值的不是“从 Oral 预测下一篇 Oral”，而是给每个 operator 加一份 **failure boundary**：同一种高层动作什么时候只是把先验塞进架构、什么时候缺少 identifiable contribution、什么时候 naive baseline 已足够。它是生成时的反例记忆，不是 acceptance classifier。

## 6. Forced multi-label classification 如何补上 47.7% 缺口

**事实**：15-pattern framework 对全部 1,891 个 complete records 另跑 independent multi-label tagging，不要求样本属于 HDBSCAN cluster。因此 unclustered samples 也会被强制映射进现有 15-pattern vocabulary。每篇平均 2.28 个 pattern；最常见是 2 个（59.2%）。运行时由此默认组合至少两个 pattern。[论文 §6.5, pp. 16–17](../../papers/researchstudio-idea-2607.04439.pdf)

**解释**：这里有两种不同的“coverage”：

- **discovery coverage**：只有 989/1,891 直接参与 density-cluster discovery；
- **classification coverage**：taxonomy 形成后，所有 1,891 被标入一个或多个既有类别。

后者不能倒推前者完整。forced classification 可以让 runtime 每篇都有标签，却也可能把 taxonomy 外的新 strategy 硬塞进最近的类别。

## 7. 证据强度与未解决风险

| 结论 | 当前证据 | dossier 判断 |
|---|---|---|
| corpus 同时含成功与失败样本 | 数据构造、label counts、review fields | 强事实，但标签含混杂因素 |
| abstraction 有助于形成 strategy 而非 topic cluster | paper ablation/self-report | 有支持，缺第三方复现 |
| 31 clusters 是稳定 subpattern inventory | 单一 embedding family、固定 UMAP seed、一次 sweep | 不足；未见跨 seed/model/bootstrap stability |
| 15 patterns 覆盖 ML ideation | forced classification + card construction | operationally 覆盖，scientifically 非穷尽 |
| pattern composition 比单 pattern 更好 | paper runtime design 与有限 ablation | 有方向性证据，仍依赖 LLM judge |

**开放问题**：若个人采用，应先做三项窄验证：换 embedding/seed 的 cluster adjusted mutual information；由领域专家抽查 abstraction fidelity；允许 `unknown/new pattern` 的 open-set classifier，统计 forced-fit rate。否则 taxonomy 最适合当 operator library，不适合当“科研创新的真分类学”。

