---
title: "Retrofitting Linear Attention into Diffusion Language Models"
description: "Diffusion language models (dLLMs) offer a promising alternative to autoregressive models by accelerating inference through parallel decoding."
---

**评分：46/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2608.06628) · [PDF](https://arxiv.org/pdf/2608.06628)

## 一句话摘要

Diffusion language models (dLLMs) offer a promising alternative to autoregressive models by accelerating inference through parallel decoding.

## 为什么值得关注

待编辑增强。

## 摘要原文

Diffusion language models (dLLMs) offer a promising alternative to autoregressive models by accelerating inference through parallel decoding. Recent dLLMs commonly use blockwise semi-autoregressive decoding, generating blocks autoregressively while denoising tokens within each active block in parallel. However, despite KV caching, each denoising step still attends to all previous blocks, repeatedly incurring prefix-attention cost. Motivated by this bottleneck, we ask whether dLLM inference can be further accelerated by linearizing attention over previous blocks. We introduce block-hybrid attention, which retains exact softmax attention within the active denoising block while applying linear attention over previous blocks. We show that this hybrid attention can be retrofitted into a pretrained dLLM with minimal post-training: LLaDA-Hybrid replaces 6 of the 20 attention layers in LLaDA~2.1, a 16B open-source dLLM, largely following LoLCAT (Zhang et al, 2024). The conversion takes only approximately 60 hours while preserving benchmark performance: 72.0% vs. 75.6% on HumanEval, 63.0% vs. 57.7% on MBPP+, and 86.7% vs. 88.3% on CMATH. With a Triton implementation, LLaDA-Hybrid achieves up to $1.7\times$ higher decoding throughput and supports more concurrent requests before exhausting memory, showing that pretrained dLLMs can be efficiently linearized for faster inference. Our code is available at: https://github.com/Diuven/LLaDA-Hybrid.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 11 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: parallel decoding
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Jinha Kim, Younghun Roh, Jaeyeon Kim
- 发布：2026-08-10；更新：2026-08-10
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/Diuven/LLaDA-Hybrid](https://github.com/Diuven/LLaDA-Hybrid)
- 阅读深度：metadata
