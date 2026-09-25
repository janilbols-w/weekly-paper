---
title: "Compressing Long Context into Answer-Aligned Memory Embeddings for LLM Inference"
description: "Large language model (LLM) inference is constrained by the quadratic scaling of self-attention and the linear scaling of the KV cache, increasing latency, energy consumption, and GPU memory demand as context length scales."
---

**评分：49/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2609.25537) · [PDF](https://arxiv.org/pdf/2609.25537)

## 一句话摘要

Large language model (LLM) inference is constrained by the quadratic scaling of self-attention and the linear scaling of the KV cache, increasing latency, energy consumption, and GPU memory demand as context length scales.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language model (LLM) inference is constrained by the quadratic scaling of self-attention and the linear scaling of the KV cache, increasing latency, energy consumption, and GPU memory demand as context length scales. Existing soft-compression methods either lack query-guided memory selection at inference time, train without answer-targeted supervision, or couple compression tightly to a specific decoder architecture. We propose a Context-to-Answer-Aligned Memory Compression (CMC) framework, which compresses long input contexts into compact Context Memory Embeddings (CMEs) aligned to any frozen decoder's embedding space, reducing inference costs without modifying decoder weights. CMC introduces a two-tier KV cache that combines question-guided CME selection with a local context window, and trains the compressor with answer-targeted distillation from a frozen LLM. Experiments across nine encoder-decoder combinations and four QA benchmarks show that CMC consistently outperforms the baseline, achieving up to 7.3 EM and 4.0 F1 point gains on SQuAD, while reducing inference time and energy consumption by up to 20% and peak reserved GPU memory by up to 50% at 3,000 generation tokens. Ablation studies confirm that each architectural component and training objective contributes to the performance.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 13 |
| practical impact | 13 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Md Mostafizer Rahman, Md Faizul Ibne Amin, Md Shahajada Mia, Yutaka Watanobe, Fang Liu
- 发布：2026-09-22；更新：2026-09-23
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
