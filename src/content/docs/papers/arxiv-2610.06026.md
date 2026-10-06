---
title: "Differentiable Bit-Widths: Co-optimizing Pruning and Quantization via SVD for Ultra-Efficient LLM Compression"
description: "SVD-based pruning and quantization have recently emerged as a promising strategy for the ultra-efficient compression of large language models."
---

**评分：47/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2610.06026) · [PDF](https://arxiv.org/pdf/2610.06026)

## 一句话摘要

SVD-based pruning and quantization have recently emerged as a promising strategy for the ultra-efficient compression of large language models.

## 为什么值得关注

待编辑增强。

## 摘要原文

SVD-based pruning and quantization have recently emerged as a promising strategy for the ultra-efficient compression of large language models. In these methods, compression is performed in two stages: components are first truncated, and the remaining ones are subsequently quantized. Although this decoupled pipeline benefits from both pruning and quantization, it requires separate optimization for each stage and fails to fully exploit their balance, which can lead to suboptimal performance under aggressive compression. To address this limitation, we propose a new LLM compression method that co-optimizes pruning and quantization in a unified framework. Our key idea is a differentiable method for learning component-wise bit-widths, allowing less important components to be assigned 0-bit precision and pruned away. Notably, our method performs favorably against two-stage baselines, even when subjected to extreme quantization settings ($1.61$ bits) designed for ultra-efficiency. Code: https://github.com/MMAI-Laboratory/DBW.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Hankyul Kang, Jongbin Ryu
- 发布：2026-10-06；更新：2026-10-06
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/MMAI-Laboratory/DBW](https://github.com/MMAI-Laboratory/DBW)
- 阅读深度：metadata
