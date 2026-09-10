# OPD 当前决策

> 只记录仍影响现行流程的原因；完整旧记录见 `../archive/DECISIONS-through-2026-07-27.md`。

## 2026-07-27 — L1 与脚本解耦

新卡只保存稳定身份字段，正文不被脚本解析。Registry 直接扫描 cards，只保留 `lookup/status/validate`；71 张旧卡不迁移。

原因：避免 YAML taxonomy、正文结构、队列和生成物互相耦合。

## 2026-07-27 — Cards 是 ideation 上游索引

Cards 用于大范围 recall 和 routing；具体方向仍需 freshness retrieval，关键 bottleneck、novelty 和 idea claim 回查原文。

原因：只读原文成本过高，只读摘要又会继承压缩偏差。

## 2026-07-27 — 抽卡标准单一化

抽卡准入只在 `doc/card-acceptance.md` 维护；`AGENTS.md` 只负责按任务路由。旧的 trust-gated、triage 分级和 venue landscape 规则不再参与执行。

原因：多个规则源和复杂分级会增加 context rot 与执行偏差。

## 2026-07-28 — Synthesis 按 failure mode 组织

每个重要 failure mode 使用一份 Markdown；正文说明现象、diagnosis、残余瓶颈，主表以方法为行、决策点为列，并按主要干预位置聚集。Failure mode 回答“为什么值得研究”，决策点回答“已有方法如何选择”。

增量维护时，新论文默认只增加表格行。只有出现新的决策选择、反驳或修改现有 diagnosis、或真正改变残余瓶颈时，才修改最多 3–5 条“当前判断”。不保存逐次更新日志，不因每张新卡重写全文；跨 failure mode 的决策轴总表仅在真实查询需要时创建。
