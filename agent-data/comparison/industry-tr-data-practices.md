# Industry TR: Agent 数据怎么处理（清洗 / 筛选 / 合成）

> 范围：基于 `~/Research/foundation-model-systems/sources/` 已读 TR notes 提炼。
>
> **第一档（TR-anchored 共识，本报告主线）**：Qwen3、MiniMax-M2、GLM-5.2、LongCat-2601、Step-3.5、DeepSeek-V4、Nemotron-Cascade-2、Kimi-K2.5。这一档每条 claim 都有具体 TR 页码 anchor。
>
> **第二档（blog-level / closed-weights 信号，§8 集中处理）**：Qwen3.5/3.6/3.7、Anthropic Claude 4.5、OpenAI Operator、Google Gemini 2.5、Meta frontier。这一档 confidence 偏低，不进主线共识表，仅在 §8 列已知信号与开放问题。

## 0. 一句话结论

工业界处理 agent 数据的共识不是某个单一技巧，而是一条**纯 reject、不修不改**的流水线：环境/verifier 先建好 → teacher rollout 生成候选 → 多层 reject sampling 过滤 → 合格的进训练。失败轨迹整条丢。

## 1. 共识 vs 单家做法

| 实践 | 强共识 | 单家做法 |
|---|---|---|
| 多维 rejection sampling 过滤 | Qwen3 / Step-3.5 / Kimi-K2.5 / Nemotron-Cascade | — |
| sandbox / executable environment 是数据的前提 | MiniMax / LongCat / DeepSeek / GLM | — |
| 多层 verifier（execution + interaction + artifact） | MiniMax 最完整；其他家局部用 | — |
| Anti-hacking 当训练机制 | — | GLM-5.2（在线拦 + dummy continue） |
| Planning augmentation（不靠 rollout 教元认知） | — | LongCat-2601 |
| Mixed-domain 同阶段混训防 forgetting | MiniMax / Qwen3 | — |
| GRM / rubric judge 处理 hard-to-verify | DeepSeek / Kimi GRMs | — |

## 2. 关键机制（按你最关心的三件事）

### 2.1 筛选（rejection sampling，最强共识）

Qwen3 / Step-3.5 都用 teacher 跑候选，然后按多维度**整条 reject**：

- **incorrect**：最终答案错
- **repetition**：中途重复 step / 工具调用
- **guesswork**：太简单，不需要 CoT 就能答对（怕教成浅层猜）
- **thinking/summary inconsistency**：思考过程和最终输出对不上
- **language mixing**：中英文混杂
- **overthinking**（Step）：推理冗长

工程做法：规则先粗筛 → 单次 LLM 检查一致性。每条 ≤1 次 forward。

### 2.2 清洗（verifier-driven，artifact 类任务必备）

**MiniMax-M2 AppDev pipeline 三层 verifier**[F]（TR pages 7-16）：

| 层 | 验什么 | 怎么验 |
|---|---|---|
| execution | 能跑吗 | 启动 sandbox + 跑测试 + 检查 stderr / endpoint |
| interaction | 用起来对吗 | 起一个 verifier agent 假装用户去操作 |
| visual aesthetics | 长得对吗 | 截图 + VLM rubric judge |

三层任一不过 → 整条丢。

**关键差别**：verifier 自己用工具（不是只读文本判断）。LLM judge 读文本，AaaV 起 agent 调工具。

不同 domain 的 verifier 形态：

- SWE：F2P / P2P 单测
- Terminal：自动 Dockerfile + test script
- Cowork（office/finance/slides）：artifact-specific verifier + pairwise comparison

**Anti-hacking（GLM-5.2）**[F]：rule high-recall + LLM judge high-precision。在线版本 block call + dummy return + 继续 rollout；离线版本退化为 hack 检出后整条丢或截断。常见 hack pattern：读 hidden eval、抄 upstream commits、fetch GitHub target source。

### 2.3 构造（synthesis 模式，全部基于环境）

**没有任何 TR 直接拿原始日志做 SFT**——日志只用来抽 task skeleton / tool schema / 失败模式。

四种公开合成路线：

