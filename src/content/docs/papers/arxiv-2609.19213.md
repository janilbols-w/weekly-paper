---
title: "Layer-wise Curriculum Learning for Efficient LLM Compression"
description: "In this paper, we introduce layer-wise curriculum learning for efficient LLM compression."
---

**评分：41/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2609.19213) · [PDF](https://arxiv.org/pdf/2609.19213)

## 一句话摘要

In this paper, we introduce layer-wise curriculum learning for efficient LLM compression.

## 为什么值得关注

待编辑增强。

## 摘要原文

In this paper, we introduce layer-wise curriculum learning for efficient LLM compression. The proposed method facilitates the knowledge transfer from the teacher model to the student model, utilizing a curriculum learning approach that begins with easier optimization tasks and progressively tackles harder ones. In order to adopt the layer-wise learning in LLM compression, we partition the whole model into multiple segments consisting of layers, thereby enabling more computationally efficient knowledge transfer for LLMs. Based on our theoretical analysis of cumulative error phenomenon, layer-wise curriculum learning accelerates convergence while stabilizing the knowledge transfer process. In addition, we present a feature caching method with a multi-threading strategy to efficiently address feature misalignment across layers, maximizing GPU utilization. Consequently, our method exhibits advanced model compression performance, as well as high computational efficiency in terms of minimized memory usage and short training hours. Experiments on multiple datasets show that the proposed method achieves state-of-the-art performance while reducing GPU memory usage and training hours by more than 50\% on BERT and GPT-2. Moreover, it outperforms the other pruning methods on LLaMA-family and Qwen models under the same training hours, with a lower GPU memory footprint.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu memory
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Donggeon Lee, Dooyeon Na, Seungmin Oh, Jongbin Ryu
- 发布：2026-09-16；更新：2026-09-18
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
