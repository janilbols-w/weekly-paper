---
title: "Temporal Self-Distillation: Faster Inference in Discrete Diffusion Language Models"
description: "Diffusion language models (dLLMs) promise fast inference by generating multiple tokens in parallel, but suffer severe performance degradation when parallel decoding is pushed too aggressively."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.15177) · [PDF](https://arxiv.org/pdf/2609.15177)

## 一句话摘要

Diffusion language models (dLLMs) promise fast inference by generating multiple tokens in parallel, but suffer severe performance degradation when parallel decoding is pushed too aggressively.

## 为什么值得关注

待编辑增强。

## 摘要原文

Diffusion language models (dLLMs) promise fast inference by generating multiple tokens in parallel, but suffer severe performance degradation when parallel decoding is pushed too aggressively. We introduce Temporal Self-Distillation (TSD), a simple on-policy method that trains dLLMs for fast inference by distilling predictions across time. Specifically, TSD distills the model's denoising distribution at earlier timesteps toward its distribution at the final timestep at which a token is committed. This encourages earlier predictions to better anticipate the model's eventual output, enabling much more aggressive parallel decoding. Because its teacher signal comes from the model itself, TSD requires no offline teacher generation and applies seamlessly to both base and post-trained policies. Across seven benchmarks in mathematics, planning, and code, TSD substantially shifts the speed--quality frontier toward the low-compute regime. TSD thus provides a simple, single-stage approach to accelerating dLLMs, achieving speedups competitive with offline distillation while avoiding a complex two-stage pipeline.

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

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Shijian Xu, Andrea Miele, Metod Jazbec, Volker Roth, Eric Nalisnick, Ilija Bogunovic
- 发布：2026-09-15；更新：2026-09-15
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
