---
title: "Accelerating Dense LLMs via L0-regularized Mixture-of-Experts"
description: "Large language models (LLMs) achieve strong performance but suffer from slow and costly inference."
---

**评分：46/100** · LLM 高效推理 > Serving 与分布式推理 > Batching 与请求调度

[论文原文](https://arxiv.org/abs/2609.21672) · [PDF](https://arxiv.org/pdf/2609.21672)

## 一句话摘要

Large language models (LLMs) achieve strong performance but suffer from slow and costly inference.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models (LLMs) achieve strong performance but suffer from slow and costly inference. Existing acceleration methods often lead to noticeable performance degradation, while Mixture-of-Experts (MoE) models require extensive computational resources. In this paper, we propose L0-MoE, a lightweight MoE approach using L0-regularization to accelerate dense LLMs nearly without performance loss. Our method introduces a cluster confusion matrix for domain-aware dataset curation and applies dynamic batching for efficient training. Experiments show that L0-MoE achieves up to 2.5x speedup over dense models while maintaining competitive performance, outperforming existing LLM acceleration baselines.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: dynamic batching
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Zhenyu Zhang, Jiudong Yang, Zhaowen Tao, Meng Chen
- 发布：2026-09-21；更新：2026-09-21
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
