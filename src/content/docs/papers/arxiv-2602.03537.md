---
title: "MatGPTQ: Efficient and Accurate Inference over Nested Quantized Models"
description: "Matryoshka Quantization (MatQuant), Any-Precision-LLM (AP) and AnyBCQ (AB) are recent quantization approaches showing that a single integer-quantized model can be served across multiple precisions."
---

**评分：52/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2602.03537) · [PDF](https://arxiv.org/pdf/2602.03537)

## 一句话摘要

Matryoshka Quantization (MatQuant), Any-Precision-LLM (AP) and AnyBCQ (AB) are recent quantization approaches showing that a single integer-quantized model can be served across multiple precisions.

## 为什么值得关注

待编辑增强。

## 摘要原文

Matryoshka Quantization (MatQuant), Any-Precision-LLM (AP) and AnyBCQ (AB) are recent quantization approaches showing that a single integer-quantized model can be served across multiple precisions. In this paradigm, lower-precision models are extracted from a higher-precision model by simply reading fewer bits of the weights. This enables a single checkpoint to cover a wide range of memory and latency budgets, but makes both quantization and efficient execution substantially harder. Existing methods rely on expensive quantization-aware training (QAT) or gradient-based post-training quantization (PTQ) rather than fast one-shot PTQ, and offer limited system support: dedicated kernels are either missing or restricted to single- or small-batch decoding. We address these limitations with Post-Training Matryoshka Quantization (MatGPTQ), an end-to-end pipeline for nested-model quantization and inference. MatGPTQ casts Matryoshka quantization as multi-precision error compensation, producing a single "sliceable" parent model jointly optimized for multiple target precisions in one pass over a small calibration set. We further refine the MatQuant representation so that an $r$-bit model reads exactly $r$ bits, and introduce the first dedicated inference kernels for this format, supporting batch sizes beyond one and integrated into vLLM. Across standard LLMs and benchmarks, MatGPTQ outperforms MatQuant while remaining competitive with AP and AB at the smallest checkpoint size, and our kernels achieve end-to-end speedups of up to 3.5$\times$ over BF16 at the low-bit regime. Overall, MatGPTQ makes nested quantized models practical to serve from a single, compact checkpoint. Code is available at https://github.com/IST-DASLab/MatGPTQ.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 11 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Maximilian Kleinegger, Elvir Crn\v{c}evi\'c, Dan Alistarh
- 发布：2026-10-01；更新：2026-10-01
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/IST-DASLab/MatGPTQ](https://github.com/IST-DASLab/MatGPTQ)
- 阅读深度：metadata
