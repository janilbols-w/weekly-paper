---
title: "LIBRA: Runtime Co-Tuning of Batch Size and Parallelism for Time-Efficient LLM Training"
description: "Training large language models (LLMs) requires choosing both a batch size and a parallel configuration."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2611.32008) · [PDF](https://arxiv.org/pdf/2611.32008)

## 一句话摘要

Training large language models (LLMs) requires choosing both a batch size and a parallel configuration.

## 为什么值得关注

待编辑增强。

## 摘要原文

Training large language models (LLMs) requires choosing both a batch size and a parallel configuration. Existing systems make these decisions in isolation, tuning parallelism for throughput and batch size for convergence, but neither objective alone determines training efficiency. We present LIBRA, a lightweight runtime framework that co-tunes batch size and parallel configuration to minimize end-to-end time. LIBRA treats throughput and convergence as two noisy objectives and searches their joint space using parallel noisy expected hypervolume improvement (qNEHVI). To make this runtime search efficient, we propose hierarchical pruning, which removes infeasible and low-throughput parallel configurations through system-level performance estimation and then narrows batch-size candidates through critical-batch-size-aware convergence monitoring. We further design acquisition-guided parallel evaluation (AGPE), which evaluates surviving candidates concurrently across GPU groups in order of their acquisition values. On clusters of up to 256 GPUs, LIBRA reduces time-to-convergence by 31.1% on average over state-of-the-art methods, while runtime tuning accounts for only 0.3-3.5% of overall time.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Shengkai Lyu, Hairui Zhao, Daran Sun, Yida Gu, Xingchen Liu, YueYuan Zhou, Zheng Wei, Guangming Tan, Dingwen Tao
- 发布：2026-11-24；更新：2026-11-25
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
