# ResearchStudio-Idea：evaluation 与个人采用判断

> 返回 [overview.md](overview.md)。评价证据以论文 [§14–§15, pp. 36–40](../../papers/researchstudio-idea-2607.04439.pdf) 和固定 commit 的 [evaluation protocol](https://github.com/microsoft/ResearchStudio/blob/298ca64ae5e3f242d58278601db34bfa6daa53b8/ResearchStudio-Idea/evaluation/README.md) 为主。

## 1. 官方评价协议

**事实**：benchmark 有 100 个 prompts，每个从一篇 ICLR 2026 Oral 的 **title only** 改写：保留 domain object/task，移除显式 method suffix，不用 abstract-derived bottleneck。每个 seed 保存 original title/OpenReview ID 与 leakage-risk notes。[evaluation README](https://github.com/microsoft/ResearchStudio/blob/298ca64ae5e3f242d58278601db34bfa6daa53b8/ResearchStudio-Idea/evaluation/README.md)；[seed file](https://github.com/microsoft/ResearchStudio/blob/298ca64ae5e3f242d58278601db34bfa6daa53b8/ResearchStudio-Idea/evaluation/iclr2026_oral_problem_seeds_formal_100.jsonl)

**事实**：每个 seed 比较四个系统：IdeaSpark on Opus 4.8、Opus 4.8 bare、Opus 4.8 self-generated、GPT-5.5 bare。质量由 `idea-quality` skill 对 Title/Motivation/Method 的 problem position、method quality、problem–method fit 打分/盲 pairwise；novelty 由 `scoop-check` 对 prior-art overlap 分五级。官方 headline 是 IdeaSpark mean quality 3.87/4、100 个中赢 88 个，同时 novelty 保持竞争力。[论文 pp. 36–39, §14](../../papers/researchstudio-idea-2607.04439.pdf)；[idea-quality skill](https://github.com/microsoft/ResearchStudio/blob/298ca64ae5e3f242d58278601db34bfa6daa53b8/ResearchStudio-Idea/evaluation/idea_quality/SKILL.md)

## 2. 为什么这还不能证明 scientific SOTA

### LLM judge 与同源优化

**事实**：质量与 novelty 都由 LLM-based skills 自动判断；没有 human domain-expert blind study，也没有执行 idea、复现实验或真实 peer-review outcome。论文在 limitations 中承认 automated judges、seed construction、contamination 与 execution validation 的限制。[论文 pp. 39–40, §15](../../papers/researchstudio-idea-2607.04439.pdf)

**判断**：系统的输出格式、审计语言和 judge rubric 共享“reviewer-defensible idea card”偏好，存在 evaluator affinity。即使 judge blind，也可能奖励更完整、更具体、更符合 rubric 的文案，而不是真正更可能产生新科学。

### baseline 公平性

**解释**：IdeaSpark 获得 live retrieval、1,947-paper-induced cards、多阶段大 token budget、fresh contexts 与多次 audit；bare baselines 的计算与工具预算明显更小。这个比较回答的是“完整 harness 是否胜过一次裸模型调用”，不是“pattern induction 在 compute-matched 条件下的独立因果增益”。最关键的 ablation 应包括：

- 同检索、同 token、同 audit，但去掉 induced patterns；
- 手写 generic patterns vs induced patterns；
- accepted-only vs accepted+reject cards；
- single-pattern vs composition；
- coherence/collision gates 的逐项移除。

论文有内部 ablations，但未形成第三方、compute-matched、human-evaluated benchmark。

### leakage 与时间问题

**事实**：seed 来自已公开 Oral title；frontier models 可能见过 title 或相关 discussion。作者只使用 title 改写、记录 leakage risk，能降低直接抄 method 的风险，但无法证明 parametric contamination 为零。live retrieval 也不是 backdated 到 idea 产生时点。[论文 §14–§15](../../papers/researchstudio-idea-2607.04439.pdf)

## 3. “operational frontier” 与 “scientific SOTA”

**判断**：截至 2026-07-22，可称它为 **open, general-purpose, idea-only systems 的 operational frontier candidate**：源码活跃、流程完整、artifact/gate 细、安装到主流 agent host，且有公开 evaluation fixtures。

不能称为 established scientific SOTA，因为缺：

- 独立团队复现；
- 人类专家盲评与 inter-rater agreement；
- compute-matched baselines；
- idea → implementation → result 的 longitudinal success rate；
- taxonomy/quality 在版本和模型变化下的 stability。

GitHub stars、Microsoft affiliation 和 automated score 都是可信度线索，不是科学结论。

## 4. 与本项目 L1/cards/failure-mode 系统的关系

### 不应该替代 cards

**判断**：现有 L1 cards 是长期 research index，负责“哪些系统/论文提供了什么证据”；IdeaSpark 是一次运行时 operator，负责“围绕当前问题从证据编译一个 candidate”。前者提供可积累、可横向比较的记忆，后者提供生成纪律。用 IdeaSpark 替代 cards，会把知识交给每次检索的短窗口与作者 taxonomy；用 cards 替代 IdeaSpark，则缺少从证据到候选的显式转换过程。

### failure mode 是否太狭窄

**解释**：现有 failure-mode taxonomy 主要描述坏结果，适合 audit；要做 idea generation，还需要两个正交维度：

1. `bottleneck`：为什么系统在这个点受限的因果假说；
2. `design operator/pattern`：对这个约束施加什么结构变换。

因此不是放弃 failure modes，而是形成：

```text
evidence → observed failure mode → causal bottleneck hypothesis
         → design operator(s) → candidate → non-source verifier
```

## 5. 值得吸收的部分

- 将广泛 cards/论文池作为 Phase 0 的长期上游，而不是每次只靠新搜 40–60 篇；对当前问题仍需窄检索验证 freshness。
- 给每个 idea 强制写 `bottleneck evidence`、`operator chain`、`strongest naive baseline`、`falsification/kill switch`。
- generation 与 coherence/audit 分上下文；blocking evidence 用文件传递，避免同一模型自我辩护。
- novelty 检索拆为 topic search 与 candidate-specific signature/alias collision search。
- retry 只在得到新反例/新约束时发生；否则停止，不批量重抽同质 idea。
- 把 pattern 当可编辑 operator library，记录来自哪些成功/失败 cases，而不是只让 prompt 自由生成。

## 6. 不应照搬的部分

- 不把 15 patterns 当封闭 ontology；允许 `unknown/new operator`。
- 不把 40–45 records 当 bottleneck 已充分覆盖；优先接入已有 cards、citation graph 和经典 ancestor papers。
- 不用同一类 LLM judge 分数做 idea 主排序或 optimization target；本项目已有稳定规则是 “filter, not scorer”。
- 不追求一次跑完的长 token 流程作为默认；先按风险启用 retrieval、coherence、collision 三个最值钱的 gate。
- 不把 idea card 的“看起来可实现”当实验可行；应交给下游 execution/assurance layer。

## 7. 推荐的个人接入形态

**判断**：采用“保留自己的系统，吸收它的 operator layer”，而不是二选一：

1. 本项目 cards/comparisons 提供 broad evidence memory；
2. 针对一个方向做 freshness retrieval 和 bottleneck reconstruction；
3. 复用/改写 pattern composition、coherence trace、dual-channel collision；
4. 人选 idea，不让 LLM score 决定主推荐；
5. 交给实验 harness，使用 raw execution evidence 更新 bottleneck/failure-mode/cards。

**开放问题**：在个人流程中最先应实测的是“pattern layer 是否比同检索同审计、但无 pattern 的 prompt 更好”。如果不能在 10–20 个自己熟悉的方向上由盲人评审稳定区分，就没理由承担完整流程成本。

