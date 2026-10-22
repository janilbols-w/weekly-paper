---
title: "InfoQuant: Shaping Activation Distributions for Low-Bit LLM Quantization"
description: "Low-bit activation quantization remains a major bottleneck in efficient large language model (LLM) deployment."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2605.26175) · [PDF](https://arxiv.org/pdf/2605.26175)

## 一句话摘要

Low-bit activation quantization remains a major bottleneck in efficient large language model (LLM) deployment.

## 为什么值得关注

待编辑增强。

## 摘要原文

Low-bit activation quantization remains a major bottleneck in efficient large language model (LLM) deployment. The difficulty is not only that activations contain outliers, but that their distributions are often poorly matched to a low-bit uniform quantizer. Existing post-training quantization (PTQ) methods suppress peaks, balance channels, or minimize reconstruction error, yet they rarely specify what activation distribution is actually easy to discretize. As a result, activations may appear numerically smoother while still incurring large quantization error because the quantization range remains wide or most values collapse into a few levels near the mean. We recast activation transformation as quantizer-facing distribution design and analyze quantization error from an information-theoretic perspective. Our analysis shows that quantization-friendly activations should jointly have a smaller numerical range and sufficient dispersion within that range. Guided by this analysis, we propose InfoQuant, a train-free method that employs Peak Suppression Orthogonal Transformation (PSOT) to shape activations into more quantization-friendly distributions. We further introduce adaptive outlier-token selection to improve the robustness of PSOT during optimization. Across multiple LLM families, InfoQuant consistently outperforms prior PTQ and end-to-end training baselines. Under W4A4KV4, it preserves 97% of floating-point accuracy on average and reduces the LLaMA-2 13B performance gap by 42% over the previous state of the art. Code is available at [https://github.com/LLIKKE/InfoQuant](https://github.com/LLIKKE/InfoQuant)

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Ke Li, Dong An, Xiaoling Zang, Can Ye, Liang Xie, Qibo Qiu, Chen Shen, Xiaofei He, Wenxiao Wang
- 发布：2026-10-22；更新：2026-10-22
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/LLIKKE/InfoQuant](https://github.com/LLIKKE/InfoQuant)
- 阅读深度：metadata
