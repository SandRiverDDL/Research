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

## 问题

Scope：base 的三阶段数据 curriculum；2026-10-07 回读重点为 pretraining / midtraining。
- Web/PDF/code/math 怎样处理与筛选？
- 数据配比由什么实验决定？
- LR、batch、schedule、token budget 和 epoch 是多少？
- 哪些配置有选择依据，哪些只披露了最终值？

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

## 数据处理与 mixture 选择（2026-10-07 回读）

### Web：清洗、去重、再控制质量与主题

- **事实**：104 个 CommonCrawl dumps，cutoff 为 2024-12-31；Resiliparse 提取语义文本，规则过滤 spam/adult URL、长度、符号、内部重复、spam phrases；fastText language classifier 保留 English，再做 Madlad400 sentence heuristics。[html-web]
- **事实**：三层去重：global text-hash exact dedup；MinHash fuzzy dedup 后在 clusters 内做 Jaccard 检查、保留较新的 crawl；suffix-array substring dedup 清理重复 filler/boilerplate，并保留至少一份。[html-web]
- **事实**：WebOrganizer 24 topics × topic 内 quality percentile 的 20 档，得到 480 subsets；quality fastText 用 instruction/chat 数据作 positives、DCLM-RefinedWeb 抽样作 negatives。[html-web]
- **事实**：不是自然重复多少就训练多少。先 aggressive dedup，再以 quality-aware upsampling 控制重复；quality score 是模型估计的 proxy，不能当客观质量真值。[html-web; html-mixing]

### PDF / code / math

- **事实**：science PDFs 经 olmOCR 提取、fuzzy dedup、document-type-aware PII filtering、English/表格/数字比例等 heuristics，再按 topic 分类；PII filtering 使用 Gemma 3 12B / 4B。[html-sources]
- **事实**：code 使用 Stack-Edu，保留 programming-language partitions 供混合实验；math 使用保留 LaTeX 的 arXiv/Proof-Pile-2 与 FineMath 3+；另保留 Wikipedia/Wikibooks。[html-sources]

### Pretraining mixing：小模型实验 → 回归 → 受约束搜索

1. **事实**：训练一批 30M proxy models，各 3B tokens；从以 natural distribution 为中心的 Dirichlet 分布抽 mixture，swarm size 的经验值约为 domains 数的 5 倍。[html-mixing]
2. **事实**：在 Base Easy suite 上测每个 task 的 answer bits-per-byte（BPB）；小规模模型 accuracy 信号弱，连续 BPB 更适合决策。该 proxy eval 的尺度行为经过 OLMo 2 scaling models 检查。[html-eval; html-mixing]
3. **事实**：每 task 拟合 mixture weights → BPB 的 generalized linear model；搜索平均预测 BPB 最低的配比，加入 6T budget 与每 domain 约 4–7 次最大重复约束。[html-mixing]
4. **事实**：conditional mixing 将此前优化的 mix 冻结为一个 virtual domain，仅重新搜索新增/改动 sources 与旧 mix 的组合，减少昂贵的全空间重搜。[html-mixing]
5. **事实**：先在 DCLM-Baseline 研究 web topic mix；code-language mixing 那一轮固定 web 75% / Stack-Edu 25%，只优化语言构成；后续再整合 PDF。**75/25 是中间实验设置，不是 final source mix**。[html-mixing]
6. **事实**：topic weights 确定后再按 quality percentile 设置 upsampling curve；最多重复 7 次，不同 topic 的曲线满足 topic token budget，非全 corpus 同一 cutoff。[html-mixing]

**解释**：final ratios 是给定 eval objective、data pools、repeat constraints 下的 recipe choice，不是跨模型/跨规模的普适最优比例。报告展示 web topic mix 在 1B 模型上的收益，但不能因此假定所有 30M → 32B 的排序都保持。

### Midtraining mixing：单源 microanneal + 全 mix integration

