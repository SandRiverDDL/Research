# harness-rl

面向一个或多个 agent harness 进行 RL 后训练，使模型学会相应的工具调用、信息处理、记忆 / 上下文管理和任务推进，并研究适配、混合训练与跨 harness 泛化。

用户进一步明确：在某些 harness 下训练 RL，使模型适应其工具调用、信息处理等运行方式；同时询问多个 harness 混合 RL 的现状。此前以 harness 编辑或分段优化为中心的解释过窄，现以模型的 harness 适配、混合训练与泛化为主线。

解释：值得作为 agentic RL 内独立维护的研究 lens，核心是模型如何学会使用 harness，以及专用适配、多 harness 联合学习与泛化。研究对象不要求新算法才能收录；但论文贡献仍需建立在具体问题与证据上，不能只靠接入某个框架。

## 用 CompactionRL 理解范围

作者方法事实（局部原文核查）：[CompactionRL §4–4.1](https://arxiv.org/html/2607.05378v1#S4)在上下文预算接近耗尽时，以固定阈值触发同一 trainable policy 生成摘要；用摘要与最近交互重建上下文并继续执行。任务执行与摘要生成共享最终任务奖励。§4 的方法概述说明用 token-level loss normalization 与 cross-trajectory GAE 处理分段训练和跨压缩边界的信用分配。未完整精读实验或核查全部公式。

解释：这里学习的是模型在带 compaction 的运行机制下完成任务、生成有用摘要的能力；不要求模型改写 harness 代码，也不能据此称 CompactionRL 学会了触发时机。

邻近入口：[LEGO-RL 原始摘要](https://arxiv.org/abs/2608.17393)明确以原生 coding-agent harness 下的 policy-gradient optimization 为目标，处理 compaction / re-serialization 后的 token 对齐和 log-prob 重算；本次只核查摘要。

## 入口

- [项目规则](AGENTS.md)
- [当前状态](doc/memory/STATE.md)
- [待读种子](synthesis/seed-sources.md)
- [候选队列](synthesis/queue.md)

基于 `../doc/research-project-template/` 初始化；helper 只做结构检查，不替代原文核查。仅按用户要求启动后续调研、idea 生成或实验规划；此处不跑训练。

## 验证边界

当前仅建项、范围纠正与少量定向原文核查，未完成系统调研或查新。6 条候选、0 张正式卡；本次 helper 与本地链接检查结果见状态文档。

## 多 harness 训练的证据边界（2026-10-16）

- 作者报告：[OpenForge RL v3 §5.2 / Table 5](https://arxiv.org/html/2607.21557v3#S5.SS2)对比 ZeroClaw 单 harness 与 ZeroClaw + OpenClaw + Codex 联合训练；原文明确二者的 SFT distillation 和 RL rollout 都采用相应 harness。联合设置效果更好，但不能仅据这一对照把全部收益归给 RL 阶段的 harness 混合。§5.3 分析 RL 后工具使用、自我验证和错误恢复等行为变化。
- 作者报告：[HarnessBandit 摘要](https://arxiv.org/abs/2609.13739)训练一个共享 policy 跨六个 harness，每个 optimizer step 选择一个 harness，研究 learnability / transferability 调度。当前仅核查摘要，未精读方法或实验。
- 作者报告：[Poolside Laguna TR §4.3.3–4.4，PDF 第20页](https://poolside.ai/assets/laguna/laguna-m1-xs2-technical-report.pdf#page=20)明确 multi-harness trajectories 加入 SFT mix；随后 RL 使用与生产部署一致的 harness。该报告不能被改述为已经确认 multi-harness 混合 RL。
- 解释：多 harness RL 已有明确公开研究，但“所有主流模型都在多个 harness 混合 RL”未获本次证据支持。多任务 / 多环境 RL、多工具 RL、多 harness SFT 与多 harness RL 需要分别核实。
- 用语：若“基模”指供 agent 调用的基础模型，可讨论其后训练适配；若指严格的 pretrained base checkpoint，则应与 RL 后训练后的 checkpoint 区分。

仅定向核查上述节段 / 摘要；未完成系统调研、查新或复现。

## CompactionRL 文献谱系

[归属、related work、10篇已核实引用与近邻矩阵](synthesis/compactionrl-reading-matrix.md)。本次以2026-10-01的v2为准；上文此前的v1 §4说明保留版本语义，v2方法为§3。10篇为已核实下界，不是完整引用数。
