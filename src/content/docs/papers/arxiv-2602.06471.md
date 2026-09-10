---
title: "Revisiting the Shape Convention of Transformer Language Models"
description: "The architectural shape of dense Transformers has remained remarkably stable: narrow-wide-narrow feed-forward networks (FFNs) consume most non-embedding parameters."
---

**评分：38/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2602.06471) · [PDF](https://arxiv.org/pdf/2602.06471)

## 一句话摘要

The architectural shape of dense Transformers has remained remarkably stable: narrow-wide-narrow feed-forward networks (FFNs) consume most non-embedding parameters.

## 为什么值得关注

待编辑增强。

## 摘要原文

The architectural shape of dense Transformers has remained remarkably stable: narrow-wide-narrow feed-forward networks (FFNs) consume most non-embedding parameters. Motivated by theoretical and empirical evidences that residual wide-narrow-wide (hourglass) MLPs remain expressive despite bottlenecks, we revisit whether this architectural convention is necessary for dense language models. We study Hourglass Transformers, which replace the conventional FFN with residual stacks of hourglass sub-MLPs and use hourglass attention to decouple residual-stream width from attention width. This exposes a practical depth-width trade-off: compressing the FFN intermediate dimension allows wider hidden states and fewer layers at matched parameter budgets. Across model scales from 113M to 8B parameters, Hourglass Transformers achieve language-modeling and downstream performance comparable to conventional Transformers, while improving training compute efficiency by $8.7\%$ at matched average downstream accuracy across the 906M, 3B, and 8B scales. After long-context extension, the 8B Hourglass model also outperforms its matched conventional baseline across 4k-64k context lengths. At 64k context, the reduced attention layer count lowers both computation and KV-cache requirements, yielding up to $1.93\times$ faster token decoding and $50\%$ lower KV-cache memory at the 1B scale. These results identify hourglass structures as a practical architecture-efficiency alternative for compute- and latency-conscious Transformer design.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv-cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Feng-Ting Liao, Guan-Ting Yi, Tzu-Quan Lin, Meng-Hsi Chen, Da-shan Shiu
- 发布：2026-09-10；更新：2026-09-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
