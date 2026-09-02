---
title: "Latent Recurrent Transformer: Architecture Exploration, Training Strategies, and Scaling Behavior"
description: "We study Latent Recurrent Transformer (LRT), a lightweight augmentation of autoregressive transformers that reuses a high-level source-layer hidden state from the previous token as recurrent memory for the next token."
---

**评分：40/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2605.26797) · [PDF](https://arxiv.org/pdf/2605.26797)

## 一句话摘要

We study Latent Recurrent Transformer (LRT), a lightweight augmentation of autoregressive transformers that reuses a high-level source-layer hidden state from the previous token as recurrent memory for the next token.

## 为什么值得关注

待编辑增强。

## 摘要原文

We study Latent Recurrent Transformer (LRT), a lightweight augmentation of autoregressive transformers that reuses a high-level source-layer hidden state from the previous token as recurrent memory for the next token. Because this state is already computed during ordinary decoding, LRT introduces a cross-token, cross-layer latent pathway while preserving the standard attention mechanism, KV-cache interface, and one model forward per generated token. To pretrain this recurrence without sequentially unrolling the full sequence, we introduce interleaved parallel training: one full-sequence initialization forward constructs a shared buffer, followed by sequential refinement of disjoint position subsets with parallel computation within each subset. This provides every token with recurrent-memory-aware supervision at approximately 2x ideal token compute. Across 1.3B- and 2.1B-parameter nanochat-style backbones and a wide range of training budgets, LRT improves both BPB and CORE under matched effective compute. Additionally, LRT outperforms two-forward PonderLM-2 and matches a three-loop Transformer in BPB, while retaining one-forward-per-token decoding with 9% latency overhead over the standard Transformer.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv-cache
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Zeyi Huang, Xuehai He, LiLiang Ren, Yiping Wang, Baolin Peng, Hao Cheng, Shuohang Wang, Pengcheng He, Jianfeng Gao, Yong Jae Lee, Yelong Shen
- 发布：2026-09-02；更新：2026-09-02
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
