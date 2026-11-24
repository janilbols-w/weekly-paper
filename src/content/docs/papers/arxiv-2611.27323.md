---
title: "Cruella: A Unified Microscaling and Floating-Point Dot-Product Unit for LLM Inference on FPGAs"
description: "The number formats that accelerators execute natively are fixed at fabrication, yet large language model (LLM) checkpoints are released with MXFP4 weights in the Microscaling (MX) formats standardized in 2023."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2611.27323) · [PDF](https://arxiv.org/pdf/2611.27323)

## 一句话摘要

The number formats that accelerators execute natively are fixed at fabrication, yet large language model (LLM) checkpoints are released with MXFP4 weights in the Microscaling (MX) formats standardized in 2023.

## 为什么值得关注

待编辑增强。

## 摘要原文

The number formats that accelerators execute natively are fixed at fabrication, yet large language model (LLM) checkpoints are released with MXFP4 weights in the Microscaling (MX) formats standardized in 2023. FPGAs adopt new formats through bitstreams. However, to the best of our knowledge, no deployed FPGA LLM accelerator executes MXFP4 weights alongside BF16 products. We characterize the decoding of MXFP4 checkpoints, whose layers alternate between MXFP4$\times$BF16 products and BF16$\times$BF16 products of attention and BF16 layers. With a BF16 KV cache, BF16$\times$BF16 products take 56%-77% of the datapath time, during which a separate MXFP4 unit idles. We present Cruella, whose unified dot-product unit (UDPU) executes both product types on one DSP array and reduction pipeline. First, per-group pre-alignment keeps this pipeline at the BF16 width and changes perplexity by at most 0.7%. Second, pre-adder packing places two signed MXFP4$\times$BF16 products in one DSP48E2 multiplier with an exact correction. On an Alveo U55C, the UDPU needs 23% fewer DSP slices and 36% fewer LUTs than separate MXFP4 and BF16 units of equal throughput. On this board, MXFP4 weights speed up decoding by 1.15$\times$-1.87$\times$ over BF16 weights, and an NVIDIA A40 GPU decodes faster but spends 0.92$\times$-2.01$\times$ the board's energy per token.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: microscaling
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jinho Yang, Taehyeong Kim, Mincheol Cha, Hyeoncheol Kim, Donggeun Kim, Nahye Kim, Yujin Lee, Ryeowook Ko, Woong Gyu Park, Jiwoong Park, Junsoo Kim, Tae-Hyoung Kim, Yongjun Park, Seongmin Hong, Joo-Young Kim
- 发布：2026-11-23；更新：2026-11-23
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
