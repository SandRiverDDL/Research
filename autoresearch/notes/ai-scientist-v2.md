---
title: The AI Scientist-v2 - Workshop-Level Automated Scientific Discovery via Agentic Tree Search
year: 2025
venue: arxiv
paper_type: core-method
lifecycle_role: canonical-anchor
boundary_risk: none

failure_modes: [hallucinated-novelty, citation-fabrication, weak-experimental-design, human-in-the-loop-hidden, cherry-picked-showcase, reviewer-model-hacking, verifier-blind-spot]
design_knobs: [pipeline-scope, stage-decomposition, iteration-control, agent-role-organization, verifier-type, novelty-check, human-intervention-point, reproducibility-artifact]
---

## 一句话定位

v1 的直接迭代：agentic tree search + VLM reviewer + 多 seed replication，产出第一篇 workshop peer-review 通过的 AI 论文。

## 难题 / Failure Modes

| Failure mode | 本文诊断 | 本文处理方式 | 仍未解决 |
|---|---|---|---|
| `hallucinated-novelty` | 作者内部审计明说"citation hallucination inaccuracies"仍普遍存在 [§4] | Semantic Scholar in-the-loop novelty check 从 post-hoc 提前到 idea generation 阶段 [§3.1] | 未定量报告 hallucination 率；Beel 2025 对 v1 揭穿的 keyword-match novelty check 是否在 v2 修复未 ablation |
| `citation-fabrication` | 作者自认为 unresolved [§4] | VLM 检 figure/caption 对齐 + o1 reflection stage | 未量化改善程度；无独立 audit |
| `weak-experimental-design` | 作者承认 "lacked methodological rigor and in-depth analysis, none met top-tier main-track conference quality" [§4] | Tree search + ablation stage + replication node 多 seed | ICBINB workshop 特殊（欢迎 negative result），主 track 上未测 |
| `human-in-the-loop-hidden` | 声称"fully autonomous"，实际两层 human meta-selection：40 idea 挑 3 + 每 idea 多 seed 各出一份 manuscript 挑最好 [§4.2] | 承认存在 "meta-selection"，坚称单 run 内无人编辑 | 端到端 acceptance rate（若只跑单 seed 单 idea）未 report |
| `cherry-picked-showcase` | 只 report 3/3 中最好那 1 篇；两次筛选后 report top-of-tail | 明说 post-review withdrawal 避免入正式记录 | 未 report distribution：多少 seed run 才出一份 workshop-worthy |
| `reviewer-model-hacking` | Tree search 的 LLM evaluator 与生成器仍同源（都靠 LLM 判 node 好坏） | 引入 VLM 做 figure/caption 检查，异构一部分 | 主 evaluator + reviewer 仍是 LLM，SoundnessBench 说这类 first-gate 有 74% FPR |
| `verifier-blind-spot` | 内部审计说 "citation hallucination" 和 "缺 rigor" 未被系统内部 reviewer 拦截 | VLM 检图但不检语义 | 与 Beel 揭示的 v1 reviewer 盲区同源 |

## 方法机制

- **Idea generation 提前抽象化** [§3.1]：从 workshop theme prompt 开始，非从 code base；Semantic Scholar in-loop novelty check（v1 是 post-hoc keyword match）。
- **4 stage + Experiment Progress Manager Agent** [§3.2.1]：Preliminary Investigation → Hyperparameter Tuning → Research Agenda Execution → Ablation Studies；每 stage 有显式 stopping criteria；stage 结束后 launch 多 replication 拿 mean±std。
- **Parallel Agentic Tree Search** [§3.2.2]：每 node = 代码执行结果 + 状态 (buggy/non-buggy)；每 iteration 并行 expand 多 node；一定概率选 buggy 做 debug，否则 best-first 靠 LLM evaluator 判 (metric + training dynamics + plot 质量)；特殊 node：hyperparameter / ablation / replication / aggregation。
- **VLM feedback** [§3.4]：experiment 阶段检 figure accuracy；writing 阶段检 figure-caption 对齐 + legend/label 清晰度 + main text vs appendix 重复。
- **Writing** [§3]：抛弃 v1 的 Aider incremental，改 single-pass + o1 reflection stage 检 hallucination/length。
- **Evaluation** [§4]：3 篇提交 ICLR 2025 ICBINB workshop（43 总投稿），reviewer 知情有 AI paper 但不知具体是哪几篇；1/3 得 6/6/7 = 6.33（top 45% 达 accept 门槛）；post-review withdrawal。

