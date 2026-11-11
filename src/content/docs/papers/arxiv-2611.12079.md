---
title: "Correct First, Fast Second: What a Local 7B Code Model Can and Cannot Do for GPU Kernel Optimization"
description: "We study how much the interaction strategy around a fixed, locally hosted 7B-parameter code model (Qwen2.5-Coder-7B-Instruct) affects its ability to replace PyTorch operators with custom CUDA kernels."
---

**评分：54/100** · LLM 高效推理 > Runtime 与内存效率 > Kernel 与算子融合

[论文原文](https://arxiv.org/abs/2611.12079) · [PDF](https://arxiv.org/pdf/2611.12079)

## 一句话摘要

We study how much the interaction strategy around a fixed, locally hosted 7B-parameter code model (Qwen2.5-Coder-7B-Instruct) affects its ability to replace PyTorch operators with custom CUDA kernels.

## 为什么值得关注

待编辑增强。

## 摘要原文

We study how much the interaction strategy around a fixed, locally hosted 7B-parameter code model (Qwen2.5-Coder-7B-Instruct) affects its ability to replace PyTorch operators with custom CUDA kernels. On 30 KernelBench tasks (levels 1-3, first 10 each, evaluated on a V100), we compare four regimes of increasing structure: zero-shot prompting, profiling-guided prompting, iterative refinement on execution feedback, and a multi-agent loop (analysis, retrieval, generation, evaluation, feedback triage) in which the same model fills four roles around a non-LLM evaluator. Three findings stand out. (1) Correctness, not speed, is the binding constraint: even correct generated kernels average 0.97-0.99x the speed of eager PyTorch, because a 7B model cannot out-write cuBLAS/cuDNN on dense GEMM and convolution; the only real wins are fused memory-bound epilogues. (2) The best strategy depends on difficulty: profiling-guided prompting is strongest overall (43% correct, 27% faster than baseline), but the agent loop is the only method that solves any level-2 fusion problem (3/10 vs. 0/10 for all others). (3) Naive agentic scaffolding is actively harmful: our first agent scored 3% correct, below zero-shot's 30%, and the decisive repairs were matching the agent's ambition to the model's competence and spending compute on best-of-n sampling under a real execution oracle (3% to 33% correct from n=1 to n=8), not on more reasoning steps.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 22 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu kernel, kernel optimization
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Jui-Chien Tsou, Po-Yi Wu
- 发布：2026-11-10；更新：2026-11-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
