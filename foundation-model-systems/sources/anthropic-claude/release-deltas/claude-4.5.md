# Claude 4.5 Release Delta

```yaml
---
delta_id: claude-4.5
parent_source: anthropic-claude
release_date: 2025-09  # Sonnet 4.5 GA；后续 Opus/Haiku 4.5 视实际节奏更新
role: release-delta
confidence: medium
status: section-notes
openness: closed-weights
---
```

## 定位

Claude 4.5 是当前 Anthropic 主线 frontier release：Sonnet 4.5 是核心 agent + coding 旗舰，Opus 4.5 / Haiku 4.5 在不同 capability tier 上补全 family。它是本项目 closed-weights agent data 视角**最重要的 anchor**，因为 Anthropic 周边产品（Claude Code、Skills、Sub-agents、Computer Use）都对应 Claude 4.5 时代的部署形态。

## 关键 release（lineup）

- Sonnet 4.5 — agent / coding 旗舰，Claude Code 主力。
- Haiku 4.5 — speed / cost 优化层，sub-agent / 工具调用底座。
- Opus 4.5 — 高端推理。
- 周边能力（不一定单独 model）：Skills、Sub-agents、Memory、Computer Use 升级。

## 公开材料范围

- **Engineering blog 系列**：`Building effective agents`、`Claude Code` 主题文章、`Skills`、`Sub-agents`、`Computer Use`。
- **System card**：Claude 4.5 / Sonnet 4.5 / Opus 4.5 / Haiku 4.5 各有 PDF，含 agentic capability eval、refusal、reward hacking、red-team。
- **Model spec / Acceptable Use**：政策文件，间接暴露 reward / refusal 设计取舍。

具体 URL 留到 stage notes / 引用时再补；本文件只做 framing 与边界。

## Agent data 视角的可用信号

> 以下 confidence 全部 medium：依据是 blog + system card framing，不是训练 recipe 公开。

- **任务分解粒度（sub-agent / skill）**：Anthropic 把"复杂任务拆成多个专门 sub-agent + 可重用 skill"作为产品级机制 → 间接说明训练时 trajectory 的组织方式偏向 **多 agent 组合**，而不是 single-agent long trajectory。这与 MiniMax AaaV 的"verifier 自己起 agent 调工具"是同一思路：用更多 agent 替代更复杂的单点 verifier。
- **Computer Use trajectory**：从 Claude 3.5 Sonnet 引入，到 Claude 4.5 升级；blog 提到训练时使用了基于 screenshot + action 的 agent trajectory，但**没披露**合成 / 筛选 pipeline。可作为"frontier 级 GUI agent trajectory 数据存在"的存在性证据。
- **Reward hacking / agentic safety 评测**：system card 公开了多种 agent 误用 / hack 模式（窃取 secrets、escape sandbox、misalign tool use），是除 GLM-5.2 anti-hacking blog 外**第二个**公开的 agent reward hacking 工程证据来源。**注意**：system card 是 evaluation 文件不是 training recipe，不能直接当作 anti-hacking pipeline 证据。
- **"Building effective agents" 框架**：把 agent 设计区分为 workflow（确定性 chaining）vs agent（动态决策 + tool use），是工业界少见的公开 agent 设计 taxonomy；但属于 design philosophy，不是 data pipeline。

## 不能从 Claude 4.5 推出的事

- **训练数据规模 / mixture / RL recipe**：全部 unknown。
- **trajectory 合成 pipeline**：是否有 teacher rollout、verifier 层数、rejection 维度——零公开。
- **reward model / GRM 设计**：除政策类 framing 外没有公开材料。
- **Claude Code 的训练数据**：blog 强调 product 设计而不是 training data 来源；不要把 Claude Code 的工程 framing 当作训练数据 pipeline 证据。

## 与本项目其他 source 的横向对照（待 lens 沉淀）

- vs **GLM-5.2 anti-hacking**：Claude system card 给出 hacking 现象目录，但 anti-hacking 训练机制不公开；GLM-5.2 反过来——机制公开但单家。
- vs **MiniMax AaaV**：MiniMax 用三层 verifier（exec/interact/visual），Claude 体系把 verification 分布到 sub-agent / skill 层；前者是 pipeline 内部分层，后者是产品架构分层。
- vs **Qwen3 thinking-mode-fusion / Qwen3.6 thinking preservation**：Anthropic 没公开类似的"reasoning chain 跨轮保留"机制 framing，但 Claude Code 长任务里实际效果接近——属于 **architecture vs product** 的不同实现路径。

## Source

- 引用必须落到具体 blog / system card URL，引用标签遵循 `sources/anthropic-claude/source-bundle.md` 的 citation labels。
- stage notes 升级时按以下顺序锚定：
  1. system card PDF（agentic eval / reward hacking 段落）
  2. `Building effective agents` blog（design taxonomy）
  3. Claude Code 工程 blog 系列（产品形态）
  4. Skills / Sub-agents blog（任务分解粒度）
  5. Computer Use blog + system card 段落（GUI trajectory 存在性）

## 升级 trigger

- **不**单独成独立 dossier。Anthropic 没出 TR，独立化没有信息密度支撑。
- 升级条件：Anthropic 后续若公开训练 recipe（极不可能）或第三方有可信复现 / 反向工程材料（小概率），再考虑升级 stage notes。

## Caveats

- closed-weights、零 TR：不要从 Anthropic 历史 paper（Constitutional AI、Sleeper Agents、Sycophancy 等）反推 Claude 4.5 现行训练设计。
- product-level claim ≠ training-time data pipeline。Claude Code "能做 X" 是 inference + scaffolding 结果，不是训练数据存在 X 的证据。
- system card eval 数字不是 training set 比例；引用时区分 evaluation domain 和 training-time domain。
