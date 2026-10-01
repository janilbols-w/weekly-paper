---
title: "Replay the Curvature: Accurate and Scalable NVFP4 Quantization for Large Language Model Inference"
description: "Large language models make weight storage and memory traffic major inference costs, motivating low-precision formats that represent each weight with only a few bits."
---

**评分：45/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2609.36654) · [PDF](https://arxiv.org/pdf/2609.36654)

## 一句话摘要

Large language models make weight storage and memory traffic major inference costs, motivating low-precision formats that represent each weight with only a few bits.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models make weight storage and memory traffic major inference costs, motivating low-precision formats that represent each weight with only a few bits. Such formats use a scale to map floating-point values into a small codebook; NVFP4 improves local range utilization by letting every 16 E2M1 weights share an E4M3 block scale. Choosing that scale is difficult in GPTQ because quantizing one column updates those that follow, so evaluating a block independently can misestimate its final reconstruction error. Large models pose a second challenge: full-precision weights, calibration activations, and second-order state cannot all remain on one accelerator, while assigning complete layers to devices leaves each time-consuming layer solve serial. We introduce \emph{Schur Replay}, a scale-selection algorithm that reproduces the GPTQ updates caused by each block scale and scores the resulting block error after accounting for compensation from unquantized columns. Separately, our execution infrastructure keeps only the active layer resident, tiers activations across device, host, and disk, retires full-precision layers after export, and distributes independent output rows across tensor-parallel ranks. Together, the algorithm and infrastructure attain $99.35\%$ and $100.84\%$ question-weighted recovery from BF16 across seven benchmarks on Qwen3.5-397B-A17B and Llama-3.3-70B-Instruct. On the 397B model, the infrastructure reduces measured per-layer time by $15.17\times$ over ModelOpt and $23.14\times$ over LLM Compressor, with lower memory used per GPU.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Ruiyi Ding, Jie Li, Kang He, Ziyan Liu, Chengru Song, Yuedong Xu, Yuan Cheng
- 发布：2026-09-30；更新：2026-10-01
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
