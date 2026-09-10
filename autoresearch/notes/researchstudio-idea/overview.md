# ResearchStudio-Idea source dossier

> 唯一入口。对象：[ResearchStudio-Idea](https://github.com/microsoft/ResearchStudio/tree/298ca64ae5e3f242d58278601db34bfa6daa53b8/ResearchStudio-Idea)，源码快照固定于 `298ca64ae5e3f242d58278601db34bfa6daa53b8`（2026-07-22）。论文镜像：[researchstudio-idea-2607.04439.pdf](../../papers/researchstudio-idea-2607.04439.pdf)。

## 一句话定位

**事实**：ResearchStudio-Idea 是 Microsoft Research 等团队发布的、运行在 Claude Code 或 Codex 中的 research-ideation skill suite。核心 `IdeaSpark` 把“给一个研究方向”编排成：检索近邻工作、重建 bottleneck、用会议结果归纳出的 pattern 生成一个候选、查撞车、审计、输出 idea card。它止于 idea 和实现性说明，不执行实验。[论文 pp. 30–35, §13](../../papers/researchstudio-idea-2607.04439.pdf)；[IdeaSpark runbook](https://github.com/microsoft/ResearchStudio/blob/298ca64ae5e3f242d58278601db34bfa6daa53b8/ResearchStudio-Idea/skills/idea_spark/SKILL.md)

**判断**：它不是“会科研的独立模型”，而是把检索、结构化中间件、多个隔离 LLM 调用和确定性 gate 串起来的 **idea compiler**。它值得研究的重点不是 15 个 pattern 名称本身，而是 `evidence → bottleneck → operator → candidate → collision/audit` 这一可审计编译链。

## 适用边界

- **适合**：已有可检索近邻文献的 ML method idea；用户想把模糊方向压成一个可反驳、可实现的 proposal。
- **不适合**：单篇论文总结、跨十年 survey、代码调试、纯自由联想，以及以 dataset/benchmark/system construction 为主体的项目；runbook 对这些情况明确提供 `do_not_generate` 路由。[runbook: When NOT to use / Phase 1](https://github.com/microsoft/ResearchStudio/blob/298ca64ae5e3f242d58278601db34bfa6daa53b8/ResearchStudio-Idea/skills/idea_spark/SKILL.md)
- **不覆盖**：真正的 code implementation、GPU experiment、结果到 claim、论文投稿。论文也把“止于一张 idea card”作为设计边界。[论文 p. 9, §2.6；pp. 30–35, §13](../../papers/researchstudio-idea-2607.04439.pdf)

## 怎么安装、怎么调用

**事实**：官方根仓库提供两条安装路径：clone 后运行 `bash install.sh`，或 `npx github:microsoft/ResearchStudio`；二者把 skills 安装/链接到宿主。官方声明 skills 运行在 Claude Code 与 Codex，推荐模型不低于 Claude Opus 4.6 或 GPT-5.5。[固定 commit 的根 README](https://github.com/microsoft/ResearchStudio/blob/298ca64ae5e3f242d58278601db34bfa6daa53b8/README.md)

安装后的典型入口是让宿主调用 `/idea-spark`。源码层的 canonical loop 则是：

```bash
python3 "$SKILL_DIR/scripts/run.py" next \
  --dir "$RUN_DIR" \
  --query "<research question>"
```

`next` 只读已有 artifacts，每次发出一个 Bash step 或 isolated LLM step，直至 `DONE`、`do_not_generate` 或 `phase_3_failed`；因此中断后可以从磁盘状态恢复。[runbook: the `next` loop](https://github.com/microsoft/ResearchStudio/blob/298ca64ae5e3f242d58278601db34bfa6daa53b8/ResearchStudio-Idea/skills/idea_spark/SKILL.md)；[navigator implementation](https://github.com/microsoft/ResearchStudio/blob/298ca64ae5e3f242d58278601db34bfa6daa53b8/ResearchStudio-Idea/skills/idea_spark/scripts/next_step.py)

## 是否靠 API，成本在哪里

**事实**：它不是一个“只付一次订阅就完全离线”的系统。运行需要：

1. 宿主 LLM 多次推理；Phase 1、2、2.3、3.2、4.fill、4.1.5 等被要求使用 fresh/isolated context。
2. 外部检索连接器：arXiv、OpenAlex、Semantic Scholar、OpenReview；部分配置需要 Semantic Scholar key 与 OpenReview credentials。
3. PDF/full-text 下载与解析；可选 LaTeX renderer。

`NOVELTY_LLM_REASONING_LARGE_CMD` 与 `NOVELTY_LLM_CLASSIFY_FAST_CMD` 允许接入任意宿主/子进程模型；没有这些命令时，宿主 agent 自己完成 LLM step。因此 **是否额外按 API token 计费取决于宿主和路由**，但总推理成本不会消失。runbook 自报完整中间状态约 180–250k tokens，并建议 pattern tagging 用便宜模型；这只是工程预算提示，不是标准化成本测量。[runbook: Context discipline / Configuration](https://github.com/microsoft/ResearchStudio/blob/298ca64ae5e3f242d58278601db34bfa6daa53b8/ResearchStudio-Idea/skills/idea_spark/SKILL.md)

**判断**：如果直接全程用昂贵 API frontier model，成本确实偏高；在 Codex/Claude Code 已有订阅额度、把 tagging/derive 分流到便宜 tier、利用 full-text cache 时更合理。首轮采用应先跑 1–3 个真实方向，记录每 phase 的 token、wall time、检索失败率，不能用作者的抽象 token 描述代替自己的账单。

## 总体流程：严肃版

1. **离线知识构造**：从 2021–2025 ICLR/ICML/NeurIPS 的 Oral、High-Cited、Reject 结果构建 1,947-paper corpus；将论文抽成 domain-agnostic innovation signatures，经 embedding、UMAP、HDBSCAN 得到 31 clusters，再由 LLM 归为 15 patterns 与 31 subpatterns。[详见 pattern-induction.md](pattern-induction.md)
2. **Phase 0 — evidence acquisition**：4–6 个 mechanism-first query 从四个连接器拉取约 40–45 个 metadata records；对至多 15 个高相关候选加用户引用抓 full text。
3. **Phase 1 — bottleneck reconstruction**：不是统计几十篇里哪个词最多，而是用近邻方法的“已解决部分 + 残余限制”重建一个有至少两条 paper-id 支撑的 bottleneck；证据不足则终止。
4. **Phase 2 — pattern composition + generation**：把 anchor gap 映射到 pattern/subpattern，默认组合至少两个相互依赖的 move，只生成一个带 premise、机制、naive baseline、falsification 和 budget 的候选。
5. **Phase 2.3 / 3 — adversarial gates**：fresh context 做 coherence trace 与数值 dry run；另一路按 mechanism signature 和跨社区 alias 查撞车；audit 检查 reject lesson、pattern 是否真被执行、anti-pattern、具体威胁论文与 falsification。
6. **Phase 4 — rendering**：确定性 skeleton 填机械字段，LLM 只写 prose TODO；再做 implementability audit、validators、渲染三种 card。全程不跑实验。[详见 runtime-pipeline.md](runtime-pipeline.md)

## 总体流程：通俗版

把它想成一个有质检工位的“idea 装配线”：

1. 先找一批最近在解决同一难题的人；
2. 不是问“还有什么没人做”，而是追问“这些解法为什么到这里就卡住”；
3. 从过去高价值论文常用的解题动作里挑两个能接起来的动作；
4. 只造一个方案，写清它凭什么工作、最朴素替代是什么、什么结果会判它失败；
5. 换一个上下文算一遍它会不会退化，再换关键词查别人是否已做过；
6. 有洞就只补洞，补不动就放弃，而不是靠润色把它包装成“新颖”。

## 维护状态快照（2026-07-22）

**事实**：仓库 2026-07-03 公开，审计日主分支为 `298ca64…`，GitHub 页面显示 47 commits、约 1.6k stars、96 forks，无正式 GitHub release；主分支当天仍有提交。以上只能说明活跃采用与快速迭代，不能说明 scientific validity。[GitHub operational snapshot](https://github.com/microsoft/ResearchStudio)

**开放问题**：项目太新，尚缺跨版本 taxonomy stability、第三方真实运行复现、human expert blind evaluation、以及从 idea 到实验结果的成功率证据。

## 本 dossier 导航

- [pattern-induction.md](pattern-induction.md)：15 patterns / 31 subpatterns 到底如何产生，accepted/rejected contrast 与 forced classification 的风险。
- [runtime-pipeline.md](runtime-pipeline.md)：运行时检索、bottleneck、composition、collision、audit，以及哪些是代码 gate、哪些仍是 LLM judgment。
- [evaluation-and-adoption.md](evaluation-and-adoption.md)：评价协议、SOTA 边界、与现有 cards/failure-mode 系统怎么接。

