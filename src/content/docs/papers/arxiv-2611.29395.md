---
title: "BQDNA: Multi-Head Binary Spherical Quantization for Genomic Sequence Modeling"
description: "Decoding biological information from long, repetitive DNA remains challenging."
---

**评分：47/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2611.29395) · [PDF](https://arxiv.org/pdf/2611.29395)

## 一句话摘要

Decoding biological information from long, repetitive DNA remains challenging.

## 为什么值得关注

待编辑增强。

## 摘要原文

Decoding biological information from long, repetitive DNA remains challenging. Genomic language models (gLMs) often follow the conventional language-model pretrain-and-adapt paradigm. However, the lack of inherent semantic segmentation and prior rules makes hand-crafted tokenizers like k-mer and BPE suboptimal. We introduce context-aware \textbf{BQVAE} for scalar quantization of DNA and \textbf{BQDNA}, an autoregressive gLM supporting multi-head codebooks. Comprehensive experiments reveal that: (1) unique training dynamics of vector quantization in DNA space, including the importance of alignment between training corpus and downstream data. (2) superior performance of BQVAE over hand-crafted tokenizers and vanilla VQVAE. (3) remarkable cross-species generalization capability of BQDNA, which achieves state-of-the-art performance with merely 0.1B multi-species training for BQVAE and 1 epoch training on hg38 for BQDNA, outperforming gLMs pretrained with 10$\sim$100x more tokens. Our findings underscore the potential of learned vector quantization for genomic sequence representation. Code is available at https://github.com/Sophie10001b/BQDNA

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 8 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- quantitative claim detected
- code/artifact link detected

## 元数据

- 作者：Xudong Wang, Siwei Cheng, Haozhe Hu
- 发布：2026-11-22；更新：2026-11-24
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/Sophie10001b/BQDNA](https://github.com/Sophie10001b/BQDNA)
- 阅读深度：metadata
