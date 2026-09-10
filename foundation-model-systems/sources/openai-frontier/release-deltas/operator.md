# OpenAI Operator Release Delta

```yaml
---
delta_id: operator
parent_source: openai-frontier
release_date: 2025-01  # Operator research preview launch；后续与 ChatGPT Agent 合流
role: release-delta
confidence: medium
status: section-notes
openness: closed-weights
---
```

## 定位

Operator 是 OpenAI 的 browser / computer-use agent 产品（基于 CUA - Computer-Using Agent 模型），后续与 Deep Research、ChatGPT Agent 合流为统一 ChatGPT Agent 体系。它是 OpenAI 阵营中 agent data / trajectory / verifier 视角**最直接的 anchor**，因为产品形态本身就是 long-horizon GUI agent，且发布配套了 system card / safety report。

## 关键 release / 演进

- **Operator (2025-01)** — research preview，CUA 模型驱动 browser agent。
- **ChatGPT Agent (2025+)** — Operator + Deep Research + Codex agent 合流为 ChatGPT 内部统一 agent 模式。
- **后续 GPT-5 + agent 集成** — agent 能力作为 GPT-5 一线产品功能。

## 公开材料范围

- **Operator system card / safety report**：browser / computer-use 模型的 agentic capability eval、refusal、prompt injection、reward hacking。
- **Introducing Operator blog**：产品形态、CUA 模型 framing、browser agent 任务范围。
- **后续 ChatGPT Agent 公告 + system card 更新**。
- **API / platform docs**（Computer Use API、Responses API、Agents SDK）：tool schema 与产品集成方式。

具体 URL 留到引用时补；本文件只做 framing 与边界。

## Agent data 视角的可用信号

> 全部 confidence: medium，依据是 system card + blog framing。

- **Browser agent trajectory 评测**：Operator system card 明确以 long-horizon browser task 作为 capability + safety 评测对象；这是 frontier closed 阵营**第一个**把 browser trajectory 当作主线 agent eval 的公开样本。
- **Prompt injection / external manipulation**：system card 大量篇幅讨论 web 环境中第三方 prompt injection 的 attack surface 与 mitigation，是 GLM-5.2 anti-hacking 之外**第二个**公开的 agent-环境对抗工程证据来源（**仍是 evaluation / safety mitigation，不是 training pipeline**）。
- **"refusal-on-uncertain-action"**：Operator 在 high-risk action 前会 ask user / confirm，这是 product-level safety scaffolding，但**间接**暗示训练时存在"区分高低风险 action + 触发 confirmation"的 reward / refusal 设计。
- **CUA 模型 framing**：产品材料把 Computer-Using Agent 作为独立模型类，可能对应一个专门 fine-tune 的 checkpoint；不能确认是与 GPT-5 同体还是独立 head，这是 open question。

## 不能从 Operator 推出的事

- **训练 trajectory 来源**：人类示范 / synthetic rollout / 真实日志？全部 unknown。
- **verifier / reward design**：是否有类似 MiniMax AaaV 的多层 verifier、是否用 LLM judge——零公开。
- **ChatGPT Agent 与 Operator 的训练继承关系**：合流是产品层还是模型层（继续训练 / 蒸馏 / 重训）——未公开。
- **CUA 模型规模 / 架构**：未公开。

## 与本项目其他 source 的横向对照（待 lens 沉淀）

- vs **MiniMax-M2 AppDev pipeline**：MiniMax 用 sandbox + 三层 verifier 给 SWE / cowork artifact 任务做 trajectory 验证；Operator 在 browser 环境的对应做法没有公开 → MiniMax 给的是 verification 透明度，Operator 给的是 frontier 级**问题难度**透明度（browser 是更脏的环境）。
- vs **GLM-5.2 anti-hacking**：GLM 公开了 in-training anti-hack 机制；Operator 公开的是 deployment-time mitigation。两者代表 anti-hacking 在两个不同生命周期的工业实践。
- vs **Anthropic Computer Use**：与 Claude 4.5 Computer Use 是同领域 frontier 双样本，但 Anthropic 偏 system card framing，Operator 在 browser-specific 评测上更具体（Browse / form-fill / scheduling 等）。

## Source

- 引用必须落到具体 blog / system card URL，标签遵循 `sources/openai-frontier/source-bundle.md` 的 citation labels（`[blog-oai-operator]`、`[sys-card-operator]`、`[api-docs]` 等）。
- stage notes 升级时按以下顺序锚定：
  1. Operator system card PDF（agentic eval / prompt injection / refusal）
  2. `Introducing Operator` blog（产品 framing）
  3. ChatGPT Agent 合流公告（lineage）
  4. Computer Use API / Responses API docs（tool schema）

## 升级 trigger

- **不**单独成独立 dossier，除非 OpenAI 公开 CUA 模型的训练 / 架构细节（极不可能）。
- 若 ChatGPT Agent 后续替代 Operator 成为主线产品并出独立 system card，可在 release-deltas 下加 `chatgpt-agent.md` 单独跟踪，不动本文件。

## Caveats

- closed-weights、零 TR：不要从 InstructGPT / RLHF 老 paper 反推 Operator / CUA 训练设计。
- system card 评测数字不能反推 training 数据规模或比例。
- 产品演示视频里的 trajectory 不是训练数据样本；不要把 demo 当作 trajectory data 公开证据。
- "agent 能完成 X 类任务"是 capability claim，需要 system card 评测 setup 才能进 comparison；blog framing 单独不够。
