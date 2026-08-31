---
title: "A Method for Layer Bit-Width Allocation in LLM Quantization via Performance Maximization Under a Quality-Degradation Constraint"
description: "This paper proposes a layer bit allocation method for Gemma-3-1B, formulating the problem as performance maximization (latency decrease) given a degradation budget constraint (allowable level of generation quality loss)."
---

**评分：47/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2608.28003) · [PDF](https://arxiv.org/pdf/2608.28003)

## 一句话摘要

This paper proposes a layer bit allocation method for Gemma-3-1B, formulating the problem as performance maximization (latency decrease) given a degradation budget constraint (allowable level of generation quality loss).

## 为什么值得关注

待编辑增强。

## 摘要原文

This paper proposes a layer bit allocation method for Gemma-3-1B, formulating the problem as performance maximization (latency decrease) given a degradation budget constraint (allowable level of generation quality loss). This approach is different from time- and resource-consuming uniform layer quantization methods that are used in the literature (like GPTQ or AWQ) or allocation methods without proven performance-accelerating effect (like MixLLM or TorchAO). The layer sensitivity profile resulting from our prior work SA-PTQ is applied using the activation pass-through mode inside TensorRT-LLM. For each layer precision is determined individually in blocks, according to a grouping introduced in the prior step (5+5, 10+10, all26), differentiating the contribution of FFN, Attention, and lm_head to the overall speedup. The clock speed was measured for 13 W8A8 variants on an RTX 5090. We find that for FFN and lm_head the time cost of quantization/dequantization is compensated for by the use of integer arithmetic, while for short context lengths, the opposite holds true for Attention: an additional step of quantization slows execution down. We propose a manual implementation of SmoothQuant for TensorRT-LLM which was necessary due to export failures, unavailable for lm_head. The best solution found under joint consideration of all three criteria with minimal degradation was FFN 5+5 with lm_head, providing an 11.0% reduction in latency with negligible quality loss (98.90% Top-1 agreement, +0.85% perplexity degradation). With acceptable quality loss for FFN all26 + lm_head, a speedup up to 19.1% was found possible. We suggest further optimizations: fused attention kernels in INT8, KV-cache quantization, using FP8 instead of INT8 and partial Attention quantization analogous to FFN.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 20 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: fp8, int8, quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Artem Safronov
- 发布：2026-08-31；更新：2026-08-31
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
