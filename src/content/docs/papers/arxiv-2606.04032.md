---
title: "Do Transformers Need Three Projections? Systematic Study of QKV Variants"
description: "Transformers have become the standard solution for various AI tasks, with the query, key, and value (QKV) attention formulation playing a central role."
---

**评分：43/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2606.04032) · [PDF](https://arxiv.org/pdf/2606.04032)

## 一句话摘要

Transformers have become the standard solution for various AI tasks, with the query, key, and value (QKV) attention formulation playing a central role.

## 为什么值得关注

待编辑增强。

## 摘要原文

Transformers have become the standard solution for various AI tasks, with the query, key, and value (QKV) attention formulation playing a central role. However, the individual contribution of these three projections and the impact of omitting some remain poorly understood. We systematically evaluate three projection sharing constraints: a) Q-K=V (shared key-value), b) Q=K-V (shared query-key), and c) Q=K=V (single projection). The last two variants produce symmetric attention maps; to address this, we also explore asymmetric attention via 2D positional encodings. Through experiments spanning synthetic tasks, vision (MNIST, CIFAR, TinyImageNet, anomaly), and language modeling (300M and 1.2B parameter models on 10B tokens), we discovered that our transformers perform on par or occasionally better than the QKV transformer. In language modeling, Q-K=V projection sharing achieves 50% KV cache reduction with only 3.1% perplexity degradation. Crucially, projection sharing is complementary to head sharing (GQA/MQA): combining Q-K=V with GQA-4 yields 87.5% cache reduction, while Q-K=V + MQA achieves 96.9%, enabling practical on-device inference. We show that Q-K=V preserves quality because keys and values can occupy similar representational spaces and attention operates in a low-rank regime, whereas Q=K-V breaks attention directionality. Our results systematically characterize projection sharing as an underexplored instance of weight tying in attention, with direct, quantifiable inference memory benefits, particularly valuable for edge deployment. The code is publicly available at https://github.com/Brainchip-Inc/Do-Transformers-Need-3-Projections

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Ali Kayyam, Anusha Madan Gopal, M Anthony Lewis
- 发布：2026-08-14；更新：2026-08-14
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/Brainchip-Inc/Do-Transformers-Need-3-Projections](https://github.com/Brainchip-Inc/Do-Transformers-Need-3-Projections)
- 阅读深度：metadata
