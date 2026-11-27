---
title: "MXFP4 for LLM Inference: Complementary Post-Training Quantization Techniques and Their Interactions"
description: "Recent advances in low-precision representation have introduced several microscaling numerical formats for LLM quantization."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2611.32873) · [PDF](https://arxiv.org/pdf/2611.32873)

## 一句话摘要

Recent advances in low-precision representation have introduced several microscaling numerical formats for LLM quantization.

## 为什么值得关注

待编辑增强。

## 摘要原文

Recent advances in low-precision representation have introduced several microscaling numerical formats for LLM quantization. By sharing a scale factor across groups of 16 or 32 elements, these formats enable aggressive low-precision quantization with minimal accuracy degradation, particularly when combined with modern PTQ algorithms. Their accuracy depends on how the numerical format interacts with rotation, PTQ, and scale selection. We study the composability of PTQ configurations across six LLMs and three microscaling formats: MXFP6, MXFP4, and NVFP4, systematically varying Hadamard rotation granularity, PTQ algorithm, and scale-selection strategy. Our central finding is that effective quantization recipes are format dependent: both MXFP4 and NVFP4 support accurate 4-bit inference, but techniques that benefit one do not necessarily transfer to the other. MXFP4 benefits substantially from rotation and error-correcting PTQ, whereas NVFP4 gains less from rotation, consistent with its finer-grained scales capturing more within-block variation. Building on these findings, we introduce Midmax, a calibration-free scale-selection strategy that mitigates clipping error in power-of-two block scales and improves accuracy across a majority of the evaluated MXFP4 configurations. We show that pairing MXFP6 activations with MXFP4 weights recovers most of the accuracy lost at 4-bit and, on Llama-3.1-8B, matches or exceeds our in-house BF16 baseline. An additional study finds that augmenting MXFP4 with a per-tensor macroscale, a mechanism intrinsic to NVFP4, does not improve average accuracy, suggesting that global rescaling alone does not address the limitations of E8M0 block scales for MXFP4 quantization. Together, these results provide practical guidance for combining numerical formats, rotation, PTQ, and scale selection for accurate low-precision LLM inference.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: microscaling, quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Natalia Frumkin, Alireza Khodamoradi, Kristof Denolf, Eric Dellinger, Stuart Biles
- 发布：2026-11-24；更新：2026-11-25
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
