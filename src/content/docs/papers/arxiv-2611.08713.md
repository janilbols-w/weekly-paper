---
title: "ResServe: Accurate and Efficient FP4 LLM Inference with Residue Compensation"
description: "Block-scaled 4-bit floating-point (FP4) quantization reduces large language model inference costs but can degrade task quality."
---

**评分：46/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2611.08713) · [PDF](https://arxiv.org/pdf/2611.08713)

## 一句话摘要

Block-scaled 4-bit floating-point (FP4) quantization reduces large language model inference costs but can degrade task quality.

## 为什么值得关注

待编辑增强。

## 摘要原文

Block-scaled 4-bit floating-point (FP4) quantization reduces large language model inference costs but can degrade task quality. Higher-precision computation can mitigate this loss at the expense of some of the efficiency gains from FP4 inference. Narrow matrix computations common in decoding often leave spare hardware capacity for low-cost precision recovery. ResServe combines an FP4 activation base with an FP4-quantized residue representing information lost during quantization. It uses this spare capacity to compute the residue's contribution and combines results on-chip, avoiding extra result transfers. We apply this principle to linear layers and decode attention, while selective compensation limits added work when processing input prompts. On NVIDIA B200, compensated linear kernels using the NVFP4 format improve numerical precision while retaining latency close to uncompensated execution for the evaluated operations with few rows. In the evaluated NVFP4 inference configurations, ResServe adds at most 3.4% request-latency overhead over W4A4 and reduces request latency by 22.4-53.3% relative to W4A8. Across five models, code-generation accuracy improves over same-format uncompensated inference, with mean relative gains of 15.04% for NVFP4 and 53.57% for MXFP4.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 20 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: fp4, quantization, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Shuo Rong, Ruibo Fan, Jiawen Wen, Xiaowen Chu
- 发布：2026-11-09；更新：2026-11-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
