---
title: "Concertina: Data-Centric Adaptive Pipeline Parallelism for Efficient Heterogeneous Long-Context LLM Training"
description: "Long context training is crucial for extending LLM context windows."
---

**评分：50/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2509.21275) · [PDF](https://arxiv.org/pdf/2509.21275)

## 一句话摘要

Long context training is crucial for extending LLM context windows.

## 为什么值得关注

待编辑增强。

## 摘要原文

Long context training is crucial for extending LLM context windows. Existing schemes, such as sequence parallelism, incur substantial communication overhead. Pipeline parallelism (PP) reduces this cost, but its effectiveness hinges on partitioning granularity. Batch-level PP employing sequence packing exhibits high memory consumption in long-context scenarios, whereas token-level PP splitting sequences into slices alleviates memory overhead but may introduce performance degradation. Moreover, the skewed sequence-length distribution in real-world datasets defeats any monolithic, static choice of PP granularity. In this paper, we propose \textit{Dynamic Pipeline Parallelism} (DPP), which transforms PP granularity from a static design choice into a workload-adaptive optimization space over packed, split, and hybrid chunks. DPP further introduces a new coupling between heterogeneous pipeline scheduling and gradient checkpointing. To solve this coupling, \name co-optimizes dynamic chunk scheduling with \textit{Stage-Aware Chunk-Level Adaptive Checkpointing}. Comprehensive experiments demonstrate that \name achieves up to 1.69\texttimes\ speedup over FlexSP and up to 1.40\texttimes\ over MEPipe. The source code is available at https://github.com/wsjdsg/InfiniPipe-code.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 11 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpointing
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Shiju Wang, Yujie Wang, Fangcheng Fu, Ao Sun, Yinxiao Feng, Zijian Zhu, Bin Cui, Xu Han, Kaisheng Ma
- 发布：2026-09-15；更新：2026-09-15
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/wsjdsg/InfiniPipe-code](https://github.com/wsjdsg/InfiniPipe-code)
- 阅读深度：metadata
