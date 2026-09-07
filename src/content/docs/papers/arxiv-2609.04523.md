---
title: "MaxKernel: Agentic Kernel Generation for TPUs"
description: "Designing and authoring high-performance custom kernels for accelerators is a complex task that requires deep hardware-level expertise."
---

**评分：49/100** · LLM 高效推理 > Runtime 与内存效率 > Kernel 与算子融合

[论文原文](https://arxiv.org/abs/2609.04523) · [PDF](https://arxiv.org/pdf/2609.04523)

## 一句话摘要

Designing and authoring high-performance custom kernels for accelerators is a complex task that requires deep hardware-level expertise.

## 为什么值得关注

待编辑增强。

## 摘要原文

Designing and authoring high-performance custom kernels for accelerators is a complex task that requires deep hardware-level expertise. Large Language Models (LLM) can be leveraged together with real-time compiler feedback to build agentic systems for kernel generation. In this work, we present MaxKernel, a multi-agent system that implements three distinct paradigms for TPU kernel development: (1) a Human-in-the-Loop (HITL) agent for collaborative, step-by-step design; (2) an Autonomous (Auto) agent that executes a fully automated, metric/trace-driven optimization loop; and (3) a Graph-Based Autonomous Search that scales the Auto agent for global exploration of the design space. All three paradigms leverage a shared pool of specialized sub-agents to handle planning, implementation, self-debugging, testing, and hardware profiling. We evaluate MaxKernel on JaxBench, a comprehensive suite of 50 diverse kernel tasks for TPUs, alongside complex, real-world workloads from state-of-the-art open-source models. We demonstrate that MaxKernel consistently generates highly optimized implementations, matching expert hand-tuned baselines and delivering significant performance across the benchmark. Our agent is open-sourced and available https://github.com/AI-Hypercomputer/accelerator-agents/tree/main/MaxKernel.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 13 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kernel generation
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Shangkun Wang, Nina Cai, Charles Hoong, Julian Walker, Gerson Kroiz, George Vanica, Deepak Patil, Andi Gavrilescu, Hassan Sipra, Sethu Sankaran
- 发布：2026-09-07；更新：2026-09-07
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/AI-Hypercomputer/accelerator-agents/tree/main/MaxKernel](https://github.com/AI-Hypercomputer/accelerator-agents/tree/main/MaxKernel)
- 阅读深度：metadata
