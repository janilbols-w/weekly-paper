---
title: "BF1: A Causal Dyadic Sparse-Attention Retrofit for Efficient Long-Context Transformers"
description: "Dense causal attention remains expensive at long context even when implemented with highly optimized exact kernels."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2608.20427) · [PDF](https://arxiv.org/pdf/2608.20427)

## 一句话摘要

Dense causal attention remains expensive at long context even when implemented with highly optimized exact kernels.

## 为什么值得关注

待编辑增强。

## 摘要原文

Dense causal attention remains expensive at long context even when implemented with highly optimized exact kernels. We study BF1, a deterministic block-aligned dyadic sparse-attention route that combines a small exact local neighborhood, a global first block, and logarithmically spaced historical blocks. The route is related to prior log-sparse and dilated attention patterns; our contribution is a correctness-gated pretrained-model retrofit, a matched topology-control study, and a systems characterization that connects per-layer sparsity to whole-model latency. For fixed block width, every converted layer uses O(n log n) selected token interactions and has O(log n) graph communication depth. On an NVIDIA RTX PRO 6000 Blackwell GPU, an optimized BF16 implementation crosses dense attention between 2K and 4K tokens and reaches a 10.91x per-layer prefill speedup at 32K. Retrofitting eight of 28 Qwen3-0.6B attention layers lowers warm whole-model time to first token by 7.7%, 11.3%, and 15.3% at 8K, 16K, and 32K, respectively, while the remaining dense layers keep the complete model asymptotically quadratic. Under a matched 1,000-step, 16.384M-token adaptation protocol, BF1 ranks first across three training seeds: mean report perplexity is 1.68639 versus 1.69154 for a matched static-random nonlocal graph, 1.69258 for dense continued training, and 1.81505 for equal-budget local sliding. At seed 1234, the packed-report paired interval places Dense-CT 0.3169-0.4055% above BF1 and static-random graph 17 0.2441-0.3642% above BF1. These results establish BF1 as a reproducible sparse operator and selective retrofit primitive with real long-context systems value. This paper evaluates numerical correctness, selected-interaction scaling, kernel performance, partial-model inference, and matched next-token language modeling.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 12 |
| reproducibility | 3 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: sparsity
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Hina Dixit
- 发布：2026-08-24；更新：2026-08-24
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
