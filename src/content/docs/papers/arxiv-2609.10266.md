---
title: "KVShareArena: KV-Cache Reuse Across Contexts and Model Checkpoints"
description: "Reusing key-value (KV) caches speeds up LLM inference by avoiding repeated computation on shared text."
---

**评分：63/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2609.10266) · [PDF](https://arxiv.org/pdf/2609.10266)

## 一句话摘要

Reusing key-value (KV) caches speeds up LLM inference by avoiding repeated computation on shared text.

## 为什么值得关注

待编辑增强。

## 摘要原文

Reusing key-value (KV) caches speeds up LLM inference by avoiding repeated computation on shared text. Standard prefix caching reuses a KV cache only when the LLM is the same and all preceding text is identical, but real workloads often break both conditions: RAG systems place different documents before the same one, agents with different system prompts read the same file or tool output, multi-agent workflows use specialized LLMs on shared material, and an updated model reads documents cached by its previous version. Because KV caches depend on both the preceding text and the model weights, direct reuse can reduce answer quality. Many methods repair or compress the reused cache, but each paper uses its own tasks, models, and cost measures, and existing benchmarks mainly test long-context processing or reuse of an unchanged prefix. We introduce KVShareArena, a benchmark and open evaluation framework for comparing them under the same conditions. KVShareArena has (1) reuse tests on 2,150 questions from three QA datasets, where the preceding text, the cache-writing LLM, or both change while the answering LLM and input stay fixed; (2) five dense and mixture-of-experts LLMs (4B-30B) and six LLM pairs where one version of an LLM reads caches written by another, for 33 model-dataset settings; (3) 11 repair and compression methods from six method classes; (4) four evaluation perspectives: answer quality, prefill computation, KV-cache memory, and latency; and (5) a common interface for adding new methods and an interactive leaderboard. Experiments yield two findings. First, both the quality loss from reuse and which repairs help depend on the LLM, even between two 8B models. Second, most repairs keep their quality when another LLM version wrote the cache, but a trained repair adapter loses quality in 12 of 18 pair-dataset tests. Code and data: https://github.com/xishi404/KVShare-Arena

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 20 |
| novelty | 7 |
| rigor | 15 |
| practical impact | 11 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache, kv-cache, prefix caching
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Xi Shi, Qian Lou
- 发布：2026-09-09；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/xishi404/KVShare-Arena](https://github.com/xishi404/KVShare-Arena)
- 阅读深度：metadata
