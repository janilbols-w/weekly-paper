---
title: "HBQ: Hierarchical Scaling Block Quantization with Hardware-Efficiency-Aware Design for Accurate LLM Inference"
description: "Block Quantization (BQ) is a promising approach for efficient deployment of large language models (LLMs), enabling low-precision computation with controlled accuracy degradation."
---

**评分：46/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2609.00450) · [PDF](https://arxiv.org/pdf/2609.00450)

## 一句话摘要

Block Quantization (BQ) is a promising approach for efficient deployment of large language models (LLMs), enabling low-precision computation with controlled accuracy degradation.

## 为什么值得关注

待编辑增强。

## 摘要原文

Block Quantization (BQ) is a promising approach for efficient deployment of large language models (LLMs), enabling low-precision computation with controlled accuracy degradation. Compared to scalar weight-only quantization (WoQ), BQ quantizes both weight and activation, offering higher hardware efficiency and end-to-end inference on a unified datapath, but its design space, spanning bit-width, block size, scaling, and numeric formats, remains underexplored. We provide hardware/benchmark results through design space exploration (DSE). We find that increasing block size improves hardware efficiency by amortizing dequantization and accumulation costs, but degrades accuracy. This trade-off limits conventional BQ methods. Motivated by this insight, we propose Hierarchical Block Quantization (HBQ). Unlike prior methods [1], [2], which use small blocks and conventional Power-of-Two (PoT) or integer-based scaling, HBQ uses large blocks to maximize efficiency and introduces low-overhead significand (SIG) scaling for second-level quantization. By allocating quantization levels effectively and accounting for distinct activation and weight distributions, SIG scaling compensates for large-block errors more effectively than prior PoT and INT schemes. HBQ-A (accurate) achieves W4A16-level accuracy using only W4A5 while requiring less silicon area than NVFP4. HBQ-E (efficient) further reduces hardware cost by 17% while maintaining higher accuracy than all existing BQ methods. We implemented a 28nm ASIC accelerator applying HBQ to weights, activations, and KV cache, and integrated a novel partial-sum BQ scheme to further reduce EMA energy. Compared to state-of-the-art WoQ, HBQ delivers $2.3\times$/$4.6\times$ higher area/energy efficiency at the same accuracy level; $1.6$--$3.3\times$ system energy reduction and $1.5$--$3.0\times$ speedup over prior BQ methods while providing best accuracy.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Chun-Ting Chen, Dongmin Han, Hangyeol Mun, Jake Hyun, Arnab Raha, Amit Agarwal, Mark Anders, Mohamed Abdelfattah, Jae-sun Seo
- 发布：2026-09-02；更新：2026-09-02
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
