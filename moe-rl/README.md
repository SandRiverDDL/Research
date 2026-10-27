# moe-rl

针对 MoE 模型结构特性设计或验证的 RL 优化算法：重要性采样、路由不一致、梯度估计及 router / expert 更新。

解释：值得独立维护，范围不算过窄；将问题定义为 MoE-aware RL optimization，而非 GSPO 小改。独立性来自结构引起的估计、路由和优化问题，尚不代表已有新颖方法或保证可发表。

范围确认：用户已明确：关注针对 MoE 模型做针对性优化的 RL 算法，类似 GSPO；不以泛化的 MoE 后训练 recipe 或多专家 agent 为核心。

## 入口

- [项目规则](AGENTS.md)
- [当前状态](doc/memory/STATE.md)
- [待读种子](synthesis/seed-sources.md)
- [候选队列](synthesis/queue.md)

基于 `../doc/research-project-template/` 初始化；helper 只做结构检查，不替代原文核查。
仅在用户要求时启动文献批处理、idea 生成或实验规划；此处不跑训练。

## 判断依据与验证

初步证据入口：[Qwen GSPO 官方说明](https://qwenlm.github.io/blog/gspo/#benefits-for-moe-rl-and-infrastructure)报告专家激活波动与 Routing Replay 问题，并采用 sequence-level 优化。GSPO 是通用 LLM RL 算法；“在 MoE 上训练有效”与“机制专门针对 MoE”须分别判断。算法不必仅适用于 MoE，但应有结构动机或结构相关证据。

当前只是建项与初步判断，未完成系统调研或查新。结构检查：0 errors / 0 warnings；2 条待读 seed、0 张正式卡。
