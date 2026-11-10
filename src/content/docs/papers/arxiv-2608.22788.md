---
title: "TailSieve: Partial-Rollout-Guided Tail Routing for LLM Rollouts"
description: "Large-scale rollouts have become a core component of modern LLM systems, spanning reinforcement learning (RL) post-training, on-policy distillation, and sampling-heavy evaluation."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2608.22788) · [PDF](https://arxiv.org/pdf/2608.22788)

## 一句话摘要

Large-scale rollouts have become a core component of modern LLM systems, spanning reinforcement learning (RL) post-training, on-policy distillation, and sampling-heavy evaluation.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large-scale rollouts have become a core component of modern LLM systems, spanning reinforcement learning (RL) post-training, on-policy distillation, and sampling-heavy evaluation. Unlike online serving, which typically targets request-level latency and throughput, synchronous rollouts must collect a complete batch before proceeding. A few long-tail generations can therefore dominate an entire rollout step, and uniform routing can slow these generations further by placing them in high-concurrency decoding batches. We present TailSieve, a partial-rollout-guided framework that jointly controls tail routing and replica allocation. Motivated by the observed persistence of prompt-level tail tendencies across policy updates, TailSieve uses partial-rollout completion status as a training-free signal for identifying candidate tail groups. Selected prompts are combined with newly sampled prompts, and all responses are generated from scratch under the current policy. A hierarchical controller uses response-work history and a serving model: a fast inner loop adjusts the number of isolated groups to balance completion times, while a slower outer loop adapts how many replicas serve these groups. The resulting low-concurrency execution also enables route-specialized speculative decoding with MTP or DFlash. Across the evaluated configurations, TailSieve achieves up to $1.67\times$ speedup with routing alone and $2.59\times$ with routing and speculation combined, both over uniform group routing.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Tianqi Xu, Lu Lv, Haoyang Huang, Wenjie Huang, Zhanming Shen, Yuhao Shen, Baolin Zhang, Xinyi Hu, Shuang Ge, Jun Dai, Tianyu Liu, Suorong Yang, Zhikai Li, Ye Bai, Jun Zhang, Lei Chen, Yue Li, Mingchen Wan
- 发布：2026-08-24；更新：2026-11-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
