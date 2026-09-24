---
title: "DeltaS: Reading the Gated Linear Attention State for KV Cache Eviction in Streaming Video"
description: "Recent video-language models increasingly adopt hybrid architectures that interleave linear and full attention layers for efficient long-context processing."
---

**评分：50/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2609.27470) · [PDF](https://arxiv.org/pdf/2609.27470)

## 一句话摘要

Recent video-language models increasingly adopt hybrid architectures that interleave linear and full attention layers for efficient long-context processing.

## 为什么值得关注

待编辑增强。

## 摘要原文

Recent video-language models increasingly adopt hybrid architectures that interleave linear and full attention layers for efficient long-context processing. While the recurrent state of linear attention remains fixed in size, the KV cache of full attention continues to grow with the video stream, making eviction necessary under a bounded memory budget. The key challenge in streaming is that eviction must occur before the question arrives, so what to retain has to be decided without the question. Existing eviction methods derive token scores from the KV cache itself, using position, attention, or key-value representations, and attention-based scores further require proxy queries or extra computation. Hybrid backbones offer another source of signal. In gated-delta linear attention, the recurrent state is updated by the residual between each input and what can already be retrieved from the state, so its change over a chunk of frames reflects how much new information the chunk brings. We propose DeltaS, a query-agnostic, training-free method that retains video chunks inducing larger normalized state change, or state drift. In a controlled comparison with the budget and retention policy held fixed, state drift outperforms position-, attention-, and key-value-based signals. With a signal costing only 1.9% of the forward pass, DeltaS surpasses the strongest query-agnostic bounded-memory baseline by 2.1 points on average across six long-video benchmarks and by 5.6 points on the longest benchmark. These results suggest that the two memories of hybrid architectures can work cooperatively. Code is available at https://github.com/MaumAI-Company/DeltaS.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Taeyoun Kwon, Seungjin Kim, Hyeonyu Kim, Moon Hwan Kim
- 发布：2026-09-24；更新：2026-09-24
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/MaumAI-Company/DeltaS](https://github.com/MaumAI-Company/DeltaS)
- 阅读深度：metadata
