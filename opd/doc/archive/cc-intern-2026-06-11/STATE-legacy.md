# OPD Autoresearch State (as of 2026-06-11)

> 给下个 cc session 看的状态文件。compact / new chat 后从这里恢复 context。
> 
> **最新状态补丁（2026-06-12）**：v2 pointer-only schema 已被推翻，当前进入 Codex autoresearch 流程。当前入口是 `doc/codex-research-process.md`；稳定决策见 `doc/memory/DECISIONS.md`；长期未决问题见 `doc/memory/OPEN-QUESTIONS.md`。旧 dogfood handoff 已归档到 `doc/archive/codex-dogfood-2026-06-12/`。

## 当前阶段

`lit-collection` → 第一轮 autoresearch 完成（部分），转入 schema 重构 + 补写。

## 已完成的工作

### 1. paper-summary skill 三套方法论确立

- **Surveys**：综述不写 L1，输出 queue 文件
- **Autoresearch Mode**：cc 读原文，chy 只审，verified 字段（a/s/r 三档）
- **Comparison tables**：YAML source-of-truth + markdown 派生表 + Dataview 给人用

详见 `~/.claude-internal/skills/paper-summary/SKILL.md`。

### 2. MCP 工具栈装好

- `arxiv` (uv tool, 命令 `arxiv-mcp-server --storage-path ~/.arxiv-mcp-storage`)
- `semantic-scholar` (uv tool, `semantic-scholar-fastmcp`)
- `openreview` (uv tool, `openreview-mcp-server`, no auth needed for public papers)

配置在 `~/.claude-internal/.claude.json` 的 `mcpServers`。

### 3. 综述提取（song-2026 OPD survey, arxiv 2604.00626）

完成产物：
- 三轴框架（Feedback Signal × Teacher Access × Granularity）— 章节框架不采纳
- 5 个 missing axes（divergence-direction / on-policy-degree / iteration-cadence / reward-source / trajectory-granularity）
- 25 篇 must-read paper list
- queue 文件**未落盘**（arxiv id 等数据已清洗，等本轮重跑后再写）

### 4. Phase 1 Autoresearch 三源并发 discover

- OpenReview / Semantic Scholar / arXiv 三源并发查询
- 总计 92 hits + 12 综述 seeds = 104
- python dedup（无 LLM）→ 94 篇
- 5 维 score → 35 篇 score≥3
- 缓存 28/29 papers 到 `~/.arxiv-mcp-storage/`

### 5. Phase 3 Write L1（部分成功）

- 29 篇并发跑 → **12 篇成功**，17 篇 schema 强制 StructuredOutput tool 失败
- 已落盘 `~/Research/opd/notes/` 12 张 .md（旧 schema，author-year 命名）
- opus cross-check 完成，找到 3 个真问题：
  - **ye-2026-policy 与 ye-2026-online 疑似同篇 paper 不同 instance**（dedup 漏）
  - **afsharrad** RL 负面结果与 R1/GAD 正面结果方向相反，需查
  - **yu-2026-multi** baseline 数字异常低

## 待办（按顺序）

1. ~~**改 L1 模板**（task #22）~~ ✅ 已完成
2. ~~**改 SKILL.md**（task #24）~~ ✅ 已完成
3. ~~**迁移 12 张已写卡片**（task #26）~~ ✅ 已完成（YAML 精简到 9 字段，但 decisions 大量 `unknown`，需 cc 重读论文填）
4. ~~**补写 17 篇失败论文**（task #28）~~ ✅ 已完成 — 实际是 15 篇有缓存 + 7 篇无 PDF（其中 1 dup 已合并）。本轮 workflow 并发跑 15 篇，11 直出成功；4 篇（tip/vicur/hdpo/distillm-2）公司代理 400 限流，串行重跑全部补齐。所有 27 张卡片落盘 `~/Research/opd/notes/`。
    - 注意：26_hdpo.md（49 行）/ 25_distillm-2.md（50 行）超出 30 行约束，但内容扎实，未压缩
    - 7 篇无 PDF 留待后续：yan-2025-luffy / xu-2025-kdrl / agrawal-2026-reinforcement / wu-2025-rethinking / khan-2025-dataenvgym / gao-2025-regressing / chen-2025-clarify
5. ~~**补 4 篇 cross-check 漏卡**~~ ✅ 已完成 — OPSD(2601.18734, meta-ucla)/Lightning OPD(2604.13010, nvidia)/REOPOLD(2603.11137, kaist-microsoft)/EOPD(2603.07079, ibm)。串行 sonnet 直出，全部 body ≤ 30 行（除 REOPOLD 32 行）。注：Lightning OPD 作者 affiliation 是 NVIDIA 不是 MIT，用户原"NV Lightning OPD"判断对，cross-check 之前误判。
6. **decisions 字段补全 12 张迁移卡片** — 这些卡片正文有 method 描述，让 sonnet 看正文抽 decisions（不需要重读 PDF）。同时修 cross-check 发现的 4 张 suspicious：26_global-token-filter / 26_multi-rollout-peer / 26_oprd（decisions 全 unknown 但正文写清）+ 25_taid（rollout 应填 offline）+ 26_internalize（signal 应填 logit 不是 outcome）
7. ~~**写 song-2026 survey 的 queue 文件**~~ ✅ 已落盘 `notes/26_opd-survey-queue.md`：56 篇 with arxiv_id + 10 篇缺 id，用 written/off-scope 31 篇做 negative list
8. ~~**更新 `~/Research/opd/CLAUDE.md`**~~ ✅ 旧 10 维 Comparison Dimensions 替换成 6 字段 decisions dict + 辅助 frontmatter；阶段从 `lit-collection` 改 `comparison`
9. ~~**修复 ye-2026-policy / ye-2026-online 疑似重复**~~ ✅ 验证非重复 — 同一组作者（Tianzhu Ye/MSRA）连续工作但分别是 OPCD 方法 paper（2602.12275）vs OEL 应用 paper（2603.16856，consolidation step 调用 OPCD），arxiv_id / 标题 / decisions 都分化，保留两张
10. ~~**scope 清理**~~ ✅ 已移 `25_deepseek-r1.md` + `26_rl-policy-distill.md` 到 `_meta/off-scope/`，frontmatter 加 `scope: off`
11. **覆盖 gap 待补**：cross-check 发现 preference signal / PRM step-level signal 几乎空白；hardness/curriculum filter 仅 2 篇代表（DistiLLM-2 + TAID）。需后续 search 补。

