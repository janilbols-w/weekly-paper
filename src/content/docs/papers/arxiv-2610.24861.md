---
title: "FlowMaker: From Tasks to Cost-Efficient Generative AI Workflow Deployments"
description: "Generative AI workflows execute user tasks by composing sequences of LLM calls, where each call performs a sub-task (e.g., summarization or translation), forming a workflow."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.24861) · [PDF](https://arxiv.org/pdf/2610.24861)

## 一句话摘要

Generative AI workflows execute user tasks by composing sequences of LLM calls, where each call performs a sub-task (e.g., summarization or translation), forming a workflow.

## 为什么值得关注

待编辑增强。

## 摘要原文

Generative AI workflows execute user tasks by composing sequences of LLM calls, where each call performs a sub-task (e.g., summarization or translation), forming a workflow. Executing such workflows requires decisions over workflow structure, model assignments, and deployment configurations, which jointly determine latency, cost, and accuracy under dynamic workloads and resource constraints. Existing systems optimize these decisions in isolation or fix them early, leading to suboptimal cost and goodput. We make two key observations. First, efficient serving requires jointly exploring all combinations of workflows, model choices, and deployment configurations under dynamic cluster state. Second, reuse of deployed LLMs is critical for reducing cost, but must be performed on-the-fly, as reuse depends on current load and resource availability. Together, these make selecting a workflow-variant-a combination of workflow, models, and deployment configuration-a time-critical problem. We present FlowMaker, which exposes a task-level interface and selects workflow-variants on behalf of users. To realize this, we design a constraint-guided load-aware pruning algorithm for fast, on-the-fly decisions. FlowMaker improves goodput by up to 10.14$\times$ and reduces cost by up to 2.77$\times$ compared to state-of-the-art baselines, including Murakkab.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Dimitrios Liakopoulos, Prasoon Sinha, Neeraja J. Yadwadkar
- 发布：2026-10-20；更新：2026-10-20
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
