---
title: "GaugeQuant: Online Learning of Quantization-Optimal Bases from LLM Symmetries"
description: "Transformers are known to have internal continuous symmetries that leave outputs invariant while altering how activations are distributed across coordinates, and hence how well they quantize."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2607.20757) · [PDF](https://arxiv.org/pdf/2607.20757)

## 一句话摘要

Transformers are known to have internal continuous symmetries that leave outputs invariant while altering how activations are distributed across coordinates, and hence how well they quantize.

## 为什么值得关注

待编辑增强。

## 摘要原文

Transformers are known to have internal continuous symmetries that leave outputs invariant while altering how activations are distributed across coordinates, and hence how well they quantize. GaugeQuant leverages this in-training by introducing a LogSumExp term to the loss that breaks the symmetries, thus selecting a basis that minimizes activation outliers. A stop-gradient operator ensures that only rotation matrices are updated, yielding the language modeling objective completely unaltered. Our quantization strategy requires no specific calibration data, no quantization simulation, and adds a small inference overhead. As a proof of concept, we evaluate on WikiText-2 perplexity and zero-shot reasoning. On Qwen-2.5 0.5B, GaugeQuant reduces perplexity (e.g. $25.62 \to 16.76$ under W4A16) and improves zero-shot accuracy. On LLaMA-2 7B, perplexity improves but downstream accuracy does not. The code is available at: https://github.com/MPedraBento/gauge-quant.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Miguel P. Bento, Jo\~ao F. Seabra
- 发布：2026-11-05；更新：2026-11-05
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/MPedraBento/gauge-quant](https://github.com/MPedraBento/gauge-quant)
- 阅读深度：metadata
