---
title: "SinAE: A Single-Architecture Flow-Matching Autoencoder for Cross-Domain Atomic Systems"
description: "Small molecules, crystals, and proteins all reduce to atoms in 3D space, yet their generative pipelines remain fragmented across domains, each with its Small molecules, crystals, and proteins all reduce to atoms in 3D space, yet their generative pipelines remain fragmented across domains, each with its own graph, equivariant, or frame-based architecture."
---

**评分：42/100** · LLM 高效推理 > Serving 与分布式推理 > 并行与通信

[论文原文](https://arxiv.org/abs/2607.12380) · [PDF](https://arxiv.org/pdf/2607.12380)

## 一句话摘要

Small molecules, crystals, and proteins all reduce to atoms in 3D space, yet their generative pipelines remain fragmented across domains, each with its Small molecules, crystals, and proteins all reduce to atoms in 3D space, yet their generative pipelines remain fragmented across domains, each with its own graph, equivariant, or frame-based architecture.

## 为什么值得关注

待编辑增强。

## 摘要原文

Small molecules, crystals, and proteins all reduce to atoms in 3D space, yet their generative pipelines remain fragmented across domains, each with its Small molecules, crystals, and proteins all reduce to atoms in 3D space, yet their generative pipelines remain fragmented across domains, each with its own graph, equivariant, or frame-based architecture. Cross-domain training would mitigate per-domain data scarcity, but direct generation in 3D coordinate space cannot easily handle the heterogeneous structural priors of all three domains, and no prior latent autoencoder is simultaneously lossless and architecturally general across all three. We introduce SinAE, a single-architecture flow-matching autoencoder for molecules, crystals, and proteins, with vanilla Transformer encoder and decoder and no equivariant, graph, or domain-specific operators. Rather than requiring the encoder to capture fine-grained geometry, SinAE shifts the reconstruction burden into an iterative flow-matching decoder, achieving near-lossless reconstruction across domains and reducing reconstruction errors by orders of magnitude relative to prior latent baselines. The same per-token latent supports a standard Diffusion Transformer prior that reaches strong performance on molecular, crystal, and protein generation benchmarks. Joint molecule--crystal training strictly improves both domains, providing direct evidence of cross-domain transfer through a shared atomic latent. Code is available at https://github.com/BlueWhaleLab/SinAE .

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: all reduce
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Yuxuan Ren, Fan Yang, Jianhua Yao, Yatao Bian
- 发布：2026-11-10；更新：2026-11-10
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/BlueWhaleLab/SinAE](https://github.com/BlueWhaleLab/SinAE)
- 阅读深度：metadata
