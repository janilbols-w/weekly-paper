---
title: "Ask, Don't Equip: Question-Driven Coding Agents for Deep Kernel Optimization"
description: "LLM agents for GPU kernel optimization sit at two ends of a structure-freedom tradeoff."
---

**评分：46/100** · LLM 高效推理 > Runtime 与内存效率 > Kernel 与算子融合

[论文原文](https://arxiv.org/abs/2611.03517) · [PDF](https://arxiv.org/pdf/2611.03517)

## 一句话摘要

LLM agents for GPU kernel optimization sit at two ends of a structure-freedom tradeoff.

## 为什么值得关注

待编辑增强。

## 摘要原文

LLM agents for GPU kernel optimization sit at two ends of a structure-freedom tradeoff. Scripted agents fix what the model does at each step, via a learned policy, an optimization menu, or fixed roles, and are sample-efficient where the recipe applies and stall where it does not. Open-ended agents let a self-directed model mutate a population of kernels and pay for the freedom in trials: thousands of evaluations, repeated edits, and wrong candidates. Both respond to hard targets by equipping the agent with more: parsed profiler output, disassembly analysis, retrieval over documentation and libraries, and stores of lessons. We argue that both lack direction, a hypothesis about where the remaining gap is, and that a short question asked at the right moment supplies it without narrowing what the agent may do next. We present KernelSeek, a question-driven agent that makes an existing CUDA kernel faster with no operator-specific knowledge and no faster implementation to imitate: a general-purpose coding agent, a minimal harness that enforces a verifiable goal, and questions at decision points, first from a human, then from a bank the agent applies to itself. On the same task, evaluator, hardware, and week, a tool-rich autonomous agent built in the prevailing style plateaued at 0.50x FlashAttention-3 after 133 model-driven steps; KernelSeek reached 1.13x. It then produced dependency-free FlashAttention forward kernels for Hopper and Blackwell, single CUDA files with no CUTLASS, CuTe, cuBLAS, or cuDNN, correct on all 182 scenarios per architecture and 1.16x FlashAttention-3 and 1.46x FlashAttention-4 (geometric mean). Across 162 human messages and 11.5K agent tool calls, every large gain followed a question that moved the agent to a different layer of the system or rejected a claimed limit, never one that supplied information. We release the kernels, harness, question bank, and all traces.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 20 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 8 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: cuda kernel, gpu kernel, kernel optimization
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Gabriele Oliaro, Jaeseong Lee, Zhaoyuan Su, Sreeram Vennam, Zhihao Jia, Samyam Rajbhandari
- 发布：2026-11-03；更新：2026-11-03
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
