---
title: "ResCom: Activation Residual Compensation for Large Language Model Quantization"
description: "Low-bit weight--activation quantization reduces the memory and computation needed to deploy large language models, but activation rounding can still degrade accuracy after calibration."
---

**评分：46/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2610.35955) · [PDF](https://arxiv.org/pdf/2610.35955)

## 一句话摘要

Low-bit weight--activation quantization reduces the memory and computation needed to deploy large language models, but activation rounding can still degrade accuracy after calibration.

## 为什么值得关注

待编辑增强。

## 摘要原文

Low-bit weight--activation quantization reduces the memory and computation needed to deploy large language models, but activation rounding can still degrade accuracy after calibration. Reconstruction from rounded inputs cannot distinguish activations within the same quantization bin. We propose ResCom, a low-rank correction that uses the activation rounding residual to compensate for the resulting layer-output error. An output-aware calibration procedure selects residual directions by their contribution to output reconstruction and computes the correction in closed form, without gradient training or updates to the calibrated weights. On Llama-3-8B with 4-bit weights and activations, rank-32 attention corrections reduce WikiText-2 perplexity from 7.708 to 7.147, improve MMLU by 2.89 percentage points, and raise five-shot GSM8K accuracy from 23.96 to 36.16 percent. Evaluations on models from 1B to 70B parameters and on held-out C4 test the method beyond this setting. The evaluated FP32 implementation adds 2.25 percent to 4K prefill time; a separate compact-storage implementation retains a 27.7 percent peak-memory reduction relative to FP16.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Ning Yang, Bohan Cui, Zhuowen Liu, Yuting Wang
- 发布：2026-10-28；更新：2026-10-28
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
