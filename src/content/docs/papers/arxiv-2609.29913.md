---
title: "MILO: Efficient Many-shot In-Context Learning with Block-wise Low-rank Compression"
description: "Many-shot in-context learning (ICL) enables large language models (LLMs) to adapt to complex tasks by conditioning on thousands of demonstration examples, but this paradigm shifts the inference efficiency bottleneck to the key-value (KV) cache memory."
---

**评分：47/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2609.29913) · [PDF](https://arxiv.org/pdf/2609.29913)

## 一句话摘要

Many-shot in-context learning (ICL) enables large language models (LLMs) to adapt to complex tasks by conditioning on thousands of demonstration examples, but this paradigm shifts the inference efficiency bottleneck to the key-value (KV) cache memory.

## 为什么值得关注

待编辑增强。

## 摘要原文

Many-shot in-context learning (ICL) enables large language models (LLMs) to adapt to complex tasks by conditioning on thousands of demonstration examples, but this paradigm shifts the inference efficiency bottleneck to the key-value (KV) cache memory. Due to the linear scaling behavior of the KV cache, storing these intermediate tensors has become a paramount challenge for both online serving and on-device deployment. To address this issue, we propose a novel compression framework, termed MILO, that exploits the low-rank redundancy inherent in many-shot contexts. Specifically, MILO features a block-wise low-rank compression strategy that compresses the KV cache at the block granularity, where each block contains multiple many-shot examples. Furthermore, to handle the heterogeneous context density across different blocks, MILO dynamically allocates rank budgets based on the information entropy, preserving the fidelity of critical blocks while aggressively compressing redundant ones. Experimental results on Qwen2.5 models demonstrate that our method achieves up to 50% reduction in KV cache memory and 1.8x throughput improvement, with negligible performance degradation on classification and reasoning benchmarks, significantly outperforming prior baselines.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 11 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Youpeng Zhao, Tian Tan, Liqian Peng, Jun Wang, Alec Go
- 发布：2026-09-24；更新：2026-09-25
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
