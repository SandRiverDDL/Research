---
title: SoundnessBench - Can Your AI Scientist Really Tell Good Research Ideas from Bad Ones?
year: 2026
venue: arxiv
paper_type: benchmark-eval
lifecycle_role: critique-anchor
boundary_risk: eval

failure_modes: [verifier-blind-spot, reviewer-model-hacking, weak-experimental-design, metric-selection-bias, cherry-picked-showcase]
design_knobs: [evaluation-protocol, evaluation-scope, evaluation-judge, verifier-type, novelty-check]
---

## 一句话定位

pre-execution methodological soundness 评测：LLM 作 first-gate reviewer 有 74% FPR，scale up 反而更乐观。

## 难题 / Failure Modes

| Failure mode | 本文诊断 | 本文处理方式 | 仍未解决 |
|---|---|---|---|
| `verifier-blind-spot` | 12 model 平均把 74% 低质量 proposal 判为 high soundness [Table 2, Fig 3] | 提出 pre-exec soundness benchmark，1099 例 ICLR proposal + reviewer label | 只测 first-gate；实际 pipeline 里 verifier 还有 execution/review 两层未合起来评 |
| `reviewer-model-hacking` | AI Scientist v1/v2 类 pipeline 都用同类 LLM 做 automated reviewer——若 base LLM 有 74% FPR，reviewer 自然会通过烂 idea | 用真实 ICLR reviewer soundness score 作 external label | ICLR reviewer 本身有噪，用 std<0.15 的 agreement filter 只是缓解 |
| `weak-experimental-design` | 定义 low-soundness 涵盖 improper baseline / data leakage / mismatched metric——这些是 autoresearch pipeline 高发失败模式 | Reviewer 已识别过一次，本 bench 只是暴露 LLM 复识别能力弱 | 未测 idea 生成时是否会自我引入这些 flaw |
| `metric-selection-bias` | Aggressive prompt 把 Low R 拉到 80% 但 High R 崩到 36%，Macro F1 反降；单独 report Low R 会误导 | 强制 report 双向 recall + Macro F1 [Table 2] | 未提供综合校准 metric |
| `cherry-picked-showcase` | 相同模型家族 Qwen3.5 2B→122B：scale up 后 permissive 加强（Low R 31%→19%）[Fig 4] | 六个 size 同族对照 | 只跨一个 open family，闭源 scale-vs-behavior 未覆盖 |

## 方法机制

- **Benchmark 建构五步** [§2]：ICLR 2022-2026 抓 35k submission + 138k review → 用 reviewer confidence≥3 + soundness std<0.15 高一致度筛 → 用 reviewer soundness sub-score 打 label（≥3 high、≤2 low、中间去）→ Gemini 2.5 Pro 抠 near-verbatim proposal（去 result / acceptance cue，防 leakage）→ atomic-claim + BM25 audit（τ=0.7，保留 66.93%）→ 1099 例（458 low / 641 high，16 subfield）。
- **评测协议** [§3.1]：LLM 看 results-masked proposal，二分类 high/low + 给 justification；两种 prompt：standard（无 prior）vs aggressive（默认拒绝，除非明显强）。
- **核心发现** [§3.2, Table 2]：Standard prompt 下 mean FPR 74% / High R 91.8%；9/12 model 把 >70% low-soundness 判成 high。Aggressive prompt 把 mean Low R 拉到 80.1% 但 High R 崩到 36.1%，Macro F1 反降至 49.3。**calibration 不稳**——prompt 一变，错误从 FP 换成 FN，没有真判断力。
- **Scale 反向** [§3.2, Fig 4]：同 Qwen3.5 家族 2B→122B，standard 下 High R 提升但 Low R 反降；aggressive 下无系统改善。
- **Contamination controls** [§3.3]：ICLR 2026-only split（含训练 cutoff 后数据）optimism bias 仍稳；identifier removal / surface feature / adversarial injection 均不改主结论。

## 相对方法

| 对比对象 | 对方问题 | 本文改动 | 代价 / 风险 |
|---|---|---|---|
| MLE-Bench / PaperBench / InnovatorBench | 只测 execution outcome，绕过 first-gate 判断 | 专测 pre-exec proposal 是否 sound | 不评能否落地成功、只评是否**该开始** |
| Si 2024 / RINoBench | pre-exec 但测 **novelty** | 换成 **soundness**——methodological 而非新颖性 | 未整合两者，实际 pipeline 需要综合 |
| HindSight / Tong 2026 | post-hoc，用未来 citation 做 ground truth | 用同期 reviewer 的 soundness 作 label | 依赖 reviewer 判断可靠性；proposal-only 让 model 缺 results 参照 |
| AI Scientist v1/v2 auto-reviewer | 用同源 LLM 做 reviewer，声称与人类 near-human | 揭示 base LLM 有 74% FPR，automated reviewer 结构不成立 | 未直接测 AI Scientist 的 reviewer，只测 base model |

## 设计决策 / Design Knobs

| Design knob | 本文选择 | 常见替代选择 |
|---|---|---|
| `evaluation-protocol` | Pre-exec binary classification + reviewer-agreement label | Post-exec outcome / peer-review score prediction |
| `evaluation-scope` | Proposal-only（去 results 和 acceptance cue） | Full paper / execution outcome |
| `evaluation-judge` | LLM classifier（被评对象） vs ICLR reviewer sub-score（label） | LLM-as-Judge / expert rubric |
| `verifier-type` | Reviewer-derived label + atomic-claim audit for extraction fidelity | Human panel / execution-check / hybrid |
| `novelty-check` | 不测（本 bench 与 novelty 正交，专测 methodological soundness） | LLM 判 / embedding 相似 |

## 方法优缺点 / 适用边界

- 优势：
  - 首个 pre-exec methodological soundness benchmark，1099 例远超此前小规模 human study；label 来自真 ICLR reviewer，evidence tier 高于 LLM-Judge。
  - Furong Huang 组 + UMD，可信度档次高于单作者 arxiv；数据集 HF 开源，pipeline 完全 transparent。
  - 揭示 **calibration 不稳** + **scale 反向**——不是简单的"更大模型更好"，直接打脸 AI Scientist v1/v2 类的 automated reviewer 结构。
  - Contamination 控制做得干净（ICLR 2026-only、identifier removal、adversarial injection 三方面），主结论不因单一 artifact 崩掉。
- 不足 / 风险：
  - Reviewer soundness 是 proxy 不是 ground truth，ICLR reviewer 本身有噪；作者也承认 recoverable proposal-stage 而非绝对 validity。
  - Proposal-only：LLM 看到的信息比原 reviewer 少（无 results），可能低估其潜在能力（虽然这正是 first-gate 场景真实约束）。
  - Prompt 空间只探 2 个（standard / aggressive），未测 CoT / consistency / multi-agent debate 等 mitigation。
  - 仍是自报 metric（非 independent audit）；但 label 来源比 LLM-Judge 高一档，介于 self-report 和 audit 之间。
  - Domain 限 ML/CS，跨学科 soundness 未覆盖。

<!-- meta:
authors: [Sy-Tuyen Ho, Minghui Liu, Huy Nghiem, Furong Huang]
url: https://arxiv.org/abs/2605.30329
arxiv_id: 2605.30329
pdf: null
brief: _meta/briefs/papers/2605.30329.md
survey: arxiv-search-2026-idea-eval
-->
