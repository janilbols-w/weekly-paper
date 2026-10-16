---
title: "PrefixFlow: Training-Time KV Caching for Schedule-Level Prefix Reuse in LLM RL Training"
description: "In reinforcement learning (RL) post-training, one prompt fans out into $N$ trajectories, yet standard trainers replay the shared prefix's forward and backward pass $N$ times; in long-context retrieval-augmented generation (RAG) and multimodal workloads, this repetition dominates training compute."
---

**评分：40/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2606.01143) · [PDF](https://arxiv.org/pdf/2606.01143)

## 一句话摘要

In reinforcement learning (RL) post-training, one prompt fans out into $N$ trajectories, yet standard trainers replay the shared prefix's forward and backward pass $N$ times; in long-context retrieval-augmented generation (RAG) and multimodal workloads, this repetition dominates training compute.

## 为什么值得关注

待编辑增强。

## 摘要原文

In reinforcement learning (RL) post-training, one prompt fans out into $N$ trajectories, yet standard trainers replay the shared prefix's forward and backward pass $N$ times; in long-context retrieval-augmented generation (RAG) and multimodal workloads, this repetition dominates training compute. Existing designs reuse the prefix within one computation graph (a packed sequence, fused kernel, or tree traversal); under the trainer's memory limits and parallelism, their compute savings do not reliably become shorter steps. We present PrefixFlow, which takes the prefix out of that graph and into the training schedule through a training-time KV cache: Phase A runs one prefix forward and caches its keys and values ($K/V$); Phase B trains suffixes as ordinary microbatches that read only $K/V$ and write back only their gradients ($gK/gV$); Phase C runs one delayed prefix backward on the accumulated $gK/gV$. Memory and parallelism then become manageable: dormant prefix activations are offloaded during Phase B to free high-bandwidth memory (HBM) for suffixes, and context, pipeline, and data parallelism each schedule the phases through a local rule while tensor and expert parallelism need no change, so saved compute becomes shorter steps under any microbatch split. On dense models, and on mixture-of-experts (MoE) models under Rollout Routing Replay, PrefixFlow matches full-sequence training within bfloat16 (BF16) tolerance. Against an identically configured baseline, it speeds up end-to-end verl RL training on a long-prefix RAG workload by $1.90\times$ ($6.1\times$ on the actor update). In controlled sweeps, actor-side speedup grows with prefix ratio and group size, reaching $4.4\times$ at an 83% prefix ratio, while suffix-dominated splits gain little; offloading dormant prefix activations lowers Phase-B peak HBM by up to 59% and extends trainable sequences by $1.66\times$.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Pengbo Li, Feiyuan Zhang, Guangming Sheng, Guangxin He, Di Chai, Ziniu Li, Taiqiang Wu, Han Tian, Wenyu Mao, Binhang Yuan, Kai Chen
- 发布：2026-10-16；更新：2026-10-16
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
