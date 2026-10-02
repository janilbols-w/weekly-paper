---
title: "FedFit: Federated Fine-Tuning of LLMs via Vector-Bank Parameterization and Quantization"
description: "Federated Learning (FL) enables privacy-preserving fine-tuning of Large Language Models (LLMs), yet the massive communication overhead remains a critical bottleneck."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2610.01537) · [PDF](https://arxiv.org/pdf/2610.01537)

## 一句话摘要

Federated Learning (FL) enables privacy-preserving fine-tuning of Large Language Models (LLMs), yet the massive communication overhead remains a critical bottleneck.

## 为什么值得关注

待编辑增强。

## 摘要原文

Federated Learning (FL) enables privacy-preserving fine-tuning of Large Language Models (LLMs), yet the massive communication overhead remains a critical bottleneck. Furthermore, applying Low-Rank Adaptation (LoRA) in FL faces a fundamental "aggregation dilemma" between the accurate Sum-of-Products (SoP) and the communication-efficient Product-of-Sums (PoS) implementations. To tackle these challenges, we propose FedFit. First, to significantly reduce communication overhead, we introduce a disjoint shared vector-bank parameterization that reconstructs high-dimensional adapter matrices from two compact and disjoint global vector banks. Second, to address the aggregation dilemma, we devise an alternating optimization schedule. By cycling between decoupled single-bank updates (which allow for accurate aggregation) and joint updates corrected by a Residual Spectral Aggregation mechanism, we resolve the conflict between SoP and PoS. Additionally, we integrate blockwise quantization with client-side error feedback to further compress the transmitted vectors. Furthermore, we establish theoretical convergence guarantees for the proposed algorithm. Extensive experiments on Qwen2.5 models demonstrate that FedFit achieves perplexity performance comparable to standard federated LoRA methods, while providing compression ratios up to 100x higher.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 8 |
| rigor | 7 |
| practical impact | 8 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Hang Zou, Chao Zhang, Yuzhi Yang, Yu Tian, Samson Lasaulce, Mérouane Debbah
- 发布：2026-10-01；更新：2026-10-02
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
