---
title: "Accuracy is Not Enough: A Divergence-Based Approach to Evaluate Fidelity Loss in Quantized LLMs"
description: "Deployment of Large Language Models (LLMs) on memory-constrained edge devices relies heavily on aggressive post-training quantization."
---

**评分：49/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2609.07664) · [PDF](https://arxiv.org/pdf/2609.07664)

## 一句话摘要

Deployment of Large Language Models (LLMs) on memory-constrained edge devices relies heavily on aggressive post-training quantization.

## 为什么值得关注

待编辑增强。

## 摘要原文

Deployment of Large Language Models (LLMs) on memory-constrained edge devices relies heavily on aggressive post-training quantization. However, evaluating these models is largely based on zero-shot task accuracy, which depends solely on argmax predictions and is insensitive to changes in the underlying predictive distribution. Consequently, accuracy can exhibit unstable, non-monotonic behavior under progressive quantization, masking substantial fidelity loss relative to the BFloat16 (BF16) uncompressed base model and providing misleading deployment signals. We introduce a distribution-sensitive evaluation framework quantifying information loss in quantized LLMs as the divergence between full-vocabulary predictive distributions at the token decision boundary. We compute statistical distances, including Jensen-Shannon Divergence and Total Variation Distance, between outputs of full-precision and quantized models, enabling a fine-grained analysis of distributional shift. Using this framework, we quantify probability mass displacement and distributional drift relative to the BF16 reference, capturing predictive distribution changes not reflected in top-1 accuracy. We conduct a 120-run experimental matrix across five foundation architectures and four reasoning benchmarks under progressive quantization regimes, from uncompressed BF16 to Q2_K, providing a systematic fidelity analysis. Our results show divergence metrics generally increase under stronger quantization, complementing task accuracy with a fidelity signal. Across tested llama.cpp schemes, mixed-precision Q4_K generally yields lower divergence than uniform Q4_0 at similar memory footprints. These findings motivate distribution-aware evaluation as a practical diagnostic complement to task accuracy; they do not directly establish correctness, calibration, safety, or user-perceived quality.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 13 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Shahzeb Qamar, Lorenz Sparrenberg, Christian Bauckhage, Baha Rababah, Carson Leung, Murat Kantarcioglu, Cuneyt Gurcan Akcora, Rafet Sifa
- 发布：2026-09-09；更新：2026-09-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
