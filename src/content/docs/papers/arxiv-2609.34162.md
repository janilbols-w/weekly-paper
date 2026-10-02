---
title: "SlideDP: Scaling Host-Resident LLM Fine-Tuning Across Multiple GPUs"
description: "Host-resident layer streaming enables full-parameter LLM fine-tuning beyond GPU memory, but data-parallel ranks compete for shared host resources."
---

**评分：41/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](http://arxiv.org/abs/2609.34162v1) · [PDF](https://arxiv.org/pdf/2609.34162v1)

## 一句话摘要

Host-resident layer streaming enables full-parameter LLM fine-tuning beyond GPU memory, but data-parallel ranks compete for shared host resources.

## 为什么值得关注

待编辑增强。

## 摘要原文

Host-resident layer streaming enables full-parameter LLM fine-tuning beyond GPU memory, but data-parallel ranks compete for shared host resources. Replicated transfers amplify traffic, while strong scaling can expose host work as computation windows shrink. We present SlideDP, a synchronous data-parallel runtime for shared-host multi-GPU systems. It maintains one authoritative host state, decouples communication routes from state layout, and pipelines parameter delivery, gradient aggregation, and CPU updates across ranks and chunks. An analytical step-time model characterizes resource bottlenecks and pipeline exposure; runtime measurements guide communication, chunking, and activation policies under a GPU memory budget. In matched-batch sweeps, SlideDP achieves geometric-mean throughput ratios of 1.46-2.64$\times$ over SlideFormer, MegaTrain, and ZeRO-Offload. On four H100s, SlideDP approaches GPU-resident FSDP2 throughput for Qwen3-14B at a smaller batch size. With a larger batch, it processes over 1M tokens per step and exceeds FSDP2's measured peak throughput by 11.2%. Separately, it supports 256K-token sequences for the same model and fine-tunes Qwen2.5-72B on four RTX 4090 GPUs. Project page: https://github.com/RegiaYoung/SlideDP.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 9 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu memory
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Ruijia Yang, Shiyuan Lin, Yulong Ao, Zhiyu Li, Yingli Zhao, Xianduo Li, Yonghua Lin, Zeyi Wen
- 发布：2026-09-28；更新：2026-09-28
- 来源：arXiv；Venue：未确认
- 代码：[https://github.com/RegiaYoung/SlideDP](https://github.com/RegiaYoung/SlideDP)
- 阅读深度：metadata
