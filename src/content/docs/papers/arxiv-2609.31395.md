---
title: "ActKV: Efficient LLM Agents through Action-Guided KV Cache Management"
description: "Agentic LLM inference accumulates long KV caches across iterative observation-reasoning-action loops, imposing substantial memory overhead and limiting serving throughput."
---

**评分：45/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2609.31395) · [PDF](https://arxiv.org/pdf/2609.31395)

## 一句话摘要

Agentic LLM inference accumulates long KV caches across iterative observation-reasoning-action loops, imposing substantial memory overhead and limiting serving throughput.

## 为什么值得关注

待编辑增强。

## 摘要原文

Agentic LLM inference accumulates long KV caches across iterative observation-reasoning-action loops, imposing substantial memory overhead and limiting serving throughput. Existing compression methods emphasize overall output quality, overlooking the asymmetric importance of actions in driving task progress. Our key idea is to establish a compression criterion that values KV entries by their contribution to action generation and prioritizes action quality. However, iterative execution, dynamic memory demands, and scattered action-critical entries pose challenges to eviction policies, budget allocation, and paged memory integration. To this end, we propose ActKV, the first KV cache compression framework tailored for agentic LLM inference. (i) Action-oriented KV cache eviction exploits stable action access patterns to retain entries critical to future actions, supporting reliable task progress under compression. (ii) Confidence-driven adaptive budget allocation uses LLM's intrinsic confidence to adapt the budget to evolving action-critical memory demands. (iii) Page-aware compression management standardizes compression into three primitives with customized kernels, realizing practical throughput gains. On long-trace tasks, ActKV retains an average of 98.53% of FullKV's accuracy with only 25.98% of its peak KV cache memory. It also achieves 3.97 times and 3.58 times FullKV's token and task throughput, delivering state-of-the-art performance.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 5 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Zihan Wang, Cheng Tang, Lei Gong, Chao Wang, Wenqi Lou, Teng Wang, Xuehai Zhou
- 发布：2026-09-28；更新：2026-09-28
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
