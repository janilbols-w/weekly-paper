---
title: "ECHO: Early-layer Collaborative Hierarchical Orchestration with Bonus Logits in Speculative Decoding"
description: "While draft-model-free speculative decoding offers a promising path to efficient LLM inference, it is frequently constrained by stale draft candidates and the high computational cost of the verification."
---

**评分：52/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2609.17241) · [PDF](https://arxiv.org/pdf/2609.17241)

## 一句话摘要

While draft-model-free speculative decoding offers a promising path to efficient LLM inference, it is frequently constrained by stale draft candidates and the high computational cost of the verification.

## 为什么值得关注

待编辑增强。

## 摘要原文

While draft-model-free speculative decoding offers a promising path to efficient LLM inference, it is frequently constrained by stale draft candidates and the high computational cost of the verification. To address these challenges, we propose ECHO, a hierarchical dual-loop framework that exploits the functional asymmetry between LLM layers. Leveraging the high discriminative efficiency of early layers and the authoritative distribution of final layers, ECHO bifurcates inference into a high-frequency inner loop and a low-frequency outer loop. Within the inner loop, early-layer bonus logits drive rapid, multi-step draft-tree exploration at a minimal cost. Simultaneously, the outer loop performs authoritative full-model verification through a state-reuse mechanism. Crucially, the outer loop also utilizes final-layer bonus logits to correct existing paths and supplement the tree with high-confidence candidates for subsequent cycles. Experimental results across diverse benchmarks demonstrate that ECHO significantly boosts mean accepted tokens and achieves a 2.4$\times$ to 2.9$\times$ speedup, outperforming existing state-of-the-art baselines with negligible engineering overhead and no extra deployment parameters, albeit with a one-shot fine-tuning dependency for optimal acceleration. The code is available at https://github.com/whucs21Mzy/ECHO.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 9 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: speculative decoding
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Ziyang Ma, Zihong Zhang, Zuchao Li, Lefei Zhang, Baoyuan Qi, Siqi Li, Simin Yu
- 发布：2026-09-15；更新：2026-09-16
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/whucs21Mzy/ECHO](https://github.com/whucs21Mzy/ECHO)
- 阅读深度：metadata
