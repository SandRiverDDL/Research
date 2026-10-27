# MOPD 项目约定

继承 `../AGENTS.md`；本项目的流程以这里为准。

## 研究什么

研究 Multi-Teacher On-Policy Distillation：多个 teacher 的能力如何通过 student 自采样轨迹上的监督，整合进一个可部署的 student。关注监督选择与聚合、训练信号尺度、能力干扰、组合泛化、初始化及总训练成本。

- 目标是寻找有实质贡献、可规模化的方法论文；诊断服务于方法验证。
- 核心收录多 teacher OPD 的方法、训练 recipe 和直接相关证据；离线蒸馏、RL、模型合并作为必要对照。
- 多视角 OPSD、专家反馈驱动的自蒸馏、多模态 MOPD 按相关性阅读；不自动继承 `agentic-opd/` 那批论文的排除条件。
- `../opd/` 负责通用 OPD 原理、单 teacher 方法和背景；`../agentic-opd/` 负责多轮 Agent 的状态、工具反馈与长程学习。交叉论文链接已有记录，按本项目视角补充，不批量复制。

## 怎么做

- 使用 ARIS wiki；覆盖根默认流程，不默认启用 `research-codex-workflow` / `autoresearch`，不维护另一套 queue、L1/L2 cards 或 card validator。
- 原论文有可用且版本一致的 HTML 时优先读 HTML；仅在内容缺失、解析有歧义或用户要求时读取对应 PDF 部分。
- 事实追到原文章节、公式或图表；区分作者报告、自己的解释、待验证假设。Seed 链接不代表论文已读完。
- 先读 `doc/memory/STATE.md` 和 `research-wiki/index.md`，再按任务需要读取资料。论文写入 `research-wiki/`，跨论文分析写入 `synthesis/`。
- 入库和索引复用 ARIS helper；脚本检查结构与链接，原文阅读核查内容。不为每篇新造检查流程。
- 评估方法的规模化开销，不默认逐状态 probe、环境重置或分叉 rollout；这些是候选实现，不能作为用户已确认约束。
- 仅在用户明确要求时运行 idea 生成、方案细化或实验规划。此目录不运行训练，也不修改链接指向的上游 skills。

## 输出边界

以本项目为工作目录。只修改当前任务所需文件；跨项目链接不授权修改其他项目。ARIS skills 的本机链接位于 `.agents/skills/`，恢复说明见 `README.md`。
