---
title: "KVUse: Reusable-KV User Memory for Efficient LLM Recommenders"
description: "Memory-augmented recommenders built on large language models (LLMs) maintain a natural-language profile of each user."
---

**评分：43/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2611.21920) · [PDF](https://arxiv.org/pdf/2611.21920)

## 一句话摘要

Memory-augmented recommenders built on large language models (LLMs) maintain a natural-language profile of each user.

## 为什么值得关注

待编辑增强。

## 摘要原文

Memory-augmented recommenders built on large language models (LLMs) maintain a natural-language profile of each user. These profiles are updated by a user profile update path that revises the profile as new interactions arrive and are consumed by downstream task paths like ranking. Because these user profiles are stored as text in the user memory, every ranking LLM call that consumes them must splice them in the prompt and calculate the KV cache of them during the prefill phase. Given these ranking LLM calls are prefill heavy (long prompt but short decoded output) and repeatedly called, these repeated prefill of user profile text dominates the serving. Prefix caching cannot remove it, because these user profiles are preceded by different text in different calls. We present KVUse, which stores the user profiles as reusable key-value (KV) caches instead of text. KVUse trains lightweight LoRA writers by self-distillation, so that the user profile update call produces the reusable KV of the user profile while decoding it, and the LLM can read these reusable KV at new positions and behind new context without recomputation. KVUse also has a customized KV scheduler that uploads the stored reusable KV of the next batch while the current batch is computed, hiding the KV transfer from host memory behind GPU computation. On four InstructRec datasets with Llama-3.1-8B-Instruct, KVUse shows no statistically significant difference in ranking quality from full prefill over continuous memory update rounds. Under saturated load, KVUse raises the throughput of the downstream scoring path by 4.0x-4.5x and of the profile update path by 1.4x-1.9x.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache, prefix caching
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Xin Guo, Qiang Zhang, Xiang Zhou, Arushi Rai, Siyu Lin, Yifan Wu, Xiang Shen, Lei Huang, Qunshu Zhang, Xiangjun Fan, Lizhu Zhang
- 发布：2026-11-18；更新：2026-11-18
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
