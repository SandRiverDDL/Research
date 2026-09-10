# Agentic RL 决策记录

## 2026-06-16 — Agentic RL 独立于 Agent Data

决策：Agentic RL 单独维护在 `/Users/chy/Research/agentic-rl/`。Agent Data 只收 data mechanism；本项目收 RL learning loop。

原因：Agentic RL 体量接近 OPD，社区类目更明确，包含 reward、policy update、environment interaction、credit assignment、exploration 等独立问题。

影响：两个会话可以并行抽卡，但不得混用 notes。混合论文可以双登记，各写一个视角。

## 2026-06-16 — Queue 宽、Card 准入用简单外部证据

决策：放弃“LLM 自己判断重要性”的严格机制 gate。新规则是：queue 宽，card 用简单硬信号。

规则：

- survey 正文提到 + 开源代码/环境 + 顶会/TMLR/COLM/ACL/EMNLP/NeurIPS/ICML/ICLR 等强出处：直接下载并写 L1 card。
- survey 正文提到 + arXiv + 官方开源 + 明确 RL mechanism：走 arXiv exception，可写 L1 card。
- survey 正文提到但缺 venue 或缺 code：进入 queue，不立即抽卡。
- reference-only、prompt-only、benchmark-only、generic agent framework：默认忽略或 background。

原因：survey mention 是 recall 信号，不是 importance 信号；让 LLM 判断“重要不重要”不稳定。外部硬信号更适合批量调研。

影响：`comparison/selected-literature-from-survey-seeds.md` 应扩成较宽 queue；notes 只为满足 card rule 的论文写。

## 2026-06-16 — 必须做 Post-Survey Forward Recall

决策：seed survey 不能作为唯一 recall 来源。对 Agentic RL 这种高速方向，必须从已抽卡 anchor 做 forward recall。

规则：

- 如果新论文晚于 seed survey cutoff，但直接对比或改进已抽卡 anchor（例如 GRPO、GiGPO、RAGEN、WebRL、Search-R1、ArCHer），进入 queue。
- 若同时满足 arXiv + 官方代码 + 明确 RL mechanism，可直接写 L1 card。
- 例子：BEACON 提交于 2026-05，晚于当前 seed survey 主要覆盖窗口，但直接对比 GRPO/GiGPO，并提出 milestone-anchored credit assignment，因此写卡。

原因：只靠 survey mention 会系统性漏掉 seed 之后的关键工作。

## 2026-06-16 — Paper Type 必须独立于 Lane

决策：新增 `paper_type` 概念，和 `lane` 分开。`lane` 表示使用环境；`paper_type` 表示论文贡献类型。

类型：

- `core-rl-method`: 直接改 RL 方法，例如 optimizer、credit assignment、reward shaping、advantage estimation、rollout/replay。
- `environment-recipe`: 把 RL 用到某个 agent 场景，贡献常在 workflow、reward recipe、training recipe。
- `infra-interface`: 训练/执行系统、tool interface、rollout infra、observability/disaggregation。
- `benchmark-env`: benchmark、environment、verifier、evaluation protocol。
- `survey`: survey / taxonomy / overview。
- `data-overlap`: 核心对象是数据、轨迹或环境生成，需要和 Agent Data cross-link。

例子：

- GiGPO 是 `core-rl-method`。
- Search-R1 是 `environment-recipe`，机制标签是 search + outcome reward + multi-turn rollout。
- Agent Lightning / VerlTool 是 `infra-interface`，但含 credit / rollout mechanism。

原因：只按 web/search/tool/code lane 会把方法论文和应用 recipe 混在一起，影响判断。

## 2026-06-16 — No Original Brief, No Formal Card

决策：正式 L1 card 必须有 original paper PDF/HTML evidence 和 bounded paper brief。Survey mention 只能作为 recall signal。

规则：

- `notes/` 根目录只放正式 L1/L2 note。
- survey-derived stub 必须放 `notes/provisional-survey-derived/`，不计入 valid card。
- card body 不再内嵌 `Bounded Brief`，而是链接 `_meta/briefs/papers/` 或 `_meta/briefs/surveys/`。
- 批量抽卡完成前必须运行 `scripts/autoresearch.py validate`。

原因：前一次把 survey table 直接写成 card，导致 queue / provisional / formal card 混淆。这个 gate 用脚本防止同类错误复发。

## 2026-06-17 — Strict Agentic RL Core Recall 不再只依赖 survey

决策：针对 `core-rl-method` 的扩充，新增 strict recall pass。Seed survey 仍是高精度起点，但不能作为完整 universe；必须加入 related-work 二次检索、关键词直接检索，以及 source-verified 的 Codex 候选假设。

Strict core 定义：

- 论文主贡献直接训练 LLM agent policy。
- 机制属于 RL objective / optimizer、reward 或 verifier-to-policy update、long-horizon credit assignment、exploration / replay / off-policy、tree search / world-model / synthetic environment learning loop 之一。
- 纯 application recipe、generic framework、benchmark、data generation 不算 strict core，除非其主要贡献是可复用的 RL 训练机制。

筛选规则：

- 召回进 queue 要宽；升级为正式 L1 card 要严。
- Method paper 默认需要 official code / training or eval implementation；大厂 / frontier lab 论文可走 closed-lab exception，但必须标注原因。
- 以当前日期 2026-06-17 计，first public date 早于 2025-12-17 的旧论文，正式抽卡需满足 top venue、公开代码加社区影响力、或大厂例外之一。
- 新论文不要求 venue 已稳定，但必须有原文、清楚 RL mechanism，并优先检查 code / project page / related-work baseline 地位。
- Codex 自有记忆只能生成候选；没有 arXiv / OpenReview / ACL / PDF / project page 等 source verification，不进入 queue。