## 用户偏好（chy 在本次 session 拍板）

| 维度 | 决定 |
|---|---|
| 文件命名 | `<year短>_<method-shortname>.md`，如 `26_lightning-opd.md` |
| confidence | 数字 1-4（1 最高），不用 T1-T4 |
| org | 用 slug 字段（`openai`/`gdm`/`deepseek`/...），不用 affiliations 数组 |
| families | 删掉，改 **decisions dict**（决策点而非分类） |
| relevance | 删（写在 opd/ 目录就是相关） |
| reproducibility | 删（open_source + verified 已表达） |
| type | 删（看文件名/内容） |
| read_depth | 删（看文件名后缀 `-deep.md` 表示 L2） |
| score 5 维加权 | 改成 **4 类直接分类**（class S/A/B/C） |

### 4-class 分类（替代 score）

```python
def classify(p):
    fa = p.get('first_author','').lower()
    if any(name in fa for name in T1_T2_AUTHORS):    return 'S'  # 大厂
    if conf in venue and code_open:                   return 'A'  # 接受版+开源
    if (p.get('citation_count') or 0) > 50:           return 'A'  # 高引
    if p.get('year') == 2026 and topic_match:        return 'B'  # 近期 sota
    return 'C'  # 跳过
```

S + A 写 L1，B 进 queue，C 丢弃。

### decisions dict（决策点框架）

OPD 论文按 pipeline 步骤打 tag：

```yaml
decisions:
  rollout: student          # student | teacher | mixed | offline
  loss: reverse-kl          # forward-kl | jsd | adaptive-kl | advantage
  signal: logit             # outcome | preference | verifier
  iteration: one-shot       # iterative | continuous
  filter: none              # score-threshold | hardness | curriculum
  extra: none               # privileged-info | verbal-feedback | hint
```

grep `loss: reverse-kl` 等价于 SQL where——这是 autoresearch 真正能给研究员的杠杆。

## 关键文件位置

```
~/Research/opd/
  AGENTS.md                      # OPD topic-local agent rules
  CLAUDE.md                      # cc-intern legacy project memory
  doc/
    codex-research-process.md    # current Codex workflow and directory map
    templates/l1-card.md         # current L1 card contract
    taxonomy/failure-modes.md    # addresses controlled vocab
    memory/
      STATE.md                   # 本文件；handoff / 项目状态
      DECISIONS.md               # stable decisions and rationale
      OPEN-QUESTIONS.md          # long-lived unresolved questions
  notes/                         # L1 paper cards
  papers/cache/                  # 空（论文 cache 在 ~/.arxiv-mcp-storage/）
  _meta/
    generated/                   # manifest / target queue / validation reports
    briefs/papers/               # bounded paper snippets
    briefs/surveys/              # bounded survey mention windows
    raw/                         # discovery JSON, scored lists, dedup log, workflow result
    off-scope/                   # out-of-scope notes retained for audit

~/.arxiv-mcp-storage/             # 27 个论文 markdown，autoresearch 复用
~/.claude-internal/skills/paper-summary/
  SKILL.md
  templates/L1-base.md / L2-base.md / ext-{method,recipe,eval,mechanistic}.md
  scripts/cache-papers.sh        # bash + curl + pandoc 预热缓存
```

## 不要重做的事

- ❌ 重新跑三源 discover（已有 104 hits 在 `_meta/raw/discover-hits-raw.json`）
- ❌ 重新 dedup（已有 94 篇在 `_meta/raw/papers-94-scored.json`）
- ❌ 重新缓存 27 个 paper PDF（已在 `~/.arxiv-mcp-storage/`）
- ❌ 重新提取综述 taxonomy（已在 `_meta/raw/workflow-result-2026-06-11.json` 之前的 wf_5d2bee35-360 任务输出）

## 已知 bug / 坑

1. **slug 重复**：`zhang-2025-aligndistil` 和 `zhang-2025-aligndistil-aligndistil` 都进了 list（python 自动 disambiguate 加了后缀）。新命名规则会消除。
2. **author 解析问题**：sonnet 处理 100+ 引用时出现 `Cao Cao` / `Fan Fan` last-name 复用，原始数据需 enrich 校验。
3. **schema StructuredOutput tool 失败率 ~60%**：sonnet 写完 markdown 直接 stop 不 submit。修法：去 schema，agent 直接 return markdown 字符串。

## 下一 session 的第一句话建议

> "继续 OPD autoresearch。读 doc/memory/STATE.md 恢复 context，按待办顺序执行：先改 L1 模板，再迁移 12 张，最后补 17 篇。"
