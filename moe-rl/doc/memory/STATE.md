# MoE-Aware RL Optimization — 当前状态

更新：2026-10-16。

## 任务 contract

用户要求建立 `moe-rl` 并评估独立项目价值。用户已明确：关注针对 MoE 模型做针对性优化的 RL 算法，类似 GSPO；不以泛化的 MoE 后训练 recipe 或多专家 agent 为核心。

## 当前边界

针对 MoE 模型结构特性设计或验证的 RL 优化算法：重要性采样、路由不一致、梯度估计及 router / expert 更新。

- 针对 MoE 路由特性设计的 RL objective、importance weighting、clipping 与梯度估计。
- router-aware policy optimization、routing replay / correction 及 router / expert 更新规则。
- GSPO 等通用 RL 算法：有明确 MoE 动机、机制分析或实验证据时纳入核心对照。

## 完成与证据边界

- 已基于根项目模板初始化目录、规则、taxonomy、queue 与 helper。
- 解释：值得独立维护，范围不算过窄；将问题定义为 MoE-aware RL optimization，而非 GSPO 小改。独立性来自结构引起的估计、路由和优化问题，尚不代表已有新颖方法或保证可发表。
- seed 只核查原始摘要 / 元数据，未精读全文、未写正式卡、未导入 Zotero。
- 本次 helper 检查完成：0 errors、0 warnings，2 条待读 queue、0 张正式卡。
- 结构检查结果见 `_meta/generated/card-validation.md`；零张卡通过不代表论文内容验证。

## 后续

等待新的研究任务；未授权自动批量调研、idea 生成、实验规划或训练。下一次先读 `AGENTS.md` 与本文件，再按任务读 queue。
