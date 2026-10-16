---
title: "Energy Consumption Analysis of Discrete Diffusion and Autoregressive Language Models"
description: "As Large Language Models (LLMs) continue to scale, their energy consumption during inference has become a critical concern."
---

**评分：39/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](http://arxiv.org/abs/2610.19855v1) · [PDF](https://arxiv.org/pdf/2610.19855v1)

## 一句话摘要

As Large Language Models (LLMs) continue to scale, their energy consumption during inference has become a critical concern.

## 为什么值得关注

待编辑增强。

## 摘要原文

As Large Language Models (LLMs) continue to scale, their energy consumption during inference has become a critical concern. While Autoregressive (AR) models are the industry standard, Diffusion Language Models (DLLMs) have emerged as a promising alternative capable of parallel token generation. In this paper, we perform a comparative energy benchmark of diffusion models (LLaDA-8B, Dream-7B) against AR counterparts (Llama-3.1-8B, Qwen-2.5-7B). We analyze the trade-offs between model architecture, KV-cache optimization, and Joules-per-token efficiency. Our results show that at longer sequences (200--600 tokens), diffusion models achieve 2.5--2.7 J/token, approximately 2$\times$ more efficient than AR models with KV-cache (5.3--5.7 J/token). KV-cache provides substantial benefits for AR models at longer sequences (50--70\% energy reduction).

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 6 |

## 证据与限制

- taxonomy keywords: kv-cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Boris Ruf, Marcin Detyniecki
- 发布：2026-10-14；更新：2026-10-14
- 来源：arXiv；Venue：GreenSys '26: Proceedings of the 2nd International Workshop on Systems and Methods for Sustainable Large-Scale AI, 2026, pp. 7-12
- 代码：未发现
- 阅读深度：metadata
