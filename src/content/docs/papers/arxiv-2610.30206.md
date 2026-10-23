---
title: "MoEZip: Routing-Aware KV Cache Compression for Sparse Mixture-of-Experts LLMs"
description: "Mixture-of-Experts (MoE) language models scale model capacity efficiently by activating a small subset of parameters per token."
---

**评分：48/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2610.30206) · [PDF](https://arxiv.org/pdf/2610.30206)

## 一句话摘要

Mixture-of-Experts (MoE) language models scale model capacity efficiently by activating a small subset of parameters per token.

## 为什么值得关注

待编辑增强。

## 摘要原文

Mixture-of-Experts (MoE) language models scale model capacity efficiently by activating a small subset of parameters per token. However, in long-context inference, memory remains a major bottleneck because the KV cache grows linearly with sequence length. Existing KV cache compression methods reduce this cost for dense transformers, but overlook a problem specific to MoE: KV eviction can change which experts are selected during answer generation, degrading the generation quality. We propose MoEZip, a routing-aware KV cache compression for sparse MoE language models. To estimate the sensitivity of expert routing to perturbation, we propose a novel metric based on the Fisher information matrix of routing distributions. MoEZip combines this metric with attention weights for routing-aware scoring of contexts. Finally, we compose a complementary scoring system that combines eviction methods for dense and sparse-MoE architectures. Experiments show that MoEZip achieves robust performance under aggressive cache compression on various benchmarks. At a KV retention ratio of 10\%, MoEZip improves over the SoTA baseline by +24 and +20 points on average on LongBench and RULER, corresponding to 2.3$\times$ and 4.9$\times$ higher scores, respectively.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 11 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Minsang Kim, Seungjun Baek
- 发布：2026-10-23；更新：2026-10-23
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
