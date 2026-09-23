---
title: "HBQ: Hierarchical Scaling Block Quantization with Hardware-Efficiency-Aware Design for Accurate LLM Inference"
description: "Block Quantization (BQ) enables efficient LLM inference by quantizing both weights and activations, but its design space remains underexplored."
---

**评分：51/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2609.00450) · [PDF](https://arxiv.org/pdf/2609.00450)

## 一句话摘要

Block Quantization (BQ) enables efficient LLM inference by quantizing both weights and activations, but its design space remains underexplored.

## 为什么值得关注

待编辑增强。

## 摘要原文

Block Quantization (BQ) enables efficient LLM inference by quantizing both weights and activations, but its design space remains underexplored. Through hardware-accuracy design space exploration, we identify block size as a key trade-off: larger blocks improve hardware efficiency by amortizing dequantization and accumulation costs, but degrade accuracy. Motivated by this insight, we propose Hierarchical Block Quantization (HBQ), which combines large blocks with low-overhead significand (SIG) scaling for second-level quantization. SIG scaling effectively compensates for large-block quantization errors while accounting for distinct weight and activation distributions. HBQ-A achieves W4A16-level accuracy with W4A5 and lower area than NVFP4, while HBQ-E further reduces hardware cost by 17% while outperforming existing BQ methods in accuracy. We implement HBQ for weights, activations, and KV cache in a 28nm ASIC accelerator and introduce partial-sum BQ to reduce EMA energy. At comparable accuracy, HBQ achieves 2.3x/4.6x higher area/energy efficiency than state-of-the-art weight-only quantization and 1.6-3.3x lower system energy with 1.5-3x speedup over prior BQ methods. Our implementation is publicly available at: https://github.com/SeoLabCornell/HBQ.git.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 14 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- quantitative claim detected
- code/artifact link detected

## 元数据

- 作者：Chun-Ting Chen, Dongmin Han, Hangyeol Mun, Jake Hyun, Arnab Raha, Amit Agarwal, Mark Anders, Mohamed Abdelfattah, Jae-sun Seo
- 发布：2026-08-31；更新：2026-09-23
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/SeoLabCornell/HBQ.git](https://github.com/SeoLabCornell/HBQ.git)
- 阅读深度：metadata