影响：后续 strict core method 扩充先维护 `doc/retrieval-strategy.md` 和 `comparison/strict-core-recall.md`；抽卡仍必须遵守 no original brief, no formal card。

## 2026-06-17 — L1 Card Schema 降级为 Minimal YAML + Human-Readable Body

决策：Agentic RL L1 card 不再扩展新的 `decisions` / `addresses` / `source_status` YAML 层。已有 `rl_axes` 足够承担结构化聚合；其余判断放在正文。

最终设计：

- YAML 只保留机器需要的最小字段：bibliographic metadata、`lane`、`paper_type`、`lifecycle_role`、`boundary_risk`、`rl_axes`。
- `data_overlap` 废弃；迁移期旧卡可以暂留，但 validator 不再要求新卡填写。
- `rl_axes` 是唯一固定机制 taxonomy：environment、interaction、reward、optimizer、credit、data reuse、SFT warm start。
- Failure mode 不进 YAML。正文用 `难题 / Failure Modes` 小表解释本文如何定义和处理；标签来自 `doc/taxonomy/failure-modes.md`。
- Decision points 不进 YAML。正文用 `决策点 / Comparison Hooks` 自由写后续 comparison 真会用到的问题。
- `收录判定` 不放入 card body；它属于 queue / triage / agent workflow。
- 不再保留单独 `Evidence` 节；PDF/brief 路径只放 HTML 注释，有用证据锚点写进正文。

原因：之前的 card schema 过度结构化，导致 AI 机械填字段、正文噪音变多，用户阅读价值下降。最小 YAML + 6 个正文栏目能同时支持自动聚合和人工判断。

当前正文栏目：

1. `一句话定位`
2. `难题 / Failure Modes`
3. `方法机制`
4. `相对方法`
5. `决策点 / Comparison Hooks`
6. `方法优缺点 / 适用边界`

影响：后续新写或重写 card 以 `doc/templates/l1-card.md` 为准。已有 card 不做一次性大迁移；先在 GiGPO / BEACON / HCAPO 等少量样例上试运行，确认效果后再批量整理。

## 2026-06-17 — L1 Card 增加压缩契约和引用策略

决策：L1 card 模板增加明确的长度预算、栏目职责和 citation anchor policy，避免 GPT 把 L1 写成 mini-survey。

规则：

- L1 目标长度是 700-1000 中文字；超过 1200 字通常应拆到 L2 note 或 `comparison/`。
- `难题 / Failure Modes` 表只写 2-3 行，每格一句短句；不为填表而凑 failure。
- `方法机制` 控制在 3-5 句话，只说明 rollout、reward/advantage、policy update 和核心模块。
- `相对方法` 保留，但定位是 method contrast：只说明这篇论文为什么要和谁比；正式横向判断放 `comparison/`。
- `决策点 / Comparison Hooks` 控制在 3 个 bullet 左右，只写会影响采用、baseline 地位或 novelty risk 的问题。
- `方法优缺点 / 适用边界` 各 1-2 条，不复述全部实验。

Citation 规则：

- 每张 L1 通常 3-6 个锚点足够。
- 必须锚定关键数字、核心机制出处、作者承认的 limitation、关键 ablation。
- 一句话定位、项目判断、常识性概括不需要机械引用。
- PDF/brief 路径只保留 HTML 注释；不恢复单独 `Evidence` 节。

原因：BEACON 试写显示新栏目方向正确，但篇幅仍偏长，且过密引用会打断阅读。L1 应服务快速判断和后续索引；完整证据链和横向分析交给 L2 / comparison。

## 2026-06-17 — Obsidian-Friendly Frontmatter 与 Design Knobs

决策：下一版 L1 card 使用短 frontmatter + 尾部 machine meta，避免 Obsidian 顶部 properties 过长以及 nested `rl_axes` 显示成 JSON object。

新规则：

- 开头 YAML 控制在 8-12 行，只放人会看、Obsidian 会筛选的字段。
- `authors`、`url`、`arxiv_id`、`pdf`、`brief`、`survey` 等 source/provenance metadata 放尾部 `<!-- meta: ... -->`。
- nested `rl_axes` 不再用于新卡；改用 flat fields：`rl_env`、`rl_interaction`、`rl_reward`、`rl_credit`。不常看的 `rl_optimizer`、`rl_data_reuse`、`rl_warm_start` 放尾部 meta 或必要时才提升到 YAML。
- `failure_modes` 放 YAML，值必须来自 `doc/taxonomy/failure-modes.md`。
- `design_knobs` 放 YAML，值必须来自 `doc/taxonomy/design-knobs.md`。
- body 中 `难题 / Failure Modes` 和 `设计决策 / Design Knobs` 表只负责解释标签在本文中的含义；YAML 负责机器聚类和 Obsidian filter。
- `Design Knobs` 指的是 agentic RL training loop 的设计位点，例如 credit unit、reward/progress signal、advantage estimation、rollout source、trajectory filtering、prompt/action interface；不是 paper-specific 风险点。

兼容策略：

- 旧卡不做一次性迁移；validator 放宽旧必填字段，接受旧 nested `rl_axes` 和新 flat fields 共存。
- 新写或重写卡以 `doc/templates/l1-card.md` 为准。
- 需要批量迁移时先做 3 张 smol test，确认 Obsidian 显示和 validator 都正常，再迁移更多卡。

原因：开头 YAML 太长会挤占阅读第一屏；尾部 YAML 不能被 Obsidian 当作 frontmatter。短 frontmatter + 尾部 HTML meta 能同时满足 Obsidian、脚本和阅读体验。
