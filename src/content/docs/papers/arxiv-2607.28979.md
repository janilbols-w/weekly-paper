---
title: "KV Cache Translation across Heterogeneous Large Language Models"
description: "Heterogeneous Large Language Model (LLM) systems increasingly share contexts, retrieved evidence, and multi-agent dialogue histories, yet their internal key-value (KV) caches remain model-specific and cannot be reused across architectures."
---

**评分：52/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2607.28979) · [PDF](https://arxiv.org/pdf/2607.28979)

## 一句话摘要

Heterogeneous Large Language Model (LLM) systems increasingly share contexts, retrieved evidence, and multi-agent dialogue histories, yet their internal key-value (KV) caches remain model-specific and cannot be reused across architectures.

## 为什么值得关注

待编辑增强。

## 摘要原文

Heterogeneous Large Language Model (LLM) systems increasingly share contexts, retrieved evidence, and multi-agent dialogue histories, yet their internal key-value (KV) caches remain model-specific and cannot be reused across architectures. Consequently, each model must repeatedly prefill or store caches for the same context, limiting the scalability of multi-model reasoning and long-context generation. We propose Mixture-of-Translators (MoT), a cache translation framework that maps context KV caches from a source LLM into the cache space of a target LLM. Unlike prior approaches that depend on a single projection path or global shared latent space, MoT uses multiple translator modules with token-level routing to capture diverse cache translations. We further introduce a Context Correction Loss that aligns the replayed target trajectory with the native target trajectory, reducing residual translation error. Our analysis reveals two competing failure modes: propagation error from early injection and correction-deficit error from late injection. We evaluate heterogeneous translation among Llama, Gemma, and Qwen, spanning substantially different architectures and KV-cache spaces. MoT achieves an average accuracy of 57.6% and F1 of 0.42. These scores recover 95.0% and 120.6% of native target performance and reach 1.5x and 3.5x the strongest-baseline scores, respectively. In practical case studies, MoT enables accurate heterogeneous-agent discussion with scale-invariant KV-memory behavior as the number of agents grows, while retaining near-native generation quality in long-context cache-augmented generation. These results demonstrate scalable KV-cache reuse across heterogeneous LLMs.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 20 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: context cache, kv cache, kv-cache
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Jin-woo Lee, Minkyung Song, Junghyun Oh, Seunghoon Han, Gwangseon Jang, Soyoung Park, Sungsu Lim
- 发布：2026-10-06；更新：2026-10-06
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
