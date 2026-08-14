---
title: "StitchCUDA: An Automated Multi-Agents End-to-End GPU Programing Framework with Rubric-based Agentic Reinforcement Learning"
description: "StitchCUDA 以 Planner、Coder 和 Verifier 协作生成端到端 GPU 程序，并用真实执行反馈与 rubric 奖励训练 Coder，覆盖主机侧设置、内核融合和 cuBLAS epilogue 等优化。"
---

**评分：55/100** · LLM 高效推理 > Runtime 与内存效率 > Kernel 与算子融合

[论文原文](https://arxiv.org/abs/2603.02637) · [PDF](https://arxiv.org/pdf/2603.02637)

## 一句话摘要

StitchCUDA 以 Planner、Coder 和 Verifier 协作生成端到端 GPU 程序，并用真实执行反馈与 rubric 奖励训练 Coder，覆盖主机侧设置、内核融合和 cuBLAS epilogue 等优化。

## 为什么值得关注

该工作把自动优化从单个 GPU 内核扩展到主机代码与内核协同的完整程序，并把正确性检查、Nsys/NCU 分析纳入闭环，更接近实际 GPU 应用的调优流程。

## 摘要原文

Modern machine learning (ML) workloads increasingly rely on GPUs, yet achieving high end-to-end performance remains challenging due to dependencies on both GPU kernel efficiency and host-side settings. Although LLM-based methods show promise on automated GPU kernel generation, prior works mainly focus on single-kernel optimization and do not extend to end-to-end programs, hindering practical deployment. To address the challenge, in this work, we propose StitchCUDA, a multi-agent framework for end-to-end GPU program generation, with three specialized agents: a Planner to orchestrate whole system design, a Coder dedicated to implementing it step-by-step, and a Verifier for correctness check and performance profiling using Nsys/NCU. To fundamentally improve the Coder's ability in end-to-end GPU programming, StitchCUDA integrates rubric-based agentic reinforcement learning over two atomic skills, task-to-code generation and feedback-driven code optimization, with combined rubric reward and rule-based reward from real executions. Therefore, the Coder learns how to implement advanced CUDA programming techniques (e.g., custom kernel fusion, cublas epilogue), and we also effectively prevent Coder's reward hacking (e.g., just copy PyTorch code or hardcoding output) during benchmarking. Experiments on KernelBench show that StitchCUDA achieves nearly 100% success rate on end-to-end GPU programming tasks, with 1.72x better speedup over the multi-agent baseline and 2.73x than the RL model baselines. Code of the STITCHCUDA framework is avalaible at https://github.com/UMN-APEX-Lab/StitchCUDA.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 13 |
| practical impact | 10 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu kernel, kernel generation, kernel optimization
- quantitative claim detected
- code/artifact link detected
- 限制：接近 100% 的成功率和加速结果均基于 KernelBench；基准对真实应用依赖、长时间运行稳定性及跨硬件迁移的代表性，摘要中尚无充分证据。

## 元数据

- 作者：Shiyang Li, Zijian Zhang, Winson Chen, Yuebo Luo, Mingyi Hong, Caiwen Ding
- 发布：2026-08-11；更新：2026-08-11
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/UMN-APEX-Lab/StitchCUDA](https://github.com/UMN-APEX-Lab/StitchCUDA)
- 阅读深度：abstract
