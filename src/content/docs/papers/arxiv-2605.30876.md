---
title: "dMoE: dLLMs with Learnable Block Experts"
description: "Diffusion Large Language Models (dLLMs) have recently emerged as a promising alternative to autoregressive models, offering competitive performance while naturally supporting parallel decoding."
---

**评分：48/100** · LLM 高效推理 > 模型与算法效率 > MoE 路由与专家优化

[论文原文](https://arxiv.org/abs/2605.30876) · [PDF](https://arxiv.org/pdf/2605.30876)

## 一句话摘要

Diffusion Large Language Models (dLLMs) have recently emerged as a promising alternative to autoregressive models, offering competitive performance while naturally supporting parallel decoding.

## 为什么值得关注

待编辑增强。

## 摘要原文

Diffusion Large Language Models (dLLMs) have recently emerged as a promising alternative to autoregressive models, offering competitive performance while naturally supporting parallel decoding. However, as dLLMs are increasingly integrated with Mixture-of-Experts (MoE) architectures to scale model capacity, a fundamental mismatch arises between block parallel decoding and token-level expert selection. Specifically, each dLLM forward pass processes multiple tokens with bidirectional dependencies, whereas conventional MoE layers route each token independently. This mismatch substantially increases the number of uniquely activated experts, making inference increasingly memory-bound. To address this, we propose dMoE, a simple yet effective block-level MoE framework. The central idea of dMoE is to aggregate token-level expert distributions within each block into a unified block-level expert distribution, which is then used to guide block expert routing in a coherent manner. In this way, dMoE substantially reduces the number of uniquely activated experts during inference without sacrificing performance, thereby mitigating the memory-bound bottleneck. Extensive experiments across a variety of benchmarks demonstrate the effectiveness of dMoE. On average, dMoE reduces the number of uniquely activated experts from 69.5 to 16.6 while retaining 99.55% of the original performance. Meanwhile, it reduces memory usage by 74.36% to 76.78% and achieves $1.36\times$ to $2.04\times$ end-to-end latency speedup. Code is available at: https://github.com/fscdc/dMoE.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 11 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: expert routing
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Sicheng Feng, Zigeng Chen, Gongfan Fang, Xinyin Ma, Xinchao Wang
- 发布：2026-11-10；更新：2026-11-10
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/fscdc/dMoE](https://github.com/fscdc/dMoE)
- 阅读深度：metadata
