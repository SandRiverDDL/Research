# Autoresearch Decisions

> Stable decisions go here. Temporary state belongs in `STATE.md`.

## 2026-07-14 — 建立 Autoresearch 项目

Decision: 基于 `doc/research-project-template/` 新建 `autoresearch/` 主题目录，研究"自动化科研系统的机制、缺陷、评测与改进"。

Reason: 用户希望有一个独立主题追踪 AI-for-research pipeline 本身（不是 AI 用来做别的研究），涵盖端到端 autoresearch agent、子任务系统、评测、critique 与改进方向。命名与 `autoresearch` skill 相同但语义正交（一个是研究主题，一个是 legacy pipeline skill），在 AGENTS.md 顶部显式说明避免混淆。

Impact:
- 邻近项目分工写入 boundary：`agentic-rl/`、`agent-data/`、`foundation-model-systems/` 各守 core mechanism。
- 新增 `critique-audit` / `position` 两个 paper_type 以及 `critique-anchor` lifecycle_role，`evidence-tier-mixing` failure mode，反映"三档证据"纪律。
- Pilot 目标：先建 3-5 张 L1 卡压 taxonomy，不急扩规模。

## 2026-07-14 — 按 paper_type 分档设置时效 cutoff

Decision: Time / Venue Gate 从"2023 之后优先 + 一刀切"改为按 `paper_type` 分档 cutoff：`core-method` 约 12 个月、`benchmark-eval` 约 18 个月、`critique-audit` / `position` / `survey` 不设 cutoff、`background` / `adjacent` 约 24 个月。超期 `core-method` 仅在 canonical anchor 或 critique target 情况下例外保留。

Reason: autoresearch 方法迭代极快（AI Scientist v1 → v2 → Agent Laboratory 类系统在 12-18 个月内迭代整代），一年前的方法通常已被后续吸收。但**分析类工作**（critique / position / failure-mode audit）的类型变化远慢——2024 年发现的 LLM ideation 偏 bridging，2026 年仍在。评测基础设施居中。一刀切 cutoff 要么砍太狠（丢批判背景），要么砍不动（塞方法陈货）。

Impact:
- 触发本次批处理时的筛选：从 `notes/measuring-gap-human-llm-research-ideas.md` 的 related work 抽出的 13 个候选中砍掉 8+ 篇过时 `core-method`（Meincke 2024、SciMON、Nova、SciAgents、Gu 2024、ResearchAgent、Su 2025、Pu 2025、Sanyal 2025、Garikaparthi 2025、Vasu 2025、Smith 2025），保留 10 篇（其中 Lu 2024、Boiko 2023、Si 2025a 作为 canonical anchor 例外）。
- 未来 recall 时按 paper_type 直接查表，减少 case-by-case 争论。
- `lifecycle_role: canonical-anchor` 现在是**硬信号**：不打这个标签的老 core-method 一律砍。

## 2026-07-15 — LLM-Judge 使用规则：能做 filter 不做 scorer

Decision: 本项目内**任何 LLM-Judge 分数不进 optimization target / RL reward / 单点排名 / 主推荐排序**。LLM-Judge 仅可用作 filtering、diversity 保底、similarity 匹配。判 novelty 时强制走 mitigation 组合：pairwise 替代 pointwise + retrieval grounding + 多 backbone panel + 分歧作为尾部 idea signal + prompt 对抗 novel-sounding + execution 端做辅助 filter + calibration set 量化 drift。

Reason: 从 [[hindsight-future-impact-eval]] (ρ=-0.29 LLM novelty vs 真 impact) + [[soundnessbench]] (12 model 平均 FPR 74%，scale up 反向 permissive) + [[agent-laboratory]] (auto reviewer 6.1 vs human 3.8 落差 2.3 分) 三条正交证据得出结论：LLM 判 pointwise novelty / impact / proposal-only soundness 系统性偏 grand-but-vague，方向可预测。任何把这个分数当 optimization target 的系统会**训 bullshit generator**——不是 mitigation 能救的架构问题。同源问题不因换 model 家族缓解（74% FPR 跨 GPT/Claude/Gemini/Qwen/Llama 一致）。

