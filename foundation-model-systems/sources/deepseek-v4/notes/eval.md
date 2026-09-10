# DeepSeek-V4 Evaluation

```yaml
---
source_id: deepseek-v4
section_type: eval
stage: eval
substage: none
depth: working
confidence: medium
need_expert_review: false
---
```

## Scope / Coverage

- 覆盖页段：TR pages 27-28, 36-44。
- 覆盖阶段：base eval、post-trained eval、formal/tool eval、long-context eval、internal real-world eval。
- 子问题：
  - 哪些 eval 支撑 DeepSeek-V4 的能力 claim？
  - 哪些 eval 能作为 strong evidence，哪些只是 product / internal signal？
  - reasoning mode、context budget 和 tool access 如何影响可比性？

## Core Summary

- 事实：Base-model evaluation 覆盖 world knowledge、language/reasoning、code/math 和 long context，使用 internal unified framework。[27-28]
- 事实：Post-trained benchmark suite 包括 knowledge/reasoning、code、formal math、1M context 和 agentic tasks，混合 public + internal benchmarks。[36-37]
- 事实：formal math evaluation 使用 Lean v4.28.0-rc1 和 semantic tactic search engine，最多 500 tool calls，并用 strict verifier acceptance。[37]
- 事实：code-agent tasks 使用 internal framework，工具是 bash 和 file-edit，max 500 interaction steps，max context length 512K。[37]
- 解释：DeepSeek eval suite 比经典 static benchmark reporting 更 broad、也更 agentic；但最有意思的一些 eval 是 internal 或 framework-dependent，所以 public evidence 强度不均。[36-38, 43-44]

## Eval Map

### Base Model Eval

- Base eval 覆盖 world knowledge、language/reasoning、code/math 和 long context。[27-28]
- 报告称 V4-Flash-Base 虽然 active/total parameters 更少，但在很多 benchmarks 上超过 V3.2-Base。[28]
- 解释：base eval 用来支撑 architecture/data/training setup 的效率 claim，但依赖 internal unified framework，外部复现仍要看具体 benchmark setup。[27-28]

### Post-trained Public + Internal Benchmarks

- Post-trained suite 包含 LiveCodeBench、Codeforces、MRCR、CorpusQA、Terminal-Bench、SWE-Verified、SWE-Pro、SWE Multilingual、BrowseComp、MCPAtlas、GDPval-AA、Toolathlon。[36-37]
- Table 6 报告 DeepSeek-V4-Pro-Max 在多个 reasoning/agentic benchmarks 上是强 open model，并和 closed models 有竞争；但在 SimpleQA/HLE 以及若干 closed-frontier agentic numbers 上仍落后 Gemini/闭源模型。[38]
- 解释：这里不能把 V4 当成一个单一 scalar 分数；报告明确把 performance 和 reasoning effort / context budget 绑定。[40]

### Formal / Executable / Agentic Eval

- Formal math 使用 Lean verifier 和 tactic search，属于比 judge-only 更硬的 eval surface。[37]
- Code-agent tasks 使用 bash/file-edit 工具和最多 500 interaction steps，max context length 512K。[37]
- 解释：strict formal verification 和 executable coding tasks 证据强度更高，但结果仍依赖 tool choice、scaffold、interaction budget 和 context length。[37]

### Long-context / Reasoning Effort

- Max mode 使用更长 context 和更弱 length penalties，在难任务上优于 High mode。[40]
- MRCR 在 128K 后出现 degradation，但 1M 下仍保持较强；CorpusQA 被报告为更接近真实场景。[40]
- 解释：1M context 不是“所有长上下文任务都解决了”，要按任务类型和 retrieval/generation 负载解释。[40]

### Real-world / Internal Eval

- Real-world task eval 包括中文写作和 internal R&D coding benchmark；R&D coding benchmark 从约 200 个内部任务过滤到 30 个，并有人类 rubrics。[43-44]
- Internal R&D coding result：DeepSeek-V4-Pro-Max pass rate 67%，Claude Sonnet 4.5 为 47%，Opus 4.5 为 70/73，Opus 4.6 Thinking 为 80。[44]
- 解释：internal R&D coding 对 DeepSeek 自身 workflow 可能很高信号，但 task selection/rubric 不公开，泛化性有限。[43-44]

## Gaps / Open Questions

- 哪些 benchmark 可能受 pretraining 或 post-training data contamination 影响，需要外部 audit。
- 每个 compared model 使用了多少 inference compute / reasoning budget，不总是清楚。
- Internal Codeforces/R&D/GDP-style evals 可复现性有限。
- “real-world task” 当前主要覆盖写作/search/coding，是否代表更广泛工作流不确定。

## Transfer Hooks

- worth-internalizing: frontier eval 应按 mode / reasoning effort / tool budget 分层，不应只看一个总分。
- try-at-small-scale: 建立 public benchmarks + internal workflow tasks 的双轨 eval，但 internal task selection 和 rubrics 要透明。
- lookup-only: Table 6 / Table 8 的具体 benchmark numbers 和 closed-model comparison。

## Split Check

- current scope: eval overview and evidence-strength audit。
- if this file grows beyond ~220 lines, split by: public benchmark eval vs internal/agentic eval。

## Evidence Anchors

- 27-28: base-model eval setup 和 Table 1。
- 36-38: post-training eval setup 和 Table 6。
- 37: formal math 和 agentic code evaluation details。
- 40: reasoning effort 和 long-context observations。
- 43-44: Chinese writing 和 internal R&D coding eval。
