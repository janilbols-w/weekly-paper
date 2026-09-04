---
title: "Hardware Acceleration of Block-Diffusion LLM for Edge Devices"
description: "Single-stream (batch-one) edge inference cannot amortize weight traffic across requests."
---

**评分：47/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.01084) · [PDF](https://arxiv.org/pdf/2609.01084)

## 一句话摘要

Single-stream (batch-one) edge inference cannot amortize weight traffic across requests.

## 为什么值得关注

待编辑增强。

## 摘要原文

Single-stream (batch-one) edge inference cannot amortize weight traffic across requests. Full-attention diffusion LLMs recompute the entire sequence at every step; native block diffusion makes completed blocks immutable and exactly cacheable, yet refinement still streams prefix KV and FFN weights. We co-design WIFiV-LPDDR, a wide-I/O LPDDR system for precision-tagged reads, BRQ-KV for a canonical low-rank-plus-INT8-residual prefix with query-dependent per-entry precision, and DAT-FFN for drift-mapped canonical replacement, adjacent-stage-corrected low-bit delta, or cached-state carry while keeping live activations unquantized. Both map to an input-stationary mixed-precision systolic array. For the evaluated 1.5B/7B models on modeled Jetson-class platforms, the full stack provides arithmetic-mean energy-reduction factors of 3.79x/3.96x and arithmetic-mean latency speedups of 2.88x/4.44x at the reported DAT-FFN settings; every corresponding compressed model-benchmark score drops by less than one absolute percentage point from its baseline.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: compressed model
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Wei-Hsing Huang, Kiseok Lee, Ming-Yen Lee, Weiyu Sun, Cheng-Jhih Shih, Gayatri Tanksali, Arpit Khandelwal, Pin-Jun Chen, Yingyan Celine Lin, Shimeng Yu
- 发布：2026-09-01；更新：2026-09-02
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
