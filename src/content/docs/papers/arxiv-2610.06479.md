---
title: "Behavior-Preserving KV Cache Compression"
description: "KV caches are a major bottleneck in long-context inference and long-form generation with large language models."
---

**评分：41/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2610.06479) · [PDF](https://arxiv.org/pdf/2610.06479)

## 一句话摘要

KV caches are a major bottleneck in long-context inference and long-form generation with large language models.

## 为什么值得关注

待编辑增强。

## 摘要原文

KV caches are a major bottleneck in long-context inference and long-form generation with large language models. Existing training-free eviction policies largely rely on proxy importance signals, such as attention mass, to decide which past tokens to retain. We argue that cache compression should instead preserve the predictive behavior of the full-cache model, retaining entries whose removal would substantially change the model's output distribution. We propose Behavior-Preserving KV Cache Compression, a training-free framework that scores candidate evictions by estimating the compressed-cache logits induced by their removal and evaluating the resulting KL to the full-cache next-token distribution. Using pre-eviction forward statistics, the method avoids running separate masked forward passes for each candidate. Across diverse architectures and both prefill-time and generation-time compression, our method delivers substantial gains in downstream task quality over lightweight attention-based heuristics at matched retained-KV budgets, with the largest gains under aggressive compression. It achieves these gains with additional compression-time computation while retaining an end-to-end speedup over full-cache inference in our evaluated settings.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Doo Hwan Hwang, Junyoung Jang, Junho Na, Hosung Lim, Kee-Eung Kim
- 发布：2026-10-06；更新：2026-10-06
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
