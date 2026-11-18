---
title: "Quantize, Qualify, Rerank: A Recipe for Compressing LLMs Without Losing Quality"
description: "Compressing large language models lowers serving cost, but a single automatic metric may miss quality loss."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2611.18587) · [PDF](https://arxiv.org/pdf/2611.18587)

## 一句话摘要

Compressing large language models lowers serving cost, but a single automatic metric may miss quality loss.

## 为什么值得关注

待编辑增强。

## 摘要原文

Compressing large language models lowers serving cost, but a single automatic metric may miss quality loss. For the WMT26 Model Compression constrained track, we compress google/gemma-3-12b-it (24.4 GB in bf16) for three translation directions on one H100. Paired bootstrap analysis exposes metric disagreement on 4-bit quantization; guided by WMT24 human meta-evaluation, we use MetricX24-XXL as primary and CometKiwi-XXL as a cross-check. Removing the unused vision stack and non-task vocabulary and using int8 weights or fp8 activations causes no resolved loss, whereas int4 leaves a small residual. QLoRA healing overfits its calibration domain. A Cometoid best-of-4 reranker at $T=0.3$ improves both the 8-bit and 4-bit systems under WMT25 test set. On post-submission WMT26, both remain competitive with bf16 under reference-free metrics; the small difference between the reranked variants is treated as noise.

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

- taxonomy keywords: fp8, int4, int8, quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Thamme Gowda
- 发布：2026-11-17；更新：2026-11-17
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
