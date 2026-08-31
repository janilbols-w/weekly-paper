---
title: "Gen-TAS: A Generative AI-Aided Hardware-Software Task Allocation Framework for FPGA-GPP Heterogeneous Systems"
description: "Gen-TAS 将任务图分析、基于历史实现知识的 RAG、人工选择和确定性后端串成 FPGA-GPP 任务分配流程，按时延、通信、资源利用或功耗目标生成可解释方案。摘要报告，在 CNN 与 SDR 负载上，时延导向方案相对各自全 GPP 基线最高加速 2.45 倍和 92.53 倍。"
---

**评分：45/100** · AI 基础设施 > 训练与数据中心基础设施 > 能耗、成本与散热

[论文原文](https://arxiv.org/abs/2608.28160) · [PDF](https://arxiv.org/pdf/2608.28160)

## 一句话摘要

Gen-TAS 将任务图分析、基于历史实现知识的 RAG、人工选择和确定性后端串成 FPGA-GPP 任务分配流程，按时延、通信、资源利用或功耗目标生成可解释方案。摘要报告，在 CNN 与 SDR 负载上，时延导向方案相对各自全 GPP 基线最高加速 2.45 倍和 92.53 倍。

## 为什么值得关注

它把异构部署中的任务划分从专家驱动的设计空间探索转为有知识约束的辅助决策，为边缘与加速器 AI 系统按目标选择硬件映射提供了一条可落地路径。

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
- 限制：证据仅来自摘要所述 CNN、SDR 工作负载和 FPGA SoC 实现；两个加速倍数对应不同任务，不能直接横向比较或外推。摘要未说明平台覆盖、基线调优、搜索成本及人工选择敏感性。

## 元数据

- 作者：Mary Kong, Yuqin Zhao, Semih Vazgecen, Cristian Sestito, Themis Prodromakis
- 发布：2026-08-31；更新：2026-08-31
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：abstract
