---
title: "UE5M3 FP4 Block Scaling for Stable Language Model Pretraining"
description: "Stable 4-bit floating-point (FP4) pretraining is difficult because the E2M1 payload represents only a narrow range of magnitudes."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2609.02846) · [PDF](https://arxiv.org/pdf/2609.02846)

## 一句话摘要

Stable 4-bit floating-point (FP4) pretraining is difficult because the E2M1 payload represents only a narrow range of magnitudes.

## 为什么值得关注

待编辑增强。

## 摘要原文

Stable 4-bit floating-point (FP4) pretraining is difficult because the E2M1 payload represents only a narrow range of magnitudes. NVIDIA's Transformer Engine \nv{} recipe addresses this with current-tensor scaling, a randomized Hadamard transform (RHT), and bfloat16 (BF16) final layers, adding work outside the FP4 matrix multiplications. We instead pair E2M1 payloads with unsigned E5M3 (\ue{}) block scales. Their wider range permits periodic tensor scaling, while our recipe applies selective stochastic rounding to backward gradients, omits RHT, and uses FP4 in all eligible internal linears. We pretrain a Nemotron-H 8B model for nearly 190 billion tokens. Compared with Transformer Engine \nv{}, the proposed block-16 recipe finishes with lower final-window training loss and, under their respective quantized-inference policies, lower validation loss measured as held-out negative log-likelihood. Its quantized-inference downstream point estimates are also higher on all three reported aggregates. A native \nv{} execution ablation that jointly removes RHT and the BF16 final-block exemption increases measured model-body token throughput by 21.2\%. These results demonstrate end-to-end software-emulated \uefp{} pretraining with a simpler recipe and motivate native support for \ue{} block scaling.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: fp4, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Robert Hu, Carlo Luschi, Paul Balanca
- 发布：2026-09-03；更新：2026-09-03
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
