---
title: "SQS: Bayesian DNN Compression through Sparse Quantized Sub-distributions"
description: "Compressing large-scale neural networks is essential for deploying models on resource-constrained devices."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2510.08999) · [PDF](https://arxiv.org/pdf/2510.08999)

## 一句话摘要

Compressing large-scale neural networks is essential for deploying models on resource-constrained devices.

## 为什么值得关注

待编辑增强。

## 摘要原文

Compressing large-scale neural networks is essential for deploying models on resource-constrained devices. Most existing methods adopt weight pruning or low-bit quantization individually, often resulting in suboptimal compression rates to preserve acceptable performance drops. We introduce a unified framework for simultaneous pruning and low-bit quantization via Bayesian variational learning (\method), which achieves higher compression rates than prior baselines while maintaining comparable performance. The key idea is to employ a spike-and-slab prior to induce sparsity and model quantized weights using Gaussian Mixture Models (GMMs) to enable low-bit precision. Due to the intractability of the objective involving spike-and-slab priors with GMMs, we derive an efficient approximation that facilitates effective compression with minimal accuracy loss. In theory, we provide a consistent result for our proposed variational approach to a sparse and quantized deep neural network. Extensive experiments on compressing ResNet, BERT-base, Llama3.2, and Qwen2.5 models show that our method achieves higher compression rates than a line of existing methods with comparable performance drops. Project page: https://comeusr.github.io/SQS_Webpage.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Ziyi Wang, Nan Jiang, Guang Lin, Qifan Song
- 发布：2026-09-09；更新：2026-09-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
