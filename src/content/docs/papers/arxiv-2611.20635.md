---
title: "Contrastive Activation-Guided Zeroth-Order Preference Optimisation for Memory-Efficient LLM Alignment"
description: "Direct Preference Optimisation (DPO) simplifies reinforcement learning from human feedback, but still relies on traditional backpropagation and its associated activation-memory cost."
---

**评分：42/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2611.20635) · [PDF](https://arxiv.org/pdf/2611.20635)

## 一句话摘要

Direct Preference Optimisation (DPO) simplifies reinforcement learning from human feedback, but still relies on traditional backpropagation and its associated activation-memory cost.

## 为什么值得关注

待编辑增强。

## 摘要原文

Direct Preference Optimisation (DPO) simplifies reinforcement learning from human feedback, but still relies on traditional backpropagation and its associated activation-memory cost. Zeroth-order (ZO) optimisation avoids backpropagation, yet isotropic perturbations can produce noisy updates for preference objectives defined by differences between chosen and rejected responses. We introduce Contrastive Activation-guided Zeroth-Order Direct Preference Optimisation (CA-ZODPO), which constructs a low-rank search subspace from the activation discrepancy between the chosen and rejected responses in each preference pair. Perturbations are restricted to this subspace, while momentum is maintained in low-rank coordinates to preserve the memory advantages of ZO training. On Qwen2.5-1.5B with Anthropic HH-RLHF, CA-ZODPO outperforms common ZO baselines and remains competitive with first-order DPO in pairwise preference evaluation. It also reduces peak GPU memory by about 59\% at a sequence length of 2048 while retaining the sequence-length scaling behaviour of zeroth-order training.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu memory
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Weiyun Huang, Alessio Galatolo
- 发布：2026-11-17；更新：2026-11-17
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
