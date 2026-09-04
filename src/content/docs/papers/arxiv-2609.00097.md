---
title: "Faster Than Flash: Exploiting Attention Sparsity for Efficient Long-Context Decoding"
description: "The development of long-context Large Language Models (LLMs) is constrained by the memory bandwidth bottleneck and quadratic complexity of the attention mechanism during decoding."
---

**评分：52/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.00097) · [PDF](https://arxiv.org/pdf/2609.00097)

## 一句话摘要

The development of long-context Large Language Models (LLMs) is constrained by the memory bandwidth bottleneck and quadratic complexity of the attention mechanism during decoding.

## 为什么值得关注

待编辑增强。

## 摘要原文

The development of long-context Large Language Models (LLMs) is constrained by the memory bandwidth bottleneck and quadratic complexity of the attention mechanism during decoding. To overcome the inherent trade-offs between the memory overhead of metadata-based metrics and the computational inefficiency of adaptive selection strategies, we present Faster Flash Decoding (FFD), a novel hardware-algorithm co-design framework designed to break the memory wall in long-context decoding. FFD integrates the selector and computer into a fully fused kernel, replacing external metadata indices with content-aware scanning via low-bit quantization. Furthermore, we introduce the top-delta strategy, which dynamically filters blocks to achieve distribution-adaptive sparsity without global synchronization. Offering a training-free and plug-and-play solution, FFD also enables the reuse of scanning results for computation, achieving up to 11.6x kernel-level speedup and scaling to 256K context length, with 2.37x end-to-end throughput improvement. Empirical validation on RULER and LongBench confirms that FFD maintains model accuracy while delivering high-ratio sparsity, with code available at https://github.com/qluoluo/faster-flash-decoding

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 5 |
| practical impact | 14 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: sparsity
- quantitative claim detected
- code/artifact link detected

## 元数据

- 作者：Zhigeng Liu, Zhiyuan Ning, Ruixiao Li, Xiaoran Liu, Yuerong Song, Min Zhang, Ziwei He, Xipeng Qiu
- 发布：2026-08-31；更新：2026-09-02
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/qluoluo/faster-flash-decoding](https://github.com/qluoluo/faster-flash-decoding)
- 阅读深度：metadata
