---
title: "KVMem: Virtualizing Million-Token Agent Workspaces on a Consumer GPU"
description: "Modern LLM agents operate in persistent workspaces whose accumulated history can exceed both GPU KV capacity and the model's native context window."
---

**评分：38/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2609.04852) · [PDF](https://arxiv.org/pdf/2609.04852)

## 一句话摘要

Modern LLM agents operate in persistent workspaces whose accumulated history can exceed both GPU KV capacity and the model's native context window.

## 为什么值得关注

待编辑增强。

## 摘要原文

Modern LLM agents operate in persistent workspaces whose accumulated history can exceed both GPU KV capacity and the model's native context window. Existing systems typically compact older context into summaries or retrieve it later as text, either losing fine-grained execution evidence or repeatedly prefilling content that the model has already processed. We present KVMem, a KV-context virtualization system that preserves overflowed workspace history as paged KV state across GPU memory, host memory, and NVMe. KVMem uses lightweight, model-native attention-space indexes to select relevant historical blocks and materializes a query-dependent execution view bounded by the model's native context window. Extensive evaluations on long-context agent benchmarks spanning histories up to one million tokens, including LongMemEval, MemoryAgentBench, and AgentLongBench, show that KVMem generally achieves higher task utility and greater inference efficiency than compaction-based approaches, the de facto standard for handling context overflow. In the DeepSWE long-context test with Qwen3.8-27B, KVMem improves task success from 43.8% with compaction-only context management to 48.4%. In our local-deployment evaluation, KVMem runs Qwen3.6/3.8-27B NVFP4 with MTP on an off-the-shelf laptop equipped with a 24\,GB RTX 5090 Laptop GPU, virtualizing agent workspaces of up to 1M tokens-four times the model's native 256K-token context window. In a single-session setting, KVMem generates $\sim$50 tokens/s, providing interactive responsiveness for local agent execution. More broadly, by decoupling addressable workspace size from the LLM's native context window, KVMem provides a practical path toward long-running agents whose workspaces can grow beyond that window.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu memory
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Di Chai, Leye Wang, Zeshen Su, Zhiguo Xia, Zhihang Yu
- 发布：2026-09-07；更新：2026-09-07
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
