---
title: "GraphVQ: Structure-Aware Autoregressive Decoding over Context-Quantized Graph Tokens"
description: "Graph foundation models need a discrete token representation, but casting a graph as a generatable token sequence faces a structural obstacle: edges spanning beyond the serialization window cannot be emitted in one pass--so one-pass autoregressive generators systematically under-produce cycles--and a single global condition cannot tell candidate edges apart."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](http://arxiv.org/abs/2609.37604v1) · [PDF](https://arxiv.org/pdf/2609.37604v1)

## 一句话摘要

Graph foundation models need a discrete token representation, but casting a graph as a generatable token sequence faces a structural obstacle: edges spanning beyond the serialization window cannot be emitted in one pass--so one-pass autoregressive generators systematically under-produce cycles--and a single global condition cannot tell candidate edges apart.

## 为什么值得关注

待编辑增强。

## 摘要原文

Graph foundation models need a discrete token representation, but casting a graph as a generatable token sequence faces a structural obstacle: edges spanning beyond the serialization window cannot be emitted in one pass--so one-pass autoregressive generators systematically under-produce cycles--and a single global condition cannot tell candidate edges apart. GraphVQ removes both obstacles: node contexts--features plus a local edge mask under multi-order breadth-first serialization--are quantized into a shared codebook by a VQ-VAE with BCE-calibrated Bernoulli edge decoding, and a second-stage structure-aware decoder emits the global adjacency conditioned on token-derived pair features, whose necessity over any global-summary condition is formalized in a scoped impossibility result. The tokenizer reconstructs node features at 0.86--0.99 accuracy and decodes local edges at AUROC >= 0.89 (ECE 0.174 on PROTEINS and 3.4x on a ring stress test, and vanishes on a random-label control--the signature of attribute--topology coupling--so the gain is claimed exactly where attributes carry edge-relevant signal. GraphVQ ranks first among learned generators on PROTEINS, ties for first on SYN-COMM, and improves orbit MMD 2.7--17x over one-stage generation on three datasets, with seed-level bootstrap intervals confirming the rankings are not seed noise; on MUTAG the unweighted edge target under-generates and is reported as such. These results locate the structural control of autoregressive graph generation in the granularity of the condition: pair-level token context turns a quantized vocabulary into a usable capacity axis for distribution-faithful graph generation and future token-level pretraining.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 8 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantized
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Yuxiang Yao, Zijun Zhao
- 发布：2026-09-29；更新：2026-09-29
- 来源：arXiv；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
