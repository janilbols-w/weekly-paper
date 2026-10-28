---
title: "Quantized Edge Inference of a Self-Supervised SAR-Optical Encoder on Commodity x86 Hardware"
description: "Self-supervised vision transformers are increasingly used as reusable encoders for Earth observation, but their inference cost on the hardware available in the field is rarely characterized."
---

**评分：49/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2610.37056) · [PDF](https://arxiv.org/pdf/2610.37056)

## 一句话摘要

Self-supervised vision transformers are increasingly used as reusable encoders for Earth observation, but their inference cost on the hardware available in the field is rarely characterized.

## 为什么值得关注

待编辑增强。

## 摘要原文

Self-supervised vision transformers are increasingly used as reusable encoders for Earth observation, but their inference cost on the hardware available in the field is rarely characterized. We deploy a pretrained SAR-optical masked-autoencoder encoder on three commodity x86 nodes, from a low-power CPU without AVX2 to an AVX2+VNNI reference, at FP32, FP16 and INT8 on the CPU and, where present, the integrated GPU, and report latency, energy (RAPL and wall plug) and linear-probe accuracy. Quantization is accuracy-neutral: INT8 changes micro-mAP by only +0.0006, within the seed spread, so precision becomes a pure cost decision. INT8 lowers CPU latency on every node, by 1.45x even on the CPU without AVX2, and CPU energy wherever it is measured, and the VNNI reference (1.53x) suggests a further gain beyond AVX2. The Pareto-optimal device shifts from the integrated GPU, which is 4.38x faster than the CPU on the weakest node, to the CPU as the CPU class improves.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 20 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: int8, quantization, quantized
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Christian Sanchez-Leon, Dongming Chen
- 发布：2026-10-28；更新：2026-10-28
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
