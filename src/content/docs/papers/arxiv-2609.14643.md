---
title: "BigMoMo: Efficient Inference of Large-Scale MoE with Speculative Decoding on Mobile Devices"
description: "Mixture-of-Experts (MoE) models expand language model capacity on smartphones, but expert offloading remains constrained by limited DRAM capacity and costly data movement."
---

**评分：46/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2609.14643) · [PDF](https://arxiv.org/pdf/2609.14643)

## 一句话摘要

Mixture-of-Experts (MoE) models expand language model capacity on smartphones, but expert offloading remains constrained by limited DRAM capacity and costly data movement.

## 为什么值得关注

待编辑增强。

## 摘要原文

Mixture-of-Experts (MoE) models expand language model capacity on smartphones, but expert offloading remains constrained by limited DRAM capacity and costly data movement. Sequential token routing couples expert execution to fragmented flash reads and multistage NPU preparation, leaving sparse computation stalled on weight transfers. Each transfer serves few tokens before execution moves on. We exploit the multi-token verification window of speculative decoding to decouple expert movement from single-token execution, enabling weight reuse, contiguous flash reads, and load-compute overlap. We present \textsc{BigMoMo}, a mobile MoE runtime that exploits this window across the memory hierarchy. It prunes speculative branches and expert activations using acceptance rates, routing impact, and movement cost; reorganizes on-flash experts according to runtime co-loading patterns; and batches ready experts to overlap NPU computation with pending transfers. Across four MoE models and five benchmarks on two mobile platforms, \textsc{BigMoMo} achieves mean decoding speedups of $4.83\times$ over on-demand autoregressive offloading and $1.82\times$ over the best speculative MoE baseline, supporting MoE models up to 30B parameter.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: speculative decoding
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Maoliang Li, Hailong Zou, Taohong Han, Haoze Chi, Jiayu Chen, Zihao Zheng, Jie Zhang, Guojie Luo, Xiang Chen
- 发布：2026-09-15；更新：2026-09-15
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