1. **issue/PR → sandbox → trajectory**（MiniMax SWE）：从真实 PR 反推 Docker 环境 + F2P/P2P 测试
2. **domain spec → 自动生成 tool/env**（LongCat）：从 domain specification 自动生成 tool set + database schema + tool code + unit tests，> 95% 自动化成功率
3. **reverse synthesis**（LongCat）：从已验证的执行路径反推 user prompt，扩 prompt 多样性
4. **planning-oriented augmentation**（LongCat，**唯一公开的元认知数据生成法**）：把线性成功轨迹改写成"考虑过 A/B/C，因为 X 选了 B"，最终选择保持原轨迹不变。不需要 rollout / MCTS。

## 3. 几个值得纠正的常见误解

| 误解 | TR 实际做法 |
|---|---|
| 大模型直接生成轨迹给小模型 SFT | TR 主流是 specialist → student distillation（MOPD 系），不是 vanilla SFT |
| 几万真实日志直接训练 | 没人这么做。日志是 task/env 的来源，不是训练数据本身 |
| LLM judge 就够了 | artifact 类任务 TR 共识是 Agent-as-Verifier（要工具调用），不是文本判断 |

## 4. 对 30B A3B agent SFT 的可操作 pipeline

按 TR 共识能落地、不需要 RL infra 的最小组合：

```
原始用户日志
  ↓ 抽 task skeleton + tool schema + 典型失败模式（不直接当数据）
  ↓
搭 sandbox + verifier（按 domain：SWE 用单测、cowork 用 artifact judge）
  ↓
teacher 在 sandbox 跑候选 trajectory（不是改写日志）
  ↓
[Layer 1] anti-hacking pattern 扫描：hack 检出 → 丢
[Layer 2] Qwen3-style 多维 rejection：incorrect / repetition / inconsistency / lang-mix → 丢
[Layer 3] AaaV verifier（execution + interaction + artifact）→ 任一不过丢
  ↓
[Augment] LongCat planning augmentation：成功轨迹改写为带 plan + self-check 版本
  ↓
mixed-domain 混训（reasoning + code + agent + general 同阶段）
SFT 数据
```

每个环节都对应一条 TR 证据，不靠论文外推。

## 5. 证据强度

| claim | strength | source |
|---|---|---|
| 多维 rejection 整条丢 | 强 | Qwen3 [10], Step-3.5 [16] |
| 三层 verifier（exec/interact/artifact）on artifact 类任务 | 中-强 | MiniMax [9-11] |
| Anti-hacking 是 RL 训练机制 | 中 | GLM-5.2 blog（单家） |
| Planning augmentation 教元认知 | 中-弱 | LongCat [3-4]（单家，且未给 ablation） |
| Mixed-domain 防 forgetting | 强 | MiniMax [19], Qwen3 [11] |

## 6. 开放问题

- LongCat planning augmentation 没有公开 ablation，无法确认对元认知 eval slice 的实际增益。
- MiniMax AaaV 三层 verifier 的 false-positive rate / 通过率分布未披露。
- GLM anti-hacking 的 LLM judge 误杀率未披露。
- 所有 TR 都没回答："小模型应该用 teacher SFT 还是 specialist distillation"——MOPD 系（MiMo / GLM / Qwen3-Coder-Next / Step）走 specialist 路线，但工程门槛高。

## 7. 指针

- 详细 TR notes：`~/Research/foundation-model-systems/sources/<model>/notes/`
- 论文层面对应分析：[agent-sft-data-synthesis](agent-sft-data-synthesis.md)
- 数据配比：[data-mixture-comparison](data-mixture-comparison.md)

## 8. 第二档：blog-level / closed-weights 信号

> 这一档**不进主线共识表**：要么没有 TR、要么 TR-equivalent 的 blog 没披露 data pipeline。仅记录"frontier 阵营存在哪些方向信号"，所有 claim confidence ≤ medium，引用必须落到具体 source。

### 8.1 Qwen3.5 / 3.6 / 3.7（Qwen 主线）

- **Qwen3.5（2026-02，blog bundle）**[blog-qwen35]：架构换代（hybrid attention 3:1 + 高稀疏 MoE 397B-A17B + native multimodal early fusion + MTP + 词表 250k/201 语言）。Agent / 视觉 agent claim 提到 mobile/PC 操作、视觉编程、空间智能，**data pipeline 未公开**；只能写"Qwen 主线在 3.5 把 visual agent 提到产品级"。
  - 对本报告的方向信号：**native multimodal early fusion** 暗示 agent trajectory 里 screenshot / UI 状态可能是原生 token 而非 post-hoc adapter 输入；与 Anthropic Computer Use / OpenAI Operator 的 GUI agent trajectory 形成 frontier 三方信号，但 Qwen 这边数据合成方式零披露。
