---
title: "Towards Fully-fledged GPU Multitasking via Proactive Memory Scheduling"
description: "Limited HBM capacity has become the primary bottleneck for hosting a growing number of increasingly larger-scale GPU tasks."
---

**评分：45/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2512.24637) · [PDF](https://arxiv.org/pdf/2512.24637)

## 一句话摘要

Limited HBM capacity has become the primary bottleneck for hosting a growing number of increasingly larger-scale GPU tasks.

## 为什么值得关注

待编辑增强。

## 摘要原文

Limited HBM capacity has become the primary bottleneck for hosting a growing number of increasingly larger-scale GPU tasks. While demand paging extends capacity via host DRAM, it can incur order-of-magnitude slowdowns due to the massive working sets of GPU workloads. However, we observe that GPU memory accesses are inherently predictable from kernel launch arguments, prior executions, and the asynchronous execution nature. Leveraging this opportunity, we propose MSched, an OS-level scheduler that extends GPU context switching to include proactive working set preparation. This approach coalesces fragmented, eventual, and expensive page faults into a single efficient migration. MSched combines parameterized templates with page fault feedback to accurately predict working sets, and co-designs the task scheduler and memory manager to resolve global access order and enforce near-optimal page replacement. Across scientific, deep learning, and LLM workloads, MSched outperforms demand paging by up to 186.69x and whole-process swapping by up to 8.63x. MSched is open-source and has been integrated into https://github.com/XpuOS/nvxsched.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 10 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu memory
- quantitative claim detected
- code/artifact link detected

## 元数据

- 作者：Weihang Shen, Yinqiu Chen, Rong Chen, Haibo Chen
- 发布：2026-11-09；更新：2026-11-09
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/XpuOS/nvxsched](https://github.com/XpuOS/nvxsched)
- 阅读深度：metadata
