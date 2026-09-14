---
title: "SAS: Simple Attention Sparsification via End-to-End Optimization of Context Ranking"
description: "Post-training attention sparsification reduces the quadratic cumulative attention cost of pretrained Transformers by selecting a small set of context units (tokens or blocks) for each query."
---

**评分：39/100** · LLM 高效推理 > Runtime 与内存效率 > Kernel 与算子融合

[论文原文](https://arxiv.org/abs/2609.13141) · [PDF](https://arxiv.org/pdf/2609.13141)

## 一句话摘要

Post-training attention sparsification reduces the quadratic cumulative attention cost of pretrained Transformers by selecting a small set of context units (tokens or blocks) for each query.

## 为什么值得关注

待编辑增强。

## 摘要原文

Post-training attention sparsification reduces the quadratic cumulative attention cost of pretrained Transformers by selecting a small set of context units (tokens or blocks) for each query. Existing trainable methods usually use a lightweight selector to score context units, followed by hard Top-K selection that blocks gradients from the language modeling loss. Consequently, these methods commonly distill layer-wise dense attention distributions. Although this encourages the selector to rank context units by dense attention weights in the original model, the ranking is not directly aligned with their impact on predictions under a fixed attention budget (i.e., the number of attended context units per query), potentially wasting the limited budget on less useful units. To address this misalignment, we propose Simple Attention Sparsification (SAS), a gated sparse attention mechanism that optimizes context ranking end-to-end with the language modeling loss. The key idea is to inject the selector's continuous scores into attention logits during training, allowing the loss to update the selector through standard backpropagation. We identify several choices crucial for this simple design to work well in practice: placing the gate inside the attention softmax in log form, using normalized softmax gates to calibrate historical context against the always-retained current block, and preserving continuous selector scores so the model learns relative priorities rather than only hard selections. To support long-sequence training, we implement a memory-efficient Triton kernel that integrates SAS into FlashAttention-style computation. Across reasoning, long-context understanding, and agentic tasks, SAS consistently outperforms trainable sparse attention baselines across attention budgets, with especially large gains under tight budgets, demonstrating more effective context ranking for downstream tasks.

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

- taxonomy keywords: triton kernel
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zhiwei Li, Lei Zhu, Hao Gu, Xiang Hu, Yan Wang, Haitao Mi, Sirui Han, Leo Liang, Zhijiang Guo
- 发布：2026-09-14；更新：2026-09-14
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
