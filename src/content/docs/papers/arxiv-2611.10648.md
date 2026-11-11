---
title: "PENSA: A Spatial Accelerator for BitNet b1.58 Inference on an HBM-equipped AMD Alveo FPGA"
description: "Ternary large language models (tLLMs) replace general multiplication in dominant linear layers with sign-controlled accumulation, shifting hardware bottlenecks toward packed-weight delivery, reduction, and operator occupancy."
---

**评分：42/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2611.10648) · [PDF](https://arxiv.org/pdf/2611.10648)

## 一句话摘要

Ternary large language models (tLLMs) replace general multiplication in dominant linear layers with sign-controlled accumulation, shifting hardware bottlenecks toward packed-weight delivery, reduction, and operator occupancy.

## 为什么值得关注

待编辑增强。

## 摘要原文

Ternary large language models (tLLMs) replace general multiplication in dominant linear layers with sign-controlled accumulation, shifting hardware bottlenecks toward packed-weight delivery, reduction, and operator occupancy. PENSA is an end-to-end FPGA accelerator for the BitNet b1.58 2B4T model on an AMD Alveo U50. Two row-partitioned ternary matrix engines consume packed TQ1_0 weights from eight independent high-bandwidth memory (HBM) pseudo-channels, each processing 1,280 ternary weights per cycle through sign selection and integer reduction. The sequencer, attention, and vocabulary-projection units remain resident on the FPGA, while two-stream interleaved scheduling overlaps sequences across the persistent pipeline to form the Penta-Unit. At 104.1~MHz, PENSA achieves 58.09 tok/s at context 128 and 24.60 tok/s at context 2048, corresponding to 2.14-3.14$\times$ the throughput of a same-model Xeon E-2356G baseline. The resulting system demonstrates end-to-end FPGA execution of 2B-scale BitNet topology without modifying its model structure.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: accelerator
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Karthikeyan B. Kalyanasundara, Ivan S. Maksymo, Philip H. W. Leong
- 发布：2026-11-10；更新：2026-11-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
