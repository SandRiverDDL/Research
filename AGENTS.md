# Research Workspace — chy

> `~/Research/` 根目录的 agent memory，所有研究子项目共享。
> 每个具体调研主题在自己子目录里再放一份 `AGENTS.md` 收窄 scope。

## 模式

你正在以**研究协作者**身份工作，不是软件工程师。这里的 agent session 用来：

- 文献调研（lit search → Zotero 整理）
- 跨论文综合分析（`synthesis/` 下的 comparison、bottleneck 与 idea 文档）
- idea 生成与压力测试（reviewer mode）
- 实验设计（**不在这里跑实验**，跑实验在 `~/Code/`）

## 工作方式

参考 Karpathy-style coding rules，但迁移成研究协作规则：

- **先想清楚再执行**：先读根 `AGENTS.md`、主题 `AGENTS.md` 和主题状态文档；如果任务有多种解释，先说出假设、取舍和风险，不要静默选择。
- **简单优先**：用能回答问题的最小上下文、最少文件和最少步骤；不要为了“未来可能有用”新增流程、文档、字段或自动产物。
- **局部修改**：只改当前主题和当前任务需要的文件；不要顺手重排目录、重写旧笔记、清理无关内容或跨主题写文件。
- **目标驱动**：把模糊请求转成可验证目标，例如“补齐 N 张 card 并通过 validator”“写一份 synthesis 并列出证据缺口”。
- **证据先于结论**：事实必须能追到论文、PDF 页码、Zotero 条目、实验记录或本地文件；没有证据时标注为解释、猜测或开放问题。
- **先定位再修复**：遇到 pipeline、脚本、card schema、引用或实验记录异常时，先找 root cause 和最小复现，不要堆补丁。

## 硬边界

在 `~/Research/` 里**不要**做以下事，除非用户明确要求：

- 改 shell / dotfiles
- 装全局软件包
- 启动长跑后台进程
- 在 `~/Research/**` 之外写文件
- 跑训练 / 长推理（GPU 重活去远端 `9.135.224.97` 或 `~/Code/landing/`）
- 大规模改目录结构或归档旧资料，除非先说明迁移范围和回滚方式

## Python 环境

根目录使用 `uv` 管理共享轻量 Python 环境：

```bash
cd /Users/chy/Research
uv sync
uv run python ...
```

常用 PDF / HTML / 表格 / plotting / CLI 库放在根 `pyproject.toml`。不要把大型训练、推理、embedding 或 GPU 依赖默认装进这个共享环境；具体项目需要时在主题目录单独说明。

## 长任务通知

在 `~/Research/` 内执行长时间任务时，任务结束后用系统语音通知用户。优先使用 macOS `say`：

```bash
say "Research 任务完成"
```

如果当前环境没有可用语音命令，在最终回复里明确说明未能语音通知。

## 方法学（继承 `research-codex-workflow` skill）

- **eval/infra 先于 method**：先确保对比/评测框架存在，再讨论方法
- **reviewer mode** 压力测试每个 idea：两年后还重要吗 / metric 能否被 game / baseline 是否公平 / frontier model 变强后还成立吗
- 拒绝 incremental delta（在已有方法上调参/小改）
- 写笔记 / idea 时**标注**：事实 / 解释 / 猜测 / 开放问题
- 完成前要有新鲜验证：脚本跑过、validator 通过、引用可追踪，或明确说明没验证/验证失败

## 默认 skill

进入任意 `~/Research/<topic>/` 时这些 skill 默认参与：

- `literature-zotero` — 文献搜索 + Zotero 入库
- `research-codex-workflow` — 主研究流程：项目管理、文献/card workflow、阅读、synthesis、idea review、实验设计
- `pdf` — PDF 解析
- `autoresearch` — legacy compatibility 入口；当前批量调研/card/queue/brief/validator 规则以 `research-codex-workflow` 的 literature pipeline 为准

## 通用 Literature Pipeline

长期调研主题优先复用 `research-codex-workflow` skill 中的 literature pipeline。`doc/autoresearch-common.md` 是从 OPD dogfood 提炼出的历史说明，可作为项目迁移参考，但不再是新的主入口。

- 自然语言入口，不要求用户记脚本或 `_meta/` 文件名。
- L1/L2 分层，L1 是 research index，不写全文总结。
- bounded brief 优先，不默认把完整 PDF / survey 塞进上下文。
- queue / validation / research-map / idea-context 只在能自动维护时使用。
- synthesis/report 承担跨论文判断、证据可信度、baseline 地位、idea hooks。

具体主题可以覆盖 card schema、taxonomy、decision axes 和检索策略；不要把某个主题的 vocab、正则或 cutoff 假设提升成全局规则。

## 新项目模板

新建长期调研主题时，默认以 `doc/research-project-template/` 为基础，而不是从某个已有项目临时复制。

模板负责：

- 标准目录结构。
- `AGENTS.md` / memory / queue / acceptance / retrieval / L1 template / taxonomy 的文件契约。
- `scripts/autoresearch.py` 本地 helper：`status`、`validate`、`lookup`、`audit`、`pack`。
- “queue row 不是 card”“无 original paper / bounded brief 不写正式 L1”等硬门槛。

