---
title: "Reformulating KV Cache Eviction Problem for Long-Context LLM Inference"
description: "Large language models (LLMs) support long-context inference but suffer from substantial memory and runtime overhead due to Key-Value (KV) Cache growth."
---

**评分：55/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2605.07234) · [PDF](https://arxiv.org/pdf/2605.07234)

## 一句话摘要

Large language models (LLMs) support long-context inference but suffer from substantial memory and runtime overhead due to Key-Value (KV) Cache growth.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models (LLMs) support long-context inference but suffer from substantial memory and runtime overhead due to Key-Value (KV) Cache growth. Existing KV Cache eviction methods primarily rely on local attention weights, neglecting the influence of value representations, output projection, and inter-head interactions. In this work, we reformulate KV Cache eviction from a conventional head-wise, weight-averaging approach into an output-aware, layer-wise matrix multiplication approximation problem. We introduce LaProx, a novel eviction strategy that explicitly models the multiplicative interaction between attention maps and projected value states to accurately quantify token contributions while accounting for inter-head dependencies. Building on this metric, we propose the first unified eviction strategy that assigns globally comparable importance scores to tokens, enabling model-wide selection instead of local, head-wise decisions. Experimental results across 19 datasets on long-context benchmarks LongBench and Needle-In-A-Haystack demonstrate that our approach maintains model performance with only 5% of the KV cache and consistently outperforms prior works across all configurations. Notably, our method achieves up to 2$\times$ accuracy loss reduction under extreme compression scenarios compared to existing state-of-the-art baselines with minimal overhead. Our code is available at https://github.com/huuthomai/LaProx.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 9 |
| rigor | 13 |
| practical impact | 7 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Tho Mai, Joo-Young Kim
- 发布：2026-11-09；更新：2026-11-09
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/huuthomai/LaProx](https://github.com/huuthomai/LaProx)
- 阅读深度：metadata
