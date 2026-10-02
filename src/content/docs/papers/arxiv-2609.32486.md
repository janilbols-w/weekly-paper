---
title: "Elastic Selective Spectral Hybrids for Train-Once, Export-Many Budgeted Inference"
description: "Deploying a language model under different computing and latency budgets calls for compact models with different quality-cost trade-offs."
---

**评分：46/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.32486) · [PDF](https://arxiv.org/pdf/2609.32486)

## 一句话摘要

Deploying a language model under different computing and latency budgets calls for compact models with different quality-cost trade-offs.

## 为什么值得关注

待编辑增强。

## 摘要原文

Deploying a language model under different computing and latency budgets calls for compact models with different quality-cost trade-offs. Towards this end, elastic spectral state space models provide ordered and temporally decomposed channels that can be truncated, but they are associated with linear time-invariant filters that cannot selectively preserve relevant past information or forget irrelevant information as the context evolves. To address this, we introduce the Elastic Selective Spectral Hybrid (ESSH), which realizes each Hankel spectral channel as an independent recurrent unit using fitted damped rotation modes. It also features an input-dependent decay and write/read gates that make temporal retention and state update input-dependent while preserving channel-wise truncation and a structured recurrence for efficient execution. ESSH combines these selective spectral mixers with sliding-window attention and jointly trains multiple capacities by reducing spectral-channel count and feed-forward width at different rates through a two-rate capacity map with full-model distillation. The resulting models support chunked parallel training and fused recurrent decoding while avoiding computation for discarded channels. At full capacity, ESSH achieves language-modeling quality comparable to similarly sized independently trained models, while smaller exports exhibit a smooth quality-cost trade-off. We validate the effectiveness of the proposed framework using language understanding, retrieval, cross-domain text, and DNA experiments, by assessing quality retention and the trade-off against independently trained and elastic baselines. At the 1.53B model configuration, fused batch-one decoding takes 1.37 ms per token on a B300, providing a 2.14-2.80x speedup over the tested Mamba-2 and Mamba-3 implementations and 3.03x over Transformer++ at matched parameter counts.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Dachuan Song, Chuchu Chen, Xuan Wang
- 发布：2026-09-26；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
