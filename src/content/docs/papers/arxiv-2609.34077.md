---
title: "MaskCoFT: Masked Co-Adaptive Fine-Tuning for Memory-Efficient MoE Inference"
description: "Mixture-of-experts (MoE) language models often exceed the memory of a single GPU."
---

**评分：45/100** · LLM 高效推理 > 模型与算法效率 > MoE 路由与专家优化

[论文原文](https://arxiv.org/abs/2609.34077) · [PDF](https://arxiv.org/pdf/2609.34077)

## 一句话摘要

Mixture-of-experts (MoE) language models often exceed the memory of a single GPU.

## 为什么值得关注

待编辑增强。

## 摘要原文

Mixture-of-experts (MoE) language models often exceed the memory of a single GPU. Expert offloading keeps most experts in host memory and loads them on demand, so decoding speed depends on how many experts each token must fetch. Caching and prefetching reduce this cost only as far as the routing allows. Router-only fine-tuning can reshape the routing to reuse experts, but it keeps the experts frozen, so they cannot adapt to the tokens the new routing sends them. We propose MaskCoFT, a masked co-adaptive fine-tuning method that trains routers and experts together with the cross-entropy loss alone. During fine-tuning, a learnable binary mask restricts the Top-K routing of each layer to a subset of experts, and the experts adapt to the tokens redirected to them. At inference, the learned mask becomes a soft prior that re-ranks experts, so every expert remains selectable. We simulate a GPU cache of 4 experts per layer for Mixtral-8x7B and 12 for DeepSeek-V2-Lite. MaskCoFT cuts expert fetches per token by 23.7% and 10.1% relative to the base model. In real offloading system serving, it lowers the time per output token by up to 16.4% and 5.5%, respectively. Its average accuracy over nine benchmarks stays above the base model by 0.92 and 0.53 points.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: expert offloading, moe inference
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Junfeng Wu, Zehao Fan, Hadjer Benmeziane, Kaoutar El Maghraoui, Liu Liu, Yinan Wang
- 发布：2026-09-28；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
