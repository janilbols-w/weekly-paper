---
title: "Exploring the Role of LLMs in HPC Programming: A Survey"
description: "Large Language Models (LLMs) are emerging as promising assistants in High-Performance Computing (HPC), where programming remains complex and expertise-intensive."
---

**评分：40/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2608.26110) · [PDF](https://arxiv.org/pdf/2608.26110)

## 一句话摘要

Large Language Models (LLMs) are emerging as promising assistants in High-Performance Computing (HPC), where programming remains complex and expertise-intensive.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large Language Models (LLMs) are emerging as promising assistants in High-Performance Computing (HPC), where programming remains complex and expertise-intensive. This survey systematically reviews their application across five categories: code generation, parallelization and optimization, frameworks and architectures, evaluation and benchmarking, and broader challenges. The analysis highlights both opportunities and limitations: while general-purpose LLMs perform reasonably well on serial and OpenMP-like tasks, they fall short in distributed paradigms such as MPI, where correctness and scalability are critical. Domain-specialized models (e.g., HPC-Coder, HPC-GPT, chatHPC) achieve higher accuracy through fine-tuning, curated datasets, and retrieval-augmented generation (RAG), yet their scope remains narrow and their evaluations largely limited to benchmarks or micro-kernels. The broader picture is one of dual potential and fragility: LLMs can lower barriers to entry, accelerate prototyping, and support code modernization, but they remain brittle under production-level requirements where correctness, performance portability, and scaling cannot be compromised. We conclude that LLMs are unlikely to replace HPC experts in the near term but are positioned to become powerful collaborators in the software development pipeline. Their effective deployment will require richer datasets, integration with performance analysis and schedulers, rigorous evaluation frameworks, and governance structures that ensure transparency and trust. The convergence of AI and HPC should therefore be understood as a long-term, co-evolutionary process, where each advance uncovers new challenges and opportunities for reshaping scientific software development.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Strahinja Ljaljevic, Josep Jorba, Sergio Iserte
- 发布：2026-08-28；更新：2026-08-28
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
