---
title: "MXCode: Vector Quantization for MX-Native Inference at Scale"
description: "Memory capacity and bandwidth are major bottlenecks in LLM inference, motivating weight compression beyond conventional 4-bit quantization."
---

**评分：49/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2611.00403) · [PDF](https://arxiv.org/pdf/2611.00403)

## 一句话摘要

Memory capacity and bandwidth are major bottlenecks in LLM inference, motivating weight compression beyond conventional 4-bit quantization.

## 为什么值得关注

待编辑增强。

## 摘要原文

Memory capacity and bandwidth are major bottlenecks in LLM inference, motivating weight compression beyond conventional 4-bit quantization. Vector quantization (VQ) enables approximately 2-bit weight storage but often relies on codebooks incompatible with native FP4 computation. We introduce MXCode (MX-Native Codebook Quantization), a framework bridging ultra-low-bit VQ compression with MicroXcaling (MX)-native FP4 computation. MXCode proposes three strategies: PostScale, which quantizes learned codebooks to MXFP4; PreScale, which extracts MX scales before codebook learning; and PreScale+, which further compresses these scales using VQ. These strategies explore tradeoffs among quantization quality, scale overhead, and codebook granularity. All reconstruct MX-native W4A4 operands without materializing intermediate high-precision weights. We evaluate MXCode on Qwen3 (235B), DeepSeek-R1 (671B), and GLM-5.2 (753B) using the Microsoft MX Emulation Library. MXCode achieves approximately 2 bits per weight with competitive, workload-dependent model quality. On GB300 hardware, experiments with Qwen3 (235B) show approximately 50% lower model-load memory than Native FP4 while maintaining near-Native-FP4 serving throughput. Under memory-constrained prefix reuse, P90 TTFT improves by up to 94.5%. These results demonstrate software-based reconstruction on existing FP4 hardware and inform the development of future MX-native inference systems.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: fp4, quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Gaurav Kolhe, Cansu Demirkiran, Shubhi Tyagi, Sulaiman Sadiq, Boyao Wang, Richard Wang, Maximiliana Behnke, Shreyas Labhsetwar, Levi Melnick, Matthew Mattina, Partha Maji
- 发布：2026-11-03；更新：2026-11-03
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
