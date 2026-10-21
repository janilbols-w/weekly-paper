---
title: "Compaction-Aware Reinforcement Learning For Ascend Triton Kernel Generation"
description: "Automatically generating high-performance kernels with LLM-based agents promises substantial gains in development efficiency, but two obstacles remain."
---

**评分：50/100** · LLM 高效推理 > Runtime 与内存效率 > Kernel 与算子融合

[论文原文](https://arxiv.org/abs/2610.23950) · [PDF](https://arxiv.org/pdf/2610.23950)

## 一句话摘要

Automatically generating high-performance kernels with LLM-based agents promises substantial gains in development efficiency, but two obstacles remain.

## 为什么值得关注

待编辑增强。

## 摘要原文

Automatically generating high-performance kernels with LLM-based agents promises substantial gains in development efficiency, but two obstacles remain. First, while increasing multi-turn interaction with execution environments is crucial for refining generation quality, continuous context accumulation rapidly exceeds the model's effective context window. Second, training long-horizon tasks via GRPO inherently incurs sparse rewards due to its reliance on terminal outcome evaluation, severely hindering step-level credit assignment; To address these obstacles, we propose ATRL (Ascend Triton Reinforcement Learning), a post-training method that refines GRPO into a compaction-aware, segment-level objective for long-horizon kernel generation. We also design a lightweight agent harness providing cascaded compilation, correctness, and profiling feedback, alongside an Ascend-specific knowledge base injected during agentic RL training and evaluation to compensate for the base model's missing platform expertise. Evaluations on NPUKernelBench and KernelBench, both executed on Ascend hardware, show that ATRL consistently surpasses all baselines, including GRPO, in both correctness and speedup.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 22 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kernel generation, triton kernel
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Chuansai Zhou, Yanlin Liu, Bingning Huang, Shidi Xi, Chao Huang, Boxing Chen, Mingming Zhu, Guanghuan Fang, Ben Feng, Zongzuo Wang
- 发布：2026-10-20；更新：2026-10-21
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
