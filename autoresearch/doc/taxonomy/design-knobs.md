# Autoresearch Design Knobs

> Stable cross-paper design decision tags. Extend only when a tag will be reused.

## Pipeline Structure

- `pipeline-scope`: 端到端 / 单子任务 / 半自主 human-in-the-loop 的组织范围。
- `stage-decomposition`: 如何拆分 research pipeline（idea → lit → hypothesis → experiment → analysis → write → review）。
- `iteration-control`: 迭代终止条件（固定轮数 / verifier pass / human accept / budget）。
- `agent-role-organization`: 多 agent 是同质 rollout 还是 role-specialized（planner / coder / reviewer / critic）。

## Grounding & Tool Use

- `tool-grounding`: 系统对外部工具的依赖（搜索、代码执行、模拟器、真实实验室）。
- `literature-access`: 文献检索方式（Semantic Scholar / arXiv / vector DB / retrieval-augmented）。
- `code-execution-env`: 代码执行沙箱设计（notebook / container / real hardware）。
- `dataset-provisioning`: 实验数据来源（内置 benchmark / 现搜 / 生成 synthetic）。

## Verifier & Reward

- `verifier-type`: LLM-as-reviewer / rule-based / execution-check / human-in-loop / hybrid。
- `novelty-check`: 如何验证新颖性（embedding 相似度 / LLM 判断 / literature retrieval + comparison）。
- `experiment-verifier`: 实验结果如何被 accept（内部 metric / cross-run consistency / independent replication）。
- `reward-signal`: 训练/迭代信号（binary accept / reviewer score / gradient from human feedback / self-consistency）。

## Evaluation Protocol

- `evaluation-protocol`: how success is measured or compared.
- `evaluation-scope`: 评测覆盖的 pipeline 阶段（末端产出 / 中间过程 / 全流程）。
- `evaluation-judge`: reviewer model / expert human / mixed / consensus。
- `reproducibility-artifact`: 是否公开 code / prompts / seeds / generated papers。

## Data & Training

- `data-selection`: how examples / runs / sources are kept, dropped, repaired, or weighted.
- `training-source`: 是否针对 autoresearch 专门做 SFT / RL / 只做 prompting。
- `demonstration-corpus`: 用什么人类科研 trajectory 做 seed（GitHub PR / notebook / paper drafts）。

## Interface & Control

- `interface-design`: how the method exposes inputs, actions, tools, states, or constraints.
- `human-intervention-point`: 人工介入的位置和粒度（idea gate / experiment gate / final review / none）。
- `failure-recovery`: 出错后的处理（回退 / 重试 / 人工救援 / 终止）。
