---
title: "Zarya: A Hybrid Autoregressive--Masked Diffusion Language Model with Flexible Training and Dual-Mode Inference"
description: "Autoregressive language models (ARMs) are constrained by sequential, left-to-right generation, while masked diffusion models (MDMs) enable parallel decoding but suffer from high computational overhead due to the inability to reuse Key-Value (KV) cache and from incoherent generation arising from learning dependencies over an intractable space of token combina"
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2609.19868) · [PDF](https://arxiv.org/pdf/2609.19868)

## 一句话摘要

Autoregressive language models (ARMs) are constrained by sequential, left-to-right generation, while masked diffusion models (MDMs) enable parallel decoding but suffer from high computational overhead due to the inability to reuse Key-Value (KV) cache and from incoherent generation arising from learning dependencies over an intractable space of token combina

## 为什么值得关注

待编辑增强。

## 摘要原文

Autoregressive language models (ARMs) are constrained by sequential, left-to-right generation, while masked diffusion models (MDMs) enable parallel decoding but suffer from high computational overhead due to the inability to reuse Key-Value (KV) cache and from incoherent generation arising from learning dependencies over an intractable space of token combinations. We introduce Zarya, a family of hybrid language models that jointly optimizes an autoregressive (AR) objective and a masked-diffusion objective within a single architecture. Zarya structures training data into variable-size slots and employs a curriculum that gradually increases slot granularity, enabling a smooth transition from fine-grained AR learning to coarse-grained diffusion learning. At inference, Zarya provides two distinct decoding paradigms through a unified interface: (i) MDM sampling with first-hitting denoising, and (ii) slotted speculative decoding that interleaves inter-slot diffusion-based selection with intra-slot autoregressive infilling, achieving full KV cache reuse. The training and inference regimes are fully decoupled, allowing a model trained with any configuration to be deployed in either mode. Extensive configurability --- including grouped noise patterns (Prefix Completion, Fill-In-the-Prefix, Fill-In-the-Middle), ordered sampling schedules, and noise-level permutation strategies --- enables flexible research exploration. We release Zarya models publicly in sizes 0.6B, 1.7B, and 4B, demonstrating performance on standard benchmarks while offering a principled integration of autoregressive and diffusion paradigms.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: parallel decoding, speculative decoding
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Leonid Sinev, Ilya Koziev, Vladislav Leshchuk
- 发布：2026-09-17；更新：2026-09-18
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
