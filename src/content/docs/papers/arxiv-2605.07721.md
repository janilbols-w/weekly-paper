---
title: "Memory-Efficient Looped Transformer: Decoupling Compute from Memory in Looped Language Models"
description: "Recurrent LLM architectures have emerged as a promising approach for improving reasoning, as they enable multi-step computation in the embedding space without generating intermediate tokens."
---

**评分：38/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2605.07721) · [PDF](https://arxiv.org/pdf/2605.07721)

## 一句话摘要

Recurrent LLM architectures have emerged as a promising approach for improving reasoning, as they enable multi-step computation in the embedding space without generating intermediate tokens.

## 为什么值得关注

待编辑增强。

## 摘要原文

Recurrent LLM architectures have emerged as a promising approach for improving reasoning, as they enable multi-step computation in the embedding space without generating intermediate tokens. Models such as Ouro perform reasoning by iteratively updating internal representations while retaining a standard Key-Value (KV) cache across iterations, causing memory consumption to grow linearly with reasoning depth. Consequently, increasing the number of reasoning iterations can lead to prohibitive memory usage, limiting the practical scalability of such architectures. In this work, we propose Memory-Efficient Looped Transformer (MELT), a novel architecture that decouples reasoning depth from memory consumption. Instead of using a standard KV cache per layer and loop, MELT maintains a single KV cache per layer that is shared across reasoning loops. This cache is updated over time via a learnable gating mechanism. To enable stable and efficient training under this architecture, we propose to train MELT using chunk-wise training in a two phase procedure: interpolated transition, followed by attention-aligned distillation, both from the LoopLM starting model to MELT. Empirically, we show that MELT models fine-tuned from pretrained Ouro parameters outperform standard LLMs of comparable size, while maintaining a memory footprint comparable to those models and dramatically smaller than Ouro's. Overall, MELT achieves constant-memory iterative reasoning without sacrificing LoopLM performance, using only a lightweight post-training procedure.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 5 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Victor Conchello Vendrell, Arnau Padres Masdemont, Niccol\`o Grillo, Jordi Ros-Giralt, Arash Behboodi, Fabio Valerio Massoli
- 发布：2026-09-30；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
