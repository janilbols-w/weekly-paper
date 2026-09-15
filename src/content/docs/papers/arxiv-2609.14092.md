---
title: "NeuroFlex: Lossless Element-Level ANN-SNN Co-Execution for Efficient Sparse Inference"
description: "Sparse DNN accelerators specialize in ANN or SNN execution, leaving energy or latency on the table when workload characteristics vary within a layer."
---

**评分：56/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.14092) · [PDF](https://arxiv.org/pdf/2609.14092)

## 一句话摘要

Sparse DNN accelerators specialize in ANN or SNN execution, leaving energy or latency on the table when workload characteristics vary within a layer.

## 为什么值得关注

待编辑增强。

## 摘要原文

Sparse DNN accelerators specialize in ANN or SNN execution, leaving energy or latency on the table when workload characteristics vary within a layer. Hybrid accelerator designs that switch modes at layer or tile granularity suffer from low PE utilization since one core type idles whenever the other is active. NeuroFlex is the first accelerator to assign every output element independently to ANN or SNN execution mode with zero accuracy loss. We extend integer-exact ANN-SNN equivalence from layers to individual output elements, thereby enabling mode switching with no conversion error. An offline cost-guided scheduler scores each element by its marginal energy-delay trade-off and packs work across PEs, achieving 97-99% PE utilization compared to 40-45% for layer-wise hybrids. NeuroFlex reduces EDP by 57-67% over a strong ANN-only baseline and delivers up to 2.5x speedup over a dual-sparse SNN-only baseline. Our cost-guided scheduler improves throughput by 16-19% over random element assignment across vision, language, and transformer workloads.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 20 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: sparse inference
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Varun Manjunath, Pranav Ramesh, Gopalakrishnan Srinivasan
- 发布：2026-09-15；更新：2026-09-15
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
