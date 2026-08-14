---
title: "NeurIPS 2026 · Workshop 议程观察"
description: "NeurIPS 2026 于 8 月 10 日公布 102 个 workshop 的正式初步名单；其中高效深度学习、分布式训练、Agent 系统、端侧模型与芯片设计形成了值得持续跟踪的 AI Infra 议程簇。"
---

> **2026-12-06 — 2026-12-13 · Sydney, Australia / Atlanta, United States / Paris, France**
> 状态：<span class="event-status event-status--upcoming"><span aria-hidden="true">🟡</span> 即将举行</span> · 重点议程 9 项 · 更新于 2026-08-14

[会议官网](https://neurips.cc/Conferences/2026) · [官方 Workshop 公告](https://blog.neurips.cc/2026/08/10/announcing-the-neurips-2026-workshops/)

## 一分钟结论

NeurIPS 2026 于 8 月 10 日公布 102 个 workshop 的正式初步名单；其中高效深度学习、分布式训练、Agent 系统、端侧模型与芯片设计形成了值得持续跟踪的 AI Infra 议程簇。

这次发布的价值在于给出了年末技术议程的结构化先验，而不是论文结论。最强信号集中在资源预算驱动的 agent、Agentic OS 抽象、跨数据中心训练、量化/稀疏/自适应推理，以及 ML 与系统、芯片的协同设计。

## 当前阶段

官方目前公布的是 workshop 名单与部分主办方议程。多场主题相关 workshop 的投稿截止日集中在 8 月 29 日前后，录用通知最晚为 9 月 29 日；NeurIPS 主会论文通知为 9 月 24 日。因此本次只做议程级调研，不收录或评分尚未录用的 workshop 投稿，也不把非归档 workshop 论文当作正式 proceedings。

## 官方规模

| 指标 | 官方数据 |
|---|---:|
| Workshop proposals | 477 |
| Valid proposals | 454 |
| Accepted workshops | 102 |
| Sydney | 48 |
| Sydney acceptance rate | 21.5% |
| Paris | 28 |
| Paris acceptance rate | 25.4% |
| Atlanta | 26 |
| Atlanta acceptance rate | 23.6% |

## 关键议程

| 环节 | 日期 / 地点 | 工程观察 |
|---|---|---|
| [DiffuLM — Diffusion Language Models](https://7amin.github.io/diffulm-neurips2026/) | 2026-12-12<br>Sydney | 聚焦并行解码、快速采样、长上下文 serving 与硬件感知系统；已公布 Stefano Ermon、Arash Vahdat、Itai Gat 等六位邀请演讲者。 |
| [On-Device Intelligence](https://odi2026.github.io/) | 2026-12-11/12（待定）<br>Sydney | 直接面向现实资源约束下的端侧 foundation model，是能耗、内存与本地部署交叉方向的观察窗口；具体讲题尚未公布。 |
| [Machine Learning for Systems](https://mlforsystems.org/) | 2026-12-11/12（待定）<br>Sydney | 同时讨论“用 ML 优化系统”与大模型训练、serving 的效率、可靠性和扩展性，并强调 benchmark、数据集、模拟器与可复现方法。 |
| [CODEC-FM — Collaborative, Open, and Decentralized Training](https://collaborative-open-decentralized-fomo.github.io/) | 2026-12-11/12（待定）<br>Sydney | 覆盖跨数据中心、低带宽并行、异构设备、容错与 straggler；已公布 Peter Richtárik、Max Ryabinin、Virginia Smith 等演讲者及 keynote、poster、panel 框架。 |
| [AgenticOS](https://agentic-fmos.github.io/) | 2026-12-12<br>Sydney | 把 agent 的内存、调度、路由、状态恢复、GPU autoscaling 和可观测性上升为 OS 层协同设计；Ion Stoica 将作 keynote，另有系统专题与 panel。 |
| [LIGHT — Lightweight Trustworthy Foundation Models](https://almaai-disi-unibo.github.io/neurips2026-light-smallModels/) | 2026-12-12/13（待定）<br>Paris | 以蒸馏、压缩、量化、剪枝和 runtime guarantee 推动小模型真实部署；安排研究 session、panel、poster，演讲题目仍待公布。 |
| [AI for Chip Design](https://neurips-ai-for-chip-design-2026.github.io/) | 2026-12-12<br>Paris | 连接 LLM/agent 与 HDL、EDA、验证、PPA 优化及开放 benchmark，适合跟踪 AI infra 的硬件设计闭环。 |
| [AXIOM — Foundations of Efficient Deep Learning](https://axiom-neurips2026.github.io/) | 2026-12-12<br>Paris | 用 scaling law、优化理论解释量化、稀疏、压缩、自适应推理和内存高效训练；已公布六场 vision talk、Grand Challenges 与 panel。 |
| [Resource-Aware Agentic AI](https://resource-aware-workshop.github.io/) | 2026-12-12/13（待定）<br>Atlanta | 把 compute、energy、memory、latency、tool cost 纳入 agent 规划、编排、上下文管理与评测；演讲者和最终日程尚未公布。 |

## 来源与核验范围

- [NeurIPS 2026 conference page](https://neurips.cc/Conferences/2026)（核验于 2026-08-14；核验三地会期、主会论文通知日期与官网公告入口）。
- [Official workshop announcement](https://blog.neurips.cc/2026/08/10/announcing-the-neurips-2026-workshops/)（核验于 2026-08-14；核验发布日期、102 个正式 workshop、分地数量、会期和投稿阶段）。
- [NeurIPS workshop guidance](https://neurips.cc/Conferences/2026/WorkshopsGuidance)（核验于 2026-08-14；核验 workshop 非归档属性及 9 月 29 日强制通知期限）。
- [DiffuLM official workshop site](https://7amin.github.io/diffulm-neurips2026/)（核验于 2026-08-14）。
- [ML for Systems official workshop site](https://mlforsystems.org/)（核验于 2026-08-14）。
- [CODEC-FM official workshop site](https://collaborative-open-decentralized-fomo.github.io/)（核验于 2026-08-14）。
- [AgenticOS official workshop site](https://agentic-fmos.github.io/)（核验于 2026-08-14）。
- [LIGHT official workshop site](https://almaai-disi-unibo.github.io/neurips2026-light-smallModels/)（核验于 2026-08-14）。
- [AI for Chip Design official workshop site](https://neurips-ai-for-chip-design-2026.github.io/)（核验于 2026-08-14）。
- [AXIOM official workshop site](https://axiom-neurips2026.github.io/)（核验于 2026-08-14）。
- [Resource-Aware Agentic AI official workshop site](https://resource-aware-workshop.github.io/)（核验于 2026-08-14）。

- 触发类型：`program_released`；来源摘要：`3edeef7735c5`。
- 本页记录的是 workshop 正式名单与主办方已公开议程，不把 workshop CFP 当作正式论文 proceedings。
- 尚未公布的讲题、录用论文与最终日程明确标为待更新，不据此推断性能结论或奖项。
