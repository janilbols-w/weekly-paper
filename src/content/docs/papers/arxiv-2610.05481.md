---
title: "CodeForge-MA: Execution-Verified Multi-Agent Learning with Language-Conditioned LoRA for Multilingual Code Generation"
description: "Large language models for code generation often fail on execution, multilingual coverage, and contamination control, especially under frozen backbone constraints."
---

**评分：40/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2610.05481) · [PDF](https://arxiv.org/pdf/2610.05481)

## 一句话摘要

Large language models for code generation often fail on execution, multilingual coverage, and contamination control, especially under frozen backbone constraints.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models for code generation often fail on execution, multilingual coverage, and contamination control, especially under frozen backbone constraints. We present CodeForge-MA, a unified framework that improves code synthesis through a multi-agent data forge, execution verified reinforced instruction tuning, and a language conditioned mixture of LoRA adapters. Four specialized agents, Composer, Reviewer, Executor, and Curator, iteratively refine instruction code pairs, validate them with tests, and filter duplicates and benchmark leakage. During training, we combine masked supervised fine tuning with a test driven reinforcement objective to align generations with executable correctness. For the larger model, we use sparse expert routing over low rank adapters to improve cross language transfer while keeping the base model unchanged at inference. Experiments show that joint data, objective, and adapter design yields robust gains across programming languages.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zhizhou Gu, Xianting Wu, Siyu Gu, Tian Zhang, Kejian Tong
- 发布：2026-10-06；更新：2026-10-06
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
