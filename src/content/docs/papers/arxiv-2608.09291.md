---
title: "UnionSparse: An Index-Efficient Sparsity Framework for Low-Bit Sparse LLM Inference on Edge"
description: "Edge LLM inference combines sparsity and low-bit quantization to meet device memory, latency, and power limits."
---

**评分：52/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2608.09291) · [PDF](https://arxiv.org/pdf/2608.09291)

## 一句话摘要

Edge LLM inference combines sparsity and low-bit quantization to meet device memory, latency, and power limits.

## 为什么值得关注

待编辑增强。

## 摘要原文

Edge LLM inference combines sparsity and low-bit quantization to meet device memory, latency, and power limits. Yet quantization shrinks weight payloads without proportionally reducing sparse metadata, so index traffic and nonzero extraction become critical SpMM bottlenecks. We introduce the Payload-to-Metadata Ratio (PMR) and show that improving PMR raises effective compute intensity in decoding. We present UnionSparse, an index-efficient framework that combines Index-Efficient Bitmap Encoding (IE-BME) with a SpMM kernel using Low-Bit Shared-Memory Parallel Decoding (LSPD). IE-BME amortizes metadata and aligns sparse traversal with fragment assembly, while LSPD improves small-batch execution. Under W4A4 quantization and 30%--70% sparsity, UnionSparse outperforms FlashLLM and SpInfer by 2.30x and 1.43x, and CUTLASS and cuBLAS Tensor Core by 1.56x and 3.46x, respectively. These results establish payload-extraction efficiency as a first-order concern for low-bit sparse inference on edge GPUs. Source code is available at: https://github.com/Victor-Alen/UnionSparse.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 7 |
| rigor | 5 |
| practical impact | 12 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: sparse inference, sparsity
- quantitative claim detected
- code/artifact link detected

## 元数据

- 作者：Tianhao Jiang, Hang Gu, Teng Wang, Qianyu Cheng, ZhenDong Zheng, Cheng Tang, Qiyue Su, Wenqi Lou, Lei Gong, Chao Wang, Xi Li, Xuehai Zhou
- 发布：2026-08-10；更新：2026-08-11
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/Victor-Alen/UnionSparse](https://github.com/Victor-Alen/UnionSparse)
- 阅读深度：metadata
