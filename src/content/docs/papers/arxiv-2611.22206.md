---
title: "TAILROLL: Tail-Aware Rollout Acceleration for RL-Based LLM Post-Training"
description: "RL post-training of large language models (LLMs) is bottlenecked by rollout: heavy-tailed responses leave engines idle as each step waits for the longest response."
---

**评分：39/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2611.22206) · [PDF](https://arxiv.org/pdf/2611.22206)

## 一句话摘要

RL post-training of large language models (LLMs) is bottlenecked by rollout: heavy-tailed responses leave engines idle as each step waits for the longest response.

## 为什么值得关注

待编辑增强。

## 摘要原文

RL post-training of large language models (LLMs) is bottlenecked by rollout: heavy-tailed responses leave engines idle as each step waits for the longest response. Asynchronous training masks, but does not eliminate, idle time. We distinguish imbalance waste (uneven placement and decode contention) from straggler waste (waiting for the longest response). Tail length, not average load, often sets the step bound. We propose TAILROLL, an online scheduler integrated into an open-source RL framework. It combines stateless in-flight migration and sufficiency-gated termination. Migration moves decoding requests between engines at chunk boundaries and resumes them with one re-prefill under a freeness-based, cost-aware tail-balancing policy. Termination stops a response when its GRPO group has enough completed samples for advantage estimation, masking its partial output from the training loss. Across ten configurations, TAILROLL reduces rollout bubble ratio by 21% to 74% and cross-engine KV-cache imbalance by 44% to 79%. In end-to-end RL training, it cuts rollout time by 24% to 34%, full step time by 21% to 22% on long-CoT RL, and p95 request latency by 28% to 37%, while raising generation throughput by up to 33% with comparable or higher final reward.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv-cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Niloofar Gholipour, Marcos Assuncao, Timothy Yu, Gursimran Singh, Rajkumar Buyya, Julien Gascon-Samson, Zhenan Fan, Yong Zhang
- 发布：2026-11-17；更新：2026-11-18
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
