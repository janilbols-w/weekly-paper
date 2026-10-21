---
title: "PeekKV: The First Content Token Already Knows Which Heads Matter"
description: "The size of the KV cache grows linearly with context length, making it a major memory bottleneck in LLM serving."
---

**评分：40/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2610.23939) · [PDF](https://arxiv.org/pdf/2610.23939)

## 一句话摘要

The size of the KV cache grows linearly with context length, making it a major memory bottleneck in LLM serving.

## 为什么值得关注

待编辑增强。

## 摘要原文

The size of the KV cache grows linearly with context length, making it a major memory bottleneck in LLM serving. Motivated by recent progress in identifying the functional roles of attention heads, a growing body of work compresses the KV cache non-uniformly across heads. Existing methods either fix the important heads via offline profiling or select them using attention signals from the prefill stage. In both cases, however, accuracy fluctuates substantially across workloads. While investigating the cause of this instability, we find that the active heads shift between the prefill and decode stages even within a single input. Along the decode path, by contrast, the activehead composition remains stable across content tokens once format tokens are filtered out. Based on this observation, we propose PeekKV. PeekKV observes a single content token immediately after prefill - a one-token peek - to jointly obtain head-group scores and token-importance scores. Guided by these scores, PeekKV allocates KV cache budgets to head groups in proportion to their group scores and retains only the top-scoring tokens within each budget. PeekKV requires no offline profiling or training and thus applies directly to unseen workloads and new models. Across four public benchmarks, PeekKV achieves the highest accuracy in more than half of the per-model comparisons against state-of-the-art methods, and stays closest to the full-cache accuracy on RULER and LongBench. On Llama-3.1-8B-Instruct, PeekKV retains 95.7% of the full-cache accuracy at a 10% memory budget on RULER with 16K contexts and 95.9% at a 1.5% budget on LongBench.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Minyoung Go, Yongjun Park
- 发布：2026-10-20；更新：2026-10-21
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
