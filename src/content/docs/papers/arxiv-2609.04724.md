---
title: "FlexPosit: Tunable Fractional Precision for LLM Inference Accelerators"
description: "Large language models (LLMs) offer remarkable capabilities but impose prohibitive compute and energy costs."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2609.04724) · [PDF](https://arxiv.org/pdf/2609.04724)

## 一句话摘要

Large language models (LLMs) offer remarkable capabilities but impose prohibitive compute and energy costs.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models (LLMs) offer remarkable capabilities but impose prohibitive compute and energy costs. Quantization governs the trade-offs between accuracy and hardware efficiency across granularity and bit-width. Finer granularity (e.g., group-wise) provides high accuracy but incurs scaling and control overhead, while coarser granularity (e.g., channel-wise) has lower overhead but loses accuracy at low precision. Meanwhile, mixed-precision quantization exposes rich accuracy-efficiency trade-offs algorithmically, but existing LLM accelerators remain limited to discrete precision modes, leaving the fractional design space between them unexplored. FlexPosit bridges these gaps through co-design of Posit-based quantization and a precision-tunable bit-serial architecture. Algorithmically, FlexPosit employs distribution-aware quantization with hardware-aligned, sensitivity-guided mixed-precision allocation, leveraging the Posit format's tapered precision to achieve group-wise-like accuracy with channel-wise-like regularity. Architecturally, FlexPosit is a unified bit-serial systolic array with lightweight per-column decoders, unified Processing Elements (PEs), and a global precision controller, enabling tunable fractional precision while preserving fully regular systolic dataflow. Across diverse LLMs, FlexPosit achieves near-FP16 accuracy with sub-5-bit fractional weights. It achieves 1.8x higher throughput and 1.2x lower energy than BitMoD (group-wise quantization), and 1.5x higher throughput and 2.0x lower energy than OliVe (channel-wise quantization), establishing a new Pareto frontier for precision-tunable LLM acceleration.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: low precision, quantization
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Yimin Gao, Liangtao Dai, Jun Yin, Xinfei Guo, Mircea Stan
- 发布：2026-09-07；更新：2026-09-15
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
