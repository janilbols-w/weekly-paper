---
title: "BridgeKV: Large-Model Prefill and Small-Model Decoding for LLM Inference via KV Cache Translation"
description: "LLM inference has two phases with different bottlenecks: LLM prefill runs once per request and is compute-intensive."
---

**评分：50/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2611.11761) · [PDF](https://arxiv.org/pdf/2611.11761)

## 一句话摘要

LLM inference has two phases with different bottlenecks: LLM prefill runs once per request and is compute-intensive.

## 为什么值得关注

待编辑增强。

## 摘要原文

LLM inference has two phases with different bottlenecks: LLM prefill runs once per request and is compute-intensive. Decoding repeats for every output token and is limited by memory bandwidth. To address the challenges associated with this issue, different solutions have been proposed. All of these solutions use the same model for both prefill and decode phases. We propose BridgeKV, which uses a larger model for prefill and a smaller model of the same family for decoding. A lightweight KV-stitching module translates the larger model's prompt cache into the smaller model's cache layout. It handles differences in cache shape and representation through learned local layer mixing and separate nonlinear maps for keys and values. With both models frozen, we train the module to align their caches and make the smaller model follow the larger model's next-token predictions. A second training stage adds low-rank adapters when further task adaptation is needed. Across six model pairs and five datasets, BridgeKV outperforms fine-tuned small-model baselines with matched trainable parameter budgets in all 30 settings. It closes up to 80% of the quality gap to using the larger model for both phases. On one A40 GPU, Llama-3.1-Instruct-8B to Llama-3.2-Instruct-1B achieves 3.0X faster requests than the larger model alone, with latency close to the smaller model alone. BridgeKV can improve the hardware and system solutions that separate prefill and decode phases across GPUs. A separate serving simulation models request arrivals, queues, and cache transfer. For Llama-3.1-Instruct-70B to Llama-3.2-Instruct-1B, it predicts up to 33.86X faster requests and 27.5X lower energy use than using the larger model for both prefill and decode phases.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Payman Behnam, Debopam Sanyal, Pranav Ponnusamy, Kusum Meda Ravi, Pranav Sastry, Mani Chandana Bandaru, Alind Khare, Myungjin Lee, Alexey Tumanov
- 发布：2026-11-10；更新：2026-11-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
