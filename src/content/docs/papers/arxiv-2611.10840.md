---
title: "Simple Test-Time Refinement for Plot-to-Code Generation via Visual-Code Diagnostics"
description: "Plot-to-code generation has been greatly advanced by recent multimodal large language models (MLLMs)."
---

**评分：42/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2611.10840) · [PDF](https://arxiv.org/pdf/2611.10840)

## 一句话摘要

Plot-to-code generation has been greatly advanced by recent multimodal large language models (MLLMs).

## 为什么值得关注

待编辑增强。

## 摘要原文

Plot-to-code generation has been greatly advanced by recent multimodal large language models (MLLMs). However, existing studies mainly focus on one-pass generation or iterative sampling guided by verifier-based filtering, which does not align with the typical human programming workflow of generate first, then iteratively error-location and fix. This naturally motivates a test-time refinement paradigm for plot-to-code generation. In this work, we present the first study on plot-to-code generation via iterative test-time refinement. We propose a Visual-Code Diagnostics framework that enables refinement through visual feedback from source code. Specifically, we first categorize generation errors into four coarse-grained types, and then train lightweight discriminators to recognize and localize these errors based on the rendered visual outputs and corresponding code. Unlike traditional compiler- or debugger-based verification, our approach performs iterative refinement guided by one diagnostics system, enabling more effective semantic and visual correction during test time. Extensive experiments demonstrate that our method consistently improves generation quality across diverse generators and significantly outperforms strong test-time scaling baselines.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Peiming Guo, Jinpeng Huang, Yangbin Sun, Gaoxiong Cao, Ensheng Shi, Yuchi Ma, Yu Zhang, Meishan Zhang, Baotian Hu, Min Zhang
- 发布：2026-11-10；更新：2026-11-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
