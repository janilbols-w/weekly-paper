---
title: "Unified AI Gateway: A Framework for Joint Model Routing and KV Cache Management"
description: "Large language model (LLM) inference increasingly spans models that differ in size, capability, price, and provider."
---

**评分：44/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2609.06940) · [PDF](https://arxiv.org/pdf/2609.06940)

## 一句话摘要

Large language model (LLM) inference increasingly spans models that differ in size, capability, price, and provider.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language model (LLM) inference increasingly spans models that differ in size, capability, price, and provider. This shift creates two costs for developers. One is the integration cost of choosing among and switching between many models. The other is the inference cost of rebuilding a KV cache when it is unavailable or incompatible with the selected model. We define and analyze the Unified AI Gateway as a system setting for an edge-deployed AI traffic hub. It coordinates model routing, KV cache management, and compute placement across end devices, edge resources, and cloud model services. At request time, the gateway jointly selects a target model, an execution site, and a KV cache action under task-quality, latency, cost, and resource constraints. In parallel, background cache-management actions optimize KV cache placement, replication, retrieval, and lifecycle decisions for subsequent requests. We synthesize existing evidence on KV cache reuse, compression, cross-model mapping, distributed storage, and transfer, and discuss the remaining challenges of integrating these capabilities into one system. Across eight typical workload profiles, our workload-level analytical simulation reports TTFT speedups of 1.25$\times$--13.28$\times$ and input-cost benefits of 1.20$\times$--6.16$\times$.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jiaxun Lu, Xiang Zhang, Yunfeng Shao
- 发布：2026-09-09；更新：2026-09-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
