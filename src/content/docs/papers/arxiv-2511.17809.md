---
title: "Adaptive Layer-Wise Transformations for Post-Training Quantization of Large Language Models"
description: "Large language models require significant computational resources for deployment, making quantization essential for practical applications."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2511.17809) · [PDF](https://arxiv.org/pdf/2511.17809)

## 一句话摘要

Large language models require significant computational resources for deployment, making quantization essential for practical applications.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models require significant computational resources for deployment, making quantization essential for practical applications. However, the main obstacle to effective quantization lies in systematic outliers in activations and weights, which cause substantial LLM performance degradation, especially at low-bit settings. While existing transformation-based methods like affine and rotation transformations successfully mitigate outliers, they apply the homogeneous transformation setting, i.e., using the same transformation types across all layers, ignoring the heterogeneous distribution characteristics within LLMs. In this paper, we propose an adaptive transformation selection framework that systematically determines optimal transformations on a per-layer basis. To this end, we first formulate transformation selection as a differentiable optimization problem to achieve the accurate transformation type for each layer. However, searching for optimal layer-wise transformations for every model is computationally expensive. To this end, we establish the connection between weight distribution kurtosis and accurate transformation type. Specifically, we propose an outlier-guided layer selection method using robust $z$-score normalization that achieves comparable performance to differentiable search with significantly reduced overhead. Comprehensive experiments on LLaMA family models demonstrate that our adaptive approach consistently outperforms the widely-used fixed transformation settings. For example, our method achieves an improvement of up to 4.58 perplexity points and a 2.11% gain in average six-task zero-shot accuracy under aggressive W3A3KV2 quantization settings for the LLaMA-3-8B model compared to the current best existing method, FlatQuant, demonstrating the necessity of heterogeneous transformation selection for optimal LLM quantization.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Cuong Pham, Hoang Anh Dung, Cuong C. Nguyen, Trung Le, Gustavo Carneiro, Jianfei Cai, Thanh-Toan Do
- 发布：2026-11-17；更新：2026-11-17
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
