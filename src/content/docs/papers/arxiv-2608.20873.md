---
title: "Nothing Changed but the Model: CellFill -- Bounded In-Cell Learning for Bit-Identical, Revocable Updates to Quantized LLMs"
description: "Every way of teaching a deployed language model something new -- full fine-tuning, adapter merging, model editing -- replaces the released checkpoint, and with it every evaluation and cache that referred to those exact bits."
---

**评分：46/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2608.20873) · [PDF](https://arxiv.org/pdf/2608.20873)

## 一句话摘要

Every way of teaching a deployed language model something new -- full fine-tuning, adapter merging, model editing -- replaces the released checkpoint, and with it every evaluation and cache that referred to those exact bits.

## 为什么值得关注

待编辑增强。

## 摘要原文

Every way of teaching a deployed language model something new -- full fine-tuning, adapter merging, model editing -- replaces the released checkpoint, and with it every evaluation and cache that referred to those exact bits. We instead learn inside the dequantization gap: with the integer codes and scales of a 4-bit release frozen, new knowledge is written only into the per-weight residual that lives strictly inside each quantization decision cell. Re-quantization then returns the released artifact bit-for-bit, a machine-checkable guarantee; updates are exactly revocable by dropping the residual; and drift is bounded. We give six propositions and three training paths, including CellFill, a bounded reparameterization that makes invariance structural rather than enforced. Exact invariance turns out to be nearly free: across three paired seeds the constrained dense path matches an unconstrained reference whose weights provably escape the artifact (58.9 vs 59.3 percent fact recall; paired difference -0.5 points, 95% CI [-5.0,+4.0]), and is better on held-out cross-domain perplexity. Against the natural null hypothesis -- serving the same update as an unmerged adapter -- projecting into the cells reduces cross-domain forgetting in every run that converged, and a diverged control shows the boundary: projection is a trust region, not a repair. What no method escapes is the cost of knowledge itself, and the apparent free lunch of in-domain perplexity improving past the anchor is an artifact of rehearsal sharing a corpus with the metric. Methods differ threefold at matched rehearsal in knowledge bought per point of cross-domain perplexity, a ranking that is not the recall ranking. The method transfers to a 27B hybrid linear-attention model (2.4e10 constrained weights, verified bit-identical), where matched recall costs about half as much cross-domain perplexity as at 1.7B.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 10 |
| reproducibility | 3 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Zifeng Liu, Zhiyong Du, Yaxin Lu, Yiming Mao, Zhenhe Wang, Wenqi Shi, Zhengkun Jing
- 发布：2026-08-24；更新：2026-08-24
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
