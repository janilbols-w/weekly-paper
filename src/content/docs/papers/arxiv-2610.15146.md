---
title: "Compute-Optimal Scaling Laws for Spiking Language Models"
description: "Spiking neural networks target energy-efficient language modeling through sparse, binary activations, but the efficiency-accuracy tradeoff of spiking language models is uncharacterized at scale."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.15146) · [PDF](https://arxiv.org/pdf/2610.15146)

## 一句话摘要

Spiking neural networks target energy-efficient language modeling through sparse, binary activations, but the efficiency-accuracy tradeoff of spiking language models is uncharacterized at scale.

## 为什么值得关注

待编辑增强。

## 摘要原文

Spiking neural networks target energy-efficient language modeling through sparse, binary activations, but the efficiency-accuracy tradeoff of spiking language models is uncharacterized at scale. We present the first Chinchilla-style IsoFLOP scaling study of a spiking language model, sweeping SpikeGPT-family models (RWKV backbone) from width 384 to 1536 across compute budgets from $3\times10^{17}$ to $10^{19}$ FLOPs on FineWeb-EDU. We report two findings. First, the compute-optimal frontier is $N_{opt} \propto C^{0.56}$, close to the 0.50 that Hoffmann et al. report for dense Transformers, so spiking does not change how parameters and data should be traded off under a compute budget. Second, against non-spiking RWKV and Transformer baselines trained the same way, the loss gap splits into a backbone cost of about 0.16 nats that does not change with compute and a spiking cost that falls steadily with compute, from 0.34 to 0.23 nats over our range. These results give the first compute-optimal recipe for spiking language models and quantify the accuracy cost of their sparsity.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: sparsity
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Dan Saunders, Benjamin Ren, Catherine He
- 发布：2026-11-11；更新：2026-11-11
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
