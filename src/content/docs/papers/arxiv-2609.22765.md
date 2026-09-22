---
title: "Quality over Quantity: Diversity-Aware Data Selection for Efficient Verilog Code Generation"
description: "Large Language Models (LLMs) have shown remarkable potential in Verilog code generation, yet existing datasets contain con siderable noise and redundancy."
---

**评分：48/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2609.22765) · [PDF](https://arxiv.org/pdf/2609.22765)

## 一句话摘要

Large Language Models (LLMs) have shown remarkable potential in Verilog code generation, yet existing datasets contain con siderable noise and redundancy.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large Language Models (LLMs) have shown remarkable potential in Verilog code generation, yet existing datasets contain con siderable noise and redundancy. Prior data selection methods address only isolated quality aspects, neglect the global diversity of the training set, and cannot capture Verilog-specific structural semantics. To bridge this gap, we propose VeriSelector, the first data selection framework for Verilog code generation that jointly optimizes quality and diversity. We formulate the selec tion problem as a constrained bi-objective subset selection problem and solve it via a three-stage approximation. For quality, a multi-granularity pipeline first verifies functional correctness through testbench simulation and then filters misaligned samples via Instruction-Following Difficulty (IFD) scoring. For diversity, 109-dimensional Verilog-specific structural features (AST, CFG, and Netlist) are fused with textual embeddings for clustering-based diversity modeling. A proportional adaptive sampling strat egy then allocates per-cluster quotas guided by IFD ranks, with a provable distribution preservation guarantee. Experiments on three LLMs and three benchmarks show that VeriSelector outperforms full-dataset training and state-of-the-art baselines us ing only 20%-25% of the data, achieving Performance Retention Rates above 118% and reducing training time by over 80%. Notably, VeriSelector improves average Pass@1 by 18.49%-29.43% over full-dataset training and by 1.36%-7.95% over the best-performing baseline across all evaluated models.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 15 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yiheng Shen, Wei Zheng, Xiao Wei, Hao Shen, Xiang Chen, Guang Yang
- 发布：2026-09-22；更新：2026-09-22
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
