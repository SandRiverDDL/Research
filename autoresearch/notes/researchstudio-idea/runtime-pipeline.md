# ResearchStudio-Idea：runtime pipeline

> 返回 [overview.md](overview.md)。源码固定于 [`298ca64…`](https://github.com/microsoft/ResearchStudio/tree/298ca64ae5e3f242d58278601db34bfa6daa53b8/ResearchStudio-Idea)。论文运行时描述见 [§13, pp. 30–35](../../papers/researchstudio-idea-2607.04439.pdf)。

## 先回答：代码实际执行到哪里

**事实**：`IdeaSpark` 不是一段单 prompt。`scripts/run.py` 提供 phase commands，`scripts/next_step.py` 根据磁盘 artifacts 发出下一步；检索、去重、full-text fetch、state routing、citation gate、revision merge、skeleton/assemble、validators 与 rendering 有 Python/bash 实现。真正需要语义判断的 Phase 1、2.1/2.2、2.3、3.2/3.3、4.fill、4.1.5 则由 host LLM 或配置的 subprocess LLM 按 system prompt 读写 JSON。[run.py](https://github.com/microsoft/ResearchStudio/blob/298ca64ae5e3f242d58278601db34bfa6daa53b8/ResearchStudio-Idea/skills/idea_spark/scripts/run.py)；[next_step.py](https://github.com/microsoft/ResearchStudio/blob/298ca64ae5e3f242d58278601db34bfa6daa53b8/ResearchStudio-Idea/skills/idea_spark/scripts/next_step.py)；[system prompts](https://github.com/microsoft/ResearchStudio/tree/298ca64ae5e3f242d58278601db34bfa6daa53b8/ResearchStudio-Idea/skills/idea_spark/references/system-prompts)

**判断**：这是“deterministic control plane + probabilistic reasoning workers”。代码能保证步骤被跑、字段存在、引用 ID 可解析、patch 不碰 guarded fields；代码不能保证 LLM 重建的 bottleneck 真是领域的因果瓶颈。

## Phase 0：第一轮检索

### 检索什么

**事实**：宿主先写 4–6 个 mechanism-first queries，其中至少一个用可能的 solution vocabulary 做 escape query。连接器分工：arXiv 0–6 months cap 10；OpenAlex 与 Semantic Scholar 6–24 months 各 cap 12/13、published-only；OpenReview 0–6 months cap 10、in-review。目标约 40–45 records，按 external IDs/title 去重。[runbook: Phase 0](https://github.com/microsoft/ResearchStudio/blob/298ca64ae5e3f242d58278601db34bfa6daa53b8/ResearchStudio-Idea/skills/idea_spark/SKILL.md)；[connector scripts](https://github.com/microsoft/ResearchStudio/tree/298ca64ae5e3f242d58278601db34bfa6daa53b8/ResearchStudio-Idea/skills/idea_spark/scripts)

接着 fast model 把每条记录标成 1–3 个 patterns，并写 `lit_table.md`。然后 mandatory full-text gate 选 U（用户指定，无上限）+ top-10 published + top-5 arXiv，最多 15 篇非用户文献，抓 introduction/method；失败降级为 abstract 并留 warning。

### “几十篇就能找到 bottleneck”准确吗

**解释**：不能把它理解为“40 篇足以发现一个领域的真正瓶颈”。40–45 是一个 **局部 frontier reconstruction budget**：先高召回找近邻，再精读约 15 篇，用它们重建当前方法谱系和 residual gaps。它寻找的是“对这个 query、这个时间窗、这些连接器而言可证据化的局部瓶颈”，不是全领域唯一 bottleneck。

**事实**：Phase 1 要求 bottleneck statement 内联至少两个 retrieved paper IDs；如果少于 5 篇真正相关、空间几乎空白、方向过宽/无 anchor、或任务是 benchmark/system construction，则应 `do_not_generate`。[bottleneck prompt](https://github.com/microsoft/ResearchStudio/blob/298ca64ae5e3f242d58278601db34bfa6daa53b8/ResearchStudio-Idea/skills/idea_spark/references/system-prompts/bottleneck_identify.txt)；[runbook: Phase 1](https://github.com/microsoft/ResearchStudio/blob/298ca64ae5e3f242d58278601db34bfa6daa53b8/ResearchStudio-Idea/skills/idea_spark/SKILL.md)

**风险**：query formulation、24-month window、full-text top-15 ranking 和模型已有知识都会造成盲区。尤其经典祖先方法可能只存在于 model memory，而不在 recent retrieved evidence 中。>=2 citations 是 provenance floor，不是因果充分性证明。

## Phase 1：bottleneck reconstruction

输出至少包含：

- `bottleneck_statement`；
- `closest_adjacent[]`：每篇已经解决什么、还剩什么；
- `what_phase_0_did_not_address[]`：结构性 gap 与 stakes；
- `state: proceed | do_not_generate`。

**解释：bottleneck 与 failure mode 的差别**：failure mode 是观察到的坏现象，例如“novelty hallucination”“metric 被 game”；bottleneck 是阻止性能/可信度继续前进的因果约束，例如“评价信号与真实科研价值同源且不可校准”。同一个 failure mode 可由多个 bottleneck 造成，一个 bottleneck也可产生多个 failure modes。IdeaSpark 需要 bottleneck，是因为 pattern 要作用在“可改变的约束”上，而不是只对症状起名字。

## Phase 2：gap × pattern composition → 一个 candidate

**事实**：Phase 2.1 先选择 anchor gap，再按 operational signature 判断 pattern fit；默认至少两个 pattern，且必须说明它们如何链式依赖。若一个 pattern 被移除而方案仍不变，则它只是 decorative sibling，不应保留。[ideate-select prompt](https://github.com/microsoft/ResearchStudio/blob/298ca64ae5e3f242d58278601db34bfa6daa53b8/ResearchStudio-Idea/skills/idea_spark/references/system-prompts/ideate_select.txt)

**事实**：Phase 2.2 只生成一个 candidate，不做 K-way ranking。关键字段包括 premises、gap closure、最强 naive baseline、mechanism/dataflow、相对近邻工作的 delta、`signature_terms`、跨社区 `alias_terms`、falsification/kill switch、资源预算。[ideate-generate prompt](https://github.com/microsoft/ResearchStudio/blob/298ca64ae5e3f242d58278601db34bfa6daa53b8/ResearchStudio-Idea/skills/idea_spark/references/system-prompts/ideate_generate.txt)；[design notes](https://github.com/microsoft/ResearchStudio/blob/298ca64ae5e3f242d58278601db34bfa6daa53b8/ResearchStudio-Idea/skills/idea_spark/references/design-notes.md)

随后 deterministic citation gate 检查 paper IDs 与 parent/subpattern 关系，但不判断内容是否真的正确。这也是为什么后面仍需 semantic audit。

## Phase 2.3：fresh-context coherence trace

**事实**：新的上下文拿 candidate 做：逐步 dataflow、最小 numeric dry run、degenerate probes、与 naive baseline 的独立比较、claim grading。歧义术语要按所有合理 reading 分别执行；blocking findings 作为独立文件交给 Phase 3 audit。修复是 patch-only，由 deterministic merger 合并，避免整份 candidate 被重写。[coherence prompt](https://github.com/microsoft/ResearchStudio/blob/298ca64ae5e3f242d58278601db34bfa6daa53b8/ResearchStudio-Idea/skills/idea_spark/references/system-prompts/coherence_trace.txt)；[merge_revisions.py](https://github.com/microsoft/ResearchStudio/blob/298ca64ae5e3f242d58278601db34bfa6daa53b8/ResearchStudio-Idea/skills/idea_spark/scripts/merge_revisions.py)

**判断**：这是整个系统比普通 “critique your idea” prompt 更实质的创新点之一：要求执行微型反例/数值 trace，并把执行证据跨上下文传给审计，而不是让生成模型自我解释。

## Phase 3.1：后续检索主要就是防撞车，但不只如此

**事实**：第一轮检索是 topic/frontier search；后续 collision search 是 candidate-specific：

- `signature_terms` 在最近 10 months 查相同机制表述；
- `alias_terms` 在 48 months 查另一个社区对同一机制的叫法。

完整命中保存在 `collision_hits.full.json`，audit-facing pool 以每 channel lexical relevance 截到 top 120；abstract 截短到 1,000 chars。[design notes: dual-channel collision](https://github.com/microsoft/ResearchStudio/blob/298ca64ae5e3f242d58278601db34bfa6daa53b8/ResearchStudio-Idea/skills/idea_spark/references/design-notes.md)；[phase3 collision implementation](https://github.com/microsoft/ResearchStudio/blob/298ca64ae5e3f242d58278601db34bfa6daa53b8/ResearchStudio-Idea/skills/idea_spark/scripts/gen_pipeline.py)

**解释**：后续检索有三项功能：查“已经一模一样”；找可能 subsume candidate 的祖先；把具体威胁论文送进 audit，迫使 candidate 写清 delta。它不是为了补一篇 related work 装饰引用。

**风险**：alias terms 本身由模型参数知识生成；真正未知的跨社区词汇仍可能漏掉。lexical truncation 是精度工程，不增加 recall。

## Phase 3.2–3.3：五项 audit 与有信息增益的 retry

**事实**：fresh audit 检查五项：

1. Reject lessons 是否命中；
2. subpattern recipe 是否真的被执行；
3. anti-pattern 是否被缓解；
4. 是否存在 paper-pointed threat；
5. falsification structure 是否完整。

输出 `advance | revise | abandon`。revise 仍是 patch-only；abandon 只有在失败产生了此前没有的 binding lesson 时才重试。预算最多 3 个 candidate cycles；若两个独立 mechanism 都被具体论文不可修复地 subsume，可做一次 bottleneck re-diagnosis，再给一次 candidate attempt。[critique prompt](https://github.com/microsoft/ResearchStudio/blob/298ca64ae5e3f242d58278601db34bfa6daa53b8/ResearchStudio-Idea/skills/idea_spark/references/system-prompts/critique.txt)；[design notes: information-gain retry](https://github.com/microsoft/ResearchStudio/blob/298ca64ae5e3f242d58278601db34bfa6daa53b8/ResearchStudio-Idea/skills/idea_spark/references/design-notes.md)

## Phase 4：card expansion，而非实验设计

**事实**：确定性 skeleton 先填引用、kill switch echo、join/group-by 等机械字段；LLM 填约 12 个 prose TODO；另一个 fresh implementing-engineer context 把 method steps 改到可编码粒度；validators 检查 completeness/readability/kill-switch integrity，最后渲染三种 cards。[phase4_skeleton.py](https://github.com/microsoft/ResearchStudio/blob/298ca64ae5e3f242d58278601db34bfa6daa53b8/ResearchStudio-Idea/skills/idea_spark/scripts/phase4_skeleton.py)；[validators](https://github.com/microsoft/ResearchStudio/tree/298ca64ae5e3f242d58278601db34bfa6daa53b8/ResearchStudio-Idea/skills/idea_spark/scripts/validators)

**边界**：官方明确不输出 experiment matrix、ablation plan、baseline table、expected figures，也不跑代码/训练。它给出 falsifiability 与 feasibility judgment，实验工程留给下游。[design notes: Output surface policy](https://github.com/microsoft/ResearchStudio/blob/298ca64ae5e3f242d58278601db34bfa6daa53b8/ResearchStudio-Idea/skills/idea_spark/references/design-notes.md)

## 流程的创新与普通之处

**普通**：retrieve → generate → critique → revise 本身非常常见；15 个高层 pattern（decompose、reframe、replace operator 等）也不是新科学理论。

**相对创新/工程贡献**：

- pattern cards 来自 accepted/HC/reject contrast，而非作者手写 brainstorm checklist；
- bottleneck、pattern、candidate、collision、audit 都有显式 artifact contract；
- fresh-context coherence trace 用可执行 dry run 对抗自洽幻觉；
- collision 采用 signature + cross-community alias 双通道；
- revision 被限制为 patch-only，retry 受 information gain 而非盲目 reroll 控制；
- deterministic state machine 让失败分支和恢复路径可检查。

**判断**：创新主要在 **harness design 与证据流约束**，不是某个新推理算法。觉得“流程普通”是对的；它的价值恰恰在于把普通但经常被省略的研究纪律做成难以绕开的工序。

