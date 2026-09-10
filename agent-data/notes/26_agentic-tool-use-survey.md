---
title: "Agentic Tool Use in Large Language Models"
year: 2026
venue: arxiv
paper_type: survey
lifecycle_role: survey-seed
boundary_risk: none

failure_modes: [action-grammar-fragility, coverage-gap]
data_knobs: [tool-call-grammar, trajectory-to-sft, action-schema]

agent_domain: tool
data_object: tool-call
data_source: mixed
selection_signal: coverage
adaptivity: static
failure_use: ignore
training_consumer: sft
---

## 一句话

作为 tool-call data / supervised tool learning 的 2026 入口综述。

## 核心做法

综述指出 tool-use 研究碎片化，按任务、工具类型、训练设置分散；它把文献组织成 prompting as plug-and-play、supervised tool learning、reward-driven tool policy learning 三类，并比较方法、优势、failure modes 和 evaluation landscape。

对本项目最有价值的是 supervised tool learning 部分：tool-call data、action grammar、tool-use trajectory、format validity、evaluation landscape。reward-driven tool policy learning 属于 Agentic RL，迁到 `/Users/chy/Research/agentic-rl/`，不在当前项目抽完整卡。

## Data-Centric 判断

- data object: tool-use tasks、tool call、tool trajectory。
- source: tool-use literature。
- selection / filtering: survey 层面覆盖，需从 references 里抽具体 data methods。
- adaptivity: static survey。
- failure trajectory use: 只在 failure modes 层面提到，需回具体论文。
- downstream effect: 作为 tool-call data / action grammar / trajectory data 的 seed taxonomy。

## 谱系位置

- 上游：Tool Learning with Foundation Models。
- 同期：tool-call SFT、agent trajectory tuning、synthetic tool-use data papers。
- 下游：Agent Data report 的核心 survey seed。

## 优缺点

- ✅ [arXiv Abstract]: 明确按 prompting、supervised tool learning、reward-driven tool policy learning 三范式组织。
- ⚠️ [本项目判断]: 当前只用 supervised tool learning 相关 references；ToolRL / reward-driven policy learning 迁到 `agentic-rl` queue。

## Evidence

- arXiv: title / abstract。

<!-- meta:
authors: [Jinchao Hu, et al.]
url: https://arxiv.org/abs/2604.00835
arxiv_id: 2604.00835
pdf: arXiv abstract
brief:
survey: none
agentic_rl_overlap: false
agentic_rl_queue: none
-->
