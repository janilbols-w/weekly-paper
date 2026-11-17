---
title: "DRTriton: Large-Scale Synthetic Data Driven Reinforcement Learning for Triton Kernel Generation"
description: "Developing efficient CUDA kernels is a fundamental yet challenging task in the generative AI industry."
---

**评分：47/100** · LLM 高效推理 > Runtime 与内存效率 > Kernel 与算子融合

[论文原文](https://arxiv.org/abs/2603.21465) · [PDF](https://arxiv.org/pdf/2603.21465)

## 一句话摘要

Developing efficient CUDA kernels is a fundamental yet challenging task in the generative AI industry.

## 为什么值得关注

待编辑增强。

## 摘要原文

Developing efficient CUDA kernels is a fundamental yet challenging task in the generative AI industry. Recent research leverages Large Language Models (LLMs) to automatically convert PyTorch reference implementations to CUDA kernels, significantly reducing engineering effort. State-of-the-art LLMs, such as GPT-5.2 and Claude-Sonnet-4.5, still struggle with this task. To address this challenge, we propose DRTriton, a scalable learning framework for training LLMs to convert PyTorch programs into highly optimized Triton kernels, which are then compiled to CUDA kernels at runtime. DRTriton consists of three key components: (i) a data synthetic algorithm CSP-DAG that guarantees full coverage and unbiased uniform sampling over the operator space with controlled difficulty; (ii) a curriculum RL framework with decoupled rewards that jointly optimizes conversion success rate and execution speed; and (iii) a test-time search algorithm that further improves the execution speed of the generated Triton kernels. With a warmup stage of SFT on limited PyTorch-Triton pairs curated using existing LLMs, DRTriton trained by RL on synthesized PyTorch programs generalizes effectively to real-world CUDA kernels that are challenging even for human experts. Experimental results show that DRTriton-7B achieves speedup over PyTorch on 92% of KernelBench Level 2 tasks, compared to 23% for GPT-5.2 and 19% for Claude-Sonnet-4.5.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 22 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kernel generation, triton kernel
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Siqi Guo, Ming Lin, Tianbao Yang
- 发布：2026-11-16；更新：2026-11-16
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
