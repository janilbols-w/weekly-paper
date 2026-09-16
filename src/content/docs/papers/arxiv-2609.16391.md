---
title: "Where Post-Training Quantization Breaks Text Embedders: A Measured Map Across Four Embedder Families"
description: "Weight-only post-training quantization is the cheapest way to shrink a retrieval embedder, and the received advice for applying it -- protect the embedding table, allocate bits by module sensitivity, prefer a ranking-aware objective over weight reconstruction -- was carried into LLM quantization largely intact."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2609.16391) · [PDF](https://arxiv.org/pdf/2609.16391)

## 一句话摘要

Weight-only post-training quantization is the cheapest way to shrink a retrieval embedder, and the received advice for applying it -- protect the embedding table, allocate bits by module sensitivity, prefer a ranking-aware objective over weight reconstruction -- was carried into LLM quantization largely intact.

## 为什么值得关注

待编辑增强。

## 摘要原文

Weight-only post-training quantization is the cheapest way to shrink a retrieval embedder, and the received advice for applying it -- protect the embedding table, allocate bits by module sensitivity, prefer a ranking-aware objective over weight reconstruction -- was carried into LLM quantization largely intact. We test that advice on retrieval embedders directly, quantizing five checkpoints from four architecture families across a grid of bit widths and group sizes, and isolating the embedding, attention and feed-forward blocks at each width. Every heuristic fails to transfer as stated. The embedding table never emerges as the dominant isolated protection priority in any family, despite being the largest tensor in several of them. Module sensitivity does not survive as a transferable ordering: at INT4/g16 the spread between modules is too small to allocate against, at INT3 the ordering becomes family-dependent and joint damage stops being the sum of its parts, and at INT2 comparable reconstruction error accompanies retention ranging from 1.3 to 65.9 percent of full precision. A cheap reconstruction proxy is useful for screening uniform bit widths but substantially less reliable for choosing which tensors to protect; its apparent strength across the whole grid is a range-extension artifact. A distilled 109M student at INT3 holds 78.04 NDCG@10 in 68.4 MB and dominates the extreme-PTQ arm of its own 0.6B teacher, 297.9 MB at 64.46, on both size and quality -- but only inside the task it was distilled for. Sizes are byte counts of files that exist rather than arithmetic estimates, and the measurement repository carries the byte provenance for every one of them.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 8 |
| reproducibility | 4 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: int4, quantization
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Hyojung Han
- 发布：2026-09-16；更新：2026-09-16
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
