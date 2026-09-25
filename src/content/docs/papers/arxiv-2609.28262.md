---
title: "RAMP: Robust Adaptive Mixed-Precision Quantization for Edge CPU Vision Models"
description: "Deploying deep learning models on edge CPUs is bottlenecked by computational and memory constraints."
---

**评分：49/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2609.28262) · [PDF](https://arxiv.org/pdf/2609.28262)

## 一句话摘要

Deploying deep learning models on edge CPUs is bottlenecked by computational and memory constraints.

## 为什么值得关注

待编辑增强。

## 摘要原文

Deploying deep learning models on edge CPUs is bottlenecked by computational and memory constraints. Mixed-precision quantization promises to reduce inference latency while preserving accuracy. However, quantization affects different layer types in inconsistent ways, so identifying where accuracy loss is minimized and latency reduction is maximized is critical, as the effect accumulates over a full deployment into substantial savings or unacceptable task degradation. Such identification relies on sensitivity metrics, proxies that estimate layer-wise degradation without evaluating the task accuracy of every candidate policy. Nevertheless, widely used metrics fail systematically on modern architectures. We present a systematic empirical study of 13 sensitivity metrics for layer-wise INT8 quantization across four distinctly different neural networks, and validate the resulting policies on two ARM64 platforms. Gradient-based sensitivity methods fail on 4 out of 8 model-hardware configurations and weight-based statistics on 2. In contrast, the Jensen-Shannon Divergence achieves zero catastrophic failures, reliably isolating the layers that cannot be safely quantized. A sensitivity metric alone does not define a policy, and the fixed thresholds typically used for that step are fragile over the highly skewed distributions of modern architectures. We address this with K-Means clustering, achieving near-lossless accuracy and a mean speed-up of $1.81\times$ over the full-precision model. Finally, we reveal that excluding from quantization the layers whose speed-up is negligible, regardless of their sensitivity, can be counterproductive, as it induces computational graph fragmentation and disables operator fusion. Our results yield concrete allocation policies for practitioners and researchers deploying quantized vision models on heterogeneous edge CPUs, without GPU access or gradient computation.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 20 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 9 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: int8, quantization, quantized
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：David Población-Criado, Dario Garcia-Gasulla, Eduardo Quinones
- 发布：2026-09-23；更新：2026-09-24
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/davidpob99/ramp-mpq](https://github.com/davidpob99/ramp-mpq)
- 阅读深度：metadata
