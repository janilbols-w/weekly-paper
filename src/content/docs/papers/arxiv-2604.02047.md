---
title: "Goose: Anisotropic Speculation Trees for Training-Free Speculative Decoding"
description: "Speculative decoding accelerates large language model inference by drafting multiple candidate tokens and verifying them in a single forward pass."
---

**评分：45/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2604.02047) · [PDF](https://arxiv.org/pdf/2604.02047)

## 一句话摘要

Speculative decoding accelerates large language model inference by drafting multiple candidate tokens and verifying them in a single forward pass.

## 为什么值得关注

待编辑增强。

## 摘要原文

Speculative decoding accelerates large language model inference by drafting multiple candidate tokens and verifying them in a single forward pass. Candidates are organized as a tree: deeper trees accept more tokens per step, but adding depth requires sacrificing breadth (fallback options) under a fixed verification budget. Existing training-free methods draft from a single token source and shape their trees without distinguishing candidate quality across origins. We observe that two common training-free token sources -- n-gram matches copied from the input context, and statistical predictions from prior forward passes -- differ sharply in acceptance rate (~6x median gap, range 2-18x across five models and five benchmarks). We prove that when such a quality gap exists, the optimal tree is anisotropic (asymmetric): reliable tokens should form a deep chain while unreliable tokens spread as wide branches, raising the depth ceiling of balanced trees. We realize this structure in GOOSE, a training-free framework that builds an adaptive spine tree: a deep chain of high-acceptance context-matched tokens with wide branches of low-acceptance alternatives at each node. The resulting tree provably accepts at least as many tokens per step as either source alone. On five LLMs (7B-33B) and five benchmarks, GOOSE achieves 1.9-4.3x lossless speedup, outperforming balanced-tree baselines by 12-33% under the same budget.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: speculative decoding
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Tao Jin, Phuong Minh Nguyen, Naoya Inoue
- 发布：2026-08-11；更新：2026-08-11
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
