---
title: "Key-Value Means: Transformers with Expandable Block-Recurrent Compressed Memory"
description: "Recall presents a difficult choice: transformers have a linearly growing memory that slows each successive token, while linear RNNs typically have fixed costs but limited recall."
---

**评分：44/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2605.09877) · [PDF](https://arxiv.org/pdf/2605.09877)

## 一句话摘要

Recall presents a difficult choice: transformers have a linearly growing memory that slows each successive token, while linear RNNs typically have fixed costs but limited recall.

## 为什么值得关注

待编辑增强。

## 摘要原文

Recall presents a difficult choice: transformers have a linearly growing memory that slows each successive token, while linear RNNs typically have fixed costs but limited recall. We present Key-Value Means ("KVM"), a novel block-recurrence for attention that can accommodate either fixed-size or growing state. Equipping a strong transformer baseline with fixed-size KVM attention layers yields a strong $O(N)$ chunked RNN, while adding only an insignificant number of new parameters. We train a transformer with a growable KVM cache and show it performs competitively on long-context tests with only subquadratic prefill time and sublinear state growth. KVM is implementable with standard operations and without custom kernels, and supports chunk-wise parallelizable training and prefill. It provides many of the benefits of both traditional transformers (expandable context memory, chunk-wise parallelizable training and prefill) and RNNs in a single unified package. It can be used on every layer, saving KV-cache memory, and allowing a continuous range of choices of prefill time complexity between $O(N)$ and $O(N^2)$. We release our code at https://github.com/featherless-ai/KVM-paper and trained models at https://huggingface.co/collections/featherless-ai/kvm-paper under the Apache 2.0 license.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv-cache
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Daniel Goldstein, Navneel Singhal, Eugene Cheah
- 发布：2026-08-04；更新：2026-08-04
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/featherless-ai/KVM-paper](https://github.com/featherless-ai/KVM-paper)
- 阅读深度：metadata
