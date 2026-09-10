# Foundation Model Systems — Decisions

> 这里只记录稳定决策及历史理由；临时任务状态放在 `STATE.md`。

## 2026-06-16：项目名称

Decision：使用 `foundation-model-systems`。

Reason：`model-systems` 范围过宽，`training-recipes` 又过窄。本项目研究 foundation model system construction，包括 architecture、data、training、post-training、eval、safety 与 infra。

## 2026-06-16：不直接复制 OPD pipeline

Decision：采用轻量 source dossier workflow。

Reason：OPD 面向大量 paper candidate，需要 L1 card throughput；本项目的 source 数量较少但辨识度高，长期价值主要来自 source dossier、lens 与 comparison。

## 2026-06-16：L1 只作为 index

Decision：不为本项目建立完整 L1 paper-card workflow。

Reason：关键模型容易定位，核心工作是 source interpretation 与跨 source 判断；L1 只需承担 manifest / index 功能。

## 2026-06-18：TR / recipe workflow 保持 project-local

Decision：不把 model TR / open recipe dossier 的项目规则写入全局 `research-codex-workflow` skill。

Reason：通用 skill 提供 evidence gate 与研究卫生规则；frontier model TR 通常是 source bundle，需要本项目特有的 source dossier、section index、human-first stage note 与 citation style。

Impact：跨项目原则留在 skill；目录结构、stage checklist、citation style 与 dossier admission rule 留在本项目。只有该流程被多个独立项目复用时，才考虑拆成单独 local skill。

## 2026-07-21：保持 project memory 精简，不使用 compact hook

Decision：`STATE.md` 作为短期 hot state，`DECISIONS.md` 作为 append-only 的稳定理由记录。不添加 model-backed `PreCompact` hook、raw prompt journal 或 compact-time context reinjection。

Reason：hook 若要理解语义，必须额外调用模型或依赖不稳定的 transcript parsing，会增加延迟、token 与故障面；在有意义的任务事件后增量更新状态更简单可靠。

Impact：

- `STATE.md` 目标控制在约 4 KB，通过替换旧状态而不是追加历史来保持精简。
- scope / priority / authorization 变化后、高 context 工作前、实质里程碑后和长任务最终回复前同步状态。
- compact 后先读项目 `AGENTS.md` 与 `STATE.md`；只有 STATE 引用了相关 decision 时才读本文件。
- Codex built-in Memories 未来可以作为辅助 recall，但不能作为 authoritative task contract。

## 2026-07-21：综合产物需要显式授权

Decision：lens、comparison 与 cross-model summary 是独立交付物，只有用户明确要求时才生成。

Reason：workflow 说明的是如何创建这些 artifact，不代表每次 source-dossier 任务都自动获得创建权限。

Impact：补 dossier、stage note 或 release delta 不隐含授权综合产物；assistant 建议与旧 candidate list 在用户确认前必须保持 unconfirmed。
