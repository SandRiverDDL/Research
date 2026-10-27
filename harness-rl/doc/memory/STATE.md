# Harness RL — 当前状态

更新：2026-10-16。

## 任务 contract

用户要求建立 `harness-rl` 并判断独立项目价值，随后提供 CompactionRL 线索纠正含义。用户进一步明确：在某些 harness 下训练 RL，使模型适应其工具调用、信息处理等运行方式；同时询问多个 harness 混合 RL 的现状。此前以 harness 编辑或分段优化为中心的解释过窄，现以模型的 harness 适配、混合训练与泛化为主线。

## 当前边界

面向一个或多个 agent harness 进行 RL 后训练，使模型学会相应的工具调用、信息处理、记忆 / 上下文管理和任务推进，并研究适配、混合训练与跨 harness 泛化。

- 在目标 harness 下用 RL 训练模型使用工具、理解返回信息、管理状态并完成任务；不要求修改 harness 或提出新的 RL objective。
- 多个 harness 的联合 / 混合 RL、配比或调度，以及专用适配与通用能力之间的迁移 / 干扰。
- 已见和未见 harness 上的泛化、训练部署一致性，以及支撑这些目标的 rollout / optimization 机制；compaction 是具体子问题。

## 本次新增核查

OpenForge RL v3 §5.2–5.3 / Table 5 局部核查；HarnessBandit 仅原始摘要核查；Laguna TR §4.3.3–4.4 局部核查。后者 multi-harness 在 SFT mix，不能冒充已确认混合 RL。来源与判断见 README“多 harness 训练的证据边界”。

## 当前判断

解释：值得作为 agentic RL 内独立维护的研究 lens，核心是模型如何学会使用 harness，以及专用适配、多 harness 联合学习与泛化。研究对象不要求新算法才能收录；但论文贡献仍需建立在具体问题与证据上，不能只靠接入某个框架。

## 完成与证据边界

- 初始化模板已完成；本次同步修订 scope、acceptance、retrieval、triage、taxonomy、README 与 seed / queue。
- CompactionRL 已定向核查 v1 HTML §1、§4–4.1 与 §4.2 起始段，未完整精读方法公式、实验或全部消融；固定触发阈值，不声称学会压缩时机。
- LEGO-RL、Harness-1、Co-Harness 仅核查原始摘要 / 元数据。Co-Harness 保留邻近对照，不据摘要当作 RL 方法。
- 6 条候选、0 张正式卡；未导入 Zotero、未做系统检索或查新、未运行实验。
- 本次更新后 helper 与本地链接检查通过：0 errors、0 warnings；零张卡通过不代表内容验证。

## 后续授权边界

本次仅解释概念、核查单 / 多 harness 训练的公开证据并纠正项目范围；未授权自动批量调研、idea 生成、实验规划或训练。下一次先读 `AGENTS.md` 与本文件，再按任务读 queue。

## 当前任务：CompactionRL 文献谱系核查（2026-10-16）

用户要求定位 CompactionRL 的研究归属、原文 related work、引用它的论文、后续 follow-up 与最近邻。授权定向文献检索和原文核查，交付简短对照与证据入口；不做 idea 生成、实验规划、训练或 Zotero 导入。首先确认 arXiv 最新版本；明确区分引用关系、时间先后和方法延续，不恢复成批量建卡任务。已完成；交付 `synthesis/compactionrl-reading-matrix.md`。

## CompactionRL 谱系核查结果（2026-10-16）

- 定位为 agentic RL 的 learned context compaction / long-horizon memory 专题；这是本次分析判断，不是用户确认的新项目改名或目录迁移。
- 最新原文为 v2（2026-10-01），已核查 §2–3、§4.3 / Table 3 与 Limitations；v1 的 §4 方法现在对应 v2 §3，cross-segment GAE 为近似。SUPO 是直接前序与 v2 实验 baseline。
- 已在原始 HTML 正文 / bibliography 确认10篇引用，不冒充完整 citation count。Occamy 明确采用 recipe；AutoCompact、CAMG-RL 为直接对照，CCM 为同问题邻近路线。完整清单、来源与各自阅读边界见报告。
- S2 429、OpenAlex cited_by_count=0 与原文引用不一致；以原文逐项确认，不作没有引用的判断。
- 本轮只新增一份 synthesis，并更新状态、README入口及已有 CompactionRL queue / seed 的版本说明；仍为6条queue、0张正式卡。未入库、未训练、未做 idea 或实验规划。
- 报告本地链接与10篇引用去重检查通过；无可用语音命令。
