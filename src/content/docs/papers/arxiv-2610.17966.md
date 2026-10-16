---
title: "BELT : BEhavior-Aligned Low-Rank KV Cache Compression with Learned Top-k Rank Allocation"
description: "Long-context inference makes the key-value (KV) cache a major memory bottleneck for large language models."
---

**评分：54/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](http://arxiv.org/abs/2610.17966v1) · [PDF](https://arxiv.org/pdf/2610.17966v1)

## 一句话摘要

Long-context inference makes the key-value (KV) cache a major memory bottleneck for large language models.

## 为什么值得关注

待编辑增强。

## 摘要原文

Long-context inference makes the key-value (KV) cache a major memory bottleneck for large language models. We propose BELT, a low-rank KV cache compression framework. Its key-side objective targets attention distributions rather than raw keys or pre-softmax logits, yielding a quadratic surrogate with a closed-form low-rank solution. A learned global rank allocator uses differentiable soft selection during training and hard selection at deployment to meet a user-specified component budget. Experiments demonstrate improved model quality under aggressive compression and increased decoding throughput at comparable accuracy. Evaluated across three LLMs and multiple benchmarks, BELT achieves up to 70% low-rank KV cache compression while outperforming the strongest baseline by up to 23.3 points on LongBench, and up to 17.8x overall KV cache reduction when combined with quantization. With Triton-based GPU kernels and a quantized cache, BELT delivers up to 2.7x speedup for the attention module and 3.3x end-to-end decoding throughput.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 13 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Yaoyang Liu, Shuwei Shen, Jincheng Tang, Jinguang Liu, Jinbao Xue, Hailong Yang, Ke Zhang, Yinjun Wu
- 发布：2026-10-13；更新：2026-10-13
- 来源：arXiv；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
