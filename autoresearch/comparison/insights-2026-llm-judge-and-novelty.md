# 26 年 Autoresearch SOTA Insights

> 从 12 张卡（measuring-gap 系 6 张 + 26 年新抽 6 张：hindsight / soundnessbench / beel / ai-sci-v2 / agent-lab / co-scientist）交叉综合出的方法学发现。事实 / 解释 / 猜测 / 开放问题分别标注。

## 主结论：LLM-Judge 是能力光谱，不是二元

**事实**：LLM 越靠近 execution 端的判断越准，越靠近 ideation / novelty / impact 端越差。原因是前者信号具体可核对（数字、citation、代码 bug）hard-to-fake，后者信号抽象 rhetoric-driven fake-able，且 LLM 训练偏好正好放大后者。

| 任务 | LLM 能不能做 | 证据 |
|---|---|---|
| pairwise 同档次质量比较 | 相对能 | 用户朋友经验、MT-Bench 类文献 |
| paper draft execution 层 review | 相对能 | Beel 2025 v1 reviewer 抓不到 bug 是 model+prompt 问题 |
| 成品 soundness（含 results） | 能到一定程度 | SoundnessBench GPT-5.4 Macro F1 69.7 |
| **proposal-only soundness** | **不能** | [[soundnessbench]] 74% FPR |
| **pointwise novelty score** | **不能** | [[hindsight-future-impact-eval]] ρ=-0.29 |
| 判未来 impact | **不能** | HindSight + FAME |

**推论**：任何把 LLM-Judge 分当 optimization target 的系统都是在**训 bullshit generator**——不是 mitigation 能救的架构问题。LLM-Judge 只该做 filter 不做 scorer。

## Same-source verifier 循环 + 三次打破

**机制**（解释）：LLM 生成 idea → LLM 判 idea 好不好，评判器和生成器共享同一套训练偏好，分数好看不代表 idea 真好。同源不指同模型，指**同类训练目标造出的偏好**——所有主流 LLM 都经历 next-token prediction on web + RLHF + CoT，都是众数估计器且系统性偏好 grand-but-vague。**换不同 model 自评救不了**（SoundnessBench 12 model 平均 74% FPR 是家族无关）。

**三次独立打破**（事实）：
| 打破方式 | 论文 | Ground truth | 关键数字 |
|---|---|---|---|
| 时间切片 | [[hindsight-future-impact-eval]] | 未来 30 月发表 + citation + venue | LLM novelty vs 真 impact ρ=-0.29 |
| 同期 human reviewer | [[soundnessbench]] | ICLR reviewer soundness sub-score | 12 model 平均 FPR 74%，scale up 反向 |
| 真实物理实验 | [[google-co-scientist]] | AML 体外细胞毒 / 肝纤维化 organoid / cf-PICI 独立重现 | 3 domain positive |

三条路径正交，共同结论：**LLM 自评系统性高估，且方向可预测（偏 novel-sounding 而非 anticipatory）**。

## Test-time compute scaling 需要非同源 selection signal

**事实**（表面矛盾）：Measuring-Gap 说 thinking mode 让 idea 分布更窄，Co-Scientist 说 test-time compute Elo 未饱和上升。

**解释**：两者测的不是同一件事。
- CoT / thinking = 单 call 内自我延伸，无外部反馈，是**放大 RLHF 收敛的众数估计器**
- Tournament + evolution = **计算 + selection 压力**，但只有 selection 来自外部 ground truth 时才真正 compound

**因此修正上一版 insight**：test-time compute 只有配上非同源 selection signal 才 scaling。同源 LLM-Judge 打分的 tree search / self-refine 只是搜索空间大但目标错（AI Sci v2 tree search 天花板由 SoundnessBench 揭示的 74% FPR evaluator 决定）。Co-Scientist 敢报未饱和是因为 wet-lab 兜底。Karpathy 5min execution loop 是同一件事：execution 是**免费外部 selection signal**。

**推论**：LLM 训练领域天然吃亏——反馈周期以小时/天计，且大部分工作被 LLM-Judge 评价。是 autoresearch 最差的 domain。

## Domain 决定天花板（不是方法）

**事实**：
- Biomed（Co-Scientist）：wet-lab in vitro 兜底 → 真进 physical ground truth
- ML paper（AI Sci v2）：ICBINB workshop 6.33/10 accept，依赖 human meta-select + workshop 特殊
- ML engineering（MLE-Bench 上 mle-solver）：Kaggle 明确 metric → 可直接测

**推论**：domain 里 ground truth 越近越硬，autoresearch 越有意义。ML 训练是最差的 domain。选 domain 比选方法更决定项目天花板。

## Fully autonomous 是叙事不是现实

**事实**：
- AI Sci v2 明面 fully autonomous，实际两层 human meta-selection（40 idea 挑 3 + 每 idea 多 seed 挑最好）
- Agent Lab 明说 copilot mode +0.75 quality，把 human involvement 视为 feature
- Co-Scientist 明确 scientist-in-the-loop 定位
- Beel 2025 audit v1：$15/paper claim 忽略 25h 人力

