---
title: "A Time-Based Readout for Vector-Matrix Multiplication in Fully Analog Memristive SNNs"
description: "Artificial neural networks rely on vector-matrix multiplications (VMMs), whose implementation in von Neumann architectures is dominated by costly data movement between memory and processing units."
---

**评分：38/100** · AI 基础设施 > 训练与数据中心基础设施 > 能耗、成本与散热

[论文原文](https://arxiv.org/abs/2609.11713) · [PDF](https://arxiv.org/pdf/2609.11713)

## 一句话摘要

Artificial neural networks rely on vector-matrix multiplications (VMMs), whose implementation in von Neumann architectures is dominated by costly data movement between memory and processing units.

## 为什么值得关注

待编辑增强。

## 摘要原文

Artificial neural networks rely on vector-matrix multiplications (VMMs), whose implementation in von Neumann architectures is dominated by costly data movement between memory and processing units. Spiking neural networks (SNNs) mitigate this bottleneck by performing in-memory, analog VMMs using memristive crossbar arrays. However, conventional current-mode readout circuits incur significant area and power overhead. This work proposes a fully analog readout architecture based on voltage-to-time conversion of the VMM output. By sensing the column voltage, the proposed approach avoids current-mode summing and scaling circuitry, improving area and energy efficiency. Post-layout simulations of a 10x1 SNN implemented in a 130 nm CMOS technology validate the proposed architecture, while application to a trained 64x10 SNN for digit classification further demonstrates its feasibility for SNN inference.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: energy efficiency
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Elia Mateu-Barriendos, \'Alvaro G\'omez-Pau, Josep Rius, Daniel Arum\'i, Rosa Rodr\'iguez-Monta\~n\'es, Salvador Manich
- 发布：2026-09-11；更新：2026-09-11
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