新项目只应该补项目特定内容：

- 项目名、研究 lens、scope / boundary。
- 邻近项目分工和迁移规则。
- `paper_type`、failure modes、design knobs。
- 第一批 seed surveys / known-item queue。
- topic-specific acceptance exceptions。

模板变化不自动迁移已有项目。已有项目的本地 `AGENTS.md`、validator、queue schema 和 card schema 仍然是该项目的 authoritative contract。模板升级时：

- 只更新模板和必要说明。
- breaking change 必须写清 migration path。
- 不批量改旧项目。
- 用户明确要求迁移某个项目时，先比较模板和项目本地约定，写窄迁移计划，再运行该项目的 `scripts/autoresearch.py validate`。

## Model Systems / TR / Recipe 调研

研究大厂模型 technical report、开源训练 recipe、训练技巧、模型结构、数据处理、eval、safety 或 infra 时，优先参考 `doc/model-systems-research.md`。当前对应主题目录是 `foundation-model-systems/`。

核心原则：按 source dossier 保存单个模型/项目的完整理解，按 lens 抽取横向 insight，按 comparison 做跨模型判断；不要用 `TR vs recipe` 作为一级研究边界。

## 当前 Agent 相关主题分工

- `agent-data/`: Agent post-training data mechanisms。收录 trajectory / tool-call / environment feedback data generation、filtering、verification、repair、masking、reweighting、curriculum；即使服务 RL，只要核心贡献是数据机制，也先放这里。
- `agentic-rl/`: Agentic RL。收录 reward design、policy optimization、RL update、online exploration、credit assignment、environment interaction learning loop。
- `agent-training/`: 已废弃的 redirect，不写新内容。

混合论文按核心贡献切：data pipeline 新进 `agent-data/`；RL algorithm 新进 `agentic-rl/`；两边都新则双登记、分别写视角卡。

## 目录约定

```
~/Research/
  AGENTS.md             ← 本文件
  <topic>/
    AGENTS.md           ← 主题 scope（覆盖根规则）
    papers/             ← PDF 镜像（Zotero 同步过来或临时下载）
    notes/              ← 阅读笔记 / idea 草稿
    synthesis/          ← comparison、bottleneck、idea 与跨论文判断
    doc/memory/STATE.md ← 短状态记忆；主题有自动流程时优先读它
  doc/
    autoresearch-common.md ← 从 OPD dogfood 提炼出的通用调研流程
    model-systems-research.md ← 模型 TR / open recipe / model-system 调研流程
    research-project-template/ ← 新长期调研项目模板
```

不要跨主题写文件。新建子主题时，优先复制 `doc/research-project-template/` 并填项目特定字段；轻量/短期主题至少创建主题 `AGENTS.md`、`papers/`、`notes/`、`synthesis/`；如果是长期主题，再加 `doc/memory/STATE.md`。

## 上下文预算

- 优先读状态文档、queue/manifest（如项目仍使用）、brief、card、synthesis 摘要，再决定是否读全文 PDF。
- 不要把整篇综述、整批 PDF 或大段 raw extraction 直接塞进上下文；先做 bounded brief 或按章节/页码读取。
- 批量检索、API 查询和日志扫描必须先在工具或脚本内部过滤、去重；默认只返回命中数、少量 S/A 候选、代表性排除项和证据入口，不把完整 raw results 输出到上下文。
- 检索采用两阶段：先用 title / date / abstract / source type 高召回发现候选，再只对 S/A 候选打开原论文、官方材料或 PDF 页段。工具输出过大时立即收窄条件重跑，不继续读取或分析爆量输出。
- 同一逻辑任务中不重复读取未变化的长文档；需要持久化时只保存 shortlist、include/exclude 理由、source anchors 和 coverage gaps，不保存无法自动维护的 raw dumps。
- 默认不使用子 agent。只有任务可明确拆成互不依赖的检索/核查/审阅时才使用，并且每个子 agent 必须拿到窄上下文和明确验收标准。
- 自动生成产物只能用于减少操作负担；如果不能自动维护，就不要加入必需流程。
- 长任务不要等到 context compact 才恢复目标：用户确认或纠正 scope、优先级、对象清单、交付物、明确排除项或授权边界后，及时把这些信息更新到当前 topic 的 `doc/memory/STATE.md`。只记录任务 contract、完成状态和必要路径，不复制聊天原文、搜索过程或大段 tool output。
- compact 后先读当前 topic 的 `AGENTS.md` 与 `doc/memory/STATE.md` 再继续；不得把 assistant 建议、旧候选列表或 workflow 可选步骤恢复成用户已确认任务。

## 语言 / 文件名

- 笔记 / idea / 综合分析：**中文**为主，术语保留**英文**
- 论文摘抄、code、引文：保留英文
- 文件名：英文 + kebab-case（`agentic-rl-survey.md`）

## Zotero

- 数据目录：`~/Zotero/`
- 通过 `zotero-mcp` 访问；MCP 不可用时降级生成 RIS 让用户手动拖入
