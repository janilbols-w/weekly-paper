---
title: "MAPLE: MoE Adaptive Plug-and-play Layer-wise Expert allocation"
description: "Sparsely-activated Mixture-of-Experts (MoE) Transformers universally fix the same number of routed experts across all layers, a convention that ignores the well-documented heterogeneity in layer-wise redundancy."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2608.15299) · [PDF](https://arxiv.org/pdf/2608.15299)

## 一句话摘要

Sparsely-activated Mixture-of-Experts (MoE) Transformers universally fix the same number of routed experts across all layers, a convention that ignores the well-documented heterogeneity in layer-wise redundancy.

## 为什么值得关注

待编辑增强。

## 摘要原文

Sparsely-activated Mixture-of-Experts (MoE) Transformers universally fix the same number of routed experts across all layers, a convention that ignores the well-documented heterogeneity in layer-wise redundancy. We demonstrate that this uniformity is systematically suboptimal and propose MAPLE, a plug-and-play framework that reallocates the routed-expert budget heterogeneously across layers of any pretrained MoE LLM, without modifying weights or requiring retraining. Our core contribution is a closed-form sensitivity-guided allocation: we probe each layer's response to variation in expert count, quantify sensitivity using three measures, and derive an analytically optimal budget assignment that directs capacity towards sensitive layers and absorbs reductions in redundant layers. This closed-form solution is further refined by a sensitivity-constrained genetic search that uses layer-wise sensitivity as a prior to guide exploration, yielding faster convergence and superior allocation quality. On four MoE models spanning different scales and architectures, MAPLE outperforms uniform and pruning-based baselines under a 75% routed-expert budget. Notably, on DeepSeek-MoE-16B, MAPLE uses only 75% of the experts yet surpasses the original 100% expert-uniform baseline on ARC-E, ARC-C, and BoolQ, improving accuracy from 65.09 to 71.40, 48.49 to 51.50, and 80.03 to 82.38, respectively. These accuracy gains translate into measured deployment efficiency: implementing MAPLE in SGLang reduces single-GPU end-to-end serving latency by 32.2% and improves throughput by 47.4%. These results show that well-designed heterogeneous allocation can be more effective than simply activating more experts, establishing it as a principled and practical axis for improving MoE efficiency.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Lie Li, Wen Li, Junxiao Shen, Gusheng Hu
- 发布：2026-08-18；更新：2026-08-19
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
