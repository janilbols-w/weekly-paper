---
title: "Gen-TAS: A Generative AI-Aided Hardware-Software Task Allocation Framework for FPGA-GPP Heterogeneous Systems"
description: "FPGA-GPP heterogeneous systems combine software flexibility with the performance and energy efficiency of reconfigurable hardware."
---

**评分：45/100** · AI 基础设施 > 训练与数据中心基础设施 > 能耗、成本与散热

[论文原文](https://arxiv.org/abs/2608.28160) · [PDF](https://arxiv.org/pdf/2608.28160)

## 一句话摘要

FPGA-GPP heterogeneous systems combine software flexibility with the performance and energy efficiency of reconfigurable hardware.

## 为什么值得关注

待编辑增强。

## 摘要原文

FPGA-GPP heterogeneous systems combine software flexibility with the performance and energy efficiency of reconfigurable hardware. However, determining which application tasks should execute on the GPP or FPGA requires extensive expertise and design-space exploration, particularly when user objectives vary across latency, communication, resource utilisation, and power. This paper proposes Gen-TAS, a knowledge-grounded LLM framework for user-specific FPGA-GPP task allocation. By combining task-graph analysis with RAG, Gen-TAS grounds LLM reasoning in historical implementation knowledge and generates multiple explainable strategies tailored to the specified objectives. Human-in-the-loop selection and a deterministic backend connect LLM-generated decisions to reproducible FPGA SoC implementations. Experiments on CNN and SDR workloads across multiple LLMs demonstrate stable, requirement-driven allocation. Under latency-oriented objectives, implementations following the selected strategies achieve speedups of up to 2.45$\times$ and 92.53$\times$, respectively, relative to the corresponding all-GPP baselines while other objectives select strategies that trade some acceleration performance for FPGA-GPP communication, resource utilisation, or FPGA power.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 11 |
| reproducibility | 3 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: energy efficiency
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Mary Kong, Yuqin Zhao, Semih Vazgecen, Cristian Sestito, Themis Prodromakis
- 发布：2026-08-31；更新：2026-08-31
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
