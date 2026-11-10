---
title: "Know What You Need: Efficient Activation Checkpointing"
description: "Large Language Model training is increasingly constrained by memory capacity."
---

**评分：42/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2611.09614) · [PDF](https://arxiv.org/pdf/2611.09614)

## 一句话摘要

Large Language Model training is increasingly constrained by memory capacity.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large Language Model training is increasingly constrained by memory capacity. Activation Checkpointing reduces activation memory by avoiding storing selected activations during the forward pass and rematerializing them during backpropagation, thereby trading memory savings for additional computation. Although this technique is essential for scaling model training, rematerialization can be prohibitively expensive, particularly for Transformer linear layers. Approximate computation could reduce this overhead, but conventional approaches either introduce errors that accumulate over the backward pass or fail to exploit information available from the initial forward pass. We introduce a novel approximate rematerialization method that can yield unbiased gradient estimates: using information collected during the initial forward pass, the method selectively recomputes only the most important layer components, either through greedy selection or randomized sketching. Ablation studies show that the resulting gradients closely match the exact gradients. When applied to feed-forward layers, attention layers, or both, our method can recompute only two-thirds of the layer components in a Llama-488M model, while increasing perplexity by just 1.7%, 1.2%, and 2.5%, respectively.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpointing
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Danyal Ahmed (MLIA), Edouard Oyallon (MLIA)
- 发布：2026-11-09；更新：2026-11-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
