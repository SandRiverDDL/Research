# Harness RL Decisions

## 2026-10-16 — 建项

用户授权新建；采用根模板。用户纠正：harness-rl 指在 harness 下训练 RL，并以 CompactionRL 为线索；用户仍在探索概念。主线采用 harness-aware / harness-native agent RL，不把优化 harness 本身设为必要条件。

解释：值得作为 agentic RL 内的独立调研 lens；研究价值来自真实 harness 机制引出的学习问题。“使用 harness”本身不足以构成方法贡献，也尚不据此宣称它是边界成熟的 RL 子类。

## 2026-10-16 — 用户纠正主线

此前以“优化 harness 本身”为主的解释偏离用户意图；上面的初始化范围说明已同步修正。CompactionRL 与 LEGO-RL 分别作为运行机制纳入学习、真实 harness 接入优化的入口；不据此扩大为系统调研任务。

## 2026-10-16 — 明确以模型适配为主线

用户进一步明确：在某些 harness 下训练 RL，使模型适应其工具调用、信息处理等运行方式；同时询问多个 harness 混合 RL 的现状。此前以 harness 编辑或分段优化为中心的解释过窄，现以模型的 harness 适配、混合训练与泛化为主线。

解释：值得作为 agentic RL 内独立维护的研究 lens，核心是模型如何学会使用 harness，以及专用适配、多 harness 联合学习与泛化。研究对象不要求新算法才能收录；但论文贡献仍需建立在具体问题与证据上，不能只靠接入某个框架。

多 harness 混合 RL 是待研究主问题之一；不能把用户询问的普遍性当成已确认事实。
