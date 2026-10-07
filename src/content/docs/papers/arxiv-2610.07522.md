---
title: "Activation Denoising: A Robustness View on Parallel vs Sequential LLM Quantization"
description: "Post-training quantization is a powerful tool for compressing large language models."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2610.07522) · [PDF](https://arxiv.org/pdf/2610.07522)

## 一句话摘要

Post-training quantization is a powerful tool for compressing large language models.

## 为什么值得关注

待编辑增强。

## 摘要原文

Post-training quantization is a powerful tool for compressing large language models. The most scalable methods quantize every layer in parallel, but quantization errors then compound through the residual stream, as no layer corrects for the errors of the layers before it. Sequential quantization accounts for this error compounding by re-calibrating each layer on the already-quantized outputs of its predecessors, yielding stronger results but at the cost of a serial schedule that becomes a bottleneck at scale. As a solution, we propose parallel quantization with activation denoising, which recovers much of the sequential benefit while keeping quantization fully parallel. Rather than re-calibrating layer-by-layer, we take a robustness perspective and model the upstream error as noise, regularizing to be robust to it through a preprocessing step followed by metric-weighted rounding. Applied at every layer, this regularization forms a depth-compounding smoothness penalty that dampens how strongly quantization errors amplify through the model. Unlike orthogonal rotations commonly used in quantization, which must preserve the model's function, we multiply the weights by a more general linear transformation. We find that the two are complementary and their effects compound. Empirically, our robustness regularization recovers a significant part of sequential quantization's benefit in a single parallel pass, at a fraction of its time. Overall, by treating compounding quantization errors as a robustness problem, we offer a principled foundation for more efficient and accurate LLM quantization at scale.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yan Scholten, Rachel Lawrence, James Hensman, Stephan G\"unnemann, Alicia Curth, Riccardo Grazzi
- 发布：2026-10-07；更新：2026-10-07
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
