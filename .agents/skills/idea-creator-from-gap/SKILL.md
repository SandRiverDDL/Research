---
name: idea-creator-from-gap
description: Generate and rank research ideas from a user-supplied gap using ARIS idea-creator, skipping its wiki-loading and landscape-survey phases. Use when the user already has a gap or literature synthesis and wants concrete solutions without repeating the preliminary survey. Questions about the workflow alone do not start idea generation.
---

# Idea Creator from Gap

这是 ARIS `idea-creator` 的局部覆盖入口。以用户提供的 gap 为起点，跳过上游 Phase 0、1，从 Phase 2 开始；后续流程复用上游，不复制维护另一套 idea-creator。

## 加载依赖

读取当前研究主题安装的 `.agents/skills/idea-creator/SKILL.md`；若不存在，使用当前会话可用的 `aris:idea-creator` skill。两者均不可用时，说明缺少上游依赖，不冒称已执行完整 ARIS 流程。安装恢复参考 Research 根目录的 [doc/aris-setup.md](../../../doc/aris-setup.md)。

读取上游后，先应用下面的覆盖规则，再执行其 Phase 2–7。上游引用的 shared references、review tracing 和 helper 按上游 skill 的真实目录及安装约定解析，不相对于本补丁目录解析。

## 输入与覆盖规则

- 输入为用户指定的 gap，以及用户提供或指定路径的背景、文献综合、证据与约束。可以只给 gap；不要为了补齐背景而自动恢复前置调研。
- 用户给出的 gap 是本次生成的研究问题，不自动视为已被证明的事实或已确认的新颖性。缺少证据的前提标为假设或开放问题。
- **跳过上游 Phase 0（Load Research Wiki）。** 不自动加载、重建或扫描 `query_pack.md`，不展开与当前 gap 无关的 wiki 论文、gap 或历史 idea；当前 gap 的已有文献上下文按下述输入规则读取。
- **跳过上游 Phase 1（Landscape Survey）。** 不扫描本地论文库，不做宽泛文献检索，不重建 landscape，不重新发现或扩展 gap；不因 wiki 新鲜度而补跑最近 3–6 个月检索。
- **复用已有 lit 产物是 Phase 2 的输入准备，不能随 Phase 0、1 一起跳过。** 对项目中已有的 gap，必须定位并读取对应的 gap map 条目、其链接的文献综合/完整分析，以及理解已有方法与判断边界所需的直接证据；可通过项目状态、索引和直接链接定位，不要求用户再次提供文件路径，不扫描或加载整个文献库。
- 在生成 lenses 前，将这些已有产物中的相关方法、已有覆盖与局限、证据边界，以及用户指定的 gap，填入 Phase 2 的 landscape / key gaps 上下文。跳过的是重新构建这些产物，不是省略其内容。若确实没有已有产物且用户只给了 gap，明确标注背景缺失，不编造领域共识，也不自动补跑前置调研。
- 不调用 `idea-discovery`，也不重新无条件调用完整 `idea-creator`；始终在本覆盖规则下执行上游后续阶段。

## 保留的后续流程

- Phase 2：先围绕给定 gap 生成 lenses 并展示给用户，必须让用户确认后续使用哪些 lenses；收到确认后，才按选定的 lenses 生成具体方法候选，沿用上游生成与审阅机制。
- Phase 3–4：保留去重、客观可行性判断、针对具体候选的相关工作检索、查新和批判审阅。跳过前置调研不等于关闭后续查新；查新若发现 gap 的前提不成立，应记录并反馈。
- Phase 5：按上游条件和当前项目的实验授权边界处理 pilot。不能把本 skill 的调用视为跨目录写入、训练或后台任务的额外授权；未运行的 pilot 标记为未验证。
- Phase 6–7：保留上游报告与 wiki 写回规则。Phase 7 写回不触发补跑 Phase 0。只使用输入中有据可查的 paper / gap ID，缺失时不编造关系。

当前项目的语言、输出路径和工作边界优先于上游默认值。不要把某个主题的约束固化为所有项目的统一要求。

报告简要注明：本次跳过上游 Phase 0、1，列出实际使用的 gap 与输入来源，并区分候选生成、查新和 pilot 各自的完成状态。

## 调用示例

```text
$idea-creator-from-gap
Gap：<具体研究问题>
背景材料：<可选，指定已有综述或文件路径>
约束：<可选，计算预算、研究视角或输出要求>
```
