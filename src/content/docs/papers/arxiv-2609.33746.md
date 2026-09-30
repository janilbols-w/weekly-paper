---
title: "PQ-HSA: Reusing Product-Quantized Scores for Hybrid Sparse-Approximate Attention"
description: "At each decoding step a language model attends over the key-value (KV) cache of every earlier token, so at long context the attention call is bounded by memory bandwidth."
---

**评分：52/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2609.33746) · [PDF](https://arxiv.org/pdf/2609.33746)

## 一句话摘要

At each decoding step a language model attends over the key-value (KV) cache of every earlier token, so at long context the attention call is bounded by memory bandwidth.

## 为什么值得关注

待编辑增强。

## 摘要原文

At each decoding step a language model attends over the key-value (KV) cache of every earlier token, so at long context the attention call is bounded by memory bandwidth. Sparse attention reads only a subset of keys chosen by a cheap score estimate, and most methods give the unread tokens zero weight. The output then draws on only a small fraction of the KV cache, and accuracy drops at small budgets, most on tasks that aggregate information across the context. An inverted-file product-quantization (IVF-PQ) index over the cached keys computes an approximate score for every indexed token in order to rank them; after ranking, those scores approximate the attention logits of the tokens left out. PQ-HSA (hybrid sparse-approximate attention) attends the selected tokens with their original keys and values, and the unselected tokens, the background, enter the same softmax through those scores, summed per inverted list and multiplied by the list's mean value. At 128K and a 1-2% retrieval budget, PQ-HSA is more accurate than Quest and SnapKV on Llama-3.1-8B and Qwen3-30B-A3B and stays close to full attention in macro accuracy; with the same selector, the background term raises macro accuracy on the 8B model from 0.71 to 0.83. In the same 128K setting, inside vLLM on one NVIDIA H20, the decode attention call runs 1.6x faster than the FlashAttention-3 kernel; the speedup grows with context length, and a cost model fitted on 8B to 30B models gives the context length at which it begins. A vLLM plugin runs PQ-HSA on two engine versions without changes to the engine source; code is available at https://github.com/KunmingSHAO/pqhsa_release.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 14 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- quantitative claim detected
- code/artifact link detected

## 元数据

- 作者：Kunming Shao, Jierun Chen, Yanli Wang, Ruoyu Wang, Haoli Bai, Kwang-Ting Cheng, Chi Ying Tsui
- 发布：2026-09-30；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/KunmingSHAO/pqhsa_release](https://github.com/KunmingSHAO/pqhsa_release)
- 阅读深度：metadata
