---
title: "AMDKernelVault: Large-Scale Datasets and Agentic Training for AMD GPU Kernel Optimization"
description: "We introduce AMDKernelVault, an open HIP and Triton kernel corpus and training framework for recent AMD CDNA GPUs."
---

**评分：56/100** · LLM 高效推理 > Runtime 与内存效率 > Kernel 与算子融合

[论文原文](https://arxiv.org/abs/2609.12471) · [PDF](https://arxiv.org/pdf/2609.12471)

## 一句话摘要

We introduce AMDKernelVault, an open HIP and Triton kernel corpus and training framework for recent AMD CDNA GPUs.

## 为什么值得关注

待编辑增强。

## 摘要原文

We introduce AMDKernelVault, an open HIP and Triton kernel corpus and training framework for recent AMD CDNA GPUs. Existing LLM-based kernel agents are largely CUDA/NVIDIA-centric and often depend on repeated frontier-LLM calls for generation, reflection, and optimization. To address this gap, we develop HIPKernelGen and TritonKernelGen, agent-driven pipelines that transform PyTorch references into HIP or Triton kernels, compile and validate candidates under ROCm, and latency-profile them on AMD hardware. The corpus contains 62,153 execution-verified HIP kernel samples, 2,377 production-grounded ROCm Libraries QA entries, and 39,893 Triton kernels. We further train Qwen3-8B with supervised fine-tuning and execution-aware reinforcement learning as a demonstration of the corpus's utility. Under fixed evaluation budgets, it achieves the highest correctness among the compared models on PyTorch-to-HIP (34.0% Pass@1), TritonBench-G (33.2% Corr@3), and ROCmBench (41.94% Corr@3), but does not uniformly lead compilation or speed metrics. The corpus and documentation are available at https://huggingface.co/datasets/amd/AIG-Datasets, and the associated training and kernel-generation code is available at https://github.com/AMD-AGI/hip_kernel_llm_lab.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 24 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu kernel, kernel optimization, triton kernel
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Ji Liu, Saptarshi Majumder, Yiqing Huang, Wenwen Ouyang, Umang Pandey, Zeping Li, Chushi Chen, Zihao An, Puyuan Yang, Zekai Li, Sina Rafati, Ziqiong Liu, Pratik Prabhanjan Brahma, Dong Li, Zicheng Liu, Sharon Zhou, Emad Barsoum
- 发布：2026-09-14；更新：2026-09-14
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/AMD-AGI/hip_kernel_llm_lab](https://github.com/AMD-AGI/hip_kernel_llm_lab)
- 阅读深度：metadata