Impact:
- 新建 [[insights-2026-llm-judge-and-novelty]] 记录 LLM-Judge 能力光谱、三次打破、mitigation 组合详情
- 未来 idea generation / verifier 设计的 acceptance rule 补条：verifier 来源必须标 evidence tier（self-report / third-party / audit），reward signal 必须非同源
- 引申 architectural 立场：test-time compute scaling 只在有非同源 selection signal 时才 compound（Co-Scientist wet-lab / Karpathy execution loop 兜底），CoT / thinking mode / self-refine / same-source tree search 会加剧 taste 收敛
- Domain 选择比方法选择更决定项目天花板：ML 训练是最差 domain（反馈周期长 + 大部分工作被 LLM-Judge 评价）

## 2026-07-15 — LLM-Judge 使用规则：能做 filter 不做 scorer

Decision: 本项目内**任何 LLM-Judge 分数不进 optimization target / RL reward / 单点排名 / 主推荐排序**。LLM-Judge 仅可用作 filtering、diversity 保底、similarity 匹配。判 novelty 时强制走 mitigation 组合：pairwise 替代 pointwise + retrieval grounding + 多 backbone panel + 分歧作为尾部 idea signal + prompt 对抗 novel-sounding + execution 端做辅助 filter + calibration set 量化 drift。

Reason: 从 [[hindsight-future-impact-eval]] (ρ=-0.29 LLM novelty vs 真 impact) + [[soundnessbench]] (12 model 平均 FPR 74%，scale up 反向 permissive) + [[agent-laboratory]] (auto reviewer 6.1 vs human 3.8 落差 2.3 分) 三条正交证据得出结论：LLM 判 pointwise novelty / impact / proposal-only soundness 系统性偏 grand-but-vague，方向可预测。任何把这个分数当 optimization target 的系统会**训 bullshit generator**——不是 mitigation 能救的架构问题。同源问题不因换 model 家族缓解（74% FPR 跨 GPT/Claude/Gemini/Qwen/Llama 一致）。

Impact:
- 新建 [[insights-2026-llm-judge-and-novelty]] 记录 LLM-Judge 能力光谱、三次打破、mitigation 组合详情
- 未来 idea generation / verifier 设计的 acceptance rule 补条：verifier 来源必须标 evidence tier（self-report / third-party / audit），reward signal 必须非同源
- 引申 architectural 立场：test-time compute scaling 只在有非同源 selection signal 时才 compound（Co-Scientist wet-lab / Karpathy execution loop 兜底），CoT / thinking mode / self-refine / same-source tree search 会加剧 taste 收敛
- Domain 选择比方法选择更决定项目天花板：ML 训练是最差 domain（反馈周期长 + 大部分工作被 LLM-Judge 评价）

## 2026-07-22 — Open-source system 使用 nested source dossier

Decision: 对需要同时记录机制、源码实现、运行方式、评价证据与采用判断的开源系统，使用 `notes/<system-slug>/` 作为 source dossier；`overview.md` 是唯一入口。nested notes 不属于正式 L1，不进入 card count，也不再增加 `notes/dossiers/` 中间层或同名 root-level L1。

Reason: 单张 L1 适合做 research index，无法在不膨胀 schema 的情况下承载系统级源码审计；而额外 `dossiers/` 层只增加导航成本。按 source 直接建目录既保留一处入口，也让机制子问题能局部展开。

Impact:
- 首批采用该契约的对象是 `notes/aris/` 与 `notes/researchstudio-idea/`。
- 现有 validator 只校验 `notes/*.md`；nested dossier 应保持被忽略，不修改 queue、taxonomy 或 validator。
- dossier 内仍遵守事实/解释/判断/开放问题标注与 source anchor 纪律，但不套 L1 frontmatter/card schema。