**推论**：26 年的诚实版本是"human 介入是必需，剩下的争论只是粒度和透明度"。任何声称 fully autonomous 且未量化 human effort 的系统读作 `human-in-the-loop-hidden`。

## LLM 不是厌恶 novelty，是分不出真 novelty 和 novel-sounding

**事实**（[[hindsight-future-impact-eval]] 四象限）：
- Hidden Gem（HindSight 高 / LLM-Judge 低）：23% RA idea——**技术具体 idea 被判 incremental**
- Overhyped（LLM-Judge 高 / HindSight 零）：26% RA / 34% BL——**"grand but vague"（holistic framework / unified approach）**

**解释**：LLM 的 novelty 概念被 "grand but vague" rhetoric 拟合，与真 anticipatory 反向。这个错分模式比"厌恶 novelty"更糟——它会 push 生成器往 novel-sounding 方向走，若拿 LLM-Judge 当 RL reward 训 idea 生成器，训出的是**更会说大话的 bullshit generator**。

## 若一定要用 LLM 判 novelty 的 mitigation 组合

**不是让它变准，是让它少犯系统性错误**：

1. **pairwise 替代 pointwise**：最大蛋糕，消除开放尺度飘 + verbosity/self-preference bias
2. **不裸判，加 grounding**：retrieval augmentation / knowledge graph relational context / time-split 匹配已发表——把 novelty 判断转化为 similarity 匹配（execution 端任务）
3. **多 backbone panel + 只信一致票**：GPT / Claude / Gemini / open-source 家族偏好虽重合但不同；**分歧本身是尾部 idea 的 proxy**，flip 直觉——分歧不是噪声是创新性信号
4. **prompt 显式对抗 novel-sounding**：判定"holistic / unified / principled" abstract 表述扣分，要求 justification 必须引具体 mechanism / dataset / experiment design（会误伤真 revolutionary，故意的——宁可漏也别被 gaming）
5. **execution 端做辅助 filter**：先判 feasibility，novel + not feasible 直接淘汰（砍掉 HindSight overhyped 象限），保留 hidden gem
6. **calibration set**：用已知 impact 的老 idea 定期跑 judge 配置，量化 drift；没做 calibration 就上 LLM-Judge = 用没校准的秤称重

**架构立场**：LLM-Judge 可以进 filtering / diversity 保底 / similarity 匹配；**不能进 RL reward / 单点排名 / 主推荐排序**。

## Recursive feedback loop（长期风险，猜测）

Sourati 2026 明说：用户用 LLM 写作 → 输出被训进下一代 → 长期同质化加速。**对 autoresearch 特别危险**：如果社区大规模用 LLM 生成 idea，几年后训练数据里 grand-but-vague idea 密度会显著升高，下一代 LLM 更加分不出真 novelty vs novel-sounding。**是一个 self-reinforcing 陷阱**。开放问题：有没有可测量的 proxy 追踪这个 drift？

## 开放问题

1. HindSight 30 个月窗口偏短，慢发酵领域被截尾——如何延长又保留统计功效？
2. Co-Scientist 只 3 wet-lab case，未 report hit rate 分布——**failure 分布未公开**是本项目最缺的 metric
3. AI Sci v2 未被 Beel-style 独立 audit——v1 的 42% code fail、8%/iter change、5 citation 中位数在 v2 是多少？
4. Agent Lab copilot mode human effort 未量化——真实 human hour/paper 对比 v1 v2 差多少？
5. LLM-Judge 光谱上"execution 端相对准"的具体边界在哪？pairwise 同档次 quality 判断能到多准？需要 calibration set 量化
6. 分歧作为创新性 proxy 假设是否成立？需要实证：多 backbone 分歧 idea 是否在 HindSight 时间切片上比一致 idea 得分更高？

## 相关卡

- [[measuring-gap-human-llm-research-ideas]] — 项目锚论文，taste-gap 分布评法
- [[can-llms-generate-novel-research-ideas]] — Si 2025a 人类 100+ NLP 研究员
- [[ideation-execution-gap]] — Si 2025b execution 后 idea 分数崩
- [[the-ai-scientist]] — v1 canonical anchor
- [[ai-scientist-v2]] — v2 tree search + VLM
- [[agent-laboratory]] — auto reviewer vs human 落差 2.3 分
- [[google-co-scientist]] — wet-lab 兜底 verifier
- [[beel-2025-audit-ai-scientist]] — 唯一 independent audit
- [[hindsight-future-impact-eval]] — 时间切片
- [[soundnessbench]] — pre-exec soundness + 74% FPR + scale 反向
- [[ai-can-learn-scientific-taste]] — measuring-gap 对立命题
- [[homogenizing-effect-of-llms]] — 上位理论 + recursive feedback loop
