---
title: "CUDA-Harness: Harnessing Agentic CUDA Kernel Generation and Optimization from Natural Language"
description: "Developing high-performance CUDA kernels demands specialized knowledge in algorithm implementation, correctness validation, and hardware-aware parallel optimization, creating a substantial expertise barrier and making generating CUDA kernels directly from natural language (Text2CUDA) essential."
---

**评分：48/100** · LLM 高效推理 > Runtime 与内存效率 > Kernel 与算子融合

[论文原文](https://arxiv.org/abs/2609.00058) · [PDF](https://arxiv.org/pdf/2609.00058)

## 一句话摘要

Developing high-performance CUDA kernels demands specialized knowledge in algorithm implementation, correctness validation, and hardware-aware parallel optimization, creating a substantial expertise barrier and making generating CUDA kernels directly from natural language (Text2CUDA) essential.

## 为什么值得关注

待编辑增强。

## 摘要原文

Developing high-performance CUDA kernels demands specialized knowledge in algorithm implementation, correctness validation, and hardware-aware parallel optimization, creating a substantial expertise barrier and making generating CUDA kernels directly from natural language (Text2CUDA) essential. Meanwhile, the general-purpose code generation capability of Large Language Models (LLMs) prompts a series of works exploring LLM-based CUDA kernel generation. They mainly focus on transpilation from high-level frameworks such as PyTorch to CUDA (Torch2CUDA) rather than Text2CUDA, where models must understand the high-level input semantics and handle low-level kernel implementation and validation. Additionally, these methods are vulnerable to reward hacking due to reliance on predefined test inputs. In this paper, we propose CUDA-Harness, a framework for harnessing agentic CUDA kernel generation and optimization from natural language. Specifically, we introduce Intermediate-Structured Generation to connect high-level semantic understanding with low-level kernel generation. To dilute reward hacking in Text2CUDA, we construct Synthesis-Based Verification to provide isolated test data and progressive validation. Furthermore, we propose Feedback-Adaptive Evolution, a kernel evolution strategy that prioritizes correctness while optimizing performance. Finally, through extensive experiments, we demonstrate the effectiveness of CUDA-Harness, with further evaluations illustrating generalization across LLMs, hardware platforms, and to C-to-CUDA transpilation.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 22 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: cuda kernel, kernel generation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Qi Fan, An Zou, Yehan Ma
- 发布：2026-09-02；更新：2026-09-02
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
