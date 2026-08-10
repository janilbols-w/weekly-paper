---
title: "An Empirical Study of openPangu Quantization on Ascend NPUs"
description: "openPangu models are attractive targets for private and domestic large-language-model deployment, yet their robustness under aggressive post-training quantization on Ascend NPUs has not been systematically characterized."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2606.21257) · [PDF](https://arxiv.org/pdf/2606.21257)

## 一句话摘要

openPangu models are attractive targets for private and domestic large-language-model deployment, yet their robustness under aggressive post-training quantization on Ascend NPUs has not been systematically characterized.

## 为什么值得关注

待编辑增强。

## 摘要原文

openPangu models are attractive targets for private and domestic large-language-model deployment, yet their robustness under aggressive post-training quantization on Ascend NPUs has not been systematically characterized. This paper conducts a controlled empirical study of openPangu 1B and 7B models on Huawei Ascend 910B1 NPUs. We evaluate representative weight-only and weight-activation post-training quantization methods, including RTN, GPTQ, AWQ, SmoothQuant, GPTAQ, BiLLM, and SliM-LLM, under a unified calibration and evaluation protocol. Across 18 evaluation tasks, we find that 8-bit weight-only quantization is effectively lossless for both models, while 4-bit quantization remains practical for the 7B model but is visibly more harmful for the 1B model on reasoning, math, and code tasks. Ultra-low precision remains challenging: most 2-bit and binary settings collapse to near-random behavior, and W4A4 SmoothQuant produces non-finite perplexity in our evaluation. These results provide an NPU-oriented accuracy map for selecting openPangu quantization settings and highlight the persistent difficulty of extreme low-bit compression.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: low precision, quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Tong Shi, Jiacheng Wang, Hui Xie, Ying Li, Aishan Liu, Jinyang Guo, Xianglong Liu
- 发布：2026-08-10；更新：2026-08-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
