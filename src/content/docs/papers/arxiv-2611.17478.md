---
title: "ERGo: Energy-Efficient Hybrid Graph Neural Network Training on Processing-In-Memory Architectures"
description: "Processing-in-memory (PIM) has been proposed as an alternative computing paradigm for training Deep Neural Networks, including Graph Neural Networks (GNNs)."
---

**评分：47/100** · AI 基础设施 > 训练与数据中心基础设施 > 能耗、成本与散热

[论文原文](https://arxiv.org/abs/2611.17478) · [PDF](https://arxiv.org/pdf/2611.17478)

## 一句话摘要

Processing-in-memory (PIM) has been proposed as an alternative computing paradigm for training Deep Neural Networks, including Graph Neural Networks (GNNs).

## 为什么值得关注

待编辑增强。

## 摘要原文

Processing-in-memory (PIM) has been proposed as an alternative computing paradigm for training Deep Neural Networks, including Graph Neural Networks (GNNs). Despite these advancements, training GNN workloads on PIM devices necessitates off-chip memory access. This off-chip access is expensive in terms of performance and energy, thereby impacting the overall energy efficiency of the training process on PIM platforms. In this paper, we propose a novel hybrid training framework called ERGo that automatically switches from a full-parameter phase to a parameter-efficient phase during the training process with negligible loss in predictive accuracy. The parameter-efficient phase employs low-rank representations of GNN weights, effectively reducing the number of trainable parameters. This helps in reducing the off-chip access during the end-to-end training process on PIM architectures, leading to notable improvements in both performance and energy efficiency. ERGo outperforms the conventional full-parameter GNN training on a PIM-based platform by up to 3.15x in speedup and enhances energy efficiency by 10.5x. Furthermore, ERGo offers additional advantages when utilized on heterogeneous architectures incorporating non-volatile memory (NVM) and static random-access memory (SRAM). Training on the heterogeneous NVM-SRAM architecture typically utilizes NVM for the forward-pass and SRAM for the backward-pass. However, NVM cells suffer from low device endurance and repeated write operations due to weight updates can lead to poor lifetime. ERGo improves the lifetime of NVM devices by freezing the weights and preventing weight updates in the parameter-efficient phase. Experimental results demonstrate that ERGo improves the lifetime of heterogeneous NVM-SRAM architecture by up to 33x in comparison to full-parameter implementation.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: energy efficiency
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Pratyush Dhingra, Chibuike E. Ugwu, Janardhan Rao Doppa, Partha Pratim Pande
- 发布：2026-11-16；更新：2026-11-16
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