- **Qwen3.6（2026-04，blog）**[blog-qwen36]：**Thinking Preservation** —— 多轮 / tool-use 中保留前几轮 reasoning chain。
  - 对本报告的方向信号：是 trajectory **数据 / serving 维度**的新方向：训练时 reasoning chain history 是否进入 packing、如何 mask、是否影响多轮 trajectory 的 reject 粒度——blog 未说清是 inference scaffolding 还是真改了 training format。这是与 Qwen3 thinking-mode-fusion 的明显增量。
- **Qwen3.7-Max preview（2026-05）**[preview-blog]：All-field Thinking + 35h agent claim，零 data pipeline 证据。仅作 framing trace，不进任何强结论。

### 8.2 Anthropic Claude 4.5（closed-weights，blog + system card）

证据来源：`sources/anthropic-claude/release-deltas/claude-4.5.md`；引用 `[blog-anth-...]`、`[sys-card-claude-4.5]`。

- **任务分解粒度（sub-agent / skill）**[blog-anth-sub-agents, blog-anth-skills]：把"复杂任务拆成多个专门 sub-agent + 可重用 skill"作为产品级机制 → 间接说明训练时 trajectory 偏 **多 agent 组合**而非 single-agent long trajectory。与 MiniMax AaaV"verifier 自己起 agent 调工具"是同一思路（用更多 agent 替代更复杂单点 verifier），但 Anthropic 把这个设计推到产品架构层。
- **Computer Use trajectory**[blog-anth-cu, sys-card-claude-4.5]：3.5 → 4.5 持续升级；blog 提了基于 screenshot + action 的 agent trajectory，**合成 / 筛选 pipeline 零披露**。可作为"frontier 级 GUI agent trajectory 数据存在"的存在性证据。
- **Reward hacking / agentic safety eval**[sys-card-claude-4.5]：system card 公开多种 agent 误用 / hack 模式（窃取 secrets、escape sandbox、misalign tool use）。**这是 evaluation 文件不是 training pipeline**——和 GLM-5.2 anti-hacking 形成对照：GLM 公开**机制**（in-training），Claude 公开**现象目录**（deployment-time 评测）。

### 8.3 OpenAI Operator / ChatGPT Agent（closed-weights，blog + system card）

证据来源：`sources/openai-frontier/release-deltas/operator.md`；引用 `[blog-oai-operator]`、`[sys-card-operator]`。

- **Browser agent trajectory 评测**[sys-card-operator]：frontier closed 阵营**第一个**把 long-horizon browser task 当主线 agent eval 的公开样本。
- **Prompt injection / external manipulation**[sys-card-operator]：system card 大篇幅讨论 web 第三方 prompt injection 的 attack surface 与 mitigation，是 GLM-5.2 anti-hacking 之外**第二个**公开的 agent-环境对抗工程证据来源；**但仍是 evaluation / deployment-time mitigation，不是 training pipeline**。
- **High-risk action confirmation**[blog-oai-operator]：高风险动作前 ask user，是 product-level safety scaffolding，间接暗示训练时存在"区分高低风险 action + 触发 confirmation"的 reward / refusal 设计——单独不能作 training 证据。

### 8.4 Google Gemini 2.5 / 3（closed-weights，paper + blog）

证据来源：`sources/google-gemini/release-deltas/gemini-2.5.md`、`sources/google-gemini/release-deltas/gemini-3.md`；引用 `[paper-gemini-2.5]`、`[blog-dm-...]`、`[model-card-...]`。

**Gemini 2.5（paper-level，§8 内证据强度最高）**

