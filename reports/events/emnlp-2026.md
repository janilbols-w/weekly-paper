---
title: "EMNLP 2026 · 会议周议程导览"
description: "EMNLP 2026 于 10 月 24 日在布达佩斯开始，25 至 27 日为主会，28 至 29 日为 tutorial 与 workshop。本次会议周导览重点追踪 world model、开放语言模型研究、agent 可靠性与长时记忆、价值对齐、生产级 agent、高效 tokenization 和样本高效预训练。"
---

> **2026-10-24 — 2026-10-29 · Budapest, Hungary**
> 状态：<span class="event-status event-status--upcoming"><span aria-hidden="true">🟡</span> 即将举行</span> · 重点议程 12 项 · 更新于 2026-10-23

[会议官网](https://2026.emnlp.org/) · [官方议程](https://2026.emnlp.org/program/)

## 一分钟结论

EMNLP 2026 于 10 月 24 日在布达佩斯开始，25 至 27 日为主会，28 至 29 日为 tutorial 与 workshop。本次会议周导览重点追踪 world model、开放语言模型研究、agent 可靠性与长时记忆、价值对齐、生产级 agent、高效 tokenization 和样本高效预训练。

对 LLM efficient inference / AI Infra 最有用的信号不是未公开的论文排名，而是一条跨层议程：world model 与工具使用扩展 agent 能力，长时记忆、失败诊断和价值对齐限定生产可靠性，tokenization 和受限数据预训练则直接关联训练与推理成本。相关摘要仍是讲者与主办方对议题的描述，不作为已验证的性能结论。

## 当前阶段

本次命中 `event_week`：RUN_DATE 为大会正式开始前一天。官方已公布总议程、三场主会 keynote、两场 industry keynote、六场 tutorial 和 28 个 workshop；本周官方仓库更改主要是 workshop 时间提示、讲者简介与参会物流，没有新的研究议程发布。main、Findings、industry 与 demo 论文页均仍无条目，awards 页也只有空奖项栏目，ACL Anthology 尚无 EMNLP 2026 proceedings；因此保持论文覆盖与评分为 0，不推断录用规模或奖项归属。

## 官方规模

| 指标 | 官方数据 |
|---|---:|
| Conference days | 6 |
| Main conference days | 3 |
| Tutorials | 6 |
| Workshops | 28 |
| Main keynotes | 3 |
| Industry keynotes | 2 |

## 关键议程

| 环节 | 日期 / 地点 | 工程观察 |
|---|---|---|
| [Keynote — Towards AI that understands the Real World](https://2026.emnlp.org/program/keynotes/) | 2026-10-25 09:30-10:30 CEST<br>Main conference | Pascale Fung 从物理世界、人类意图与连续多模态数据出发讨论 world model，强调为推理、计划、记忆和行动建立超越 next-token prediction 的环境抽象。 |
| [Keynote — On the Value of Open Research in Language Modeling](https://2026.emnlp.org/program/keynotes/) | 2026-10-26 15:15-16:15 CEST<br>Main conference | Graham Neubig 以对抗式辩论检视大模型的资源密集性、商业价值与开放发布之间的张力，直接关联 AI Infra 研究的可复现性和公开实验门槛。 |
| [Preliminary Report on the AI Reviewing Experiment](https://2026.emnlp.org/program/) | 2026-10-25 14:00-14:30 CEST<br>Main conference | 9 月 7 日新加入的独立报告环节，值得关注 AI 辅助审稿实验会公开哪些方法、失败模式与治理边界；详细材料尚未公布。 |
| [Panel: New Missions in NLP](https://2026.emnlp.org/program/) | 2026-10-25 14:30-15:30 CEST<br>Main conference | 9 月 7 日由 TBD 更新为正式主题；本次按最新总议程把时间校正到 10 月 25 日下午，嘉宾与问题清单仍待公布。 |
| [Keynote — AI for the Many: Starting from the World, Not the Model](https://2026.emnlp.org/program/keynotes/) | 2026-10-27 14:00-15:00 CEST<br>Main conference | Anna Korhonen 从真实世界需求、语言多样性和可用资源出发讨论 AI 研究取向；本次按最新总议程校正时间。 |
| [Industry Keynote — Agentic Challenges: Trustworthy Collaboration, World Discovery, and Long-Horizon Memory](https://2026.emnlp.org/program/industry/) | 2026-10-25 16:30-17:30 CEST<br>Industry track | Mohit Bansal 聚焦 agent 的可信多 agent 协作、技能与 world model 发现、长时记忆和 tool/computer use；这是 9 月 21 日官方提交明确重排的议程，具体方法与结果仍待演讲材料核验。 |
| [Industry Keynote — What are we aligning to? Positive Alignment for Value-based Agents](https://2026.emnlp.org/program/industry/) | 2026-10-26 09:00-10:30 CEST<br>Industry track | Verena Rieser 讨论 agent 在分布外情形下的价值推理、民主式原则提取与多 agent 协调失败，补充生产系统在能力之外的控制与评测边界。 |
| [Industry Track — Agents in Production and AI Agents in the Real World](https://2026.emnlp.org/program/industry/) | 2026-10-27 09:00-12:30 CEST<br>Industry track | 上午连续安排 Agents in Production、oral 与真实世界 agent panel，议题覆盖可靠性、控制、责任、价值和部署条件；官方尚未公布每篇 oral 的标题与材料。 |
| [Tutorial — Failure Modes in Agentic AI: From Reproducible Triggers and Diagnostics to Reliable Fixes](https://2026.emnlp.org/program/tutorials/) | 2026-10-28 09:00-12:30 CEST<br>Tutorials | 围绕 agent 失败的可复现触发、诊断和可靠修复建立系统化框架，与生产 agent 的评测、可观测性和恢复机制直接相关。 |
| [Tutorial — Tokenization for Large Language Models](https://2026.emnlp.org/program/tutorials/) | 2026-10-28 09:00-12:30 CEST<br>Tutorials | 从 tokenizer 设计、效率与多语言公平性切入，观察 tokenization 对训练成本、上下文长度和推理吞吐的系统影响。 |
| [BabyLM — Sample-Efficient Pretraining Workshop](https://2026.emnlp.org/program/workshops/) | 2026-10-29 09:00-17:30 CEST<br>Workshops | 以不超过 1 亿词等受限数据条件推动样本高效训练和可比较评测，适合跟踪小数据训练、规模律边界与低资源复现。 |
| [REALM — Workshop on Agent Language Models](https://2026.emnlp.org/program/workshops/) | 2026-10-29 09:00-17:30 CEST<br>Workshops | 面向 agent language model 的推理、规划、工具使用、记忆、交互和评估；最终 talk 与论文清单仍以主办方后续日程为准。 |

## 来源与核验范围

- [EMNLP 2026 official program overview](https://2026.emnlp.org/program/)（核验于 2026-10-23；核验 10 月 24 至 29 日总体结构、AI 审稿实验报告、New Missions in NLP panel、Best Paper Award 时段与主会日程）。
- [EMNLP 2026 official industry track](https://2026.emnlp.org/program/industry/)（核验于 2026-10-23；核验两场 industry keynote、Retrieval/RAG、Trust/Safety/Control、Agents in Production 与真实部署 panel）。
- [Official industry program update commit](https://github.com/acl-org/emnlp-2026/commit/bd259efc08c2d299999855d11d8376eb344a0a1a)（核验于 2026-09-25；核验 9 月 21 日 industry track 重排和 Mohit Bansal keynote 时段变更）。
- [Official keynote timing correction commit](https://github.com/acl-org/emnlp-2026/commit/6199e4a226f82bb8aab1651435c125bc74b88ada)（核验于 2026-09-25；核验 Mohit Bansal keynote 最终标注为 16:30 至 17:30）。
- [EMNLP 2026 official keynotes](https://2026.emnlp.org/program/keynotes/)（核验于 2026-10-23；核验三场主会 keynote、两场 industry keynote 的题目、摘要、讲者与时间）。
- [EMNLP 2026 official tutorials](https://2026.emnlp.org/program/tutorials/)（核验于 2026-10-23）。
- [EMNLP 2026 official workshops](https://2026.emnlp.org/program/workshops/)（核验于 2026-10-23）。
- [EMNLP 2026 main papers page](https://2026.emnlp.org/program/main_papers/)（核验于 2026-10-23；main、Findings、industry 与 demo 页面均只有标题、无论文条目，故不作为论文全集或 proceedings 证据）。
- [EMNLP 2026 official awards page](https://2026.emnlp.org/program/awards/)（核验于 2026-10-23；奖项栏目已建立但获奖内容为空；10 月 27 日的 Best Paper Award 仅是未来议程时段）。
- [ACL Anthology EMNLP 2026 event index](https://aclanthology.org/events/emnlp-2026/)（核验于 2026-10-23；截至 RUN_DATE 无可核验的 EMNLP 2026 proceedings 条目）。
- [EMNLP 2026 official repository history](https://github.com/acl-org/emnlp-2026/commits/main/)（核验于 2026-10-23；核验本周变更仅涉及 workshop 时间提示、panelist 简介、演讲指南和物流链接，未发布论文全集或奖项结果）。

- 触发类型：`event_week`；来源摘要：`ea56cc101f0d`。
- 本页是会议周议程导览，不把 keynote、tutorial 或 workshop 描述当作同行评审论文结论。
- 官网四类论文页均无条目，ACL Anthology 也尚无可核验的 2026 proceedings，因此论文覆盖与评分均保持为 0。
- 官方仓库本周的变更属日程提示、简介与参会物流修正；不另立 `program_released` 触发，也不把演讲摘要中的方法方向当作已发表结果。
- Workshop 与 tutorial 数量来自官方列表的逐项计数；房间、讲者细节和最终时间仍可能更新。
