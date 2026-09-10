# Autoresearch Retrieval Strategy

> This document defines how to find papers. Admission rules live in `doc/acceptance-rules.md`.

## Recall Focus

Candidates must primarily contribute to **自动化科研系统的机制、缺陷、评测与改进**:

- 端到端或子任务 autoresearch pipeline 的**机制设计**
- Autoresearch **失败模式**的实证研究、audit、批判
- Autoresearch 系统的**评测方法**（benchmark、reviewer model、人工评审 protocol）
- Autoresearch **改进方向**（verifier、human-in-the-loop、tool grounding、domain 适配）

Do not default-include:

- 通用 LLM agent / reasoning / tool-use 方法，除非明确以 research task 为主要 evaluation
- 单一 domain 的 autonomous experimentation 系统，除非 mechanism 可迁移
- 只讨论 AI-generated content 检测 / 学术诚信的一般性文章

## Recall Sources

Use:

1. **Seed survey recall**: 从 autoresearch / AI-for-science / autonomous experimentation 综述里抽直接方法引用。
2. **Known-item recovery**: 用户/项目命名的论文（AI Scientist、AI Scientist-v2、STORM、AgentLaboratory、Sakana 系）先入 queue，再核验 source。
3. **Neighbor backflow**: 检查 `agentic-rl/`、`agent-data/`、`foundation-model-systems/` 的 queue 里是否有 autoresearch 相关论文。
4. **Keyword direct search**: 一次性搜索仅用于发现新术语族（例："AI scientist"、"autonomous research agent"、"LLM peer reviewer"、"citation fabrication"、"research reproducibility LLM"）。
5. **Critique / audit 优先入口**: 主动搜"limitations of AI scientist"、"reproducibility of LLM-generated research"、"reward hacking reviewer model"这类反向证据。

## Bounded Snowballing Loop

```text
seed / known-item
  -> source verification
  -> candidate classification
  -> apply doc/acceptance-rules.md
  -> collect PDF / HTML / brief
  -> write approved L1 cards
  -> validate
```

Stop recall when two consecutive rounds add <= 2 high-priority candidates.

## Batch-First Admission

Classify candidates before writing cards:

| candidate | class | reason | action |
|---|---|---|---|
| paper title | core / survey / benchmark-eval / adjacent / background / critique / reject | 1 sentence | card / hold / ask user |

Do not write more than 3-5 L1 cards in one batch without validation.

## Candidate Log

Write candidates to `comparison/queue.md` or a focused comparison document. Do not leave recall state only in chat.

Each candidate row should include:

- `source`
- `recall_reason`
- `boundary_risk`
- `action`

## Special: Critique / Audit Recall

因为本项目特别关心 autoresearch 的**缺陷**，独立走一条 recall 支路：

- Retraction Watch / AI-generated paper 相关报道
- OpenReview 上关于 AI-assisted review 的 meta-review
- Reproducibility challenge 报告里涉及 AI-generated code / experiment 的部分
- Position papers 与 workshop 上关于 AI4Science limitations 的讨论
