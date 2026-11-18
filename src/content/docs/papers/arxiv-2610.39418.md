---
title: "LinQuant: Functional Invariances for Low-Precision Linear Recurrences"
description: "Linear recurrences are emerging as practical alternatives to softmax attention in large language models, appearing in both standalone and hybrid architectures."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2610.39418) · [PDF](https://arxiv.org/pdf/2610.39418)

## 一句话摘要

Linear recurrences are emerging as practical alternatives to softmax attention in large language models, appearing in both standalone and hybrid architectures.

## 为什么值得关注

待编辑增强。

## 摘要原文

Linear recurrences are emerging as practical alternatives to softmax attention in large language models, appearing in both standalone and hybrid architectures. However, despite their rapid emergence, low-precision inference remains much less developed for these models than for softmax attention. During prefill, chunkwise-parallel algorithms cast much of the recurrence as dense matrix multiplications, suggesting a natural path to low-precision execution. Simply quantizing these operations in their native form, however, can be fragile. In this work, we identify functional invariances that preserve the full-precision computation while making the operands more amenable to quantization. Building on this observation, we introduce LinQuant, a framework for low-precision recurrent prefill based on seven such invariances, including rotations, diagonal rescalings, and alternative placements of recurrent decay and write factors. We derive when these transformations remain valid across common recurrence families spanning linear, gated, and delta-rule updates, and show that they provide complementary degrees of freedom for improving low-precision accuracy. We implement these transformations in INT8 and INT4 kernels and evaluate them on the recurrences of Nemotron-H, Qwen3.5, and Kimi Linear, recovering most of the accuracy lost to quantization while accelerating recurrent prefill. We also augment SSDi8, an existing low-precision prefill pipeline for Mamba-2, improving perplexity at matched prefill latency on pretrained Mamba-2 and Nemotron-H models. Altogether, these results demonstrate the practical utility of invariance-based quantization for recurrent models.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: int4, int8, quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Neehal Tumma, Philipp Nazari, Rohan Cherukuri, Daniela Rus, T. Konstantin Rusch
- 发布：2026-11-17；更新：2026-11-17
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