- **Long-horizon web/agent eval（Mariner-style）**[paper-gemini-2.5]：closed 阵营**唯一**有 paper page anchor 的 agent eval 公开材料。可作为 OpenAI Operator system card / Anthropic Computer Use 的 paper 对照样本。
- **Long context + multimodal 联合 eval**[paper-gemini-2.5]：paper 给 audio / video / 大码库的 needle-in-haystack 类评测，间接说明训练时可能混合长序列与 multimodal token；**合成 pipeline 仍未公开**。
- **Deep Think 模式**[paper-gemini-2.5]：把 extended reasoning 当独立模式 + 切换 cost 公开。是 Qwen3 thinking-mode-fusion / Qwen3.6 Thinking Preservation 的 closed 阵营 paper 对照样本——但 paper 没到 training recipe 层。
- **不能推出**：trajectory 来源、verifier、RL recipe、Mariner 训练数据是否真用 Mariner-style trajectory——零公开。

**Gemini 3（blog-only，disclosure 退步信号）**

- **Antigravity（agent IDE）**[blog-google-antigravity]：与 Claude Code / Codex 形成 frontier coding-agent 三方对照样本。product framing 暗示 multi-agent / 任务分解组织，**training data 零披露**。
- **Long-horizon agent / Deep Research / Mariner 升级**[blog-dm-gemini-3]：blog 提到能力提升，但**没有** 2.5 paper 那种评测 page anchor。
- **Disclosure 退步本身是信号**：Gemini 1.5 → 2.5 → 3 的公开材料从 paper 退到 blog-only。这与 Anthropic / OpenAI / Meta 的 closed 阵营路径合起来看，提示 **frontier closed 阵营整体在收敛到 blog + system card 的 disclosure floor**。如果这个趋势持续，agent data 公开实践将主要由开源阵营（Qwen / GLM / DeepSeek / Kimi / MiniMax / Step）支撑。这条本身可以作为本报告的元结论之一。
- **不能推出**：Gemini 3 任何 training recipe / Antigravity trajectory 数据 / Deep Think 在 3 上的机制变化。

### 8.5 Meta frontier（Llama 4 / Avocado）

证据来源：`sources/meta-frontier/release-deltas/llama-4.md`、`sources/meta-frontier/release-deltas/avocado.md`。

- **Llama 4**：agent / tool use 在 model card 有提及，**data pipeline 零披露**；benchmark gaming 与长 context 复现失败使其 disclosure 可信度偏低。仅作"frontier 阵营 disclosure 下限"参考，**不进 current-practice**。
- **Avocado (codename, 2026 H1)**：rumor 级，零可用证据。仅占位。

### 8.6 第二档信号汇总：哪些值得拉进 lens / 后续跟踪

| 信号 | 来源 | 与第一档共识的关系 |
|---|---|---|
| GUI / browser trajectory 是 frontier 现役主线 | Anthropic Computer Use / OpenAI Operator / Qwen3.5 visual agent | 第一档 TR 没人公开 GUI trajectory 合成 pipeline，是公开缺口 |
| 多 agent / sub-agent 组合替代单点 verifier | Anthropic sub-agents/skills | 与 MiniMax AaaV 同思路；前者推到产品层，后者在 pipeline 内 |
| Reasoning chain 跨轮保留 | Qwen3.6 Thinking Preservation | 第一档 TR 没有；是 trajectory packing / mask 的新维度 |
| Anti-hacking 在评测层 vs 训练层 | OpenAI Operator system card vs GLM-5.2 blog | 形成两条工程路径的对照样本 |
| Frontier 阵营 disclosure 下限 | Meta Llama 4 | 提示 disclosure 不是技术能力的代理，frontier ≠ open about training |
| Frontier closed 阵营 disclosure 整体退化 | Gemini 1.5/2.5 paper → 3 blog-only；Anthropic / OpenAI 一直 system card-only；Meta paper → frontier blog | 元结论：未来 agent data 公开实践主要由开源阵营支撑 |

### 8.7 第二档专属开放问题

- frontier closed 阵营是否真在用第一档 TR 共识的 reject-only pipeline？还是有 in-training repair / DPO-style preference learning 在数据层？零证据。
- GUI / browser trajectory 数据规模、人类示范 vs synthetic 比例、verifier 形态——**所有 frontier closed 厂商都未公开**。
- Qwen3.6 Thinking Preservation 是 inference scaffolding 还是 training format 改动？无法确认。
- Avocado / Meta 后续若公开 frontier reset 的训练 post-mortem，会显著改变本报告的 frontier disclosure 边界判断；目前无证据。
