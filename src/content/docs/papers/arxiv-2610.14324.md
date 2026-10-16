---
title: "EV-JEPA: Elastic V-JEPA for Any Device and Cross-Device Inference"
description: "Foundation models like V-JEPA are increasingly deployed across a heterogeneous edge-cloud continuum spanning smart glasses, phones, robots, and servers."
---

**评分：39/100** · AI 基础设施 > 训练与数据中心基础设施 > 容错与弹性

[论文原文](https://arxiv.org/abs/2610.14324) · [PDF](https://arxiv.org/pdf/2610.14324)

## 一句话摘要

Foundation models like V-JEPA are increasingly deployed across a heterogeneous edge-cloud continuum spanning smart glasses, phones, robots, and servers.

## 为什么值得关注

待编辑增强。

## 摘要原文

Foundation models like V-JEPA are increasingly deployed across a heterogeneous edge-cloud continuum spanning smart glasses, phones, robots, and servers. Yet, they are typically trained as rigid, fixed-capacity networks bound to one device, supporting neither reconfigurable compute budgets nor collaborative execution. Existing approaches address only one axis at a time: slimmable and NAS-based methods provide width elasticity but assume single-device inference, whereas split-computing methods enable cross-device collaboration only for fixed partitions and static capacities. We introduce Elastic V-JEPA (EV-JEPA), a single model trained once and deployable everywhere along the continuum. Its width is reconfigurable, and it is natively partitionable across heterogeneous devices. At its core is Transition-Aware Triplet Training (T3). At each step we pick a narrow and a wide width, and train three paths: each width alone, plus a hybrid path that runs the early layers narrow and the rest wide. The hybrid switch point is where one device hands off to another, so the same weights learn both single-device and cross-device execution. Across various benchmarks, EV-JEPA falls within 1 accuracy point of independently trained baselines while improving over previous elastic training approaches by up to 11 accuracy points. Narrow-to-wide cross-device hybrid execution recovers to within 1.1 points of the highest-capacity standalone model and supports many-to-one, any-to-any, and variable-split configurations. Finally, we show that the elastic principle extends beyond the backbone to an elastic token compression mechanism that exposes controllable trade-offs among on-device computation, latency, and accuracy.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: elastic training
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Anxhelo Diko, Jieyu Lin, Stefano Ambrogio, Ziyun Li, Mahmoud Assran, Th\'eo Moutakanni, Barbara De Salvo, Chiao Liu
- 发布：2026-10-16；更新：2026-10-16
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
