---
title: "Kernelized Parameter Sensitivity Atlases for Amortized Conditional Interpretability"
description: "Gradient-based attribution provides input-specific information about model parameters, but computing it via backpropagation for many samples is expensive, while static importance scores discard input dependence."
---

**评分：46/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2610.12737) · [PDF](https://arxiv.org/pdf/2610.12737)

## 一句话摘要

Gradient-based attribution provides input-specific information about model parameters, but computing it via backpropagation for many samples is expensive, while static importance scores discard input dependence.

## 为什么值得关注

待编辑增强。

## 摘要原文

Gradient-based attribution provides input-specific information about model parameters, but computing it via backpropagation for many samples is expensive, while static importance scores discard input dependence. We derive KPSA (Kernelized Parameter Sensitivity Atlas) from a block decomposition of the empirical neural tangent kernel. It measures normalized parameter-group sensitivity, embeds those sources in an explicit query space, and uses a lightweight kernel to estimate sensitivities for unseen inputs. We derive bounds that separate finite-source from irreducible representation error and give margin-based top-$k$ recovery. This paper studies two interpretability applications. Firstly, KPSA identifies parameter groups with high susceptibility to perturbations across vision, forecasting, and protein-modeling setups. Across a fivefold range of parameter budgets ($0.02$-$0.1\%$), its selected groups attain $39$-$85\%$ of the perturbation susceptibility of a first-order backpropagation oracle. In vision and forecasting, these parameter groups form sparse sensitivity circuits that extend across depth and vary systematically with the input. Secondly, we use KPSA on an activation-attribution problem for MLP features in transformers. It retains $81\%$ of the gap between a backpropagation oracle and a constant-sensitivity baseline on vision while increasing batched query-time throughput from 551 to 2,041 images/s and reducing peak GPU memory from 4.55 to 0.44GB. On the protein-modeling task, it recovers $68\%$ of this gap. An ablation of KPSA's kernel aggregation shows that nearest-neighbor retrieval in KPSA space can remain competitive. The empirics show that compact kernel atlases can store useful input-dependent parameter sensitivity while amortizing repeated gradient attribution, a step toward scalable conditional interpretability. Code can be found at https://github.com/Axym-Labs/kpsa .

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu memory
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Davide Wiest, Ahanaf Hasan Ariq, Abdul Monaf Chowdhury
- 发布：2026-10-12；更新：2026-10-12
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/Axym-Labs/kpsa](https://github.com/Axym-Labs/kpsa)
- 阅读深度：metadata
