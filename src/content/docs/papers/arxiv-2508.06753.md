---
title: "Pushing the Envelope of LLM Inference with Ultra-Low-Bit Quantized Models"
description: "The advent of ultra-low-bit LLM models, approaching the perplexity and task accuracy of their full precision counterparts, is ushering in a new era of LLM inference."
---

**评分：51/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2508.06753) · [PDF](https://arxiv.org/pdf/2508.06753)

## 一句话摘要

The advent of ultra-low-bit LLM models, approaching the perplexity and task accuracy of their full precision counterparts, is ushering in a new era of LLM inference.

## 为什么值得关注

待编辑增强。

## 摘要原文

The advent of ultra-low-bit LLM models, approaching the perplexity and task accuracy of their full precision counterparts, is ushering in a new era of LLM inference. While these advances promise models that are cost-effective regarding latency, memory, throughput, and energy consumption, the efficiency of runtimes for deploying ultra-low-bit models remains under-explored. In this work, we take a bottom-up approach: we first implement 2-bit microkernels for modern CPUs, achieving close-to-roofline performance. We integrate these microkernels into LLM inference pipelines and present end-to-end results with 2-bit models, outperforming the state-of-the-art (SOTA) bitnet.cpp runtime by 2.2$\times$, and deliver up to 7$\times$ speedup compared to 16-bit inference. We extend this work to Intel Xe2 GPUs where we implement mixed-precision, 2-bit kernels, and show their performance to be close-to-optimal. We integrated the GPU kernels in the vLLM framework and evaluated end-to-end inference for a range of models and Xe2 GPUs. We obtain up to 6.7$\times$ speedup compared to the 16-bit pipeline, pushing the envelope of LLM inference.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 17 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Evangelos Georganas, Dhiraj Kalamkar, Alexander Heinecke, Pradeep Dubey
- 发布：2026-08-28；更新：2026-08-28
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
