---
title: "How to Train Your Little Dragon: Teaching a Small Language Model to Construct and Refine GPU Optimization Scripts"
description: "Compiler transformations interact, making GPU kernel optimization a search for combinations that preserve the computation while improving performance."
---

**评分：39/100** · LLM 高效推理 > Runtime 与内存效率 > Kernel 与算子融合

[论文原文](https://arxiv.org/abs/2610.20980) · [PDF](https://arxiv.org/pdf/2610.20980)

## 一句话摘要

Compiler transformations interact, making GPU kernel optimization a search for combinations that preserve the computation while improving performance.

## 为什么值得关注

待编辑增强。

## 摘要原文

Compiler transformations interact, making GPU kernel optimization a search for combinations that preserve the computation while improving performance. We introduce HOW TO TRAIN YOUR LITTLE DRAGON, a training method that teaches a small language model both to construct complete optimization scripts and to improve existing ones. Instead of ranking candidates or generating kernel code, our model generates optimization scripts. We devise a compact, lossless representation whose deterministic decoding reconstructs the exact compiler trace, preserving its transformation parameters and dependencies. We use a compiler framework TVM MetaSchedule to build training data on 54,116 distinct workloads, and construct 108,594 examples in two training sets: 60,236 teach the model to generate an optimized script from an unoptimized kernel, while 48,358 teach it to produce a better script given the kernel and a somewhat optimized script. Supervised fine-tuning teaches the model to construct and improve optimization scripts from these search-derived examples. We then add reinforcement learning with a shaped reward that combines correctness with measured performance, awarding a latency-based bonus only to numerically correct kernels. We apply this training method to a model with 8 billion parameters. After supervised fine-tuning and reinforcement learning, the model achieves per-attempt correctness of 91.27% for construction and 92.01% for refinement, while reinforcement learning produces faster kernels than supervised training on 88 of 102 construction tasks and 145 of 170 refinement prompts. With only 8B parameters, our LITTLE DRAGON achieves higher per-attempt correctness and better kernel performance than six frontier LLMs: GPT-6 Astra, Opus 5, Kimi-K3, and GLM-5.3 among them, each with hundreds of billions to trillions of parameters, for which task-specific training is unavailable or expensive.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu kernel, kernel optimization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Annabelle Sujun Tang, Wei Tang, Songyao Jiang, Tianhui Li, Shengzhe Xu, Jiin Woo, Kaan Ozkara, Youngsuk Park, Zhen Jia, Hadi Esmaeilzadeh
- 发布：2026-10-14；更新：2026-10-16
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