## 相对方法

| 对比对象 | 对方问题 | 本文改动 | 代价 / 风险 |
|---|---|---|---|
| AI Scientist v1 (Lu 2024) | 依赖 human template + linear experimentation + Aider iterative writing + 自评 reviewer | 去 template + tree search + o1 reflection + VLM figure check + 提交真 peer review | 未与 v1 定量对比（fail rate、char/iter、citation freshness） |
| AIDE (Jiang 2025, MLEBench) | 只做 ML engineering 单目标 tree search | 扩到多 stage scientific workflow 且引入 replication node | 承担了 workflow 复杂度但 evaluator 仍 LLM 单源 |
| Reflexion (Shinn 2024) | 迭代反思但线性 | Tree 结构允许 dead-end abandon 和 parallel branch | 计算开销 + evaluator 一致性挑战 |
| Beel 2025 audit (v1) | 揭示 v1 有 42% code fail + 8%/iter char change + citation 过时 | 本文声称多项改进 | v2 未被独立 audit，改进是否真实存在只靠 self-report |

## 设计决策 / Design Knobs

| Design knob | 本文选择 | 常见替代选择 |
|---|---|---|
| `pipeline-scope` | End-to-end (idea → code → exp → viz → write → review) | 单子任务 |
| `stage-decomposition` | 4 显式 stage + tree search within stage | Linear iterations / DAG |
| `iteration-control` | Stage-specific stopping criteria + compute budget | Fixed rounds |
| `agent-role-organization` | 单一 experiment manager + 多类 node 特化 | Multi-agent role split |
| `verifier-type` | LLM evaluator (node 选择) + VLM (figure check) + o1 (reflection) | Human-in-the-loop / execution-check |
| `novelty-check` | Semantic Scholar in-loop during idea generation | Post-hoc / embedding |
| `human-intervention-point` | Idea 层面 meta-selection + 多 seed 结果层面 meta-selection（未标为 intervention） | 明确 gate 或全自动 |
| `reproducibility-artifact` | 开源 code + 生成 manuscript 附录 | Prompts only |

## 方法优缺点 / 适用边界

- 优势：
  - **canonical-anchor 例外保留**：first AI-generated peer-review-accepted workshop paper 是命名事件，后续 end-to-end 系统都会引用它作 baseline。
  - Tree search + 多 seed replication + VLM 图检 相对 v1 是明确结构性改进（不只是换模型）。
  - ICBINB 是**外部** peer review，比 v1 全内部 automated reviewer 高一档 evidence（虽然工作坊接受 negative result 让门槛降）。
  - 开源代码，方便复现和 audit。
- 不足 / 风险：
  - **两层 human meta-selection**（40 idea 挑 3 + 每 idea 多 seed 挑最好）让 "fully autonomous" claim 只在单 run 内成立；端到端 acceptance rate 未 report → 落入 v1 同款 `cherry-picked-showcase`。
  - 与 v1 无定量对比：Beel 2025 报的 5/12 code fail、8%/iter change、median 5 citation/paper 等具体 metric 在 v2 未 re-measure。
  - 主 evaluator + 主 reviewer 仍是 LLM 单源，`reviewer-model-hacking` / `verifier-blind-spot` 结构未变；SoundnessBench 揭示的 74% FPR 直接威胁 tree search 的 node 选择合理性。
  - ICBINB workshop 特殊（欢迎 negative result + accept rate 相对宽），主 track 或普通 workshop 上性能未验证。
  - 内部审计仅由作者做，未 independent audit；v2 版本目前**没有** Beel-style 独立复现——本项目一个开放缺口。

<!-- meta:
authors: [Yutaro Yamada, Robert Tjarko Lange, Cong Lu, Shengran Hu, Chris Lu, Jakob Foerster, Jeff Clune, David Ha]
url: https://arxiv.org/abs/2504.08066
arxiv_id: 2504.08066
pdf: null
brief: _meta/briefs/papers/2504.08066.md
survey: measuring-gap-RW + queue-add
-->
