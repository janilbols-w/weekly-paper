---
title: "Resource-Efficient Pruning for Transformer via Low-Rank Importance Estimation"
description: "With the rapid development of large-scale pre-trained language models based on Transformer architectures, their high computational and memory costs have become a major obstacle to deployment, especially in resource-constrained environments."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2608.24973) · [PDF](https://arxiv.org/pdf/2608.24973)

## 一句话摘要

With the rapid development of large-scale pre-trained language models based on Transformer architectures, their high computational and memory costs have become a major obstacle to deployment, especially in resource-constrained environments.

## 为什么值得关注

待编辑增强。

## 摘要原文

With the rapid development of large-scale pre-trained language models based on Transformer architectures, their high computational and memory costs have become a major obstacle to deployment, especially in resource-constrained environments. Traditional pruning methods typically depend on full gradient-based importance estimation, and they necessitate prior finetuning of the model to achieve satisfactory performance. This process often results in intolerable resource consumption. This paper proposes REP-LIE, a new approach to enable resource-efficient pruning during the process of finetuning. REP-LIE leverages the gradients of LoRA low-rank matrices to estimate the importance of weights without requiring full gradient computation. To address the inherent randomness in importance estimation, a stability score is introduced, serving as the basis for iterative pruning of unimportant model parameters. The pruned model is further finetuned through lightweight updates, eliminating the need for full-parameter optimization in the process of finetuning. Extensive experiments on both medium-scale encoder models and large-scale generative models (LLaMA-7B and Mistral-7B) demonstrate that REP-LIE still achieves competitive performance compared to existing approaches.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Peng Liu, Huibing Zeng, Yiqun Zhang, Yang Yi, Jigang Wu
- 发布：2026-08-27；更新：2026-08-27
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