1. **事实**：标准 microanneal 为 5B candidate tokens + 5B web tokens，和 10B web-only baseline 比较，分离数据收益与单纯继续训练的收益；部分小数据实验采用更短预算/不同占比。[html-mid-method]
2. **事实**：有希望的来源进入 100B candidate mix，保留此前强来源，做五轮主要 integration tests；不只评 base，还快速 SFT 后检查 post-trainability。[html-mid-method]
3. **事实**：偏 math/code/thinking 的 mix 与偏 QA 的 mix 有显著 tradeoffs；最终选择 balanced mix。加入 thinking/instruction 内容对 base eval 也有收益，但移除 chat template / special tokens，使用简单 newline formatting，正式 special-token behavior 留给 SFT。[html-mid-findings]
4. **事实**：Round 5 纳入 decontamination；报告发现 external instruction/synthetic datasets 可以包含整个 benchmark splits，过滤范围覆盖用于 eval 的各 splits。[html-mid-findings]
5. **事实**：32B 从同一 pretraining checkpoint 跑两个不同 data-order seeds 的 100B midtraining，再平均权重；7B 没有观察到相似收益，只用一个 run。[html-mid-findings; html-hparams]

### Proxy scale 与预测阶段：Olmix 配套方法论文补充

2026-10-07 回读 Olmix §3.3–3.4；它比 OLMo 3 TR 更具体地解释 search design，不能把 surrogate optimization 与真实训练混为一谈。

- **事实**：比较 1M / 15M / 30M / 60M proxies，各采用 5× Chinchilla token multiplier；相同 mixture 配对 1B / 100B-token target，测 average BPB 的 Spearman rank correlation。30M 得到约 0.896；1M 约 0.73；≥15M 的表现更可靠。这是测试场景内的经验选择，不是 universal scale-transfer guarantee。[olmix-swarm]
- **解释**：3B = 30M × 20 × 5（使用 Chinchilla-style 20 tokens/parameter heuristic）；这是相对 compute-optimal 基准的 overtraining budget，不是 5 epochs。参数规模选择有 ablation，5× multiplier 作为固定设置使用，不能声称 jointly 搜索得到了最优 30M/3B。
- **事实**：给不同 mixtures 训练多个同大小 LM，得到 mixture → per-task BPB 观测；每个 task 拟合 log-linear surrogate：f_i(p)=c_i+exp(A_i^T p)。Surrogate 本身是回归模型，不是另一个 teacher LM。[olmix-regression]
- **事实**：Olmix 比较从 swarm 选最优、不同 regression families 与不同 solver；推荐用 CVXPY 求解 convex predicted objective，含 KL(p||natural mix) penalty 及 finite-data repetition constraints。A.7 也描述 guided-search baseline：一轮最好的配比作为下一轮 Dirichlet prior。Search/prediction evaluation 不需要再训练 LM。[olmix-optimization]
- **事实**：无 KL 的 exact solver 最小化预测 BPB 最好，却不是实际 1B BPB 最好；λ=0.05 的 regularization 更好，说明代理误差和跨尺度误差确实存在。[olmix-optimization]
- **事实**：Olmix 的建议为至少 3(m+1) proxy runs（log-linear）；TR 的实际经验设置约 5× domains，两个表述分别是方法建议和项目 recipe。[olmix-swarm; html-mixing]
- **证据边界**：配套方法论文的直接 rank-transfer test 是到 1B；TR 另给 1B mixing validation，7B/32B 成品采用该 recipe 不等于已遍历多个 full-scale mixture 并证明全局最优。
- **解释**：最可迁移的是训练数据选择的相对方向，非精确预测大模型 capability score；更换 architecture、token/parameter ratio、data quality、eval target 均可能改变最优 mix。

## Lookup-only：实际数据配比与训练配置

以下为 **token share**，非 document/sample share；均按 TR tables 核验。

### Pretraining final mix（Table 4，5.93T）

| Source | Token share |
|---|---:|
| Common Crawl | 76.1% |
| olmOCR science PDFs | 13.6% |
| Stack-Edu | 6.89% |
| arXiv | 0.86% |
| FineMath 3+ | 2.56% |
| Wikipedia / Wikibooks | 0.04% |

**事实**：9.31T 是候选 pool，5.93T 是重采样后的 final training mix。7B 对 final mix 训练约一轮；32B 对该 mix 的 schedule 在 5.5T 提前截止，约 0.93 轮。高质量 documents 已在 mix 构建时重复，因此“一轮 final mix”不等于原始文档只见一次。[html-pre-mix; html-hparams; html-architecture]

### Midtraining final mix（Table 5，约 100B，按表中类别汇总）

| Category | Approx. token share |
|---|---:|
| HQ Common Crawl + STEM-heavy crawl + science PDFs | 32.5% |
| Code: Stack-Edu FIM + CraneCode | 20.0% |
| Synthetic math | 19.2% |
| Synthetic QA | 13.9% |
| Thinking traces | 8.3% |
| Instruction | 6.1% |

分类是本 note 对 Table 5 的汇总，精确 source-level shares 回原表；pool 2.19T 不代表训练 2.19T。[html-mid-mix]

### Base stage hyperparameters（Table 35 / Figure 4）

| Setting | 7B pretrain | 32B pretrain | 7B midtrain | 32B midtrain |
|---|---:|---:|---:|---:|
| Peak LR | 3e-4 | 6e-4 | 2.074e-4 | 2.071e-4 |
| Global batch tokens | 4,194,304 | 8,388,608 | 2,097,152 | 4,194,304 |
| Sequence length | 8,192 | 8,192 | 8,192 | 8,192 |
| LR warmup | 2,000 steps | 2,000 steps | 0 | 0 |
| Schedule | modified cosine | cosine, truncated | linear decay | linear decay |
| Final LR | 3e-5 | actual 6.210e-5 | 0 | 0 |
| Token budget per run | 5.93T | 5.5T | 100B | 100B |

- **事实**：32B pretraining Table 35 写目标 final LR 6e-5；Figure 4 注明提前截止后的实际值 6.210e-5，应保留这个区别。[html-hparams; html-architecture]
- **事实**：7B 的 cosine 原先按 5T 设计，后半段 stretch 到 final mix 一轮 5.93T；32B 以 5.93T cosine 为目标，实际在 5.5T 截止。[html-architecture]
- **事实**：32B 更高 peak LR 同时配合更大 batch；报告只说 larger batch 部分补偿这一差异，不能用此推出通用 LR scaling law。[html-architecture]
- **开放问题**：TR 说 base 大体继承 OLMo 2 hyperparameters；本轮回读没有找到这些 pretraining LR/batch 的完整 sweep 及 selection curve。最终配置公开 ≠ 每个超参如何选都有实验披露。Optimizer 的完整实现需另核官方 run configs，不由现代常规默认值反推。

## Gaps / Open Questions

- 本轮核验了处理 pipeline、Tables 4/5/35 和 §3.4–3.5 的实验选择逻辑；未逐份验证公开数据/训练日志或从代码重现配比。
- 原 macOS PDF 路径在本机不存在，本轮使用官方 HTML，未重验 PDF 页码。
- LR/batch 的最终值有证据，完整 hyperparameter search 的理由仍缺位。

## Evidence Anchors

- Source [html-web]: https://arxiv.org/html/2512.13961v2#S3.SS4.SSS1
- Source [html-sources]: https://arxiv.org/html/2512.13961v2#S3.SS4.SSS2
- Source [html-mixing]: https://arxiv.org/html/2512.13961v2#S3.SS4.SSS4
- Source [html-eval]: https://arxiv.org/html/2512.13961v2#S3.SS3.SSS2
- Source [html-pre-mix]: https://arxiv.org/html/2512.13961v2#S3.T4
- Source [html-mid-mix]: https://arxiv.org/html/2512.13961v2#S3.T5
- Source [html-mid-method]: https://arxiv.org/html/2512.13961v2#S3.SS5.SSS1
- Source [html-mid-findings]: https://arxiv.org/html/2512.13961v2#S3.SS5.SSS4
- Source [html-hparams]: https://arxiv.org/html/2512.13961v2#Ax2.T35
- Source [html-architecture]: https://arxiv.org/html/2512.13961v2#S3.SS2
- 原有 overview anchors：4–5；详细 sections：13–35；本轮以 HTML anchors 为准。

- Source [olmix-swarm]: https://arxiv.org/html/2602.12237#S3.SS3.SSS2
- Source [olmix-regression]: https://arxiv.org/html/2602.12237#S3.SS3.SSS3
- Source [olmix-optimization]: https://arxiv.org/html/2602.12237#S3.SS3.SSS4
